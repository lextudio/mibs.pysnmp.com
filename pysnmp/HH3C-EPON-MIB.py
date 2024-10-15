# SNMP MIB module (HH3C-EPON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-EPON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:09 2024
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

(hh3cLswFrameIndex,
 hh3cLswSlotIndex) = mibBuilder.importSymbols(
    "HH3C-LSW-DEV-ADM-MIB",
    "hh3cLswFrameIndex",
    "hh3cLswSlotIndex")

(hh3cEpon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cEpon")

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

hh3cEponMibObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cEponSysMan_ObjectIdentity = ObjectIdentity
hh3cEponSysMan = _Hh3cEponSysMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1)
)


class _Hh3cEponAutoAuthorize_Type(TruthValue):
    """Custom type hh3cEponAutoAuthorize based on TruthValue"""


_Hh3cEponAutoAuthorize_Object = MibScalar
hh3cEponAutoAuthorize = _Hh3cEponAutoAuthorize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 1),
    _Hh3cEponAutoAuthorize_Type()
)
hh3cEponAutoAuthorize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponAutoAuthorize.setStatus("current")
_Hh3cEponMonitorCycle_Type = Integer32
_Hh3cEponMonitorCycle_Object = MibScalar
hh3cEponMonitorCycle = _Hh3cEponMonitorCycle_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 2),
    _Hh3cEponMonitorCycle_Type()
)
hh3cEponMonitorCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponMonitorCycle.setStatus("current")


class _Hh3cEponMsgTimeOut_Type(Integer32):
    """Custom type hh3cEponMsgTimeOut based on Integer32"""
    defaultValue = 600


_Hh3cEponMsgTimeOut_Object = MibScalar
hh3cEponMsgTimeOut = _Hh3cEponMsgTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 3),
    _Hh3cEponMsgTimeOut_Type()
)
hh3cEponMsgTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponMsgTimeOut.setStatus("current")


class _Hh3cEponMsgLoseNum_Type(Integer32):
    """Custom type hh3cEponMsgLoseNum based on Integer32"""
    defaultValue = 20


_Hh3cEponMsgLoseNum_Object = MibScalar
hh3cEponMsgLoseNum = _Hh3cEponMsgLoseNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 4),
    _Hh3cEponMsgLoseNum_Type()
)
hh3cEponMsgLoseNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponMsgLoseNum.setStatus("current")
_Hh3cEponSysHasEPONBoard_Type = TruthValue
_Hh3cEponSysHasEPONBoard_Object = MibScalar
hh3cEponSysHasEPONBoard = _Hh3cEponSysHasEPONBoard_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 5),
    _Hh3cEponSysHasEPONBoard_Type()
)
hh3cEponSysHasEPONBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponSysHasEPONBoard.setStatus("current")


class _Hh3cEponMonitorCycleEnable_Type(TruthValue):
    """Custom type hh3cEponMonitorCycleEnable based on TruthValue"""


_Hh3cEponMonitorCycleEnable_Object = MibScalar
hh3cEponMonitorCycleEnable = _Hh3cEponMonitorCycleEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 6),
    _Hh3cEponMonitorCycleEnable_Type()
)
hh3cEponMonitorCycleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponMonitorCycleEnable.setStatus("current")


class _Hh3cEponOltSoftwareErrAlmEnable_Type(TruthValue):
    """Custom type hh3cEponOltSoftwareErrAlmEnable based on TruthValue"""


_Hh3cEponOltSoftwareErrAlmEnable_Object = MibScalar
hh3cEponOltSoftwareErrAlmEnable = _Hh3cEponOltSoftwareErrAlmEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 7),
    _Hh3cEponOltSoftwareErrAlmEnable_Type()
)
hh3cEponOltSoftwareErrAlmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponOltSoftwareErrAlmEnable.setStatus("current")


class _Hh3cEponPortLoopBackAlmEnable_Type(TruthValue):
    """Custom type hh3cEponPortLoopBackAlmEnable based on TruthValue"""


_Hh3cEponPortLoopBackAlmEnable_Object = MibScalar
hh3cEponPortLoopBackAlmEnable = _Hh3cEponPortLoopBackAlmEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 8),
    _Hh3cEponPortLoopBackAlmEnable_Type()
)
hh3cEponPortLoopBackAlmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponPortLoopBackAlmEnable.setStatus("current")
_Hh3cEponMonitorCycleMinVal_Type = Integer32
_Hh3cEponMonitorCycleMinVal_Object = MibScalar
hh3cEponMonitorCycleMinVal = _Hh3cEponMonitorCycleMinVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 9),
    _Hh3cEponMonitorCycleMinVal_Type()
)
hh3cEponMonitorCycleMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponMonitorCycleMinVal.setStatus("current")
_Hh3cEponMonitorCycleMaxVal_Type = Integer32
_Hh3cEponMonitorCycleMaxVal_Object = MibScalar
hh3cEponMonitorCycleMaxVal = _Hh3cEponMonitorCycleMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 10),
    _Hh3cEponMonitorCycleMaxVal_Type()
)
hh3cEponMonitorCycleMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponMonitorCycleMaxVal.setStatus("current")
_Hh3cEponMsgTimeOutMinVal_Type = Integer32
_Hh3cEponMsgTimeOutMinVal_Object = MibScalar
hh3cEponMsgTimeOutMinVal = _Hh3cEponMsgTimeOutMinVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 11),
    _Hh3cEponMsgTimeOutMinVal_Type()
)
hh3cEponMsgTimeOutMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponMsgTimeOutMinVal.setStatus("current")
_Hh3cEponMsgTimeOutMaxVal_Type = Integer32
_Hh3cEponMsgTimeOutMaxVal_Object = MibScalar
hh3cEponMsgTimeOutMaxVal = _Hh3cEponMsgTimeOutMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 12),
    _Hh3cEponMsgTimeOutMaxVal_Type()
)
hh3cEponMsgTimeOutMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponMsgTimeOutMaxVal.setStatus("current")
_Hh3cEponMsgLoseNumMinVal_Type = Integer32
_Hh3cEponMsgLoseNumMinVal_Object = MibScalar
hh3cEponMsgLoseNumMinVal = _Hh3cEponMsgLoseNumMinVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 13),
    _Hh3cEponMsgLoseNumMinVal_Type()
)
hh3cEponMsgLoseNumMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponMsgLoseNumMinVal.setStatus("current")
_Hh3cEponMsgLoseNumMaxVal_Type = Integer32
_Hh3cEponMsgLoseNumMaxVal_Object = MibScalar
hh3cEponMsgLoseNumMaxVal = _Hh3cEponMsgLoseNumMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 14),
    _Hh3cEponMsgLoseNumMaxVal_Type()
)
hh3cEponMsgLoseNumMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponMsgLoseNumMaxVal.setStatus("current")
_Hh3cEponSysScalarGroup_ObjectIdentity = ObjectIdentity
hh3cEponSysScalarGroup = _Hh3cEponSysScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 15)
)
_Hh3cEponSysManTable_Object = MibTable
hh3cEponSysManTable = _Hh3cEponSysManTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 16)
)
if mibBuilder.loadTexts:
    hh3cEponSysManTable.setStatus("current")
_Hh3cEponSysManEntry_Object = MibTableRow
hh3cEponSysManEntry = _Hh3cEponSysManEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 16, 1)
)
hh3cEponSysManEntry.setIndexNames(
    (0, "HH3C-EPON-MIB", "hh3cEponSlotIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponSysManEntry.setStatus("current")
_Hh3cEponSlotIndex_Type = Integer32
_Hh3cEponSlotIndex_Object = MibTableColumn
hh3cEponSlotIndex = _Hh3cEponSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 16, 1, 1),
    _Hh3cEponSlotIndex_Type()
)
hh3cEponSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEponSlotIndex.setStatus("current")


class _Hh3cEponModeSwitch_Type(Integer32):
    """Custom type hh3cEponModeSwitch based on Integer32"""
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


_Hh3cEponModeSwitch_Type.__name__ = "Integer32"
_Hh3cEponModeSwitch_Object = MibTableColumn
hh3cEponModeSwitch = _Hh3cEponModeSwitch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 16, 1, 2),
    _Hh3cEponModeSwitch_Type()
)
hh3cEponModeSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponModeSwitch.setStatus("current")


class _Hh3cEponAutomaticMode_Type(Integer32):
    """Custom type hh3cEponAutomaticMode based on Integer32"""
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


_Hh3cEponAutomaticMode_Type.__name__ = "Integer32"
_Hh3cEponAutomaticMode_Object = MibTableColumn
hh3cEponAutomaticMode = _Hh3cEponAutomaticMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 16, 1, 3),
    _Hh3cEponAutomaticMode_Type()
)
hh3cEponAutomaticMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponAutomaticMode.setStatus("current")


class _Hh3cEponOamDiscoveryTimeout_Type(Integer32):
    """Custom type hh3cEponOamDiscoveryTimeout based on Integer32"""
    defaultValue = 30


_Hh3cEponOamDiscoveryTimeout_Object = MibTableColumn
hh3cEponOamDiscoveryTimeout = _Hh3cEponOamDiscoveryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 16, 1, 4),
    _Hh3cEponOamDiscoveryTimeout_Type()
)
hh3cEponOamDiscoveryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponOamDiscoveryTimeout.setStatus("current")


class _Hh3cEponEncryptionNoReplyTimeOut_Type(Integer32):
    """Custom type hh3cEponEncryptionNoReplyTimeOut based on Integer32"""
    defaultValue = 30


_Hh3cEponEncryptionNoReplyTimeOut_Object = MibTableColumn
hh3cEponEncryptionNoReplyTimeOut = _Hh3cEponEncryptionNoReplyTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 16, 1, 5),
    _Hh3cEponEncryptionNoReplyTimeOut_Type()
)
hh3cEponEncryptionNoReplyTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponEncryptionNoReplyTimeOut.setStatus("current")


class _Hh3cEponEncryptionUpdateTime_Type(Integer32):
    """Custom type hh3cEponEncryptionUpdateTime based on Integer32"""
    defaultValue = 10


_Hh3cEponEncryptionUpdateTime_Object = MibTableColumn
hh3cEponEncryptionUpdateTime = _Hh3cEponEncryptionUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 16, 1, 6),
    _Hh3cEponEncryptionUpdateTime_Type()
)
hh3cEponEncryptionUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponEncryptionUpdateTime.setStatus("current")


class _Hh3cEponAutoBindStatus_Type(Integer32):
    """Custom type hh3cEponAutoBindStatus based on Integer32"""
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


_Hh3cEponAutoBindStatus_Type.__name__ = "Integer32"
_Hh3cEponAutoBindStatus_Object = MibTableColumn
hh3cEponAutoBindStatus = _Hh3cEponAutoBindStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 16, 1, 7),
    _Hh3cEponAutoBindStatus_Type()
)
hh3cEponAutoBindStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponAutoBindStatus.setStatus("current")
_Hh3cEponAutoUpdateTable_Object = MibTable
hh3cEponAutoUpdateTable = _Hh3cEponAutoUpdateTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 17)
)
if mibBuilder.loadTexts:
    hh3cEponAutoUpdateTable.setStatus("current")
_Hh3cEponAutoUpdateEntry_Object = MibTableRow
hh3cEponAutoUpdateEntry = _Hh3cEponAutoUpdateEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 17, 1)
)
hh3cEponAutoUpdateEntry.setIndexNames(
    (0, "HH3C-EPON-MIB", "hh3cEponSlotIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponAutoUpdateEntry.setStatus("current")


class _Hh3cEponAutoUpdateFileName_Type(DisplayString):
    """Custom type hh3cEponAutoUpdateFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cEponAutoUpdateFileName_Type.__name__ = "DisplayString"
_Hh3cEponAutoUpdateFileName_Object = MibTableColumn
hh3cEponAutoUpdateFileName = _Hh3cEponAutoUpdateFileName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 17, 1, 1),
    _Hh3cEponAutoUpdateFileName_Type()
)
hh3cEponAutoUpdateFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponAutoUpdateFileName.setStatus("current")


class _Hh3cEponAutoUpdateSchedStatus_Type(Integer32):
    """Custom type hh3cEponAutoUpdateSchedStatus based on Integer32"""
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


_Hh3cEponAutoUpdateSchedStatus_Type.__name__ = "Integer32"
_Hh3cEponAutoUpdateSchedStatus_Object = MibTableColumn
hh3cEponAutoUpdateSchedStatus = _Hh3cEponAutoUpdateSchedStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 17, 1, 2),
    _Hh3cEponAutoUpdateSchedStatus_Type()
)
hh3cEponAutoUpdateSchedStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponAutoUpdateSchedStatus.setStatus("current")


class _Hh3cEponAutoUpdateSchedTime_Type(OctetString):
    """Custom type hh3cEponAutoUpdateSchedTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cEponAutoUpdateSchedTime_Type.__name__ = "OctetString"
_Hh3cEponAutoUpdateSchedTime_Object = MibTableColumn
hh3cEponAutoUpdateSchedTime = _Hh3cEponAutoUpdateSchedTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 17, 1, 3),
    _Hh3cEponAutoUpdateSchedTime_Type()
)
hh3cEponAutoUpdateSchedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponAutoUpdateSchedTime.setStatus("current")


class _Hh3cEponAutoUpdateSchedType_Type(Integer32):
    """Custom type hh3cEponAutoUpdateSchedType based on Integer32"""
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


_Hh3cEponAutoUpdateSchedType_Type.__name__ = "Integer32"
_Hh3cEponAutoUpdateSchedType_Object = MibTableColumn
hh3cEponAutoUpdateSchedType = _Hh3cEponAutoUpdateSchedType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 17, 1, 4),
    _Hh3cEponAutoUpdateSchedType_Type()
)
hh3cEponAutoUpdateSchedType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponAutoUpdateSchedType.setStatus("current")


class _Hh3cEponAutoUpdateRealTimeStatus_Type(Integer32):
    """Custom type hh3cEponAutoUpdateRealTimeStatus based on Integer32"""
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


_Hh3cEponAutoUpdateRealTimeStatus_Type.__name__ = "Integer32"
_Hh3cEponAutoUpdateRealTimeStatus_Object = MibTableColumn
hh3cEponAutoUpdateRealTimeStatus = _Hh3cEponAutoUpdateRealTimeStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 17, 1, 5),
    _Hh3cEponAutoUpdateRealTimeStatus_Type()
)
hh3cEponAutoUpdateRealTimeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponAutoUpdateRealTimeStatus.setStatus("current")
_Hh3cEponOuiIndexNextTable_Object = MibTable
hh3cEponOuiIndexNextTable = _Hh3cEponOuiIndexNextTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 18)
)
if mibBuilder.loadTexts:
    hh3cEponOuiIndexNextTable.setStatus("current")
_Hh3cEponOuiIndexNextEntry_Object = MibTableRow
hh3cEponOuiIndexNextEntry = _Hh3cEponOuiIndexNextEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 18, 1)
)
hh3cEponOuiIndexNextEntry.setIndexNames(
    (0, "HH3C-EPON-MIB", "hh3cEponSlotIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponOuiIndexNextEntry.setStatus("current")
_Hh3cEponOuiIndexNext_Type = Integer32
_Hh3cEponOuiIndexNext_Object = MibTableColumn
hh3cEponOuiIndexNext = _Hh3cEponOuiIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 18, 1, 1),
    _Hh3cEponOuiIndexNext_Type()
)
hh3cEponOuiIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponOuiIndexNext.setStatus("current")
_Hh3cEponOuiTable_Object = MibTable
hh3cEponOuiTable = _Hh3cEponOuiTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 19)
)
if mibBuilder.loadTexts:
    hh3cEponOuiTable.setStatus("current")
_Hh3cEponOuiEntry_Object = MibTableRow
hh3cEponOuiEntry = _Hh3cEponOuiEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 19, 1)
)
hh3cEponOuiEntry.setIndexNames(
    (0, "HH3C-EPON-MIB", "hh3cEponSlotIndex"),
    (0, "HH3C-EPON-MIB", "hh3cEponOuiIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponOuiEntry.setStatus("current")
_Hh3cEponOuiIndex_Type = Integer32
_Hh3cEponOuiIndex_Object = MibTableColumn
hh3cEponOuiIndex = _Hh3cEponOuiIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 19, 1, 1),
    _Hh3cEponOuiIndex_Type()
)
hh3cEponOuiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEponOuiIndex.setStatus("current")


class _Hh3cEponOuiValue_Type(OctetString):
    """Custom type hh3cEponOuiValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_Hh3cEponOuiValue_Type.__name__ = "OctetString"
_Hh3cEponOuiValue_Object = MibTableColumn
hh3cEponOuiValue = _Hh3cEponOuiValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 19, 1, 2),
    _Hh3cEponOuiValue_Type()
)
hh3cEponOuiValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponOuiValue.setStatus("current")


class _Hh3cEponOamVersion_Type(OctetString):
    """Custom type hh3cEponOamVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cEponOamVersion_Type.__name__ = "OctetString"
_Hh3cEponOamVersion_Object = MibTableColumn
hh3cEponOamVersion = _Hh3cEponOamVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 19, 1, 3),
    _Hh3cEponOamVersion_Type()
)
hh3cEponOamVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponOamVersion.setStatus("current")
_Hh3cEponOuiRowStatus_Type = RowStatus
_Hh3cEponOuiRowStatus_Object = MibTableColumn
hh3cEponOuiRowStatus = _Hh3cEponOuiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 19, 1, 4),
    _Hh3cEponOuiRowStatus_Type()
)
hh3cEponOuiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponOuiRowStatus.setStatus("current")
_Hh3cEponMulticastControlTable_Object = MibTable
hh3cEponMulticastControlTable = _Hh3cEponMulticastControlTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 20)
)
if mibBuilder.loadTexts:
    hh3cEponMulticastControlTable.setStatus("current")
_Hh3cEponMulticastControlEntry_Object = MibTableRow
hh3cEponMulticastControlEntry = _Hh3cEponMulticastControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 20, 1)
)
hh3cEponMulticastControlEntry.setIndexNames(
    (0, "HH3C-EPON-MIB", "hh3cEponMulticastVlanId"),
)
if mibBuilder.loadTexts:
    hh3cEponMulticastControlEntry.setStatus("current")
_Hh3cEponMulticastVlanId_Type = Integer32
_Hh3cEponMulticastVlanId_Object = MibTableColumn
hh3cEponMulticastVlanId = _Hh3cEponMulticastVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 20, 1, 1),
    _Hh3cEponMulticastVlanId_Type()
)
hh3cEponMulticastVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEponMulticastVlanId.setStatus("current")


class _Hh3cEponMulticastAddressList_Type(OctetString):
    """Custom type hh3cEponMulticastAddressList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cEponMulticastAddressList_Type.__name__ = "OctetString"
_Hh3cEponMulticastAddressList_Object = MibTableColumn
hh3cEponMulticastAddressList = _Hh3cEponMulticastAddressList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 20, 1, 2),
    _Hh3cEponMulticastAddressList_Type()
)
hh3cEponMulticastAddressList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponMulticastAddressList.setStatus("current")
_Hh3cEponMulticastStatus_Type = RowStatus
_Hh3cEponMulticastStatus_Object = MibTableColumn
hh3cEponMulticastStatus = _Hh3cEponMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 1, 20, 1, 3),
    _Hh3cEponMulticastStatus_Type()
)
hh3cEponMulticastStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponMulticastStatus.setStatus("current")
_Hh3cEponFileName_ObjectIdentity = ObjectIdentity
hh3cEponFileName = _Hh3cEponFileName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 2)
)


class _Hh3cEponDbaUpdateFileName_Type(OctetString):
    """Custom type hh3cEponDbaUpdateFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cEponDbaUpdateFileName_Type.__name__ = "OctetString"
_Hh3cEponDbaUpdateFileName_Object = MibScalar
hh3cEponDbaUpdateFileName = _Hh3cEponDbaUpdateFileName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 2, 1),
    _Hh3cEponDbaUpdateFileName_Type()
)
hh3cEponDbaUpdateFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponDbaUpdateFileName.setStatus("current")


class _Hh3cEponOnuUpdateFileName_Type(OctetString):
    """Custom type hh3cEponOnuUpdateFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cEponOnuUpdateFileName_Type.__name__ = "OctetString"
_Hh3cEponOnuUpdateFileName_Object = MibScalar
hh3cEponOnuUpdateFileName = _Hh3cEponOnuUpdateFileName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 2, 2),
    _Hh3cEponOnuUpdateFileName_Type()
)
hh3cEponOnuUpdateFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponOnuUpdateFileName.setStatus("current")
_Hh3cEponOltMan_ObjectIdentity = ObjectIdentity
hh3cEponOltMan = _Hh3cEponOltMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3)
)
_Hh3cOltSysManTable_Object = MibTable
hh3cOltSysManTable = _Hh3cOltSysManTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cOltSysManTable.setStatus("current")
_Hh3cOltSysManEntry_Object = MibTableRow
hh3cOltSysManEntry = _Hh3cOltSysManEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 1, 1)
)
hh3cOltSysManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cOltSysManEntry.setStatus("current")


class _Hh3cOltLaserOnTime_Type(Integer32):
    """Custom type hh3cOltLaserOnTime based on Integer32"""
    defaultValue = 96


_Hh3cOltLaserOnTime_Object = MibTableColumn
hh3cOltLaserOnTime = _Hh3cOltLaserOnTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 1, 1, 1),
    _Hh3cOltLaserOnTime_Type()
)
hh3cOltLaserOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOltLaserOnTime.setStatus("current")


class _Hh3cOltLaserOffTime_Type(Integer32):
    """Custom type hh3cOltLaserOffTime based on Integer32"""
    defaultValue = 96


_Hh3cOltLaserOffTime_Object = MibTableColumn
hh3cOltLaserOffTime = _Hh3cOltLaserOffTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 1, 1, 2),
    _Hh3cOltLaserOffTime_Type()
)
hh3cOltLaserOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOltLaserOffTime.setStatus("current")


class _Hh3cOltMultiCopyBrdCast_Type(TruthValue):
    """Custom type hh3cOltMultiCopyBrdCast based on TruthValue"""


_Hh3cOltMultiCopyBrdCast_Object = MibTableColumn
hh3cOltMultiCopyBrdCast = _Hh3cOltMultiCopyBrdCast_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 1, 1, 3),
    _Hh3cOltMultiCopyBrdCast_Type()
)
hh3cOltMultiCopyBrdCast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOltMultiCopyBrdCast.setStatus("current")


class _Hh3cOltEnableDiscardPacket_Type(TruthValue):
    """Custom type hh3cOltEnableDiscardPacket based on TruthValue"""


_Hh3cOltEnableDiscardPacket_Object = MibTableColumn
hh3cOltEnableDiscardPacket = _Hh3cOltEnableDiscardPacket_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 1, 1, 4),
    _Hh3cOltEnableDiscardPacket_Type()
)
hh3cOltEnableDiscardPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOltEnableDiscardPacket.setStatus("current")


class _Hh3cOltSelfTest_Type(Integer32):
    """Custom type hh3cOltSelfTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("selftest", 1)
    )


_Hh3cOltSelfTest_Type.__name__ = "Integer32"
_Hh3cOltSelfTest_Object = MibTableColumn
hh3cOltSelfTest = _Hh3cOltSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 1, 1, 5),
    _Hh3cOltSelfTest_Type()
)
hh3cOltSelfTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOltSelfTest.setStatus("current")


class _Hh3cOltSelfTestResult_Type(Integer32):
    """Custom type hh3cOltSelfTestResult based on Integer32"""
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


_Hh3cOltSelfTestResult_Type.__name__ = "Integer32"
_Hh3cOltSelfTestResult_Object = MibTableColumn
hh3cOltSelfTestResult = _Hh3cOltSelfTestResult_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 1, 1, 6),
    _Hh3cOltSelfTestResult_Type()
)
hh3cOltSelfTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltSelfTestResult.setStatus("current")
_Hh3cOltMaxRtt_Type = Unsigned32
_Hh3cOltMaxRtt_Object = MibTableColumn
hh3cOltMaxRtt = _Hh3cOltMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 1, 1, 7),
    _Hh3cOltMaxRtt_Type()
)
hh3cOltMaxRtt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOltMaxRtt.setStatus("current")
_Hh3cOltInfoTable_Object = MibTable
hh3cOltInfoTable = _Hh3cOltInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cOltInfoTable.setStatus("current")
_Hh3cOltInfoEntry_Object = MibTableRow
hh3cOltInfoEntry = _Hh3cOltInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 2, 1)
)
hh3cOltInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cOltInfoEntry.setStatus("current")
_Hh3cOltFirmMajorVersion_Type = OctetString
_Hh3cOltFirmMajorVersion_Object = MibTableColumn
hh3cOltFirmMajorVersion = _Hh3cOltFirmMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 2, 1, 1),
    _Hh3cOltFirmMajorVersion_Type()
)
hh3cOltFirmMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltFirmMajorVersion.setStatus("current")
_Hh3cOltFirmMinorVersion_Type = OctetString
_Hh3cOltFirmMinorVersion_Object = MibTableColumn
hh3cOltFirmMinorVersion = _Hh3cOltFirmMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 2, 1, 2),
    _Hh3cOltFirmMinorVersion_Type()
)
hh3cOltFirmMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltFirmMinorVersion.setStatus("current")
_Hh3cOltHardMajorVersion_Type = OctetString
_Hh3cOltHardMajorVersion_Object = MibTableColumn
hh3cOltHardMajorVersion = _Hh3cOltHardMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 2, 1, 3),
    _Hh3cOltHardMajorVersion_Type()
)
hh3cOltHardMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltHardMajorVersion.setStatus("current")
_Hh3cOltHardMinorVersion_Type = OctetString
_Hh3cOltHardMinorVersion_Object = MibTableColumn
hh3cOltHardMinorVersion = _Hh3cOltHardMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 2, 1, 4),
    _Hh3cOltHardMinorVersion_Type()
)
hh3cOltHardMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltHardMinorVersion.setStatus("current")
_Hh3cOltAgcLockTime_Type = Integer32
_Hh3cOltAgcLockTime_Object = MibTableColumn
hh3cOltAgcLockTime = _Hh3cOltAgcLockTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 2, 1, 5),
    _Hh3cOltAgcLockTime_Type()
)
hh3cOltAgcLockTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltAgcLockTime.setStatus("current")
_Hh3cOltAgcCdrTime_Type = Integer32
_Hh3cOltAgcCdrTime_Object = MibTableColumn
hh3cOltAgcCdrTime = _Hh3cOltAgcCdrTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 2, 1, 6),
    _Hh3cOltAgcCdrTime_Type()
)
hh3cOltAgcCdrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltAgcCdrTime.setStatus("current")
_Hh3cOltMacAddress_Type = MacAddress
_Hh3cOltMacAddress_Object = MibTableColumn
hh3cOltMacAddress = _Hh3cOltMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 2, 1, 7),
    _Hh3cOltMacAddress_Type()
)
hh3cOltMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltMacAddress.setStatus("current")


