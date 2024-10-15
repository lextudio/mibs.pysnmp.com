# SNMP MIB module (HPN-ICF-EPON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-EPON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:09 2024
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

(hpnicfLswFrameIndex,
 hpnicfLswSlotIndex) = mibBuilder.importSymbols(
    "HPN-ICF-LSW-DEV-ADM-MIB",
    "hpnicfLswFrameIndex",
    "hpnicfLswSlotIndex")

(hpnicfEpon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfEpon")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpnicfEponMibObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfEponSysMan_ObjectIdentity = ObjectIdentity
hpnicfEponSysMan = _HpnicfEponSysMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1)
)


class _HpnicfEponAutoAuthorize_Type(TruthValue):
    """Custom type hpnicfEponAutoAuthorize based on TruthValue"""


_HpnicfEponAutoAuthorize_Object = MibScalar
hpnicfEponAutoAuthorize = _HpnicfEponAutoAuthorize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 1),
    _HpnicfEponAutoAuthorize_Type()
)
hpnicfEponAutoAuthorize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponAutoAuthorize.setStatus("current")
_HpnicfEponMonitorCycle_Type = Integer32
_HpnicfEponMonitorCycle_Object = MibScalar
hpnicfEponMonitorCycle = _HpnicfEponMonitorCycle_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 2),
    _HpnicfEponMonitorCycle_Type()
)
hpnicfEponMonitorCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponMonitorCycle.setStatus("current")


class _HpnicfEponMsgTimeOut_Type(Integer32):
    """Custom type hpnicfEponMsgTimeOut based on Integer32"""
    defaultValue = 600


_HpnicfEponMsgTimeOut_Object = MibScalar
hpnicfEponMsgTimeOut = _HpnicfEponMsgTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 3),
    _HpnicfEponMsgTimeOut_Type()
)
hpnicfEponMsgTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponMsgTimeOut.setStatus("current")


class _HpnicfEponMsgLoseNum_Type(Integer32):
    """Custom type hpnicfEponMsgLoseNum based on Integer32"""
    defaultValue = 20


_HpnicfEponMsgLoseNum_Object = MibScalar
hpnicfEponMsgLoseNum = _HpnicfEponMsgLoseNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 4),
    _HpnicfEponMsgLoseNum_Type()
)
hpnicfEponMsgLoseNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponMsgLoseNum.setStatus("current")
_HpnicfEponSysHasEPONBoard_Type = TruthValue
_HpnicfEponSysHasEPONBoard_Object = MibScalar
hpnicfEponSysHasEPONBoard = _HpnicfEponSysHasEPONBoard_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 5),
    _HpnicfEponSysHasEPONBoard_Type()
)
hpnicfEponSysHasEPONBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponSysHasEPONBoard.setStatus("current")


class _HpnicfEponMonitorCycleEnable_Type(TruthValue):
    """Custom type hpnicfEponMonitorCycleEnable based on TruthValue"""


_HpnicfEponMonitorCycleEnable_Object = MibScalar
hpnicfEponMonitorCycleEnable = _HpnicfEponMonitorCycleEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 6),
    _HpnicfEponMonitorCycleEnable_Type()
)
hpnicfEponMonitorCycleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponMonitorCycleEnable.setStatus("current")


class _HpnicfEponOltSoftwareErrAlmEnable_Type(TruthValue):
    """Custom type hpnicfEponOltSoftwareErrAlmEnable based on TruthValue"""


_HpnicfEponOltSoftwareErrAlmEnable_Object = MibScalar
hpnicfEponOltSoftwareErrAlmEnable = _HpnicfEponOltSoftwareErrAlmEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 7),
    _HpnicfEponOltSoftwareErrAlmEnable_Type()
)
hpnicfEponOltSoftwareErrAlmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponOltSoftwareErrAlmEnable.setStatus("current")


class _HpnicfEponPortLoopBackAlmEnable_Type(TruthValue):
    """Custom type hpnicfEponPortLoopBackAlmEnable based on TruthValue"""


_HpnicfEponPortLoopBackAlmEnable_Object = MibScalar
hpnicfEponPortLoopBackAlmEnable = _HpnicfEponPortLoopBackAlmEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 8),
    _HpnicfEponPortLoopBackAlmEnable_Type()
)
hpnicfEponPortLoopBackAlmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponPortLoopBackAlmEnable.setStatus("current")
_HpnicfEponMonitorCycleMinVal_Type = Integer32
_HpnicfEponMonitorCycleMinVal_Object = MibScalar
hpnicfEponMonitorCycleMinVal = _HpnicfEponMonitorCycleMinVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 9),
    _HpnicfEponMonitorCycleMinVal_Type()
)
hpnicfEponMonitorCycleMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponMonitorCycleMinVal.setStatus("current")
_HpnicfEponMonitorCycleMaxVal_Type = Integer32
_HpnicfEponMonitorCycleMaxVal_Object = MibScalar
hpnicfEponMonitorCycleMaxVal = _HpnicfEponMonitorCycleMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 10),
    _HpnicfEponMonitorCycleMaxVal_Type()
)
hpnicfEponMonitorCycleMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponMonitorCycleMaxVal.setStatus("current")
_HpnicfEponMsgTimeOutMinVal_Type = Integer32
_HpnicfEponMsgTimeOutMinVal_Object = MibScalar
hpnicfEponMsgTimeOutMinVal = _HpnicfEponMsgTimeOutMinVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 11),
    _HpnicfEponMsgTimeOutMinVal_Type()
)
hpnicfEponMsgTimeOutMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponMsgTimeOutMinVal.setStatus("current")
_HpnicfEponMsgTimeOutMaxVal_Type = Integer32
_HpnicfEponMsgTimeOutMaxVal_Object = MibScalar
hpnicfEponMsgTimeOutMaxVal = _HpnicfEponMsgTimeOutMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 12),
    _HpnicfEponMsgTimeOutMaxVal_Type()
)
hpnicfEponMsgTimeOutMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponMsgTimeOutMaxVal.setStatus("current")
_HpnicfEponMsgLoseNumMinVal_Type = Integer32
_HpnicfEponMsgLoseNumMinVal_Object = MibScalar
hpnicfEponMsgLoseNumMinVal = _HpnicfEponMsgLoseNumMinVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 13),
    _HpnicfEponMsgLoseNumMinVal_Type()
)
hpnicfEponMsgLoseNumMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponMsgLoseNumMinVal.setStatus("current")
_HpnicfEponMsgLoseNumMaxVal_Type = Integer32
_HpnicfEponMsgLoseNumMaxVal_Object = MibScalar
hpnicfEponMsgLoseNumMaxVal = _HpnicfEponMsgLoseNumMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 14),
    _HpnicfEponMsgLoseNumMaxVal_Type()
)
hpnicfEponMsgLoseNumMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponMsgLoseNumMaxVal.setStatus("current")
_HpnicfEponSysScalarGroup_ObjectIdentity = ObjectIdentity
hpnicfEponSysScalarGroup = _HpnicfEponSysScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 15)
)
_HpnicfEponSysManTable_Object = MibTable
hpnicfEponSysManTable = _HpnicfEponSysManTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 16)
)
if mibBuilder.loadTexts:
    hpnicfEponSysManTable.setStatus("current")
_HpnicfEponSysManEntry_Object = MibTableRow
hpnicfEponSysManEntry = _HpnicfEponSysManEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 16, 1)
)
hpnicfEponSysManEntry.setIndexNames(
    (0, "HPN-ICF-EPON-MIB", "hpnicfEponSlotIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEponSysManEntry.setStatus("current")
_HpnicfEponSlotIndex_Type = Integer32
_HpnicfEponSlotIndex_Object = MibTableColumn
hpnicfEponSlotIndex = _HpnicfEponSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 16, 1, 1),
    _HpnicfEponSlotIndex_Type()
)
hpnicfEponSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEponSlotIndex.setStatus("current")


class _HpnicfEponModeSwitch_Type(Integer32):
    """Custom type hpnicfEponModeSwitch based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cmode", 1),
          ("hmode", 2))
    )


_HpnicfEponModeSwitch_Type.__name__ = "Integer32"
_HpnicfEponModeSwitch_Object = MibTableColumn
hpnicfEponModeSwitch = _HpnicfEponModeSwitch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 16, 1, 2),
    _HpnicfEponModeSwitch_Type()
)
hpnicfEponModeSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponModeSwitch.setStatus("current")


class _HpnicfEponAutomaticMode_Type(Integer32):
    """Custom type hpnicfEponAutomaticMode based on Integer32"""
    defaultValue = 1

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


_HpnicfEponAutomaticMode_Type.__name__ = "Integer32"
_HpnicfEponAutomaticMode_Object = MibTableColumn
hpnicfEponAutomaticMode = _HpnicfEponAutomaticMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 16, 1, 3),
    _HpnicfEponAutomaticMode_Type()
)
hpnicfEponAutomaticMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponAutomaticMode.setStatus("current")


class _HpnicfEponOamDiscoveryTimeout_Type(Integer32):
    """Custom type hpnicfEponOamDiscoveryTimeout based on Integer32"""
    defaultValue = 30


_HpnicfEponOamDiscoveryTimeout_Object = MibTableColumn
hpnicfEponOamDiscoveryTimeout = _HpnicfEponOamDiscoveryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 16, 1, 4),
    _HpnicfEponOamDiscoveryTimeout_Type()
)
hpnicfEponOamDiscoveryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponOamDiscoveryTimeout.setStatus("current")


class _HpnicfEponEncryptionNoReplyTimeOut_Type(Integer32):
    """Custom type hpnicfEponEncryptionNoReplyTimeOut based on Integer32"""
    defaultValue = 30


_HpnicfEponEncryptionNoReplyTimeOut_Object = MibTableColumn
hpnicfEponEncryptionNoReplyTimeOut = _HpnicfEponEncryptionNoReplyTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 16, 1, 5),
    _HpnicfEponEncryptionNoReplyTimeOut_Type()
)
hpnicfEponEncryptionNoReplyTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponEncryptionNoReplyTimeOut.setStatus("current")


class _HpnicfEponEncryptionUpdateTime_Type(Integer32):
    """Custom type hpnicfEponEncryptionUpdateTime based on Integer32"""
    defaultValue = 10


_HpnicfEponEncryptionUpdateTime_Object = MibTableColumn
hpnicfEponEncryptionUpdateTime = _HpnicfEponEncryptionUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 16, 1, 6),
    _HpnicfEponEncryptionUpdateTime_Type()
)
hpnicfEponEncryptionUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponEncryptionUpdateTime.setStatus("current")


class _HpnicfEponAutoBindStatus_Type(Integer32):
    """Custom type hpnicfEponAutoBindStatus based on Integer32"""
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


_HpnicfEponAutoBindStatus_Type.__name__ = "Integer32"
_HpnicfEponAutoBindStatus_Object = MibTableColumn
hpnicfEponAutoBindStatus = _HpnicfEponAutoBindStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 16, 1, 7),
    _HpnicfEponAutoBindStatus_Type()
)
hpnicfEponAutoBindStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponAutoBindStatus.setStatus("current")
_HpnicfEponAutoUpdateTable_Object = MibTable
hpnicfEponAutoUpdateTable = _HpnicfEponAutoUpdateTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 17)
)
if mibBuilder.loadTexts:
    hpnicfEponAutoUpdateTable.setStatus("current")
_HpnicfEponAutoUpdateEntry_Object = MibTableRow
hpnicfEponAutoUpdateEntry = _HpnicfEponAutoUpdateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 17, 1)
)
hpnicfEponAutoUpdateEntry.setIndexNames(
    (0, "HPN-ICF-EPON-MIB", "hpnicfEponSlotIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEponAutoUpdateEntry.setStatus("current")


class _HpnicfEponAutoUpdateFileName_Type(DisplayString):
    """Custom type hpnicfEponAutoUpdateFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfEponAutoUpdateFileName_Type.__name__ = "DisplayString"
_HpnicfEponAutoUpdateFileName_Object = MibTableColumn
hpnicfEponAutoUpdateFileName = _HpnicfEponAutoUpdateFileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 17, 1, 1),
    _HpnicfEponAutoUpdateFileName_Type()
)
hpnicfEponAutoUpdateFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponAutoUpdateFileName.setStatus("current")


class _HpnicfEponAutoUpdateSchedStatus_Type(Integer32):
    """Custom type hpnicfEponAutoUpdateSchedStatus based on Integer32"""
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


_HpnicfEponAutoUpdateSchedStatus_Type.__name__ = "Integer32"
_HpnicfEponAutoUpdateSchedStatus_Object = MibTableColumn
hpnicfEponAutoUpdateSchedStatus = _HpnicfEponAutoUpdateSchedStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 17, 1, 2),
    _HpnicfEponAutoUpdateSchedStatus_Type()
)
hpnicfEponAutoUpdateSchedStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponAutoUpdateSchedStatus.setStatus("current")


class _HpnicfEponAutoUpdateSchedTime_Type(OctetString):
    """Custom type hpnicfEponAutoUpdateSchedTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfEponAutoUpdateSchedTime_Type.__name__ = "OctetString"
_HpnicfEponAutoUpdateSchedTime_Object = MibTableColumn
hpnicfEponAutoUpdateSchedTime = _HpnicfEponAutoUpdateSchedTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 17, 1, 3),
    _HpnicfEponAutoUpdateSchedTime_Type()
)
hpnicfEponAutoUpdateSchedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponAutoUpdateSchedTime.setStatus("current")


class _HpnicfEponAutoUpdateSchedType_Type(Integer32):
    """Custom type hpnicfEponAutoUpdateSchedType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("comingdate", 3),
          ("daily", 1),
          ("weekly", 2))
    )


_HpnicfEponAutoUpdateSchedType_Type.__name__ = "Integer32"
_HpnicfEponAutoUpdateSchedType_Object = MibTableColumn
hpnicfEponAutoUpdateSchedType = _HpnicfEponAutoUpdateSchedType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 17, 1, 4),
    _HpnicfEponAutoUpdateSchedType_Type()
)
hpnicfEponAutoUpdateSchedType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponAutoUpdateSchedType.setStatus("current")


class _HpnicfEponAutoUpdateRealTimeStatus_Type(Integer32):
    """Custom type hpnicfEponAutoUpdateRealTimeStatus based on Integer32"""
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


_HpnicfEponAutoUpdateRealTimeStatus_Type.__name__ = "Integer32"
_HpnicfEponAutoUpdateRealTimeStatus_Object = MibTableColumn
hpnicfEponAutoUpdateRealTimeStatus = _HpnicfEponAutoUpdateRealTimeStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 17, 1, 5),
    _HpnicfEponAutoUpdateRealTimeStatus_Type()
)
hpnicfEponAutoUpdateRealTimeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponAutoUpdateRealTimeStatus.setStatus("current")
_HpnicfEponOuiIndexNextTable_Object = MibTable
hpnicfEponOuiIndexNextTable = _HpnicfEponOuiIndexNextTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 18)
)
if mibBuilder.loadTexts:
    hpnicfEponOuiIndexNextTable.setStatus("current")
_HpnicfEponOuiIndexNextEntry_Object = MibTableRow
hpnicfEponOuiIndexNextEntry = _HpnicfEponOuiIndexNextEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 18, 1)
)
hpnicfEponOuiIndexNextEntry.setIndexNames(
    (0, "HPN-ICF-EPON-MIB", "hpnicfEponSlotIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEponOuiIndexNextEntry.setStatus("current")
_HpnicfEponOuiIndexNext_Type = Integer32
_HpnicfEponOuiIndexNext_Object = MibTableColumn
hpnicfEponOuiIndexNext = _HpnicfEponOuiIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 18, 1, 1),
    _HpnicfEponOuiIndexNext_Type()
)
hpnicfEponOuiIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponOuiIndexNext.setStatus("current")
_HpnicfEponOuiTable_Object = MibTable
hpnicfEponOuiTable = _HpnicfEponOuiTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 19)
)
if mibBuilder.loadTexts:
    hpnicfEponOuiTable.setStatus("current")
_HpnicfEponOuiEntry_Object = MibTableRow
hpnicfEponOuiEntry = _HpnicfEponOuiEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 19, 1)
)
hpnicfEponOuiEntry.setIndexNames(
    (0, "HPN-ICF-EPON-MIB", "hpnicfEponSlotIndex"),
    (0, "HPN-ICF-EPON-MIB", "hpnicfEponOuiIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEponOuiEntry.setStatus("current")
_HpnicfEponOuiIndex_Type = Integer32
_HpnicfEponOuiIndex_Object = MibTableColumn
hpnicfEponOuiIndex = _HpnicfEponOuiIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 19, 1, 1),
    _HpnicfEponOuiIndex_Type()
)
hpnicfEponOuiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEponOuiIndex.setStatus("current")


class _HpnicfEponOuiValue_Type(OctetString):
    """Custom type hpnicfEponOuiValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_HpnicfEponOuiValue_Type.__name__ = "OctetString"
_HpnicfEponOuiValue_Object = MibTableColumn
hpnicfEponOuiValue = _HpnicfEponOuiValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 19, 1, 2),
    _HpnicfEponOuiValue_Type()
)
hpnicfEponOuiValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponOuiValue.setStatus("current")


class _HpnicfEponOamVersion_Type(OctetString):
    """Custom type hpnicfEponOamVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfEponOamVersion_Type.__name__ = "OctetString"
_HpnicfEponOamVersion_Object = MibTableColumn
hpnicfEponOamVersion = _HpnicfEponOamVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 19, 1, 3),
    _HpnicfEponOamVersion_Type()
)
hpnicfEponOamVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponOamVersion.setStatus("current")
_HpnicfEponOuiRowStatus_Type = RowStatus
_HpnicfEponOuiRowStatus_Object = MibTableColumn
hpnicfEponOuiRowStatus = _HpnicfEponOuiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 19, 1, 4),
    _HpnicfEponOuiRowStatus_Type()
)
hpnicfEponOuiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponOuiRowStatus.setStatus("current")
_HpnicfEponMulticastControlTable_Object = MibTable
hpnicfEponMulticastControlTable = _HpnicfEponMulticastControlTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 20)
)
if mibBuilder.loadTexts:
    hpnicfEponMulticastControlTable.setStatus("current")
_HpnicfEponMulticastControlEntry_Object = MibTableRow
hpnicfEponMulticastControlEntry = _HpnicfEponMulticastControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 20, 1)
)
hpnicfEponMulticastControlEntry.setIndexNames(
    (0, "HPN-ICF-EPON-MIB", "hpnicfEponMulticastVlanId"),
)
if mibBuilder.loadTexts:
    hpnicfEponMulticastControlEntry.setStatus("current")
_HpnicfEponMulticastVlanId_Type = Integer32
_HpnicfEponMulticastVlanId_Object = MibTableColumn
hpnicfEponMulticastVlanId = _HpnicfEponMulticastVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 20, 1, 1),
    _HpnicfEponMulticastVlanId_Type()
)
hpnicfEponMulticastVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEponMulticastVlanId.setStatus("current")


class _HpnicfEponMulticastAddressList_Type(OctetString):
    """Custom type hpnicfEponMulticastAddressList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfEponMulticastAddressList_Type.__name__ = "OctetString"
_HpnicfEponMulticastAddressList_Object = MibTableColumn
hpnicfEponMulticastAddressList = _HpnicfEponMulticastAddressList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 20, 1, 2),
    _HpnicfEponMulticastAddressList_Type()
)
hpnicfEponMulticastAddressList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponMulticastAddressList.setStatus("current")
_HpnicfEponMulticastStatus_Type = RowStatus
_HpnicfEponMulticastStatus_Object = MibTableColumn
hpnicfEponMulticastStatus = _HpnicfEponMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 1, 20, 1, 3),
    _HpnicfEponMulticastStatus_Type()
)
hpnicfEponMulticastStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponMulticastStatus.setStatus("current")
_HpnicfEponFileName_ObjectIdentity = ObjectIdentity
hpnicfEponFileName = _HpnicfEponFileName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 2)
)


class _HpnicfEponDbaUpdateFileName_Type(OctetString):
    """Custom type hpnicfEponDbaUpdateFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfEponDbaUpdateFileName_Type.__name__ = "OctetString"
_HpnicfEponDbaUpdateFileName_Object = MibScalar
hpnicfEponDbaUpdateFileName = _HpnicfEponDbaUpdateFileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 2, 1),
    _HpnicfEponDbaUpdateFileName_Type()
)
hpnicfEponDbaUpdateFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponDbaUpdateFileName.setStatus("current")


class _HpnicfEponOnuUpdateFileName_Type(OctetString):
    """Custom type hpnicfEponOnuUpdateFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfEponOnuUpdateFileName_Type.__name__ = "OctetString"
_HpnicfEponOnuUpdateFileName_Object = MibScalar
hpnicfEponOnuUpdateFileName = _HpnicfEponOnuUpdateFileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 2, 2),
    _HpnicfEponOnuUpdateFileName_Type()
)
hpnicfEponOnuUpdateFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponOnuUpdateFileName.setStatus("current")
_HpnicfEponOltMan_ObjectIdentity = ObjectIdentity
hpnicfEponOltMan = _HpnicfEponOltMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3)
)
_HpnicfOltSysManTable_Object = MibTable
hpnicfOltSysManTable = _HpnicfOltSysManTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpnicfOltSysManTable.setStatus("current")
_HpnicfOltSysManEntry_Object = MibTableRow
hpnicfOltSysManEntry = _HpnicfOltSysManEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 1, 1)
)
hpnicfOltSysManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfOltSysManEntry.setStatus("current")


class _HpnicfOltLaserOnTime_Type(Integer32):
    """Custom type hpnicfOltLaserOnTime based on Integer32"""
    defaultValue = 96


_HpnicfOltLaserOnTime_Object = MibTableColumn
hpnicfOltLaserOnTime = _HpnicfOltLaserOnTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 1, 1, 1),
    _HpnicfOltLaserOnTime_Type()
)
hpnicfOltLaserOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOltLaserOnTime.setStatus("current")


class _HpnicfOltLaserOffTime_Type(Integer32):
    """Custom type hpnicfOltLaserOffTime based on Integer32"""
    defaultValue = 96


_HpnicfOltLaserOffTime_Object = MibTableColumn
hpnicfOltLaserOffTime = _HpnicfOltLaserOffTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 1, 1, 2),
    _HpnicfOltLaserOffTime_Type()
)
hpnicfOltLaserOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOltLaserOffTime.setStatus("current")


class _HpnicfOltMultiCopyBrdCast_Type(TruthValue):
    """Custom type hpnicfOltMultiCopyBrdCast based on TruthValue"""


_HpnicfOltMultiCopyBrdCast_Object = MibTableColumn
hpnicfOltMultiCopyBrdCast = _HpnicfOltMultiCopyBrdCast_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 1, 1, 3),
    _HpnicfOltMultiCopyBrdCast_Type()
)
hpnicfOltMultiCopyBrdCast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOltMultiCopyBrdCast.setStatus("current")


class _HpnicfOltEnableDiscardPacket_Type(TruthValue):
    """Custom type hpnicfOltEnableDiscardPacket based on TruthValue"""


_HpnicfOltEnableDiscardPacket_Object = MibTableColumn
hpnicfOltEnableDiscardPacket = _HpnicfOltEnableDiscardPacket_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 1, 1, 4),
    _HpnicfOltEnableDiscardPacket_Type()
)
hpnicfOltEnableDiscardPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOltEnableDiscardPacket.setStatus("current")


class _HpnicfOltSelfTest_Type(Integer32):
    """Custom type hpnicfOltSelfTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("selftest", 1)
    )


_HpnicfOltSelfTest_Type.__name__ = "Integer32"
_HpnicfOltSelfTest_Object = MibTableColumn
hpnicfOltSelfTest = _HpnicfOltSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 1, 1, 5),
    _HpnicfOltSelfTest_Type()
)
hpnicfOltSelfTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOltSelfTest.setStatus("current")


class _HpnicfOltSelfTestResult_Type(Integer32):
    """Custom type hpnicfOltSelfTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 3),
          ("ok", 2),
          ("other", 1))
    )


_HpnicfOltSelfTestResult_Type.__name__ = "Integer32"
_HpnicfOltSelfTestResult_Object = MibTableColumn
hpnicfOltSelfTestResult = _HpnicfOltSelfTestResult_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 1, 1, 6),
    _HpnicfOltSelfTestResult_Type()
)
hpnicfOltSelfTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltSelfTestResult.setStatus("current")
_HpnicfOltMaxRtt_Type = Unsigned32
_HpnicfOltMaxRtt_Object = MibTableColumn
hpnicfOltMaxRtt = _HpnicfOltMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 1, 1, 7),
    _HpnicfOltMaxRtt_Type()
)
hpnicfOltMaxRtt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOltMaxRtt.setStatus("current")
_HpnicfOltInfoTable_Object = MibTable
hpnicfOltInfoTable = _HpnicfOltInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hpnicfOltInfoTable.setStatus("current")
_HpnicfOltInfoEntry_Object = MibTableRow
hpnicfOltInfoEntry = _HpnicfOltInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 2, 1)
)
hpnicfOltInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfOltInfoEntry.setStatus("current")
_HpnicfOltFirmMajorVersion_Type = OctetString
_HpnicfOltFirmMajorVersion_Object = MibTableColumn
hpnicfOltFirmMajorVersion = _HpnicfOltFirmMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 2, 1, 1),
    _HpnicfOltFirmMajorVersion_Type()
)
hpnicfOltFirmMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltFirmMajorVersion.setStatus("current")
_HpnicfOltFirmMinorVersion_Type = OctetString
_HpnicfOltFirmMinorVersion_Object = MibTableColumn
hpnicfOltFirmMinorVersion = _HpnicfOltFirmMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 2, 1, 2),
    _HpnicfOltFirmMinorVersion_Type()
)
hpnicfOltFirmMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltFirmMinorVersion.setStatus("current")
_HpnicfOltHardMajorVersion_Type = OctetString
_HpnicfOltHardMajorVersion_Object = MibTableColumn
hpnicfOltHardMajorVersion = _HpnicfOltHardMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 2, 1, 3),
    _HpnicfOltHardMajorVersion_Type()
)
hpnicfOltHardMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltHardMajorVersion.setStatus("current")
_HpnicfOltHardMinorVersion_Type = OctetString
_HpnicfOltHardMinorVersion_Object = MibTableColumn
hpnicfOltHardMinorVersion = _HpnicfOltHardMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 2, 1, 4),
    _HpnicfOltHardMinorVersion_Type()
)
hpnicfOltHardMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltHardMinorVersion.setStatus("current")
_HpnicfOltAgcLockTime_Type = Integer32
_HpnicfOltAgcLockTime_Object = MibTableColumn
hpnicfOltAgcLockTime = _HpnicfOltAgcLockTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 2, 1, 5),
    _HpnicfOltAgcLockTime_Type()
)
hpnicfOltAgcLockTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltAgcLockTime.setStatus("current")
_HpnicfOltAgcCdrTime_Type = Integer32
_HpnicfOltAgcCdrTime_Object = MibTableColumn
hpnicfOltAgcCdrTime = _HpnicfOltAgcCdrTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 2, 1, 6),
    _HpnicfOltAgcCdrTime_Type()
)
hpnicfOltAgcCdrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltAgcCdrTime.setStatus("current")
_HpnicfOltMacAddress_Type = MacAddress
_HpnicfOltMacAddress_Object = MibTableColumn
hpnicfOltMacAddress = _HpnicfOltMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 2, 1, 7),
    _HpnicfOltMacAddress_Type()
)
hpnicfOltMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltMacAddress.setStatus("current")


class _HpnicfOltWorkMode_Type(Integer32):
    """Custom type hpnicfOltWorkMode based on Integer32"""
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
        *(("closed", 4),
          ("open", 2),
          ("other", 1),
          ("reset", 3))
    )


_HpnicfOltWorkMode_Type.__name__ = "Integer32"
_HpnicfOltWorkMode_Object = MibTableColumn
hpnicfOltWorkMode = _HpnicfOltWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 2, 1, 8),
    _HpnicfOltWorkMode_Type()
)
hpnicfOltWorkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltWorkMode.setStatus("current")
_HpnicfOltOpticalPowerTx_Type = Integer32
_HpnicfOltOpticalPowerTx_Object = MibTableColumn
hpnicfOltOpticalPowerTx = _HpnicfOltOpticalPowerTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 2, 1, 9),
    _HpnicfOltOpticalPowerTx_Type()
)
hpnicfOltOpticalPowerTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltOpticalPowerTx.setStatus("current")
_HpnicfOltOpticalPowerRx_Type = Integer32
_HpnicfOltOpticalPowerRx_Object = MibTableColumn
hpnicfOltOpticalPowerRx = _HpnicfOltOpticalPowerRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 2, 1, 10),
    _HpnicfOltOpticalPowerRx_Type()
)
hpnicfOltOpticalPowerRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltOpticalPowerRx.setStatus("current")
_HpnicfOltDbaManTable_Object = MibTable
hpnicfOltDbaManTable = _HpnicfOltDbaManTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hpnicfOltDbaManTable.setStatus("current")
_HpnicfOltDbaManEntry_Object = MibTableRow
hpnicfOltDbaManEntry = _HpnicfOltDbaManEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 3, 1)
)
hpnicfOltDbaManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfOltDbaManEntry.setStatus("current")


class _HpnicfOltDbaEnabledType_Type(Integer32):
    """Custom type hpnicfOltDbaEnabledType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_HpnicfOltDbaEnabledType_Type.__name__ = "Integer32"
