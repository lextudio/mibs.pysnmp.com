# SNMP MIB module (SW-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SW-COMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:48 2024
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
 enterprises,
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
    "enterprises",
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

_Marconi_ObjectIdentity = ObjectIdentity
marconi = _Marconi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326)
)
_Systems_ObjectIdentity = ObjectIdentity
systems = _Systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2)
)
_External_ObjectIdentity = ObjectIdentity
external = _External_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20)
)
_Dlink_ObjectIdentity = ObjectIdentity
dlink = _Dlink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1)
)
_Dlinkcommon_ObjectIdentity = ObjectIdentity
dlinkcommon = _Dlinkcommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 1)
)
_Golf_ObjectIdentity = ObjectIdentity
golf = _Golf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2)
)
_Golfproducts_ObjectIdentity = ObjectIdentity
golfproducts = _Golfproducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1)
)
_Es2000_ObjectIdentity = ObjectIdentity
es2000 = _Es2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3)
)
_Golfcommon_ObjectIdentity = ObjectIdentity
golfcommon = _Golfcommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2)
)
_Marconi_mgmt_ObjectIdentity = ObjectIdentity
marconi_mgmt = _Marconi_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2)
)
_Es2000Mgmt_ObjectIdentity = ObjectIdentity
es2000Mgmt = _Es2000Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28)
)
_SwL2Mgmt_ObjectIdentity = ObjectIdentity
swL2Mgmt = _SwL2Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2)
)
_SwL2DevMgmt_ObjectIdentity = ObjectIdentity
swL2DevMgmt = _SwL2DevMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1)
)
_SwL2DevCtrl_ObjectIdentity = ObjectIdentity
swL2DevCtrl = _SwL2DevCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 1)
)


class _SwL2DevCtrlStpState_Type(Integer32):
    """Custom type swL2DevCtrlStpState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2DevCtrlStpState_Type.__name__ = "Integer32"
_SwL2DevCtrlStpState_Object = MibScalar
swL2DevCtrlStpState = _SwL2DevCtrlStpState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 1, 1),
    _SwL2DevCtrlStpState_Type()
)
swL2DevCtrlStpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlStpState.setStatus("mandatory")


class _SwL2DevCtrlPartitionModeState_Type(Integer32):
    """Custom type swL2DevCtrlPartitionModeState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2DevCtrlPartitionModeState_Type.__name__ = "Integer32"
_SwL2DevCtrlPartitionModeState_Object = MibScalar
swL2DevCtrlPartitionModeState = _SwL2DevCtrlPartitionModeState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 1, 2),
    _SwL2DevCtrlPartitionModeState_Type()
)
swL2DevCtrlPartitionModeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlPartitionModeState.setStatus("mandatory")


class _SwL2DevCtrlTableLockState_Type(Integer32):
    """Custom type swL2DevCtrlTableLockState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2DevCtrlTableLockState_Type.__name__ = "Integer32"
_SwL2DevCtrlTableLockState_Object = MibScalar
swL2DevCtrlTableLockState = _SwL2DevCtrlTableLockState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 1, 3),
    _SwL2DevCtrlTableLockState_Type()
)
swL2DevCtrlTableLockState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlTableLockState.setStatus("mandatory")


class _SwL2DevCtrlHOLState_Type(Integer32):
    """Custom type swL2DevCtrlHOLState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2DevCtrlHOLState_Type.__name__ = "Integer32"
_SwL2DevCtrlHOLState_Object = MibScalar
swL2DevCtrlHOLState = _SwL2DevCtrlHOLState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 1, 4),
    _SwL2DevCtrlHOLState_Type()
)
swL2DevCtrlHOLState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlHOLState.setStatus("mandatory")


class _SwL2DevCtrlAddrLookupModesAndHitRate_Type(Integer32):
    """Custom type swL2DevCtrlAddrLookupModesAndHitRate based on Integer32"""
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
        *(("level0", 1),
          ("level1", 2),
          ("level2", 3),
          ("level3", 4),
          ("level4", 5),
          ("level5", 6),
          ("level6", 7),
          ("level7", 8))
    )


_SwL2DevCtrlAddrLookupModesAndHitRate_Type.__name__ = "Integer32"
_SwL2DevCtrlAddrLookupModesAndHitRate_Object = MibScalar
swL2DevCtrlAddrLookupModesAndHitRate = _SwL2DevCtrlAddrLookupModesAndHitRate_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 1, 5),
    _SwL2DevCtrlAddrLookupModesAndHitRate_Type()
)
swL2DevCtrlAddrLookupModesAndHitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlAddrLookupModesAndHitRate.setStatus("mandatory")