class _Hh3cOltWorkMode_Type(Integer32):
    """Custom type hh3cOltWorkMode based on Integer32"""
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


_Hh3cOltWorkMode_Type.__name__ = "Integer32"
_Hh3cOltWorkMode_Object = MibTableColumn
hh3cOltWorkMode = _Hh3cOltWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 2, 1, 8),
    _Hh3cOltWorkMode_Type()
)
hh3cOltWorkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltWorkMode.setStatus("current")
_Hh3cOltOpticalPowerTx_Type = Integer32
_Hh3cOltOpticalPowerTx_Object = MibTableColumn
hh3cOltOpticalPowerTx = _Hh3cOltOpticalPowerTx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 2, 1, 9),
    _Hh3cOltOpticalPowerTx_Type()
)
hh3cOltOpticalPowerTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltOpticalPowerTx.setStatus("current")
_Hh3cOltOpticalPowerRx_Type = Integer32
_Hh3cOltOpticalPowerRx_Object = MibTableColumn
hh3cOltOpticalPowerRx = _Hh3cOltOpticalPowerRx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 2, 1, 10),
    _Hh3cOltOpticalPowerRx_Type()
)
hh3cOltOpticalPowerRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltOpticalPowerRx.setStatus("current")
_Hh3cOltDbaManTable_Object = MibTable
hh3cOltDbaManTable = _Hh3cOltDbaManTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hh3cOltDbaManTable.setStatus("current")
_Hh3cOltDbaManEntry_Object = MibTableRow
hh3cOltDbaManEntry = _Hh3cOltDbaManEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 3, 1)
)
hh3cOltDbaManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cOltDbaManEntry.setStatus("current")


class _Hh3cOltDbaEnabledType_Type(Integer32):
    """Custom type hh3cOltDbaEnabledType based on Integer32"""
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


_Hh3cOltDbaEnabledType_Type.__name__ = "Integer32"
_Hh3cOltDbaEnabledType_Object = MibTableColumn
hh3cOltDbaEnabledType = _Hh3cOltDbaEnabledType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 3, 1, 1),
    _Hh3cOltDbaEnabledType_Type()
)
hh3cOltDbaEnabledType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOltDbaEnabledType.setStatus("current")


class _Hh3cOltDbaDiscoveryLength_Type(Integer32):
    """Custom type hh3cOltDbaDiscoveryLength based on Integer32"""
    defaultValue = 41500


_Hh3cOltDbaDiscoveryLength_Object = MibTableColumn
hh3cOltDbaDiscoveryLength = _Hh3cOltDbaDiscoveryLength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 3, 1, 2),
    _Hh3cOltDbaDiscoveryLength_Type()
)
hh3cOltDbaDiscoveryLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOltDbaDiscoveryLength.setStatus("current")


class _Hh3cOltDbaDiscovryFrequency_Type(Integer32):
    """Custom type hh3cOltDbaDiscovryFrequency based on Integer32"""
    defaultValue = 50


_Hh3cOltDbaDiscovryFrequency_Object = MibTableColumn
hh3cOltDbaDiscovryFrequency = _Hh3cOltDbaDiscovryFrequency_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 3, 1, 3),
    _Hh3cOltDbaDiscovryFrequency_Type()
)
hh3cOltDbaDiscovryFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOltDbaDiscovryFrequency.setStatus("current")


class _Hh3cOltDbaCycleLength_Type(Integer32):
    """Custom type hh3cOltDbaCycleLength based on Integer32"""
    defaultValue = 65535


_Hh3cOltDbaCycleLength_Object = MibTableColumn
hh3cOltDbaCycleLength = _Hh3cOltDbaCycleLength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 3, 1, 4),
    _Hh3cOltDbaCycleLength_Type()
)
hh3cOltDbaCycleLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOltDbaCycleLength.setStatus("current")
_Hh3cOltDbaVersion_Type = OctetString
_Hh3cOltDbaVersion_Object = MibTableColumn
hh3cOltDbaVersion = _Hh3cOltDbaVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 3, 1, 5),
    _Hh3cOltDbaVersion_Type()
)
hh3cOltDbaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltDbaVersion.setStatus("current")


class _Hh3cOltDbaUpdate_Type(Integer32):
    """Custom type hh3cOltDbaUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("update", 1)
    )


_Hh3cOltDbaUpdate_Type.__name__ = "Integer32"
_Hh3cOltDbaUpdate_Object = MibTableColumn
hh3cOltDbaUpdate = _Hh3cOltDbaUpdate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 3, 1, 6),
    _Hh3cOltDbaUpdate_Type()
)
hh3cOltDbaUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOltDbaUpdate.setStatus("current")


class _Hh3cOltDbaUpdateResult_Type(Integer32):
    """Custom type hh3cOltDbaUpdateResult based on Integer32"""
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


_Hh3cOltDbaUpdateResult_Type.__name__ = "Integer32"
_Hh3cOltDbaUpdateResult_Object = MibTableColumn
hh3cOltDbaUpdateResult = _Hh3cOltDbaUpdateResult_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 3, 1, 7),
    _Hh3cOltDbaUpdateResult_Type()
)
hh3cOltDbaUpdateResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltDbaUpdateResult.setStatus("current")
_Hh3cOltPortAlarmThresholdTable_Object = MibTable
hh3cOltPortAlarmThresholdTable = _Hh3cOltPortAlarmThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 4)
)
if mibBuilder.loadTexts:
    hh3cOltPortAlarmThresholdTable.setStatus("current")
_Hh3cOltPortAlarmThresholdEntry_Object = MibTableRow
hh3cOltPortAlarmThresholdEntry = _Hh3cOltPortAlarmThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 4, 1)
)
hh3cOltPortAlarmThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cOltPortAlarmThresholdEntry.setStatus("current")


class _Hh3cOltPortAlarmBerEnabled_Type(TruthValue):
    """Custom type hh3cOltPortAlarmBerEnabled based on TruthValue"""


_Hh3cOltPortAlarmBerEnabled_Object = MibTableColumn
hh3cOltPortAlarmBerEnabled = _Hh3cOltPortAlarmBerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 4, 1, 1),
    _Hh3cOltPortAlarmBerEnabled_Type()
)
hh3cOltPortAlarmBerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOltPortAlarmBerEnabled.setStatus("current")


class _Hh3cOltPortAlarmBerDirect_Type(Integer32):
    """Custom type hh3cOltPortAlarmBerDirect based on Integer32"""
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


_Hh3cOltPortAlarmBerDirect_Type.__name__ = "Integer32"
_Hh3cOltPortAlarmBerDirect_Object = MibTableColumn
hh3cOltPortAlarmBerDirect = _Hh3cOltPortAlarmBerDirect_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 4, 1, 2),
    _Hh3cOltPortAlarmBerDirect_Type()
)
hh3cOltPortAlarmBerDirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOltPortAlarmBerDirect.setStatus("current")


class _Hh3cOltPortAlarmBerThreshold_Type(Integer32):
    """Custom type hh3cOltPortAlarmBerThreshold based on Integer32"""
    defaultValue = 10


_Hh3cOltPortAlarmBerThreshold_Object = MibTableColumn
hh3cOltPortAlarmBerThreshold = _Hh3cOltPortAlarmBerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 4, 1, 3),
    _Hh3cOltPortAlarmBerThreshold_Type()
)
hh3cOltPortAlarmBerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOltPortAlarmBerThreshold.setStatus("current")


class _Hh3cOltPortAlarmFerEnabled_Type(TruthValue):
    """Custom type hh3cOltPortAlarmFerEnabled based on TruthValue"""


_Hh3cOltPortAlarmFerEnabled_Object = MibTableColumn
hh3cOltPortAlarmFerEnabled = _Hh3cOltPortAlarmFerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 4, 1, 4),
    _Hh3cOltPortAlarmFerEnabled_Type()
)
hh3cOltPortAlarmFerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOltPortAlarmFerEnabled.setStatus("current")


class _Hh3cOltPortAlarmFerDirect_Type(Integer32):
    """Custom type hh3cOltPortAlarmFerDirect based on Integer32"""
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


_Hh3cOltPortAlarmFerDirect_Type.__name__ = "Integer32"
_Hh3cOltPortAlarmFerDirect_Object = MibTableColumn
hh3cOltPortAlarmFerDirect = _Hh3cOltPortAlarmFerDirect_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 4, 1, 5),
    _Hh3cOltPortAlarmFerDirect_Type()
)
hh3cOltPortAlarmFerDirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOltPortAlarmFerDirect.setStatus("current")


class _Hh3cOltPortAlarmFerThreshold_Type(Integer32):
    """Custom type hh3cOltPortAlarmFerThreshold based on Integer32"""
    defaultValue = 1


_Hh3cOltPortAlarmFerThreshold_Object = MibTableColumn
hh3cOltPortAlarmFerThreshold = _Hh3cOltPortAlarmFerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 4, 1, 6),
    _Hh3cOltPortAlarmFerThreshold_Type()
)
hh3cOltPortAlarmFerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOltPortAlarmFerThreshold.setStatus("current")


class _Hh3cOltPortAlarmLlidMismatchEnabled_Type(TruthValue):
    """Custom type hh3cOltPortAlarmLlidMismatchEnabled based on TruthValue"""


_Hh3cOltPortAlarmLlidMismatchEnabled_Object = MibTableColumn
hh3cOltPortAlarmLlidMismatchEnabled = _Hh3cOltPortAlarmLlidMismatchEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 4, 1, 7),
    _Hh3cOltPortAlarmLlidMismatchEnabled_Type()
)
hh3cOltPortAlarmLlidMismatchEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOltPortAlarmLlidMismatchEnabled.setStatus("current")


class _Hh3cOltPortAlarmLlidMismatchThreshold_Type(Integer32):
    """Custom type hh3cOltPortAlarmLlidMismatchThreshold based on Integer32"""
    defaultValue = 5000


_Hh3cOltPortAlarmLlidMismatchThreshold_Object = MibTableColumn
hh3cOltPortAlarmLlidMismatchThreshold = _Hh3cOltPortAlarmLlidMismatchThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 4, 1, 8),
    _Hh3cOltPortAlarmLlidMismatchThreshold_Type()
)
hh3cOltPortAlarmLlidMismatchThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOltPortAlarmLlidMismatchThreshold.setStatus("current")


class _Hh3cOltPortAlarmRemoteStableEnabled_Type(TruthValue):
    """Custom type hh3cOltPortAlarmRemoteStableEnabled based on TruthValue"""


_Hh3cOltPortAlarmRemoteStableEnabled_Object = MibTableColumn
hh3cOltPortAlarmRemoteStableEnabled = _Hh3cOltPortAlarmRemoteStableEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 4, 1, 9),
    _Hh3cOltPortAlarmRemoteStableEnabled_Type()
)
hh3cOltPortAlarmRemoteStableEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOltPortAlarmRemoteStableEnabled.setStatus("current")


class _Hh3cOltPortAlarmLocalStableEnabled_Type(TruthValue):
    """Custom type hh3cOltPortAlarmLocalStableEnabled based on TruthValue"""


_Hh3cOltPortAlarmLocalStableEnabled_Object = MibTableColumn
hh3cOltPortAlarmLocalStableEnabled = _Hh3cOltPortAlarmLocalStableEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 4, 1, 10),
    _Hh3cOltPortAlarmLocalStableEnabled_Type()
)
hh3cOltPortAlarmLocalStableEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOltPortAlarmLocalStableEnabled.setStatus("current")


class _Hh3cOltPortAlarmRegistrationEnabled_Type(TruthValue):
    """Custom type hh3cOltPortAlarmRegistrationEnabled based on TruthValue"""


_Hh3cOltPortAlarmRegistrationEnabled_Object = MibTableColumn
hh3cOltPortAlarmRegistrationEnabled = _Hh3cOltPortAlarmRegistrationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 4, 1, 11),
    _Hh3cOltPortAlarmRegistrationEnabled_Type()
)
hh3cOltPortAlarmRegistrationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOltPortAlarmRegistrationEnabled.setStatus("current")


class _Hh3cOltPortAlarmOamDisconnectionEnabled_Type(TruthValue):
    """Custom type hh3cOltPortAlarmOamDisconnectionEnabled based on TruthValue"""


_Hh3cOltPortAlarmOamDisconnectionEnabled_Object = MibTableColumn
hh3cOltPortAlarmOamDisconnectionEnabled = _Hh3cOltPortAlarmOamDisconnectionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 4, 1, 12),
    _Hh3cOltPortAlarmOamDisconnectionEnabled_Type()
)
hh3cOltPortAlarmOamDisconnectionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOltPortAlarmOamDisconnectionEnabled.setStatus("current")


class _Hh3cOltPortAlarmEncryptionKeyEnabled_Type(TruthValue):
    """Custom type hh3cOltPortAlarmEncryptionKeyEnabled based on TruthValue"""


_Hh3cOltPortAlarmEncryptionKeyEnabled_Object = MibTableColumn
hh3cOltPortAlarmEncryptionKeyEnabled = _Hh3cOltPortAlarmEncryptionKeyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 4, 1, 13),
    _Hh3cOltPortAlarmEncryptionKeyEnabled_Type()
)
hh3cOltPortAlarmEncryptionKeyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOltPortAlarmEncryptionKeyEnabled.setStatus("current")


class _Hh3cOltPortAlarmVendorSpecificEnabled_Type(TruthValue):
    """Custom type hh3cOltPortAlarmVendorSpecificEnabled based on TruthValue"""


_Hh3cOltPortAlarmVendorSpecificEnabled_Object = MibTableColumn
hh3cOltPortAlarmVendorSpecificEnabled = _Hh3cOltPortAlarmVendorSpecificEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 4, 1, 14),
    _Hh3cOltPortAlarmVendorSpecificEnabled_Type()
)
hh3cOltPortAlarmVendorSpecificEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOltPortAlarmVendorSpecificEnabled.setStatus("current")


class _Hh3cOltPortAlarmRegExcessEnabled_Type(TruthValue):
    """Custom type hh3cOltPortAlarmRegExcessEnabled based on TruthValue"""


_Hh3cOltPortAlarmRegExcessEnabled_Object = MibTableColumn
hh3cOltPortAlarmRegExcessEnabled = _Hh3cOltPortAlarmRegExcessEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 4, 1, 15),
    _Hh3cOltPortAlarmRegExcessEnabled_Type()
)
hh3cOltPortAlarmRegExcessEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOltPortAlarmRegExcessEnabled.setStatus("current")


class _Hh3cOltPortAlarmDFEEnabled_Type(TruthValue):
    """Custom type hh3cOltPortAlarmDFEEnabled based on TruthValue"""


_Hh3cOltPortAlarmDFEEnabled_Object = MibTableColumn
hh3cOltPortAlarmDFEEnabled = _Hh3cOltPortAlarmDFEEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 4, 1, 16),
    _Hh3cOltPortAlarmDFEEnabled_Type()
)
hh3cOltPortAlarmDFEEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOltPortAlarmDFEEnabled.setStatus("current")
_Hh3cOltLaserOnTimeMinVal_Type = Integer32
_Hh3cOltLaserOnTimeMinVal_Object = MibScalar
hh3cOltLaserOnTimeMinVal = _Hh3cOltLaserOnTimeMinVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 5),
    _Hh3cOltLaserOnTimeMinVal_Type()
)
hh3cOltLaserOnTimeMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltLaserOnTimeMinVal.setStatus("current")
_Hh3cOltLaserOnTimeMaxVal_Type = Integer32
_Hh3cOltLaserOnTimeMaxVal_Object = MibScalar
hh3cOltLaserOnTimeMaxVal = _Hh3cOltLaserOnTimeMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 6),
    _Hh3cOltLaserOnTimeMaxVal_Type()
)
hh3cOltLaserOnTimeMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltLaserOnTimeMaxVal.setStatus("current")
_Hh3cOltLaserOffTimeMinVal_Type = Integer32
_Hh3cOltLaserOffTimeMinVal_Object = MibScalar
hh3cOltLaserOffTimeMinVal = _Hh3cOltLaserOffTimeMinVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 7),
    _Hh3cOltLaserOffTimeMinVal_Type()
)
hh3cOltLaserOffTimeMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltLaserOffTimeMinVal.setStatus("current")
_Hh3cOltLaserOffTimeMaxVal_Type = Integer32
_Hh3cOltLaserOffTimeMaxVal_Object = MibScalar
hh3cOltLaserOffTimeMaxVal = _Hh3cOltLaserOffTimeMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 8),
    _Hh3cOltLaserOffTimeMaxVal_Type()
)
hh3cOltLaserOffTimeMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltLaserOffTimeMaxVal.setStatus("current")
_Hh3cOltDbaDiscoveryLengthMinVal_Type = Integer32
_Hh3cOltDbaDiscoveryLengthMinVal_Object = MibScalar
hh3cOltDbaDiscoveryLengthMinVal = _Hh3cOltDbaDiscoveryLengthMinVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 9),
    _Hh3cOltDbaDiscoveryLengthMinVal_Type()
)
hh3cOltDbaDiscoveryLengthMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltDbaDiscoveryLengthMinVal.setStatus("current")
_Hh3cOltDbaDiscoveryLengthMaxVal_Type = Integer32
_Hh3cOltDbaDiscoveryLengthMaxVal_Object = MibScalar
hh3cOltDbaDiscoveryLengthMaxVal = _Hh3cOltDbaDiscoveryLengthMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 10),
    _Hh3cOltDbaDiscoveryLengthMaxVal_Type()
)
hh3cOltDbaDiscoveryLengthMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltDbaDiscoveryLengthMaxVal.setStatus("current")
_Hh3cOltDbaDiscovryFrequencyMinVal_Type = Integer32
_Hh3cOltDbaDiscovryFrequencyMinVal_Object = MibScalar
hh3cOltDbaDiscovryFrequencyMinVal = _Hh3cOltDbaDiscovryFrequencyMinVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 11),
    _Hh3cOltDbaDiscovryFrequencyMinVal_Type()
)
hh3cOltDbaDiscovryFrequencyMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltDbaDiscovryFrequencyMinVal.setStatus("current")
_Hh3cOltDbaDiscovryFrequencyMaxVal_Type = Integer32
_Hh3cOltDbaDiscovryFrequencyMaxVal_Object = MibScalar
hh3cOltDbaDiscovryFrequencyMaxVal = _Hh3cOltDbaDiscovryFrequencyMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 12),
    _Hh3cOltDbaDiscovryFrequencyMaxVal_Type()
)
hh3cOltDbaDiscovryFrequencyMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltDbaDiscovryFrequencyMaxVal.setStatus("current")
_Hh3cOltDbaCycleLengthMinVal_Type = Integer32
_Hh3cOltDbaCycleLengthMinVal_Object = MibScalar
hh3cOltDbaCycleLengthMinVal = _Hh3cOltDbaCycleLengthMinVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 13),
    _Hh3cOltDbaCycleLengthMinVal_Type()
)
hh3cOltDbaCycleLengthMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltDbaCycleLengthMinVal.setStatus("current")
_Hh3cOltDbaCycleLengthMaxVal_Type = Integer32
_Hh3cOltDbaCycleLengthMaxVal_Object = MibScalar
hh3cOltDbaCycleLengthMaxVal = _Hh3cOltDbaCycleLengthMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 14),
    _Hh3cOltDbaCycleLengthMaxVal_Type()
)
hh3cOltDbaCycleLengthMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltDbaCycleLengthMaxVal.setStatus("current")
_Hh3cOltPortAlarmLlidMisMinVal_Type = Integer32
_Hh3cOltPortAlarmLlidMisMinVal_Object = MibScalar
hh3cOltPortAlarmLlidMisMinVal = _Hh3cOltPortAlarmLlidMisMinVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 15),
    _Hh3cOltPortAlarmLlidMisMinVal_Type()
)
hh3cOltPortAlarmLlidMisMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltPortAlarmLlidMisMinVal.setStatus("current")
_Hh3cOltPortAlarmLlidMisMaxVal_Type = Integer32
_Hh3cOltPortAlarmLlidMisMaxVal_Object = MibScalar
hh3cOltPortAlarmLlidMisMaxVal = _Hh3cOltPortAlarmLlidMisMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 16),
    _Hh3cOltPortAlarmLlidMisMaxVal_Type()
)
hh3cOltPortAlarmLlidMisMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltPortAlarmLlidMisMaxVal.setStatus("current")
_Hh3cOltPortAlarmBerMinVal_Type = Integer32
_Hh3cOltPortAlarmBerMinVal_Object = MibScalar
hh3cOltPortAlarmBerMinVal = _Hh3cOltPortAlarmBerMinVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 17),
    _Hh3cOltPortAlarmBerMinVal_Type()
)
hh3cOltPortAlarmBerMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltPortAlarmBerMinVal.setStatus("current")
_Hh3cOltPortAlarmBerMaxVal_Type = Integer32
_Hh3cOltPortAlarmBerMaxVal_Object = MibScalar
hh3cOltPortAlarmBerMaxVal = _Hh3cOltPortAlarmBerMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 18),
    _Hh3cOltPortAlarmBerMaxVal_Type()
)
hh3cOltPortAlarmBerMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltPortAlarmBerMaxVal.setStatus("current")
_Hh3cOltPortAlarmFerMinVal_Type = Integer32
_Hh3cOltPortAlarmFerMinVal_Object = MibScalar
hh3cOltPortAlarmFerMinVal = _Hh3cOltPortAlarmFerMinVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 19),
    _Hh3cOltPortAlarmFerMinVal_Type()
)
hh3cOltPortAlarmFerMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltPortAlarmFerMinVal.setStatus("current")
_Hh3cOltPortAlarmFerMaxVal_Type = Integer32
_Hh3cOltPortAlarmFerMaxVal_Object = MibScalar
hh3cOltPortAlarmFerMaxVal = _Hh3cOltPortAlarmFerMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 20),
    _Hh3cOltPortAlarmFerMaxVal_Type()
)
hh3cOltPortAlarmFerMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltPortAlarmFerMaxVal.setStatus("current")
_Hh3cOnuSilentTable_Object = MibTable
hh3cOnuSilentTable = _Hh3cOnuSilentTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 21)
)
if mibBuilder.loadTexts:
    hh3cOnuSilentTable.setStatus("current")
_Hh3cOnuSilentEntry_Object = MibTableRow
hh3cOnuSilentEntry = _Hh3cOnuSilentEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 21, 1)
)
hh3cOnuSilentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-MIB", "hh3cOnuSilentMacAddr"),
)
if mibBuilder.loadTexts:
    hh3cOnuSilentEntry.setStatus("current")
_Hh3cOnuSilentMacAddr_Type = MacAddress
_Hh3cOnuSilentMacAddr_Object = MibTableColumn
hh3cOnuSilentMacAddr = _Hh3cOnuSilentMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 21, 1, 1),
    _Hh3cOnuSilentMacAddr_Type()
)
hh3cOnuSilentMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cOnuSilentMacAddr.setStatus("current")
_Hh3cOnuSilentTime_Type = Integer32
_Hh3cOnuSilentTime_Object = MibTableColumn
hh3cOnuSilentTime = _Hh3cOnuSilentTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 21, 1, 2),
    _Hh3cOnuSilentTime_Type()
)
hh3cOnuSilentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuSilentTime.setStatus("current")
_Hh3cOltUsingOnuTable_Object = MibTable
hh3cOltUsingOnuTable = _Hh3cOltUsingOnuTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 22)
)
if mibBuilder.loadTexts:
    hh3cOltUsingOnuTable.setStatus("current")
_Hh3cOltUsingOnuEntry_Object = MibTableRow
hh3cOltUsingOnuEntry = _Hh3cOltUsingOnuEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 22, 1)
)
hh3cOltUsingOnuEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-MIB", "hh3cOltUsingOnuNum"),
)
if mibBuilder.loadTexts:
    hh3cOltUsingOnuEntry.setStatus("current")


class _Hh3cOltUsingOnuNum_Type(Integer32):
    """Custom type hh3cOltUsingOnuNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Hh3cOltUsingOnuNum_Type.__name__ = "Integer32"
_Hh3cOltUsingOnuNum_Object = MibTableColumn
hh3cOltUsingOnuNum = _Hh3cOltUsingOnuNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 22, 1, 1),
    _Hh3cOltUsingOnuNum_Type()
)
hh3cOltUsingOnuNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cOltUsingOnuNum.setStatus("current")
_Hh3cOltUsingOnuIfIndex_Type = Integer32
_Hh3cOltUsingOnuIfIndex_Object = MibTableColumn
hh3cOltUsingOnuIfIndex = _Hh3cOltUsingOnuIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 22, 1, 2),
    _Hh3cOltUsingOnuIfIndex_Type()
)
hh3cOltUsingOnuIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOltUsingOnuIfIndex.setStatus("current")
_Hh3cOltUsingOnuRowStatus_Type = RowStatus
_Hh3cOltUsingOnuRowStatus_Object = MibTableColumn
hh3cOltUsingOnuRowStatus = _Hh3cOltUsingOnuRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 3, 22, 1, 3),
    _Hh3cOltUsingOnuRowStatus_Type()
)
hh3cOltUsingOnuRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cOltUsingOnuRowStatus.setStatus("current")
_Hh3cEponOnuMan_ObjectIdentity = ObjectIdentity
hh3cEponOnuMan = _Hh3cEponOnuMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5)
)
_Hh3cOnuSysManTable_Object = MibTable
hh3cOnuSysManTable = _Hh3cOnuSysManTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hh3cOnuSysManTable.setStatus("current")
_Hh3cOnuSysManEntry_Object = MibTableRow
hh3cOnuSysManEntry = _Hh3cOnuSysManEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 1, 1)
)
hh3cOnuSysManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cOnuSysManEntry.setStatus("current")