_HpnicfOltDbaEnabledType_Object = MibTableColumn
hpnicfOltDbaEnabledType = _HpnicfOltDbaEnabledType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 3, 1, 1),
    _HpnicfOltDbaEnabledType_Type()
)
hpnicfOltDbaEnabledType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOltDbaEnabledType.setStatus("current")


class _HpnicfOltDbaDiscoveryLength_Type(Integer32):
    """Custom type hpnicfOltDbaDiscoveryLength based on Integer32"""
    defaultValue = 41500


_HpnicfOltDbaDiscoveryLength_Object = MibTableColumn
hpnicfOltDbaDiscoveryLength = _HpnicfOltDbaDiscoveryLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 3, 1, 2),
    _HpnicfOltDbaDiscoveryLength_Type()
)
hpnicfOltDbaDiscoveryLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOltDbaDiscoveryLength.setStatus("current")


class _HpnicfOltDbaDiscovryFrequency_Type(Integer32):
    """Custom type hpnicfOltDbaDiscovryFrequency based on Integer32"""
    defaultValue = 50


_HpnicfOltDbaDiscovryFrequency_Object = MibTableColumn
hpnicfOltDbaDiscovryFrequency = _HpnicfOltDbaDiscovryFrequency_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 3, 1, 3),
    _HpnicfOltDbaDiscovryFrequency_Type()
)
hpnicfOltDbaDiscovryFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOltDbaDiscovryFrequency.setStatus("current")


class _HpnicfOltDbaCycleLength_Type(Integer32):
    """Custom type hpnicfOltDbaCycleLength based on Integer32"""
    defaultValue = 65535


_HpnicfOltDbaCycleLength_Object = MibTableColumn
hpnicfOltDbaCycleLength = _HpnicfOltDbaCycleLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 3, 1, 4),
    _HpnicfOltDbaCycleLength_Type()
)
hpnicfOltDbaCycleLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOltDbaCycleLength.setStatus("current")
_HpnicfOltDbaVersion_Type = OctetString
_HpnicfOltDbaVersion_Object = MibTableColumn
hpnicfOltDbaVersion = _HpnicfOltDbaVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 3, 1, 5),
    _HpnicfOltDbaVersion_Type()
)
hpnicfOltDbaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltDbaVersion.setStatus("current")


class _HpnicfOltDbaUpdate_Type(Integer32):
    """Custom type hpnicfOltDbaUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("update", 1)
    )


_HpnicfOltDbaUpdate_Type.__name__ = "Integer32"
_HpnicfOltDbaUpdate_Object = MibTableColumn
hpnicfOltDbaUpdate = _HpnicfOltDbaUpdate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 3, 1, 6),
    _HpnicfOltDbaUpdate_Type()
)
hpnicfOltDbaUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOltDbaUpdate.setStatus("current")


class _HpnicfOltDbaUpdateResult_Type(Integer32):
    """Custom type hpnicfOltDbaUpdateResult based on Integer32"""
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
        *(("fail", 3),
          ("fileNotExist", 4),
          ("notSetFilename", 5),
          ("ok", 2),
          ("other", 1))
    )


_HpnicfOltDbaUpdateResult_Type.__name__ = "Integer32"
_HpnicfOltDbaUpdateResult_Object = MibTableColumn
hpnicfOltDbaUpdateResult = _HpnicfOltDbaUpdateResult_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 3, 1, 7),
    _HpnicfOltDbaUpdateResult_Type()
)
hpnicfOltDbaUpdateResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltDbaUpdateResult.setStatus("current")
_HpnicfOltPortAlarmThresholdTable_Object = MibTable
hpnicfOltPortAlarmThresholdTable = _HpnicfOltPortAlarmThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 4)
)
if mibBuilder.loadTexts:
    hpnicfOltPortAlarmThresholdTable.setStatus("current")
_HpnicfOltPortAlarmThresholdEntry_Object = MibTableRow
hpnicfOltPortAlarmThresholdEntry = _HpnicfOltPortAlarmThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 4, 1)
)
hpnicfOltPortAlarmThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfOltPortAlarmThresholdEntry.setStatus("current")


class _HpnicfOltPortAlarmBerEnabled_Type(TruthValue):
    """Custom type hpnicfOltPortAlarmBerEnabled based on TruthValue"""


_HpnicfOltPortAlarmBerEnabled_Object = MibTableColumn
hpnicfOltPortAlarmBerEnabled = _HpnicfOltPortAlarmBerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 4, 1, 1),
    _HpnicfOltPortAlarmBerEnabled_Type()
)
hpnicfOltPortAlarmBerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOltPortAlarmBerEnabled.setStatus("current")


class _HpnicfOltPortAlarmBerDirect_Type(Integer32):
    """Custom type hpnicfOltPortAlarmBerDirect based on Integer32"""
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
        *(("berAll", 3),
          ("berDownlink", 2),
          ("berUplink", 1))
    )


_HpnicfOltPortAlarmBerDirect_Type.__name__ = "Integer32"
_HpnicfOltPortAlarmBerDirect_Object = MibTableColumn
hpnicfOltPortAlarmBerDirect = _HpnicfOltPortAlarmBerDirect_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 4, 1, 2),
    _HpnicfOltPortAlarmBerDirect_Type()
)
hpnicfOltPortAlarmBerDirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOltPortAlarmBerDirect.setStatus("current")


class _HpnicfOltPortAlarmBerThreshold_Type(Integer32):
    """Custom type hpnicfOltPortAlarmBerThreshold based on Integer32"""
    defaultValue = 10


_HpnicfOltPortAlarmBerThreshold_Object = MibTableColumn
hpnicfOltPortAlarmBerThreshold = _HpnicfOltPortAlarmBerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 4, 1, 3),
    _HpnicfOltPortAlarmBerThreshold_Type()
)
hpnicfOltPortAlarmBerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOltPortAlarmBerThreshold.setStatus("current")


class _HpnicfOltPortAlarmFerEnabled_Type(TruthValue):
    """Custom type hpnicfOltPortAlarmFerEnabled based on TruthValue"""


_HpnicfOltPortAlarmFerEnabled_Object = MibTableColumn
hpnicfOltPortAlarmFerEnabled = _HpnicfOltPortAlarmFerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 4, 1, 4),
    _HpnicfOltPortAlarmFerEnabled_Type()
)
hpnicfOltPortAlarmFerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOltPortAlarmFerEnabled.setStatus("current")


class _HpnicfOltPortAlarmFerDirect_Type(Integer32):
    """Custom type hpnicfOltPortAlarmFerDirect based on Integer32"""
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
        *(("ferAll", 3),
          ("ferDownlink", 2),
          ("ferUplink", 1))
    )


_HpnicfOltPortAlarmFerDirect_Type.__name__ = "Integer32"
_HpnicfOltPortAlarmFerDirect_Object = MibTableColumn
hpnicfOltPortAlarmFerDirect = _HpnicfOltPortAlarmFerDirect_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 4, 1, 5),
    _HpnicfOltPortAlarmFerDirect_Type()
)
hpnicfOltPortAlarmFerDirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOltPortAlarmFerDirect.setStatus("current")


class _HpnicfOltPortAlarmFerThreshold_Type(Integer32):
    """Custom type hpnicfOltPortAlarmFerThreshold based on Integer32"""
    defaultValue = 1


_HpnicfOltPortAlarmFerThreshold_Object = MibTableColumn
hpnicfOltPortAlarmFerThreshold = _HpnicfOltPortAlarmFerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 4, 1, 6),
    _HpnicfOltPortAlarmFerThreshold_Type()
)
hpnicfOltPortAlarmFerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOltPortAlarmFerThreshold.setStatus("current")


class _HpnicfOltPortAlarmLlidMismatchEnabled_Type(TruthValue):
    """Custom type hpnicfOltPortAlarmLlidMismatchEnabled based on TruthValue"""


_HpnicfOltPortAlarmLlidMismatchEnabled_Object = MibTableColumn
hpnicfOltPortAlarmLlidMismatchEnabled = _HpnicfOltPortAlarmLlidMismatchEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 4, 1, 7),
    _HpnicfOltPortAlarmLlidMismatchEnabled_Type()
)
hpnicfOltPortAlarmLlidMismatchEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOltPortAlarmLlidMismatchEnabled.setStatus("current")


class _HpnicfOltPortAlarmLlidMismatchThreshold_Type(Integer32):
    """Custom type hpnicfOltPortAlarmLlidMismatchThreshold based on Integer32"""
    defaultValue = 5000


_HpnicfOltPortAlarmLlidMismatchThreshold_Object = MibTableColumn
hpnicfOltPortAlarmLlidMismatchThreshold = _HpnicfOltPortAlarmLlidMismatchThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 4, 1, 8),
    _HpnicfOltPortAlarmLlidMismatchThreshold_Type()
)
hpnicfOltPortAlarmLlidMismatchThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOltPortAlarmLlidMismatchThreshold.setStatus("current")


class _HpnicfOltPortAlarmRemoteStableEnabled_Type(TruthValue):
    """Custom type hpnicfOltPortAlarmRemoteStableEnabled based on TruthValue"""


_HpnicfOltPortAlarmRemoteStableEnabled_Object = MibTableColumn
hpnicfOltPortAlarmRemoteStableEnabled = _HpnicfOltPortAlarmRemoteStableEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 4, 1, 9),
    _HpnicfOltPortAlarmRemoteStableEnabled_Type()
)
hpnicfOltPortAlarmRemoteStableEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOltPortAlarmRemoteStableEnabled.setStatus("current")


class _HpnicfOltPortAlarmLocalStableEnabled_Type(TruthValue):
    """Custom type hpnicfOltPortAlarmLocalStableEnabled based on TruthValue"""


_HpnicfOltPortAlarmLocalStableEnabled_Object = MibTableColumn
hpnicfOltPortAlarmLocalStableEnabled = _HpnicfOltPortAlarmLocalStableEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 4, 1, 10),
    _HpnicfOltPortAlarmLocalStableEnabled_Type()
)
hpnicfOltPortAlarmLocalStableEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOltPortAlarmLocalStableEnabled.setStatus("current")


class _HpnicfOltPortAlarmRegistrationEnabled_Type(TruthValue):
    """Custom type hpnicfOltPortAlarmRegistrationEnabled based on TruthValue"""


_HpnicfOltPortAlarmRegistrationEnabled_Object = MibTableColumn
hpnicfOltPortAlarmRegistrationEnabled = _HpnicfOltPortAlarmRegistrationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 4, 1, 11),
    _HpnicfOltPortAlarmRegistrationEnabled_Type()
)
hpnicfOltPortAlarmRegistrationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOltPortAlarmRegistrationEnabled.setStatus("current")


class _HpnicfOltPortAlarmOamDisconnectionEnabled_Type(TruthValue):
    """Custom type hpnicfOltPortAlarmOamDisconnectionEnabled based on TruthValue"""


_HpnicfOltPortAlarmOamDisconnectionEnabled_Object = MibTableColumn
hpnicfOltPortAlarmOamDisconnectionEnabled = _HpnicfOltPortAlarmOamDisconnectionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 4, 1, 12),
    _HpnicfOltPortAlarmOamDisconnectionEnabled_Type()
)
hpnicfOltPortAlarmOamDisconnectionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOltPortAlarmOamDisconnectionEnabled.setStatus("current")


class _HpnicfOltPortAlarmEncryptionKeyEnabled_Type(TruthValue):
    """Custom type hpnicfOltPortAlarmEncryptionKeyEnabled based on TruthValue"""


_HpnicfOltPortAlarmEncryptionKeyEnabled_Object = MibTableColumn
hpnicfOltPortAlarmEncryptionKeyEnabled = _HpnicfOltPortAlarmEncryptionKeyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 4, 1, 13),
    _HpnicfOltPortAlarmEncryptionKeyEnabled_Type()
)
hpnicfOltPortAlarmEncryptionKeyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOltPortAlarmEncryptionKeyEnabled.setStatus("current")


class _HpnicfOltPortAlarmVendorSpecificEnabled_Type(TruthValue):
    """Custom type hpnicfOltPortAlarmVendorSpecificEnabled based on TruthValue"""


_HpnicfOltPortAlarmVendorSpecificEnabled_Object = MibTableColumn
hpnicfOltPortAlarmVendorSpecificEnabled = _HpnicfOltPortAlarmVendorSpecificEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 4, 1, 14),
    _HpnicfOltPortAlarmVendorSpecificEnabled_Type()
)
hpnicfOltPortAlarmVendorSpecificEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOltPortAlarmVendorSpecificEnabled.setStatus("current")


class _HpnicfOltPortAlarmRegExcessEnabled_Type(TruthValue):
    """Custom type hpnicfOltPortAlarmRegExcessEnabled based on TruthValue"""


_HpnicfOltPortAlarmRegExcessEnabled_Object = MibTableColumn
hpnicfOltPortAlarmRegExcessEnabled = _HpnicfOltPortAlarmRegExcessEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 4, 1, 15),
    _HpnicfOltPortAlarmRegExcessEnabled_Type()
)
hpnicfOltPortAlarmRegExcessEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOltPortAlarmRegExcessEnabled.setStatus("current")


class _HpnicfOltPortAlarmDFEEnabled_Type(TruthValue):
    """Custom type hpnicfOltPortAlarmDFEEnabled based on TruthValue"""


_HpnicfOltPortAlarmDFEEnabled_Object = MibTableColumn
hpnicfOltPortAlarmDFEEnabled = _HpnicfOltPortAlarmDFEEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 4, 1, 16),
    _HpnicfOltPortAlarmDFEEnabled_Type()
)
hpnicfOltPortAlarmDFEEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOltPortAlarmDFEEnabled.setStatus("current")
_HpnicfOltLaserOnTimeMinVal_Type = Integer32
_HpnicfOltLaserOnTimeMinVal_Object = MibScalar
hpnicfOltLaserOnTimeMinVal = _HpnicfOltLaserOnTimeMinVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 5),
    _HpnicfOltLaserOnTimeMinVal_Type()
)
hpnicfOltLaserOnTimeMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltLaserOnTimeMinVal.setStatus("current")
_HpnicfOltLaserOnTimeMaxVal_Type = Integer32
_HpnicfOltLaserOnTimeMaxVal_Object = MibScalar
hpnicfOltLaserOnTimeMaxVal = _HpnicfOltLaserOnTimeMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 6),
    _HpnicfOltLaserOnTimeMaxVal_Type()
)
hpnicfOltLaserOnTimeMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltLaserOnTimeMaxVal.setStatus("current")
_HpnicfOltLaserOffTimeMinVal_Type = Integer32
_HpnicfOltLaserOffTimeMinVal_Object = MibScalar
hpnicfOltLaserOffTimeMinVal = _HpnicfOltLaserOffTimeMinVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 7),
    _HpnicfOltLaserOffTimeMinVal_Type()
)
hpnicfOltLaserOffTimeMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltLaserOffTimeMinVal.setStatus("current")
_HpnicfOltLaserOffTimeMaxVal_Type = Integer32
_HpnicfOltLaserOffTimeMaxVal_Object = MibScalar
hpnicfOltLaserOffTimeMaxVal = _HpnicfOltLaserOffTimeMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 8),
    _HpnicfOltLaserOffTimeMaxVal_Type()
)
hpnicfOltLaserOffTimeMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltLaserOffTimeMaxVal.setStatus("current")
_HpnicfOltDbaDiscoveryLengthMinVal_Type = Integer32
_HpnicfOltDbaDiscoveryLengthMinVal_Object = MibScalar
hpnicfOltDbaDiscoveryLengthMinVal = _HpnicfOltDbaDiscoveryLengthMinVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 9),
    _HpnicfOltDbaDiscoveryLengthMinVal_Type()
)
hpnicfOltDbaDiscoveryLengthMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltDbaDiscoveryLengthMinVal.setStatus("current")
_HpnicfOltDbaDiscoveryLengthMaxVal_Type = Integer32
_HpnicfOltDbaDiscoveryLengthMaxVal_Object = MibScalar
hpnicfOltDbaDiscoveryLengthMaxVal = _HpnicfOltDbaDiscoveryLengthMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 10),
    _HpnicfOltDbaDiscoveryLengthMaxVal_Type()
)
hpnicfOltDbaDiscoveryLengthMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltDbaDiscoveryLengthMaxVal.setStatus("current")
_HpnicfOltDbaDiscovryFrequencyMinVal_Type = Integer32
_HpnicfOltDbaDiscovryFrequencyMinVal_Object = MibScalar
hpnicfOltDbaDiscovryFrequencyMinVal = _HpnicfOltDbaDiscovryFrequencyMinVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 11),
    _HpnicfOltDbaDiscovryFrequencyMinVal_Type()
)
hpnicfOltDbaDiscovryFrequencyMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltDbaDiscovryFrequencyMinVal.setStatus("current")
_HpnicfOltDbaDiscovryFrequencyMaxVal_Type = Integer32
_HpnicfOltDbaDiscovryFrequencyMaxVal_Object = MibScalar
hpnicfOltDbaDiscovryFrequencyMaxVal = _HpnicfOltDbaDiscovryFrequencyMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 12),
    _HpnicfOltDbaDiscovryFrequencyMaxVal_Type()
)
hpnicfOltDbaDiscovryFrequencyMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltDbaDiscovryFrequencyMaxVal.setStatus("current")
_HpnicfOltDbaCycleLengthMinVal_Type = Integer32
_HpnicfOltDbaCycleLengthMinVal_Object = MibScalar
hpnicfOltDbaCycleLengthMinVal = _HpnicfOltDbaCycleLengthMinVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 13),
    _HpnicfOltDbaCycleLengthMinVal_Type()
)
hpnicfOltDbaCycleLengthMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltDbaCycleLengthMinVal.setStatus("current")
_HpnicfOltDbaCycleLengthMaxVal_Type = Integer32
_HpnicfOltDbaCycleLengthMaxVal_Object = MibScalar
hpnicfOltDbaCycleLengthMaxVal = _HpnicfOltDbaCycleLengthMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 14),
    _HpnicfOltDbaCycleLengthMaxVal_Type()
)
hpnicfOltDbaCycleLengthMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltDbaCycleLengthMaxVal.setStatus("current")
_HpnicfOltPortAlarmLlidMisMinVal_Type = Integer32
_HpnicfOltPortAlarmLlidMisMinVal_Object = MibScalar
hpnicfOltPortAlarmLlidMisMinVal = _HpnicfOltPortAlarmLlidMisMinVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 15),
    _HpnicfOltPortAlarmLlidMisMinVal_Type()
)
hpnicfOltPortAlarmLlidMisMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltPortAlarmLlidMisMinVal.setStatus("current")
_HpnicfOltPortAlarmLlidMisMaxVal_Type = Integer32
_HpnicfOltPortAlarmLlidMisMaxVal_Object = MibScalar
hpnicfOltPortAlarmLlidMisMaxVal = _HpnicfOltPortAlarmLlidMisMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 16),
    _HpnicfOltPortAlarmLlidMisMaxVal_Type()
)
hpnicfOltPortAlarmLlidMisMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltPortAlarmLlidMisMaxVal.setStatus("current")
_HpnicfOltPortAlarmBerMinVal_Type = Integer32
_HpnicfOltPortAlarmBerMinVal_Object = MibScalar
hpnicfOltPortAlarmBerMinVal = _HpnicfOltPortAlarmBerMinVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 17),
    _HpnicfOltPortAlarmBerMinVal_Type()
)
hpnicfOltPortAlarmBerMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltPortAlarmBerMinVal.setStatus("current")
_HpnicfOltPortAlarmBerMaxVal_Type = Integer32
_HpnicfOltPortAlarmBerMaxVal_Object = MibScalar
hpnicfOltPortAlarmBerMaxVal = _HpnicfOltPortAlarmBerMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 18),
    _HpnicfOltPortAlarmBerMaxVal_Type()
)
hpnicfOltPortAlarmBerMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltPortAlarmBerMaxVal.setStatus("current")
_HpnicfOltPortAlarmFerMinVal_Type = Integer32
_HpnicfOltPortAlarmFerMinVal_Object = MibScalar
hpnicfOltPortAlarmFerMinVal = _HpnicfOltPortAlarmFerMinVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 19),
    _HpnicfOltPortAlarmFerMinVal_Type()
)
hpnicfOltPortAlarmFerMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltPortAlarmFerMinVal.setStatus("current")
_HpnicfOltPortAlarmFerMaxVal_Type = Integer32
_HpnicfOltPortAlarmFerMaxVal_Object = MibScalar
hpnicfOltPortAlarmFerMaxVal = _HpnicfOltPortAlarmFerMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 20),
    _HpnicfOltPortAlarmFerMaxVal_Type()
)
hpnicfOltPortAlarmFerMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltPortAlarmFerMaxVal.setStatus("current")
_HpnicfOnuSilentTable_Object = MibTable
hpnicfOnuSilentTable = _HpnicfOnuSilentTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 21)
)
if mibBuilder.loadTexts:
    hpnicfOnuSilentTable.setStatus("current")
_HpnicfOnuSilentEntry_Object = MibTableRow
hpnicfOnuSilentEntry = _HpnicfOnuSilentEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 21, 1)
)
hpnicfOnuSilentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EPON-MIB", "hpnicfOnuSilentMacAddr"),
)
if mibBuilder.loadTexts:
    hpnicfOnuSilentEntry.setStatus("current")
_HpnicfOnuSilentMacAddr_Type = MacAddress
_HpnicfOnuSilentMacAddr_Object = MibTableColumn
hpnicfOnuSilentMacAddr = _HpnicfOnuSilentMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 21, 1, 1),
    _HpnicfOnuSilentMacAddr_Type()
)
hpnicfOnuSilentMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfOnuSilentMacAddr.setStatus("current")
_HpnicfOnuSilentTime_Type = Integer32
_HpnicfOnuSilentTime_Object = MibTableColumn
hpnicfOnuSilentTime = _HpnicfOnuSilentTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 21, 1, 2),
    _HpnicfOnuSilentTime_Type()
)
hpnicfOnuSilentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuSilentTime.setStatus("current")
_HpnicfOltUsingOnuTable_Object = MibTable
hpnicfOltUsingOnuTable = _HpnicfOltUsingOnuTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 22)
)
if mibBuilder.loadTexts:
    hpnicfOltUsingOnuTable.setStatus("current")
_HpnicfOltUsingOnuEntry_Object = MibTableRow
hpnicfOltUsingOnuEntry = _HpnicfOltUsingOnuEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 22, 1)
)
hpnicfOltUsingOnuEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EPON-MIB", "hpnicfOltUsingOnuNum"),
)
if mibBuilder.loadTexts:
    hpnicfOltUsingOnuEntry.setStatus("current")


class _HpnicfOltUsingOnuNum_Type(Integer32):
    """Custom type hpnicfOltUsingOnuNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HpnicfOltUsingOnuNum_Type.__name__ = "Integer32"
_HpnicfOltUsingOnuNum_Object = MibTableColumn
hpnicfOltUsingOnuNum = _HpnicfOltUsingOnuNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 22, 1, 1),
    _HpnicfOltUsingOnuNum_Type()
)
hpnicfOltUsingOnuNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfOltUsingOnuNum.setStatus("current")
_HpnicfOltUsingOnuIfIndex_Type = Integer32
_HpnicfOltUsingOnuIfIndex_Object = MibTableColumn
hpnicfOltUsingOnuIfIndex = _HpnicfOltUsingOnuIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 22, 1, 2),
    _HpnicfOltUsingOnuIfIndex_Type()
)
hpnicfOltUsingOnuIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOltUsingOnuIfIndex.setStatus("current")
_HpnicfOltUsingOnuRowStatus_Type = RowStatus
_HpnicfOltUsingOnuRowStatus_Object = MibTableColumn
hpnicfOltUsingOnuRowStatus = _HpnicfOltUsingOnuRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 3, 22, 1, 3),
    _HpnicfOltUsingOnuRowStatus_Type()
)
hpnicfOltUsingOnuRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfOltUsingOnuRowStatus.setStatus("current")
_HpnicfEponOnuMan_ObjectIdentity = ObjectIdentity
hpnicfEponOnuMan = _HpnicfEponOnuMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5)
)
_HpnicfOnuSysManTable_Object = MibTable
hpnicfOnuSysManTable = _HpnicfOnuSysManTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hpnicfOnuSysManTable.setStatus("current")
_HpnicfOnuSysManEntry_Object = MibTableRow
hpnicfOnuSysManEntry = _HpnicfOnuSysManEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 1, 1)
)
hpnicfOnuSysManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfOnuSysManEntry.setStatus("current")


class _HpnicfOnuEncryptMan_Type(Integer32):
    """Custom type hpnicfOnuEncryptMan based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("downlink", 2),
          ("off", 1),
          ("updownlink", 3))
    )


_HpnicfOnuEncryptMan_Type.__name__ = "Integer32"
_HpnicfOnuEncryptMan_Object = MibTableColumn
hpnicfOnuEncryptMan = _HpnicfOnuEncryptMan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 1, 1, 1),
    _HpnicfOnuEncryptMan_Type()
)
hpnicfOnuEncryptMan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuEncryptMan.setStatus("current")


class _HpnicfOnuReAuthorize_Type(Integer32):
    """Custom type hpnicfOnuReAuthorize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reAuthorize", 1)
    )