class _SwL2DevCtrlBuzzerState_Type(Integer32):
    """Custom type swL2DevCtrlBuzzerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL2DevCtrlBuzzerState_Type.__name__ = "Integer32"
_SwL2DevCtrlBuzzerState_Object = MibScalar
swL2DevCtrlBuzzerState = _SwL2DevCtrlBuzzerState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 1, 6),
    _SwL2DevCtrlBuzzerState_Type()
)
swL2DevCtrlBuzzerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlBuzzerState.setStatus("mandatory")
_SwL2DevCtrlBuzzerTest_Type = Integer32
_SwL2DevCtrlBuzzerTest_Object = MibScalar
swL2DevCtrlBuzzerTest = _SwL2DevCtrlBuzzerTest_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 1, 7),
    _SwL2DevCtrlBuzzerTest_Type()
)
swL2DevCtrlBuzzerTest.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    swL2DevCtrlBuzzerTest.setStatus("mandatory")
_SwL2DevAlarm_ObjectIdentity = ObjectIdentity
swL2DevAlarm = _SwL2DevAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2)
)


class _SwL2DevAlarmPartition_Type(Integer32):
    """Custom type swL2DevAlarmPartition based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2DevAlarmPartition_Type.__name__ = "Integer32"
_SwL2DevAlarmPartition_Object = MibScalar
swL2DevAlarmPartition = _SwL2DevAlarmPartition_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 1),
    _SwL2DevAlarmPartition_Type()
)
swL2DevAlarmPartition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevAlarmPartition.setStatus("mandatory")


class _SwL2DevAlarmNewRoot_Type(Integer32):
    """Custom type swL2DevAlarmNewRoot based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2DevAlarmNewRoot_Type.__name__ = "Integer32"
_SwL2DevAlarmNewRoot_Object = MibScalar
swL2DevAlarmNewRoot = _SwL2DevAlarmNewRoot_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 2),
    _SwL2DevAlarmNewRoot_Type()
)
swL2DevAlarmNewRoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevAlarmNewRoot.setStatus("mandatory")


class _SwL2DevAlarmTopChange_Type(Integer32):
    """Custom type swL2DevAlarmTopChange based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2DevAlarmTopChange_Type.__name__ = "Integer32"
_SwL2DevAlarmTopChange_Object = MibScalar
swL2DevAlarmTopChange = _SwL2DevAlarmTopChange_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 3),
    _SwL2DevAlarmTopChange_Type()
)
swL2DevAlarmTopChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevAlarmTopChange.setStatus("mandatory")


class _SwL2DevAlarmLinkChange_Type(Integer32):
    """Custom type swL2DevAlarmLinkChange based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2DevAlarmLinkChange_Type.__name__ = "Integer32"
_SwL2DevAlarmLinkChange_Object = MibScalar
swL2DevAlarmLinkChange = _SwL2DevAlarmLinkChange_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 4),
    _SwL2DevAlarmLinkChange_Type()
)
swL2DevAlarmLinkChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevAlarmLinkChange.setStatus("mandatory")
_SwL2DevAlarmPowerTable_Object = MibTable
swL2DevAlarmPowerTable = _SwL2DevAlarmPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    swL2DevAlarmPowerTable.setStatus("mandatory")
_SwL2DevAlarmPowerEntry_Object = MibTableRow
swL2DevAlarmPowerEntry = _SwL2DevAlarmPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 5, 1)
)
swL2DevAlarmPowerEntry.setIndexNames(
    (0, "SW-COMMON-MIB", "swL2DevAlarmPowerIndex"),
)
if mibBuilder.loadTexts:
    swL2DevAlarmPowerEntry.setStatus("mandatory")
_SwL2DevAlarmPowerIndex_Type = Integer32
_SwL2DevAlarmPowerIndex_Object = MibTableColumn
swL2DevAlarmPowerIndex = _SwL2DevAlarmPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 5, 1, 1),
    _SwL2DevAlarmPowerIndex_Type()
)
swL2DevAlarmPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2DevAlarmPowerIndex.setStatus("mandatory")


class _SwL2DevAlarmPowerTemperature_Type(Integer32):
    """Custom type swL2DevAlarmPowerTemperature based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2DevAlarmPowerTemperature_Type.__name__ = "Integer32"
_SwL2DevAlarmPowerTemperature_Object = MibTableColumn
swL2DevAlarmPowerTemperature = _SwL2DevAlarmPowerTemperature_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 5, 1, 2),
    _SwL2DevAlarmPowerTemperature_Type()
)
swL2DevAlarmPowerTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevAlarmPowerTemperature.setStatus("mandatory")


class _SwL2DevAlarmPowerVolt_Type(Integer32):
    """Custom type swL2DevAlarmPowerVolt based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2DevAlarmPowerVolt_Type.__name__ = "Integer32"
_SwL2DevAlarmPowerVolt_Object = MibTableColumn
swL2DevAlarmPowerVolt = _SwL2DevAlarmPowerVolt_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 5, 1, 3),
    _SwL2DevAlarmPowerVolt_Type()
)
swL2DevAlarmPowerVolt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevAlarmPowerVolt.setStatus("mandatory")


class _SwL2DevAlarmPowerCurrent_Type(Integer32):
    """Custom type swL2DevAlarmPowerCurrent based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2DevAlarmPowerCurrent_Type.__name__ = "Integer32"