class _Hh3cOnuEncryptMan_Type(Integer32):
    """Custom type hh3cOnuEncryptMan based on Integer32"""
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


_Hh3cOnuEncryptMan_Type.__name__ = "Integer32"
_Hh3cOnuEncryptMan_Object = MibTableColumn
hh3cOnuEncryptMan = _Hh3cOnuEncryptMan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 1, 1, 1),
    _Hh3cOnuEncryptMan_Type()
)
hh3cOnuEncryptMan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuEncryptMan.setStatus("current")


class _Hh3cOnuReAuthorize_Type(Integer32):
    """Custom type hh3cOnuReAuthorize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reAuthorize", 1)
    )


_Hh3cOnuReAuthorize_Type.__name__ = "Integer32"
_Hh3cOnuReAuthorize_Object = MibTableColumn
hh3cOnuReAuthorize = _Hh3cOnuReAuthorize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 1, 1, 2),
    _Hh3cOnuReAuthorize_Type()
)
hh3cOnuReAuthorize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuReAuthorize.setStatus("current")


class _Hh3cOnuMulticastFilterStatus_Type(TruthValue):
    """Custom type hh3cOnuMulticastFilterStatus based on TruthValue"""


_Hh3cOnuMulticastFilterStatus_Object = MibTableColumn
hh3cOnuMulticastFilterStatus = _Hh3cOnuMulticastFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 1, 1, 3),
    _Hh3cOnuMulticastFilterStatus_Type()
)
hh3cOnuMulticastFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuMulticastFilterStatus.setStatus("current")


class _Hh3cOnuDbaReportQueueSetNumber_Type(Integer32):
    """Custom type hh3cOnuDbaReportQueueSetNumber based on Integer32"""
    defaultValue = 2


_Hh3cOnuDbaReportQueueSetNumber_Object = MibTableColumn
hh3cOnuDbaReportQueueSetNumber = _Hh3cOnuDbaReportQueueSetNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 1, 1, 4),
    _Hh3cOnuDbaReportQueueSetNumber_Type()
)
hh3cOnuDbaReportQueueSetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuDbaReportQueueSetNumber.setStatus("current")


class _Hh3cOnuRemoteFecStatus_Type(Integer32):
    """Custom type hh3cOnuRemoteFecStatus based on Integer32"""
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


_Hh3cOnuRemoteFecStatus_Type.__name__ = "Integer32"
_Hh3cOnuRemoteFecStatus_Object = MibTableColumn
hh3cOnuRemoteFecStatus = _Hh3cOnuRemoteFecStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 1, 1, 5),
    _Hh3cOnuRemoteFecStatus_Type()
)
hh3cOnuRemoteFecStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuRemoteFecStatus.setStatus("current")


class _Hh3cOnuPortBerStatus_Type(Integer32):
    """Custom type hh3cOnuPortBerStatus based on Integer32"""
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


_Hh3cOnuPortBerStatus_Type.__name__ = "Integer32"
_Hh3cOnuPortBerStatus_Object = MibTableColumn
hh3cOnuPortBerStatus = _Hh3cOnuPortBerStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 1, 1, 6),
    _Hh3cOnuPortBerStatus_Type()
)
hh3cOnuPortBerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuPortBerStatus.setStatus("current")


class _Hh3cOnuReset_Type(Integer32):
    """Custom type hh3cOnuReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Hh3cOnuReset_Type.__name__ = "Integer32"
_Hh3cOnuReset_Object = MibTableColumn
hh3cOnuReset = _Hh3cOnuReset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 1, 1, 7),
    _Hh3cOnuReset_Type()
)
hh3cOnuReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuReset.setStatus("current")


class _Hh3cOnuMulticastControlMode_Type(Integer32):
    """Custom type hh3cOnuMulticastControlMode based on Integer32"""
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


_Hh3cOnuMulticastControlMode_Type.__name__ = "Integer32"
_Hh3cOnuMulticastControlMode_Object = MibTableColumn
hh3cOnuMulticastControlMode = _Hh3cOnuMulticastControlMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 1, 1, 8),
    _Hh3cOnuMulticastControlMode_Type()
)
hh3cOnuMulticastControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuMulticastControlMode.setStatus("current")
_Hh3cOnuAccessVlan_Type = Integer32
_Hh3cOnuAccessVlan_Object = MibTableColumn
hh3cOnuAccessVlan = _Hh3cOnuAccessVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 1, 1, 9),
    _Hh3cOnuAccessVlan_Type()
)
hh3cOnuAccessVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuAccessVlan.setStatus("current")


class _Hh3cOnuEncryptKey_Type(DisplayString):
    """Custom type hh3cOnuEncryptKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cOnuEncryptKey_Type.__name__ = "DisplayString"
_Hh3cOnuEncryptKey_Object = MibTableColumn
hh3cOnuEncryptKey = _Hh3cOnuEncryptKey_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 1, 1, 10),
    _Hh3cOnuEncryptKey_Type()
)
hh3cOnuEncryptKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuEncryptKey.setStatus("current")


class _Hh3cOnuUniUpDownTrapStatus_Type(TruthValue):
    """Custom type hh3cOnuUniUpDownTrapStatus based on TruthValue"""


_Hh3cOnuUniUpDownTrapStatus_Object = MibTableColumn
hh3cOnuUniUpDownTrapStatus = _Hh3cOnuUniUpDownTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 1, 1, 11),
    _Hh3cOnuUniUpDownTrapStatus_Type()
)
hh3cOnuUniUpDownTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuUniUpDownTrapStatus.setStatus("current")


class _Hh3cOnuFecStatus_Type(Integer32):
    """Custom type hh3cOnuFecStatus based on Integer32"""
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


_Hh3cOnuFecStatus_Type.__name__ = "Integer32"
_Hh3cOnuFecStatus_Object = MibTableColumn
hh3cOnuFecStatus = _Hh3cOnuFecStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 1, 1, 12),
    _Hh3cOnuFecStatus_Type()
)
hh3cOnuFecStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuFecStatus.setStatus("current")
_Hh3cOnuMcastCtrlHostAgingTime_Type = Integer32
_Hh3cOnuMcastCtrlHostAgingTime_Object = MibTableColumn
hh3cOnuMcastCtrlHostAgingTime = _Hh3cOnuMcastCtrlHostAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 1, 1, 13),
    _Hh3cOnuMcastCtrlHostAgingTime_Type()
)
hh3cOnuMcastCtrlHostAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuMcastCtrlHostAgingTime.setStatus("current")
_Hh3cOnuMulticastFastLeaveEnable_Type = TruthValue
_Hh3cOnuMulticastFastLeaveEnable_Object = MibTableColumn
hh3cOnuMulticastFastLeaveEnable = _Hh3cOnuMulticastFastLeaveEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 1, 1, 14),
    _Hh3cOnuMulticastFastLeaveEnable_Type()
)
hh3cOnuMulticastFastLeaveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuMulticastFastLeaveEnable.setStatus("current")
_Hh3cOnuPortIsolateEnable_Type = TruthValue
_Hh3cOnuPortIsolateEnable_Object = MibTableColumn
hh3cOnuPortIsolateEnable = _Hh3cOnuPortIsolateEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 1, 1, 15),
    _Hh3cOnuPortIsolateEnable_Type()
)
hh3cOnuPortIsolateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuPortIsolateEnable.setStatus("current")
_Hh3cOnuLinkTestTable_Object = MibTable
hh3cOnuLinkTestTable = _Hh3cOnuLinkTestTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 2)
)
if mibBuilder.loadTexts:
    hh3cOnuLinkTestTable.setStatus("current")
_Hh3cOnuLinkTestEntry_Object = MibTableRow
hh3cOnuLinkTestEntry = _Hh3cOnuLinkTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 2, 1)
)
hh3cOnuLinkTestEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cOnuLinkTestEntry.setStatus("current")


class _Hh3cOnuLinkTestFrameNum_Type(Integer32):
    """Custom type hh3cOnuLinkTestFrameNum based on Integer32"""
    defaultValue = 20


_Hh3cOnuLinkTestFrameNum_Object = MibTableColumn
hh3cOnuLinkTestFrameNum = _Hh3cOnuLinkTestFrameNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 2, 1, 1),
    _Hh3cOnuLinkTestFrameNum_Type()
)
hh3cOnuLinkTestFrameNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuLinkTestFrameNum.setStatus("current")


class _Hh3cOnuLinkTestFrameSize_Type(Integer32):
    """Custom type hh3cOnuLinkTestFrameSize based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1514),
    )


_Hh3cOnuLinkTestFrameSize_Type.__name__ = "Integer32"
_Hh3cOnuLinkTestFrameSize_Object = MibTableColumn
hh3cOnuLinkTestFrameSize = _Hh3cOnuLinkTestFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 2, 1, 2),
    _Hh3cOnuLinkTestFrameSize_Type()
)
hh3cOnuLinkTestFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuLinkTestFrameSize.setStatus("current")


class _Hh3cOnuLinkTestDelay_Type(TruthValue):
    """Custom type hh3cOnuLinkTestDelay based on TruthValue"""


_Hh3cOnuLinkTestDelay_Object = MibTableColumn
hh3cOnuLinkTestDelay = _Hh3cOnuLinkTestDelay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 2, 1, 3),
    _Hh3cOnuLinkTestDelay_Type()
)
hh3cOnuLinkTestDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuLinkTestDelay.setStatus("current")


class _Hh3cOnuLinkTestVlanTag_Type(TruthValue):
    """Custom type hh3cOnuLinkTestVlanTag based on TruthValue"""


_Hh3cOnuLinkTestVlanTag_Object = MibTableColumn
hh3cOnuLinkTestVlanTag = _Hh3cOnuLinkTestVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 2, 1, 4),
    _Hh3cOnuLinkTestVlanTag_Type()
)
hh3cOnuLinkTestVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuLinkTestVlanTag.setStatus("current")


class _Hh3cOnuLinkTestVlanPriority_Type(Integer32):
    """Custom type hh3cOnuLinkTestVlanPriority based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cOnuLinkTestVlanPriority_Type.__name__ = "Integer32"
_Hh3cOnuLinkTestVlanPriority_Object = MibTableColumn
hh3cOnuLinkTestVlanPriority = _Hh3cOnuLinkTestVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 2, 1, 5),
    _Hh3cOnuLinkTestVlanPriority_Type()
)
hh3cOnuLinkTestVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuLinkTestVlanPriority.setStatus("current")


class _Hh3cOnuLinkTestVlanTagID_Type(Integer32):
    """Custom type hh3cOnuLinkTestVlanTagID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cOnuLinkTestVlanTagID_Type.__name__ = "Integer32"
_Hh3cOnuLinkTestVlanTagID_Object = MibTableColumn
hh3cOnuLinkTestVlanTagID = _Hh3cOnuLinkTestVlanTagID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 2, 1, 6),
    _Hh3cOnuLinkTestVlanTagID_Type()
)
hh3cOnuLinkTestVlanTagID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuLinkTestVlanTagID.setStatus("current")
_Hh3cOnuLinkTestResultSentFrameNum_Type = Integer32
_Hh3cOnuLinkTestResultSentFrameNum_Object = MibTableColumn
hh3cOnuLinkTestResultSentFrameNum = _Hh3cOnuLinkTestResultSentFrameNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 2, 1, 7),
    _Hh3cOnuLinkTestResultSentFrameNum_Type()
)
hh3cOnuLinkTestResultSentFrameNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuLinkTestResultSentFrameNum.setStatus("current")
_Hh3cOnuLinkTestResultRetFrameNum_Type = Integer32
_Hh3cOnuLinkTestResultRetFrameNum_Object = MibTableColumn
hh3cOnuLinkTestResultRetFrameNum = _Hh3cOnuLinkTestResultRetFrameNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 2, 1, 8),
    _Hh3cOnuLinkTestResultRetFrameNum_Type()
)
hh3cOnuLinkTestResultRetFrameNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuLinkTestResultRetFrameNum.setStatus("current")
_Hh3cOnuLinkTestResultRetErrFrameNum_Type = Integer32
_Hh3cOnuLinkTestResultRetErrFrameNum_Object = MibTableColumn
hh3cOnuLinkTestResultRetErrFrameNum = _Hh3cOnuLinkTestResultRetErrFrameNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 2, 1, 9),
    _Hh3cOnuLinkTestResultRetErrFrameNum_Type()
)
hh3cOnuLinkTestResultRetErrFrameNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuLinkTestResultRetErrFrameNum.setStatus("current")
_Hh3cOnuLinkTestResultMinDelay_Type = Integer32
_Hh3cOnuLinkTestResultMinDelay_Object = MibTableColumn
hh3cOnuLinkTestResultMinDelay = _Hh3cOnuLinkTestResultMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 2, 1, 10),
    _Hh3cOnuLinkTestResultMinDelay_Type()
)
hh3cOnuLinkTestResultMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuLinkTestResultMinDelay.setStatus("current")
_Hh3cOnuLinkTestResultMeanDelay_Type = Integer32
_Hh3cOnuLinkTestResultMeanDelay_Object = MibTableColumn
hh3cOnuLinkTestResultMeanDelay = _Hh3cOnuLinkTestResultMeanDelay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 2, 1, 11),
    _Hh3cOnuLinkTestResultMeanDelay_Type()
)
hh3cOnuLinkTestResultMeanDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuLinkTestResultMeanDelay.setStatus("current")
_Hh3cOnuLinkTestResultMaxDelay_Type = Integer32
_Hh3cOnuLinkTestResultMaxDelay_Object = MibTableColumn
hh3cOnuLinkTestResultMaxDelay = _Hh3cOnuLinkTestResultMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 2, 1, 12),
    _Hh3cOnuLinkTestResultMaxDelay_Type()
)
hh3cOnuLinkTestResultMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuLinkTestResultMaxDelay.setStatus("current")
_Hh3cOnuBandWidthTable_Object = MibTable
hh3cOnuBandWidthTable = _Hh3cOnuBandWidthTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 3)
)
if mibBuilder.loadTexts:
    hh3cOnuBandWidthTable.setStatus("current")
_Hh3cOnuBandWidthEntry_Object = MibTableRow
hh3cOnuBandWidthEntry = _Hh3cOnuBandWidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 3, 1)
)
hh3cOnuBandWidthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cOnuBandWidthEntry.setStatus("current")


class _Hh3cOnuDownStreamBandWidthPolicy_Type(TruthValue):
    """Custom type hh3cOnuDownStreamBandWidthPolicy based on TruthValue"""


_Hh3cOnuDownStreamBandWidthPolicy_Object = MibTableColumn
hh3cOnuDownStreamBandWidthPolicy = _Hh3cOnuDownStreamBandWidthPolicy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 3, 1, 1),
    _Hh3cOnuDownStreamBandWidthPolicy_Type()
)
hh3cOnuDownStreamBandWidthPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuDownStreamBandWidthPolicy.setStatus("current")


class _Hh3cOnuDownStreamMaxBandWidth_Type(Integer32):
    """Custom type hh3cOnuDownStreamMaxBandWidth based on Integer32"""
    defaultValue = 1000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_Hh3cOnuDownStreamMaxBandWidth_Type.__name__ = "Integer32"
_Hh3cOnuDownStreamMaxBandWidth_Object = MibTableColumn
hh3cOnuDownStreamMaxBandWidth = _Hh3cOnuDownStreamMaxBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 3, 1, 2),
    _Hh3cOnuDownStreamMaxBandWidth_Type()
)
hh3cOnuDownStreamMaxBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuDownStreamMaxBandWidth.setStatus("current")


class _Hh3cOnuDownStreamMaxBurstSize_Type(Integer32):
    """Custom type hh3cOnuDownStreamMaxBurstSize based on Integer32"""
    defaultValue = 8388480

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8388480),
    )


_Hh3cOnuDownStreamMaxBurstSize_Type.__name__ = "Integer32"
_Hh3cOnuDownStreamMaxBurstSize_Object = MibTableColumn
hh3cOnuDownStreamMaxBurstSize = _Hh3cOnuDownStreamMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 3, 1, 3),
    _Hh3cOnuDownStreamMaxBurstSize_Type()
)
hh3cOnuDownStreamMaxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuDownStreamMaxBurstSize.setStatus("current")


class _Hh3cOnuDownStreamHighPriorityFirst_Type(TruthValue):
    """Custom type hh3cOnuDownStreamHighPriorityFirst based on TruthValue"""


_Hh3cOnuDownStreamHighPriorityFirst_Object = MibTableColumn
hh3cOnuDownStreamHighPriorityFirst = _Hh3cOnuDownStreamHighPriorityFirst_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 3, 1, 4),
    _Hh3cOnuDownStreamHighPriorityFirst_Type()
)
hh3cOnuDownStreamHighPriorityFirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuDownStreamHighPriorityFirst.setStatus("current")


class _Hh3cOnuDownStreamShortFrameFirst_Type(TruthValue):
    """Custom type hh3cOnuDownStreamShortFrameFirst based on TruthValue"""


_Hh3cOnuDownStreamShortFrameFirst_Object = MibTableColumn
hh3cOnuDownStreamShortFrameFirst = _Hh3cOnuDownStreamShortFrameFirst_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 3, 1, 5),
    _Hh3cOnuDownStreamShortFrameFirst_Type()
)
hh3cOnuDownStreamShortFrameFirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuDownStreamShortFrameFirst.setStatus("current")


class _Hh3cOnuP2PBandWidthPolicy_Type(TruthValue):
    """Custom type hh3cOnuP2PBandWidthPolicy based on TruthValue"""


_Hh3cOnuP2PBandWidthPolicy_Object = MibTableColumn
hh3cOnuP2PBandWidthPolicy = _Hh3cOnuP2PBandWidthPolicy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 3, 1, 6),
    _Hh3cOnuP2PBandWidthPolicy_Type()
)
hh3cOnuP2PBandWidthPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuP2PBandWidthPolicy.setStatus("current")


class _Hh3cOnuP2PMaxBandWidth_Type(Integer32):
    """Custom type hh3cOnuP2PMaxBandWidth based on Integer32"""
    defaultValue = 1000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_Hh3cOnuP2PMaxBandWidth_Type.__name__ = "Integer32"
_Hh3cOnuP2PMaxBandWidth_Object = MibTableColumn
hh3cOnuP2PMaxBandWidth = _Hh3cOnuP2PMaxBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 3, 1, 7),
    _Hh3cOnuP2PMaxBandWidth_Type()
)
hh3cOnuP2PMaxBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuP2PMaxBandWidth.setStatus("current")


class _Hh3cOnuP2PMaxBurstSize_Type(Integer32):
    """Custom type hh3cOnuP2PMaxBurstSize based on Integer32"""
    defaultValue = 8388480

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8388480),
    )


_Hh3cOnuP2PMaxBurstSize_Type.__name__ = "Integer32"
_Hh3cOnuP2PMaxBurstSize_Object = MibTableColumn
hh3cOnuP2PMaxBurstSize = _Hh3cOnuP2PMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 3, 1, 8),
    _Hh3cOnuP2PMaxBurstSize_Type()
)
hh3cOnuP2PMaxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuP2PMaxBurstSize.setStatus("current")


class _Hh3cOnuP2PHighPriorityFirst_Type(TruthValue):
    """Custom type hh3cOnuP2PHighPriorityFirst based on TruthValue"""


_Hh3cOnuP2PHighPriorityFirst_Object = MibTableColumn
hh3cOnuP2PHighPriorityFirst = _Hh3cOnuP2PHighPriorityFirst_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 3, 1, 9),
    _Hh3cOnuP2PHighPriorityFirst_Type()
)
hh3cOnuP2PHighPriorityFirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuP2PHighPriorityFirst.setStatus("current")


class _Hh3cOnuP2PShortFrameFirst_Type(TruthValue):
    """Custom type hh3cOnuP2PShortFrameFirst based on TruthValue"""


_Hh3cOnuP2PShortFrameFirst_Object = MibTableColumn
hh3cOnuP2PShortFrameFirst = _Hh3cOnuP2PShortFrameFirst_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 3, 1, 10),
    _Hh3cOnuP2PShortFrameFirst_Type()
)
hh3cOnuP2PShortFrameFirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuP2PShortFrameFirst.setStatus("current")
_Hh3cOnuSlaManTable_Object = MibTable
hh3cOnuSlaManTable = _Hh3cOnuSlaManTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 4)
)
if mibBuilder.loadTexts:
    hh3cOnuSlaManTable.setStatus("current")
_Hh3cOnuSlaManEntry_Object = MibTableRow
hh3cOnuSlaManEntry = _Hh3cOnuSlaManEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 4, 1)
)
hh3cOnuSlaManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cOnuSlaManEntry.setStatus("current")
_Hh3cOnuSlaMaxBandWidth_Type = Integer32
_Hh3cOnuSlaMaxBandWidth_Object = MibTableColumn
hh3cOnuSlaMaxBandWidth = _Hh3cOnuSlaMaxBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 4, 1, 1),
    _Hh3cOnuSlaMaxBandWidth_Type()
)
hh3cOnuSlaMaxBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuSlaMaxBandWidth.setStatus("current")
_Hh3cOnuSlaMinBandWidth_Type = Integer32
_Hh3cOnuSlaMinBandWidth_Object = MibTableColumn
hh3cOnuSlaMinBandWidth = _Hh3cOnuSlaMinBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 4, 1, 2),
    _Hh3cOnuSlaMinBandWidth_Type()
)
hh3cOnuSlaMinBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuSlaMinBandWidth.setStatus("current")
_Hh3cOnuSlaBandWidthStepVal_Type = Integer32
_Hh3cOnuSlaBandWidthStepVal_Object = MibTableColumn
hh3cOnuSlaBandWidthStepVal = _Hh3cOnuSlaBandWidthStepVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 4, 1, 3),
    _Hh3cOnuSlaBandWidthStepVal_Type()
)
hh3cOnuSlaBandWidthStepVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuSlaBandWidthStepVal.setStatus("current")


class _Hh3cOnuSlaDelay_Type(Integer32):
    """Custom type hh3cOnuSlaDelay based on Integer32"""
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


_Hh3cOnuSlaDelay_Type.__name__ = "Integer32"
_Hh3cOnuSlaDelay_Object = MibTableColumn
hh3cOnuSlaDelay = _Hh3cOnuSlaDelay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 4, 1, 4),
    _Hh3cOnuSlaDelay_Type()
)
hh3cOnuSlaDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuSlaDelay.setStatus("current")
_Hh3cOnuSlaFixedBandWidth_Type = Integer32
_Hh3cOnuSlaFixedBandWidth_Object = MibTableColumn
hh3cOnuSlaFixedBandWidth = _Hh3cOnuSlaFixedBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 4, 1, 5),
    _Hh3cOnuSlaFixedBandWidth_Type()
)
hh3cOnuSlaFixedBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuSlaFixedBandWidth.setStatus("current")


class _Hh3cOnuSlaPriorityClass_Type(Integer32):
    """Custom type hh3cOnuSlaPriorityClass based on Integer32"""
    defaultValue = 0


_Hh3cOnuSlaPriorityClass_Object = MibTableColumn
hh3cOnuSlaPriorityClass = _Hh3cOnuSlaPriorityClass_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 4, 1, 6),
    _Hh3cOnuSlaPriorityClass_Type()
)
hh3cOnuSlaPriorityClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuSlaPriorityClass.setStatus("current")
_Hh3cOnuSlaFixedPacketSize_Type = Integer32
_Hh3cOnuSlaFixedPacketSize_Object = MibTableColumn
hh3cOnuSlaFixedPacketSize = _Hh3cOnuSlaFixedPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 4, 1, 7),
    _Hh3cOnuSlaFixedPacketSize_Type()
)
hh3cOnuSlaFixedPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuSlaFixedPacketSize.setStatus("current")
_Hh3cOnuInfoTable_Object = MibTable
hh3cOnuInfoTable = _Hh3cOnuInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 5)
)
if mibBuilder.loadTexts:
    hh3cOnuInfoTable.setStatus("current")
_Hh3cOnuInfoEntry_Object = MibTableRow
hh3cOnuInfoEntry = _Hh3cOnuInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 5, 1)
)
hh3cOnuInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cOnuInfoEntry.setStatus("current")
_Hh3cOnuHardMajorVersion_Type = OctetString
_Hh3cOnuHardMajorVersion_Object = MibTableColumn
hh3cOnuHardMajorVersion = _Hh3cOnuHardMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 5, 1, 1),
    _Hh3cOnuHardMajorVersion_Type()
)
hh3cOnuHardMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuHardMajorVersion.setStatus("current")
_Hh3cOnuHardMinorVersion_Type = OctetString
_Hh3cOnuHardMinorVersion_Object = MibTableColumn
hh3cOnuHardMinorVersion = _Hh3cOnuHardMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 5, 1, 2),
    _Hh3cOnuHardMinorVersion_Type()
)
hh3cOnuHardMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuHardMinorVersion.setStatus("current")
_Hh3cOnuSoftwareVersion_Type = OctetString
_Hh3cOnuSoftwareVersion_Object = MibTableColumn
hh3cOnuSoftwareVersion = _Hh3cOnuSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 5, 1, 3),
    _Hh3cOnuSoftwareVersion_Type()
)
hh3cOnuSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuSoftwareVersion.setStatus("current")


class _Hh3cOnuUniMacType_Type(Integer32):
    """Custom type hh3cOnuUniMacType based on Integer32"""
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


_Hh3cOnuUniMacType_Type.__name__ = "Integer32"
_Hh3cOnuUniMacType_Object = MibTableColumn
hh3cOnuUniMacType = _Hh3cOnuUniMacType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 5, 1, 4),
    _Hh3cOnuUniMacType_Type()
)
hh3cOnuUniMacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuUniMacType.setStatus("current")
_Hh3cOnuLaserOnTime_Type = Integer32
_Hh3cOnuLaserOnTime_Object = MibTableColumn
hh3cOnuLaserOnTime = _Hh3cOnuLaserOnTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 5, 1, 5),
    _Hh3cOnuLaserOnTime_Type()
)
hh3cOnuLaserOnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuLaserOnTime.setStatus("current")
_Hh3cOnuLaserOffTime_Type = Integer32
_Hh3cOnuLaserOffTime_Object = MibTableColumn
hh3cOnuLaserOffTime = _Hh3cOnuLaserOffTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 5, 1, 6),
    _Hh3cOnuLaserOffTime_Type()
)
hh3cOnuLaserOffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuLaserOffTime.setStatus("current")


