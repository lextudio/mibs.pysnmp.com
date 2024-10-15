# SNMP MIB module (TIMETRA-ELMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-ELMI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:02:11 2024
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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")

(tmnxChassisIndex,) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "tmnxChassisIndex")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(tmnxPortEtherEntry,
 tmnxPortPortID) = mibBuilder.importSymbols(
    "TIMETRA-PORT-MIB",
    "tmnxPortEtherEntry",
    "tmnxPortPortID")

(TmnxEncapVal,) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TmnxEncapVal")


# MODULE-IDENTITY

tmnxElmiMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 68)
)
tmnxElmiMIBModule.setRevisions(
        ("1908-10-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxElmiIdentifierString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )



# MIB Managed Objects in the order of their OIDs

_TmnxElmiConformance_ObjectIdentity = ObjectIdentity
tmnxElmiConformance = _TmnxElmiConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 68)
)
_TmnxElmiCompliances_ObjectIdentity = ObjectIdentity
tmnxElmiCompliances = _TmnxElmiCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 68, 1)
)
_TmnxElmiGroups_ObjectIdentity = ObjectIdentity
tmnxElmiGroups = _TmnxElmiGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 68, 2)
)
_TmnxElmiObjs_ObjectIdentity = ObjectIdentity
tmnxElmiObjs = _TmnxElmiObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68)
)
_TmnxElmiConfigurationTimeStamps_ObjectIdentity = ObjectIdentity
tmnxElmiConfigurationTimeStamps = _TmnxElmiConfigurationTimeStamps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 0)
)
_TmnxElmiIfConfigTableLastChanged_Type = TimeStamp
_TmnxElmiIfConfigTableLastChanged_Object = MibScalar
tmnxElmiIfConfigTableLastChanged = _TmnxElmiIfConfigTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 0, 1),
    _TmnxElmiIfConfigTableLastChanged_Type()
)
tmnxElmiIfConfigTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxElmiIfConfigTableLastChanged.setStatus("current")
_TmnxElmiEvcCfgTableLastChanged_Type = TimeStamp
_TmnxElmiEvcCfgTableLastChanged_Object = MibScalar
tmnxElmiEvcCfgTableLastChanged = _TmnxElmiEvcCfgTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 0, 2),
    _TmnxElmiEvcCfgTableLastChanged_Type()
)
tmnxElmiEvcCfgTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxElmiEvcCfgTableLastChanged.setStatus("current")
_TmnxElmiConfigurations_ObjectIdentity = ObjectIdentity
tmnxElmiConfigurations = _TmnxElmiConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 1)
)
_TmnxElmiIfConfigTable_Object = MibTable
tmnxElmiIfConfigTable = _TmnxElmiIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxElmiIfConfigTable.setStatus("current")
_TmnxElmiIfConfigEntry_Object = MibTableRow
tmnxElmiIfConfigEntry = _TmnxElmiIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxElmiIfConfigEntry.setStatus("current")


class _TmnxElmiIfCfgMode_Type(Integer32):
    """Custom type tmnxElmiIfCfgMode based on Integer32"""
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
        *(("none", 0),
          ("uniC", 2),
          ("uniN", 1))
    )


_TmnxElmiIfCfgMode_Type.__name__ = "Integer32"
_TmnxElmiIfCfgMode_Object = MibTableColumn
tmnxElmiIfCfgMode = _TmnxElmiIfCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 1, 1, 1, 1),
    _TmnxElmiIfCfgMode_Type()
)
tmnxElmiIfCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxElmiIfCfgMode.setStatus("current")


class _TmnxElmiIfCfgStatus_Type(Integer32):
    """Custom type tmnxElmiIfCfgStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_TmnxElmiIfCfgStatus_Type.__name__ = "Integer32"
_TmnxElmiIfCfgStatus_Object = MibTableColumn
tmnxElmiIfCfgStatus = _TmnxElmiIfCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 1, 1, 1, 2),
    _TmnxElmiIfCfgStatus_Type()
)
tmnxElmiIfCfgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxElmiIfCfgStatus.setStatus("current")


class _TmnxElmiIfCfgN393_Type(Unsigned32):
    """Custom type tmnxElmiIfCfgN393 based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_TmnxElmiIfCfgN393_Type.__name__ = "Unsigned32"