_HpnicfOnuReAuthorize_Type.__name__ = "Integer32"
_HpnicfOnuReAuthorize_Object = MibTableColumn
hpnicfOnuReAuthorize = _HpnicfOnuReAuthorize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 1, 1, 2),
    _HpnicfOnuReAuthorize_Type()
)
hpnicfOnuReAuthorize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuReAuthorize.setStatus("current")


class _HpnicfOnuMulticastFilterStatus_Type(TruthValue):
    """Custom type hpnicfOnuMulticastFilterStatus based on TruthValue"""


_HpnicfOnuMulticastFilterStatus_Object = MibTableColumn
hpnicfOnuMulticastFilterStatus = _HpnicfOnuMulticastFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 1, 1, 3),
    _HpnicfOnuMulticastFilterStatus_Type()
)
hpnicfOnuMulticastFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuMulticastFilterStatus.setStatus("current")


class _HpnicfOnuDbaReportQueueSetNumber_Type(Integer32):
    """Custom type hpnicfOnuDbaReportQueueSetNumber based on Integer32"""
    defaultValue = 2


_HpnicfOnuDbaReportQueueSetNumber_Object = MibTableColumn
hpnicfOnuDbaReportQueueSetNumber = _HpnicfOnuDbaReportQueueSetNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 1, 1, 4),
    _HpnicfOnuDbaReportQueueSetNumber_Type()
)
hpnicfOnuDbaReportQueueSetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuDbaReportQueueSetNumber.setStatus("current")


class _HpnicfOnuRemoteFecStatus_Type(Integer32):
    """Custom type hpnicfOnuRemoteFecStatus based on Integer32"""
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


_HpnicfOnuRemoteFecStatus_Type.__name__ = "Integer32"
_HpnicfOnuRemoteFecStatus_Object = MibTableColumn
hpnicfOnuRemoteFecStatus = _HpnicfOnuRemoteFecStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 1, 1, 5),
    _HpnicfOnuRemoteFecStatus_Type()
)
hpnicfOnuRemoteFecStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuRemoteFecStatus.setStatus("current")


class _HpnicfOnuPortBerStatus_Type(Integer32):
    """Custom type hpnicfOnuPortBerStatus based on Integer32"""
    defaultValue = 1

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


_HpnicfOnuPortBerStatus_Type.__name__ = "Integer32"
_HpnicfOnuPortBerStatus_Object = MibTableColumn
hpnicfOnuPortBerStatus = _HpnicfOnuPortBerStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 1, 1, 6),
    _HpnicfOnuPortBerStatus_Type()
)
hpnicfOnuPortBerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuPortBerStatus.setStatus("current")


class _HpnicfOnuReset_Type(Integer32):
    """Custom type hpnicfOnuReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HpnicfOnuReset_Type.__name__ = "Integer32"
_HpnicfOnuReset_Object = MibTableColumn
hpnicfOnuReset = _HpnicfOnuReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 1, 1, 7),
    _HpnicfOnuReset_Type()
)
hpnicfOnuReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuReset.setStatus("current")


class _HpnicfOnuMulticastControlMode_Type(Integer32):
    """Custom type hpnicfOnuMulticastControlMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("igmpsnooping", 1),
          ("multicastcontrol", 2))
    )


_HpnicfOnuMulticastControlMode_Type.__name__ = "Integer32"
_HpnicfOnuMulticastControlMode_Object = MibTableColumn
hpnicfOnuMulticastControlMode = _HpnicfOnuMulticastControlMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 1, 1, 8),
    _HpnicfOnuMulticastControlMode_Type()
)
hpnicfOnuMulticastControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuMulticastControlMode.setStatus("current")
_HpnicfOnuAccessVlan_Type = Integer32
_HpnicfOnuAccessVlan_Object = MibTableColumn
hpnicfOnuAccessVlan = _HpnicfOnuAccessVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 1, 1, 9),
    _HpnicfOnuAccessVlan_Type()
)
hpnicfOnuAccessVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuAccessVlan.setStatus("current")


class _HpnicfOnuEncryptKey_Type(DisplayString):
    """Custom type hpnicfOnuEncryptKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfOnuEncryptKey_Type.__name__ = "DisplayString"
_HpnicfOnuEncryptKey_Object = MibTableColumn
hpnicfOnuEncryptKey = _HpnicfOnuEncryptKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 1, 1, 10),
    _HpnicfOnuEncryptKey_Type()
)
hpnicfOnuEncryptKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuEncryptKey.setStatus("current")


class _HpnicfOnuUniUpDownTrapStatus_Type(TruthValue):
    """Custom type hpnicfOnuUniUpDownTrapStatus based on TruthValue"""


_HpnicfOnuUniUpDownTrapStatus_Object = MibTableColumn
hpnicfOnuUniUpDownTrapStatus = _HpnicfOnuUniUpDownTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 1, 1, 11),
    _HpnicfOnuUniUpDownTrapStatus_Type()
)
hpnicfOnuUniUpDownTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuUniUpDownTrapStatus.setStatus("current")


class _HpnicfOnuFecStatus_Type(Integer32):
    """Custom type hpnicfOnuFecStatus based on Integer32"""
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


_HpnicfOnuFecStatus_Type.__name__ = "Integer32"
_HpnicfOnuFecStatus_Object = MibTableColumn
hpnicfOnuFecStatus = _HpnicfOnuFecStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 1, 1, 12),
    _HpnicfOnuFecStatus_Type()
)
hpnicfOnuFecStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuFecStatus.setStatus("current")
_HpnicfOnuMcastCtrlHostAgingTime_Type = Integer32
_HpnicfOnuMcastCtrlHostAgingTime_Object = MibTableColumn
hpnicfOnuMcastCtrlHostAgingTime = _HpnicfOnuMcastCtrlHostAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 1, 1, 13),
    _HpnicfOnuMcastCtrlHostAgingTime_Type()
)
hpnicfOnuMcastCtrlHostAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuMcastCtrlHostAgingTime.setStatus("current")
_HpnicfOnuMulticastFastLeaveEnable_Type = TruthValue
_HpnicfOnuMulticastFastLeaveEnable_Object = MibTableColumn
hpnicfOnuMulticastFastLeaveEnable = _HpnicfOnuMulticastFastLeaveEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 1, 1, 14),
    _HpnicfOnuMulticastFastLeaveEnable_Type()
)
hpnicfOnuMulticastFastLeaveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuMulticastFastLeaveEnable.setStatus("current")
_HpnicfOnuPortIsolateEnable_Type = TruthValue
_HpnicfOnuPortIsolateEnable_Object = MibTableColumn
hpnicfOnuPortIsolateEnable = _HpnicfOnuPortIsolateEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 1, 1, 15),
    _HpnicfOnuPortIsolateEnable_Type()
)
hpnicfOnuPortIsolateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuPortIsolateEnable.setStatus("current")
_HpnicfOnuLinkTestTable_Object = MibTable
hpnicfOnuLinkTestTable = _HpnicfOnuLinkTestTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 2)
)
if mibBuilder.loadTexts:
    hpnicfOnuLinkTestTable.setStatus("current")
_HpnicfOnuLinkTestEntry_Object = MibTableRow
hpnicfOnuLinkTestEntry = _HpnicfOnuLinkTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 2, 1)
)
hpnicfOnuLinkTestEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfOnuLinkTestEntry.setStatus("current")


class _HpnicfOnuLinkTestFrameNum_Type(Integer32):
    """Custom type hpnicfOnuLinkTestFrameNum based on Integer32"""
    defaultValue = 20


_HpnicfOnuLinkTestFrameNum_Object = MibTableColumn
hpnicfOnuLinkTestFrameNum = _HpnicfOnuLinkTestFrameNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 2, 1, 1),
    _HpnicfOnuLinkTestFrameNum_Type()
)
hpnicfOnuLinkTestFrameNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuLinkTestFrameNum.setStatus("current")


class _HpnicfOnuLinkTestFrameSize_Type(Integer32):
    """Custom type hpnicfOnuLinkTestFrameSize based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1514),
    )


_HpnicfOnuLinkTestFrameSize_Type.__name__ = "Integer32"
_HpnicfOnuLinkTestFrameSize_Object = MibTableColumn
hpnicfOnuLinkTestFrameSize = _HpnicfOnuLinkTestFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 2, 1, 2),
    _HpnicfOnuLinkTestFrameSize_Type()
)
hpnicfOnuLinkTestFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuLinkTestFrameSize.setStatus("current")


class _HpnicfOnuLinkTestDelay_Type(TruthValue):
    """Custom type hpnicfOnuLinkTestDelay based on TruthValue"""


_HpnicfOnuLinkTestDelay_Object = MibTableColumn
hpnicfOnuLinkTestDelay = _HpnicfOnuLinkTestDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 2, 1, 3),
    _HpnicfOnuLinkTestDelay_Type()
)
hpnicfOnuLinkTestDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuLinkTestDelay.setStatus("current")


class _HpnicfOnuLinkTestVlanTag_Type(TruthValue):
    """Custom type hpnicfOnuLinkTestVlanTag based on TruthValue"""


_HpnicfOnuLinkTestVlanTag_Object = MibTableColumn
hpnicfOnuLinkTestVlanTag = _HpnicfOnuLinkTestVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 2, 1, 4),
    _HpnicfOnuLinkTestVlanTag_Type()
)
hpnicfOnuLinkTestVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuLinkTestVlanTag.setStatus("current")


class _HpnicfOnuLinkTestVlanPriority_Type(Integer32):
    """Custom type hpnicfOnuLinkTestVlanPriority based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfOnuLinkTestVlanPriority_Type.__name__ = "Integer32"
_HpnicfOnuLinkTestVlanPriority_Object = MibTableColumn
hpnicfOnuLinkTestVlanPriority = _HpnicfOnuLinkTestVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 2, 1, 5),
    _HpnicfOnuLinkTestVlanPriority_Type()
)
hpnicfOnuLinkTestVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuLinkTestVlanPriority.setStatus("current")


class _HpnicfOnuLinkTestVlanTagID_Type(Integer32):
    """Custom type hpnicfOnuLinkTestVlanTagID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpnicfOnuLinkTestVlanTagID_Type.__name__ = "Integer32"
_HpnicfOnuLinkTestVlanTagID_Object = MibTableColumn
hpnicfOnuLinkTestVlanTagID = _HpnicfOnuLinkTestVlanTagID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 2, 1, 6),
    _HpnicfOnuLinkTestVlanTagID_Type()
)
hpnicfOnuLinkTestVlanTagID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuLinkTestVlanTagID.setStatus("current")
_HpnicfOnuLinkTestResultSentFrameNum_Type = Integer32
_HpnicfOnuLinkTestResultSentFrameNum_Object = MibTableColumn
hpnicfOnuLinkTestResultSentFrameNum = _HpnicfOnuLinkTestResultSentFrameNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 2, 1, 7),
    _HpnicfOnuLinkTestResultSentFrameNum_Type()
)
hpnicfOnuLinkTestResultSentFrameNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuLinkTestResultSentFrameNum.setStatus("current")
_HpnicfOnuLinkTestResultRetFrameNum_Type = Integer32
_HpnicfOnuLinkTestResultRetFrameNum_Object = MibTableColumn
hpnicfOnuLinkTestResultRetFrameNum = _HpnicfOnuLinkTestResultRetFrameNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 2, 1, 8),
    _HpnicfOnuLinkTestResultRetFrameNum_Type()
)
hpnicfOnuLinkTestResultRetFrameNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuLinkTestResultRetFrameNum.setStatus("current")
_HpnicfOnuLinkTestResultRetErrFrameNum_Type = Integer32
_HpnicfOnuLinkTestResultRetErrFrameNum_Object = MibTableColumn
hpnicfOnuLinkTestResultRetErrFrameNum = _HpnicfOnuLinkTestResultRetErrFrameNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 2, 1, 9),
    _HpnicfOnuLinkTestResultRetErrFrameNum_Type()
)
hpnicfOnuLinkTestResultRetErrFrameNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuLinkTestResultRetErrFrameNum.setStatus("current")
_HpnicfOnuLinkTestResultMinDelay_Type = Integer32
_HpnicfOnuLinkTestResultMinDelay_Object = MibTableColumn
hpnicfOnuLinkTestResultMinDelay = _HpnicfOnuLinkTestResultMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 2, 1, 10),
    _HpnicfOnuLinkTestResultMinDelay_Type()
)
hpnicfOnuLinkTestResultMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuLinkTestResultMinDelay.setStatus("current")
_HpnicfOnuLinkTestResultMeanDelay_Type = Integer32
_HpnicfOnuLinkTestResultMeanDelay_Object = MibTableColumn
hpnicfOnuLinkTestResultMeanDelay = _HpnicfOnuLinkTestResultMeanDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 2, 1, 11),
    _HpnicfOnuLinkTestResultMeanDelay_Type()
)
hpnicfOnuLinkTestResultMeanDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuLinkTestResultMeanDelay.setStatus("current")
_HpnicfOnuLinkTestResultMaxDelay_Type = Integer32
_HpnicfOnuLinkTestResultMaxDelay_Object = MibTableColumn
hpnicfOnuLinkTestResultMaxDelay = _HpnicfOnuLinkTestResultMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 2, 1, 12),
    _HpnicfOnuLinkTestResultMaxDelay_Type()
)
hpnicfOnuLinkTestResultMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuLinkTestResultMaxDelay.setStatus("current")
_HpnicfOnuBandWidthTable_Object = MibTable
hpnicfOnuBandWidthTable = _HpnicfOnuBandWidthTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 3)
)
if mibBuilder.loadTexts:
    hpnicfOnuBandWidthTable.setStatus("current")
_HpnicfOnuBandWidthEntry_Object = MibTableRow
hpnicfOnuBandWidthEntry = _HpnicfOnuBandWidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 3, 1)
)
hpnicfOnuBandWidthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfOnuBandWidthEntry.setStatus("current")


class _HpnicfOnuDownStreamBandWidthPolicy_Type(TruthValue):
    """Custom type hpnicfOnuDownStreamBandWidthPolicy based on TruthValue"""


_HpnicfOnuDownStreamBandWidthPolicy_Object = MibTableColumn
hpnicfOnuDownStreamBandWidthPolicy = _HpnicfOnuDownStreamBandWidthPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 3, 1, 1),
    _HpnicfOnuDownStreamBandWidthPolicy_Type()
)
hpnicfOnuDownStreamBandWidthPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuDownStreamBandWidthPolicy.setStatus("current")


class _HpnicfOnuDownStreamMaxBandWidth_Type(Integer32):
    """Custom type hpnicfOnuDownStreamMaxBandWidth based on Integer32"""
    defaultValue = 1000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_HpnicfOnuDownStreamMaxBandWidth_Type.__name__ = "Integer32"
_HpnicfOnuDownStreamMaxBandWidth_Object = MibTableColumn
hpnicfOnuDownStreamMaxBandWidth = _HpnicfOnuDownStreamMaxBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 3, 1, 2),
    _HpnicfOnuDownStreamMaxBandWidth_Type()
)
hpnicfOnuDownStreamMaxBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuDownStreamMaxBandWidth.setStatus("current")


class _HpnicfOnuDownStreamMaxBurstSize_Type(Integer32):
    """Custom type hpnicfOnuDownStreamMaxBurstSize based on Integer32"""
    defaultValue = 8388480

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8388480),
    )


_HpnicfOnuDownStreamMaxBurstSize_Type.__name__ = "Integer32"
_HpnicfOnuDownStreamMaxBurstSize_Object = MibTableColumn
hpnicfOnuDownStreamMaxBurstSize = _HpnicfOnuDownStreamMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 3, 1, 3),
    _HpnicfOnuDownStreamMaxBurstSize_Type()
)
hpnicfOnuDownStreamMaxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuDownStreamMaxBurstSize.setStatus("current")


class _HpnicfOnuDownStreamHighPriorityFirst_Type(TruthValue):
    """Custom type hpnicfOnuDownStreamHighPriorityFirst based on TruthValue"""


_HpnicfOnuDownStreamHighPriorityFirst_Object = MibTableColumn
hpnicfOnuDownStreamHighPriorityFirst = _HpnicfOnuDownStreamHighPriorityFirst_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 3, 1, 4),
    _HpnicfOnuDownStreamHighPriorityFirst_Type()
)
hpnicfOnuDownStreamHighPriorityFirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuDownStreamHighPriorityFirst.setStatus("current")


class _HpnicfOnuDownStreamShortFrameFirst_Type(TruthValue):
    """Custom type hpnicfOnuDownStreamShortFrameFirst based on TruthValue"""


_HpnicfOnuDownStreamShortFrameFirst_Object = MibTableColumn
hpnicfOnuDownStreamShortFrameFirst = _HpnicfOnuDownStreamShortFrameFirst_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 3, 1, 5),
    _HpnicfOnuDownStreamShortFrameFirst_Type()
)
hpnicfOnuDownStreamShortFrameFirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuDownStreamShortFrameFirst.setStatus("current")


class _HpnicfOnuP2PBandWidthPolicy_Type(TruthValue):
    """Custom type hpnicfOnuP2PBandWidthPolicy based on TruthValue"""


_HpnicfOnuP2PBandWidthPolicy_Object = MibTableColumn
hpnicfOnuP2PBandWidthPolicy = _HpnicfOnuP2PBandWidthPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 3, 1, 6),
    _HpnicfOnuP2PBandWidthPolicy_Type()
)
hpnicfOnuP2PBandWidthPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuP2PBandWidthPolicy.setStatus("current")


class _HpnicfOnuP2PMaxBandWidth_Type(Integer32):
    """Custom type hpnicfOnuP2PMaxBandWidth based on Integer32"""
    defaultValue = 1000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_HpnicfOnuP2PMaxBandWidth_Type.__name__ = "Integer32"
_HpnicfOnuP2PMaxBandWidth_Object = MibTableColumn
hpnicfOnuP2PMaxBandWidth = _HpnicfOnuP2PMaxBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 3, 1, 7),
    _HpnicfOnuP2PMaxBandWidth_Type()
)
hpnicfOnuP2PMaxBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuP2PMaxBandWidth.setStatus("current")


class _HpnicfOnuP2PMaxBurstSize_Type(Integer32):
    """Custom type hpnicfOnuP2PMaxBurstSize based on Integer32"""
    defaultValue = 8388480

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8388480),
    )


_HpnicfOnuP2PMaxBurstSize_Type.__name__ = "Integer32"
_HpnicfOnuP2PMaxBurstSize_Object = MibTableColumn
hpnicfOnuP2PMaxBurstSize = _HpnicfOnuP2PMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 3, 1, 8),
    _HpnicfOnuP2PMaxBurstSize_Type()
)
hpnicfOnuP2PMaxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuP2PMaxBurstSize.setStatus("current")


class _HpnicfOnuP2PHighPriorityFirst_Type(TruthValue):
    """Custom type hpnicfOnuP2PHighPriorityFirst based on TruthValue"""


_HpnicfOnuP2PHighPriorityFirst_Object = MibTableColumn
hpnicfOnuP2PHighPriorityFirst = _HpnicfOnuP2PHighPriorityFirst_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 3, 1, 9),
    _HpnicfOnuP2PHighPriorityFirst_Type()
)
hpnicfOnuP2PHighPriorityFirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuP2PHighPriorityFirst.setStatus("current")


class _HpnicfOnuP2PShortFrameFirst_Type(TruthValue):
    """Custom type hpnicfOnuP2PShortFrameFirst based on TruthValue"""


_HpnicfOnuP2PShortFrameFirst_Object = MibTableColumn
hpnicfOnuP2PShortFrameFirst = _HpnicfOnuP2PShortFrameFirst_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 3, 1, 10),
    _HpnicfOnuP2PShortFrameFirst_Type()
)
hpnicfOnuP2PShortFrameFirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuP2PShortFrameFirst.setStatus("current")
_HpnicfOnuSlaManTable_Object = MibTable
hpnicfOnuSlaManTable = _HpnicfOnuSlaManTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 4)
)
if mibBuilder.loadTexts:
    hpnicfOnuSlaManTable.setStatus("current")
_HpnicfOnuSlaManEntry_Object = MibTableRow
hpnicfOnuSlaManEntry = _HpnicfOnuSlaManEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 4, 1)
)
hpnicfOnuSlaManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfOnuSlaManEntry.setStatus("current")
_HpnicfOnuSlaMaxBandWidth_Type = Integer32
_HpnicfOnuSlaMaxBandWidth_Object = MibTableColumn
hpnicfOnuSlaMaxBandWidth = _HpnicfOnuSlaMaxBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 4, 1, 1),
    _HpnicfOnuSlaMaxBandWidth_Type()
)
hpnicfOnuSlaMaxBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuSlaMaxBandWidth.setStatus("current")
_HpnicfOnuSlaMinBandWidth_Type = Integer32
_HpnicfOnuSlaMinBandWidth_Object = MibTableColumn
hpnicfOnuSlaMinBandWidth = _HpnicfOnuSlaMinBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 4, 1, 2),
    _HpnicfOnuSlaMinBandWidth_Type()
)
hpnicfOnuSlaMinBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuSlaMinBandWidth.setStatus("current")
_HpnicfOnuSlaBandWidthStepVal_Type = Integer32
_HpnicfOnuSlaBandWidthStepVal_Object = MibTableColumn
hpnicfOnuSlaBandWidthStepVal = _HpnicfOnuSlaBandWidthStepVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 4, 1, 3),
    _HpnicfOnuSlaBandWidthStepVal_Type()
)
hpnicfOnuSlaBandWidthStepVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuSlaBandWidthStepVal.setStatus("current")


class _HpnicfOnuSlaDelay_Type(Integer32):
    """Custom type hpnicfOnuSlaDelay based on Integer32"""
    defaultValue = 1

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


_HpnicfOnuSlaDelay_Type.__name__ = "Integer32"
_HpnicfOnuSlaDelay_Object = MibTableColumn
hpnicfOnuSlaDelay = _HpnicfOnuSlaDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 4, 1, 4),
    _HpnicfOnuSlaDelay_Type()
)
hpnicfOnuSlaDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuSlaDelay.setStatus("current")
_HpnicfOnuSlaFixedBandWidth_Type = Integer32
_HpnicfOnuSlaFixedBandWidth_Object = MibTableColumn
hpnicfOnuSlaFixedBandWidth = _HpnicfOnuSlaFixedBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 4, 1, 5),
    _HpnicfOnuSlaFixedBandWidth_Type()
)
hpnicfOnuSlaFixedBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuSlaFixedBandWidth.setStatus("current")


class _HpnicfOnuSlaPriorityClass_Type(Integer32):
    """Custom type hpnicfOnuSlaPriorityClass based on Integer32"""
    defaultValue = 0


_HpnicfOnuSlaPriorityClass_Object = MibTableColumn
hpnicfOnuSlaPriorityClass = _HpnicfOnuSlaPriorityClass_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 4, 1, 6),
    _HpnicfOnuSlaPriorityClass_Type()
)
hpnicfOnuSlaPriorityClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuSlaPriorityClass.setStatus("current")
_HpnicfOnuSlaFixedPacketSize_Type = Integer32
_HpnicfOnuSlaFixedPacketSize_Object = MibTableColumn
hpnicfOnuSlaFixedPacketSize = _HpnicfOnuSlaFixedPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 4, 1, 7),
    _HpnicfOnuSlaFixedPacketSize_Type()
)
hpnicfOnuSlaFixedPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuSlaFixedPacketSize.setStatus("current")
_HpnicfOnuInfoTable_Object = MibTable
hpnicfOnuInfoTable = _HpnicfOnuInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 5)
)
if mibBuilder.loadTexts:
    hpnicfOnuInfoTable.setStatus("current")
_HpnicfOnuInfoEntry_Object = MibTableRow
hpnicfOnuInfoEntry = _HpnicfOnuInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 5, 1)
)
hpnicfOnuInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfOnuInfoEntry.setStatus("current")
_HpnicfOnuHardMajorVersion_Type = OctetString
_HpnicfOnuHardMajorVersion_Object = MibTableColumn
hpnicfOnuHardMajorVersion = _HpnicfOnuHardMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 5, 1, 1),
    _HpnicfOnuHardMajorVersion_Type()
)
hpnicfOnuHardMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuHardMajorVersion.setStatus("current")
_HpnicfOnuHardMinorVersion_Type = OctetString
_HpnicfOnuHardMinorVersion_Object = MibTableColumn
hpnicfOnuHardMinorVersion = _HpnicfOnuHardMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 5, 1, 2),
    _HpnicfOnuHardMinorVersion_Type()
)
hpnicfOnuHardMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuHardMinorVersion.setStatus("current")
_HpnicfOnuSoftwareVersion_Type = OctetString
_HpnicfOnuSoftwareVersion_Object = MibTableColumn
hpnicfOnuSoftwareVersion = _HpnicfOnuSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 5, 1, 3),
    _HpnicfOnuSoftwareVersion_Type()
)
hpnicfOnuSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuSoftwareVersion.setStatus("current")


class _HpnicfOnuUniMacType_Type(Integer32):
    """Custom type hpnicfOnuUniMacType based on Integer32"""
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
        *(("gmii", 3),
          ("mii", 2),
          ("other", 1),
          ("tbi", 4))
    )


_HpnicfOnuUniMacType_Type.__name__ = "Integer32"
_HpnicfOnuUniMacType_Object = MibTableColumn
hpnicfOnuUniMacType = _HpnicfOnuUniMacType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 5, 1, 4),
    _HpnicfOnuUniMacType_Type()
)
hpnicfOnuUniMacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuUniMacType.setStatus("current")
_HpnicfOnuLaserOnTime_Type = Integer32
_HpnicfOnuLaserOnTime_Object = MibTableColumn
hpnicfOnuLaserOnTime = _HpnicfOnuLaserOnTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 5, 1, 5),
    _HpnicfOnuLaserOnTime_Type()
)
hpnicfOnuLaserOnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuLaserOnTime.setStatus("current")
_HpnicfOnuLaserOffTime_Type = Integer32
_HpnicfOnuLaserOffTime_Object = MibTableColumn
hpnicfOnuLaserOffTime = _HpnicfOnuLaserOffTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 5, 1, 6),
    _HpnicfOnuLaserOffTime_Type()
)
hpnicfOnuLaserOffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuLaserOffTime.setStatus("current")