class _Hh3cOnuGrantFifoDep_Type(Integer32):
    """Custom type hh3cOnuGrantFifoDep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Hh3cOnuGrantFifoDep_Type.__name__ = "Integer32"
_Hh3cOnuGrantFifoDep_Object = MibTableColumn
hh3cOnuGrantFifoDep = _Hh3cOnuGrantFifoDep_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 5, 1, 7),
    _Hh3cOnuGrantFifoDep_Type()
)
hh3cOnuGrantFifoDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuGrantFifoDep.setStatus("current")


class _Hh3cOnuWorkMode_Type(Integer32):
    """Custom type hh3cOnuWorkMode based on Integer32"""
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


_Hh3cOnuWorkMode_Type.__name__ = "Integer32"
_Hh3cOnuWorkMode_Object = MibTableColumn
hh3cOnuWorkMode = _Hh3cOnuWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 5, 1, 8),
    _Hh3cOnuWorkMode_Type()
)
hh3cOnuWorkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuWorkMode.setStatus("current")
_Hh3cOnuPCBVersion_Type = OctetString
_Hh3cOnuPCBVersion_Object = MibTableColumn
hh3cOnuPCBVersion = _Hh3cOnuPCBVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 5, 1, 9),
    _Hh3cOnuPCBVersion_Type()
)
hh3cOnuPCBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuPCBVersion.setStatus("current")
_Hh3cOnuRtt_Type = Unsigned32
_Hh3cOnuRtt_Object = MibTableColumn
hh3cOnuRtt = _Hh3cOnuRtt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 5, 1, 10),
    _Hh3cOnuRtt_Type()
)
hh3cOnuRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuRtt.setStatus("current")
_Hh3cOnuEEPROMVersion_Type = OctetString
_Hh3cOnuEEPROMVersion_Object = MibTableColumn
hh3cOnuEEPROMVersion = _Hh3cOnuEEPROMVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 5, 1, 11),
    _Hh3cOnuEEPROMVersion_Type()
)
hh3cOnuEEPROMVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuEEPROMVersion.setStatus("current")
_Hh3cOnuRegType_Type = OctetString
_Hh3cOnuRegType_Object = MibTableColumn
hh3cOnuRegType = _Hh3cOnuRegType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 5, 1, 12),
    _Hh3cOnuRegType_Type()
)
hh3cOnuRegType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuRegType.setStatus("current")
_Hh3cOnuHostType_Type = OctetString
_Hh3cOnuHostType_Object = MibTableColumn
hh3cOnuHostType = _Hh3cOnuHostType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 5, 1, 13),
    _Hh3cOnuHostType_Type()
)
hh3cOnuHostType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuHostType.setStatus("current")
_Hh3cOnuDistance_Type = Integer32
_Hh3cOnuDistance_Object = MibTableColumn
hh3cOnuDistance = _Hh3cOnuDistance_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 5, 1, 14),
    _Hh3cOnuDistance_Type()
)
hh3cOnuDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuDistance.setStatus("current")
_Hh3cOnuLlid_Type = Integer32
_Hh3cOnuLlid_Object = MibTableColumn
hh3cOnuLlid = _Hh3cOnuLlid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 5, 1, 15),
    _Hh3cOnuLlid_Type()
)
hh3cOnuLlid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuLlid.setStatus("current")
_Hh3cOnuVendorId_Type = OctetString
_Hh3cOnuVendorId_Object = MibTableColumn
hh3cOnuVendorId = _Hh3cOnuVendorId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 5, 1, 16),
    _Hh3cOnuVendorId_Type()
)
hh3cOnuVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuVendorId.setStatus("current")
_Hh3cOnuFirmwareVersion_Type = OctetString
_Hh3cOnuFirmwareVersion_Object = MibTableColumn
hh3cOnuFirmwareVersion = _Hh3cOnuFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 5, 1, 17),
    _Hh3cOnuFirmwareVersion_Type()
)
hh3cOnuFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuFirmwareVersion.setStatus("current")
_Hh3cOnuOpticalPowerReceivedByOlt_Type = Integer32
_Hh3cOnuOpticalPowerReceivedByOlt_Object = MibTableColumn
hh3cOnuOpticalPowerReceivedByOlt = _Hh3cOnuOpticalPowerReceivedByOlt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 5, 1, 18),
    _Hh3cOnuOpticalPowerReceivedByOlt_Type()
)
hh3cOnuOpticalPowerReceivedByOlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuOpticalPowerReceivedByOlt.setStatus("current")
_Hh3cOnuMacAddrInfoTable_Object = MibTable
hh3cOnuMacAddrInfoTable = _Hh3cOnuMacAddrInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 6)
)
if mibBuilder.loadTexts:
    hh3cOnuMacAddrInfoTable.setStatus("current")
_Hh3cOnuMacAddrInfoEntry_Object = MibTableRow
hh3cOnuMacAddrInfoEntry = _Hh3cOnuMacAddrInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 6, 1)
)
hh3cOnuMacAddrInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-MIB", "hh3cOnuMacIndex"),
)
if mibBuilder.loadTexts:
    hh3cOnuMacAddrInfoEntry.setStatus("current")
_Hh3cOnuMacIndex_Type = Integer32
_Hh3cOnuMacIndex_Object = MibTableColumn
hh3cOnuMacIndex = _Hh3cOnuMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 6, 1, 1),
    _Hh3cOnuMacIndex_Type()
)
hh3cOnuMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cOnuMacIndex.setStatus("current")


class _Hh3cOnuMacAddrFlag_Type(Integer32):
    """Custom type hh3cOnuMacAddrFlag based on Integer32"""
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


_Hh3cOnuMacAddrFlag_Type.__name__ = "Integer32"
_Hh3cOnuMacAddrFlag_Object = MibTableColumn
hh3cOnuMacAddrFlag = _Hh3cOnuMacAddrFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 6, 1, 2),
    _Hh3cOnuMacAddrFlag_Type()
)
hh3cOnuMacAddrFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuMacAddrFlag.setStatus("current")
_Hh3cOnuMacAddress_Type = MacAddress
_Hh3cOnuMacAddress_Object = MibTableColumn
hh3cOnuMacAddress = _Hh3cOnuMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 6, 1, 3),
    _Hh3cOnuMacAddress_Type()
)
hh3cOnuMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuMacAddress.setStatus("current")
_Hh3cOnuBindMacAddrTable_Object = MibTable
hh3cOnuBindMacAddrTable = _Hh3cOnuBindMacAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 7)
)
if mibBuilder.loadTexts:
    hh3cOnuBindMacAddrTable.setStatus("current")
_Hh3cOnuBindMacAddrEntry_Object = MibTableRow
hh3cOnuBindMacAddrEntry = _Hh3cOnuBindMacAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 7, 1)
)
hh3cOnuBindMacAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cOnuBindMacAddrEntry.setStatus("current")
_Hh3cOnuBindMacAddress_Type = MacAddress
_Hh3cOnuBindMacAddress_Object = MibTableColumn
hh3cOnuBindMacAddress = _Hh3cOnuBindMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 7, 1, 1),
    _Hh3cOnuBindMacAddress_Type()
)
hh3cOnuBindMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuBindMacAddress.setStatus("current")
_Hh3cOnuBindType_Type = Integer32
_Hh3cOnuBindType_Object = MibTableColumn
hh3cOnuBindType = _Hh3cOnuBindType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 7, 1, 2),
    _Hh3cOnuBindType_Type()
)
hh3cOnuBindType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuBindType.setStatus("current")
_Hh3cOnuFirmwareUpdateTable_Object = MibTable
hh3cOnuFirmwareUpdateTable = _Hh3cOnuFirmwareUpdateTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 8)
)
if mibBuilder.loadTexts:
    hh3cOnuFirmwareUpdateTable.setStatus("current")
_Hh3cOnuFirmwareUpdateEntry_Object = MibTableRow
hh3cOnuFirmwareUpdateEntry = _Hh3cOnuFirmwareUpdateEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 8, 1)
)
hh3cOnuFirmwareUpdateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cOnuFirmwareUpdateEntry.setStatus("current")


class _Hh3cOnuUpdate_Type(Integer32):
    """Custom type hh3cOnuUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("update", 1)
    )


_Hh3cOnuUpdate_Type.__name__ = "Integer32"
_Hh3cOnuUpdate_Object = MibTableColumn
hh3cOnuUpdate = _Hh3cOnuUpdate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 8, 1, 1),
    _Hh3cOnuUpdate_Type()
)
hh3cOnuUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuUpdate.setStatus("current")


class _Hh3cOnuUpdateResult_Type(Integer32):
    """Custom type hh3cOnuUpdateResult based on Integer32"""
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


_Hh3cOnuUpdateResult_Type.__name__ = "Integer32"
_Hh3cOnuUpdateResult_Object = MibTableColumn
hh3cOnuUpdateResult = _Hh3cOnuUpdateResult_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 8, 1, 2),
    _Hh3cOnuUpdateResult_Type()
)
hh3cOnuUpdateResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuUpdateResult.setStatus("current")


class _Hh3cOnuUpdateFileName_Type(OctetString):
    """Custom type hh3cOnuUpdateFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cOnuUpdateFileName_Type.__name__ = "OctetString"
_Hh3cOnuUpdateFileName_Object = MibTableColumn
hh3cOnuUpdateFileName = _Hh3cOnuUpdateFileName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 8, 1, 3),
    _Hh3cOnuUpdateFileName_Type()
)
hh3cOnuUpdateFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuUpdateFileName.setStatus("current")
_Hh3cOnuLinkTestFrameNumMinVal_Type = Integer32
_Hh3cOnuLinkTestFrameNumMinVal_Object = MibScalar
hh3cOnuLinkTestFrameNumMinVal = _Hh3cOnuLinkTestFrameNumMinVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 9),
    _Hh3cOnuLinkTestFrameNumMinVal_Type()
)
hh3cOnuLinkTestFrameNumMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuLinkTestFrameNumMinVal.setStatus("current")
_Hh3cOnuLinkTestFrameNumMaxVal_Type = Integer32
_Hh3cOnuLinkTestFrameNumMaxVal_Object = MibScalar
hh3cOnuLinkTestFrameNumMaxVal = _Hh3cOnuLinkTestFrameNumMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 10),
    _Hh3cOnuLinkTestFrameNumMaxVal_Type()
)
hh3cOnuLinkTestFrameNumMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuLinkTestFrameNumMaxVal.setStatus("current")
_Hh3cOnuSlaMaxBandWidthMinVal_Type = Integer32
_Hh3cOnuSlaMaxBandWidthMinVal_Object = MibScalar
hh3cOnuSlaMaxBandWidthMinVal = _Hh3cOnuSlaMaxBandWidthMinVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 11),
    _Hh3cOnuSlaMaxBandWidthMinVal_Type()
)
hh3cOnuSlaMaxBandWidthMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuSlaMaxBandWidthMinVal.setStatus("current")
_Hh3cOnuSlaMaxBandWidthMaxVal_Type = Integer32
_Hh3cOnuSlaMaxBandWidthMaxVal_Object = MibScalar
hh3cOnuSlaMaxBandWidthMaxVal = _Hh3cOnuSlaMaxBandWidthMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 12),
    _Hh3cOnuSlaMaxBandWidthMaxVal_Type()
)
hh3cOnuSlaMaxBandWidthMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuSlaMaxBandWidthMaxVal.setStatus("current")
_Hh3cOnuSlaMinBandWidthMinVal_Type = Integer32
_Hh3cOnuSlaMinBandWidthMinVal_Object = MibScalar
hh3cOnuSlaMinBandWidthMinVal = _Hh3cOnuSlaMinBandWidthMinVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 13),
    _Hh3cOnuSlaMinBandWidthMinVal_Type()
)
hh3cOnuSlaMinBandWidthMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuSlaMinBandWidthMinVal.setStatus("current")
_Hh3cOnuSlaMinBandWidthMaxVal_Type = Integer32
_Hh3cOnuSlaMinBandWidthMaxVal_Object = MibScalar
hh3cOnuSlaMinBandWidthMaxVal = _Hh3cOnuSlaMinBandWidthMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 14),
    _Hh3cOnuSlaMinBandWidthMaxVal_Type()
)
hh3cOnuSlaMinBandWidthMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuSlaMinBandWidthMaxVal.setStatus("current")
_Hh3cEponOnuTypeManTable_Object = MibTable
hh3cEponOnuTypeManTable = _Hh3cEponOnuTypeManTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 15)
)
if mibBuilder.loadTexts:
    hh3cEponOnuTypeManTable.setStatus("current")
_Hh3cEponOnuTypeManEntry_Object = MibTableRow
hh3cEponOnuTypeManEntry = _Hh3cEponOnuTypeManEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 15, 1)
)
hh3cEponOnuTypeManEntry.setIndexNames(
    (0, "HH3C-EPON-MIB", "hh3cEponOnuTypeIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponOnuTypeManEntry.setStatus("current")
_Hh3cEponOnuTypeIndex_Type = Integer32
_Hh3cEponOnuTypeIndex_Object = MibTableColumn
hh3cEponOnuTypeIndex = _Hh3cEponOnuTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 15, 1, 1),
    _Hh3cEponOnuTypeIndex_Type()
)
hh3cEponOnuTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEponOnuTypeIndex.setStatus("current")
_Hh3cEponOnuTypeDescr_Type = OctetString
_Hh3cEponOnuTypeDescr_Object = MibTableColumn
hh3cEponOnuTypeDescr = _Hh3cEponOnuTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 15, 1, 2),
    _Hh3cEponOnuTypeDescr_Type()
)
hh3cEponOnuTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponOnuTypeDescr.setStatus("current")
_Hh3cOnuPacketManTable_Object = MibTable
hh3cOnuPacketManTable = _Hh3cOnuPacketManTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 16)
)
if mibBuilder.loadTexts:
    hh3cOnuPacketManTable.setStatus("current")
_Hh3cOnuPacketManEntry_Object = MibTableRow
hh3cOnuPacketManEntry = _Hh3cOnuPacketManEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 16, 1)
)
hh3cOnuPacketManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cOnuPacketManEntry.setStatus("current")


class _Hh3cOnuPriorityTrust_Type(Integer32):
    """Custom type hh3cOnuPriorityTrust based on Integer32"""
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


_Hh3cOnuPriorityTrust_Type.__name__ = "Integer32"
_Hh3cOnuPriorityTrust_Object = MibTableColumn
hh3cOnuPriorityTrust = _Hh3cOnuPriorityTrust_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 16, 1, 1),
    _Hh3cOnuPriorityTrust_Type()
)
hh3cOnuPriorityTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuPriorityTrust.setStatus("current")


class _Hh3cOnuQueueScheduler_Type(Integer32):
    """Custom type hh3cOnuQueueScheduler based on Integer32"""
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


_Hh3cOnuQueueScheduler_Type.__name__ = "Integer32"
_Hh3cOnuQueueScheduler_Object = MibTableColumn
hh3cOnuQueueScheduler = _Hh3cOnuQueueScheduler_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 16, 1, 2),
    _Hh3cOnuQueueScheduler_Type()
)
hh3cOnuQueueScheduler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuQueueScheduler.setStatus("current")
_Hh3cOnuProtocolTable_Object = MibTable
hh3cOnuProtocolTable = _Hh3cOnuProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 17)
)
if mibBuilder.loadTexts:
    hh3cOnuProtocolTable.setStatus("current")
_Hh3cOnuProtocolEntry_Object = MibTableRow
hh3cOnuProtocolEntry = _Hh3cOnuProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 17, 1)
)
hh3cOnuProtocolEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cOnuProtocolEntry.setStatus("current")


class _Hh3cOnuStpStatus_Type(TruthValue):
    """Custom type hh3cOnuStpStatus based on TruthValue"""


_Hh3cOnuStpStatus_Object = MibTableColumn
hh3cOnuStpStatus = _Hh3cOnuStpStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 17, 1, 1),
    _Hh3cOnuStpStatus_Type()
)
hh3cOnuStpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuStpStatus.setStatus("current")


class _Hh3cOnuIgmpSnoopingStatus_Type(TruthValue):
    """Custom type hh3cOnuIgmpSnoopingStatus based on TruthValue"""


_Hh3cOnuIgmpSnoopingStatus_Object = MibTableColumn
hh3cOnuIgmpSnoopingStatus = _Hh3cOnuIgmpSnoopingStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 17, 1, 2),
    _Hh3cOnuIgmpSnoopingStatus_Type()
)
hh3cOnuIgmpSnoopingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuIgmpSnoopingStatus.setStatus("current")


class _Hh3cOnuDhcpsnoopingOption82_Type(TruthValue):
    """Custom type hh3cOnuDhcpsnoopingOption82 based on TruthValue"""


_Hh3cOnuDhcpsnoopingOption82_Object = MibTableColumn
hh3cOnuDhcpsnoopingOption82 = _Hh3cOnuDhcpsnoopingOption82_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 17, 1, 3),
    _Hh3cOnuDhcpsnoopingOption82_Type()
)
hh3cOnuDhcpsnoopingOption82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuDhcpsnoopingOption82.setStatus("current")


class _Hh3cOnuDhcpsnooping_Type(TruthValue):
    """Custom type hh3cOnuDhcpsnooping based on TruthValue"""


_Hh3cOnuDhcpsnooping_Object = MibTableColumn
hh3cOnuDhcpsnooping = _Hh3cOnuDhcpsnooping_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 17, 1, 4),
    _Hh3cOnuDhcpsnooping_Type()
)
hh3cOnuDhcpsnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuDhcpsnooping.setStatus("current")


class _Hh3cOnuPppoe_Type(TruthValue):
    """Custom type hh3cOnuPppoe based on TruthValue"""


_Hh3cOnuPppoe_Object = MibTableColumn
hh3cOnuPppoe = _Hh3cOnuPppoe_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 17, 1, 5),
    _Hh3cOnuPppoe_Type()
)
hh3cOnuPppoe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuPppoe.setStatus("current")
_Hh3cOnuIgmpSnoopingHostAgingT_Type = Integer32
_Hh3cOnuIgmpSnoopingHostAgingT_Object = MibTableColumn
hh3cOnuIgmpSnoopingHostAgingT = _Hh3cOnuIgmpSnoopingHostAgingT_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 17, 1, 6),
    _Hh3cOnuIgmpSnoopingHostAgingT_Type()
)
hh3cOnuIgmpSnoopingHostAgingT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuIgmpSnoopingHostAgingT.setStatus("current")
_Hh3cOnuIgmpSnoopingMaxRespT_Type = Integer32
_Hh3cOnuIgmpSnoopingMaxRespT_Object = MibTableColumn
hh3cOnuIgmpSnoopingMaxRespT = _Hh3cOnuIgmpSnoopingMaxRespT_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 17, 1, 7),
    _Hh3cOnuIgmpSnoopingMaxRespT_Type()
)
hh3cOnuIgmpSnoopingMaxRespT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuIgmpSnoopingMaxRespT.setStatus("current")
_Hh3cOnuIgmpSnoopingRouterAgingT_Type = Integer32
_Hh3cOnuIgmpSnoopingRouterAgingT_Object = MibTableColumn
hh3cOnuIgmpSnoopingRouterAgingT = _Hh3cOnuIgmpSnoopingRouterAgingT_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 17, 1, 8),
    _Hh3cOnuIgmpSnoopingRouterAgingT_Type()
)
hh3cOnuIgmpSnoopingRouterAgingT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuIgmpSnoopingRouterAgingT.setStatus("current")


class _Hh3cOnuIgmpSnoopingAggReportS_Type(TruthValue):
    """Custom type hh3cOnuIgmpSnoopingAggReportS based on TruthValue"""


_Hh3cOnuIgmpSnoopingAggReportS_Object = MibTableColumn
hh3cOnuIgmpSnoopingAggReportS = _Hh3cOnuIgmpSnoopingAggReportS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 17, 1, 9),
    _Hh3cOnuIgmpSnoopingAggReportS_Type()
)
hh3cOnuIgmpSnoopingAggReportS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuIgmpSnoopingAggReportS.setStatus("current")


class _Hh3cOnuIgmpSnoopingAggLeaveS_Type(TruthValue):
    """Custom type hh3cOnuIgmpSnoopingAggLeaveS based on TruthValue"""


_Hh3cOnuIgmpSnoopingAggLeaveS_Object = MibTableColumn
hh3cOnuIgmpSnoopingAggLeaveS = _Hh3cOnuIgmpSnoopingAggLeaveS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 17, 1, 10),
    _Hh3cOnuIgmpSnoopingAggLeaveS_Type()
)
hh3cOnuIgmpSnoopingAggLeaveS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuIgmpSnoopingAggLeaveS.setStatus("current")
_Hh3cOnuDot1xTable_Object = MibTable
hh3cOnuDot1xTable = _Hh3cOnuDot1xTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 18)
)
if mibBuilder.loadTexts:
    hh3cOnuDot1xTable.setStatus("current")
_Hh3cOnuDot1xEntry_Object = MibTableRow
hh3cOnuDot1xEntry = _Hh3cOnuDot1xEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 18, 1)
)
hh3cOnuDot1xEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cOnuDot1xEntry.setStatus("current")
_Hh3cOnuDot1xAccount_Type = OctetString
_Hh3cOnuDot1xAccount_Object = MibTableColumn
hh3cOnuDot1xAccount = _Hh3cOnuDot1xAccount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 18, 1, 1),
    _Hh3cOnuDot1xAccount_Type()
)
hh3cOnuDot1xAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuDot1xAccount.setStatus("current")
_Hh3cOnuDot1xPassword_Type = OctetString
_Hh3cOnuDot1xPassword_Object = MibTableColumn
hh3cOnuDot1xPassword = _Hh3cOnuDot1xPassword_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 18, 1, 2),
    _Hh3cOnuDot1xPassword_Type()
)
hh3cOnuDot1xPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuDot1xPassword.setStatus("current")
_Hh3cOnuPriorityQueueTable_Object = MibTable
hh3cOnuPriorityQueueTable = _Hh3cOnuPriorityQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 19)
)
if mibBuilder.loadTexts:
    hh3cOnuPriorityQueueTable.setStatus("current")
_Hh3cOnuPriorityQueueEntry_Object = MibTableRow
hh3cOnuPriorityQueueEntry = _Hh3cOnuPriorityQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 19, 1)
)
hh3cOnuPriorityQueueEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-MIB", "hh3cOnuQueueDirection"),
    (0, "HH3C-EPON-MIB", "hh3cOnuQueueId"),
)
if mibBuilder.loadTexts:
    hh3cOnuPriorityQueueEntry.setStatus("current")


class _Hh3cOnuQueueDirection_Type(Integer32):
    """Custom type hh3cOnuQueueDirection based on Integer32"""
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


_Hh3cOnuQueueDirection_Type.__name__ = "Integer32"
_Hh3cOnuQueueDirection_Object = MibTableColumn
hh3cOnuQueueDirection = _Hh3cOnuQueueDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 19, 1, 1),
    _Hh3cOnuQueueDirection_Type()
)
hh3cOnuQueueDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cOnuQueueDirection.setStatus("current")


class _Hh3cOnuQueueId_Type(Integer32):
    """Custom type hh3cOnuQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cOnuQueueId_Type.__name__ = "Integer32"
_Hh3cOnuQueueId_Object = MibTableColumn
hh3cOnuQueueId = _Hh3cOnuQueueId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 19, 1, 2),
    _Hh3cOnuQueueId_Type()
)
hh3cOnuQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cOnuQueueId.setStatus("current")
_Hh3cOnuQueueSize_Type = Integer32
_Hh3cOnuQueueSize_Object = MibTableColumn
hh3cOnuQueueSize = _Hh3cOnuQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 19, 1, 3),
    _Hh3cOnuQueueSize_Type()
)
hh3cOnuQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuQueueSize.setStatus("current")
_Hh3cOnuCountTable_Object = MibTable
hh3cOnuCountTable = _Hh3cOnuCountTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 20)
)
if mibBuilder.loadTexts:
    hh3cOnuCountTable.setStatus("current")