_SwL2DevAlarmPowerCurrent_Object = MibTableColumn
swL2DevAlarmPowerCurrent = _SwL2DevAlarmPowerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 5, 1, 4),
    _SwL2DevAlarmPowerCurrent_Type()
)
swL2DevAlarmPowerCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevAlarmPowerCurrent.setStatus("mandatory")


class _SwL2DevAlarmPowerFan_Type(Integer32):
    """Custom type swL2DevAlarmPowerFan based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2DevAlarmPowerFan_Type.__name__ = "Integer32"
_SwL2DevAlarmPowerFan_Object = MibTableColumn
swL2DevAlarmPowerFan = _SwL2DevAlarmPowerFan_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 5, 1, 5),
    _SwL2DevAlarmPowerFan_Type()
)
swL2DevAlarmPowerFan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevAlarmPowerFan.setStatus("mandatory")
_SwL2DevAlarmSystemFanTable_Object = MibTable
swL2DevAlarmSystemFanTable = _SwL2DevAlarmSystemFanTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    swL2DevAlarmSystemFanTable.setStatus("mandatory")
_SwL2DevAlarmSystemFanEntry_Object = MibTableRow
swL2DevAlarmSystemFanEntry = _SwL2DevAlarmSystemFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 6, 1)
)
swL2DevAlarmSystemFanEntry.setIndexNames(
    (0, "SW-COMMON-MIB", "swL2DevAlarmSystemFanIndex"),
)
if mibBuilder.loadTexts:
    swL2DevAlarmSystemFanEntry.setStatus("mandatory")
_SwL2DevAlarmSystemFanIndex_Type = Integer32
_SwL2DevAlarmSystemFanIndex_Object = MibTableColumn
swL2DevAlarmSystemFanIndex = _SwL2DevAlarmSystemFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 6, 1, 1),
    _SwL2DevAlarmSystemFanIndex_Type()
)
swL2DevAlarmSystemFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2DevAlarmSystemFanIndex.setStatus("mandatory")


class _SwL2DevAlarmSystemFanState_Type(Integer32):
    """Custom type swL2DevAlarmSystemFanState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("notAvailable", 4),
          ("other", 1))
    )


_SwL2DevAlarmSystemFanState_Type.__name__ = "Integer32"
_SwL2DevAlarmSystemFanState_Object = MibTableColumn
swL2DevAlarmSystemFanState = _SwL2DevAlarmSystemFanState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 6, 1, 2),
    _SwL2DevAlarmSystemFanState_Type()
)
swL2DevAlarmSystemFanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevAlarmSystemFanState.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SW-COMMON-MIB",
    **{"marconi": marconi,
       "systems": systems,
       "external": external,
       "dlink": dlink,
       "dlinkcommon": dlinkcommon,
       "golf": golf,
       "golfproducts": golfproducts,
       "es2000": es2000,
       "golfcommon": golfcommon,
       "marconi-mgmt": marconi_mgmt,
       "es2000Mgmt": es2000Mgmt,
       "swL2Mgmt": swL2Mgmt,
       "swL2DevMgmt": swL2DevMgmt,
       "swL2DevCtrl": swL2DevCtrl,
       "swL2DevCtrlStpState": swL2DevCtrlStpState,
       "swL2DevCtrlPartitionModeState": swL2DevCtrlPartitionModeState,
       "swL2DevCtrlTableLockState": swL2DevCtrlTableLockState,
       "swL2DevCtrlHOLState": swL2DevCtrlHOLState,
       "swL2DevCtrlAddrLookupModesAndHitRate": swL2DevCtrlAddrLookupModesAndHitRate,
       "swL2DevCtrlBuzzerState": swL2DevCtrlBuzzerState,
       "swL2DevCtrlBuzzerTest": swL2DevCtrlBuzzerTest,
       "swL2DevAlarm": swL2DevAlarm,
       "swL2DevAlarmPartition": swL2DevAlarmPartition,
       "swL2DevAlarmNewRoot": swL2DevAlarmNewRoot,
       "swL2DevAlarmTopChange": swL2DevAlarmTopChange,
       "swL2DevAlarmLinkChange": swL2DevAlarmLinkChange,
       "swL2DevAlarmPowerTable": swL2DevAlarmPowerTable,
       "swL2DevAlarmPowerEntry": swL2DevAlarmPowerEntry,
       "swL2DevAlarmPowerIndex": swL2DevAlarmPowerIndex,
       "swL2DevAlarmPowerTemperature": swL2DevAlarmPowerTemperature,
       "swL2DevAlarmPowerVolt": swL2DevAlarmPowerVolt,
       "swL2DevAlarmPowerCurrent": swL2DevAlarmPowerCurrent,
       "swL2DevAlarmPowerFan": swL2DevAlarmPowerFan,
       "swL2DevAlarmSystemFanTable": swL2DevAlarmSystemFanTable,
       "swL2DevAlarmSystemFanEntry": swL2DevAlarmSystemFanEntry,
       "swL2DevAlarmSystemFanIndex": swL2DevAlarmSystemFanIndex,
       "swL2DevAlarmSystemFanState": swL2DevAlarmSystemFanState}
)