class _HpnicfOnuGrantFifoDep_Type(Integer32):
    """Custom type hpnicfOnuGrantFifoDep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_HpnicfOnuGrantFifoDep_Type.__name__ = "Integer32"
_HpnicfOnuGrantFifoDep_Object = MibTableColumn
hpnicfOnuGrantFifoDep = _HpnicfOnuGrantFifoDep_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 5, 1, 7),
    _HpnicfOnuGrantFifoDep_Type()
)
hpnicfOnuGrantFifoDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuGrantFifoDep.setStatus("current")


class _HpnicfOnuWorkMode_Type(Integer32):
    """Custom type hpnicfOnuWorkMode based on Integer32"""
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
        *(("off", 4),
          ("on", 2),
          ("other", 1),
          ("pending", 3))
    )


_HpnicfOnuWorkMode_Type.__name__ = "Integer32"
_HpnicfOnuWorkMode_Object = MibTableColumn
hpnicfOnuWorkMode = _HpnicfOnuWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 5, 1, 8),
    _HpnicfOnuWorkMode_Type()
)
hpnicfOnuWorkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuWorkMode.setStatus("current")
_HpnicfOnuPCBVersion_Type = OctetString
_HpnicfOnuPCBVersion_Object = MibTableColumn
hpnicfOnuPCBVersion = _HpnicfOnuPCBVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 5, 1, 9),
    _HpnicfOnuPCBVersion_Type()
)
hpnicfOnuPCBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuPCBVersion.setStatus("current")
_HpnicfOnuRtt_Type = Unsigned32
_HpnicfOnuRtt_Object = MibTableColumn
hpnicfOnuRtt = _HpnicfOnuRtt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 5, 1, 10),
    _HpnicfOnuRtt_Type()
)
hpnicfOnuRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuRtt.setStatus("current")
_HpnicfOnuEEPROMVersion_Type = OctetString
_HpnicfOnuEEPROMVersion_Object = MibTableColumn
hpnicfOnuEEPROMVersion = _HpnicfOnuEEPROMVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 5, 1, 11),
    _HpnicfOnuEEPROMVersion_Type()
)
hpnicfOnuEEPROMVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuEEPROMVersion.setStatus("current")
_HpnicfOnuRegType_Type = OctetString
_HpnicfOnuRegType_Object = MibTableColumn
hpnicfOnuRegType = _HpnicfOnuRegType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 5, 1, 12),
    _HpnicfOnuRegType_Type()
)
hpnicfOnuRegType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuRegType.setStatus("current")
_HpnicfOnuHostType_Type = OctetString
_HpnicfOnuHostType_Object = MibTableColumn
hpnicfOnuHostType = _HpnicfOnuHostType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 5, 1, 13),
    _HpnicfOnuHostType_Type()
)
hpnicfOnuHostType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuHostType.setStatus("current")
_HpnicfOnuDistance_Type = Integer32
_HpnicfOnuDistance_Object = MibTableColumn
hpnicfOnuDistance = _HpnicfOnuDistance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 5, 1, 14),
    _HpnicfOnuDistance_Type()
)
hpnicfOnuDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuDistance.setStatus("current")
_HpnicfOnuLlid_Type = Integer32
_HpnicfOnuLlid_Object = MibTableColumn
hpnicfOnuLlid = _HpnicfOnuLlid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 5, 1, 15),
    _HpnicfOnuLlid_Type()
)
hpnicfOnuLlid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuLlid.setStatus("current")
_HpnicfOnuVendorId_Type = OctetString
_HpnicfOnuVendorId_Object = MibTableColumn
hpnicfOnuVendorId = _HpnicfOnuVendorId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 5, 1, 16),
    _HpnicfOnuVendorId_Type()
)
hpnicfOnuVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuVendorId.setStatus("current")
_HpnicfOnuFirmwareVersion_Type = OctetString
_HpnicfOnuFirmwareVersion_Object = MibTableColumn
hpnicfOnuFirmwareVersion = _HpnicfOnuFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 5, 1, 17),
    _HpnicfOnuFirmwareVersion_Type()
)
hpnicfOnuFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuFirmwareVersion.setStatus("current")
_HpnicfOnuOpticalPowerReceivedByOlt_Type = Integer32
_HpnicfOnuOpticalPowerReceivedByOlt_Object = MibTableColumn
hpnicfOnuOpticalPowerReceivedByOlt = _HpnicfOnuOpticalPowerReceivedByOlt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 5, 1, 18),
    _HpnicfOnuOpticalPowerReceivedByOlt_Type()
)
hpnicfOnuOpticalPowerReceivedByOlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuOpticalPowerReceivedByOlt.setStatus("current")
_HpnicfOnuMacAddrInfoTable_Object = MibTable
hpnicfOnuMacAddrInfoTable = _HpnicfOnuMacAddrInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 6)
)
if mibBuilder.loadTexts:
    hpnicfOnuMacAddrInfoTable.setStatus("current")
_HpnicfOnuMacAddrInfoEntry_Object = MibTableRow
hpnicfOnuMacAddrInfoEntry = _HpnicfOnuMacAddrInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 6, 1)
)
hpnicfOnuMacAddrInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EPON-MIB", "hpnicfOnuMacIndex"),
)
if mibBuilder.loadTexts:
    hpnicfOnuMacAddrInfoEntry.setStatus("current")
_HpnicfOnuMacIndex_Type = Integer32
_HpnicfOnuMacIndex_Object = MibTableColumn
hpnicfOnuMacIndex = _HpnicfOnuMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 6, 1, 1),
    _HpnicfOnuMacIndex_Type()
)
hpnicfOnuMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfOnuMacIndex.setStatus("current")


class _HpnicfOnuMacAddrFlag_Type(Integer32):
    """Custom type hpnicfOnuMacAddrFlag based on Integer32"""
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
        *(("bound", 1),
          ("regIncorrect", 4),
          ("registered", 2),
          ("run", 3))
    )


_HpnicfOnuMacAddrFlag_Type.__name__ = "Integer32"
_HpnicfOnuMacAddrFlag_Object = MibTableColumn
hpnicfOnuMacAddrFlag = _HpnicfOnuMacAddrFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 6, 1, 2),
    _HpnicfOnuMacAddrFlag_Type()
)
hpnicfOnuMacAddrFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuMacAddrFlag.setStatus("current")
_HpnicfOnuMacAddress_Type = MacAddress
_HpnicfOnuMacAddress_Object = MibTableColumn
hpnicfOnuMacAddress = _HpnicfOnuMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 6, 1, 3),
    _HpnicfOnuMacAddress_Type()
)
hpnicfOnuMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuMacAddress.setStatus("current")
_HpnicfOnuBindMacAddrTable_Object = MibTable
hpnicfOnuBindMacAddrTable = _HpnicfOnuBindMacAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 7)
)
if mibBuilder.loadTexts:
    hpnicfOnuBindMacAddrTable.setStatus("current")
_HpnicfOnuBindMacAddrEntry_Object = MibTableRow
hpnicfOnuBindMacAddrEntry = _HpnicfOnuBindMacAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 7, 1)
)
hpnicfOnuBindMacAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfOnuBindMacAddrEntry.setStatus("current")
_HpnicfOnuBindMacAddress_Type = MacAddress
_HpnicfOnuBindMacAddress_Object = MibTableColumn
hpnicfOnuBindMacAddress = _HpnicfOnuBindMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 7, 1, 1),
    _HpnicfOnuBindMacAddress_Type()
)
hpnicfOnuBindMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuBindMacAddress.setStatus("current")
_HpnicfOnuBindType_Type = Integer32
_HpnicfOnuBindType_Object = MibTableColumn
hpnicfOnuBindType = _HpnicfOnuBindType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 7, 1, 2),
    _HpnicfOnuBindType_Type()
)
hpnicfOnuBindType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuBindType.setStatus("current")
_HpnicfOnuFirmwareUpdateTable_Object = MibTable
hpnicfOnuFirmwareUpdateTable = _HpnicfOnuFirmwareUpdateTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 8)
)
if mibBuilder.loadTexts:
    hpnicfOnuFirmwareUpdateTable.setStatus("current")
_HpnicfOnuFirmwareUpdateEntry_Object = MibTableRow
hpnicfOnuFirmwareUpdateEntry = _HpnicfOnuFirmwareUpdateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 8, 1)
)
hpnicfOnuFirmwareUpdateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfOnuFirmwareUpdateEntry.setStatus("current")


class _HpnicfOnuUpdate_Type(Integer32):
    """Custom type hpnicfOnuUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("update", 1)
    )


_HpnicfOnuUpdate_Type.__name__ = "Integer32"
_HpnicfOnuUpdate_Object = MibTableColumn
hpnicfOnuUpdate = _HpnicfOnuUpdate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 8, 1, 1),
    _HpnicfOnuUpdate_Type()
)
hpnicfOnuUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuUpdate.setStatus("current")


class _HpnicfOnuUpdateResult_Type(Integer32):
    """Custom type hpnicfOnuUpdateResult based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fail", 3),
          ("fileNotExist", 4),
          ("fileNotMatchONU", 6),
          ("notSetFilename", 5),
          ("ok", 2),
          ("otherError", 8),
          ("timeout", 7),
          ("updating", 1))
    )


_HpnicfOnuUpdateResult_Type.__name__ = "Integer32"
_HpnicfOnuUpdateResult_Object = MibTableColumn
hpnicfOnuUpdateResult = _HpnicfOnuUpdateResult_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 8, 1, 2),
    _HpnicfOnuUpdateResult_Type()
)
hpnicfOnuUpdateResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuUpdateResult.setStatus("current")


class _HpnicfOnuUpdateFileName_Type(OctetString):
    """Custom type hpnicfOnuUpdateFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfOnuUpdateFileName_Type.__name__ = "OctetString"
_HpnicfOnuUpdateFileName_Object = MibTableColumn
hpnicfOnuUpdateFileName = _HpnicfOnuUpdateFileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 8, 1, 3),
    _HpnicfOnuUpdateFileName_Type()
)
hpnicfOnuUpdateFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuUpdateFileName.setStatus("current")
_HpnicfOnuLinkTestFrameNumMinVal_Type = Integer32
_HpnicfOnuLinkTestFrameNumMinVal_Object = MibScalar
hpnicfOnuLinkTestFrameNumMinVal = _HpnicfOnuLinkTestFrameNumMinVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 9),
    _HpnicfOnuLinkTestFrameNumMinVal_Type()
)
hpnicfOnuLinkTestFrameNumMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuLinkTestFrameNumMinVal.setStatus("current")
_HpnicfOnuLinkTestFrameNumMaxVal_Type = Integer32
_HpnicfOnuLinkTestFrameNumMaxVal_Object = MibScalar
hpnicfOnuLinkTestFrameNumMaxVal = _HpnicfOnuLinkTestFrameNumMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 10),
    _HpnicfOnuLinkTestFrameNumMaxVal_Type()
)
hpnicfOnuLinkTestFrameNumMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuLinkTestFrameNumMaxVal.setStatus("current")
_HpnicfOnuSlaMaxBandWidthMinVal_Type = Integer32
_HpnicfOnuSlaMaxBandWidthMinVal_Object = MibScalar
hpnicfOnuSlaMaxBandWidthMinVal = _HpnicfOnuSlaMaxBandWidthMinVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 11),
    _HpnicfOnuSlaMaxBandWidthMinVal_Type()
)
hpnicfOnuSlaMaxBandWidthMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuSlaMaxBandWidthMinVal.setStatus("current")
_HpnicfOnuSlaMaxBandWidthMaxVal_Type = Integer32
_HpnicfOnuSlaMaxBandWidthMaxVal_Object = MibScalar
hpnicfOnuSlaMaxBandWidthMaxVal = _HpnicfOnuSlaMaxBandWidthMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 12),
    _HpnicfOnuSlaMaxBandWidthMaxVal_Type()
)
hpnicfOnuSlaMaxBandWidthMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuSlaMaxBandWidthMaxVal.setStatus("current")
_HpnicfOnuSlaMinBandWidthMinVal_Type = Integer32
_HpnicfOnuSlaMinBandWidthMinVal_Object = MibScalar
hpnicfOnuSlaMinBandWidthMinVal = _HpnicfOnuSlaMinBandWidthMinVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 13),
    _HpnicfOnuSlaMinBandWidthMinVal_Type()
)
hpnicfOnuSlaMinBandWidthMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuSlaMinBandWidthMinVal.setStatus("current")
_HpnicfOnuSlaMinBandWidthMaxVal_Type = Integer32
_HpnicfOnuSlaMinBandWidthMaxVal_Object = MibScalar
hpnicfOnuSlaMinBandWidthMaxVal = _HpnicfOnuSlaMinBandWidthMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 14),
    _HpnicfOnuSlaMinBandWidthMaxVal_Type()
)
hpnicfOnuSlaMinBandWidthMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuSlaMinBandWidthMaxVal.setStatus("current")
_HpnicfEponOnuTypeManTable_Object = MibTable
hpnicfEponOnuTypeManTable = _HpnicfEponOnuTypeManTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 15)
)
if mibBuilder.loadTexts:
    hpnicfEponOnuTypeManTable.setStatus("current")
_HpnicfEponOnuTypeManEntry_Object = MibTableRow
hpnicfEponOnuTypeManEntry = _HpnicfEponOnuTypeManEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 15, 1)
)
hpnicfEponOnuTypeManEntry.setIndexNames(
    (0, "HPN-ICF-EPON-MIB", "hpnicfEponOnuTypeIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEponOnuTypeManEntry.setStatus("current")
_HpnicfEponOnuTypeIndex_Type = Integer32
_HpnicfEponOnuTypeIndex_Object = MibTableColumn
hpnicfEponOnuTypeIndex = _HpnicfEponOnuTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 15, 1, 1),
    _HpnicfEponOnuTypeIndex_Type()
)
hpnicfEponOnuTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEponOnuTypeIndex.setStatus("current")
_HpnicfEponOnuTypeDescr_Type = OctetString
_HpnicfEponOnuTypeDescr_Object = MibTableColumn
hpnicfEponOnuTypeDescr = _HpnicfEponOnuTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 15, 1, 2),
    _HpnicfEponOnuTypeDescr_Type()
)
hpnicfEponOnuTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponOnuTypeDescr.setStatus("current")
_HpnicfOnuPacketManTable_Object = MibTable
hpnicfOnuPacketManTable = _HpnicfOnuPacketManTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 16)
)
if mibBuilder.loadTexts:
    hpnicfOnuPacketManTable.setStatus("current")
_HpnicfOnuPacketManEntry_Object = MibTableRow
hpnicfOnuPacketManEntry = _HpnicfOnuPacketManEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 16, 1)
)
hpnicfOnuPacketManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfOnuPacketManEntry.setStatus("current")


class _HpnicfOnuPriorityTrust_Type(Integer32):
    """Custom type hpnicfOnuPriorityTrust based on Integer32"""
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
        *(("cos", 3),
          ("dscp", 1),
          ("ipprecedence", 2))
    )


_HpnicfOnuPriorityTrust_Type.__name__ = "Integer32"
_HpnicfOnuPriorityTrust_Object = MibTableColumn
hpnicfOnuPriorityTrust = _HpnicfOnuPriorityTrust_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 16, 1, 1),
    _HpnicfOnuPriorityTrust_Type()
)
hpnicfOnuPriorityTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuPriorityTrust.setStatus("current")


class _HpnicfOnuQueueScheduler_Type(Integer32):
    """Custom type hpnicfOnuQueueScheduler based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("spq", 1),
          ("wfq", 2))
    )


_HpnicfOnuQueueScheduler_Type.__name__ = "Integer32"
_HpnicfOnuQueueScheduler_Object = MibTableColumn
hpnicfOnuQueueScheduler = _HpnicfOnuQueueScheduler_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 16, 1, 2),
    _HpnicfOnuQueueScheduler_Type()
)
hpnicfOnuQueueScheduler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuQueueScheduler.setStatus("current")
_HpnicfOnuProtocolTable_Object = MibTable
hpnicfOnuProtocolTable = _HpnicfOnuProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 17)
)
if mibBuilder.loadTexts:
    hpnicfOnuProtocolTable.setStatus("current")
_HpnicfOnuProtocolEntry_Object = MibTableRow
hpnicfOnuProtocolEntry = _HpnicfOnuProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 17, 1)
)
hpnicfOnuProtocolEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfOnuProtocolEntry.setStatus("current")


class _HpnicfOnuStpStatus_Type(TruthValue):
    """Custom type hpnicfOnuStpStatus based on TruthValue"""


_HpnicfOnuStpStatus_Object = MibTableColumn
hpnicfOnuStpStatus = _HpnicfOnuStpStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 17, 1, 1),
    _HpnicfOnuStpStatus_Type()
)
hpnicfOnuStpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuStpStatus.setStatus("current")


class _HpnicfOnuIgmpSnoopingStatus_Type(TruthValue):
    """Custom type hpnicfOnuIgmpSnoopingStatus based on TruthValue"""


_HpnicfOnuIgmpSnoopingStatus_Object = MibTableColumn
hpnicfOnuIgmpSnoopingStatus = _HpnicfOnuIgmpSnoopingStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 17, 1, 2),
    _HpnicfOnuIgmpSnoopingStatus_Type()
)
hpnicfOnuIgmpSnoopingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuIgmpSnoopingStatus.setStatus("current")


class _HpnicfOnuDhcpsnoopingOption82_Type(TruthValue):
    """Custom type hpnicfOnuDhcpsnoopingOption82 based on TruthValue"""


_HpnicfOnuDhcpsnoopingOption82_Object = MibTableColumn
hpnicfOnuDhcpsnoopingOption82 = _HpnicfOnuDhcpsnoopingOption82_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 17, 1, 3),
    _HpnicfOnuDhcpsnoopingOption82_Type()
)
hpnicfOnuDhcpsnoopingOption82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuDhcpsnoopingOption82.setStatus("current")


class _HpnicfOnuDhcpsnooping_Type(TruthValue):
    """Custom type hpnicfOnuDhcpsnooping based on TruthValue"""


_HpnicfOnuDhcpsnooping_Object = MibTableColumn
hpnicfOnuDhcpsnooping = _HpnicfOnuDhcpsnooping_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 17, 1, 4),
    _HpnicfOnuDhcpsnooping_Type()
)
hpnicfOnuDhcpsnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuDhcpsnooping.setStatus("current")


class _HpnicfOnuPppoe_Type(TruthValue):
    """Custom type hpnicfOnuPppoe based on TruthValue"""


_HpnicfOnuPppoe_Object = MibTableColumn
hpnicfOnuPppoe = _HpnicfOnuPppoe_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 17, 1, 5),
    _HpnicfOnuPppoe_Type()
)
hpnicfOnuPppoe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuPppoe.setStatus("current")
_HpnicfOnuIgmpSnoopingHostAgingT_Type = Integer32
_HpnicfOnuIgmpSnoopingHostAgingT_Object = MibTableColumn
hpnicfOnuIgmpSnoopingHostAgingT = _HpnicfOnuIgmpSnoopingHostAgingT_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 17, 1, 6),
    _HpnicfOnuIgmpSnoopingHostAgingT_Type()
)
hpnicfOnuIgmpSnoopingHostAgingT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuIgmpSnoopingHostAgingT.setStatus("current")
_HpnicfOnuIgmpSnoopingMaxRespT_Type = Integer32
_HpnicfOnuIgmpSnoopingMaxRespT_Object = MibTableColumn
hpnicfOnuIgmpSnoopingMaxRespT = _HpnicfOnuIgmpSnoopingMaxRespT_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 17, 1, 7),
    _HpnicfOnuIgmpSnoopingMaxRespT_Type()
)
hpnicfOnuIgmpSnoopingMaxRespT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuIgmpSnoopingMaxRespT.setStatus("current")
_HpnicfOnuIgmpSnoopingRouterAgingT_Type = Integer32
_HpnicfOnuIgmpSnoopingRouterAgingT_Object = MibTableColumn
hpnicfOnuIgmpSnoopingRouterAgingT = _HpnicfOnuIgmpSnoopingRouterAgingT_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 17, 1, 8),
    _HpnicfOnuIgmpSnoopingRouterAgingT_Type()
)
hpnicfOnuIgmpSnoopingRouterAgingT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuIgmpSnoopingRouterAgingT.setStatus("current")


class _HpnicfOnuIgmpSnoopingAggReportS_Type(TruthValue):
    """Custom type hpnicfOnuIgmpSnoopingAggReportS based on TruthValue"""


_HpnicfOnuIgmpSnoopingAggReportS_Object = MibTableColumn
hpnicfOnuIgmpSnoopingAggReportS = _HpnicfOnuIgmpSnoopingAggReportS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 17, 1, 9),
    _HpnicfOnuIgmpSnoopingAggReportS_Type()
)
hpnicfOnuIgmpSnoopingAggReportS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuIgmpSnoopingAggReportS.setStatus("current")


class _HpnicfOnuIgmpSnoopingAggLeaveS_Type(TruthValue):
    """Custom type hpnicfOnuIgmpSnoopingAggLeaveS based on TruthValue"""


_HpnicfOnuIgmpSnoopingAggLeaveS_Object = MibTableColumn
hpnicfOnuIgmpSnoopingAggLeaveS = _HpnicfOnuIgmpSnoopingAggLeaveS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 17, 1, 10),
    _HpnicfOnuIgmpSnoopingAggLeaveS_Type()
)
hpnicfOnuIgmpSnoopingAggLeaveS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuIgmpSnoopingAggLeaveS.setStatus("current")
_HpnicfOnuDot1xTable_Object = MibTable
hpnicfOnuDot1xTable = _HpnicfOnuDot1xTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 18)
)
if mibBuilder.loadTexts:
    hpnicfOnuDot1xTable.setStatus("current")
_HpnicfOnuDot1xEntry_Object = MibTableRow
hpnicfOnuDot1xEntry = _HpnicfOnuDot1xEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 18, 1)
)
hpnicfOnuDot1xEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfOnuDot1xEntry.setStatus("current")
_HpnicfOnuDot1xAccount_Type = OctetString
_HpnicfOnuDot1xAccount_Object = MibTableColumn
hpnicfOnuDot1xAccount = _HpnicfOnuDot1xAccount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 18, 1, 1),
    _HpnicfOnuDot1xAccount_Type()
)
hpnicfOnuDot1xAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuDot1xAccount.setStatus("current")
_HpnicfOnuDot1xPassword_Type = OctetString
_HpnicfOnuDot1xPassword_Object = MibTableColumn
hpnicfOnuDot1xPassword = _HpnicfOnuDot1xPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 18, 1, 2),
    _HpnicfOnuDot1xPassword_Type()
)
hpnicfOnuDot1xPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuDot1xPassword.setStatus("current")
_HpnicfOnuPriorityQueueTable_Object = MibTable
hpnicfOnuPriorityQueueTable = _HpnicfOnuPriorityQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 19)
)
if mibBuilder.loadTexts:
    hpnicfOnuPriorityQueueTable.setStatus("current")
_HpnicfOnuPriorityQueueEntry_Object = MibTableRow
hpnicfOnuPriorityQueueEntry = _HpnicfOnuPriorityQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 19, 1)
)
hpnicfOnuPriorityQueueEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EPON-MIB", "hpnicfOnuQueueDirection"),
    (0, "HPN-ICF-EPON-MIB", "hpnicfOnuQueueId"),
)
if mibBuilder.loadTexts:
    hpnicfOnuPriorityQueueEntry.setStatus("current")


class _HpnicfOnuQueueDirection_Type(Integer32):
    """Custom type hpnicfOnuQueueDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HpnicfOnuQueueDirection_Type.__name__ = "Integer32"
_HpnicfOnuQueueDirection_Object = MibTableColumn
hpnicfOnuQueueDirection = _HpnicfOnuQueueDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 19, 1, 1),
    _HpnicfOnuQueueDirection_Type()
)
hpnicfOnuQueueDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfOnuQueueDirection.setStatus("current")