_Hh3cOnuCountEntry_Object = MibTableRow
hh3cOnuCountEntry = _Hh3cOnuCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 20, 1)
)
hh3cOnuCountEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cOnuCountEntry.setStatus("current")
_Hh3cOnuInCRCErrPkts_Type = Counter64
_Hh3cOnuInCRCErrPkts_Object = MibTableColumn
hh3cOnuInCRCErrPkts = _Hh3cOnuInCRCErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 20, 1, 1),
    _Hh3cOnuInCRCErrPkts_Type()
)
hh3cOnuInCRCErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuInCRCErrPkts.setStatus("current")
_Hh3cOnuOutDroppedFrames_Type = Counter64
_Hh3cOnuOutDroppedFrames_Object = MibTableColumn
hh3cOnuOutDroppedFrames = _Hh3cOnuOutDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 20, 1, 2),
    _Hh3cOnuOutDroppedFrames_Type()
)
hh3cOnuOutDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuOutDroppedFrames.setStatus("current")
_Hh3cEponOnuScalarGroup_ObjectIdentity = ObjectIdentity
hh3cEponOnuScalarGroup = _Hh3cEponOnuScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 21)
)
_Hh3cOnuPriorityQueueSizeMinVal_Type = Integer32
_Hh3cOnuPriorityQueueSizeMinVal_Object = MibScalar
hh3cOnuPriorityQueueSizeMinVal = _Hh3cOnuPriorityQueueSizeMinVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 21, 1),
    _Hh3cOnuPriorityQueueSizeMinVal_Type()
)
hh3cOnuPriorityQueueSizeMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuPriorityQueueSizeMinVal.setStatus("current")
_Hh3cOnuPriorityQueueSizeMaxVal_Type = Integer32
_Hh3cOnuPriorityQueueSizeMaxVal_Object = MibScalar
hh3cOnuPriorityQueueSizeMaxVal = _Hh3cOnuPriorityQueueSizeMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 21, 2),
    _Hh3cOnuPriorityQueueSizeMaxVal_Type()
)
hh3cOnuPriorityQueueSizeMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuPriorityQueueSizeMaxVal.setStatus("current")
_Hh3cOnuPriorityQueueBandwidthMinVal_Type = Integer32
_Hh3cOnuPriorityQueueBandwidthMinVal_Object = MibScalar
hh3cOnuPriorityQueueBandwidthMinVal = _Hh3cOnuPriorityQueueBandwidthMinVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 21, 3),
    _Hh3cOnuPriorityQueueBandwidthMinVal_Type()
)
hh3cOnuPriorityQueueBandwidthMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuPriorityQueueBandwidthMinVal.setStatus("current")
_Hh3cOnuPriorityQueueBandwidthMaxVal_Type = Integer32
_Hh3cOnuPriorityQueueBandwidthMaxVal_Object = MibScalar
hh3cOnuPriorityQueueBandwidthMaxVal = _Hh3cOnuPriorityQueueBandwidthMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 21, 4),
    _Hh3cOnuPriorityQueueBandwidthMaxVal_Type()
)
hh3cOnuPriorityQueueBandwidthMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuPriorityQueueBandwidthMaxVal.setStatus("current")
_Hh3cOnuPriorityQueueBurstsizeMinVal_Type = Integer32
_Hh3cOnuPriorityQueueBurstsizeMinVal_Object = MibScalar
hh3cOnuPriorityQueueBurstsizeMinVal = _Hh3cOnuPriorityQueueBurstsizeMinVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 21, 5),
    _Hh3cOnuPriorityQueueBurstsizeMinVal_Type()
)
hh3cOnuPriorityQueueBurstsizeMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuPriorityQueueBurstsizeMinVal.setStatus("current")
_Hh3cOnuPriorityQueueBurstsizeMaxVal_Type = Integer32
_Hh3cOnuPriorityQueueBurstsizeMaxVal_Object = MibScalar
hh3cOnuPriorityQueueBurstsizeMaxVal = _Hh3cOnuPriorityQueueBurstsizeMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 21, 6),
    _Hh3cOnuPriorityQueueBurstsizeMaxVal_Type()
)
hh3cOnuPriorityQueueBurstsizeMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuPriorityQueueBurstsizeMaxVal.setStatus("current")
_Hh3cOnuUpdateByTypeNextIndex_Type = Integer32
_Hh3cOnuUpdateByTypeNextIndex_Object = MibScalar
hh3cOnuUpdateByTypeNextIndex = _Hh3cOnuUpdateByTypeNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 21, 7),
    _Hh3cOnuUpdateByTypeNextIndex_Type()
)
hh3cOnuUpdateByTypeNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuUpdateByTypeNextIndex.setStatus("current")
_Hh3cOnuQueueBandwidthTable_Object = MibTable
hh3cOnuQueueBandwidthTable = _Hh3cOnuQueueBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 22)
)
if mibBuilder.loadTexts:
    hh3cOnuQueueBandwidthTable.setStatus("current")
_Hh3cOnuQueueBandwidthEntry_Object = MibTableRow
hh3cOnuQueueBandwidthEntry = _Hh3cOnuQueueBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 22, 1)
)
hh3cOnuQueueBandwidthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-MIB", "hh3cOnuQueueDirection"),
    (0, "HH3C-EPON-MIB", "hh3cOnuQueueId"),
)
if mibBuilder.loadTexts:
    hh3cOnuQueueBandwidthEntry.setStatus("current")
_Hh3cOnuQueueMaxBandwidth_Type = Integer32
_Hh3cOnuQueueMaxBandwidth_Object = MibTableColumn
hh3cOnuQueueMaxBandwidth = _Hh3cOnuQueueMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 22, 1, 1),
    _Hh3cOnuQueueMaxBandwidth_Type()
)
hh3cOnuQueueMaxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuQueueMaxBandwidth.setStatus("current")
_Hh3cOnuQueueMaxBurstsize_Type = Integer32
_Hh3cOnuQueueMaxBurstsize_Object = MibTableColumn
hh3cOnuQueueMaxBurstsize = _Hh3cOnuQueueMaxBurstsize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 22, 1, 2),
    _Hh3cOnuQueueMaxBurstsize_Type()
)
hh3cOnuQueueMaxBurstsize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuQueueMaxBurstsize.setStatus("current")
_Hh3cOnuQueuePolicyStatus_Type = TruthValue
_Hh3cOnuQueuePolicyStatus_Object = MibTableColumn
hh3cOnuQueuePolicyStatus = _Hh3cOnuQueuePolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 22, 1, 3),
    _Hh3cOnuQueuePolicyStatus_Type()
)
hh3cOnuQueuePolicyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuQueuePolicyStatus.setStatus("current")
_Hh3cOnuIpAddressTable_Object = MibTable
hh3cOnuIpAddressTable = _Hh3cOnuIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 23)
)
if mibBuilder.loadTexts:
    hh3cOnuIpAddressTable.setStatus("current")
_Hh3cOnuIpAddressEntry_Object = MibTableRow
hh3cOnuIpAddressEntry = _Hh3cOnuIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 23, 1)
)
hh3cOnuIpAddressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cOnuIpAddressEntry.setStatus("current")
_Hh3cOnuIpAddress_Type = IpAddress
_Hh3cOnuIpAddress_Object = MibTableColumn
hh3cOnuIpAddress = _Hh3cOnuIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 23, 1, 1),
    _Hh3cOnuIpAddress_Type()
)
hh3cOnuIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuIpAddress.setStatus("current")
_Hh3cOnuIpAddressMask_Type = IpAddress
_Hh3cOnuIpAddressMask_Object = MibTableColumn
hh3cOnuIpAddressMask = _Hh3cOnuIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 23, 1, 2),
    _Hh3cOnuIpAddressMask_Type()
)
hh3cOnuIpAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuIpAddressMask.setStatus("current")
_Hh3cOnuIpAddressGateway_Type = IpAddress
_Hh3cOnuIpAddressGateway_Object = MibTableColumn
hh3cOnuIpAddressGateway = _Hh3cOnuIpAddressGateway_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 23, 1, 3),
    _Hh3cOnuIpAddressGateway_Type()
)
hh3cOnuIpAddressGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuIpAddressGateway.setStatus("current")
_Hh3cOnuDhcpallocate_Type = TruthValue
_Hh3cOnuDhcpallocate_Object = MibTableColumn
hh3cOnuDhcpallocate = _Hh3cOnuDhcpallocate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 23, 1, 4),
    _Hh3cOnuDhcpallocate_Type()
)
hh3cOnuDhcpallocate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuDhcpallocate.setStatus("current")
_Hh3cOnuManageVID_Type = Integer32
_Hh3cOnuManageVID_Object = MibTableColumn
hh3cOnuManageVID = _Hh3cOnuManageVID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 23, 1, 5),
    _Hh3cOnuManageVID_Type()
)
hh3cOnuManageVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuManageVID.setStatus("current")
_Hh3cOnuManageVlanIntfS_Type = TruthValue
_Hh3cOnuManageVlanIntfS_Object = MibTableColumn
hh3cOnuManageVlanIntfS = _Hh3cOnuManageVlanIntfS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 23, 1, 6),
    _Hh3cOnuManageVlanIntfS_Type()
)
hh3cOnuManageVlanIntfS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuManageVlanIntfS.setStatus("current")
_Hh3cOnuChipSetInfoTable_Object = MibTable
hh3cOnuChipSetInfoTable = _Hh3cOnuChipSetInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 24)
)
if mibBuilder.loadTexts:
    hh3cOnuChipSetInfoTable.setStatus("current")
_Hh3cOnuChipSetInfoEntry_Object = MibTableRow
hh3cOnuChipSetInfoEntry = _Hh3cOnuChipSetInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 24, 1)
)
hh3cOnuChipSetInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cOnuChipSetInfoEntry.setStatus("current")


class _Hh3cOnuChipSetVendorId_Type(OctetString):
    """Custom type hh3cOnuChipSetVendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cOnuChipSetVendorId_Type.__name__ = "OctetString"
_Hh3cOnuChipSetVendorId_Object = MibTableColumn
hh3cOnuChipSetVendorId = _Hh3cOnuChipSetVendorId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 24, 1, 1),
    _Hh3cOnuChipSetVendorId_Type()
)
hh3cOnuChipSetVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuChipSetVendorId.setStatus("current")


class _Hh3cOnuChipSetModel_Type(OctetString):
    """Custom type hh3cOnuChipSetModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cOnuChipSetModel_Type.__name__ = "OctetString"
_Hh3cOnuChipSetModel_Object = MibTableColumn
hh3cOnuChipSetModel = _Hh3cOnuChipSetModel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 24, 1, 2),
    _Hh3cOnuChipSetModel_Type()
)
hh3cOnuChipSetModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuChipSetModel.setStatus("current")
_Hh3cOnuChipSetRevision_Type = Integer32
_Hh3cOnuChipSetRevision_Object = MibTableColumn
hh3cOnuChipSetRevision = _Hh3cOnuChipSetRevision_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 24, 1, 3),
    _Hh3cOnuChipSetRevision_Type()
)
hh3cOnuChipSetRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuChipSetRevision.setStatus("current")
_Hh3cOnuChipSetDesignDate_Type = DateAndTime
_Hh3cOnuChipSetDesignDate_Object = MibTableColumn
hh3cOnuChipSetDesignDate = _Hh3cOnuChipSetDesignDate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 24, 1, 4),
    _Hh3cOnuChipSetDesignDate_Type()
)
hh3cOnuChipSetDesignDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuChipSetDesignDate.setStatus("current")
_Hh3cOnuCapabilityTable_Object = MibTable
hh3cOnuCapabilityTable = _Hh3cOnuCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 25)
)
if mibBuilder.loadTexts:
    hh3cOnuCapabilityTable.setStatus("current")
_Hh3cOnuCapabilityEntry_Object = MibTableRow
hh3cOnuCapabilityEntry = _Hh3cOnuCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 25, 1)
)
hh3cOnuCapabilityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cOnuCapabilityEntry.setStatus("current")


class _Hh3cOnuServiceSupported_Type(Bits):
    """Custom type hh3cOnuServiceSupported based on Bits"""
    namedValues = NamedValues(
        *(("feinterfacesupport", 1),
          ("geinterfacesupport", 0),
          ("tdmservicesupport", 3),
          ("voipservicesupport", 2))
    )

_Hh3cOnuServiceSupported_Type.__name__ = "Bits"
_Hh3cOnuServiceSupported_Object = MibTableColumn
hh3cOnuServiceSupported = _Hh3cOnuServiceSupported_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 25, 1, 1),
    _Hh3cOnuServiceSupported_Type()
)
hh3cOnuServiceSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuServiceSupported.setStatus("current")
_Hh3cOnuGEPortNumber_Type = Integer32
_Hh3cOnuGEPortNumber_Object = MibTableColumn
hh3cOnuGEPortNumber = _Hh3cOnuGEPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 25, 1, 2),
    _Hh3cOnuGEPortNumber_Type()
)
hh3cOnuGEPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuGEPortNumber.setStatus("current")
_Hh3cOnuFEPortNumber_Type = Integer32
_Hh3cOnuFEPortNumber_Object = MibTableColumn
hh3cOnuFEPortNumber = _Hh3cOnuFEPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 25, 1, 3),
    _Hh3cOnuFEPortNumber_Type()
)
hh3cOnuFEPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuFEPortNumber.setStatus("current")
_Hh3cOnuPOTSPortNumber_Type = Integer32
_Hh3cOnuPOTSPortNumber_Object = MibTableColumn
hh3cOnuPOTSPortNumber = _Hh3cOnuPOTSPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 25, 1, 4),
    _Hh3cOnuPOTSPortNumber_Type()
)
hh3cOnuPOTSPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuPOTSPortNumber.setStatus("current")
_Hh3cOnuE1PortsNumber_Type = Integer32
_Hh3cOnuE1PortsNumber_Object = MibTableColumn
hh3cOnuE1PortsNumber = _Hh3cOnuE1PortsNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 25, 1, 5),
    _Hh3cOnuE1PortsNumber_Type()
)
hh3cOnuE1PortsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuE1PortsNumber.setStatus("current")
_Hh3cOnuUpstreamQueueNumber_Type = Integer32
_Hh3cOnuUpstreamQueueNumber_Object = MibTableColumn
hh3cOnuUpstreamQueueNumber = _Hh3cOnuUpstreamQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 25, 1, 6),
    _Hh3cOnuUpstreamQueueNumber_Type()
)
hh3cOnuUpstreamQueueNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuUpstreamQueueNumber.setStatus("current")
_Hh3cOnuMaxUpstreamQueuePerPort_Type = Integer32
_Hh3cOnuMaxUpstreamQueuePerPort_Object = MibTableColumn
hh3cOnuMaxUpstreamQueuePerPort = _Hh3cOnuMaxUpstreamQueuePerPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 25, 1, 7),
    _Hh3cOnuMaxUpstreamQueuePerPort_Type()
)
hh3cOnuMaxUpstreamQueuePerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuMaxUpstreamQueuePerPort.setStatus("current")
_Hh3cOnuDownstreamQueueNumber_Type = Integer32
_Hh3cOnuDownstreamQueueNumber_Object = MibTableColumn
hh3cOnuDownstreamQueueNumber = _Hh3cOnuDownstreamQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 25, 1, 8),
    _Hh3cOnuDownstreamQueueNumber_Type()
)
hh3cOnuDownstreamQueueNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuDownstreamQueueNumber.setStatus("current")
_Hh3cOnuMaxDownstreamQueuePerPort_Type = Integer32
_Hh3cOnuMaxDownstreamQueuePerPort_Object = MibTableColumn
hh3cOnuMaxDownstreamQueuePerPort = _Hh3cOnuMaxDownstreamQueuePerPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 25, 1, 9),
    _Hh3cOnuMaxDownstreamQueuePerPort_Type()
)
hh3cOnuMaxDownstreamQueuePerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuMaxDownstreamQueuePerPort.setStatus("current")
_Hh3cOnuBatteryBackup_Type = TruthValue
_Hh3cOnuBatteryBackup_Object = MibTableColumn
hh3cOnuBatteryBackup = _Hh3cOnuBatteryBackup_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 25, 1, 10),
    _Hh3cOnuBatteryBackup_Type()
)
hh3cOnuBatteryBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuBatteryBackup.setStatus("current")
_Hh3cOnuIgspFastLeaveSupported_Type = TruthValue
_Hh3cOnuIgspFastLeaveSupported_Object = MibTableColumn
hh3cOnuIgspFastLeaveSupported = _Hh3cOnuIgspFastLeaveSupported_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 25, 1, 11),
    _Hh3cOnuIgspFastLeaveSupported_Type()
)
hh3cOnuIgspFastLeaveSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuIgspFastLeaveSupported.setStatus("current")
_Hh3cOnuMCtrlFastLeaveSupported_Type = TruthValue
_Hh3cOnuMCtrlFastLeaveSupported_Object = MibTableColumn
hh3cOnuMCtrlFastLeaveSupported = _Hh3cOnuMCtrlFastLeaveSupported_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 25, 1, 12),
    _Hh3cOnuMCtrlFastLeaveSupported_Type()
)
hh3cOnuMCtrlFastLeaveSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuMCtrlFastLeaveSupported.setStatus("current")
_Hh3cOnuDbaReportTable_Object = MibTable
hh3cOnuDbaReportTable = _Hh3cOnuDbaReportTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 26)
)
if mibBuilder.loadTexts:
    hh3cOnuDbaReportTable.setStatus("current")
_Hh3cOnuDbaReportEntry_Object = MibTableRow
hh3cOnuDbaReportEntry = _Hh3cOnuDbaReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 26, 1)
)
hh3cOnuDbaReportEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-MIB", "hh3cOnuDbaReportQueueId"),
)
if mibBuilder.loadTexts:
    hh3cOnuDbaReportEntry.setStatus("current")
_Hh3cOnuDbaReportQueueId_Type = Integer32
_Hh3cOnuDbaReportQueueId_Object = MibTableColumn
hh3cOnuDbaReportQueueId = _Hh3cOnuDbaReportQueueId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 26, 1, 1),
    _Hh3cOnuDbaReportQueueId_Type()
)
hh3cOnuDbaReportQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cOnuDbaReportQueueId.setStatus("current")
_Hh3cOnuDbaReportThreshold_Type = Integer32
_Hh3cOnuDbaReportThreshold_Object = MibTableColumn
hh3cOnuDbaReportThreshold = _Hh3cOnuDbaReportThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 26, 1, 2),
    _Hh3cOnuDbaReportThreshold_Type()
)
hh3cOnuDbaReportThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuDbaReportThreshold.setStatus("current")


class _Hh3cOnuDbaReportStatus_Type(Integer32):
    """Custom type hh3cOnuDbaReportStatus based on Integer32"""
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


_Hh3cOnuDbaReportStatus_Type.__name__ = "Integer32"
_Hh3cOnuDbaReportStatus_Object = MibTableColumn
hh3cOnuDbaReportStatus = _Hh3cOnuDbaReportStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 26, 1, 3),
    _Hh3cOnuDbaReportStatus_Type()
)
hh3cOnuDbaReportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuDbaReportStatus.setStatus("current")
_Hh3cOnuCosToLocalPrecedenceTable_Object = MibTable
hh3cOnuCosToLocalPrecedenceTable = _Hh3cOnuCosToLocalPrecedenceTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 27)
)
if mibBuilder.loadTexts:
    hh3cOnuCosToLocalPrecedenceTable.setStatus("current")
_Hh3cOnuCosToLocalPrecedenceEntry_Object = MibTableRow
hh3cOnuCosToLocalPrecedenceEntry = _Hh3cOnuCosToLocalPrecedenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 27, 1)
)
hh3cOnuCosToLocalPrecedenceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-MIB", "hh3cOnuCosToLocalPrecedenceCosIndex"),
)
if mibBuilder.loadTexts:
    hh3cOnuCosToLocalPrecedenceEntry.setStatus("current")


class _Hh3cOnuCosToLocalPrecedenceCosIndex_Type(Integer32):
    """Custom type hh3cOnuCosToLocalPrecedenceCosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cOnuCosToLocalPrecedenceCosIndex_Type.__name__ = "Integer32"
_Hh3cOnuCosToLocalPrecedenceCosIndex_Object = MibTableColumn
hh3cOnuCosToLocalPrecedenceCosIndex = _Hh3cOnuCosToLocalPrecedenceCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 27, 1, 1),
    _Hh3cOnuCosToLocalPrecedenceCosIndex_Type()
)
hh3cOnuCosToLocalPrecedenceCosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuCosToLocalPrecedenceCosIndex.setStatus("current")


class _Hh3cOnuCosToLocalPrecedenceValue_Type(Integer32):
    """Custom type hh3cOnuCosToLocalPrecedenceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cOnuCosToLocalPrecedenceValue_Type.__name__ = "Integer32"
_Hh3cOnuCosToLocalPrecedenceValue_Object = MibTableColumn
hh3cOnuCosToLocalPrecedenceValue = _Hh3cOnuCosToLocalPrecedenceValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 27, 1, 2),
    _Hh3cOnuCosToLocalPrecedenceValue_Type()
)
hh3cOnuCosToLocalPrecedenceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuCosToLocalPrecedenceValue.setStatus("current")
_Hh3cEponOnuStpPortTable_Object = MibTable
hh3cEponOnuStpPortTable = _Hh3cEponOnuStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 28)
)
if mibBuilder.loadTexts:
    hh3cEponOnuStpPortTable.setStatus("current")
_Hh3cEponOnuStpPortEntry_Object = MibTableRow
hh3cEponOnuStpPortEntry = _Hh3cEponOnuStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 28, 1)
)
hh3cEponOnuStpPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-MIB", "hh3cEponStpPortIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponOnuStpPortEntry.setStatus("current")


class _Hh3cEponStpPortIndex_Type(Integer32):
    """Custom type hh3cEponStpPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 144),
    )


_Hh3cEponStpPortIndex_Type.__name__ = "Integer32"
_Hh3cEponStpPortIndex_Object = MibTableColumn
hh3cEponStpPortIndex = _Hh3cEponStpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 28, 1, 1),
    _Hh3cEponStpPortIndex_Type()
)
hh3cEponStpPortIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cEponStpPortIndex.setStatus("current")
_Hh3cEponStpPortDescr_Type = OctetString
_Hh3cEponStpPortDescr_Object = MibTableColumn
hh3cEponStpPortDescr = _Hh3cEponStpPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 28, 1, 2),
    _Hh3cEponStpPortDescr_Type()
)
hh3cEponStpPortDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cEponStpPortDescr.setStatus("current")


class _Hh3cEponStpPortState_Type(Integer32):
    """Custom type hh3cEponStpPortState based on Integer32"""
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


_Hh3cEponStpPortState_Type.__name__ = "Integer32"
_Hh3cEponStpPortState_Object = MibTableColumn
hh3cEponStpPortState = _Hh3cEponStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 28, 1, 3),
    _Hh3cEponStpPortState_Type()
)
hh3cEponStpPortState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cEponStpPortState.setStatus("current")
_Hh3cOnuPhysicalTable_Object = MibTable
hh3cOnuPhysicalTable = _Hh3cOnuPhysicalTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 29)
)
if mibBuilder.loadTexts:
    hh3cOnuPhysicalTable.setStatus("current")
_Hh3cOnuPhysicalEntry_Object = MibTableRow
hh3cOnuPhysicalEntry = _Hh3cOnuPhysicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 29, 1)
)
hh3cOnuPhysicalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cOnuPhysicalEntry.setStatus("current")
_Hh3cOnuBridgeMac_Type = MacAddress
_Hh3cOnuBridgeMac_Object = MibTableColumn
hh3cOnuBridgeMac = _Hh3cOnuBridgeMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 29, 1, 1),
    _Hh3cOnuBridgeMac_Type()
)
hh3cOnuBridgeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuBridgeMac.setStatus("current")
_Hh3cOnuFirstPonMac_Type = MacAddress
_Hh3cOnuFirstPonMac_Object = MibTableColumn
hh3cOnuFirstPonMac = _Hh3cOnuFirstPonMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 29, 1, 2),
    _Hh3cOnuFirstPonMac_Type()
)
hh3cOnuFirstPonMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuFirstPonMac.setStatus("current")


class _Hh3cOnuFirstPonRegState_Type(Integer32):
    """Custom type hh3cOnuFirstPonRegState based on Integer32"""
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


_Hh3cOnuFirstPonRegState_Type.__name__ = "Integer32"
_Hh3cOnuFirstPonRegState_Object = MibTableColumn
hh3cOnuFirstPonRegState = _Hh3cOnuFirstPonRegState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 29, 1, 3),
    _Hh3cOnuFirstPonRegState_Type()
)
hh3cOnuFirstPonRegState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuFirstPonRegState.setStatus("current")
_Hh3cOnuSecondPonMac_Type = MacAddress
_Hh3cOnuSecondPonMac_Object = MibTableColumn
hh3cOnuSecondPonMac = _Hh3cOnuSecondPonMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 29, 1, 4),
    _Hh3cOnuSecondPonMac_Type()
)
hh3cOnuSecondPonMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuSecondPonMac.setStatus("current")


class _Hh3cOnuSecondPonRegState_Type(Integer32):
    """Custom type hh3cOnuSecondPonRegState based on Integer32"""
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


_Hh3cOnuSecondPonRegState_Type.__name__ = "Integer32"
_Hh3cOnuSecondPonRegState_Object = MibTableColumn
hh3cOnuSecondPonRegState = _Hh3cOnuSecondPonRegState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 29, 1, 5),
    _Hh3cOnuSecondPonRegState_Type()
)
hh3cOnuSecondPonRegState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuSecondPonRegState.setStatus("current")
_Hh3cOnuSmlkTable_Object = MibTable
hh3cOnuSmlkTable = _Hh3cOnuSmlkTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 30)
)
if mibBuilder.loadTexts:
    hh3cOnuSmlkTable.setStatus("current")
_Hh3cOnuSmlkEntry_Object = MibTableRow
hh3cOnuSmlkEntry = _Hh3cOnuSmlkEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 30, 1)
)
hh3cOnuSmlkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-MIB", "hh3cOnuSmlkGroupID"),
)
if mibBuilder.loadTexts:
    hh3cOnuSmlkEntry.setStatus("current")
_Hh3cOnuSmlkGroupID_Type = Integer32
_Hh3cOnuSmlkGroupID_Object = MibTableColumn
hh3cOnuSmlkGroupID = _Hh3cOnuSmlkGroupID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 30, 1, 1),
    _Hh3cOnuSmlkGroupID_Type()
)
hh3cOnuSmlkGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuSmlkGroupID.setStatus("current")


class _Hh3cOnuSmlkFirstPonRole_Type(Integer32):
    """Custom type hh3cOnuSmlkFirstPonRole based on Integer32"""
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


_Hh3cOnuSmlkFirstPonRole_Type.__name__ = "Integer32"
_Hh3cOnuSmlkFirstPonRole_Object = MibTableColumn
hh3cOnuSmlkFirstPonRole = _Hh3cOnuSmlkFirstPonRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 30, 1, 2),
    _Hh3cOnuSmlkFirstPonRole_Type()
)
hh3cOnuSmlkFirstPonRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuSmlkFirstPonRole.setStatus("current")


class _Hh3cOnuSmlkFirstPonStatus_Type(Integer32):
    """Custom type hh3cOnuSmlkFirstPonStatus based on Integer32"""
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


_Hh3cOnuSmlkFirstPonStatus_Type.__name__ = "Integer32"
_Hh3cOnuSmlkFirstPonStatus_Object = MibTableColumn
hh3cOnuSmlkFirstPonStatus = _Hh3cOnuSmlkFirstPonStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 30, 1, 3),
    _Hh3cOnuSmlkFirstPonStatus_Type()
)
hh3cOnuSmlkFirstPonStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuSmlkFirstPonStatus.setStatus("current")


class _Hh3cOnuSmlkSecondPonRole_Type(Integer32):
    """Custom type hh3cOnuSmlkSecondPonRole based on Integer32"""
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


_Hh3cOnuSmlkSecondPonRole_Type.__name__ = "Integer32"
_Hh3cOnuSmlkSecondPonRole_Object = MibTableColumn
hh3cOnuSmlkSecondPonRole = _Hh3cOnuSmlkSecondPonRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 30, 1, 4),
    _Hh3cOnuSmlkSecondPonRole_Type()
)
hh3cOnuSmlkSecondPonRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuSmlkSecondPonRole.setStatus("current")


class _Hh3cOnuSmlkSecondPonStatus_Type(Integer32):
    """Custom type hh3cOnuSmlkSecondPonStatus based on Integer32"""
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


_Hh3cOnuSmlkSecondPonStatus_Type.__name__ = "Integer32"
_Hh3cOnuSmlkSecondPonStatus_Object = MibTableColumn
hh3cOnuSmlkSecondPonStatus = _Hh3cOnuSmlkSecondPonStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 30, 1, 5),
    _Hh3cOnuSmlkSecondPonStatus_Type()
)
hh3cOnuSmlkSecondPonStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuSmlkSecondPonStatus.setStatus("current")
_Hh3cOnuRS485PropertiesTable_Object = MibTable
hh3cOnuRS485PropertiesTable = _Hh3cOnuRS485PropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 31)
)
if mibBuilder.loadTexts:
    hh3cOnuRS485PropertiesTable.setStatus("current")
_Hh3cOnuRS485PropertiesEntry_Object = MibTableRow
hh3cOnuRS485PropertiesEntry = _Hh3cOnuRS485PropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 31, 1)
)
hh3cOnuRS485PropertiesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-MIB", "hh3cOnuRS485SerialIndex"),
)
if mibBuilder.loadTexts:
    hh3cOnuRS485PropertiesEntry.setStatus("current")


class _Hh3cOnuRS485SerialIndex_Type(Integer32):
    """Custom type hh3cOnuRS485SerialIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Hh3cOnuRS485SerialIndex_Type.__name__ = "Integer32"