_TmnxElmiIfCfgN393_Object = MibTableColumn
tmnxElmiIfCfgN393 = _TmnxElmiIfCfgN393_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 1, 1, 1, 3),
    _TmnxElmiIfCfgN393_Type()
)
tmnxElmiIfCfgN393.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxElmiIfCfgN393.setStatus("current")


class _TmnxElmiIfCfgT391_Type(Unsigned32):
    """Custom type tmnxElmiIfCfgT391 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_TmnxElmiIfCfgT391_Type.__name__ = "Unsigned32"
_TmnxElmiIfCfgT391_Object = MibTableColumn
tmnxElmiIfCfgT391 = _TmnxElmiIfCfgT391_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 1, 1, 1, 4),
    _TmnxElmiIfCfgT391_Type()
)
tmnxElmiIfCfgT391.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxElmiIfCfgT391.setStatus("current")
if mibBuilder.loadTexts:
    tmnxElmiIfCfgT391.setUnits("seconds")


class _TmnxElmiIfCfgT392_Type(Unsigned32):
    """Custom type tmnxElmiIfCfgT392 based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_TmnxElmiIfCfgT392_Type.__name__ = "Unsigned32"
_TmnxElmiIfCfgT392_Object = MibTableColumn
tmnxElmiIfCfgT392 = _TmnxElmiIfCfgT392_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 1, 1, 1, 5),
    _TmnxElmiIfCfgT392_Type()
)
tmnxElmiIfCfgT392.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxElmiIfCfgT392.setStatus("current")
if mibBuilder.loadTexts:
    tmnxElmiIfCfgT392.setUnits("seconds")


class _TmnxElmiIfCfgUniType_Type(Integer32):
    """Custom type tmnxElmiIfCfgUniType based on Integer32"""
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
        *(("allToOneBundling", 1),
          ("bundling", 3),
          ("notUsed", 0),
          ("svcMultiplexNoBundling", 2))
    )


_TmnxElmiIfCfgUniType_Type.__name__ = "Integer32"
_TmnxElmiIfCfgUniType_Object = MibTableColumn
tmnxElmiIfCfgUniType = _TmnxElmiIfCfgUniType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 1, 1, 1, 6),
    _TmnxElmiIfCfgUniType_Type()
)
tmnxElmiIfCfgUniType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxElmiIfCfgUniType.setStatus("current")


class _TmnxElmiIfCfgUniIdentifier_Type(TmnxElmiIdentifierString):
    """Custom type tmnxElmiIfCfgUniIdentifier based on TmnxElmiIdentifierString"""
    subtypeSpec = TmnxElmiIdentifierString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxElmiIfCfgUniIdentifier_Type.__name__ = "TmnxElmiIdentifierString"
_TmnxElmiIfCfgUniIdentifier_Object = MibTableColumn
tmnxElmiIfCfgUniIdentifier = _TmnxElmiIfCfgUniIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 1, 1, 1, 7),
    _TmnxElmiIfCfgUniIdentifier_Type()
)
tmnxElmiIfCfgUniIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxElmiIfCfgUniIdentifier.setStatus("current")
_TmnxElmiEvcConfigTable_Object = MibTable
tmnxElmiEvcConfigTable = _TmnxElmiEvcConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxElmiEvcConfigTable.setStatus("current")
_TmnxElmiEvcConfigEntry_Object = MibTableRow
tmnxElmiEvcConfigEntry = _TmnxElmiEvcConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 1, 2, 1)
)
tmnxElmiEvcConfigEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-ELMI-MIB", "tmnxElmiEvcCfgVlanId"),
)
if mibBuilder.loadTexts:
    tmnxElmiEvcConfigEntry.setStatus("current")
_TmnxElmiEvcCfgVlanId_Type = TmnxEncapVal
_TmnxElmiEvcCfgVlanId_Object = MibTableColumn
tmnxElmiEvcCfgVlanId = _TmnxElmiEvcCfgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 1, 2, 1, 1),
    _TmnxElmiEvcCfgVlanId_Type()
)
tmnxElmiEvcCfgVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxElmiEvcCfgVlanId.setStatus("current")
_TmnxElmiEvcCfgIdentifier_Type = TmnxElmiIdentifierString
_TmnxElmiEvcCfgIdentifier_Object = MibTableColumn
tmnxElmiEvcCfgIdentifier = _TmnxElmiEvcCfgIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 1, 2, 1, 2),
    _TmnxElmiEvcCfgIdentifier_Type()
)
tmnxElmiEvcCfgIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxElmiEvcCfgIdentifier.setStatus("current")