class _HpnicfOnuQueueId_Type(Integer32):
    """Custom type hpnicfOnuQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfOnuQueueId_Type.__name__ = "Integer32"
_HpnicfOnuQueueId_Object = MibTableColumn
hpnicfOnuQueueId = _HpnicfOnuQueueId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 19, 1, 2),
    _HpnicfOnuQueueId_Type()
)
hpnicfOnuQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfOnuQueueId.setStatus("current")
_HpnicfOnuQueueSize_Type = Integer32
_HpnicfOnuQueueSize_Object = MibTableColumn
hpnicfOnuQueueSize = _HpnicfOnuQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 19, 1, 3),
    _HpnicfOnuQueueSize_Type()
)
hpnicfOnuQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuQueueSize.setStatus("current")
_HpnicfOnuCountTable_Object = MibTable
hpnicfOnuCountTable = _HpnicfOnuCountTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 20)
)
if mibBuilder.loadTexts:
    hpnicfOnuCountTable.setStatus("current")
_HpnicfOnuCountEntry_Object = MibTableRow
hpnicfOnuCountEntry = _HpnicfOnuCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 20, 1)
)
hpnicfOnuCountEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfOnuCountEntry.setStatus("current")
_HpnicfOnuInCRCErrPkts_Type = Counter64
_HpnicfOnuInCRCErrPkts_Object = MibTableColumn
hpnicfOnuInCRCErrPkts = _HpnicfOnuInCRCErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 20, 1, 1),
    _HpnicfOnuInCRCErrPkts_Type()
)
hpnicfOnuInCRCErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuInCRCErrPkts.setStatus("current")
_HpnicfOnuOutDroppedFrames_Type = Counter64
_HpnicfOnuOutDroppedFrames_Object = MibTableColumn
hpnicfOnuOutDroppedFrames = _HpnicfOnuOutDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 20, 1, 2),
    _HpnicfOnuOutDroppedFrames_Type()
)
hpnicfOnuOutDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuOutDroppedFrames.setStatus("current")
_HpnicfEponOnuScalarGroup_ObjectIdentity = ObjectIdentity
hpnicfEponOnuScalarGroup = _HpnicfEponOnuScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 21)
)
_HpnicfOnuPriorityQueueSizeMinVal_Type = Integer32
_HpnicfOnuPriorityQueueSizeMinVal_Object = MibScalar
hpnicfOnuPriorityQueueSizeMinVal = _HpnicfOnuPriorityQueueSizeMinVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 21, 1),
    _HpnicfOnuPriorityQueueSizeMinVal_Type()
)
hpnicfOnuPriorityQueueSizeMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuPriorityQueueSizeMinVal.setStatus("current")
_HpnicfOnuPriorityQueueSizeMaxVal_Type = Integer32
_HpnicfOnuPriorityQueueSizeMaxVal_Object = MibScalar
hpnicfOnuPriorityQueueSizeMaxVal = _HpnicfOnuPriorityQueueSizeMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 21, 2),
    _HpnicfOnuPriorityQueueSizeMaxVal_Type()
)
hpnicfOnuPriorityQueueSizeMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuPriorityQueueSizeMaxVal.setStatus("current")
_HpnicfOnuPriorityQueueBandwidthMinVal_Type = Integer32
_HpnicfOnuPriorityQueueBandwidthMinVal_Object = MibScalar
hpnicfOnuPriorityQueueBandwidthMinVal = _HpnicfOnuPriorityQueueBandwidthMinVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 21, 3),
    _HpnicfOnuPriorityQueueBandwidthMinVal_Type()
)
hpnicfOnuPriorityQueueBandwidthMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuPriorityQueueBandwidthMinVal.setStatus("current")
_HpnicfOnuPriorityQueueBandwidthMaxVal_Type = Integer32
_HpnicfOnuPriorityQueueBandwidthMaxVal_Object = MibScalar
hpnicfOnuPriorityQueueBandwidthMaxVal = _HpnicfOnuPriorityQueueBandwidthMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 21, 4),
    _HpnicfOnuPriorityQueueBandwidthMaxVal_Type()
)
hpnicfOnuPriorityQueueBandwidthMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuPriorityQueueBandwidthMaxVal.setStatus("current")
_HpnicfOnuPriorityQueueBurstsizeMinVal_Type = Integer32
_HpnicfOnuPriorityQueueBurstsizeMinVal_Object = MibScalar
hpnicfOnuPriorityQueueBurstsizeMinVal = _HpnicfOnuPriorityQueueBurstsizeMinVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 21, 5),
    _HpnicfOnuPriorityQueueBurstsizeMinVal_Type()
)
hpnicfOnuPriorityQueueBurstsizeMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuPriorityQueueBurstsizeMinVal.setStatus("current")
_HpnicfOnuPriorityQueueBurstsizeMaxVal_Type = Integer32
_HpnicfOnuPriorityQueueBurstsizeMaxVal_Object = MibScalar
hpnicfOnuPriorityQueueBurstsizeMaxVal = _HpnicfOnuPriorityQueueBurstsizeMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 21, 6),
    _HpnicfOnuPriorityQueueBurstsizeMaxVal_Type()
)
hpnicfOnuPriorityQueueBurstsizeMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuPriorityQueueBurstsizeMaxVal.setStatus("current")
_HpnicfOnuUpdateByTypeNextIndex_Type = Integer32
_HpnicfOnuUpdateByTypeNextIndex_Object = MibScalar
hpnicfOnuUpdateByTypeNextIndex = _HpnicfOnuUpdateByTypeNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 21, 7),
    _HpnicfOnuUpdateByTypeNextIndex_Type()
)
hpnicfOnuUpdateByTypeNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuUpdateByTypeNextIndex.setStatus("current")
_HpnicfOnuQueueBandwidthTable_Object = MibTable
hpnicfOnuQueueBandwidthTable = _HpnicfOnuQueueBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 22)
)
if mibBuilder.loadTexts:
    hpnicfOnuQueueBandwidthTable.setStatus("current")
_HpnicfOnuQueueBandwidthEntry_Object = MibTableRow
hpnicfOnuQueueBandwidthEntry = _HpnicfOnuQueueBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 22, 1)
)
hpnicfOnuQueueBandwidthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EPON-MIB", "hpnicfOnuQueueDirection"),
    (0, "HPN-ICF-EPON-MIB", "hpnicfOnuQueueId"),
)
if mibBuilder.loadTexts:
    hpnicfOnuQueueBandwidthEntry.setStatus("current")
_HpnicfOnuQueueMaxBandwidth_Type = Integer32
_HpnicfOnuQueueMaxBandwidth_Object = MibTableColumn
hpnicfOnuQueueMaxBandwidth = _HpnicfOnuQueueMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 22, 1, 1),
    _HpnicfOnuQueueMaxBandwidth_Type()
)
hpnicfOnuQueueMaxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuQueueMaxBandwidth.setStatus("current")
_HpnicfOnuQueueMaxBurstsize_Type = Integer32
_HpnicfOnuQueueMaxBurstsize_Object = MibTableColumn
hpnicfOnuQueueMaxBurstsize = _HpnicfOnuQueueMaxBurstsize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 22, 1, 2),
    _HpnicfOnuQueueMaxBurstsize_Type()
)
hpnicfOnuQueueMaxBurstsize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuQueueMaxBurstsize.setStatus("current")
_HpnicfOnuQueuePolicyStatus_Type = TruthValue
_HpnicfOnuQueuePolicyStatus_Object = MibTableColumn
hpnicfOnuQueuePolicyStatus = _HpnicfOnuQueuePolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 22, 1, 3),
    _HpnicfOnuQueuePolicyStatus_Type()
)
hpnicfOnuQueuePolicyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuQueuePolicyStatus.setStatus("current")
_HpnicfOnuIpAddressTable_Object = MibTable
hpnicfOnuIpAddressTable = _HpnicfOnuIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 23)
)
if mibBuilder.loadTexts:
    hpnicfOnuIpAddressTable.setStatus("current")
_HpnicfOnuIpAddressEntry_Object = MibTableRow
hpnicfOnuIpAddressEntry = _HpnicfOnuIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 23, 1)
)
hpnicfOnuIpAddressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfOnuIpAddressEntry.setStatus("current")
_HpnicfOnuIpAddress_Type = IpAddress
_HpnicfOnuIpAddress_Object = MibTableColumn
hpnicfOnuIpAddress = _HpnicfOnuIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 23, 1, 1),
    _HpnicfOnuIpAddress_Type()
)
hpnicfOnuIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuIpAddress.setStatus("current")
_HpnicfOnuIpAddressMask_Type = IpAddress
_HpnicfOnuIpAddressMask_Object = MibTableColumn
hpnicfOnuIpAddressMask = _HpnicfOnuIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 23, 1, 2),
    _HpnicfOnuIpAddressMask_Type()
)
hpnicfOnuIpAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuIpAddressMask.setStatus("current")
_HpnicfOnuIpAddressGateway_Type = IpAddress
_HpnicfOnuIpAddressGateway_Object = MibTableColumn
hpnicfOnuIpAddressGateway = _HpnicfOnuIpAddressGateway_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 23, 1, 3),
    _HpnicfOnuIpAddressGateway_Type()
)
hpnicfOnuIpAddressGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuIpAddressGateway.setStatus("current")
_HpnicfOnuDhcpallocate_Type = TruthValue
_HpnicfOnuDhcpallocate_Object = MibTableColumn
hpnicfOnuDhcpallocate = _HpnicfOnuDhcpallocate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 23, 1, 4),
    _HpnicfOnuDhcpallocate_Type()
)
hpnicfOnuDhcpallocate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuDhcpallocate.setStatus("current")
_HpnicfOnuManageVID_Type = Integer32
_HpnicfOnuManageVID_Object = MibTableColumn
hpnicfOnuManageVID = _HpnicfOnuManageVID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 23, 1, 5),
    _HpnicfOnuManageVID_Type()
)
hpnicfOnuManageVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuManageVID.setStatus("current")
_HpnicfOnuManageVlanIntfS_Type = TruthValue
_HpnicfOnuManageVlanIntfS_Object = MibTableColumn
hpnicfOnuManageVlanIntfS = _HpnicfOnuManageVlanIntfS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 23, 1, 6),
    _HpnicfOnuManageVlanIntfS_Type()
)
hpnicfOnuManageVlanIntfS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuManageVlanIntfS.setStatus("current")
_HpnicfOnuChipSetInfoTable_Object = MibTable
hpnicfOnuChipSetInfoTable = _HpnicfOnuChipSetInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 24)
)
if mibBuilder.loadTexts:
    hpnicfOnuChipSetInfoTable.setStatus("current")
_HpnicfOnuChipSetInfoEntry_Object = MibTableRow
hpnicfOnuChipSetInfoEntry = _HpnicfOnuChipSetInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 24, 1)
)
hpnicfOnuChipSetInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfOnuChipSetInfoEntry.setStatus("current")


class _HpnicfOnuChipSetVendorId_Type(OctetString):
    """Custom type hpnicfOnuChipSetVendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfOnuChipSetVendorId_Type.__name__ = "OctetString"
_HpnicfOnuChipSetVendorId_Object = MibTableColumn
hpnicfOnuChipSetVendorId = _HpnicfOnuChipSetVendorId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 24, 1, 1),
    _HpnicfOnuChipSetVendorId_Type()
)
hpnicfOnuChipSetVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuChipSetVendorId.setStatus("current")


class _HpnicfOnuChipSetModel_Type(OctetString):
    """Custom type hpnicfOnuChipSetModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfOnuChipSetModel_Type.__name__ = "OctetString"
_HpnicfOnuChipSetModel_Object = MibTableColumn
hpnicfOnuChipSetModel = _HpnicfOnuChipSetModel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 24, 1, 2),
    _HpnicfOnuChipSetModel_Type()
)
hpnicfOnuChipSetModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuChipSetModel.setStatus("current")
_HpnicfOnuChipSetRevision_Type = Integer32
_HpnicfOnuChipSetRevision_Object = MibTableColumn
hpnicfOnuChipSetRevision = _HpnicfOnuChipSetRevision_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 24, 1, 3),
    _HpnicfOnuChipSetRevision_Type()
)
hpnicfOnuChipSetRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuChipSetRevision.setStatus("current")
_HpnicfOnuChipSetDesignDate_Type = DateAndTime
_HpnicfOnuChipSetDesignDate_Object = MibTableColumn
hpnicfOnuChipSetDesignDate = _HpnicfOnuChipSetDesignDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 24, 1, 4),
    _HpnicfOnuChipSetDesignDate_Type()
)
hpnicfOnuChipSetDesignDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuChipSetDesignDate.setStatus("current")
_HpnicfOnuCapabilityTable_Object = MibTable
hpnicfOnuCapabilityTable = _HpnicfOnuCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 25)
)
if mibBuilder.loadTexts:
    hpnicfOnuCapabilityTable.setStatus("current")
_HpnicfOnuCapabilityEntry_Object = MibTableRow
hpnicfOnuCapabilityEntry = _HpnicfOnuCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 25, 1)
)
hpnicfOnuCapabilityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfOnuCapabilityEntry.setStatus("current")


class _HpnicfOnuServiceSupported_Type(Bits):
    """Custom type hpnicfOnuServiceSupported based on Bits"""
    namedValues = NamedValues(
        *(("feinterfacesupport", 1),
          ("geinterfacesupport", 0),
          ("tdmservicesupport", 3),
          ("voipservicesupport", 2))
    )

_HpnicfOnuServiceSupported_Type.__name__ = "Bits"
_HpnicfOnuServiceSupported_Object = MibTableColumn
hpnicfOnuServiceSupported = _HpnicfOnuServiceSupported_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 25, 1, 1),
    _HpnicfOnuServiceSupported_Type()
)
hpnicfOnuServiceSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuServiceSupported.setStatus("current")
_HpnicfOnuGEPortNumber_Type = Integer32
_HpnicfOnuGEPortNumber_Object = MibTableColumn
hpnicfOnuGEPortNumber = _HpnicfOnuGEPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 25, 1, 2),
    _HpnicfOnuGEPortNumber_Type()
)
hpnicfOnuGEPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuGEPortNumber.setStatus("current")
_HpnicfOnuFEPortNumber_Type = Integer32
_HpnicfOnuFEPortNumber_Object = MibTableColumn
hpnicfOnuFEPortNumber = _HpnicfOnuFEPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 25, 1, 3),
    _HpnicfOnuFEPortNumber_Type()
)
hpnicfOnuFEPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuFEPortNumber.setStatus("current")
_HpnicfOnuPOTSPortNumber_Type = Integer32
_HpnicfOnuPOTSPortNumber_Object = MibTableColumn
hpnicfOnuPOTSPortNumber = _HpnicfOnuPOTSPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 25, 1, 4),
    _HpnicfOnuPOTSPortNumber_Type()
)
hpnicfOnuPOTSPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuPOTSPortNumber.setStatus("current")
_HpnicfOnuE1PortsNumber_Type = Integer32
_HpnicfOnuE1PortsNumber_Object = MibTableColumn
hpnicfOnuE1PortsNumber = _HpnicfOnuE1PortsNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 25, 1, 5),
    _HpnicfOnuE1PortsNumber_Type()
)
hpnicfOnuE1PortsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuE1PortsNumber.setStatus("current")
_HpnicfOnuUpstreamQueueNumber_Type = Integer32
_HpnicfOnuUpstreamQueueNumber_Object = MibTableColumn
hpnicfOnuUpstreamQueueNumber = _HpnicfOnuUpstreamQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 25, 1, 6),
    _HpnicfOnuUpstreamQueueNumber_Type()
)
hpnicfOnuUpstreamQueueNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuUpstreamQueueNumber.setStatus("current")
_HpnicfOnuMaxUpstreamQueuePerPort_Type = Integer32
_HpnicfOnuMaxUpstreamQueuePerPort_Object = MibTableColumn
hpnicfOnuMaxUpstreamQueuePerPort = _HpnicfOnuMaxUpstreamQueuePerPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 25, 1, 7),
    _HpnicfOnuMaxUpstreamQueuePerPort_Type()
)
hpnicfOnuMaxUpstreamQueuePerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuMaxUpstreamQueuePerPort.setStatus("current")
_HpnicfOnuDownstreamQueueNumber_Type = Integer32
_HpnicfOnuDownstreamQueueNumber_Object = MibTableColumn
hpnicfOnuDownstreamQueueNumber = _HpnicfOnuDownstreamQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 25, 1, 8),
    _HpnicfOnuDownstreamQueueNumber_Type()
)
hpnicfOnuDownstreamQueueNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuDownstreamQueueNumber.setStatus("current")
_HpnicfOnuMaxDownstreamQueuePerPort_Type = Integer32
_HpnicfOnuMaxDownstreamQueuePerPort_Object = MibTableColumn
hpnicfOnuMaxDownstreamQueuePerPort = _HpnicfOnuMaxDownstreamQueuePerPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 25, 1, 9),
    _HpnicfOnuMaxDownstreamQueuePerPort_Type()
)
hpnicfOnuMaxDownstreamQueuePerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuMaxDownstreamQueuePerPort.setStatus("current")
_HpnicfOnuBatteryBackup_Type = TruthValue
_HpnicfOnuBatteryBackup_Object = MibTableColumn
hpnicfOnuBatteryBackup = _HpnicfOnuBatteryBackup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 25, 1, 10),
    _HpnicfOnuBatteryBackup_Type()
)
hpnicfOnuBatteryBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuBatteryBackup.setStatus("current")
_HpnicfOnuIgspFastLeaveSupported_Type = TruthValue
_HpnicfOnuIgspFastLeaveSupported_Object = MibTableColumn
hpnicfOnuIgspFastLeaveSupported = _HpnicfOnuIgspFastLeaveSupported_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 25, 1, 11),
    _HpnicfOnuIgspFastLeaveSupported_Type()
)
hpnicfOnuIgspFastLeaveSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuIgspFastLeaveSupported.setStatus("current")
_HpnicfOnuMCtrlFastLeaveSupported_Type = TruthValue
_HpnicfOnuMCtrlFastLeaveSupported_Object = MibTableColumn
hpnicfOnuMCtrlFastLeaveSupported = _HpnicfOnuMCtrlFastLeaveSupported_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 25, 1, 12),
    _HpnicfOnuMCtrlFastLeaveSupported_Type()
)
hpnicfOnuMCtrlFastLeaveSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuMCtrlFastLeaveSupported.setStatus("current")
_HpnicfOnuDbaReportTable_Object = MibTable
hpnicfOnuDbaReportTable = _HpnicfOnuDbaReportTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 26)
)
if mibBuilder.loadTexts:
    hpnicfOnuDbaReportTable.setStatus("current")
_HpnicfOnuDbaReportEntry_Object = MibTableRow
hpnicfOnuDbaReportEntry = _HpnicfOnuDbaReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 26, 1)
)
hpnicfOnuDbaReportEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EPON-MIB", "hpnicfOnuDbaReportQueueId"),
)
if mibBuilder.loadTexts:
    hpnicfOnuDbaReportEntry.setStatus("current")
_HpnicfOnuDbaReportQueueId_Type = Integer32
_HpnicfOnuDbaReportQueueId_Object = MibTableColumn
hpnicfOnuDbaReportQueueId = _HpnicfOnuDbaReportQueueId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 26, 1, 1),
    _HpnicfOnuDbaReportQueueId_Type()
)
hpnicfOnuDbaReportQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfOnuDbaReportQueueId.setStatus("current")
_HpnicfOnuDbaReportThreshold_Type = Integer32
_HpnicfOnuDbaReportThreshold_Object = MibTableColumn
hpnicfOnuDbaReportThreshold = _HpnicfOnuDbaReportThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 26, 1, 2),
    _HpnicfOnuDbaReportThreshold_Type()
)
hpnicfOnuDbaReportThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuDbaReportThreshold.setStatus("current")


class _HpnicfOnuDbaReportStatus_Type(Integer32):
    """Custom type hpnicfOnuDbaReportStatus based on Integer32"""
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


_HpnicfOnuDbaReportStatus_Type.__name__ = "Integer32"
_HpnicfOnuDbaReportStatus_Object = MibTableColumn
hpnicfOnuDbaReportStatus = _HpnicfOnuDbaReportStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 26, 1, 3),
    _HpnicfOnuDbaReportStatus_Type()
)
hpnicfOnuDbaReportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuDbaReportStatus.setStatus("current")
_HpnicfOnuCosToLocalPrecedenceTable_Object = MibTable
hpnicfOnuCosToLocalPrecedenceTable = _HpnicfOnuCosToLocalPrecedenceTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 27)
)
if mibBuilder.loadTexts:
    hpnicfOnuCosToLocalPrecedenceTable.setStatus("current")
_HpnicfOnuCosToLocalPrecedenceEntry_Object = MibTableRow
hpnicfOnuCosToLocalPrecedenceEntry = _HpnicfOnuCosToLocalPrecedenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 27, 1)
)
hpnicfOnuCosToLocalPrecedenceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EPON-MIB", "hpnicfOnuCosToLocalPrecedenceCosIndex"),
)
if mibBuilder.loadTexts:
    hpnicfOnuCosToLocalPrecedenceEntry.setStatus("current")


class _HpnicfOnuCosToLocalPrecedenceCosIndex_Type(Integer32):
    """Custom type hpnicfOnuCosToLocalPrecedenceCosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfOnuCosToLocalPrecedenceCosIndex_Type.__name__ = "Integer32"
_HpnicfOnuCosToLocalPrecedenceCosIndex_Object = MibTableColumn
hpnicfOnuCosToLocalPrecedenceCosIndex = _HpnicfOnuCosToLocalPrecedenceCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 27, 1, 1),
    _HpnicfOnuCosToLocalPrecedenceCosIndex_Type()
)
hpnicfOnuCosToLocalPrecedenceCosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuCosToLocalPrecedenceCosIndex.setStatus("current")


class _HpnicfOnuCosToLocalPrecedenceValue_Type(Integer32):
    """Custom type hpnicfOnuCosToLocalPrecedenceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfOnuCosToLocalPrecedenceValue_Type.__name__ = "Integer32"
_HpnicfOnuCosToLocalPrecedenceValue_Object = MibTableColumn
hpnicfOnuCosToLocalPrecedenceValue = _HpnicfOnuCosToLocalPrecedenceValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 27, 1, 2),
    _HpnicfOnuCosToLocalPrecedenceValue_Type()
)
hpnicfOnuCosToLocalPrecedenceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuCosToLocalPrecedenceValue.setStatus("current")
_HpnicfEponOnuStpPortTable_Object = MibTable
hpnicfEponOnuStpPortTable = _HpnicfEponOnuStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 28)
)
if mibBuilder.loadTexts:
    hpnicfEponOnuStpPortTable.setStatus("current")
_HpnicfEponOnuStpPortEntry_Object = MibTableRow
hpnicfEponOnuStpPortEntry = _HpnicfEponOnuStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 28, 1)
)
hpnicfEponOnuStpPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EPON-MIB", "hpnicfEponStpPortIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEponOnuStpPortEntry.setStatus("current")


class _HpnicfEponStpPortIndex_Type(Integer32):
    """Custom type hpnicfEponStpPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 144),
    )


_HpnicfEponStpPortIndex_Type.__name__ = "Integer32"
_HpnicfEponStpPortIndex_Object = MibTableColumn
hpnicfEponStpPortIndex = _HpnicfEponStpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 28, 1, 1),
    _HpnicfEponStpPortIndex_Type()
)
hpnicfEponStpPortIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfEponStpPortIndex.setStatus("current")
_HpnicfEponStpPortDescr_Type = OctetString
_HpnicfEponStpPortDescr_Object = MibTableColumn
hpnicfEponStpPortDescr = _HpnicfEponStpPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 28, 1, 2),
    _HpnicfEponStpPortDescr_Type()
)
hpnicfEponStpPortDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfEponStpPortDescr.setStatus("current")


class _HpnicfEponStpPortState_Type(Integer32):
    """Custom type hpnicfEponStpPortState based on Integer32"""
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
        *(("disabled", 1),
          ("discarding", 2),
          ("forwarding", 4),
          ("learning", 3))
    )


_HpnicfEponStpPortState_Type.__name__ = "Integer32"
_HpnicfEponStpPortState_Object = MibTableColumn
hpnicfEponStpPortState = _HpnicfEponStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 28, 1, 3),
    _HpnicfEponStpPortState_Type()
)
hpnicfEponStpPortState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfEponStpPortState.setStatus("current")
_HpnicfOnuPhysicalTable_Object = MibTable
hpnicfOnuPhysicalTable = _HpnicfOnuPhysicalTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 29)
)
if mibBuilder.loadTexts:
    hpnicfOnuPhysicalTable.setStatus("current")
_HpnicfOnuPhysicalEntry_Object = MibTableRow
hpnicfOnuPhysicalEntry = _HpnicfOnuPhysicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 29, 1)
)
hpnicfOnuPhysicalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfOnuPhysicalEntry.setStatus("current")
_HpnicfOnuBridgeMac_Type = MacAddress
_HpnicfOnuBridgeMac_Object = MibTableColumn
hpnicfOnuBridgeMac = _HpnicfOnuBridgeMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 29, 1, 1),
    _HpnicfOnuBridgeMac_Type()
)
hpnicfOnuBridgeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuBridgeMac.setStatus("current")
_HpnicfOnuFirstPonMac_Type = MacAddress
_HpnicfOnuFirstPonMac_Object = MibTableColumn
hpnicfOnuFirstPonMac = _HpnicfOnuFirstPonMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 29, 1, 2),
    _HpnicfOnuFirstPonMac_Type()
)
hpnicfOnuFirstPonMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuFirstPonMac.setStatus("current")


class _HpnicfOnuFirstPonRegState_Type(Integer32):
    """Custom type hpnicfOnuFirstPonRegState based on Integer32"""
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
        *(("absent", 2),
          ("down", 5),
          ("notExist", 1),
          ("offline", 3),
          ("silent", 4),
          ("up", 6))
    )


_HpnicfOnuFirstPonRegState_Type.__name__ = "Integer32"
_HpnicfOnuFirstPonRegState_Object = MibTableColumn
hpnicfOnuFirstPonRegState = _HpnicfOnuFirstPonRegState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 29, 1, 3),
    _HpnicfOnuFirstPonRegState_Type()
)
hpnicfOnuFirstPonRegState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuFirstPonRegState.setStatus("current")
_HpnicfOnuSecondPonMac_Type = MacAddress
_HpnicfOnuSecondPonMac_Object = MibTableColumn
hpnicfOnuSecondPonMac = _HpnicfOnuSecondPonMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 29, 1, 4),
    _HpnicfOnuSecondPonMac_Type()
)
hpnicfOnuSecondPonMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuSecondPonMac.setStatus("current")


class _HpnicfOnuSecondPonRegState_Type(Integer32):
    """Custom type hpnicfOnuSecondPonRegState based on Integer32"""
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
        *(("absent", 2),
          ("down", 5),
          ("notExist", 1),
          ("offline", 3),
          ("silent", 4),
          ("up", 6))
    )


_HpnicfOnuSecondPonRegState_Type.__name__ = "Integer32"
_HpnicfOnuSecondPonRegState_Object = MibTableColumn
hpnicfOnuSecondPonRegState = _HpnicfOnuSecondPonRegState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 29, 1, 5),
    _HpnicfOnuSecondPonRegState_Type()
)
hpnicfOnuSecondPonRegState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuSecondPonRegState.setStatus("current")
_HpnicfOnuSmlkTable_Object = MibTable
hpnicfOnuSmlkTable = _HpnicfOnuSmlkTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 30)
)
if mibBuilder.loadTexts:
    hpnicfOnuSmlkTable.setStatus("current")
_HpnicfOnuSmlkEntry_Object = MibTableRow
hpnicfOnuSmlkEntry = _HpnicfOnuSmlkEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 30, 1)
)
hpnicfOnuSmlkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EPON-MIB", "hpnicfOnuSmlkGroupID"),
)
if mibBuilder.loadTexts:
    hpnicfOnuSmlkEntry.setStatus("current")
_HpnicfOnuSmlkGroupID_Type = Integer32
_HpnicfOnuSmlkGroupID_Object = MibTableColumn
hpnicfOnuSmlkGroupID = _HpnicfOnuSmlkGroupID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 30, 1, 1),
    _HpnicfOnuSmlkGroupID_Type()
)
hpnicfOnuSmlkGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuSmlkGroupID.setStatus("current")


class _HpnicfOnuSmlkFirstPonRole_Type(Integer32):
    """Custom type hpnicfOnuSmlkFirstPonRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("null", 3),
          ("slave", 2))
    )


_HpnicfOnuSmlkFirstPonRole_Type.__name__ = "Integer32"
_HpnicfOnuSmlkFirstPonRole_Object = MibTableColumn
hpnicfOnuSmlkFirstPonRole = _HpnicfOnuSmlkFirstPonRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 30, 1, 2),
    _HpnicfOnuSmlkFirstPonRole_Type()
)
hpnicfOnuSmlkFirstPonRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuSmlkFirstPonRole.setStatus("current")


class _HpnicfOnuSmlkFirstPonStatus_Type(Integer32):
    """Custom type hpnicfOnuSmlkFirstPonStatus based on Integer32"""
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
        *(("active", 1),
          ("down", 3),
          ("null", 4),
          ("standby", 2))
    )


_HpnicfOnuSmlkFirstPonStatus_Type.__name__ = "Integer32"
_HpnicfOnuSmlkFirstPonStatus_Object = MibTableColumn
hpnicfOnuSmlkFirstPonStatus = _HpnicfOnuSmlkFirstPonStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 30, 1, 3),
    _HpnicfOnuSmlkFirstPonStatus_Type()
)
hpnicfOnuSmlkFirstPonStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuSmlkFirstPonStatus.setStatus("current")


class _HpnicfOnuSmlkSecondPonRole_Type(Integer32):
    """Custom type hpnicfOnuSmlkSecondPonRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("null", 3),
          ("slave", 2))
    )


_HpnicfOnuSmlkSecondPonRole_Type.__name__ = "Integer32"
_HpnicfOnuSmlkSecondPonRole_Object = MibTableColumn
hpnicfOnuSmlkSecondPonRole = _HpnicfOnuSmlkSecondPonRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 30, 1, 4),
    _HpnicfOnuSmlkSecondPonRole_Type()
)
hpnicfOnuSmlkSecondPonRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuSmlkSecondPonRole.setStatus("current")


class _HpnicfOnuSmlkSecondPonStatus_Type(Integer32):
    """Custom type hpnicfOnuSmlkSecondPonStatus based on Integer32"""
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
        *(("active", 1),
          ("down", 3),
          ("null", 4),
          ("standby", 2))
    )


_HpnicfOnuSmlkSecondPonStatus_Type.__name__ = "Integer32"
_HpnicfOnuSmlkSecondPonStatus_Object = MibTableColumn
hpnicfOnuSmlkSecondPonStatus = _HpnicfOnuSmlkSecondPonStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 30, 1, 5),
    _HpnicfOnuSmlkSecondPonStatus_Type()
)
hpnicfOnuSmlkSecondPonStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuSmlkSecondPonStatus.setStatus("current")
_HpnicfOnuRS485PropertiesTable_Object = MibTable
hpnicfOnuRS485PropertiesTable = _HpnicfOnuRS485PropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 31)
)
if mibBuilder.loadTexts:
    hpnicfOnuRS485PropertiesTable.setStatus("current")