_Hh3cOnuRS485SerialIndex_Object = MibTableColumn
hh3cOnuRS485SerialIndex = _Hh3cOnuRS485SerialIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 31, 1, 1),
    _Hh3cOnuRS485SerialIndex_Type()
)
hh3cOnuRS485SerialIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cOnuRS485SerialIndex.setStatus("current")


class _Hh3cOnuRS485BaudRate_Type(Integer32):
    """Custom type hh3cOnuRS485BaudRate based on Integer32"""
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


_Hh3cOnuRS485BaudRate_Type.__name__ = "Integer32"
_Hh3cOnuRS485BaudRate_Object = MibTableColumn
hh3cOnuRS485BaudRate = _Hh3cOnuRS485BaudRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 31, 1, 2),
    _Hh3cOnuRS485BaudRate_Type()
)
hh3cOnuRS485BaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuRS485BaudRate.setStatus("current")


class _Hh3cOnuRS485DataBits_Type(Integer32):
    """Custom type hh3cOnuRS485DataBits based on Integer32"""
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


_Hh3cOnuRS485DataBits_Type.__name__ = "Integer32"
_Hh3cOnuRS485DataBits_Object = MibTableColumn
hh3cOnuRS485DataBits = _Hh3cOnuRS485DataBits_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 31, 1, 3),
    _Hh3cOnuRS485DataBits_Type()
)
hh3cOnuRS485DataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuRS485DataBits.setStatus("current")
if mibBuilder.loadTexts:
    hh3cOnuRS485DataBits.setUnits("bit")


class _Hh3cOnuRS485Parity_Type(Integer32):
    """Custom type hh3cOnuRS485Parity based on Integer32"""
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


_Hh3cOnuRS485Parity_Type.__name__ = "Integer32"
_Hh3cOnuRS485Parity_Object = MibTableColumn
hh3cOnuRS485Parity = _Hh3cOnuRS485Parity_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 31, 1, 4),
    _Hh3cOnuRS485Parity_Type()
)
hh3cOnuRS485Parity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuRS485Parity.setStatus("current")


class _Hh3cOnuRS485StopBits_Type(Integer32):
    """Custom type hh3cOnuRS485StopBits based on Integer32"""
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


_Hh3cOnuRS485StopBits_Type.__name__ = "Integer32"
_Hh3cOnuRS485StopBits_Object = MibTableColumn
hh3cOnuRS485StopBits = _Hh3cOnuRS485StopBits_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 31, 1, 5),
    _Hh3cOnuRS485StopBits_Type()
)
hh3cOnuRS485StopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuRS485StopBits.setStatus("current")
if mibBuilder.loadTexts:
    hh3cOnuRS485StopBits.setUnits("bit")


class _Hh3cOnuRS485FlowControl_Type(Integer32):
    """Custom type hh3cOnuRS485FlowControl based on Integer32"""
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


_Hh3cOnuRS485FlowControl_Type.__name__ = "Integer32"
_Hh3cOnuRS485FlowControl_Object = MibTableColumn
hh3cOnuRS485FlowControl = _Hh3cOnuRS485FlowControl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 31, 1, 6),
    _Hh3cOnuRS485FlowControl_Type()
)
hh3cOnuRS485FlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuRS485FlowControl.setStatus("current")
_Hh3cOnuRS485TXOctets_Type = Integer32
_Hh3cOnuRS485TXOctets_Object = MibTableColumn
hh3cOnuRS485TXOctets = _Hh3cOnuRS485TXOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 31, 1, 7),
    _Hh3cOnuRS485TXOctets_Type()
)
hh3cOnuRS485TXOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuRS485TXOctets.setStatus("current")
_Hh3cOnuRS485RXOctets_Type = Integer32
_Hh3cOnuRS485RXOctets_Object = MibTableColumn
hh3cOnuRS485RXOctets = _Hh3cOnuRS485RXOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 31, 1, 8),
    _Hh3cOnuRS485RXOctets_Type()
)
hh3cOnuRS485RXOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuRS485RXOctets.setStatus("current")
_Hh3cOnuRS485TXErrOctets_Type = Integer32
_Hh3cOnuRS485TXErrOctets_Object = MibTableColumn
hh3cOnuRS485TXErrOctets = _Hh3cOnuRS485TXErrOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 31, 1, 9),
    _Hh3cOnuRS485TXErrOctets_Type()
)
hh3cOnuRS485TXErrOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuRS485TXErrOctets.setStatus("current")
_Hh3cOnuRS485RXErrOctets_Type = Integer32
_Hh3cOnuRS485RXErrOctets_Object = MibTableColumn
hh3cOnuRS485RXErrOctets = _Hh3cOnuRS485RXErrOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 31, 1, 10),
    _Hh3cOnuRS485RXErrOctets_Type()
)
hh3cOnuRS485RXErrOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuRS485RXErrOctets.setStatus("current")


class _Hh3cOnuRS485ResetStatistics_Type(Integer32):
    """Custom type hh3cOnuRS485ResetStatistics based on Integer32"""
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


_Hh3cOnuRS485ResetStatistics_Type.__name__ = "Integer32"
_Hh3cOnuRS485ResetStatistics_Object = MibTableColumn
hh3cOnuRS485ResetStatistics = _Hh3cOnuRS485ResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 31, 1, 11),
    _Hh3cOnuRS485ResetStatistics_Type()
)
hh3cOnuRS485ResetStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cOnuRS485ResetStatistics.setStatus("current")
_Hh3cOnuRS485SessionSummaryTable_Object = MibTable
hh3cOnuRS485SessionSummaryTable = _Hh3cOnuRS485SessionSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 32)
)
if mibBuilder.loadTexts:
    hh3cOnuRS485SessionSummaryTable.setStatus("current")
_Hh3cOnuRS485SessionSummaryEntry_Object = MibTableRow
hh3cOnuRS485SessionSummaryEntry = _Hh3cOnuRS485SessionSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 32, 1)
)
hh3cOnuRS485SessionSummaryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-MIB", "hh3cOnuRS485SerialIndex"),
)
if mibBuilder.loadTexts:
    hh3cOnuRS485SessionSummaryEntry.setStatus("current")


class _Hh3cOnuRS485SessionMaxNum_Type(Integer32):
    """Custom type hh3cOnuRS485SessionMaxNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Hh3cOnuRS485SessionMaxNum_Type.__name__ = "Integer32"
_Hh3cOnuRS485SessionMaxNum_Object = MibTableColumn
hh3cOnuRS485SessionMaxNum = _Hh3cOnuRS485SessionMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 32, 1, 1),
    _Hh3cOnuRS485SessionMaxNum_Type()
)
hh3cOnuRS485SessionMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuRS485SessionMaxNum.setStatus("current")


class _Hh3cOnuRS485SessionNextIndex_Type(Integer32):
    """Custom type hh3cOnuRS485SessionNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Hh3cOnuRS485SessionNextIndex_Type.__name__ = "Integer32"
_Hh3cOnuRS485SessionNextIndex_Object = MibTableColumn
hh3cOnuRS485SessionNextIndex = _Hh3cOnuRS485SessionNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 32, 1, 2),
    _Hh3cOnuRS485SessionNextIndex_Type()
)
hh3cOnuRS485SessionNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuRS485SessionNextIndex.setStatus("current")
_Hh3cOnuRS485SessionTable_Object = MibTable
hh3cOnuRS485SessionTable = _Hh3cOnuRS485SessionTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 33)
)
if mibBuilder.loadTexts:
    hh3cOnuRS485SessionTable.setStatus("current")
_Hh3cOnuRS485SessionEntry_Object = MibTableRow
hh3cOnuRS485SessionEntry = _Hh3cOnuRS485SessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 33, 1)
)
hh3cOnuRS485SessionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-MIB", "hh3cOnuRS485SerialIndex"),
    (0, "HH3C-EPON-MIB", "hh3cOnuRS485SessionIndex"),
)
if mibBuilder.loadTexts:
    hh3cOnuRS485SessionEntry.setStatus("current")


class _Hh3cOnuRS485SessionIndex_Type(Integer32):
    """Custom type hh3cOnuRS485SessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Hh3cOnuRS485SessionIndex_Type.__name__ = "Integer32"
_Hh3cOnuRS485SessionIndex_Object = MibTableColumn
hh3cOnuRS485SessionIndex = _Hh3cOnuRS485SessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 33, 1, 1),
    _Hh3cOnuRS485SessionIndex_Type()
)
hh3cOnuRS485SessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cOnuRS485SessionIndex.setStatus("current")


class _Hh3cOnuRS485SessionType_Type(Integer32):
    """Custom type hh3cOnuRS485SessionType based on Integer32"""
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


_Hh3cOnuRS485SessionType_Type.__name__ = "Integer32"
_Hh3cOnuRS485SessionType_Object = MibTableColumn
hh3cOnuRS485SessionType = _Hh3cOnuRS485SessionType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 33, 1, 2),
    _Hh3cOnuRS485SessionType_Type()
)
hh3cOnuRS485SessionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cOnuRS485SessionType.setStatus("current")
_Hh3cOnuRS485SessionAddType_Type = InetAddressType
_Hh3cOnuRS485SessionAddType_Object = MibTableColumn
hh3cOnuRS485SessionAddType = _Hh3cOnuRS485SessionAddType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 33, 1, 3),
    _Hh3cOnuRS485SessionAddType_Type()
)
hh3cOnuRS485SessionAddType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cOnuRS485SessionAddType.setStatus("current")
_Hh3cOnuRS485SessionRemoteIP_Type = InetAddress
_Hh3cOnuRS485SessionRemoteIP_Object = MibTableColumn
hh3cOnuRS485SessionRemoteIP = _Hh3cOnuRS485SessionRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 33, 1, 4),
    _Hh3cOnuRS485SessionRemoteIP_Type()
)
hh3cOnuRS485SessionRemoteIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cOnuRS485SessionRemoteIP.setStatus("current")


class _Hh3cOnuRS485SessionRemotePort_Type(Integer32):
    """Custom type hh3cOnuRS485SessionRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_Hh3cOnuRS485SessionRemotePort_Type.__name__ = "Integer32"
_Hh3cOnuRS485SessionRemotePort_Object = MibTableColumn
hh3cOnuRS485SessionRemotePort = _Hh3cOnuRS485SessionRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 33, 1, 5),
    _Hh3cOnuRS485SessionRemotePort_Type()
)
hh3cOnuRS485SessionRemotePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cOnuRS485SessionRemotePort.setStatus("current")


class _Hh3cOnuRS485SessionLocalPort_Type(Integer32):
    """Custom type hh3cOnuRS485SessionLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_Hh3cOnuRS485SessionLocalPort_Type.__name__ = "Integer32"
_Hh3cOnuRS485SessionLocalPort_Object = MibTableColumn
hh3cOnuRS485SessionLocalPort = _Hh3cOnuRS485SessionLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 33, 1, 6),
    _Hh3cOnuRS485SessionLocalPort_Type()
)
hh3cOnuRS485SessionLocalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cOnuRS485SessionLocalPort.setStatus("current")
_Hh3cOnuRS485SessionRowStatus_Type = RowStatus
_Hh3cOnuRS485SessionRowStatus_Object = MibTableColumn
hh3cOnuRS485SessionRowStatus = _Hh3cOnuRS485SessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 33, 1, 7),
    _Hh3cOnuRS485SessionRowStatus_Type()
)
hh3cOnuRS485SessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cOnuRS485SessionRowStatus.setStatus("current")
_Hh3cOnuRS485SessionErrInfoTable_Object = MibTable
hh3cOnuRS485SessionErrInfoTable = _Hh3cOnuRS485SessionErrInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 34)
)
if mibBuilder.loadTexts:
    hh3cOnuRS485SessionErrInfoTable.setStatus("current")
_Hh3cOnuRS485SessionErrInfoEntry_Object = MibTableRow
hh3cOnuRS485SessionErrInfoEntry = _Hh3cOnuRS485SessionErrInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 34, 1)
)
hh3cOnuRS485SessionErrInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-MIB", "hh3cOnuRS485SerialIndex"),
    (0, "HH3C-EPON-MIB", "hh3cOnuRS485SessionIndex"),
)
if mibBuilder.loadTexts:
    hh3cOnuRS485SessionErrInfoEntry.setStatus("current")
_Hh3cOnuRS485SessionErrInfo_Type = DisplayString
_Hh3cOnuRS485SessionErrInfo_Object = MibTableColumn
hh3cOnuRS485SessionErrInfo = _Hh3cOnuRS485SessionErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 5, 34, 1, 1),
    _Hh3cOnuRS485SessionErrInfo_Type()
)
hh3cOnuRS485SessionErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOnuRS485SessionErrInfo.setStatus("current")
_Hh3cEponBatchOperationMan_ObjectIdentity = ObjectIdentity
hh3cEponBatchOperationMan = _Hh3cEponBatchOperationMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 6)
)
_Hh3cEponBatchOperationBySlotTable_Object = MibTable
hh3cEponBatchOperationBySlotTable = _Hh3cEponBatchOperationBySlotTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hh3cEponBatchOperationBySlotTable.setStatus("current")
_Hh3cEponBatchOperationBySlotEntry_Object = MibTableRow
hh3cEponBatchOperationBySlotEntry = _Hh3cEponBatchOperationBySlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 6, 1, 1)
)
hh3cEponBatchOperationBySlotEntry.setIndexNames(
    (0, "HH3C-EPON-MIB", "hh3cEponBatchOperationBySlotIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponBatchOperationBySlotEntry.setStatus("current")
_Hh3cEponBatchOperationBySlotIndex_Type = Integer32
_Hh3cEponBatchOperationBySlotIndex_Object = MibTableColumn
hh3cEponBatchOperationBySlotIndex = _Hh3cEponBatchOperationBySlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 6, 1, 1, 1),
    _Hh3cEponBatchOperationBySlotIndex_Type()
)
hh3cEponBatchOperationBySlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEponBatchOperationBySlotIndex.setStatus("current")


class _Hh3cEponBatchOperationBySlotType_Type(Integer32):
    """Custom type hh3cEponBatchOperationBySlotType based on Integer32"""
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


_Hh3cEponBatchOperationBySlotType_Type.__name__ = "Integer32"
_Hh3cEponBatchOperationBySlotType_Object = MibTableColumn
hh3cEponBatchOperationBySlotType = _Hh3cEponBatchOperationBySlotType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 6, 1, 1, 2),
    _Hh3cEponBatchOperationBySlotType_Type()
)
hh3cEponBatchOperationBySlotType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponBatchOperationBySlotType.setStatus("current")


class _Hh3cEponBatchOperationBySlot_Type(Integer32):
    """Custom type hh3cEponBatchOperationBySlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("batOpBySlot", 1)
    )


_Hh3cEponBatchOperationBySlot_Type.__name__ = "Integer32"
_Hh3cEponBatchOperationBySlot_Object = MibTableColumn
hh3cEponBatchOperationBySlot = _Hh3cEponBatchOperationBySlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 6, 1, 1, 3),
    _Hh3cEponBatchOperationBySlot_Type()
)
hh3cEponBatchOperationBySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponBatchOperationBySlot.setStatus("current")
_Hh3cEponBatchOperationBySlotResult_Type = Integer32
_Hh3cEponBatchOperationBySlotResult_Object = MibTableColumn
hh3cEponBatchOperationBySlotResult = _Hh3cEponBatchOperationBySlotResult_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 6, 1, 1, 4),
    _Hh3cEponBatchOperationBySlotResult_Type()
)
hh3cEponBatchOperationBySlotResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponBatchOperationBySlotResult.setStatus("current")
_Hh3cEponBatchOperationByOLTTable_Object = MibTable
hh3cEponBatchOperationByOLTTable = _Hh3cEponBatchOperationByOLTTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 6, 2)
)
if mibBuilder.loadTexts:
    hh3cEponBatchOperationByOLTTable.setStatus("current")
_Hh3cEponBatchOperationByOLTEntry_Object = MibTableRow
hh3cEponBatchOperationByOLTEntry = _Hh3cEponBatchOperationByOLTEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 6, 2, 1)
)
hh3cEponBatchOperationByOLTEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponBatchOperationByOLTEntry.setStatus("current")


class _Hh3cEponBatchOperationByOLTType_Type(Integer32):
    """Custom type hh3cEponBatchOperationByOLTType based on Integer32"""
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


_Hh3cEponBatchOperationByOLTType_Type.__name__ = "Integer32"
_Hh3cEponBatchOperationByOLTType_Object = MibTableColumn
hh3cEponBatchOperationByOLTType = _Hh3cEponBatchOperationByOLTType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 6, 2, 1, 1),
    _Hh3cEponBatchOperationByOLTType_Type()
)
hh3cEponBatchOperationByOLTType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponBatchOperationByOLTType.setStatus("current")


class _Hh3cEponBatchOperationByOLT_Type(Integer32):
    """Custom type hh3cEponBatchOperationByOLT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("batOpByOlt", 1)
    )


_Hh3cEponBatchOperationByOLT_Type.__name__ = "Integer32"
_Hh3cEponBatchOperationByOLT_Object = MibTableColumn
hh3cEponBatchOperationByOLT = _Hh3cEponBatchOperationByOLT_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 6, 2, 1, 2),
    _Hh3cEponBatchOperationByOLT_Type()
)
hh3cEponBatchOperationByOLT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponBatchOperationByOLT.setStatus("current")
_Hh3cEponBatchOperationByOLTResult_Type = Integer32
_Hh3cEponBatchOperationByOLTResult_Object = MibTableColumn
hh3cEponBatchOperationByOLTResult = _Hh3cEponBatchOperationByOLTResult_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 6, 2, 1, 3),
    _Hh3cEponBatchOperationByOLTResult_Type()
)
hh3cEponBatchOperationByOLTResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponBatchOperationByOLTResult.setStatus("current")
_Hh3cOnuFirmwareUpdateByTypeTable_Object = MibTable
hh3cOnuFirmwareUpdateByTypeTable = _Hh3cOnuFirmwareUpdateByTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 6, 3)
)
if mibBuilder.loadTexts:
    hh3cOnuFirmwareUpdateByTypeTable.setStatus("current")
_Hh3cOnuFirmwareUpdateByTypeEntry_Object = MibTableRow
hh3cOnuFirmwareUpdateByTypeEntry = _Hh3cOnuFirmwareUpdateByTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 6, 3, 1)
)
hh3cOnuFirmwareUpdateByTypeEntry.setIndexNames(
    (0, "HH3C-EPON-MIB", "hh3cOnuUpdateByOnuTypeIndex"),
)
if mibBuilder.loadTexts:
    hh3cOnuFirmwareUpdateByTypeEntry.setStatus("current")
_Hh3cOnuUpdateByOnuTypeIndex_Type = Integer32
_Hh3cOnuUpdateByOnuTypeIndex_Object = MibTableColumn
hh3cOnuUpdateByOnuTypeIndex = _Hh3cOnuUpdateByOnuTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 6, 3, 1, 1),
    _Hh3cOnuUpdateByOnuTypeIndex_Type()
)
hh3cOnuUpdateByOnuTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cOnuUpdateByOnuTypeIndex.setStatus("current")


class _Hh3cOnuUpdateByTypeOnuType_Type(OctetString):
    """Custom type hh3cOnuUpdateByTypeOnuType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Hh3cOnuUpdateByTypeOnuType_Type.__name__ = "OctetString"
_Hh3cOnuUpdateByTypeOnuType_Object = MibTableColumn
hh3cOnuUpdateByTypeOnuType = _Hh3cOnuUpdateByTypeOnuType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 6, 3, 1, 2),
    _Hh3cOnuUpdateByTypeOnuType_Type()
)
hh3cOnuUpdateByTypeOnuType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cOnuUpdateByTypeOnuType.setStatus("current")


class _Hh3cOnuUpdateByTypeFileName_Type(OctetString):
    """Custom type hh3cOnuUpdateByTypeFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cOnuUpdateByTypeFileName_Type.__name__ = "OctetString"
_Hh3cOnuUpdateByTypeFileName_Object = MibTableColumn
hh3cOnuUpdateByTypeFileName = _Hh3cOnuUpdateByTypeFileName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 6, 3, 1, 3),
    _Hh3cOnuUpdateByTypeFileName_Type()
)
hh3cOnuUpdateByTypeFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cOnuUpdateByTypeFileName.setStatus("current")
_Hh3cOnuUpdateByTypeRowStatus_Type = RowStatus
_Hh3cOnuUpdateByTypeRowStatus_Object = MibTableColumn
hh3cOnuUpdateByTypeRowStatus = _Hh3cOnuUpdateByTypeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 6, 3, 1, 4),
    _Hh3cOnuUpdateByTypeRowStatus_Type()
)
hh3cOnuUpdateByTypeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cOnuUpdateByTypeRowStatus.setStatus("current")
_Hh3cEponErrorInfo_ObjectIdentity = ObjectIdentity
hh3cEponErrorInfo = _Hh3cEponErrorInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 7)
)
_Hh3cEponSoftwareErrorCode_Type = Integer32
_Hh3cEponSoftwareErrorCode_Object = MibScalar
hh3cEponSoftwareErrorCode = _Hh3cEponSoftwareErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 7, 1),
    _Hh3cEponSoftwareErrorCode_Type()
)
hh3cEponSoftwareErrorCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cEponSoftwareErrorCode.setStatus("current")
_Hh3cOamVendorSpecificAlarmCode_Type = Integer32
_Hh3cOamVendorSpecificAlarmCode_Object = MibScalar
hh3cOamVendorSpecificAlarmCode = _Hh3cOamVendorSpecificAlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 7, 2),
    _Hh3cOamVendorSpecificAlarmCode_Type()
)
hh3cOamVendorSpecificAlarmCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cOamVendorSpecificAlarmCode.setStatus("current")
_Hh3cEponOnuRegErrorMacAddr_Type = OctetString
_Hh3cEponOnuRegErrorMacAddr_Object = MibScalar
hh3cEponOnuRegErrorMacAddr = _Hh3cEponOnuRegErrorMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 7, 3),
    _Hh3cEponOnuRegErrorMacAddr_Type()
)
hh3cEponOnuRegErrorMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cEponOnuRegErrorMacAddr.setStatus("current")
_Hh3cOamEventLogType_Type = Unsigned32
_Hh3cOamEventLogType_Object = MibScalar
hh3cOamEventLogType = _Hh3cOamEventLogType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 7, 4),
    _Hh3cOamEventLogType_Type()
)
hh3cOamEventLogType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cOamEventLogType.setStatus("current")


class _Hh3cOamEventLogLocation_Type(Integer32):
    """Custom type hh3cOamEventLogLocation based on Integer32"""
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


_Hh3cOamEventLogLocation_Type.__name__ = "Integer32"
_Hh3cOamEventLogLocation_Object = MibScalar
hh3cOamEventLogLocation = _Hh3cOamEventLogLocation_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 7, 5),
    _Hh3cOamEventLogLocation_Type()
)
hh3cOamEventLogLocation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cOamEventLogLocation.setStatus("current")
_Hh3cEponLoopbackPortIndex_Type = Integer32
_Hh3cEponLoopbackPortIndex_Object = MibScalar
hh3cEponLoopbackPortIndex = _Hh3cEponLoopbackPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 7, 6),
    _Hh3cEponLoopbackPortIndex_Type()
)
hh3cEponLoopbackPortIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cEponLoopbackPortIndex.setStatus("current")


class _Hh3cEponLoopbackPortDescr_Type(OctetString):
    """Custom type hh3cEponLoopbackPortDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cEponLoopbackPortDescr_Type.__name__ = "OctetString"