class _TmnxElmiEvcCfgType_Type(Integer32):
    """Custom type tmnxElmiEvcCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mp2mp", 1),
          ("p2p", 0))
    )


_TmnxElmiEvcCfgType_Type.__name__ = "Integer32"
_TmnxElmiEvcCfgType_Object = MibTableColumn
tmnxElmiEvcCfgType = _TmnxElmiEvcCfgType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 1, 2, 1, 3),
    _TmnxElmiEvcCfgType_Type()
)
tmnxElmiEvcCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxElmiEvcCfgType.setStatus("current")


class _TmnxElmiEvcCfgStatus_Type(Integer32):
    """Custom type tmnxElmiEvcCfgStatus based on Integer32"""
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
        *(("active", 2),
          ("newAndActive", 3),
          ("newAndNotActive", 1),
          ("newAndPartiallyActive", 5),
          ("notActive", 0),
          ("partiallyActive", 4))
    )


_TmnxElmiEvcCfgStatus_Type.__name__ = "Integer32"
_TmnxElmiEvcCfgStatus_Object = MibTableColumn
tmnxElmiEvcCfgStatus = _TmnxElmiEvcCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 1, 2, 1, 4),
    _TmnxElmiEvcCfgStatus_Type()
)
tmnxElmiEvcCfgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxElmiEvcCfgStatus.setStatus("current")
_TmnxElmiEvcCfgStatusTimeStamp_Type = TimeStamp
_TmnxElmiEvcCfgStatusTimeStamp_Object = MibTableColumn
tmnxElmiEvcCfgStatusTimeStamp = _TmnxElmiEvcCfgStatusTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 1, 2, 1, 5),
    _TmnxElmiEvcCfgStatusTimeStamp_Type()
)
tmnxElmiEvcCfgStatusTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxElmiEvcCfgStatusTimeStamp.setStatus("current")
_TmnxElmiStatistics_ObjectIdentity = ObjectIdentity
tmnxElmiStatistics = _TmnxElmiStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 2)
)
_TmnxElmiStatTable_Object = MibTable
tmnxElmiStatTable = _TmnxElmiStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxElmiStatTable.setStatus("current")
_TmnxElmiStatEntry_Object = MibTableRow
tmnxElmiStatEntry = _TmnxElmiStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxElmiStatEntry.setStatus("current")
_TmnxElmiStatRxStatusEnqMsgTime_Type = TimeStamp
_TmnxElmiStatRxStatusEnqMsgTime_Object = MibTableColumn
tmnxElmiStatRxStatusEnqMsgTime = _TmnxElmiStatRxStatusEnqMsgTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 2, 1, 1, 1),
    _TmnxElmiStatRxStatusEnqMsgTime_Type()
)
tmnxElmiStatRxStatusEnqMsgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxElmiStatRxStatusEnqMsgTime.setStatus("current")
_TmnxElmiStatRxStatusEnqMsgs_Type = Counter32
_TmnxElmiStatRxStatusEnqMsgs_Object = MibTableColumn
tmnxElmiStatRxStatusEnqMsgs = _TmnxElmiStatRxStatusEnqMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 2, 1, 1, 2),
    _TmnxElmiStatRxStatusEnqMsgs_Type()
)
tmnxElmiStatRxStatusEnqMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxElmiStatRxStatusEnqMsgs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxElmiStatRxStatusEnqMsgs.setUnits("messages")
_TmnxElmiStatStatusEnqMsgTimeouts_Type = Counter32
_TmnxElmiStatStatusEnqMsgTimeouts_Object = MibTableColumn
tmnxElmiStatStatusEnqMsgTimeouts = _TmnxElmiStatStatusEnqMsgTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 2, 1, 1, 3),
    _TmnxElmiStatStatusEnqMsgTimeouts_Type()
)
tmnxElmiStatStatusEnqMsgTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxElmiStatStatusEnqMsgTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxElmiStatStatusEnqMsgTimeouts.setUnits("messages")
_TmnxElmiStatTxStatusMsgTime_Type = TimeStamp
_TmnxElmiStatTxStatusMsgTime_Object = MibTableColumn
tmnxElmiStatTxStatusMsgTime = _TmnxElmiStatTxStatusMsgTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 2, 1, 1, 4),
    _TmnxElmiStatTxStatusMsgTime_Type()
)
tmnxElmiStatTxStatusMsgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxElmiStatTxStatusMsgTime.setStatus("current")
_TmnxElmiStatTxStatusMsgs_Type = Counter32
_TmnxElmiStatTxStatusMsgs_Object = MibTableColumn
tmnxElmiStatTxStatusMsgs = _TmnxElmiStatTxStatusMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 2, 1, 1, 5),
    _TmnxElmiStatTxStatusMsgs_Type()
)
tmnxElmiStatTxStatusMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxElmiStatTxStatusMsgs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxElmiStatTxStatusMsgs.setUnits("messages")
_TmnxElmiStatRxStatusCheckTime_Type = TimeStamp
_TmnxElmiStatRxStatusCheckTime_Object = MibTableColumn
tmnxElmiStatRxStatusCheckTime = _TmnxElmiStatRxStatusCheckTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 2, 1, 1, 6),
    _TmnxElmiStatRxStatusCheckTime_Type()
)
tmnxElmiStatRxStatusCheckTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxElmiStatRxStatusCheckTime.setStatus("current")
_TmnxElmiStatTxStatusCheckTime_Type = TimeStamp
_TmnxElmiStatTxStatusCheckTime_Object = MibTableColumn
tmnxElmiStatTxStatusCheckTime = _TmnxElmiStatTxStatusCheckTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 2, 1, 1, 7),
    _TmnxElmiStatTxStatusCheckTime_Type()
)
tmnxElmiStatTxStatusCheckTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxElmiStatTxStatusCheckTime.setStatus("current")
_TmnxElmiStatDiscardedMsgs_Type = Counter32
_TmnxElmiStatDiscardedMsgs_Object = MibTableColumn
tmnxElmiStatDiscardedMsgs = _TmnxElmiStatDiscardedMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 2, 1, 1, 8),
    _TmnxElmiStatDiscardedMsgs_Type()
)
tmnxElmiStatDiscardedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxElmiStatDiscardedMsgs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxElmiStatDiscardedMsgs.setUnits("messages")
_TmnxElmiStatInvRxSeqNumMsgs_Type = Counter32
_TmnxElmiStatInvRxSeqNumMsgs_Object = MibTableColumn
tmnxElmiStatInvRxSeqNumMsgs = _TmnxElmiStatInvRxSeqNumMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 2, 1, 1, 9),
    _TmnxElmiStatInvRxSeqNumMsgs_Type()
)
tmnxElmiStatInvRxSeqNumMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxElmiStatInvRxSeqNumMsgs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxElmiStatInvRxSeqNumMsgs.setUnits("messages")
_TmnxElmiStatTxAsyncStatusMsgs_Type = Counter32
_TmnxElmiStatTxAsyncStatusMsgs_Object = MibTableColumn
tmnxElmiStatTxAsyncStatusMsgs = _TmnxElmiStatTxAsyncStatusMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 68, 2, 1, 1, 10),
    _TmnxElmiStatTxAsyncStatusMsgs_Type()
)
tmnxElmiStatTxAsyncStatusMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxElmiStatTxAsyncStatusMsgs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxElmiStatTxAsyncStatusMsgs.setUnits("messages")
_TmnxElmiNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxElmiNotifyPrefix = _TmnxElmiNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 68)
)
_TmnxElmiNotifications_ObjectIdentity = ObjectIdentity
tmnxElmiNotifications = _TmnxElmiNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 68, 0)
)
tmnxPortEtherEntry.registerAugmentions(
    ("TIMETRA-ELMI-MIB",
     "tmnxElmiIfConfigEntry")
)
tmnxElmiIfConfigEntry.setIndexNames(*tmnxPortEtherEntry.getIndexNames())
tmnxElmiIfConfigEntry.registerAugmentions(
    ("TIMETRA-ELMI-MIB",
     "tmnxElmiStatEntry")
)
tmnxElmiStatEntry.setIndexNames(*tmnxElmiIfConfigEntry.getIndexNames())

# Managed Objects groups

tmnxElmiTimeStampGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 68, 2, 1)
)
tmnxElmiTimeStampGroup.setObjects(
      *(("TIMETRA-ELMI-MIB", "tmnxElmiIfConfigTableLastChanged"),
        ("TIMETRA-ELMI-MIB", "tmnxElmiEvcCfgTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxElmiTimeStampGroup.setStatus("current")

tmnxElmiIfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 68, 2, 2)
)
tmnxElmiIfConfigGroup.setObjects(
      *(("TIMETRA-ELMI-MIB", "tmnxElmiIfCfgMode"),
        ("TIMETRA-ELMI-MIB", "tmnxElmiIfCfgStatus"),
        ("TIMETRA-ELMI-MIB", "tmnxElmiIfCfgN393"),
        ("TIMETRA-ELMI-MIB", "tmnxElmiIfCfgT391"),
        ("TIMETRA-ELMI-MIB", "tmnxElmiIfCfgT392"),
        ("TIMETRA-ELMI-MIB", "tmnxElmiIfCfgUniType"),
        ("TIMETRA-ELMI-MIB", "tmnxElmiIfCfgUniIdentifier"))
)
if mibBuilder.loadTexts:
    tmnxElmiIfConfigGroup.setStatus("current")

tmnxElmiEvcConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 68, 2, 3)
)
tmnxElmiEvcConfigGroup.setObjects(
      *(("TIMETRA-ELMI-MIB", "tmnxElmiEvcCfgIdentifier"),
        ("TIMETRA-ELMI-MIB", "tmnxElmiEvcCfgType"),
        ("TIMETRA-ELMI-MIB", "tmnxElmiEvcCfgStatus"),
        ("TIMETRA-ELMI-MIB", "tmnxElmiEvcCfgStatusTimeStamp"))
)
if mibBuilder.loadTexts:
    tmnxElmiEvcConfigGroup.setStatus("current")

tmnxElmiStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 68, 2, 4)
)
tmnxElmiStatsGroup.setObjects(
      *(("TIMETRA-ELMI-MIB", "tmnxElmiStatRxStatusEnqMsgTime"),
        ("TIMETRA-ELMI-MIB", "tmnxElmiStatRxStatusEnqMsgs"),
        ("TIMETRA-ELMI-MIB", "tmnxElmiStatStatusEnqMsgTimeouts"),
        ("TIMETRA-ELMI-MIB", "tmnxElmiStatTxStatusMsgTime"),
        ("TIMETRA-ELMI-MIB", "tmnxElmiStatTxStatusMsgs"),
        ("TIMETRA-ELMI-MIB", "tmnxElmiStatRxStatusCheckTime"),
        ("TIMETRA-ELMI-MIB", "tmnxElmiStatTxStatusCheckTime"),
        ("TIMETRA-ELMI-MIB", "tmnxElmiStatDiscardedMsgs"),
        ("TIMETRA-ELMI-MIB", "tmnxElmiStatInvRxSeqNumMsgs"),
        ("TIMETRA-ELMI-MIB", "tmnxElmiStatTxAsyncStatusMsgs"))
)
if mibBuilder.loadTexts:
    tmnxElmiStatsGroup.setStatus("current")


# Notification objects

tmnxElmiIfStatusChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 68, 0, 1)
)
tmnxElmiIfStatusChangeEvent.setObjects(
    ("TIMETRA-ELMI-MIB", "tmnxElmiIfCfgStatus")
)
if mibBuilder.loadTexts:
    tmnxElmiIfStatusChangeEvent.setStatus(
        "current"
    )

tmnxElmiEVCStatusChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 68, 0, 2)
)
tmnxElmiEVCStatusChangeEvent.setObjects(
    ("TIMETRA-ELMI-MIB", "tmnxElmiEvcCfgStatus")
)
if mibBuilder.loadTexts:
    tmnxElmiEVCStatusChangeEvent.setStatus(
        "current"
    )


# Notifications groups

tmnxElmiEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 68, 2, 5)
)
tmnxElmiEventGroup.setObjects(
      *(("TIMETRA-ELMI-MIB", "tmnxElmiIfStatusChangeEvent"),
        ("TIMETRA-ELMI-MIB", "tmnxElmiEVCStatusChangeEvent"))
)
if mibBuilder.loadTexts:
    tmnxElmiEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxElmiCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 68, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxElmiCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-ELMI-MIB",
    **{"TmnxElmiIdentifierString": TmnxElmiIdentifierString,
       "tmnxElmiMIBModule": tmnxElmiMIBModule,
       "tmnxElmiConformance": tmnxElmiConformance,
       "tmnxElmiCompliances": tmnxElmiCompliances,
       "tmnxElmiCompliance": tmnxElmiCompliance,
       "tmnxElmiGroups": tmnxElmiGroups,
       "tmnxElmiTimeStampGroup": tmnxElmiTimeStampGroup,
       "tmnxElmiIfConfigGroup": tmnxElmiIfConfigGroup,
       "tmnxElmiEvcConfigGroup": tmnxElmiEvcConfigGroup,
       "tmnxElmiStatsGroup": tmnxElmiStatsGroup,
       "tmnxElmiEventGroup": tmnxElmiEventGroup,
       "tmnxElmiObjs": tmnxElmiObjs,
       "tmnxElmiConfigurationTimeStamps": tmnxElmiConfigurationTimeStamps,
       "tmnxElmiIfConfigTableLastChanged": tmnxElmiIfConfigTableLastChanged,
       "tmnxElmiEvcCfgTableLastChanged": tmnxElmiEvcCfgTableLastChanged,
       "tmnxElmiConfigurations": tmnxElmiConfigurations,
       "tmnxElmiIfConfigTable": tmnxElmiIfConfigTable,
       "tmnxElmiIfConfigEntry": tmnxElmiIfConfigEntry,
       "tmnxElmiIfCfgMode": tmnxElmiIfCfgMode,
       "tmnxElmiIfCfgStatus": tmnxElmiIfCfgStatus,
       "tmnxElmiIfCfgN393": tmnxElmiIfCfgN393,
       "tmnxElmiIfCfgT391": tmnxElmiIfCfgT391,
       "tmnxElmiIfCfgT392": tmnxElmiIfCfgT392,
       "tmnxElmiIfCfgUniType": tmnxElmiIfCfgUniType,
       "tmnxElmiIfCfgUniIdentifier": tmnxElmiIfCfgUniIdentifier,
       "tmnxElmiEvcConfigTable": tmnxElmiEvcConfigTable,
       "tmnxElmiEvcConfigEntry": tmnxElmiEvcConfigEntry,
       "tmnxElmiEvcCfgVlanId": tmnxElmiEvcCfgVlanId,
       "tmnxElmiEvcCfgIdentifier": tmnxElmiEvcCfgIdentifier,
       "tmnxElmiEvcCfgType": tmnxElmiEvcCfgType,
       "tmnxElmiEvcCfgStatus": tmnxElmiEvcCfgStatus,
       "tmnxElmiEvcCfgStatusTimeStamp": tmnxElmiEvcCfgStatusTimeStamp,
       "tmnxElmiStatistics": tmnxElmiStatistics,
       "tmnxElmiStatTable": tmnxElmiStatTable,
       "tmnxElmiStatEntry": tmnxElmiStatEntry,
       "tmnxElmiStatRxStatusEnqMsgTime": tmnxElmiStatRxStatusEnqMsgTime,
       "tmnxElmiStatRxStatusEnqMsgs": tmnxElmiStatRxStatusEnqMsgs,
       "tmnxElmiStatStatusEnqMsgTimeouts": tmnxElmiStatStatusEnqMsgTimeouts,
       "tmnxElmiStatTxStatusMsgTime": tmnxElmiStatTxStatusMsgTime,
       "tmnxElmiStatTxStatusMsgs": tmnxElmiStatTxStatusMsgs,
       "tmnxElmiStatRxStatusCheckTime": tmnxElmiStatRxStatusCheckTime,
       "tmnxElmiStatTxStatusCheckTime": tmnxElmiStatTxStatusCheckTime,
       "tmnxElmiStatDiscardedMsgs": tmnxElmiStatDiscardedMsgs,
       "tmnxElmiStatInvRxSeqNumMsgs": tmnxElmiStatInvRxSeqNumMsgs,
       "tmnxElmiStatTxAsyncStatusMsgs": tmnxElmiStatTxAsyncStatusMsgs,
       "tmnxElmiNotifyPrefix": tmnxElmiNotifyPrefix,
       "tmnxElmiNotifications": tmnxElmiNotifications,
       "tmnxElmiIfStatusChangeEvent": tmnxElmiIfStatusChangeEvent,
       "tmnxElmiEVCStatusChangeEvent": tmnxElmiEVCStatusChangeEvent}
)