_HpnicfOnuRS485PropertiesEntry_Object = MibTableRow
hpnicfOnuRS485PropertiesEntry = _HpnicfOnuRS485PropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 31, 1)
)
hpnicfOnuRS485PropertiesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EPON-MIB", "hpnicfOnuRS485SerialIndex"),
)
if mibBuilder.loadTexts:
    hpnicfOnuRS485PropertiesEntry.setStatus("current")


class _HpnicfOnuRS485SerialIndex_Type(Integer32):
    """Custom type hpnicfOnuRS485SerialIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HpnicfOnuRS485SerialIndex_Type.__name__ = "Integer32"
_HpnicfOnuRS485SerialIndex_Object = MibTableColumn
hpnicfOnuRS485SerialIndex = _HpnicfOnuRS485SerialIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 31, 1, 1),
    _HpnicfOnuRS485SerialIndex_Type()
)
hpnicfOnuRS485SerialIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfOnuRS485SerialIndex.setStatus("current")


class _HpnicfOnuRS485BaudRate_Type(Integer32):
    """Custom type hpnicfOnuRS485BaudRate based on Integer32"""
    defaultValue = 6

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
        *(("baudRate115200", 10),
          ("baudRate1200", 3),
          ("baudRate19200", 7),
          ("baudRate2400", 4),
          ("baudRate300", 1),
          ("baudRate38400", 8),
          ("baudRate4800", 5),
          ("baudRate57600", 9),
          ("baudRate600", 2),
          ("baudRate9600", 6))
    )


_HpnicfOnuRS485BaudRate_Type.__name__ = "Integer32"
_HpnicfOnuRS485BaudRate_Object = MibTableColumn
hpnicfOnuRS485BaudRate = _HpnicfOnuRS485BaudRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 31, 1, 2),
    _HpnicfOnuRS485BaudRate_Type()
)
hpnicfOnuRS485BaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuRS485BaudRate.setStatus("current")


class _HpnicfOnuRS485DataBits_Type(Integer32):
    """Custom type hpnicfOnuRS485DataBits based on Integer32"""
    defaultValue = 4

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
        *(("eight", 4),
          ("five", 1),
          ("seven", 3),
          ("six", 2))
    )


_HpnicfOnuRS485DataBits_Type.__name__ = "Integer32"
_HpnicfOnuRS485DataBits_Object = MibTableColumn
hpnicfOnuRS485DataBits = _HpnicfOnuRS485DataBits_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 31, 1, 3),
    _HpnicfOnuRS485DataBits_Type()
)
hpnicfOnuRS485DataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuRS485DataBits.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfOnuRS485DataBits.setUnits("bit")


class _HpnicfOnuRS485Parity_Type(Integer32):
    """Custom type hpnicfOnuRS485Parity based on Integer32"""
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
        *(("even", 3),
          ("mark", 4),
          ("none", 1),
          ("odd", 2),
          ("space", 5))
    )


_HpnicfOnuRS485Parity_Type.__name__ = "Integer32"
_HpnicfOnuRS485Parity_Object = MibTableColumn
hpnicfOnuRS485Parity = _HpnicfOnuRS485Parity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 31, 1, 4),
    _HpnicfOnuRS485Parity_Type()
)
hpnicfOnuRS485Parity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuRS485Parity.setStatus("current")


class _HpnicfOnuRS485StopBits_Type(Integer32):
    """Custom type hpnicfOnuRS485StopBits based on Integer32"""
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
        *(("one", 1),
          ("oneAndHalf", 3),
          ("two", 2))
    )


_HpnicfOnuRS485StopBits_Type.__name__ = "Integer32"
_HpnicfOnuRS485StopBits_Object = MibTableColumn
hpnicfOnuRS485StopBits = _HpnicfOnuRS485StopBits_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 31, 1, 5),
    _HpnicfOnuRS485StopBits_Type()
)
hpnicfOnuRS485StopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuRS485StopBits.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfOnuRS485StopBits.setUnits("bit")


class _HpnicfOnuRS485FlowControl_Type(Integer32):
    """Custom type hpnicfOnuRS485FlowControl based on Integer32"""
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
        *(("hardware", 2),
          ("none", 1),
          ("xonOrxoff", 3))
    )


_HpnicfOnuRS485FlowControl_Type.__name__ = "Integer32"
_HpnicfOnuRS485FlowControl_Object = MibTableColumn
hpnicfOnuRS485FlowControl = _HpnicfOnuRS485FlowControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 31, 1, 6),
    _HpnicfOnuRS485FlowControl_Type()
)
hpnicfOnuRS485FlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuRS485FlowControl.setStatus("current")
_HpnicfOnuRS485TXOctets_Type = Integer32
_HpnicfOnuRS485TXOctets_Object = MibTableColumn
hpnicfOnuRS485TXOctets = _HpnicfOnuRS485TXOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 31, 1, 7),
    _HpnicfOnuRS485TXOctets_Type()
)
hpnicfOnuRS485TXOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuRS485TXOctets.setStatus("current")
_HpnicfOnuRS485RXOctets_Type = Integer32
_HpnicfOnuRS485RXOctets_Object = MibTableColumn
hpnicfOnuRS485RXOctets = _HpnicfOnuRS485RXOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 31, 1, 8),
    _HpnicfOnuRS485RXOctets_Type()
)
hpnicfOnuRS485RXOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuRS485RXOctets.setStatus("current")
_HpnicfOnuRS485TXErrOctets_Type = Integer32
_HpnicfOnuRS485TXErrOctets_Object = MibTableColumn
hpnicfOnuRS485TXErrOctets = _HpnicfOnuRS485TXErrOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 31, 1, 9),
    _HpnicfOnuRS485TXErrOctets_Type()
)
hpnicfOnuRS485TXErrOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuRS485TXErrOctets.setStatus("current")
_HpnicfOnuRS485RXErrOctets_Type = Integer32
_HpnicfOnuRS485RXErrOctets_Object = MibTableColumn
hpnicfOnuRS485RXErrOctets = _HpnicfOnuRS485RXErrOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 31, 1, 10),
    _HpnicfOnuRS485RXErrOctets_Type()
)
hpnicfOnuRS485RXErrOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuRS485RXErrOctets.setStatus("current")


class _HpnicfOnuRS485ResetStatistics_Type(Integer32):
    """Custom type hpnicfOnuRS485ResetStatistics based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("counting", 1))
    )


_HpnicfOnuRS485ResetStatistics_Type.__name__ = "Integer32"
_HpnicfOnuRS485ResetStatistics_Object = MibTableColumn
hpnicfOnuRS485ResetStatistics = _HpnicfOnuRS485ResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 31, 1, 11),
    _HpnicfOnuRS485ResetStatistics_Type()
)
hpnicfOnuRS485ResetStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfOnuRS485ResetStatistics.setStatus("current")
_HpnicfOnuRS485SessionSummaryTable_Object = MibTable
hpnicfOnuRS485SessionSummaryTable = _HpnicfOnuRS485SessionSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 32)
)
if mibBuilder.loadTexts:
    hpnicfOnuRS485SessionSummaryTable.setStatus("current")
_HpnicfOnuRS485SessionSummaryEntry_Object = MibTableRow
hpnicfOnuRS485SessionSummaryEntry = _HpnicfOnuRS485SessionSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 32, 1)
)
hpnicfOnuRS485SessionSummaryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EPON-MIB", "hpnicfOnuRS485SerialIndex"),
)
if mibBuilder.loadTexts:
    hpnicfOnuRS485SessionSummaryEntry.setStatus("current")


class _HpnicfOnuRS485SessionMaxNum_Type(Integer32):
    """Custom type hpnicfOnuRS485SessionMaxNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HpnicfOnuRS485SessionMaxNum_Type.__name__ = "Integer32"
_HpnicfOnuRS485SessionMaxNum_Object = MibTableColumn
hpnicfOnuRS485SessionMaxNum = _HpnicfOnuRS485SessionMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 32, 1, 1),
    _HpnicfOnuRS485SessionMaxNum_Type()
)
hpnicfOnuRS485SessionMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuRS485SessionMaxNum.setStatus("current")


class _HpnicfOnuRS485SessionNextIndex_Type(Integer32):
    """Custom type hpnicfOnuRS485SessionNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_HpnicfOnuRS485SessionNextIndex_Type.__name__ = "Integer32"
_HpnicfOnuRS485SessionNextIndex_Object = MibTableColumn
hpnicfOnuRS485SessionNextIndex = _HpnicfOnuRS485SessionNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 32, 1, 2),
    _HpnicfOnuRS485SessionNextIndex_Type()
)
hpnicfOnuRS485SessionNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuRS485SessionNextIndex.setStatus("current")
_HpnicfOnuRS485SessionTable_Object = MibTable
hpnicfOnuRS485SessionTable = _HpnicfOnuRS485SessionTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 33)
)
if mibBuilder.loadTexts:
    hpnicfOnuRS485SessionTable.setStatus("current")
_HpnicfOnuRS485SessionEntry_Object = MibTableRow
hpnicfOnuRS485SessionEntry = _HpnicfOnuRS485SessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 33, 1)
)
hpnicfOnuRS485SessionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EPON-MIB", "hpnicfOnuRS485SerialIndex"),
    (0, "HPN-ICF-EPON-MIB", "hpnicfOnuRS485SessionIndex"),
)
if mibBuilder.loadTexts:
    hpnicfOnuRS485SessionEntry.setStatus("current")


class _HpnicfOnuRS485SessionIndex_Type(Integer32):
    """Custom type hpnicfOnuRS485SessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HpnicfOnuRS485SessionIndex_Type.__name__ = "Integer32"
_HpnicfOnuRS485SessionIndex_Object = MibTableColumn
hpnicfOnuRS485SessionIndex = _HpnicfOnuRS485SessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 33, 1, 1),
    _HpnicfOnuRS485SessionIndex_Type()
)
hpnicfOnuRS485SessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfOnuRS485SessionIndex.setStatus("current")


class _HpnicfOnuRS485SessionType_Type(Integer32):
    """Custom type hpnicfOnuRS485SessionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcpClient", 2),
          ("tcpServer", 3),
          ("udp", 1))
    )


_HpnicfOnuRS485SessionType_Type.__name__ = "Integer32"
_HpnicfOnuRS485SessionType_Object = MibTableColumn
hpnicfOnuRS485SessionType = _HpnicfOnuRS485SessionType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 33, 1, 2),
    _HpnicfOnuRS485SessionType_Type()
)
hpnicfOnuRS485SessionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfOnuRS485SessionType.setStatus("current")
_HpnicfOnuRS485SessionAddType_Type = InetAddressType
_HpnicfOnuRS485SessionAddType_Object = MibTableColumn
hpnicfOnuRS485SessionAddType = _HpnicfOnuRS485SessionAddType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 33, 1, 3),
    _HpnicfOnuRS485SessionAddType_Type()
)
hpnicfOnuRS485SessionAddType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfOnuRS485SessionAddType.setStatus("current")
_HpnicfOnuRS485SessionRemoteIP_Type = InetAddress
_HpnicfOnuRS485SessionRemoteIP_Object = MibTableColumn
hpnicfOnuRS485SessionRemoteIP = _HpnicfOnuRS485SessionRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 33, 1, 4),
    _HpnicfOnuRS485SessionRemoteIP_Type()
)
hpnicfOnuRS485SessionRemoteIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfOnuRS485SessionRemoteIP.setStatus("current")


class _HpnicfOnuRS485SessionRemotePort_Type(Integer32):
    """Custom type hpnicfOnuRS485SessionRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_HpnicfOnuRS485SessionRemotePort_Type.__name__ = "Integer32"
_HpnicfOnuRS485SessionRemotePort_Object = MibTableColumn
hpnicfOnuRS485SessionRemotePort = _HpnicfOnuRS485SessionRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 33, 1, 5),
    _HpnicfOnuRS485SessionRemotePort_Type()
)
hpnicfOnuRS485SessionRemotePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfOnuRS485SessionRemotePort.setStatus("current")


class _HpnicfOnuRS485SessionLocalPort_Type(Integer32):
    """Custom type hpnicfOnuRS485SessionLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_HpnicfOnuRS485SessionLocalPort_Type.__name__ = "Integer32"
_HpnicfOnuRS485SessionLocalPort_Object = MibTableColumn
hpnicfOnuRS485SessionLocalPort = _HpnicfOnuRS485SessionLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 33, 1, 6),
    _HpnicfOnuRS485SessionLocalPort_Type()
)
hpnicfOnuRS485SessionLocalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfOnuRS485SessionLocalPort.setStatus("current")
_HpnicfOnuRS485SessionRowStatus_Type = RowStatus
_HpnicfOnuRS485SessionRowStatus_Object = MibTableColumn
hpnicfOnuRS485SessionRowStatus = _HpnicfOnuRS485SessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 33, 1, 7),
    _HpnicfOnuRS485SessionRowStatus_Type()
)
hpnicfOnuRS485SessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfOnuRS485SessionRowStatus.setStatus("current")
_HpnicfOnuRS485SessionErrInfoTable_Object = MibTable
hpnicfOnuRS485SessionErrInfoTable = _HpnicfOnuRS485SessionErrInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 34)
)
if mibBuilder.loadTexts:
    hpnicfOnuRS485SessionErrInfoTable.setStatus("current")
_HpnicfOnuRS485SessionErrInfoEntry_Object = MibTableRow
hpnicfOnuRS485SessionErrInfoEntry = _HpnicfOnuRS485SessionErrInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 34, 1)
)
hpnicfOnuRS485SessionErrInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EPON-MIB", "hpnicfOnuRS485SerialIndex"),
    (0, "HPN-ICF-EPON-MIB", "hpnicfOnuRS485SessionIndex"),
)
if mibBuilder.loadTexts:
    hpnicfOnuRS485SessionErrInfoEntry.setStatus("current")
_HpnicfOnuRS485SessionErrInfo_Type = DisplayString
_HpnicfOnuRS485SessionErrInfo_Object = MibTableColumn
hpnicfOnuRS485SessionErrInfo = _HpnicfOnuRS485SessionErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 5, 34, 1, 1),
    _HpnicfOnuRS485SessionErrInfo_Type()
)
hpnicfOnuRS485SessionErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfOnuRS485SessionErrInfo.setStatus("current")
_HpnicfEponBatchOperationMan_ObjectIdentity = ObjectIdentity
hpnicfEponBatchOperationMan = _HpnicfEponBatchOperationMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 6)
)
_HpnicfEponBatchOperationBySlotTable_Object = MibTable
hpnicfEponBatchOperationBySlotTable = _HpnicfEponBatchOperationBySlotTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hpnicfEponBatchOperationBySlotTable.setStatus("current")
_HpnicfEponBatchOperationBySlotEntry_Object = MibTableRow
hpnicfEponBatchOperationBySlotEntry = _HpnicfEponBatchOperationBySlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 6, 1, 1)
)
hpnicfEponBatchOperationBySlotEntry.setIndexNames(
    (0, "HPN-ICF-EPON-MIB", "hpnicfEponBatchOperationBySlotIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEponBatchOperationBySlotEntry.setStatus("current")
_HpnicfEponBatchOperationBySlotIndex_Type = Integer32
_HpnicfEponBatchOperationBySlotIndex_Object = MibTableColumn
hpnicfEponBatchOperationBySlotIndex = _HpnicfEponBatchOperationBySlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 6, 1, 1, 1),
    _HpnicfEponBatchOperationBySlotIndex_Type()
)
hpnicfEponBatchOperationBySlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEponBatchOperationBySlotIndex.setStatus("current")


class _HpnicfEponBatchOperationBySlotType_Type(Integer32):
    """Custom type hpnicfEponBatchOperationBySlotType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("resetUnknown", 1),
          ("updateDba", 9),
          ("updateONU", 10))
    )


_HpnicfEponBatchOperationBySlotType_Type.__name__ = "Integer32"
_HpnicfEponBatchOperationBySlotType_Object = MibTableColumn
hpnicfEponBatchOperationBySlotType = _HpnicfEponBatchOperationBySlotType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 6, 1, 1, 2),
    _HpnicfEponBatchOperationBySlotType_Type()
)
hpnicfEponBatchOperationBySlotType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponBatchOperationBySlotType.setStatus("current")


class _HpnicfEponBatchOperationBySlot_Type(Integer32):
    """Custom type hpnicfEponBatchOperationBySlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("batOpBySlot", 1)
    )


_HpnicfEponBatchOperationBySlot_Type.__name__ = "Integer32"
_HpnicfEponBatchOperationBySlot_Object = MibTableColumn
hpnicfEponBatchOperationBySlot = _HpnicfEponBatchOperationBySlot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 6, 1, 1, 3),
    _HpnicfEponBatchOperationBySlot_Type()
)
hpnicfEponBatchOperationBySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponBatchOperationBySlot.setStatus("current")
_HpnicfEponBatchOperationBySlotResult_Type = Integer32
_HpnicfEponBatchOperationBySlotResult_Object = MibTableColumn
hpnicfEponBatchOperationBySlotResult = _HpnicfEponBatchOperationBySlotResult_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 6, 1, 1, 4),
    _HpnicfEponBatchOperationBySlotResult_Type()
)
hpnicfEponBatchOperationBySlotResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponBatchOperationBySlotResult.setStatus("current")
_HpnicfEponBatchOperationByOLTTable_Object = MibTable
hpnicfEponBatchOperationByOLTTable = _HpnicfEponBatchOperationByOLTTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 6, 2)
)
if mibBuilder.loadTexts:
    hpnicfEponBatchOperationByOLTTable.setStatus("current")
_HpnicfEponBatchOperationByOLTEntry_Object = MibTableRow
hpnicfEponBatchOperationByOLTEntry = _HpnicfEponBatchOperationByOLTEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 6, 2, 1)
)
hpnicfEponBatchOperationByOLTEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEponBatchOperationByOLTEntry.setStatus("current")


class _HpnicfEponBatchOperationByOLTType_Type(Integer32):
    """Custom type hpnicfEponBatchOperationByOLTType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5)
        )
    )
    namedValues = NamedValues(
        *(("resetUnknown", 1),
          ("updateONU", 5))
    )


_HpnicfEponBatchOperationByOLTType_Type.__name__ = "Integer32"
_HpnicfEponBatchOperationByOLTType_Object = MibTableColumn
hpnicfEponBatchOperationByOLTType = _HpnicfEponBatchOperationByOLTType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 6, 2, 1, 1),
    _HpnicfEponBatchOperationByOLTType_Type()
)
hpnicfEponBatchOperationByOLTType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponBatchOperationByOLTType.setStatus("current")


class _HpnicfEponBatchOperationByOLT_Type(Integer32):
    """Custom type hpnicfEponBatchOperationByOLT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("batOpByOlt", 1)
    )


_HpnicfEponBatchOperationByOLT_Type.__name__ = "Integer32"
_HpnicfEponBatchOperationByOLT_Object = MibTableColumn
hpnicfEponBatchOperationByOLT = _HpnicfEponBatchOperationByOLT_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 6, 2, 1, 2),
    _HpnicfEponBatchOperationByOLT_Type()
)
hpnicfEponBatchOperationByOLT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponBatchOperationByOLT.setStatus("current")
_HpnicfEponBatchOperationByOLTResult_Type = Integer32
_HpnicfEponBatchOperationByOLTResult_Object = MibTableColumn
hpnicfEponBatchOperationByOLTResult = _HpnicfEponBatchOperationByOLTResult_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 6, 2, 1, 3),
    _HpnicfEponBatchOperationByOLTResult_Type()
)
hpnicfEponBatchOperationByOLTResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponBatchOperationByOLTResult.setStatus("current")
_HpnicfOnuFirmwareUpdateByTypeTable_Object = MibTable
hpnicfOnuFirmwareUpdateByTypeTable = _HpnicfOnuFirmwareUpdateByTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 6, 3)
)
if mibBuilder.loadTexts:
    hpnicfOnuFirmwareUpdateByTypeTable.setStatus("current")
_HpnicfOnuFirmwareUpdateByTypeEntry_Object = MibTableRow
hpnicfOnuFirmwareUpdateByTypeEntry = _HpnicfOnuFirmwareUpdateByTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 6, 3, 1)
)
hpnicfOnuFirmwareUpdateByTypeEntry.setIndexNames(
    (0, "HPN-ICF-EPON-MIB", "hpnicfOnuUpdateByOnuTypeIndex"),
)
if mibBuilder.loadTexts:
    hpnicfOnuFirmwareUpdateByTypeEntry.setStatus("current")
_HpnicfOnuUpdateByOnuTypeIndex_Type = Integer32
_HpnicfOnuUpdateByOnuTypeIndex_Object = MibTableColumn
hpnicfOnuUpdateByOnuTypeIndex = _HpnicfOnuUpdateByOnuTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 6, 3, 1, 1),
    _HpnicfOnuUpdateByOnuTypeIndex_Type()
)
hpnicfOnuUpdateByOnuTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfOnuUpdateByOnuTypeIndex.setStatus("current")


class _HpnicfOnuUpdateByTypeOnuType_Type(OctetString):
    """Custom type hpnicfOnuUpdateByTypeOnuType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_HpnicfOnuUpdateByTypeOnuType_Type.__name__ = "OctetString"
_HpnicfOnuUpdateByTypeOnuType_Object = MibTableColumn
hpnicfOnuUpdateByTypeOnuType = _HpnicfOnuUpdateByTypeOnuType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 6, 3, 1, 2),
    _HpnicfOnuUpdateByTypeOnuType_Type()
)
hpnicfOnuUpdateByTypeOnuType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfOnuUpdateByTypeOnuType.setStatus("current")


class _HpnicfOnuUpdateByTypeFileName_Type(OctetString):
    """Custom type hpnicfOnuUpdateByTypeFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfOnuUpdateByTypeFileName_Type.__name__ = "OctetString"
_HpnicfOnuUpdateByTypeFileName_Object = MibTableColumn
hpnicfOnuUpdateByTypeFileName = _HpnicfOnuUpdateByTypeFileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 6, 3, 1, 3),
    _HpnicfOnuUpdateByTypeFileName_Type()
)
hpnicfOnuUpdateByTypeFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfOnuUpdateByTypeFileName.setStatus("current")
_HpnicfOnuUpdateByTypeRowStatus_Type = RowStatus
_HpnicfOnuUpdateByTypeRowStatus_Object = MibTableColumn
hpnicfOnuUpdateByTypeRowStatus = _HpnicfOnuUpdateByTypeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 6, 3, 1, 4),
    _HpnicfOnuUpdateByTypeRowStatus_Type()
)
hpnicfOnuUpdateByTypeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfOnuUpdateByTypeRowStatus.setStatus("current")
_HpnicfEponErrorInfo_ObjectIdentity = ObjectIdentity
hpnicfEponErrorInfo = _HpnicfEponErrorInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 7)
)
_HpnicfEponSoftwareErrorCode_Type = Integer32
_HpnicfEponSoftwareErrorCode_Object = MibScalar
hpnicfEponSoftwareErrorCode = _HpnicfEponSoftwareErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 7, 1),
    _HpnicfEponSoftwareErrorCode_Type()
)
hpnicfEponSoftwareErrorCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfEponSoftwareErrorCode.setStatus("current")
_HpnicfOamVendorSpecificAlarmCode_Type = Integer32
_HpnicfOamVendorSpecificAlarmCode_Object = MibScalar
hpnicfOamVendorSpecificAlarmCode = _HpnicfOamVendorSpecificAlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 7, 2),
    _HpnicfOamVendorSpecificAlarmCode_Type()
)
hpnicfOamVendorSpecificAlarmCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfOamVendorSpecificAlarmCode.setStatus("current")
_HpnicfEponOnuRegErrorMacAddr_Type = OctetString
_HpnicfEponOnuRegErrorMacAddr_Object = MibScalar
hpnicfEponOnuRegErrorMacAddr = _HpnicfEponOnuRegErrorMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 7, 3),
    _HpnicfEponOnuRegErrorMacAddr_Type()
)
hpnicfEponOnuRegErrorMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfEponOnuRegErrorMacAddr.setStatus("current")
_HpnicfOamEventLogType_Type = Unsigned32
_HpnicfOamEventLogType_Object = MibScalar
hpnicfOamEventLogType = _HpnicfOamEventLogType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 7, 4),
    _HpnicfOamEventLogType_Type()
)
hpnicfOamEventLogType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfOamEventLogType.setStatus("current")


class _HpnicfOamEventLogLocation_Type(Integer32):
    """Custom type hpnicfOamEventLogLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_HpnicfOamEventLogLocation_Type.__name__ = "Integer32"
_HpnicfOamEventLogLocation_Object = MibScalar
hpnicfOamEventLogLocation = _HpnicfOamEventLogLocation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 7, 5),
    _HpnicfOamEventLogLocation_Type()
)
hpnicfOamEventLogLocation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfOamEventLogLocation.setStatus("current")
_HpnicfEponLoopbackPortIndex_Type = Integer32
_HpnicfEponLoopbackPortIndex_Object = MibScalar
hpnicfEponLoopbackPortIndex = _HpnicfEponLoopbackPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 7, 6),
    _HpnicfEponLoopbackPortIndex_Type()
)
hpnicfEponLoopbackPortIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfEponLoopbackPortIndex.setStatus("current")


class _HpnicfEponLoopbackPortDescr_Type(OctetString):
    """Custom type hpnicfEponLoopbackPortDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfEponLoopbackPortDescr_Type.__name__ = "OctetString"
_HpnicfEponLoopbackPortDescr_Object = MibScalar
hpnicfEponLoopbackPortDescr = _HpnicfEponLoopbackPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 7, 7),
    _HpnicfEponLoopbackPortDescr_Type()
)
hpnicfEponLoopbackPortDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfEponLoopbackPortDescr.setStatus("current")
_HpnicfOltPortAlarmLlidMisFrames_Type = Unsigned32
_HpnicfOltPortAlarmLlidMisFrames_Object = MibScalar
hpnicfOltPortAlarmLlidMisFrames = _HpnicfOltPortAlarmLlidMisFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 7, 8),
    _HpnicfOltPortAlarmLlidMisFrames_Type()
)
hpnicfOltPortAlarmLlidMisFrames.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfOltPortAlarmLlidMisFrames.setStatus("current")
_HpnicfOltPortAlarmBer_Type = Unsigned32
_HpnicfOltPortAlarmBer_Object = MibScalar
hpnicfOltPortAlarmBer = _HpnicfOltPortAlarmBer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 7, 9),
    _HpnicfOltPortAlarmBer_Type()
)
hpnicfOltPortAlarmBer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfOltPortAlarmBer.setStatus("current")
_HpnicfOltPortAlarmFer_Type = Unsigned32
_HpnicfOltPortAlarmFer_Object = MibScalar
hpnicfOltPortAlarmFer = _HpnicfOltPortAlarmFer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 7, 10),
    _HpnicfOltPortAlarmFer_Type()
)
hpnicfOltPortAlarmFer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfOltPortAlarmFer.setStatus("current")
_HpnicfEponOnuRegSilentMac_Type = OctetString
_HpnicfEponOnuRegSilentMac_Object = MibScalar
hpnicfEponOnuRegSilentMac = _HpnicfEponOnuRegSilentMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 7, 11),
    _HpnicfEponOnuRegSilentMac_Type()
)
hpnicfEponOnuRegSilentMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfEponOnuRegSilentMac.setStatus("current")