_Hh3cEponLoopbackPortDescr_Object = MibScalar
hh3cEponLoopbackPortDescr = _Hh3cEponLoopbackPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 7, 7),
    _Hh3cEponLoopbackPortDescr_Type()
)
hh3cEponLoopbackPortDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cEponLoopbackPortDescr.setStatus("current")
_Hh3cOltPortAlarmLlidMisFrames_Type = Unsigned32
_Hh3cOltPortAlarmLlidMisFrames_Object = MibScalar
hh3cOltPortAlarmLlidMisFrames = _Hh3cOltPortAlarmLlidMisFrames_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 7, 8),
    _Hh3cOltPortAlarmLlidMisFrames_Type()
)
hh3cOltPortAlarmLlidMisFrames.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cOltPortAlarmLlidMisFrames.setStatus("current")
_Hh3cOltPortAlarmBer_Type = Unsigned32
_Hh3cOltPortAlarmBer_Object = MibScalar
hh3cOltPortAlarmBer = _Hh3cOltPortAlarmBer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 7, 9),
    _Hh3cOltPortAlarmBer_Type()
)
hh3cOltPortAlarmBer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cOltPortAlarmBer.setStatus("current")
_Hh3cOltPortAlarmFer_Type = Unsigned32
_Hh3cOltPortAlarmFer_Object = MibScalar
hh3cOltPortAlarmFer = _Hh3cOltPortAlarmFer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 7, 10),
    _Hh3cOltPortAlarmFer_Type()
)
hh3cOltPortAlarmFer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cOltPortAlarmFer.setStatus("current")
_Hh3cEponOnuRegSilentMac_Type = OctetString
_Hh3cEponOnuRegSilentMac_Object = MibScalar
hh3cEponOnuRegSilentMac = _Hh3cEponOnuRegSilentMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 7, 11),
    _Hh3cEponOnuRegSilentMac_Type()
)
hh3cEponOnuRegSilentMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cEponOnuRegSilentMac.setStatus("current")


class _Hh3cEponOperationResult_Type(OctetString):
    """Custom type hh3cEponOperationResult based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cEponOperationResult_Type.__name__ = "OctetString"
_Hh3cEponOperationResult_Object = MibScalar
hh3cEponOperationResult = _Hh3cEponOperationResult_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 7, 12),
    _Hh3cEponOperationResult_Type()
)
hh3cEponOperationResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cEponOperationResult.setStatus("current")


class _Hh3cEponOnuLaserState_Type(Integer32):
    """Custom type hh3cEponOnuLaserState based on Integer32"""
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


_Hh3cEponOnuLaserState_Type.__name__ = "Integer32"
_Hh3cEponOnuLaserState_Object = MibScalar
hh3cEponOnuLaserState = _Hh3cEponOnuLaserState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 7, 13),
    _Hh3cEponOnuLaserState_Type()
)
hh3cEponOnuLaserState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cEponOnuLaserState.setStatus("current")
_Hh3cEponTrap_ObjectIdentity = ObjectIdentity
hh3cEponTrap = _Hh3cEponTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8)
)
_Hh3cEponTrapPrefix_ObjectIdentity = ObjectIdentity
hh3cEponTrapPrefix = _Hh3cEponTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0)
)
_Hh3cEponStat_ObjectIdentity = ObjectIdentity
hh3cEponStat = _Hh3cEponStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 9)
)
_Hh3cEponStatTable_Object = MibTable
hh3cEponStatTable = _Hh3cEponStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 9, 1)
)
if mibBuilder.loadTexts:
    hh3cEponStatTable.setStatus("current")
_Hh3cEponStatEntry_Object = MibTableRow
hh3cEponStatEntry = _Hh3cEponStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 9, 1, 1)
)
hh3cEponStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponStatEntry.setStatus("current")
_Hh3cEponStatFER_Type = Counter64
_Hh3cEponStatFER_Object = MibTableColumn
hh3cEponStatFER = _Hh3cEponStatFER_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 9, 1, 1, 1),
    _Hh3cEponStatFER_Type()
)
hh3cEponStatFER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponStatFER.setStatus("current")
_Hh3cEponStatBER_Type = Counter64
_Hh3cEponStatBER_Object = MibTableColumn
hh3cEponStatBER = _Hh3cEponStatBER_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 9, 1, 1, 2),
    _Hh3cEponStatBER_Type()
)
hh3cEponStatBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponStatBER.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cEponPortAlarmBerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 1)
)
hh3cEponPortAlarmBerTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EPON-MIB", "hh3cOltPortAlarmBerDirect"),
        ("HH3C-EPON-MIB", "hh3cOltPortAlarmBer"),
        ("HH3C-EPON-MIB", "hh3cOltPortAlarmBerThreshold"))
)
if mibBuilder.loadTexts:
    hh3cEponPortAlarmBerTrap.setStatus(
        "current"
    )

hh3cEponPortAlarmFerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 2)
)
hh3cEponPortAlarmFerTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EPON-MIB", "hh3cOltPortAlarmFerDirect"),
        ("HH3C-EPON-MIB", "hh3cOltPortAlarmFer"),
        ("HH3C-EPON-MIB", "hh3cOltPortAlarmFerThreshold"))
)
if mibBuilder.loadTexts:
    hh3cEponPortAlarmFerTrap.setStatus(
        "current"
    )

hh3cEponErrorLLIDFrameTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 3)
)
hh3cEponErrorLLIDFrameTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EPON-MIB", "hh3cOltPortAlarmLlidMisFrames"),
        ("HH3C-EPON-MIB", "hh3cOltPortAlarmLlidMismatchThreshold"))
)
if mibBuilder.loadTexts:
    hh3cEponErrorLLIDFrameTrap.setStatus(
        "current"
    )

hh3cEponLoopBackEnableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 4)
)
hh3cEponLoopBackEnableTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EPON-MIB", "hh3cEponLoopbackPortIndex"),
        ("HH3C-EPON-MIB", "hh3cEponLoopbackPortDescr"))
)
if mibBuilder.loadTexts:
    hh3cEponLoopBackEnableTrap.setStatus(
        "current"
    )

hh3cEponOnuRegistrationErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 5)
)
hh3cEponOnuRegistrationErrTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EPON-MIB", "hh3cEponOnuRegErrorMacAddr"))
)
if mibBuilder.loadTexts:
    hh3cEponOnuRegistrationErrTrap.setStatus(
        "current"
    )

hh3cEponOamDisconnectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 6)
)
hh3cEponOamDisconnectionTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cEponOamDisconnectionTrap.setStatus(
        "current"
    )

hh3cEponEncryptionKeyErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 7)
)
hh3cEponEncryptionKeyErrTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cEponEncryptionKeyErrTrap.setStatus(
        "current"
    )

hh3cEponRemoteStableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 8)
)
hh3cEponRemoteStableTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cEponRemoteStableTrap.setStatus(
        "current"
    )

hh3cEponLocalStableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 9)
)
hh3cEponLocalStableTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cEponLocalStableTrap.setStatus(
        "current"
    )

hh3cEponOamVendorSpecificTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 10)
)
hh3cEponOamVendorSpecificTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EPON-MIB", "hh3cOamVendorSpecificAlarmCode"))
)
if mibBuilder.loadTexts:
    hh3cEponOamVendorSpecificTrap.setStatus(
        "current"
    )

hh3cEponSoftwareErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 11)
)
hh3cEponSoftwareErrTrap.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-EPON-MIB", "hh3cEponSoftwareErrorCode"))
)
if mibBuilder.loadTexts:
    hh3cEponSoftwareErrTrap.setStatus(
        "current"
    )

hh3cEponPortAlarmBerRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 12)
)
hh3cEponPortAlarmBerRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EPON-MIB", "hh3cOltPortAlarmBerDirect"))
)
if mibBuilder.loadTexts:
    hh3cEponPortAlarmBerRecoverTrap.setStatus(
        "current"
    )

hh3cEponPortAlarmFerRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 13)
)
hh3cEponPortAlarmFerRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EPON-MIB", "hh3cOltPortAlarmFerDirect"))
)
if mibBuilder.loadTexts:
    hh3cEponPortAlarmFerRecoverTrap.setStatus(
        "current"
    )

hh3cEponErrorLLIDFrameRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 14)
)
hh3cEponErrorLLIDFrameRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cEponErrorLLIDFrameRecoverTrap.setStatus(
        "current"
    )

hh3cEponLoopBackEnableRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 15)
)
hh3cEponLoopBackEnableRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cEponLoopBackEnableRecoverTrap.setStatus(
        "current"
    )

hh3cEponOnuRegistrationErrRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 16)
)
hh3cEponOnuRegistrationErrRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EPON-MIB", "hh3cEponOnuRegErrorMacAddr"))
)
if mibBuilder.loadTexts:
    hh3cEponOnuRegistrationErrRecoverTrap.setStatus(
        "current"
    )

hh3cEponOamDisconnectionRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 17)
)
hh3cEponOamDisconnectionRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cEponOamDisconnectionRecoverTrap.setStatus(
        "current"
    )

hh3cEponEncryptionKeyErrRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 18)
)
hh3cEponEncryptionKeyErrRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cEponEncryptionKeyErrRecoverTrap.setStatus(
        "current"
    )

hh3cEponRemoteStableRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 19)
)
hh3cEponRemoteStableRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cEponRemoteStableRecoverTrap.setStatus(
        "current"
    )

hh3cEponLocalStableRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 20)
)
hh3cEponLocalStableRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cEponLocalStableRecoverTrap.setStatus(
        "current"
    )

hh3cEponOamVendorSpecificRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 21)
)
hh3cEponOamVendorSpecificRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EPON-MIB", "hh3cOamVendorSpecificAlarmCode"))
)
if mibBuilder.loadTexts:
    hh3cEponOamVendorSpecificRecoverTrap.setStatus(
        "current"
    )

hh3cEponSoftwareErrRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 22)
)
hh3cEponSoftwareErrRecoverTrap.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-EPON-MIB", "hh3cEponSoftwareErrorCode"))
)
if mibBuilder.loadTexts:
    hh3cEponSoftwareErrRecoverTrap.setStatus(
        "current"
    )

hh3cDot3OamThresholdRecoverEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 23)
)
hh3cDot3OamThresholdRecoverEvent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HH3C-EPON-MIB", "hh3cOamEventLogType"),
        ("HH3C-EPON-MIB", "hh3cOamEventLogLocation"))
)
if mibBuilder.loadTexts:
    hh3cDot3OamThresholdRecoverEvent.setStatus(
        "current"
    )

hh3cDot3OamNonThresholdRecoverEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 24)
)
hh3cDot3OamNonThresholdRecoverEvent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HH3C-EPON-MIB", "hh3cOamEventLogType"),
        ("HH3C-EPON-MIB", "hh3cOamEventLogLocation"))
)
if mibBuilder.loadTexts:
    hh3cDot3OamNonThresholdRecoverEvent.setStatus(
        "current"
    )

hh3cEponOnuRegExcessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 25)
)
hh3cEponOnuRegExcessTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cEponOnuRegExcessTrap.setStatus(
        "current"
    )

hh3cEponOnuRegExcessRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 26)
)
hh3cEponOnuRegExcessRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cEponOnuRegExcessRecoverTrap.setStatus(
        "current"
    )

hh3cEponOnuPowerOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 27)
)
hh3cEponOnuPowerOffTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cEponOnuPowerOffTrap.setStatus(
        "current"
    )

hh3cEponOltSwitchoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 28)
)
hh3cEponOltSwitchoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cEponOltSwitchoverTrap.setStatus(
        "current"
    )

hh3cEponOltDFETrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 29)
)
hh3cEponOltDFETrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cEponOltDFETrap.setStatus(
        "current"
    )

hh3cEponOltDFERecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 30)
)
hh3cEponOltDFERecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cEponOltDFERecoverTrap.setStatus(
        "current"
    )

hh3cEponOnuSilenceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 31)
)
hh3cEponOnuSilenceTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EPON-MIB", "hh3cEponOnuRegSilentMac"))
)
if mibBuilder.loadTexts:
    hh3cEponOnuSilenceTrap.setStatus(
        "current"
    )

hh3cEponOnuSilenceRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 32)
)
hh3cEponOnuSilenceRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EPON-MIB", "hh3cEponOnuRegSilentMac"))
)
if mibBuilder.loadTexts:
    hh3cEponOnuSilenceRecoverTrap.setStatus(
        "current"
    )

hh3cEponOnuUpdateResultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 33)
)
hh3cEponOnuUpdateResultTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EPON-MIB", "hh3cOnuBindMacAddress"),
        ("HH3C-EPON-MIB", "hh3cOnuUpdateResult"),
        ("HH3C-EPON-MIB", "hh3cOnuRegType"),
        ("HH3C-EPON-MIB", "hh3cOnuUpdateFileName"))
)
if mibBuilder.loadTexts:
    hh3cEponOnuUpdateResultTrap.setStatus(
        "current"
    )

hh3cEponOnuAutoBindTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 34)
)
hh3cEponOnuAutoBindTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EPON-MIB", "hh3cOnuBindMacAddress"),
        ("HH3C-EPON-MIB", "hh3cEponOperationResult"))
)
if mibBuilder.loadTexts:
    hh3cEponOnuAutoBindTrap.setStatus(
        "current"
    )

hh3cEponOnuPortStpStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 35)
)
hh3cEponOnuPortStpStateTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EPON-MIB", "hh3cEponStpPortIndex"),
        ("HH3C-EPON-MIB", "hh3cEponStpPortDescr"),
        ("HH3C-EPON-MIB", "hh3cEponStpPortState"))
)
if mibBuilder.loadTexts:
    hh3cEponOnuPortStpStateTrap.setStatus(
        "current"
    )

hh3cEponOnuLaserFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 36)
)
hh3cEponOnuLaserFailedTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EPON-MIB", "hh3cEponOnuLaserState"))
)
if mibBuilder.loadTexts:
    hh3cEponOnuLaserFailedTrap.setStatus(
        "current"
    )

hh3cOnuSmlkSwitchoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 1, 8, 0, 37)
)
hh3cOnuSmlkSwitchoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EPON-MIB", "hh3cOnuSmlkGroupID"),
        ("HH3C-EPON-MIB", "hh3cOnuSmlkFirstPonStatus"),
        ("HH3C-EPON-MIB", "hh3cOnuSmlkSecondPonStatus"))
)
if mibBuilder.loadTexts:
    hh3cOnuSmlkSwitchoverTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-EPON-MIB",
    **{"hh3cEponMibObjects": hh3cEponMibObjects,
       "hh3cEponSysMan": hh3cEponSysMan,
       "hh3cEponAutoAuthorize": hh3cEponAutoAuthorize,
       "hh3cEponMonitorCycle": hh3cEponMonitorCycle,
       "hh3cEponMsgTimeOut": hh3cEponMsgTimeOut,
       "hh3cEponMsgLoseNum": hh3cEponMsgLoseNum,
       "hh3cEponSysHasEPONBoard": hh3cEponSysHasEPONBoard,
       "hh3cEponMonitorCycleEnable": hh3cEponMonitorCycleEnable,
       "hh3cEponOltSoftwareErrAlmEnable": hh3cEponOltSoftwareErrAlmEnable,
       "hh3cEponPortLoopBackAlmEnable": hh3cEponPortLoopBackAlmEnable,
       "hh3cEponMonitorCycleMinVal": hh3cEponMonitorCycleMinVal,
       "hh3cEponMonitorCycleMaxVal": hh3cEponMonitorCycleMaxVal,
       "hh3cEponMsgTimeOutMinVal": hh3cEponMsgTimeOutMinVal,
       "hh3cEponMsgTimeOutMaxVal": hh3cEponMsgTimeOutMaxVal,
       "hh3cEponMsgLoseNumMinVal": hh3cEponMsgLoseNumMinVal,
       "hh3cEponMsgLoseNumMaxVal": hh3cEponMsgLoseNumMaxVal,
       "hh3cEponSysScalarGroup": hh3cEponSysScalarGroup,
       "hh3cEponSysManTable": hh3cEponSysManTable,
       "hh3cEponSysManEntry": hh3cEponSysManEntry,
       "hh3cEponSlotIndex": hh3cEponSlotIndex,
       "hh3cEponModeSwitch": hh3cEponModeSwitch,
       "hh3cEponAutomaticMode": hh3cEponAutomaticMode,
       "hh3cEponOamDiscoveryTimeout": hh3cEponOamDiscoveryTimeout,
       "hh3cEponEncryptionNoReplyTimeOut": hh3cEponEncryptionNoReplyTimeOut,
       "hh3cEponEncryptionUpdateTime": hh3cEponEncryptionUpdateTime,
       "hh3cEponAutoBindStatus": hh3cEponAutoBindStatus,
       "hh3cEponAutoUpdateTable": hh3cEponAutoUpdateTable,
       "hh3cEponAutoUpdateEntry": hh3cEponAutoUpdateEntry,
       "hh3cEponAutoUpdateFileName": hh3cEponAutoUpdateFileName,
       "hh3cEponAutoUpdateSchedStatus": hh3cEponAutoUpdateSchedStatus,
       "hh3cEponAutoUpdateSchedTime": hh3cEponAutoUpdateSchedTime,
       "hh3cEponAutoUpdateSchedType": hh3cEponAutoUpdateSchedType,
       "hh3cEponAutoUpdateRealTimeStatus": hh3cEponAutoUpdateRealTimeStatus,
       "hh3cEponOuiIndexNextTable": hh3cEponOuiIndexNextTable,
       "hh3cEponOuiIndexNextEntry": hh3cEponOuiIndexNextEntry,
       "hh3cEponOuiIndexNext": hh3cEponOuiIndexNext,
       "hh3cEponOuiTable": hh3cEponOuiTable,
       "hh3cEponOuiEntry": hh3cEponOuiEntry,
       "hh3cEponOuiIndex": hh3cEponOuiIndex,
       "hh3cEponOuiValue": hh3cEponOuiValue,
       "hh3cEponOamVersion": hh3cEponOamVersion,
       "hh3cEponOuiRowStatus": hh3cEponOuiRowStatus,
       "hh3cEponMulticastControlTable": hh3cEponMulticastControlTable,
       "hh3cEponMulticastControlEntry": hh3cEponMulticastControlEntry,
       "hh3cEponMulticastVlanId": hh3cEponMulticastVlanId,
       "hh3cEponMulticastAddressList": hh3cEponMulticastAddressList,
       "hh3cEponMulticastStatus": hh3cEponMulticastStatus,
       "hh3cEponFileName": hh3cEponFileName,
       "hh3cEponDbaUpdateFileName": hh3cEponDbaUpdateFileName,
       "hh3cEponOnuUpdateFileName": hh3cEponOnuUpdateFileName,
       "hh3cEponOltMan": hh3cEponOltMan,
       "hh3cOltSysManTable": hh3cOltSysManTable,
       "hh3cOltSysManEntry": hh3cOltSysManEntry,
       "hh3cOltLaserOnTime": hh3cOltLaserOnTime,
       "hh3cOltLaserOffTime": hh3cOltLaserOffTime,
       "hh3cOltMultiCopyBrdCast": hh3cOltMultiCopyBrdCast,
       "hh3cOltEnableDiscardPacket": hh3cOltEnableDiscardPacket,
       "hh3cOltSelfTest": hh3cOltSelfTest,
       "hh3cOltSelfTestResult": hh3cOltSelfTestResult,
       "hh3cOltMaxRtt": hh3cOltMaxRtt,
       "hh3cOltInfoTable": hh3cOltInfoTable,
       "hh3cOltInfoEntry": hh3cOltInfoEntry,
       "hh3cOltFirmMajorVersion": hh3cOltFirmMajorVersion,
       "hh3cOltFirmMinorVersion": hh3cOltFirmMinorVersion,
       "hh3cOltHardMajorVersion": hh3cOltHardMajorVersion,
       "hh3cOltHardMinorVersion": hh3cOltHardMinorVersion,
       "hh3cOltAgcLockTime": hh3cOltAgcLockTime,
       "hh3cOltAgcCdrTime": hh3cOltAgcCdrTime,
       "hh3cOltMacAddress": hh3cOltMacAddress,
       "hh3cOltWorkMode": hh3cOltWorkMode,
       "hh3cOltOpticalPowerTx": hh3cOltOpticalPowerTx,
       "hh3cOltOpticalPowerRx": hh3cOltOpticalPowerRx,
       "hh3cOltDbaManTable": hh3cOltDbaManTable,
       "hh3cOltDbaManEntry": hh3cOltDbaManEntry,
       "hh3cOltDbaEnabledType": hh3cOltDbaEnabledType,
       "hh3cOltDbaDiscoveryLength": hh3cOltDbaDiscoveryLength,
       "hh3cOltDbaDiscovryFrequency": hh3cOltDbaDiscovryFrequency,
       "hh3cOltDbaCycleLength": hh3cOltDbaCycleLength,
       "hh3cOltDbaVersion": hh3cOltDbaVersion,
       "hh3cOltDbaUpdate": hh3cOltDbaUpdate,
       "hh3cOltDbaUpdateResult": hh3cOltDbaUpdateResult,
       "hh3cOltPortAlarmThresholdTable": hh3cOltPortAlarmThresholdTable,
       "hh3cOltPortAlarmThresholdEntry": hh3cOltPortAlarmThresholdEntry,
       "hh3cOltPortAlarmBerEnabled": hh3cOltPortAlarmBerEnabled,
       "hh3cOltPortAlarmBerDirect": hh3cOltPortAlarmBerDirect,
       "hh3cOltPortAlarmBerThreshold": hh3cOltPortAlarmBerThreshold,
       "hh3cOltPortAlarmFerEnabled": hh3cOltPortAlarmFerEnabled,
       "hh3cOltPortAlarmFerDirect": hh3cOltPortAlarmFerDirect,
       "hh3cOltPortAlarmFerThreshold": hh3cOltPortAlarmFerThreshold,
       "hh3cOltPortAlarmLlidMismatchEnabled": hh3cOltPortAlarmLlidMismatchEnabled,
       "hh3cOltPortAlarmLlidMismatchThreshold": hh3cOltPortAlarmLlidMismatchThreshold,
       "hh3cOltPortAlarmRemoteStableEnabled": hh3cOltPortAlarmRemoteStableEnabled,
       "hh3cOltPortAlarmLocalStableEnabled": hh3cOltPortAlarmLocalStableEnabled,
       "hh3cOltPortAlarmRegistrationEnabled": hh3cOltPortAlarmRegistrationEnabled,
       "hh3cOltPortAlarmOamDisconnectionEnabled": hh3cOltPortAlarmOamDisconnectionEnabled,
       "hh3cOltPortAlarmEncryptionKeyEnabled": hh3cOltPortAlarmEncryptionKeyEnabled,
       "hh3cOltPortAlarmVendorSpecificEnabled": hh3cOltPortAlarmVendorSpecificEnabled,
       "hh3cOltPortAlarmRegExcessEnabled": hh3cOltPortAlarmRegExcessEnabled,
       "hh3cOltPortAlarmDFEEnabled": hh3cOltPortAlarmDFEEnabled,
       "hh3cOltLaserOnTimeMinVal": hh3cOltLaserOnTimeMinVal,
       "hh3cOltLaserOnTimeMaxVal": hh3cOltLaserOnTimeMaxVal,
       "hh3cOltLaserOffTimeMinVal": hh3cOltLaserOffTimeMinVal,
       "hh3cOltLaserOffTimeMaxVal": hh3cOltLaserOffTimeMaxVal,
       "hh3cOltDbaDiscoveryLengthMinVal": hh3cOltDbaDiscoveryLengthMinVal,
       "hh3cOltDbaDiscoveryLengthMaxVal": hh3cOltDbaDiscoveryLengthMaxVal,
       "hh3cOltDbaDiscovryFrequencyMinVal": hh3cOltDbaDiscovryFrequencyMinVal,
       "hh3cOltDbaDiscovryFrequencyMaxVal": hh3cOltDbaDiscovryFrequencyMaxVal,
       "hh3cOltDbaCycleLengthMinVal": hh3cOltDbaCycleLengthMinVal,
       "hh3cOltDbaCycleLengthMaxVal": hh3cOltDbaCycleLengthMaxVal,
       "hh3cOltPortAlarmLlidMisMinVal": hh3cOltPortAlarmLlidMisMinVal,
       "hh3cOltPortAlarmLlidMisMaxVal": hh3cOltPortAlarmLlidMisMaxVal,
       "hh3cOltPortAlarmBerMinVal": hh3cOltPortAlarmBerMinVal,
       "hh3cOltPortAlarmBerMaxVal": hh3cOltPortAlarmBerMaxVal,
       "hh3cOltPortAlarmFerMinVal": hh3cOltPortAlarmFerMinVal,
       "hh3cOltPortAlarmFerMaxVal": hh3cOltPortAlarmFerMaxVal,
       "hh3cOnuSilentTable": hh3cOnuSilentTable,
       "hh3cOnuSilentEntry": hh3cOnuSilentEntry,
       "hh3cOnuSilentMacAddr": hh3cOnuSilentMacAddr,
       "hh3cOnuSilentTime": hh3cOnuSilentTime,
       "hh3cOltUsingOnuTable": hh3cOltUsingOnuTable,
       "hh3cOltUsingOnuEntry": hh3cOltUsingOnuEntry,
       "hh3cOltUsingOnuNum": hh3cOltUsingOnuNum,
       "hh3cOltUsingOnuIfIndex": hh3cOltUsingOnuIfIndex,
       "hh3cOltUsingOnuRowStatus": hh3cOltUsingOnuRowStatus,
       "hh3cEponOnuMan": hh3cEponOnuMan,
       "hh3cOnuSysManTable": hh3cOnuSysManTable,
       "hh3cOnuSysManEntry": hh3cOnuSysManEntry,
       "hh3cOnuEncryptMan": hh3cOnuEncryptMan,
       "hh3cOnuReAuthorize": hh3cOnuReAuthorize,
       "hh3cOnuMulticastFilterStatus": hh3cOnuMulticastFilterStatus,
       "hh3cOnuDbaReportQueueSetNumber": hh3cOnuDbaReportQueueSetNumber,
       "hh3cOnuRemoteFecStatus": hh3cOnuRemoteFecStatus,
       "hh3cOnuPortBerStatus": hh3cOnuPortBerStatus,
       "hh3cOnuReset": hh3cOnuReset,
       "hh3cOnuMulticastControlMode": hh3cOnuMulticastControlMode,
       "hh3cOnuAccessVlan": hh3cOnuAccessVlan,
       "hh3cOnuEncryptKey": hh3cOnuEncryptKey,
       "hh3cOnuUniUpDownTrapStatus": hh3cOnuUniUpDownTrapStatus,
       "hh3cOnuFecStatus": hh3cOnuFecStatus,
       "hh3cOnuMcastCtrlHostAgingTime": hh3cOnuMcastCtrlHostAgingTime,
       "hh3cOnuMulticastFastLeaveEnable": hh3cOnuMulticastFastLeaveEnable,
       "hh3cOnuPortIsolateEnable": hh3cOnuPortIsolateEnable,
       "hh3cOnuLinkTestTable": hh3cOnuLinkTestTable,
       "hh3cOnuLinkTestEntry": hh3cOnuLinkTestEntry,
       "hh3cOnuLinkTestFrameNum": hh3cOnuLinkTestFrameNum,
       "hh3cOnuLinkTestFrameSize": hh3cOnuLinkTestFrameSize,
       "hh3cOnuLinkTestDelay": hh3cOnuLinkTestDelay,
       "hh3cOnuLinkTestVlanTag": hh3cOnuLinkTestVlanTag,
       "hh3cOnuLinkTestVlanPriority": hh3cOnuLinkTestVlanPriority,
       "hh3cOnuLinkTestVlanTagID": hh3cOnuLinkTestVlanTagID,
       "hh3cOnuLinkTestResultSentFrameNum": hh3cOnuLinkTestResultSentFrameNum,
       "hh3cOnuLinkTestResultRetFrameNum": hh3cOnuLinkTestResultRetFrameNum,
       "hh3cOnuLinkTestResultRetErrFrameNum": hh3cOnuLinkTestResultRetErrFrameNum,
       "hh3cOnuLinkTestResultMinDelay": hh3cOnuLinkTestResultMinDelay,
       "hh3cOnuLinkTestResultMeanDelay": hh3cOnuLinkTestResultMeanDelay,
       "hh3cOnuLinkTestResultMaxDelay": hh3cOnuLinkTestResultMaxDelay,
       "hh3cOnuBandWidthTable": hh3cOnuBandWidthTable,
       "hh3cOnuBandWidthEntry": hh3cOnuBandWidthEntry,
       "hh3cOnuDownStreamBandWidthPolicy": hh3cOnuDownStreamBandWidthPolicy,
       "hh3cOnuDownStreamMaxBandWidth": hh3cOnuDownStreamMaxBandWidth,
       "hh3cOnuDownStreamMaxBurstSize": hh3cOnuDownStreamMaxBurstSize,
       "hh3cOnuDownStreamHighPriorityFirst": hh3cOnuDownStreamHighPriorityFirst,
       "hh3cOnuDownStreamShortFrameFirst": hh3cOnuDownStreamShortFrameFirst,
       "hh3cOnuP2PBandWidthPolicy": hh3cOnuP2PBandWidthPolicy,
       "hh3cOnuP2PMaxBandWidth": hh3cOnuP2PMaxBandWidth,
       "hh3cOnuP2PMaxBurstSize": hh3cOnuP2PMaxBurstSize,
       "hh3cOnuP2PHighPriorityFirst": hh3cOnuP2PHighPriorityFirst,
       "hh3cOnuP2PShortFrameFirst": hh3cOnuP2PShortFrameFirst,
       "hh3cOnuSlaManTable": hh3cOnuSlaManTable,
       "hh3cOnuSlaManEntry": hh3cOnuSlaManEntry,
       "hh3cOnuSlaMaxBandWidth": hh3cOnuSlaMaxBandWidth,
       "hh3cOnuSlaMinBandWidth": hh3cOnuSlaMinBandWidth,
       "hh3cOnuSlaBandWidthStepVal": hh3cOnuSlaBandWidthStepVal,
       "hh3cOnuSlaDelay": hh3cOnuSlaDelay,
       "hh3cOnuSlaFixedBandWidth": hh3cOnuSlaFixedBandWidth,
       "hh3cOnuSlaPriorityClass": hh3cOnuSlaPriorityClass,
       "hh3cOnuSlaFixedPacketSize": hh3cOnuSlaFixedPacketSize,
       "hh3cOnuInfoTable": hh3cOnuInfoTable,
       "hh3cOnuInfoEntry": hh3cOnuInfoEntry,
       "hh3cOnuHardMajorVersion": hh3cOnuHardMajorVersion,
       "hh3cOnuHardMinorVersion": hh3cOnuHardMinorVersion,
       "hh3cOnuSoftwareVersion": hh3cOnuSoftwareVersion,
       "hh3cOnuUniMacType": hh3cOnuUniMacType,
       "hh3cOnuLaserOnTime": hh3cOnuLaserOnTime,
       "hh3cOnuLaserOffTime": hh3cOnuLaserOffTime,
       "hh3cOnuGrantFifoDep": hh3cOnuGrantFifoDep,
       "hh3cOnuWorkMode": hh3cOnuWorkMode,
       "hh3cOnuPCBVersion": hh3cOnuPCBVersion,
       "hh3cOnuRtt": hh3cOnuRtt,
       "hh3cOnuEEPROMVersion": hh3cOnuEEPROMVersion,
       "hh3cOnuRegType": hh3cOnuRegType,
       "hh3cOnuHostType": hh3cOnuHostType,
       "hh3cOnuDistance": hh3cOnuDistance,
       "hh3cOnuLlid": hh3cOnuLlid,
       "hh3cOnuVendorId": hh3cOnuVendorId,
       "hh3cOnuFirmwareVersion": hh3cOnuFirmwareVersion,
       "hh3cOnuOpticalPowerReceivedByOlt": hh3cOnuOpticalPowerReceivedByOlt,
       "hh3cOnuMacAddrInfoTable": hh3cOnuMacAddrInfoTable,
       "hh3cOnuMacAddrInfoEntry": hh3cOnuMacAddrInfoEntry,
       "hh3cOnuMacIndex": hh3cOnuMacIndex,
       "hh3cOnuMacAddrFlag": hh3cOnuMacAddrFlag,
       "hh3cOnuMacAddress": hh3cOnuMacAddress,
       "hh3cOnuBindMacAddrTable": hh3cOnuBindMacAddrTable,
       "hh3cOnuBindMacAddrEntry": hh3cOnuBindMacAddrEntry,
       "hh3cOnuBindMacAddress": hh3cOnuBindMacAddress,
       "hh3cOnuBindType": hh3cOnuBindType,
       "hh3cOnuFirmwareUpdateTable": hh3cOnuFirmwareUpdateTable,
       "hh3cOnuFirmwareUpdateEntry": hh3cOnuFirmwareUpdateEntry,
       "hh3cOnuUpdate": hh3cOnuUpdate,
       "hh3cOnuUpdateResult": hh3cOnuUpdateResult,
       "hh3cOnuUpdateFileName": hh3cOnuUpdateFileName,
       "hh3cOnuLinkTestFrameNumMinVal": hh3cOnuLinkTestFrameNumMinVal,
       "hh3cOnuLinkTestFrameNumMaxVal": hh3cOnuLinkTestFrameNumMaxVal,
       "hh3cOnuSlaMaxBandWidthMinVal": hh3cOnuSlaMaxBandWidthMinVal,
       "hh3cOnuSlaMaxBandWidthMaxVal": hh3cOnuSlaMaxBandWidthMaxVal,
       "hh3cOnuSlaMinBandWidthMinVal": hh3cOnuSlaMinBandWidthMinVal,
       "hh3cOnuSlaMinBandWidthMaxVal": hh3cOnuSlaMinBandWidthMaxVal,
       "hh3cEponOnuTypeManTable": hh3cEponOnuTypeManTable,
       "hh3cEponOnuTypeManEntry": hh3cEponOnuTypeManEntry,
       "hh3cEponOnuTypeIndex": hh3cEponOnuTypeIndex,
       "hh3cEponOnuTypeDescr": hh3cEponOnuTypeDescr,
       "hh3cOnuPacketManTable": hh3cOnuPacketManTable,
       "hh3cOnuPacketManEntry": hh3cOnuPacketManEntry,
       "hh3cOnuPriorityTrust": hh3cOnuPriorityTrust,
       "hh3cOnuQueueScheduler": hh3cOnuQueueScheduler,
       "hh3cOnuProtocolTable": hh3cOnuProtocolTable,
       "hh3cOnuProtocolEntry": hh3cOnuProtocolEntry,
       "hh3cOnuStpStatus": hh3cOnuStpStatus,
       "hh3cOnuIgmpSnoopingStatus": hh3cOnuIgmpSnoopingStatus,
       "hh3cOnuDhcpsnoopingOption82": hh3cOnuDhcpsnoopingOption82,
       "hh3cOnuDhcpsnooping": hh3cOnuDhcpsnooping,
       "hh3cOnuPppoe": hh3cOnuPppoe,
       "hh3cOnuIgmpSnoopingHostAgingT": hh3cOnuIgmpSnoopingHostAgingT,
       "hh3cOnuIgmpSnoopingMaxRespT": hh3cOnuIgmpSnoopingMaxRespT,
       "hh3cOnuIgmpSnoopingRouterAgingT": hh3cOnuIgmpSnoopingRouterAgingT,
       "hh3cOnuIgmpSnoopingAggReportS": hh3cOnuIgmpSnoopingAggReportS,
       "hh3cOnuIgmpSnoopingAggLeaveS": hh3cOnuIgmpSnoopingAggLeaveS,
       "hh3cOnuDot1xTable": hh3cOnuDot1xTable,
       "hh3cOnuDot1xEntry": hh3cOnuDot1xEntry,
       "hh3cOnuDot1xAccount": hh3cOnuDot1xAccount,
       "hh3cOnuDot1xPassword": hh3cOnuDot1xPassword,
       "hh3cOnuPriorityQueueTable": hh3cOnuPriorityQueueTable,
       "hh3cOnuPriorityQueueEntry": hh3cOnuPriorityQueueEntry,
       "hh3cOnuQueueDirection": hh3cOnuQueueDirection,
       "hh3cOnuQueueId": hh3cOnuQueueId,
       "hh3cOnuQueueSize": hh3cOnuQueueSize,
       "hh3cOnuCountTable": hh3cOnuCountTable,
       "hh3cOnuCountEntry": hh3cOnuCountEntry,
       "hh3cOnuInCRCErrPkts": hh3cOnuInCRCErrPkts,
       "hh3cOnuOutDroppedFrames": hh3cOnuOutDroppedFrames,
       "hh3cEponOnuScalarGroup": hh3cEponOnuScalarGroup,
       "hh3cOnuPriorityQueueSizeMinVal": hh3cOnuPriorityQueueSizeMinVal,
       "hh3cOnuPriorityQueueSizeMaxVal": hh3cOnuPriorityQueueSizeMaxVal,
       "hh3cOnuPriorityQueueBandwidthMinVal": hh3cOnuPriorityQueueBandwidthMinVal,
       "hh3cOnuPriorityQueueBandwidthMaxVal": hh3cOnuPriorityQueueBandwidthMaxVal,
       "hh3cOnuPriorityQueueBurstsizeMinVal": hh3cOnuPriorityQueueBurstsizeMinVal,
       "hh3cOnuPriorityQueueBurstsizeMaxVal": hh3cOnuPriorityQueueBurstsizeMaxVal,
       "hh3cOnuUpdateByTypeNextIndex": hh3cOnuUpdateByTypeNextIndex,
       "hh3cOnuQueueBandwidthTable": hh3cOnuQueueBandwidthTable,
       "hh3cOnuQueueBandwidthEntry": hh3cOnuQueueBandwidthEntry,
       "hh3cOnuQueueMaxBandwidth": hh3cOnuQueueMaxBandwidth,
       "hh3cOnuQueueMaxBurstsize": hh3cOnuQueueMaxBurstsize,
       "hh3cOnuQueuePolicyStatus": hh3cOnuQueuePolicyStatus,
       "hh3cOnuIpAddressTable": hh3cOnuIpAddressTable,
       "hh3cOnuIpAddressEntry": hh3cOnuIpAddressEntry,
       "hh3cOnuIpAddress": hh3cOnuIpAddress,
       "hh3cOnuIpAddressMask": hh3cOnuIpAddressMask,
       "hh3cOnuIpAddressGateway": hh3cOnuIpAddressGateway,
       "hh3cOnuDhcpallocate": hh3cOnuDhcpallocate,
       "hh3cOnuManageVID": hh3cOnuManageVID,
       "hh3cOnuManageVlanIntfS": hh3cOnuManageVlanIntfS,
       "hh3cOnuChipSetInfoTable": hh3cOnuChipSetInfoTable,
       "hh3cOnuChipSetInfoEntry": hh3cOnuChipSetInfoEntry,
       "hh3cOnuChipSetVendorId": hh3cOnuChipSetVendorId,
       "hh3cOnuChipSetModel": hh3cOnuChipSetModel,
       "hh3cOnuChipSetRevision": hh3cOnuChipSetRevision,
       "hh3cOnuChipSetDesignDate": hh3cOnuChipSetDesignDate,
       "hh3cOnuCapabilityTable": hh3cOnuCapabilityTable,
       "hh3cOnuCapabilityEntry": hh3cOnuCapabilityEntry,
       "hh3cOnuServiceSupported": hh3cOnuServiceSupported,
       "hh3cOnuGEPortNumber": hh3cOnuGEPortNumber,
       "hh3cOnuFEPortNumber": hh3cOnuFEPortNumber,
       "hh3cOnuPOTSPortNumber": hh3cOnuPOTSPortNumber,
       "hh3cOnuE1PortsNumber": hh3cOnuE1PortsNumber,
       "hh3cOnuUpstreamQueueNumber": hh3cOnuUpstreamQueueNumber,
       "hh3cOnuMaxUpstreamQueuePerPort": hh3cOnuMaxUpstreamQueuePerPort,
       "hh3cOnuDownstreamQueueNumber": hh3cOnuDownstreamQueueNumber,
       "hh3cOnuMaxDownstreamQueuePerPort": hh3cOnuMaxDownstreamQueuePerPort,
       "hh3cOnuBatteryBackup": hh3cOnuBatteryBackup,
       "hh3cOnuIgspFastLeaveSupported": hh3cOnuIgspFastLeaveSupported,
       "hh3cOnuMCtrlFastLeaveSupported": hh3cOnuMCtrlFastLeaveSupported,
       "hh3cOnuDbaReportTable": hh3cOnuDbaReportTable,
       "hh3cOnuDbaReportEntry": hh3cOnuDbaReportEntry,
       "hh3cOnuDbaReportQueueId": hh3cOnuDbaReportQueueId,
       "hh3cOnuDbaReportThreshold": hh3cOnuDbaReportThreshold,
       "hh3cOnuDbaReportStatus": hh3cOnuDbaReportStatus,
       "hh3cOnuCosToLocalPrecedenceTable": hh3cOnuCosToLocalPrecedenceTable,
       "hh3cOnuCosToLocalPrecedenceEntry": hh3cOnuCosToLocalPrecedenceEntry,
       "hh3cOnuCosToLocalPrecedenceCosIndex": hh3cOnuCosToLocalPrecedenceCosIndex,
       "hh3cOnuCosToLocalPrecedenceValue": hh3cOnuCosToLocalPrecedenceValue,
       "hh3cEponOnuStpPortTable": hh3cEponOnuStpPortTable,
       "hh3cEponOnuStpPortEntry": hh3cEponOnuStpPortEntry,
       "hh3cEponStpPortIndex": hh3cEponStpPortIndex,
       "hh3cEponStpPortDescr": hh3cEponStpPortDescr,
       "hh3cEponStpPortState": hh3cEponStpPortState,
       "hh3cOnuPhysicalTable": hh3cOnuPhysicalTable,
       "hh3cOnuPhysicalEntry": hh3cOnuPhysicalEntry,
       "hh3cOnuBridgeMac": hh3cOnuBridgeMac,
       "hh3cOnuFirstPonMac": hh3cOnuFirstPonMac,
       "hh3cOnuFirstPonRegState": hh3cOnuFirstPonRegState,
       "hh3cOnuSecondPonMac": hh3cOnuSecondPonMac,
       "hh3cOnuSecondPonRegState": hh3cOnuSecondPonRegState,
       "hh3cOnuSmlkTable": hh3cOnuSmlkTable,
       "hh3cOnuSmlkEntry": hh3cOnuSmlkEntry,
       "hh3cOnuSmlkGroupID": hh3cOnuSmlkGroupID,
       "hh3cOnuSmlkFirstPonRole": hh3cOnuSmlkFirstPonRole,
       "hh3cOnuSmlkFirstPonStatus": hh3cOnuSmlkFirstPonStatus,
       "hh3cOnuSmlkSecondPonRole": hh3cOnuSmlkSecondPonRole,
       "hh3cOnuSmlkSecondPonStatus": hh3cOnuSmlkSecondPonStatus,
       "hh3cOnuRS485PropertiesTable": hh3cOnuRS485PropertiesTable,
       "hh3cOnuRS485PropertiesEntry": hh3cOnuRS485PropertiesEntry,
       "hh3cOnuRS485SerialIndex": hh3cOnuRS485SerialIndex,
       "hh3cOnuRS485BaudRate": hh3cOnuRS485BaudRate,
       "hh3cOnuRS485DataBits": hh3cOnuRS485DataBits,
       "hh3cOnuRS485Parity": hh3cOnuRS485Parity,
       "hh3cOnuRS485StopBits": hh3cOnuRS485StopBits,
       "hh3cOnuRS485FlowControl": hh3cOnuRS485FlowControl,
       "hh3cOnuRS485TXOctets": hh3cOnuRS485TXOctets,
       "hh3cOnuRS485RXOctets": hh3cOnuRS485RXOctets,
       "hh3cOnuRS485TXErrOctets": hh3cOnuRS485TXErrOctets,
       "hh3cOnuRS485RXErrOctets": hh3cOnuRS485RXErrOctets,
       "hh3cOnuRS485ResetStatistics": hh3cOnuRS485ResetStatistics,
       "hh3cOnuRS485SessionSummaryTable": hh3cOnuRS485SessionSummaryTable,
       "hh3cOnuRS485SessionSummaryEntry": hh3cOnuRS485SessionSummaryEntry,
       "hh3cOnuRS485SessionMaxNum": hh3cOnuRS485SessionMaxNum,
       "hh3cOnuRS485SessionNextIndex": hh3cOnuRS485SessionNextIndex,
       "hh3cOnuRS485SessionTable": hh3cOnuRS485SessionTable,
       "hh3cOnuRS485SessionEntry": hh3cOnuRS485SessionEntry,
       "hh3cOnuRS485SessionIndex": hh3cOnuRS485SessionIndex,
       "hh3cOnuRS485SessionType": hh3cOnuRS485SessionType,
       "hh3cOnuRS485SessionAddType": hh3cOnuRS485SessionAddType,
       "hh3cOnuRS485SessionRemoteIP": hh3cOnuRS485SessionRemoteIP,
       "hh3cOnuRS485SessionRemotePort": hh3cOnuRS485SessionRemotePort,
       "hh3cOnuRS485SessionLocalPort": hh3cOnuRS485SessionLocalPort,
       "hh3cOnuRS485SessionRowStatus": hh3cOnuRS485SessionRowStatus,
       "hh3cOnuRS485SessionErrInfoTable": hh3cOnuRS485SessionErrInfoTable,
       "hh3cOnuRS485SessionErrInfoEntry": hh3cOnuRS485SessionErrInfoEntry,
       "hh3cOnuRS485SessionErrInfo": hh3cOnuRS485SessionErrInfo,
       "hh3cEponBatchOperationMan": hh3cEponBatchOperationMan,
       "hh3cEponBatchOperationBySlotTable": hh3cEponBatchOperationBySlotTable,
       "hh3cEponBatchOperationBySlotEntry": hh3cEponBatchOperationBySlotEntry,
       "hh3cEponBatchOperationBySlotIndex": hh3cEponBatchOperationBySlotIndex,
       "hh3cEponBatchOperationBySlotType": hh3cEponBatchOperationBySlotType,
       "hh3cEponBatchOperationBySlot": hh3cEponBatchOperationBySlot,
       "hh3cEponBatchOperationBySlotResult": hh3cEponBatchOperationBySlotResult,
       "hh3cEponBatchOperationByOLTTable": hh3cEponBatchOperationByOLTTable,
       "hh3cEponBatchOperationByOLTEntry": hh3cEponBatchOperationByOLTEntry,
       "hh3cEponBatchOperationByOLTType": hh3cEponBatchOperationByOLTType,
       "hh3cEponBatchOperationByOLT": hh3cEponBatchOperationByOLT,
       "hh3cEponBatchOperationByOLTResult": hh3cEponBatchOperationByOLTResult,
       "hh3cOnuFirmwareUpdateByTypeTable": hh3cOnuFirmwareUpdateByTypeTable,
       "hh3cOnuFirmwareUpdateByTypeEntry": hh3cOnuFirmwareUpdateByTypeEntry,
       "hh3cOnuUpdateByOnuTypeIndex": hh3cOnuUpdateByOnuTypeIndex,
       "hh3cOnuUpdateByTypeOnuType": hh3cOnuUpdateByTypeOnuType,
       "hh3cOnuUpdateByTypeFileName": hh3cOnuUpdateByTypeFileName,
       "hh3cOnuUpdateByTypeRowStatus": hh3cOnuUpdateByTypeRowStatus,
       "hh3cEponErrorInfo": hh3cEponErrorInfo,
       "hh3cEponSoftwareErrorCode": hh3cEponSoftwareErrorCode,
       "hh3cOamVendorSpecificAlarmCode": hh3cOamVendorSpecificAlarmCode,
       "hh3cEponOnuRegErrorMacAddr": hh3cEponOnuRegErrorMacAddr,
       "hh3cOamEventLogType": hh3cOamEventLogType,
       "hh3cOamEventLogLocation": hh3cOamEventLogLocation,
       "hh3cEponLoopbackPortIndex": hh3cEponLoopbackPortIndex,
       "hh3cEponLoopbackPortDescr": hh3cEponLoopbackPortDescr,
       "hh3cOltPortAlarmLlidMisFrames": hh3cOltPortAlarmLlidMisFrames,
       "hh3cOltPortAlarmBer": hh3cOltPortAlarmBer,
       "hh3cOltPortAlarmFer": hh3cOltPortAlarmFer,
       "hh3cEponOnuRegSilentMac": hh3cEponOnuRegSilentMac,
       "hh3cEponOperationResult": hh3cEponOperationResult,
       "hh3cEponOnuLaserState": hh3cEponOnuLaserState,
       "hh3cEponTrap": hh3cEponTrap,
       "hh3cEponTrapPrefix": hh3cEponTrapPrefix,
       "hh3cEponPortAlarmBerTrap": hh3cEponPortAlarmBerTrap,
       "hh3cEponPortAlarmFerTrap": hh3cEponPortAlarmFerTrap,
       "hh3cEponErrorLLIDFrameTrap": hh3cEponErrorLLIDFrameTrap,
       "hh3cEponLoopBackEnableTrap": hh3cEponLoopBackEnableTrap,
       "hh3cEponOnuRegistrationErrTrap": hh3cEponOnuRegistrationErrTrap,
       "hh3cEponOamDisconnectionTrap": hh3cEponOamDisconnectionTrap,
       "hh3cEponEncryptionKeyErrTrap": hh3cEponEncryptionKeyErrTrap,
       "hh3cEponRemoteStableTrap": hh3cEponRemoteStableTrap,
       "hh3cEponLocalStableTrap": hh3cEponLocalStableTrap,
       "hh3cEponOamVendorSpecificTrap": hh3cEponOamVendorSpecificTrap,
       "hh3cEponSoftwareErrTrap": hh3cEponSoftwareErrTrap,
       "hh3cEponPortAlarmBerRecoverTrap": hh3cEponPortAlarmBerRecoverTrap,
       "hh3cEponPortAlarmFerRecoverTrap": hh3cEponPortAlarmFerRecoverTrap,
       "hh3cEponErrorLLIDFrameRecoverTrap": hh3cEponErrorLLIDFrameRecoverTrap,
       "hh3cEponLoopBackEnableRecoverTrap": hh3cEponLoopBackEnableRecoverTrap,
       "hh3cEponOnuRegistrationErrRecoverTrap": hh3cEponOnuRegistrationErrRecoverTrap,
       "hh3cEponOamDisconnectionRecoverTrap": hh3cEponOamDisconnectionRecoverTrap,
       "hh3cEponEncryptionKeyErrRecoverTrap": hh3cEponEncryptionKeyErrRecoverTrap,
       "hh3cEponRemoteStableRecoverTrap": hh3cEponRemoteStableRecoverTrap,
       "hh3cEponLocalStableRecoverTrap": hh3cEponLocalStableRecoverTrap,
       "hh3cEponOamVendorSpecificRecoverTrap": hh3cEponOamVendorSpecificRecoverTrap,
       "hh3cEponSoftwareErrRecoverTrap": hh3cEponSoftwareErrRecoverTrap,
       "hh3cDot3OamThresholdRecoverEvent": hh3cDot3OamThresholdRecoverEvent,
       "hh3cDot3OamNonThresholdRecoverEvent": hh3cDot3OamNonThresholdRecoverEvent,
       "hh3cEponOnuRegExcessTrap": hh3cEponOnuRegExcessTrap,
       "hh3cEponOnuRegExcessRecoverTrap": hh3cEponOnuRegExcessRecoverTrap,
       "hh3cEponOnuPowerOffTrap": hh3cEponOnuPowerOffTrap,
       "hh3cEponOltSwitchoverTrap": hh3cEponOltSwitchoverTrap,
       "hh3cEponOltDFETrap": hh3cEponOltDFETrap,
       "hh3cEponOltDFERecoverTrap": hh3cEponOltDFERecoverTrap,
       "hh3cEponOnuSilenceTrap": hh3cEponOnuSilenceTrap,
       "hh3cEponOnuSilenceRecoverTrap": hh3cEponOnuSilenceRecoverTrap,
       "hh3cEponOnuUpdateResultTrap": hh3cEponOnuUpdateResultTrap,
       "hh3cEponOnuAutoBindTrap": hh3cEponOnuAutoBindTrap,
       "hh3cEponOnuPortStpStateTrap": hh3cEponOnuPortStpStateTrap,
       "hh3cEponOnuLaserFailedTrap": hh3cEponOnuLaserFailedTrap,
       "hh3cOnuSmlkSwitchoverTrap": hh3cOnuSmlkSwitchoverTrap,
       "hh3cEponStat": hh3cEponStat,
       "hh3cEponStatTable": hh3cEponStatTable,
       "hh3cEponStatEntry": hh3cEponStatEntry,
       "hh3cEponStatFER": hh3cEponStatFER,
       "hh3cEponStatBER": hh3cEponStatBER}
)