class _HpnicfEponOperationResult_Type(OctetString):
    """Custom type hpnicfEponOperationResult based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfEponOperationResult_Type.__name__ = "OctetString"
_HpnicfEponOperationResult_Object = MibScalar
hpnicfEponOperationResult = _HpnicfEponOperationResult_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 7, 12),
    _HpnicfEponOperationResult_Type()
)
hpnicfEponOperationResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfEponOperationResult.setStatus("current")


class _HpnicfEponOnuLaserState_Type(Integer32):
    """Custom type hpnicfEponOnuLaserState based on Integer32"""
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
        *(("endOfLife", 4),
          ("laserAlwaysOn", 2),
          ("normal", 1),
          ("signalDegradation", 3))
    )


_HpnicfEponOnuLaserState_Type.__name__ = "Integer32"
_HpnicfEponOnuLaserState_Object = MibScalar
hpnicfEponOnuLaserState = _HpnicfEponOnuLaserState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 7, 13),
    _HpnicfEponOnuLaserState_Type()
)
hpnicfEponOnuLaserState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfEponOnuLaserState.setStatus("current")
_HpnicfEponTrap_ObjectIdentity = ObjectIdentity
hpnicfEponTrap = _HpnicfEponTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8)
)
_HpnicfEponTrapPrefix_ObjectIdentity = ObjectIdentity
hpnicfEponTrapPrefix = _HpnicfEponTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0)
)
_HpnicfEponStat_ObjectIdentity = ObjectIdentity
hpnicfEponStat = _HpnicfEponStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 9)
)
_HpnicfEponStatTable_Object = MibTable
hpnicfEponStatTable = _HpnicfEponStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 9, 1)
)
if mibBuilder.loadTexts:
    hpnicfEponStatTable.setStatus("current")
_HpnicfEponStatEntry_Object = MibTableRow
hpnicfEponStatEntry = _HpnicfEponStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 9, 1, 1)
)
hpnicfEponStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEponStatEntry.setStatus("current")
_HpnicfEponStatFER_Type = Counter64
_HpnicfEponStatFER_Object = MibTableColumn
hpnicfEponStatFER = _HpnicfEponStatFER_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 9, 1, 1, 1),
    _HpnicfEponStatFER_Type()
)
hpnicfEponStatFER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponStatFER.setStatus("current")
_HpnicfEponStatBER_Type = Counter64
_HpnicfEponStatBER_Object = MibTableColumn
hpnicfEponStatBER = _HpnicfEponStatBER_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 9, 1, 1, 2),
    _HpnicfEponStatBER_Type()
)
hpnicfEponStatBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponStatBER.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfEponPortAlarmBerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 1)
)
hpnicfEponPortAlarmBerTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HPN-ICF-EPON-MIB", "hpnicfOltPortAlarmBerDirect"),
        ("HPN-ICF-EPON-MIB", "hpnicfOltPortAlarmBer"),
        ("HPN-ICF-EPON-MIB", "hpnicfOltPortAlarmBerThreshold"))
)
if mibBuilder.loadTexts:
    hpnicfEponPortAlarmBerTrap.setStatus(
        "current"
    )

hpnicfEponPortAlarmFerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 2)
)
hpnicfEponPortAlarmFerTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HPN-ICF-EPON-MIB", "hpnicfOltPortAlarmFerDirect"),
        ("HPN-ICF-EPON-MIB", "hpnicfOltPortAlarmFer"),
        ("HPN-ICF-EPON-MIB", "hpnicfOltPortAlarmFerThreshold"))
)
if mibBuilder.loadTexts:
    hpnicfEponPortAlarmFerTrap.setStatus(
        "current"
    )

hpnicfEponErrorLLIDFrameTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 3)
)
hpnicfEponErrorLLIDFrameTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HPN-ICF-EPON-MIB", "hpnicfOltPortAlarmLlidMisFrames"),
        ("HPN-ICF-EPON-MIB", "hpnicfOltPortAlarmLlidMismatchThreshold"))
)
if mibBuilder.loadTexts:
    hpnicfEponErrorLLIDFrameTrap.setStatus(
        "current"
    )

hpnicfEponLoopBackEnableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 4)
)
hpnicfEponLoopBackEnableTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HPN-ICF-EPON-MIB", "hpnicfEponLoopbackPortIndex"),
        ("HPN-ICF-EPON-MIB", "hpnicfEponLoopbackPortDescr"))
)
if mibBuilder.loadTexts:
    hpnicfEponLoopBackEnableTrap.setStatus(
        "current"
    )

hpnicfEponOnuRegistrationErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 5)
)
hpnicfEponOnuRegistrationErrTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HPN-ICF-EPON-MIB", "hpnicfEponOnuRegErrorMacAddr"))
)
if mibBuilder.loadTexts:
    hpnicfEponOnuRegistrationErrTrap.setStatus(
        "current"
    )

hpnicfEponOamDisconnectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 6)
)
hpnicfEponOamDisconnectionTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfEponOamDisconnectionTrap.setStatus(
        "current"
    )

hpnicfEponEncryptionKeyErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 7)
)
hpnicfEponEncryptionKeyErrTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfEponEncryptionKeyErrTrap.setStatus(
        "current"
    )

hpnicfEponRemoteStableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 8)
)
hpnicfEponRemoteStableTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfEponRemoteStableTrap.setStatus(
        "current"
    )

hpnicfEponLocalStableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 9)
)
hpnicfEponLocalStableTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfEponLocalStableTrap.setStatus(
        "current"
    )

hpnicfEponOamVendorSpecificTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 10)
)
hpnicfEponOamVendorSpecificTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HPN-ICF-EPON-MIB", "hpnicfOamVendorSpecificAlarmCode"))
)
if mibBuilder.loadTexts:
    hpnicfEponOamVendorSpecificTrap.setStatus(
        "current"
    )

hpnicfEponSoftwareErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 11)
)
hpnicfEponSoftwareErrTrap.setObjects(
      *(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"),
        ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"),
        ("HPN-ICF-EPON-MIB", "hpnicfEponSoftwareErrorCode"))
)
if mibBuilder.loadTexts:
    hpnicfEponSoftwareErrTrap.setStatus(
        "current"
    )

hpnicfEponPortAlarmBerRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 12)
)
hpnicfEponPortAlarmBerRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HPN-ICF-EPON-MIB", "hpnicfOltPortAlarmBerDirect"))
)
if mibBuilder.loadTexts:
    hpnicfEponPortAlarmBerRecoverTrap.setStatus(
        "current"
    )

hpnicfEponPortAlarmFerRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 13)
)
hpnicfEponPortAlarmFerRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HPN-ICF-EPON-MIB", "hpnicfOltPortAlarmFerDirect"))
)
if mibBuilder.loadTexts:
    hpnicfEponPortAlarmFerRecoverTrap.setStatus(
        "current"
    )

hpnicfEponErrorLLIDFrameRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 14)
)
hpnicfEponErrorLLIDFrameRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfEponErrorLLIDFrameRecoverTrap.setStatus(
        "current"
    )

hpnicfEponLoopBackEnableRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 15)
)
hpnicfEponLoopBackEnableRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfEponLoopBackEnableRecoverTrap.setStatus(
        "current"
    )

hpnicfEponOnuRegistrationErrRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 16)
)
hpnicfEponOnuRegistrationErrRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HPN-ICF-EPON-MIB", "hpnicfEponOnuRegErrorMacAddr"))
)
if mibBuilder.loadTexts:
    hpnicfEponOnuRegistrationErrRecoverTrap.setStatus(
        "current"
    )

hpnicfEponOamDisconnectionRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 17)
)
hpnicfEponOamDisconnectionRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfEponOamDisconnectionRecoverTrap.setStatus(
        "current"
    )

hpnicfEponEncryptionKeyErrRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 18)
)
hpnicfEponEncryptionKeyErrRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfEponEncryptionKeyErrRecoverTrap.setStatus(
        "current"
    )

hpnicfEponRemoteStableRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 19)
)
hpnicfEponRemoteStableRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfEponRemoteStableRecoverTrap.setStatus(
        "current"
    )

hpnicfEponLocalStableRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 20)
)
hpnicfEponLocalStableRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfEponLocalStableRecoverTrap.setStatus(
        "current"
    )

hpnicfEponOamVendorSpecificRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 21)
)
hpnicfEponOamVendorSpecificRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HPN-ICF-EPON-MIB", "hpnicfOamVendorSpecificAlarmCode"))
)
if mibBuilder.loadTexts:
    hpnicfEponOamVendorSpecificRecoverTrap.setStatus(
        "current"
    )

hpnicfEponSoftwareErrRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 22)
)
hpnicfEponSoftwareErrRecoverTrap.setObjects(
      *(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"),
        ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"),
        ("HPN-ICF-EPON-MIB", "hpnicfEponSoftwareErrorCode"))
)
if mibBuilder.loadTexts:
    hpnicfEponSoftwareErrRecoverTrap.setStatus(
        "current"
    )

hpnicfDot3OamThresholdRecoverEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 23)
)
hpnicfDot3OamThresholdRecoverEvent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HPN-ICF-EPON-MIB", "hpnicfOamEventLogType"),
        ("HPN-ICF-EPON-MIB", "hpnicfOamEventLogLocation"))
)
if mibBuilder.loadTexts:
    hpnicfDot3OamThresholdRecoverEvent.setStatus(
        "current"
    )

hpnicfDot3OamNonThresholdRecoverEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 24)
)
hpnicfDot3OamNonThresholdRecoverEvent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HPN-ICF-EPON-MIB", "hpnicfOamEventLogType"),
        ("HPN-ICF-EPON-MIB", "hpnicfOamEventLogLocation"))
)
if mibBuilder.loadTexts:
    hpnicfDot3OamNonThresholdRecoverEvent.setStatus(
        "current"
    )

hpnicfEponOnuRegExcessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 25)
)
hpnicfEponOnuRegExcessTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfEponOnuRegExcessTrap.setStatus(
        "current"
    )

hpnicfEponOnuRegExcessRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 26)
)
hpnicfEponOnuRegExcessRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfEponOnuRegExcessRecoverTrap.setStatus(
        "current"
    )

hpnicfEponOnuPowerOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 27)
)
hpnicfEponOnuPowerOffTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfEponOnuPowerOffTrap.setStatus(
        "current"
    )

hpnicfEponOltSwitchoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 28)
)
hpnicfEponOltSwitchoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfEponOltSwitchoverTrap.setStatus(
        "current"
    )

hpnicfEponOltDFETrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 29)
)
hpnicfEponOltDFETrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfEponOltDFETrap.setStatus(
        "current"
    )

hpnicfEponOltDFERecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 30)
)
hpnicfEponOltDFERecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfEponOltDFERecoverTrap.setStatus(
        "current"
    )

hpnicfEponOnuSilenceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 31)
)
hpnicfEponOnuSilenceTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HPN-ICF-EPON-MIB", "hpnicfEponOnuRegSilentMac"))
)
if mibBuilder.loadTexts:
    hpnicfEponOnuSilenceTrap.setStatus(
        "current"
    )

hpnicfEponOnuSilenceRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 32)
)
hpnicfEponOnuSilenceRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HPN-ICF-EPON-MIB", "hpnicfEponOnuRegSilentMac"))
)
if mibBuilder.loadTexts:
    hpnicfEponOnuSilenceRecoverTrap.setStatus(
        "current"
    )

hpnicfEponOnuUpdateResultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 33)
)
hpnicfEponOnuUpdateResultTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HPN-ICF-EPON-MIB", "hpnicfOnuBindMacAddress"),
        ("HPN-ICF-EPON-MIB", "hpnicfOnuUpdateResult"),
        ("HPN-ICF-EPON-MIB", "hpnicfOnuRegType"),
        ("HPN-ICF-EPON-MIB", "hpnicfOnuUpdateFileName"))
)
if mibBuilder.loadTexts:
    hpnicfEponOnuUpdateResultTrap.setStatus(
        "current"
    )

hpnicfEponOnuAutoBindTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 34)
)
hpnicfEponOnuAutoBindTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HPN-ICF-EPON-MIB", "hpnicfOnuBindMacAddress"),
        ("HPN-ICF-EPON-MIB", "hpnicfEponOperationResult"))
)
if mibBuilder.loadTexts:
    hpnicfEponOnuAutoBindTrap.setStatus(
        "current"
    )

hpnicfEponOnuPortStpStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 35)
)
hpnicfEponOnuPortStpStateTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HPN-ICF-EPON-MIB", "hpnicfEponStpPortIndex"),
        ("HPN-ICF-EPON-MIB", "hpnicfEponStpPortDescr"),
        ("HPN-ICF-EPON-MIB", "hpnicfEponStpPortState"))
)
if mibBuilder.loadTexts:
    hpnicfEponOnuPortStpStateTrap.setStatus(
        "current"
    )

hpnicfEponOnuLaserFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 36)
)
hpnicfEponOnuLaserFailedTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HPN-ICF-EPON-MIB", "hpnicfEponOnuLaserState"))
)
if mibBuilder.loadTexts:
    hpnicfEponOnuLaserFailedTrap.setStatus(
        "current"
    )

hpnicfOnuSmlkSwitchoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 1, 8, 0, 37)
)
hpnicfOnuSmlkSwitchoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HPN-ICF-EPON-MIB", "hpnicfOnuSmlkGroupID"),
        ("HPN-ICF-EPON-MIB", "hpnicfOnuSmlkFirstPonStatus"),
        ("HPN-ICF-EPON-MIB", "hpnicfOnuSmlkSecondPonStatus"))
)
if mibBuilder.loadTexts:
    hpnicfOnuSmlkSwitchoverTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-EPON-MIB",
    **{"hpnicfEponMibObjects": hpnicfEponMibObjects,
       "hpnicfEponSysMan": hpnicfEponSysMan,
       "hpnicfEponAutoAuthorize": hpnicfEponAutoAuthorize,
       "hpnicfEponMonitorCycle": hpnicfEponMonitorCycle,
       "hpnicfEponMsgTimeOut": hpnicfEponMsgTimeOut,
       "hpnicfEponMsgLoseNum": hpnicfEponMsgLoseNum,
       "hpnicfEponSysHasEPONBoard": hpnicfEponSysHasEPONBoard,
       "hpnicfEponMonitorCycleEnable": hpnicfEponMonitorCycleEnable,
       "hpnicfEponOltSoftwareErrAlmEnable": hpnicfEponOltSoftwareErrAlmEnable,
       "hpnicfEponPortLoopBackAlmEnable": hpnicfEponPortLoopBackAlmEnable,
       "hpnicfEponMonitorCycleMinVal": hpnicfEponMonitorCycleMinVal,
       "hpnicfEponMonitorCycleMaxVal": hpnicfEponMonitorCycleMaxVal,
       "hpnicfEponMsgTimeOutMinVal": hpnicfEponMsgTimeOutMinVal,
       "hpnicfEponMsgTimeOutMaxVal": hpnicfEponMsgTimeOutMaxVal,
       "hpnicfEponMsgLoseNumMinVal": hpnicfEponMsgLoseNumMinVal,
       "hpnicfEponMsgLoseNumMaxVal": hpnicfEponMsgLoseNumMaxVal,
       "hpnicfEponSysScalarGroup": hpnicfEponSysScalarGroup,
       "hpnicfEponSysManTable": hpnicfEponSysManTable,
       "hpnicfEponSysManEntry": hpnicfEponSysManEntry,
       "hpnicfEponSlotIndex": hpnicfEponSlotIndex,
       "hpnicfEponModeSwitch": hpnicfEponModeSwitch,
       "hpnicfEponAutomaticMode": hpnicfEponAutomaticMode,
       "hpnicfEponOamDiscoveryTimeout": hpnicfEponOamDiscoveryTimeout,
       "hpnicfEponEncryptionNoReplyTimeOut": hpnicfEponEncryptionNoReplyTimeOut,
       "hpnicfEponEncryptionUpdateTime": hpnicfEponEncryptionUpdateTime,
       "hpnicfEponAutoBindStatus": hpnicfEponAutoBindStatus,
       "hpnicfEponAutoUpdateTable": hpnicfEponAutoUpdateTable,
       "hpnicfEponAutoUpdateEntry": hpnicfEponAutoUpdateEntry,
       "hpnicfEponAutoUpdateFileName": hpnicfEponAutoUpdateFileName,
       "hpnicfEponAutoUpdateSchedStatus": hpnicfEponAutoUpdateSchedStatus,
       "hpnicfEponAutoUpdateSchedTime": hpnicfEponAutoUpdateSchedTime,
       "hpnicfEponAutoUpdateSchedType": hpnicfEponAutoUpdateSchedType,
       "hpnicfEponAutoUpdateRealTimeStatus": hpnicfEponAutoUpdateRealTimeStatus,
       "hpnicfEponOuiIndexNextTable": hpnicfEponOuiIndexNextTable,
       "hpnicfEponOuiIndexNextEntry": hpnicfEponOuiIndexNextEntry,
       "hpnicfEponOuiIndexNext": hpnicfEponOuiIndexNext,
       "hpnicfEponOuiTable": hpnicfEponOuiTable,
       "hpnicfEponOuiEntry": hpnicfEponOuiEntry,
       "hpnicfEponOuiIndex": hpnicfEponOuiIndex,
       "hpnicfEponOuiValue": hpnicfEponOuiValue,
       "hpnicfEponOamVersion": hpnicfEponOamVersion,
       "hpnicfEponOuiRowStatus": hpnicfEponOuiRowStatus,
       "hpnicfEponMulticastControlTable": hpnicfEponMulticastControlTable,
       "hpnicfEponMulticastControlEntry": hpnicfEponMulticastControlEntry,
       "hpnicfEponMulticastVlanId": hpnicfEponMulticastVlanId,
       "hpnicfEponMulticastAddressList": hpnicfEponMulticastAddressList,
       "hpnicfEponMulticastStatus": hpnicfEponMulticastStatus,
       "hpnicfEponFileName": hpnicfEponFileName,
       "hpnicfEponDbaUpdateFileName": hpnicfEponDbaUpdateFileName,
       "hpnicfEponOnuUpdateFileName": hpnicfEponOnuUpdateFileName,
       "hpnicfEponOltMan": hpnicfEponOltMan,
       "hpnicfOltSysManTable": hpnicfOltSysManTable,
       "hpnicfOltSysManEntry": hpnicfOltSysManEntry,
       "hpnicfOltLaserOnTime": hpnicfOltLaserOnTime,
       "hpnicfOltLaserOffTime": hpnicfOltLaserOffTime,
       "hpnicfOltMultiCopyBrdCast": hpnicfOltMultiCopyBrdCast,
       "hpnicfOltEnableDiscardPacket": hpnicfOltEnableDiscardPacket,
       "hpnicfOltSelfTest": hpnicfOltSelfTest,
       "hpnicfOltSelfTestResult": hpnicfOltSelfTestResult,
       "hpnicfOltMaxRtt": hpnicfOltMaxRtt,
       "hpnicfOltInfoTable": hpnicfOltInfoTable,
       "hpnicfOltInfoEntry": hpnicfOltInfoEntry,
       "hpnicfOltFirmMajorVersion": hpnicfOltFirmMajorVersion,
       "hpnicfOltFirmMinorVersion": hpnicfOltFirmMinorVersion,
       "hpnicfOltHardMajorVersion": hpnicfOltHardMajorVersion,
       "hpnicfOltHardMinorVersion": hpnicfOltHardMinorVersion,
       "hpnicfOltAgcLockTime": hpnicfOltAgcLockTime,
       "hpnicfOltAgcCdrTime": hpnicfOltAgcCdrTime,
       "hpnicfOltMacAddress": hpnicfOltMacAddress,
       "hpnicfOltWorkMode": hpnicfOltWorkMode,
       "hpnicfOltOpticalPowerTx": hpnicfOltOpticalPowerTx,
       "hpnicfOltOpticalPowerRx": hpnicfOltOpticalPowerRx,
       "hpnicfOltDbaManTable": hpnicfOltDbaManTable,
       "hpnicfOltDbaManEntry": hpnicfOltDbaManEntry,
       "hpnicfOltDbaEnabledType": hpnicfOltDbaEnabledType,
       "hpnicfOltDbaDiscoveryLength": hpnicfOltDbaDiscoveryLength,
       "hpnicfOltDbaDiscovryFrequency": hpnicfOltDbaDiscovryFrequency,
       "hpnicfOltDbaCycleLength": hpnicfOltDbaCycleLength,
       "hpnicfOltDbaVersion": hpnicfOltDbaVersion,
       "hpnicfOltDbaUpdate": hpnicfOltDbaUpdate,
       "hpnicfOltDbaUpdateResult": hpnicfOltDbaUpdateResult,
       "hpnicfOltPortAlarmThresholdTable": hpnicfOltPortAlarmThresholdTable,
       "hpnicfOltPortAlarmThresholdEntry": hpnicfOltPortAlarmThresholdEntry,
       "hpnicfOltPortAlarmBerEnabled": hpnicfOltPortAlarmBerEnabled,
       "hpnicfOltPortAlarmBerDirect": hpnicfOltPortAlarmBerDirect,
       "hpnicfOltPortAlarmBerThreshold": hpnicfOltPortAlarmBerThreshold,
       "hpnicfOltPortAlarmFerEnabled": hpnicfOltPortAlarmFerEnabled,
       "hpnicfOltPortAlarmFerDirect": hpnicfOltPortAlarmFerDirect,
       "hpnicfOltPortAlarmFerThreshold": hpnicfOltPortAlarmFerThreshold,
       "hpnicfOltPortAlarmLlidMismatchEnabled": hpnicfOltPortAlarmLlidMismatchEnabled,
       "hpnicfOltPortAlarmLlidMismatchThreshold": hpnicfOltPortAlarmLlidMismatchThreshold,
       "hpnicfOltPortAlarmRemoteStableEnabled": hpnicfOltPortAlarmRemoteStableEnabled,
       "hpnicfOltPortAlarmLocalStableEnabled": hpnicfOltPortAlarmLocalStableEnabled,
       "hpnicfOltPortAlarmRegistrationEnabled": hpnicfOltPortAlarmRegistrationEnabled,
       "hpnicfOltPortAlarmOamDisconnectionEnabled": hpnicfOltPortAlarmOamDisconnectionEnabled,
       "hpnicfOltPortAlarmEncryptionKeyEnabled": hpnicfOltPortAlarmEncryptionKeyEnabled,
       "hpnicfOltPortAlarmVendorSpecificEnabled": hpnicfOltPortAlarmVendorSpecificEnabled,
       "hpnicfOltPortAlarmRegExcessEnabled": hpnicfOltPortAlarmRegExcessEnabled,
       "hpnicfOltPortAlarmDFEEnabled": hpnicfOltPortAlarmDFEEnabled,
       "hpnicfOltLaserOnTimeMinVal": hpnicfOltLaserOnTimeMinVal,
       "hpnicfOltLaserOnTimeMaxVal": hpnicfOltLaserOnTimeMaxVal,
       "hpnicfOltLaserOffTimeMinVal": hpnicfOltLaserOffTimeMinVal,
       "hpnicfOltLaserOffTimeMaxVal": hpnicfOltLaserOffTimeMaxVal,
       "hpnicfOltDbaDiscoveryLengthMinVal": hpnicfOltDbaDiscoveryLengthMinVal,
       "hpnicfOltDbaDiscoveryLengthMaxVal": hpnicfOltDbaDiscoveryLengthMaxVal,
       "hpnicfOltDbaDiscovryFrequencyMinVal": hpnicfOltDbaDiscovryFrequencyMinVal,
       "hpnicfOltDbaDiscovryFrequencyMaxVal": hpnicfOltDbaDiscovryFrequencyMaxVal,
       "hpnicfOltDbaCycleLengthMinVal": hpnicfOltDbaCycleLengthMinVal,
       "hpnicfOltDbaCycleLengthMaxVal": hpnicfOltDbaCycleLengthMaxVal,
       "hpnicfOltPortAlarmLlidMisMinVal": hpnicfOltPortAlarmLlidMisMinVal,
       "hpnicfOltPortAlarmLlidMisMaxVal": hpnicfOltPortAlarmLlidMisMaxVal,
       "hpnicfOltPortAlarmBerMinVal": hpnicfOltPortAlarmBerMinVal,
       "hpnicfOltPortAlarmBerMaxVal": hpnicfOltPortAlarmBerMaxVal,
       "hpnicfOltPortAlarmFerMinVal": hpnicfOltPortAlarmFerMinVal,
       "hpnicfOltPortAlarmFerMaxVal": hpnicfOltPortAlarmFerMaxVal,
       "hpnicfOnuSilentTable": hpnicfOnuSilentTable,
       "hpnicfOnuSilentEntry": hpnicfOnuSilentEntry,
       "hpnicfOnuSilentMacAddr": hpnicfOnuSilentMacAddr,
       "hpnicfOnuSilentTime": hpnicfOnuSilentTime,
       "hpnicfOltUsingOnuTable": hpnicfOltUsingOnuTable,
       "hpnicfOltUsingOnuEntry": hpnicfOltUsingOnuEntry,
       "hpnicfOltUsingOnuNum": hpnicfOltUsingOnuNum,
       "hpnicfOltUsingOnuIfIndex": hpnicfOltUsingOnuIfIndex,
       "hpnicfOltUsingOnuRowStatus": hpnicfOltUsingOnuRowStatus,
       "hpnicfEponOnuMan": hpnicfEponOnuMan,
       "hpnicfOnuSysManTable": hpnicfOnuSysManTable,
       "hpnicfOnuSysManEntry": hpnicfOnuSysManEntry,
       "hpnicfOnuEncryptMan": hpnicfOnuEncryptMan,
       "hpnicfOnuReAuthorize": hpnicfOnuReAuthorize,
       "hpnicfOnuMulticastFilterStatus": hpnicfOnuMulticastFilterStatus,
       "hpnicfOnuDbaReportQueueSetNumber": hpnicfOnuDbaReportQueueSetNumber,
       "hpnicfOnuRemoteFecStatus": hpnicfOnuRemoteFecStatus,
       "hpnicfOnuPortBerStatus": hpnicfOnuPortBerStatus,
       "hpnicfOnuReset": hpnicfOnuReset,
       "hpnicfOnuMulticastControlMode": hpnicfOnuMulticastControlMode,
       "hpnicfOnuAccessVlan": hpnicfOnuAccessVlan,
       "hpnicfOnuEncryptKey": hpnicfOnuEncryptKey,
       "hpnicfOnuUniUpDownTrapStatus": hpnicfOnuUniUpDownTrapStatus,
       "hpnicfOnuFecStatus": hpnicfOnuFecStatus,
       "hpnicfOnuMcastCtrlHostAgingTime": hpnicfOnuMcastCtrlHostAgingTime,
       "hpnicfOnuMulticastFastLeaveEnable": hpnicfOnuMulticastFastLeaveEnable,
       "hpnicfOnuPortIsolateEnable": hpnicfOnuPortIsolateEnable,
       "hpnicfOnuLinkTestTable": hpnicfOnuLinkTestTable,
       "hpnicfOnuLinkTestEntry": hpnicfOnuLinkTestEntry,
       "hpnicfOnuLinkTestFrameNum": hpnicfOnuLinkTestFrameNum,
       "hpnicfOnuLinkTestFrameSize": hpnicfOnuLinkTestFrameSize,
       "hpnicfOnuLinkTestDelay": hpnicfOnuLinkTestDelay,
       "hpnicfOnuLinkTestVlanTag": hpnicfOnuLinkTestVlanTag,
       "hpnicfOnuLinkTestVlanPriority": hpnicfOnuLinkTestVlanPriority,
       "hpnicfOnuLinkTestVlanTagID": hpnicfOnuLinkTestVlanTagID,
       "hpnicfOnuLinkTestResultSentFrameNum": hpnicfOnuLinkTestResultSentFrameNum,
       "hpnicfOnuLinkTestResultRetFrameNum": hpnicfOnuLinkTestResultRetFrameNum,
       "hpnicfOnuLinkTestResultRetErrFrameNum": hpnicfOnuLinkTestResultRetErrFrameNum,
       "hpnicfOnuLinkTestResultMinDelay": hpnicfOnuLinkTestResultMinDelay,
       "hpnicfOnuLinkTestResultMeanDelay": hpnicfOnuLinkTestResultMeanDelay,
       "hpnicfOnuLinkTestResultMaxDelay": hpnicfOnuLinkTestResultMaxDelay,
       "hpnicfOnuBandWidthTable": hpnicfOnuBandWidthTable,
       "hpnicfOnuBandWidthEntry": hpnicfOnuBandWidthEntry,
       "hpnicfOnuDownStreamBandWidthPolicy": hpnicfOnuDownStreamBandWidthPolicy,
       "hpnicfOnuDownStreamMaxBandWidth": hpnicfOnuDownStreamMaxBandWidth,
       "hpnicfOnuDownStreamMaxBurstSize": hpnicfOnuDownStreamMaxBurstSize,
       "hpnicfOnuDownStreamHighPriorityFirst": hpnicfOnuDownStreamHighPriorityFirst,
       "hpnicfOnuDownStreamShortFrameFirst": hpnicfOnuDownStreamShortFrameFirst,
       "hpnicfOnuP2PBandWidthPolicy": hpnicfOnuP2PBandWidthPolicy,
       "hpnicfOnuP2PMaxBandWidth": hpnicfOnuP2PMaxBandWidth,
       "hpnicfOnuP2PMaxBurstSize": hpnicfOnuP2PMaxBurstSize,
       "hpnicfOnuP2PHighPriorityFirst": hpnicfOnuP2PHighPriorityFirst,
       "hpnicfOnuP2PShortFrameFirst": hpnicfOnuP2PShortFrameFirst,
       "hpnicfOnuSlaManTable": hpnicfOnuSlaManTable,
       "hpnicfOnuSlaManEntry": hpnicfOnuSlaManEntry,
       "hpnicfOnuSlaMaxBandWidth": hpnicfOnuSlaMaxBandWidth,
       "hpnicfOnuSlaMinBandWidth": hpnicfOnuSlaMinBandWidth,
       "hpnicfOnuSlaBandWidthStepVal": hpnicfOnuSlaBandWidthStepVal,
       "hpnicfOnuSlaDelay": hpnicfOnuSlaDelay,
       "hpnicfOnuSlaFixedBandWidth": hpnicfOnuSlaFixedBandWidth,
       "hpnicfOnuSlaPriorityClass": hpnicfOnuSlaPriorityClass,
       "hpnicfOnuSlaFixedPacketSize": hpnicfOnuSlaFixedPacketSize,
       "hpnicfOnuInfoTable": hpnicfOnuInfoTable,
       "hpnicfOnuInfoEntry": hpnicfOnuInfoEntry,
       "hpnicfOnuHardMajorVersion": hpnicfOnuHardMajorVersion,
       "hpnicfOnuHardMinorVersion": hpnicfOnuHardMinorVersion,
       "hpnicfOnuSoftwareVersion": hpnicfOnuSoftwareVersion,
       "hpnicfOnuUniMacType": hpnicfOnuUniMacType,
       "hpnicfOnuLaserOnTime": hpnicfOnuLaserOnTime,
       "hpnicfOnuLaserOffTime": hpnicfOnuLaserOffTime,
       "hpnicfOnuGrantFifoDep": hpnicfOnuGrantFifoDep,
       "hpnicfOnuWorkMode": hpnicfOnuWorkMode,
       "hpnicfOnuPCBVersion": hpnicfOnuPCBVersion,
       "hpnicfOnuRtt": hpnicfOnuRtt,
       "hpnicfOnuEEPROMVersion": hpnicfOnuEEPROMVersion,
       "hpnicfOnuRegType": hpnicfOnuRegType,
       "hpnicfOnuHostType": hpnicfOnuHostType,
       "hpnicfOnuDistance": hpnicfOnuDistance,
       "hpnicfOnuLlid": hpnicfOnuLlid,
       "hpnicfOnuVendorId": hpnicfOnuVendorId,
       "hpnicfOnuFirmwareVersion": hpnicfOnuFirmwareVersion,
       "hpnicfOnuOpticalPowerReceivedByOlt": hpnicfOnuOpticalPowerReceivedByOlt,
       "hpnicfOnuMacAddrInfoTable": hpnicfOnuMacAddrInfoTable,
       "hpnicfOnuMacAddrInfoEntry": hpnicfOnuMacAddrInfoEntry,
       "hpnicfOnuMacIndex": hpnicfOnuMacIndex,
       "hpnicfOnuMacAddrFlag": hpnicfOnuMacAddrFlag,
       "hpnicfOnuMacAddress": hpnicfOnuMacAddress,
       "hpnicfOnuBindMacAddrTable": hpnicfOnuBindMacAddrTable,
       "hpnicfOnuBindMacAddrEntry": hpnicfOnuBindMacAddrEntry,
       "hpnicfOnuBindMacAddress": hpnicfOnuBindMacAddress,
       "hpnicfOnuBindType": hpnicfOnuBindType,
       "hpnicfOnuFirmwareUpdateTable": hpnicfOnuFirmwareUpdateTable,
       "hpnicfOnuFirmwareUpdateEntry": hpnicfOnuFirmwareUpdateEntry,
       "hpnicfOnuUpdate": hpnicfOnuUpdate,
       "hpnicfOnuUpdateResult": hpnicfOnuUpdateResult,
       "hpnicfOnuUpdateFileName": hpnicfOnuUpdateFileName,
       "hpnicfOnuLinkTestFrameNumMinVal": hpnicfOnuLinkTestFrameNumMinVal,
       "hpnicfOnuLinkTestFrameNumMaxVal": hpnicfOnuLinkTestFrameNumMaxVal,
       "hpnicfOnuSlaMaxBandWidthMinVal": hpnicfOnuSlaMaxBandWidthMinVal,
       "hpnicfOnuSlaMaxBandWidthMaxVal": hpnicfOnuSlaMaxBandWidthMaxVal,
       "hpnicfOnuSlaMinBandWidthMinVal": hpnicfOnuSlaMinBandWidthMinVal,
       "hpnicfOnuSlaMinBandWidthMaxVal": hpnicfOnuSlaMinBandWidthMaxVal,
       "hpnicfEponOnuTypeManTable": hpnicfEponOnuTypeManTable,
       "hpnicfEponOnuTypeManEntry": hpnicfEponOnuTypeManEntry,
       "hpnicfEponOnuTypeIndex": hpnicfEponOnuTypeIndex,
       "hpnicfEponOnuTypeDescr": hpnicfEponOnuTypeDescr,
       "hpnicfOnuPacketManTable": hpnicfOnuPacketManTable,
       "hpnicfOnuPacketManEntry": hpnicfOnuPacketManEntry,
       "hpnicfOnuPriorityTrust": hpnicfOnuPriorityTrust,
       "hpnicfOnuQueueScheduler": hpnicfOnuQueueScheduler,
       "hpnicfOnuProtocolTable": hpnicfOnuProtocolTable,
       "hpnicfOnuProtocolEntry": hpnicfOnuProtocolEntry,
       "hpnicfOnuStpStatus": hpnicfOnuStpStatus,
       "hpnicfOnuIgmpSnoopingStatus": hpnicfOnuIgmpSnoopingStatus,
       "hpnicfOnuDhcpsnoopingOption82": hpnicfOnuDhcpsnoopingOption82,
       "hpnicfOnuDhcpsnooping": hpnicfOnuDhcpsnooping,
       "hpnicfOnuPppoe": hpnicfOnuPppoe,
       "hpnicfOnuIgmpSnoopingHostAgingT": hpnicfOnuIgmpSnoopingHostAgingT,
       "hpnicfOnuIgmpSnoopingMaxRespT": hpnicfOnuIgmpSnoopingMaxRespT,
       "hpnicfOnuIgmpSnoopingRouterAgingT": hpnicfOnuIgmpSnoopingRouterAgingT,
       "hpnicfOnuIgmpSnoopingAggReportS": hpnicfOnuIgmpSnoopingAggReportS,
       "hpnicfOnuIgmpSnoopingAggLeaveS": hpnicfOnuIgmpSnoopingAggLeaveS,
       "hpnicfOnuDot1xTable": hpnicfOnuDot1xTable,
       "hpnicfOnuDot1xEntry": hpnicfOnuDot1xEntry,
       "hpnicfOnuDot1xAccount": hpnicfOnuDot1xAccount,
       "hpnicfOnuDot1xPassword": hpnicfOnuDot1xPassword,
       "hpnicfOnuPriorityQueueTable": hpnicfOnuPriorityQueueTable,
       "hpnicfOnuPriorityQueueEntry": hpnicfOnuPriorityQueueEntry,
       "hpnicfOnuQueueDirection": hpnicfOnuQueueDirection,
       "hpnicfOnuQueueId": hpnicfOnuQueueId,
       "hpnicfOnuQueueSize": hpnicfOnuQueueSize,
       "hpnicfOnuCountTable": hpnicfOnuCountTable,
       "hpnicfOnuCountEntry": hpnicfOnuCountEntry,
       "hpnicfOnuInCRCErrPkts": hpnicfOnuInCRCErrPkts,
       "hpnicfOnuOutDroppedFrames": hpnicfOnuOutDroppedFrames,
       "hpnicfEponOnuScalarGroup": hpnicfEponOnuScalarGroup,
       "hpnicfOnuPriorityQueueSizeMinVal": hpnicfOnuPriorityQueueSizeMinVal,
       "hpnicfOnuPriorityQueueSizeMaxVal": hpnicfOnuPriorityQueueSizeMaxVal,
       "hpnicfOnuPriorityQueueBandwidthMinVal": hpnicfOnuPriorityQueueBandwidthMinVal,
       "hpnicfOnuPriorityQueueBandwidthMaxVal": hpnicfOnuPriorityQueueBandwidthMaxVal,
       "hpnicfOnuPriorityQueueBurstsizeMinVal": hpnicfOnuPriorityQueueBurstsizeMinVal,
       "hpnicfOnuPriorityQueueBurstsizeMaxVal": hpnicfOnuPriorityQueueBurstsizeMaxVal,
       "hpnicfOnuUpdateByTypeNextIndex": hpnicfOnuUpdateByTypeNextIndex,
       "hpnicfOnuQueueBandwidthTable": hpnicfOnuQueueBandwidthTable,
       "hpnicfOnuQueueBandwidthEntry": hpnicfOnuQueueBandwidthEntry,
       "hpnicfOnuQueueMaxBandwidth": hpnicfOnuQueueMaxBandwidth,
       "hpnicfOnuQueueMaxBurstsize": hpnicfOnuQueueMaxBurstsize,
       "hpnicfOnuQueuePolicyStatus": hpnicfOnuQueuePolicyStatus,
       "hpnicfOnuIpAddressTable": hpnicfOnuIpAddressTable,
       "hpnicfOnuIpAddressEntry": hpnicfOnuIpAddressEntry,
       "hpnicfOnuIpAddress": hpnicfOnuIpAddress,
       "hpnicfOnuIpAddressMask": hpnicfOnuIpAddressMask,
       "hpnicfOnuIpAddressGateway": hpnicfOnuIpAddressGateway,
       "hpnicfOnuDhcpallocate": hpnicfOnuDhcpallocate,
       "hpnicfOnuManageVID": hpnicfOnuManageVID,
       "hpnicfOnuManageVlanIntfS": hpnicfOnuManageVlanIntfS,
       "hpnicfOnuChipSetInfoTable": hpnicfOnuChipSetInfoTable,
       "hpnicfOnuChipSetInfoEntry": hpnicfOnuChipSetInfoEntry,
       "hpnicfOnuChipSetVendorId": hpnicfOnuChipSetVendorId,
       "hpnicfOnuChipSetModel": hpnicfOnuChipSetModel,
       "hpnicfOnuChipSetRevision": hpnicfOnuChipSetRevision,
       "hpnicfOnuChipSetDesignDate": hpnicfOnuChipSetDesignDate,
       "hpnicfOnuCapabilityTable": hpnicfOnuCapabilityTable,
       "hpnicfOnuCapabilityEntry": hpnicfOnuCapabilityEntry,
       "hpnicfOnuServiceSupported": hpnicfOnuServiceSupported,
       "hpnicfOnuGEPortNumber": hpnicfOnuGEPortNumber,
       "hpnicfOnuFEPortNumber": hpnicfOnuFEPortNumber,
       "hpnicfOnuPOTSPortNumber": hpnicfOnuPOTSPortNumber,
       "hpnicfOnuE1PortsNumber": hpnicfOnuE1PortsNumber,
       "hpnicfOnuUpstreamQueueNumber": hpnicfOnuUpstreamQueueNumber,
       "hpnicfOnuMaxUpstreamQueuePerPort": hpnicfOnuMaxUpstreamQueuePerPort,
       "hpnicfOnuDownstreamQueueNumber": hpnicfOnuDownstreamQueueNumber,
       "hpnicfOnuMaxDownstreamQueuePerPort": hpnicfOnuMaxDownstreamQueuePerPort,
       "hpnicfOnuBatteryBackup": hpnicfOnuBatteryBackup,
       "hpnicfOnuIgspFastLeaveSupported": hpnicfOnuIgspFastLeaveSupported,
       "hpnicfOnuMCtrlFastLeaveSupported": hpnicfOnuMCtrlFastLeaveSupported,
       "hpnicfOnuDbaReportTable": hpnicfOnuDbaReportTable,
       "hpnicfOnuDbaReportEntry": hpnicfOnuDbaReportEntry,
       "hpnicfOnuDbaReportQueueId": hpnicfOnuDbaReportQueueId,
       "hpnicfOnuDbaReportThreshold": hpnicfOnuDbaReportThreshold,
       "hpnicfOnuDbaReportStatus": hpnicfOnuDbaReportStatus,
       "hpnicfOnuCosToLocalPrecedenceTable": hpnicfOnuCosToLocalPrecedenceTable,
       "hpnicfOnuCosToLocalPrecedenceEntry": hpnicfOnuCosToLocalPrecedenceEntry,
       "hpnicfOnuCosToLocalPrecedenceCosIndex": hpnicfOnuCosToLocalPrecedenceCosIndex,
       "hpnicfOnuCosToLocalPrecedenceValue": hpnicfOnuCosToLocalPrecedenceValue,
       "hpnicfEponOnuStpPortTable": hpnicfEponOnuStpPortTable,
       "hpnicfEponOnuStpPortEntry": hpnicfEponOnuStpPortEntry,
       "hpnicfEponStpPortIndex": hpnicfEponStpPortIndex,
       "hpnicfEponStpPortDescr": hpnicfEponStpPortDescr,
       "hpnicfEponStpPortState": hpnicfEponStpPortState,
       "hpnicfOnuPhysicalTable": hpnicfOnuPhysicalTable,
       "hpnicfOnuPhysicalEntry": hpnicfOnuPhysicalEntry,
       "hpnicfOnuBridgeMac": hpnicfOnuBridgeMac,
       "hpnicfOnuFirstPonMac": hpnicfOnuFirstPonMac,
       "hpnicfOnuFirstPonRegState": hpnicfOnuFirstPonRegState,
       "hpnicfOnuSecondPonMac": hpnicfOnuSecondPonMac,
       "hpnicfOnuSecondPonRegState": hpnicfOnuSecondPonRegState,
       "hpnicfOnuSmlkTable": hpnicfOnuSmlkTable,
       "hpnicfOnuSmlkEntry": hpnicfOnuSmlkEntry,
       "hpnicfOnuSmlkGroupID": hpnicfOnuSmlkGroupID,
       "hpnicfOnuSmlkFirstPonRole": hpnicfOnuSmlkFirstPonRole,
       "hpnicfOnuSmlkFirstPonStatus": hpnicfOnuSmlkFirstPonStatus,
       "hpnicfOnuSmlkSecondPonRole": hpnicfOnuSmlkSecondPonRole,
       "hpnicfOnuSmlkSecondPonStatus": hpnicfOnuSmlkSecondPonStatus,
       "hpnicfOnuRS485PropertiesTable": hpnicfOnuRS485PropertiesTable,
       "hpnicfOnuRS485PropertiesEntry": hpnicfOnuRS485PropertiesEntry,
       "hpnicfOnuRS485SerialIndex": hpnicfOnuRS485SerialIndex,
       "hpnicfOnuRS485BaudRate": hpnicfOnuRS485BaudRate,
       "hpnicfOnuRS485DataBits": hpnicfOnuRS485DataBits,
       "hpnicfOnuRS485Parity": hpnicfOnuRS485Parity,
       "hpnicfOnuRS485StopBits": hpnicfOnuRS485StopBits,
       "hpnicfOnuRS485FlowControl": hpnicfOnuRS485FlowControl,
       "hpnicfOnuRS485TXOctets": hpnicfOnuRS485TXOctets,
       "hpnicfOnuRS485RXOctets": hpnicfOnuRS485RXOctets,
       "hpnicfOnuRS485TXErrOctets": hpnicfOnuRS485TXErrOctets,
       "hpnicfOnuRS485RXErrOctets": hpnicfOnuRS485RXErrOctets,
       "hpnicfOnuRS485ResetStatistics": hpnicfOnuRS485ResetStatistics,
       "hpnicfOnuRS485SessionSummaryTable": hpnicfOnuRS485SessionSummaryTable,
       "hpnicfOnuRS485SessionSummaryEntry": hpnicfOnuRS485SessionSummaryEntry,
       "hpnicfOnuRS485SessionMaxNum": hpnicfOnuRS485SessionMaxNum,
       "hpnicfOnuRS485SessionNextIndex": hpnicfOnuRS485SessionNextIndex,
       "hpnicfOnuRS485SessionTable": hpnicfOnuRS485SessionTable,
       "hpnicfOnuRS485SessionEntry": hpnicfOnuRS485SessionEntry,
       "hpnicfOnuRS485SessionIndex": hpnicfOnuRS485SessionIndex,
       "hpnicfOnuRS485SessionType": hpnicfOnuRS485SessionType,
       "hpnicfOnuRS485SessionAddType": hpnicfOnuRS485SessionAddType,
       "hpnicfOnuRS485SessionRemoteIP": hpnicfOnuRS485SessionRemoteIP,
       "hpnicfOnuRS485SessionRemotePort": hpnicfOnuRS485SessionRemotePort,
       "hpnicfOnuRS485SessionLocalPort": hpnicfOnuRS485SessionLocalPort,
       "hpnicfOnuRS485SessionRowStatus": hpnicfOnuRS485SessionRowStatus,
       "hpnicfOnuRS485SessionErrInfoTable": hpnicfOnuRS485SessionErrInfoTable,
       "hpnicfOnuRS485SessionErrInfoEntry": hpnicfOnuRS485SessionErrInfoEntry,
       "hpnicfOnuRS485SessionErrInfo": hpnicfOnuRS485SessionErrInfo,
       "hpnicfEponBatchOperationMan": hpnicfEponBatchOperationMan,
       "hpnicfEponBatchOperationBySlotTable": hpnicfEponBatchOperationBySlotTable,
       "hpnicfEponBatchOperationBySlotEntry": hpnicfEponBatchOperationBySlotEntry,
       "hpnicfEponBatchOperationBySlotIndex": hpnicfEponBatchOperationBySlotIndex,
       "hpnicfEponBatchOperationBySlotType": hpnicfEponBatchOperationBySlotType,
       "hpnicfEponBatchOperationBySlot": hpnicfEponBatchOperationBySlot,
       "hpnicfEponBatchOperationBySlotResult": hpnicfEponBatchOperationBySlotResult,
       "hpnicfEponBatchOperationByOLTTable": hpnicfEponBatchOperationByOLTTable,
       "hpnicfEponBatchOperationByOLTEntry": hpnicfEponBatchOperationByOLTEntry,
       "hpnicfEponBatchOperationByOLTType": hpnicfEponBatchOperationByOLTType,
       "hpnicfEponBatchOperationByOLT": hpnicfEponBatchOperationByOLT,
       "hpnicfEponBatchOperationByOLTResult": hpnicfEponBatchOperationByOLTResult,
       "hpnicfOnuFirmwareUpdateByTypeTable": hpnicfOnuFirmwareUpdateByTypeTable,
       "hpnicfOnuFirmwareUpdateByTypeEntry": hpnicfOnuFirmwareUpdateByTypeEntry,
       "hpnicfOnuUpdateByOnuTypeIndex": hpnicfOnuUpdateByOnuTypeIndex,
       "hpnicfOnuUpdateByTypeOnuType": hpnicfOnuUpdateByTypeOnuType,
       "hpnicfOnuUpdateByTypeFileName": hpnicfOnuUpdateByTypeFileName,
       "hpnicfOnuUpdateByTypeRowStatus": hpnicfOnuUpdateByTypeRowStatus,
       "hpnicfEponErrorInfo": hpnicfEponErrorInfo,
       "hpnicfEponSoftwareErrorCode": hpnicfEponSoftwareErrorCode,
       "hpnicfOamVendorSpecificAlarmCode": hpnicfOamVendorSpecificAlarmCode,
       "hpnicfEponOnuRegErrorMacAddr": hpnicfEponOnuRegErrorMacAddr,
       "hpnicfOamEventLogType": hpnicfOamEventLogType,
       "hpnicfOamEventLogLocation": hpnicfOamEventLogLocation,
       "hpnicfEponLoopbackPortIndex": hpnicfEponLoopbackPortIndex,
       "hpnicfEponLoopbackPortDescr": hpnicfEponLoopbackPortDescr,
       "hpnicfOltPortAlarmLlidMisFrames": hpnicfOltPortAlarmLlidMisFrames,
       "hpnicfOltPortAlarmBer": hpnicfOltPortAlarmBer,
       "hpnicfOltPortAlarmFer": hpnicfOltPortAlarmFer,
       "hpnicfEponOnuRegSilentMac": hpnicfEponOnuRegSilentMac,
       "hpnicfEponOperationResult": hpnicfEponOperationResult,
       "hpnicfEponOnuLaserState": hpnicfEponOnuLaserState,
       "hpnicfEponTrap": hpnicfEponTrap,
       "hpnicfEponTrapPrefix": hpnicfEponTrapPrefix,
       "hpnicfEponPortAlarmBerTrap": hpnicfEponPortAlarmBerTrap,
       "hpnicfEponPortAlarmFerTrap": hpnicfEponPortAlarmFerTrap,
       "hpnicfEponErrorLLIDFrameTrap": hpnicfEponErrorLLIDFrameTrap,
       "hpnicfEponLoopBackEnableTrap": hpnicfEponLoopBackEnableTrap,
       "hpnicfEponOnuRegistrationErrTrap": hpnicfEponOnuRegistrationErrTrap,
       "hpnicfEponOamDisconnectionTrap": hpnicfEponOamDisconnectionTrap,
       "hpnicfEponEncryptionKeyErrTrap": hpnicfEponEncryptionKeyErrTrap,
       "hpnicfEponRemoteStableTrap": hpnicfEponRemoteStableTrap,
       "hpnicfEponLocalStableTrap": hpnicfEponLocalStableTrap,
       "hpnicfEponOamVendorSpecificTrap": hpnicfEponOamVendorSpecificTrap,
       "hpnicfEponSoftwareErrTrap": hpnicfEponSoftwareErrTrap,
       "hpnicfEponPortAlarmBerRecoverTrap": hpnicfEponPortAlarmBerRecoverTrap,
       "hpnicfEponPortAlarmFerRecoverTrap": hpnicfEponPortAlarmFerRecoverTrap,
       "hpnicfEponErrorLLIDFrameRecoverTrap": hpnicfEponErrorLLIDFrameRecoverTrap,
       "hpnicfEponLoopBackEnableRecoverTrap": hpnicfEponLoopBackEnableRecoverTrap,
       "hpnicfEponOnuRegistrationErrRecoverTrap": hpnicfEponOnuRegistrationErrRecoverTrap,
       "hpnicfEponOamDisconnectionRecoverTrap": hpnicfEponOamDisconnectionRecoverTrap,
       "hpnicfEponEncryptionKeyErrRecoverTrap": hpnicfEponEncryptionKeyErrRecoverTrap,
       "hpnicfEponRemoteStableRecoverTrap": hpnicfEponRemoteStableRecoverTrap,
       "hpnicfEponLocalStableRecoverTrap": hpnicfEponLocalStableRecoverTrap,
       "hpnicfEponOamVendorSpecificRecoverTrap": hpnicfEponOamVendorSpecificRecoverTrap,
       "hpnicfEponSoftwareErrRecoverTrap": hpnicfEponSoftwareErrRecoverTrap,
       "hpnicfDot3OamThresholdRecoverEvent": hpnicfDot3OamThresholdRecoverEvent,
       "hpnicfDot3OamNonThresholdRecoverEvent": hpnicfDot3OamNonThresholdRecoverEvent,
       "hpnicfEponOnuRegExcessTrap": hpnicfEponOnuRegExcessTrap,
       "hpnicfEponOnuRegExcessRecoverTrap": hpnicfEponOnuRegExcessRecoverTrap,
       "hpnicfEponOnuPowerOffTrap": hpnicfEponOnuPowerOffTrap,
       "hpnicfEponOltSwitchoverTrap": hpnicfEponOltSwitchoverTrap,
       "hpnicfEponOltDFETrap": hpnicfEponOltDFETrap,
       "hpnicfEponOltDFERecoverTrap": hpnicfEponOltDFERecoverTrap,
       "hpnicfEponOnuSilenceTrap": hpnicfEponOnuSilenceTrap,
       "hpnicfEponOnuSilenceRecoverTrap": hpnicfEponOnuSilenceRecoverTrap,
       "hpnicfEponOnuUpdateResultTrap": hpnicfEponOnuUpdateResultTrap,
       "hpnicfEponOnuAutoBindTrap": hpnicfEponOnuAutoBindTrap,
       "hpnicfEponOnuPortStpStateTrap": hpnicfEponOnuPortStpStateTrap,
       "hpnicfEponOnuLaserFailedTrap": hpnicfEponOnuLaserFailedTrap,
       "hpnicfOnuSmlkSwitchoverTrap": hpnicfOnuSmlkSwitchoverTrap,
       "hpnicfEponStat": hpnicfEponStat,
       "hpnicfEponStatTable": hpnicfEponStatTable,
       "hpnicfEponStatEntry": hpnicfEponStatEntry,
       "hpnicfEponStatFER": hpnicfEponStatFER,
       "hpnicfEponStatBER": hpnicfEponStatBER}
)
