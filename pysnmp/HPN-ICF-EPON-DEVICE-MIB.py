# SNMP MIB module (HPN-ICF-EPON-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-EPON-DEVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:08 2024
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

(hpnicfEpon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfEpon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "mib-2",
    "zeroDotZero")

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

hpnicfEponDeviceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4)
)
hpnicfEponDeviceMIB.setRevisions(
        ("2004-09-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfEponDeviceObjectMIB_ObjectIdentity = ObjectIdentity
hpnicfEponDeviceObjectMIB = _HpnicfEponDeviceObjectMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1)
)
_HpnicfEponDeviceObjects_ObjectIdentity = ObjectIdentity
hpnicfEponDeviceObjects = _HpnicfEponDeviceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1)
)
_HpnicfEponDeviceControlObjects_ObjectIdentity = ObjectIdentity
hpnicfEponDeviceControlObjects = _HpnicfEponDeviceControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 1)
)
_HpnicfEponDeviceControlTable_Object = MibTable
hpnicfEponDeviceControlTable = _HpnicfEponDeviceControlTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfEponDeviceControlTable.setStatus("current")
_HpnicfEponDeviceControlEntry_Object = MibTableRow
hpnicfEponDeviceControlEntry = _HpnicfEponDeviceControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 1, 1, 1)
)
hpnicfEponDeviceControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEponDeviceControlEntry.setStatus("current")


class _HpnicfEponDeviceObjectReset_Type(Integer32):
    """Custom type hpnicfEponDeviceObjectReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 2),
          ("running", 1))
    )


_HpnicfEponDeviceObjectReset_Type.__name__ = "Integer32"
_HpnicfEponDeviceObjectReset_Object = MibTableColumn
hpnicfEponDeviceObjectReset = _HpnicfEponDeviceObjectReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 1, 1, 1, 1),
    _HpnicfEponDeviceObjectReset_Type()
)
hpnicfEponDeviceObjectReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponDeviceObjectReset.setStatus("current")


class _HpnicfEponDeviceObjectModes_Type(Integer32):
    """Custom type hpnicfEponDeviceObjectModes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("olt", 1),
          ("onu", 2))
    )


_HpnicfEponDeviceObjectModes_Type.__name__ = "Integer32"
_HpnicfEponDeviceObjectModes_Object = MibTableColumn
hpnicfEponDeviceObjectModes = _HpnicfEponDeviceObjectModes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 1, 1, 1, 2),
    _HpnicfEponDeviceObjectModes_Type()
)
hpnicfEponDeviceObjectModes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceObjectModes.setStatus("current")


class _HpnicfEponDeviceObjectFecEnabled_Type(Integer32):
    """Custom type hpnicfEponDeviceObjectFecEnabled based on Integer32"""
    defaultValue = 1

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
        *(("fecRxEnabled", 3),
          ("fecTxEnabled", 2),
          ("fecTxRxEnabled", 4),
          ("noFecEnabled", 1))
    )


_HpnicfEponDeviceObjectFecEnabled_Type.__name__ = "Integer32"
_HpnicfEponDeviceObjectFecEnabled_Object = MibTableColumn
hpnicfEponDeviceObjectFecEnabled = _HpnicfEponDeviceObjectFecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 1, 1, 1, 4),
    _HpnicfEponDeviceObjectFecEnabled_Type()
)
hpnicfEponDeviceObjectFecEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponDeviceObjectFecEnabled.setStatus("current")


class _HpnicfEponDeviceObjectOamMode_Type(Integer32):
    """Custom type hpnicfEponDeviceObjectOamMode based on Integer32"""
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
        *(("noOam", 1),
          ("oamServer", 2),
          ("oamclient", 3))
    )


_HpnicfEponDeviceObjectOamMode_Type.__name__ = "Integer32"
_HpnicfEponDeviceObjectOamMode_Object = MibTableColumn
hpnicfEponDeviceObjectOamMode = _HpnicfEponDeviceObjectOamMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 1, 1, 1, 5),
    _HpnicfEponDeviceObjectOamMode_Type()
)
hpnicfEponDeviceObjectOamMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponDeviceObjectOamMode.setStatus("current")


class _HpnicfEponDeviceObjectDeviceReadyMode_Type(Integer32):
    """Custom type hpnicfEponDeviceObjectDeviceReadyMode based on Integer32"""
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
        *(("inProcess", 2),
          ("notReady", 1),
          ("ready", 3))
    )


_HpnicfEponDeviceObjectDeviceReadyMode_Type.__name__ = "Integer32"
_HpnicfEponDeviceObjectDeviceReadyMode_Object = MibTableColumn
hpnicfEponDeviceObjectDeviceReadyMode = _HpnicfEponDeviceObjectDeviceReadyMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 1, 1, 1, 6),
    _HpnicfEponDeviceObjectDeviceReadyMode_Type()
)
hpnicfEponDeviceObjectDeviceReadyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponDeviceObjectDeviceReadyMode.setStatus("current")


class _HpnicfEponDeviceObjectPowerDown_Type(TruthValue):
    """Custom type hpnicfEponDeviceObjectPowerDown based on TruthValue"""


_HpnicfEponDeviceObjectPowerDown_Object = MibTableColumn
hpnicfEponDeviceObjectPowerDown = _HpnicfEponDeviceObjectPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 1, 1, 1, 7),
    _HpnicfEponDeviceObjectPowerDown_Type()
)
hpnicfEponDeviceObjectPowerDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponDeviceObjectPowerDown.setStatus("current")
_HpnicfEponDeviceObjectNumberOfLLIDs_Type = Integer32
_HpnicfEponDeviceObjectNumberOfLLIDs_Object = MibTableColumn
hpnicfEponDeviceObjectNumberOfLLIDs = _HpnicfEponDeviceObjectNumberOfLLIDs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 1, 1, 1, 8),
    _HpnicfEponDeviceObjectNumberOfLLIDs_Type()
)
hpnicfEponDeviceObjectNumberOfLLIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceObjectNumberOfLLIDs.setStatus("current")


class _HpnicfEponDeviceObjectReportThreshold_Type(Integer32):
    """Custom type hpnicfEponDeviceObjectReportThreshold based on Integer32"""
    defaultValue = 0


_HpnicfEponDeviceObjectReportThreshold_Object = MibTableColumn
hpnicfEponDeviceObjectReportThreshold = _HpnicfEponDeviceObjectReportThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 1, 1, 1, 9),
    _HpnicfEponDeviceObjectReportThreshold_Type()
)
hpnicfEponDeviceObjectReportThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponDeviceObjectReportThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEponDeviceObjectReportThreshold.setUnits("TQ (16nsec)")


class _HpnicfEponDeviceRemoteMACAddressLLIDControl_Type(Integer32):
    """Custom type hpnicfEponDeviceRemoteMACAddressLLIDControl based on Integer32"""
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
        *(("none", 1),
          ("resetLog", 2),
          ("useDefaultReporting", 3))
    )


_HpnicfEponDeviceRemoteMACAddressLLIDControl_Type.__name__ = "Integer32"
_HpnicfEponDeviceRemoteMACAddressLLIDControl_Object = MibTableColumn
hpnicfEponDeviceRemoteMACAddressLLIDControl = _HpnicfEponDeviceRemoteMACAddressLLIDControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 1, 1, 1, 10),
    _HpnicfEponDeviceRemoteMACAddressLLIDControl_Type()
)
hpnicfEponDeviceRemoteMACAddressLLIDControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponDeviceRemoteMACAddressLLIDControl.setStatus("current")
_HpnicfEponDeviceRemoteMACAddressLLIDTable_Object = MibTable
hpnicfEponDeviceRemoteMACAddressLLIDTable = _HpnicfEponDeviceRemoteMACAddressLLIDTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfEponDeviceRemoteMACAddressLLIDTable.setStatus("current")
_HpnicfEponDeviceRemoteMACAddressLLIDEntry_Object = MibTableRow
hpnicfEponDeviceRemoteMACAddressLLIDEntry = _HpnicfEponDeviceRemoteMACAddressLLIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 1, 2, 1)
)
hpnicfEponDeviceRemoteMACAddressLLIDEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEponDeviceRemoteMACAddressLLIDEntry.setStatus("current")


class _HpnicfEponDeviceRemoteMACAddressLLIDName_Type(SnmpAdminString):
    """Custom type hpnicfEponDeviceRemoteMACAddressLLIDName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfEponDeviceRemoteMACAddressLLIDName_Type.__name__ = "SnmpAdminString"
_HpnicfEponDeviceRemoteMACAddressLLIDName_Object = MibTableColumn
hpnicfEponDeviceRemoteMACAddressLLIDName = _HpnicfEponDeviceRemoteMACAddressLLIDName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 1, 2, 1, 1),
    _HpnicfEponDeviceRemoteMACAddressLLIDName_Type()
)
hpnicfEponDeviceRemoteMACAddressLLIDName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponDeviceRemoteMACAddressLLIDName.setStatus("current")


class _HpnicfEponDeviceRMadlLLID_Type(Unsigned32):
    """Custom type hpnicfEponDeviceRMadlLLID based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfEponDeviceRMadlLLID_Type.__name__ = "Unsigned32"
_HpnicfEponDeviceRMadlLLID_Object = MibTableColumn
hpnicfEponDeviceRMadlLLID = _HpnicfEponDeviceRMadlLLID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 1, 2, 1, 2),
    _HpnicfEponDeviceRMadlLLID_Type()
)
hpnicfEponDeviceRMadlLLID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponDeviceRMadlLLID.setStatus("current")


class _HpnicfEponDeviceRMadlLogID_Type(ObjectIdentifier):
    """Custom type hpnicfEponDeviceRMadlLogID based on ObjectIdentifier"""
    defaultValue = (0, 0)


_HpnicfEponDeviceRMadlLogID_Object = MibTableColumn
hpnicfEponDeviceRMadlLogID = _HpnicfEponDeviceRMadlLogID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 1, 2, 1, 3),
    _HpnicfEponDeviceRMadlLogID_Type()
)
hpnicfEponDeviceRMadlLogID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponDeviceRMadlLogID.setStatus("current")
_HpnicfEponDeviceRMadlRemoteAddress_Type = MacAddress
_HpnicfEponDeviceRMadlRemoteAddress_Object = MibTableColumn
hpnicfEponDeviceRMadlRemoteAddress = _HpnicfEponDeviceRMadlRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 1, 2, 1, 4),
    _HpnicfEponDeviceRMadlRemoteAddress_Type()
)
hpnicfEponDeviceRMadlRemoteAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponDeviceRMadlRemoteAddress.setStatus("current")


class _HpnicfEponDeviceRMadlType_Type(Integer32):
    """Custom type hpnicfEponDeviceRMadlType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRegister", 1),
          ("registered", 2))
    )


_HpnicfEponDeviceRMadlType_Type.__name__ = "Integer32"
_HpnicfEponDeviceRMadlType_Object = MibTableColumn
hpnicfEponDeviceRMadlType = _HpnicfEponDeviceRMadlType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 1, 2, 1, 5),
    _HpnicfEponDeviceRMadlType_Type()
)
hpnicfEponDeviceRMadlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponDeviceRMadlType.setStatus("current")


class _HpnicfEponDeviceRMadlAction_Type(Integer32):
    """Custom type hpnicfEponDeviceRMadlAction based on Integer32"""
    defaultValue = 1

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
        *(("deregister", 3),
          ("none", 1),
          ("register", 2),
          ("reregister", 4))
    )


_HpnicfEponDeviceRMadlAction_Type.__name__ = "Integer32"
_HpnicfEponDeviceRMadlAction_Object = MibTableColumn
hpnicfEponDeviceRMadlAction = _HpnicfEponDeviceRMadlAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 1, 2, 1, 6),
    _HpnicfEponDeviceRMadlAction_Type()
)
hpnicfEponDeviceRMadlAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponDeviceRMadlAction.setStatus("current")
_HpnicfEponDeviceRMadlEntryStatus_Type = RowStatus
_HpnicfEponDeviceRMadlEntryStatus_Object = MibTableColumn
hpnicfEponDeviceRMadlEntryStatus = _HpnicfEponDeviceRMadlEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 1, 2, 1, 7),
    _HpnicfEponDeviceRMadlEntryStatus_Type()
)
hpnicfEponDeviceRMadlEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponDeviceRMadlEntryStatus.setStatus("current")
_HpnicfEponDeviceStatObjects_ObjectIdentity = ObjectIdentity
hpnicfEponDeviceStatObjects = _HpnicfEponDeviceStatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 2)
)
_HpnicfEponDeviceStatTable_Object = MibTable
hpnicfEponDeviceStatTable = _HpnicfEponDeviceStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatTable.setStatus("current")
_HpnicfEponDeviceStatEntry_Object = MibTableRow
hpnicfEponDeviceStatEntry = _HpnicfEponDeviceStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 2, 1, 1)
)
hpnicfEponDeviceStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatEntry.setStatus("current")
_HpnicfEponDeviceStatTxFramesQueue0_Type = Counter32
_HpnicfEponDeviceStatTxFramesQueue0_Object = MibTableColumn
hpnicfEponDeviceStatTxFramesQueue0 = _HpnicfEponDeviceStatTxFramesQueue0_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 2, 1, 1, 1),
    _HpnicfEponDeviceStatTxFramesQueue0_Type()
)
hpnicfEponDeviceStatTxFramesQueue0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatTxFramesQueue0.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatTxFramesQueue0.setUnits("frames")
_HpnicfEponDeviceStatTxFramesQueue1_Type = Counter32
_HpnicfEponDeviceStatTxFramesQueue1_Object = MibTableColumn
hpnicfEponDeviceStatTxFramesQueue1 = _HpnicfEponDeviceStatTxFramesQueue1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 2, 1, 1, 2),
    _HpnicfEponDeviceStatTxFramesQueue1_Type()
)
hpnicfEponDeviceStatTxFramesQueue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatTxFramesQueue1.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatTxFramesQueue1.setUnits("frames")
_HpnicfEponDeviceStatTxFramesQueue2_Type = Counter32
_HpnicfEponDeviceStatTxFramesQueue2_Object = MibTableColumn
hpnicfEponDeviceStatTxFramesQueue2 = _HpnicfEponDeviceStatTxFramesQueue2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 2, 1, 1, 3),
    _HpnicfEponDeviceStatTxFramesQueue2_Type()
)
hpnicfEponDeviceStatTxFramesQueue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatTxFramesQueue2.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatTxFramesQueue2.setUnits("frames")
_HpnicfEponDeviceStatTxFramesQueue3_Type = Counter32
_HpnicfEponDeviceStatTxFramesQueue3_Object = MibTableColumn
hpnicfEponDeviceStatTxFramesQueue3 = _HpnicfEponDeviceStatTxFramesQueue3_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 2, 1, 1, 4),
    _HpnicfEponDeviceStatTxFramesQueue3_Type()
)
hpnicfEponDeviceStatTxFramesQueue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatTxFramesQueue3.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatTxFramesQueue3.setUnits("frames")
_HpnicfEponDeviceStatTxFramesQueue4_Type = Counter32
_HpnicfEponDeviceStatTxFramesQueue4_Object = MibTableColumn
hpnicfEponDeviceStatTxFramesQueue4 = _HpnicfEponDeviceStatTxFramesQueue4_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 2, 1, 1, 5),
    _HpnicfEponDeviceStatTxFramesQueue4_Type()
)
hpnicfEponDeviceStatTxFramesQueue4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatTxFramesQueue4.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatTxFramesQueue4.setUnits("frames")
_HpnicfEponDeviceStatTxFramesQueue5_Type = Counter32
_HpnicfEponDeviceStatTxFramesQueue5_Object = MibTableColumn
hpnicfEponDeviceStatTxFramesQueue5 = _HpnicfEponDeviceStatTxFramesQueue5_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 2, 1, 1, 6),
    _HpnicfEponDeviceStatTxFramesQueue5_Type()
)
hpnicfEponDeviceStatTxFramesQueue5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatTxFramesQueue5.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatTxFramesQueue5.setUnits("frames")
_HpnicfEponDeviceStatTxFramesQueue6_Type = Counter32
_HpnicfEponDeviceStatTxFramesQueue6_Object = MibTableColumn
hpnicfEponDeviceStatTxFramesQueue6 = _HpnicfEponDeviceStatTxFramesQueue6_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 2, 1, 1, 7),
    _HpnicfEponDeviceStatTxFramesQueue6_Type()
)
hpnicfEponDeviceStatTxFramesQueue6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatTxFramesQueue6.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatTxFramesQueue6.setUnits("frames")
_HpnicfEponDeviceStatTxFramesQueue7_Type = Counter32
_HpnicfEponDeviceStatTxFramesQueue7_Object = MibTableColumn
hpnicfEponDeviceStatTxFramesQueue7 = _HpnicfEponDeviceStatTxFramesQueue7_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 2, 1, 1, 8),
    _HpnicfEponDeviceStatTxFramesQueue7_Type()
)
hpnicfEponDeviceStatTxFramesQueue7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatTxFramesQueue7.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatTxFramesQueue7.setUnits("frames")
_HpnicfEponDeviceStatRxFramesQueue0_Type = Counter32
_HpnicfEponDeviceStatRxFramesQueue0_Object = MibTableColumn
hpnicfEponDeviceStatRxFramesQueue0 = _HpnicfEponDeviceStatRxFramesQueue0_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 2, 1, 1, 9),
    _HpnicfEponDeviceStatRxFramesQueue0_Type()
)
hpnicfEponDeviceStatRxFramesQueue0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatRxFramesQueue0.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatRxFramesQueue0.setUnits("frames")
_HpnicfEponDeviceStatRxFramesQueue1_Type = Counter32
_HpnicfEponDeviceStatRxFramesQueue1_Object = MibTableColumn
hpnicfEponDeviceStatRxFramesQueue1 = _HpnicfEponDeviceStatRxFramesQueue1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 2, 1, 1, 10),
    _HpnicfEponDeviceStatRxFramesQueue1_Type()
)
hpnicfEponDeviceStatRxFramesQueue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatRxFramesQueue1.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatRxFramesQueue1.setUnits("frames")
_HpnicfEponDeviceStatRxFramesQueue2_Type = Counter32
_HpnicfEponDeviceStatRxFramesQueue2_Object = MibTableColumn
hpnicfEponDeviceStatRxFramesQueue2 = _HpnicfEponDeviceStatRxFramesQueue2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 2, 1, 1, 11),
    _HpnicfEponDeviceStatRxFramesQueue2_Type()
)
hpnicfEponDeviceStatRxFramesQueue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatRxFramesQueue2.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatRxFramesQueue2.setUnits("frames")
_HpnicfEponDeviceStatRxFramesQueue3_Type = Counter32
_HpnicfEponDeviceStatRxFramesQueue3_Object = MibTableColumn
hpnicfEponDeviceStatRxFramesQueue3 = _HpnicfEponDeviceStatRxFramesQueue3_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 2, 1, 1, 12),
    _HpnicfEponDeviceStatRxFramesQueue3_Type()
)
hpnicfEponDeviceStatRxFramesQueue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatRxFramesQueue3.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatRxFramesQueue3.setUnits("frames")
_HpnicfEponDeviceStatRxFramesQueue4_Type = Counter32
_HpnicfEponDeviceStatRxFramesQueue4_Object = MibTableColumn
hpnicfEponDeviceStatRxFramesQueue4 = _HpnicfEponDeviceStatRxFramesQueue4_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 2, 1, 1, 13),
    _HpnicfEponDeviceStatRxFramesQueue4_Type()
)
hpnicfEponDeviceStatRxFramesQueue4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatRxFramesQueue4.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatRxFramesQueue4.setUnits("frames")
_HpnicfEponDeviceStatRxFramesQueue5_Type = Counter32
_HpnicfEponDeviceStatRxFramesQueue5_Object = MibTableColumn
hpnicfEponDeviceStatRxFramesQueue5 = _HpnicfEponDeviceStatRxFramesQueue5_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 2, 1, 1, 14),
    _HpnicfEponDeviceStatRxFramesQueue5_Type()
)
hpnicfEponDeviceStatRxFramesQueue5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatRxFramesQueue5.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatRxFramesQueue5.setUnits("frames")
_HpnicfEponDeviceStatRxFramesQueue6_Type = Counter32
_HpnicfEponDeviceStatRxFramesQueue6_Object = MibTableColumn
hpnicfEponDeviceStatRxFramesQueue6 = _HpnicfEponDeviceStatRxFramesQueue6_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 2, 1, 1, 15),
    _HpnicfEponDeviceStatRxFramesQueue6_Type()
)
hpnicfEponDeviceStatRxFramesQueue6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatRxFramesQueue6.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatRxFramesQueue6.setUnits("frames")
_HpnicfEponDeviceStatRxFramesQueue7_Type = Counter32
_HpnicfEponDeviceStatRxFramesQueue7_Object = MibTableColumn
hpnicfEponDeviceStatRxFramesQueue7 = _HpnicfEponDeviceStatRxFramesQueue7_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 2, 1, 1, 16),
    _HpnicfEponDeviceStatRxFramesQueue7_Type()
)
hpnicfEponDeviceStatRxFramesQueue7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatRxFramesQueue7.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatRxFramesQueue7.setUnits("frames")
_HpnicfEponDeviceStatDroppedFramesQueue0_Type = Counter32
_HpnicfEponDeviceStatDroppedFramesQueue0_Object = MibTableColumn
hpnicfEponDeviceStatDroppedFramesQueue0 = _HpnicfEponDeviceStatDroppedFramesQueue0_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 2, 1, 1, 17),
    _HpnicfEponDeviceStatDroppedFramesQueue0_Type()
)
hpnicfEponDeviceStatDroppedFramesQueue0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatDroppedFramesQueue0.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatDroppedFramesQueue0.setUnits("frames")
_HpnicfEponDeviceStatDroppedFramesQueue1_Type = Counter32
_HpnicfEponDeviceStatDroppedFramesQueue1_Object = MibTableColumn
hpnicfEponDeviceStatDroppedFramesQueue1 = _HpnicfEponDeviceStatDroppedFramesQueue1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 2, 1, 1, 18),
    _HpnicfEponDeviceStatDroppedFramesQueue1_Type()
)
hpnicfEponDeviceStatDroppedFramesQueue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatDroppedFramesQueue1.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatDroppedFramesQueue1.setUnits("frames")
_HpnicfEponDeviceStatDroppedFramesQueue2_Type = Counter32
_HpnicfEponDeviceStatDroppedFramesQueue2_Object = MibTableColumn
hpnicfEponDeviceStatDroppedFramesQueue2 = _HpnicfEponDeviceStatDroppedFramesQueue2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 2, 1, 1, 19),
    _HpnicfEponDeviceStatDroppedFramesQueue2_Type()
)
hpnicfEponDeviceStatDroppedFramesQueue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatDroppedFramesQueue2.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatDroppedFramesQueue2.setUnits("frames")
_HpnicfEponDeviceStatDroppedFramesQueue3_Type = Counter32
_HpnicfEponDeviceStatDroppedFramesQueue3_Object = MibTableColumn
hpnicfEponDeviceStatDroppedFramesQueue3 = _HpnicfEponDeviceStatDroppedFramesQueue3_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 2, 1, 1, 20),
    _HpnicfEponDeviceStatDroppedFramesQueue3_Type()
)
hpnicfEponDeviceStatDroppedFramesQueue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatDroppedFramesQueue3.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatDroppedFramesQueue3.setUnits("frames")
_HpnicfEponDeviceStatDroppedFramesQueue4_Type = Counter32
_HpnicfEponDeviceStatDroppedFramesQueue4_Object = MibTableColumn
hpnicfEponDeviceStatDroppedFramesQueue4 = _HpnicfEponDeviceStatDroppedFramesQueue4_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 2, 1, 1, 21),
    _HpnicfEponDeviceStatDroppedFramesQueue4_Type()
)
hpnicfEponDeviceStatDroppedFramesQueue4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatDroppedFramesQueue4.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatDroppedFramesQueue4.setUnits("frames")
_HpnicfEponDeviceStatDroppedFramesQueue5_Type = Counter32
_HpnicfEponDeviceStatDroppedFramesQueue5_Object = MibTableColumn
hpnicfEponDeviceStatDroppedFramesQueue5 = _HpnicfEponDeviceStatDroppedFramesQueue5_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 2, 1, 1, 22),
    _HpnicfEponDeviceStatDroppedFramesQueue5_Type()
)
hpnicfEponDeviceStatDroppedFramesQueue5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatDroppedFramesQueue5.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatDroppedFramesQueue5.setUnits("frames")
_HpnicfEponDeviceStatDroppedFramesQueue6_Type = Counter32
_HpnicfEponDeviceStatDroppedFramesQueue6_Object = MibTableColumn
hpnicfEponDeviceStatDroppedFramesQueue6 = _HpnicfEponDeviceStatDroppedFramesQueue6_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 2, 1, 1, 23),
    _HpnicfEponDeviceStatDroppedFramesQueue6_Type()
)
hpnicfEponDeviceStatDroppedFramesQueue6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatDroppedFramesQueue6.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatDroppedFramesQueue6.setUnits("frames")
_HpnicfEponDeviceStatDroppedFramesQueue7_Type = Counter32
_HpnicfEponDeviceStatDroppedFramesQueue7_Object = MibTableColumn
hpnicfEponDeviceStatDroppedFramesQueue7 = _HpnicfEponDeviceStatDroppedFramesQueue7_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 2, 1, 1, 24),
    _HpnicfEponDeviceStatDroppedFramesQueue7_Type()
)
hpnicfEponDeviceStatDroppedFramesQueue7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatDroppedFramesQueue7.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEponDeviceStatDroppedFramesQueue7.setUnits("frames")
_HpnicfEponDeviceEventObjects_ObjectIdentity = ObjectIdentity
hpnicfEponDeviceEventObjects = _HpnicfEponDeviceEventObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3)
)
_HpnicfEponDeviceEventObjectTable_Object = MibTable
hpnicfEponDeviceEventObjectTable = _HpnicfEponDeviceEventObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpnicfEponDeviceEventObjectTable.setStatus("current")
_HpnicfEponDeviceEventObjectEntry_Object = MibTableRow
hpnicfEponDeviceEventObjectEntry = _HpnicfEponDeviceEventObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 1, 1)
)
hpnicfEponDeviceEventObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEponDeviceEventObjectEntry.setStatus("current")


class _HpnicfEponDeviceSampleMinimum_Type(Integer32):
    """Custom type hpnicfEponDeviceSampleMinimum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfEponDeviceSampleMinimum_Type.__name__ = "Integer32"
_HpnicfEponDeviceSampleMinimum_Object = MibTableColumn
hpnicfEponDeviceSampleMinimum = _HpnicfEponDeviceSampleMinimum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 1, 1, 1),
    _HpnicfEponDeviceSampleMinimum_Type()
)
hpnicfEponDeviceSampleMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponDeviceSampleMinimum.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfEponDeviceSampleMinimum.setUnits("seconds")
_HpnicfEponDeviceDyingGaspAlarmState_Type = TruthValue
_HpnicfEponDeviceDyingGaspAlarmState_Object = MibTableColumn
hpnicfEponDeviceDyingGaspAlarmState = _HpnicfEponDeviceDyingGaspAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 1, 1, 2),
    _HpnicfEponDeviceDyingGaspAlarmState_Type()
)
hpnicfEponDeviceDyingGaspAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceDyingGaspAlarmState.setStatus("current")


class _HpnicfEponDeviceDyingGaspAlarmEnabled_Type(TruthValue):
    """Custom type hpnicfEponDeviceDyingGaspAlarmEnabled based on TruthValue"""


_HpnicfEponDeviceDyingGaspAlarmEnabled_Object = MibTableColumn
hpnicfEponDeviceDyingGaspAlarmEnabled = _HpnicfEponDeviceDyingGaspAlarmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 1, 1, 3),
    _HpnicfEponDeviceDyingGaspAlarmEnabled_Type()
)
hpnicfEponDeviceDyingGaspAlarmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponDeviceDyingGaspAlarmEnabled.setStatus("current")
_HpnicfEponDeviceCriticalEventState_Type = TruthValue
_HpnicfEponDeviceCriticalEventState_Object = MibTableColumn
hpnicfEponDeviceCriticalEventState = _HpnicfEponDeviceCriticalEventState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 1, 1, 4),
    _HpnicfEponDeviceCriticalEventState_Type()
)
hpnicfEponDeviceCriticalEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceCriticalEventState.setStatus("current")


class _HpnicfEponDeviceCriticalEventEnabled_Type(TruthValue):
    """Custom type hpnicfEponDeviceCriticalEventEnabled based on TruthValue"""


_HpnicfEponDeviceCriticalEventEnabled_Object = MibTableColumn
hpnicfEponDeviceCriticalEventEnabled = _HpnicfEponDeviceCriticalEventEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 1, 1, 5),
    _HpnicfEponDeviceCriticalEventEnabled_Type()
)
hpnicfEponDeviceCriticalEventEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponDeviceCriticalEventEnabled.setStatus("current")
_HpnicfEponDeviceLocalLinkFaultAlarmState_Type = TruthValue
_HpnicfEponDeviceLocalLinkFaultAlarmState_Object = MibTableColumn
hpnicfEponDeviceLocalLinkFaultAlarmState = _HpnicfEponDeviceLocalLinkFaultAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 1, 1, 6),
    _HpnicfEponDeviceLocalLinkFaultAlarmState_Type()
)
hpnicfEponDeviceLocalLinkFaultAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceLocalLinkFaultAlarmState.setStatus("current")


class _HpnicfEponDeviceLocalLinkFaultAlarmEnabled_Type(TruthValue):
    """Custom type hpnicfEponDeviceLocalLinkFaultAlarmEnabled based on TruthValue"""


_HpnicfEponDeviceLocalLinkFaultAlarmEnabled_Object = MibTableColumn
hpnicfEponDeviceLocalLinkFaultAlarmEnabled = _HpnicfEponDeviceLocalLinkFaultAlarmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 1, 1, 7),
    _HpnicfEponDeviceLocalLinkFaultAlarmEnabled_Type()
)
hpnicfEponDeviceLocalLinkFaultAlarmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponDeviceLocalLinkFaultAlarmEnabled.setStatus("current")
_HpnicfEponDeviceTemperatureEventIndicationState_Type = TruthValue
_HpnicfEponDeviceTemperatureEventIndicationState_Object = MibTableColumn
hpnicfEponDeviceTemperatureEventIndicationState = _HpnicfEponDeviceTemperatureEventIndicationState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 1, 1, 8),
    _HpnicfEponDeviceTemperatureEventIndicationState_Type()
)
hpnicfEponDeviceTemperatureEventIndicationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceTemperatureEventIndicationState.setStatus("current")


class _HpnicfEponDeviceTemperatureEventIndicationEnabled_Type(TruthValue):
    """Custom type hpnicfEponDeviceTemperatureEventIndicationEnabled based on TruthValue"""


_HpnicfEponDeviceTemperatureEventIndicationEnabled_Object = MibTableColumn
hpnicfEponDeviceTemperatureEventIndicationEnabled = _HpnicfEponDeviceTemperatureEventIndicationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 1, 1, 9),
    _HpnicfEponDeviceTemperatureEventIndicationEnabled_Type()
)
hpnicfEponDeviceTemperatureEventIndicationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponDeviceTemperatureEventIndicationEnabled.setStatus("current")
_HpnicfEponDevicePowerVoltageEventIndicationState_Type = TruthValue
_HpnicfEponDevicePowerVoltageEventIndicationState_Object = MibTableColumn
hpnicfEponDevicePowerVoltageEventIndicationState = _HpnicfEponDevicePowerVoltageEventIndicationState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 1, 1, 10),
    _HpnicfEponDevicePowerVoltageEventIndicationState_Type()
)
hpnicfEponDevicePowerVoltageEventIndicationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDevicePowerVoltageEventIndicationState.setStatus("current")


class _HpnicfEponDevicePowerVoltageEventIndicationEnabled_Type(TruthValue):
    """Custom type hpnicfEponDevicePowerVoltageEventIndicationEnabled based on TruthValue"""


_HpnicfEponDevicePowerVoltageEventIndicationEnabled_Object = MibTableColumn
hpnicfEponDevicePowerVoltageEventIndicationEnabled = _HpnicfEponDevicePowerVoltageEventIndicationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 1, 1, 11),
    _HpnicfEponDevicePowerVoltageEventIndicationEnabled_Type()
)
hpnicfEponDevicePowerVoltageEventIndicationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponDevicePowerVoltageEventIndicationEnabled.setStatus("current")
_HpnicfEponDeviceGlobalEventState_Type = TruthValue
_HpnicfEponDeviceGlobalEventState_Object = MibTableColumn
hpnicfEponDeviceGlobalEventState = _HpnicfEponDeviceGlobalEventState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 1, 1, 12),
    _HpnicfEponDeviceGlobalEventState_Type()
)
hpnicfEponDeviceGlobalEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceGlobalEventState.setStatus("current")


class _HpnicfEponDeviceGlobalEventEnabled_Type(TruthValue):
    """Custom type hpnicfEponDeviceGlobalEventEnabled based on TruthValue"""


_HpnicfEponDeviceGlobalEventEnabled_Object = MibTableColumn
hpnicfEponDeviceGlobalEventEnabled = _HpnicfEponDeviceGlobalEventEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 1, 1, 13),
    _HpnicfEponDeviceGlobalEventEnabled_Type()
)
hpnicfEponDeviceGlobalEventEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponDeviceGlobalEventEnabled.setStatus("current")
_HpnicfEponDeviceErroredSymbolPeriodEventState_Type = TruthValue
_HpnicfEponDeviceErroredSymbolPeriodEventState_Object = MibTableColumn
hpnicfEponDeviceErroredSymbolPeriodEventState = _HpnicfEponDeviceErroredSymbolPeriodEventState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 1, 1, 14),
    _HpnicfEponDeviceErroredSymbolPeriodEventState_Type()
)
hpnicfEponDeviceErroredSymbolPeriodEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceErroredSymbolPeriodEventState.setStatus("current")


class _HpnicfEponDeviceErroredSymbolPeriodEventEnabled_Type(TruthValue):
    """Custom type hpnicfEponDeviceErroredSymbolPeriodEventEnabled based on TruthValue"""


_HpnicfEponDeviceErroredSymbolPeriodEventEnabled_Object = MibTableColumn
hpnicfEponDeviceErroredSymbolPeriodEventEnabled = _HpnicfEponDeviceErroredSymbolPeriodEventEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 1, 1, 15),
    _HpnicfEponDeviceErroredSymbolPeriodEventEnabled_Type()
)
hpnicfEponDeviceErroredSymbolPeriodEventEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponDeviceErroredSymbolPeriodEventEnabled.setStatus("current")
_HpnicfEponDeviceErroredFrameEventState_Type = TruthValue
_HpnicfEponDeviceErroredFrameEventState_Object = MibTableColumn
hpnicfEponDeviceErroredFrameEventState = _HpnicfEponDeviceErroredFrameEventState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 1, 1, 16),
    _HpnicfEponDeviceErroredFrameEventState_Type()
)
hpnicfEponDeviceErroredFrameEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceErroredFrameEventState.setStatus("current")


class _HpnicfEponDeviceErroredFrameEventEnabled_Type(TruthValue):
    """Custom type hpnicfEponDeviceErroredFrameEventEnabled based on TruthValue"""


_HpnicfEponDeviceErroredFrameEventEnabled_Object = MibTableColumn
hpnicfEponDeviceErroredFrameEventEnabled = _HpnicfEponDeviceErroredFrameEventEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 1, 1, 17),
    _HpnicfEponDeviceErroredFrameEventEnabled_Type()
)
hpnicfEponDeviceErroredFrameEventEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponDeviceErroredFrameEventEnabled.setStatus("current")
_HpnicfEponDeviceErroredFramePeriodEventState_Type = TruthValue
_HpnicfEponDeviceErroredFramePeriodEventState_Object = MibTableColumn
hpnicfEponDeviceErroredFramePeriodEventState = _HpnicfEponDeviceErroredFramePeriodEventState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 1, 1, 18),
    _HpnicfEponDeviceErroredFramePeriodEventState_Type()
)
hpnicfEponDeviceErroredFramePeriodEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceErroredFramePeriodEventState.setStatus("current")


class _HpnicfEponDeviceErroredFramePeriodEventEnabled_Type(TruthValue):
    """Custom type hpnicfEponDeviceErroredFramePeriodEventEnabled based on TruthValue"""


_HpnicfEponDeviceErroredFramePeriodEventEnabled_Object = MibTableColumn
hpnicfEponDeviceErroredFramePeriodEventEnabled = _HpnicfEponDeviceErroredFramePeriodEventEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 1, 1, 19),
    _HpnicfEponDeviceErroredFramePeriodEventEnabled_Type()
)
hpnicfEponDeviceErroredFramePeriodEventEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponDeviceErroredFramePeriodEventEnabled.setStatus("current")
_HpnicfEponDeviceErroredFrameSecondsSummaryEventState_Type = TruthValue
_HpnicfEponDeviceErroredFrameSecondsSummaryEventState_Object = MibTableColumn
hpnicfEponDeviceErroredFrameSecondsSummaryEventState = _HpnicfEponDeviceErroredFrameSecondsSummaryEventState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 1, 1, 20),
    _HpnicfEponDeviceErroredFrameSecondsSummaryEventState_Type()
)
hpnicfEponDeviceErroredFrameSecondsSummaryEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceErroredFrameSecondsSummaryEventState.setStatus("current")


class _HpnicfEponDeviceErroredFrameSecondsSummaryEventEnabled_Type(TruthValue):
    """Custom type hpnicfEponDeviceErroredFrameSecondsSummaryEventEnabled based on TruthValue"""


_HpnicfEponDeviceErroredFrameSecondsSummaryEventEnabled_Object = MibTableColumn
hpnicfEponDeviceErroredFrameSecondsSummaryEventEnabled = _HpnicfEponDeviceErroredFrameSecondsSummaryEventEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 1, 1, 21),
    _HpnicfEponDeviceErroredFrameSecondsSummaryEventEnabled_Type()
)
hpnicfEponDeviceErroredFrameSecondsSummaryEventEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponDeviceErroredFrameSecondsSummaryEventEnabled.setStatus("current")
_HpnicfEponDeviceOrganizationSpecificEventState_Type = TruthValue
_HpnicfEponDeviceOrganizationSpecificEventState_Object = MibTableColumn
hpnicfEponDeviceOrganizationSpecificEventState = _HpnicfEponDeviceOrganizationSpecificEventState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 1, 1, 22),
    _HpnicfEponDeviceOrganizationSpecificEventState_Type()
)
hpnicfEponDeviceOrganizationSpecificEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceOrganizationSpecificEventState.setStatus("current")


class _HpnicfEponDeviceOrganizationSpecificEventEnabled_Type(TruthValue):
    """Custom type hpnicfEponDeviceOrganizationSpecificEventEnabled based on TruthValue"""


_HpnicfEponDeviceOrganizationSpecificEventEnabled_Object = MibTableColumn
hpnicfEponDeviceOrganizationSpecificEventEnabled = _HpnicfEponDeviceOrganizationSpecificEventEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 1, 1, 23),
    _HpnicfEponDeviceOrganizationSpecificEventEnabled_Type()
)
hpnicfEponDeviceOrganizationSpecificEventEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponDeviceOrganizationSpecificEventEnabled.setStatus("current")


class _HpnicfEponDeviceEventControl_Type(Integer32):
    """Custom type hpnicfEponDeviceEventControl based on Integer32"""
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
        *(("none", 1),
          ("resetLog", 2),
          ("useDefaultReporting", 3))
    )


_HpnicfEponDeviceEventControl_Type.__name__ = "Integer32"
_HpnicfEponDeviceEventControl_Object = MibTableColumn
hpnicfEponDeviceEventControl = _HpnicfEponDeviceEventControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 1, 1, 24),
    _HpnicfEponDeviceEventControl_Type()
)
hpnicfEponDeviceEventControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponDeviceEventControl.setStatus("current")
_HpnicfEponDeviceEventsLogTable_Object = MibTable
hpnicfEponDeviceEventsLogTable = _HpnicfEponDeviceEventsLogTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hpnicfEponDeviceEventsLogTable.setStatus("current")
_HpnicfEponDeviceEventsLogEntry_Object = MibTableRow
hpnicfEponDeviceEventsLogEntry = _HpnicfEponDeviceEventsLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 2, 1)
)
hpnicfEponDeviceEventsLogEntry.setIndexNames(
    (0, "HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceEventsLogName"),
    (0, "HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceEventsLogIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEponDeviceEventsLogEntry.setStatus("current")


class _HpnicfEponDeviceEventsLogName_Type(SnmpAdminString):
    """Custom type hpnicfEponDeviceEventsLogName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfEponDeviceEventsLogName_Type.__name__ = "SnmpAdminString"
_HpnicfEponDeviceEventsLogName_Object = MibTableColumn
hpnicfEponDeviceEventsLogName = _HpnicfEponDeviceEventsLogName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 2, 1, 1),
    _HpnicfEponDeviceEventsLogName_Type()
)
hpnicfEponDeviceEventsLogName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEponDeviceEventsLogName.setStatus("current")


class _HpnicfEponDeviceEventsLogIndex_Type(Unsigned32):
    """Custom type hpnicfEponDeviceEventsLogIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfEponDeviceEventsLogIndex_Type.__name__ = "Unsigned32"
_HpnicfEponDeviceEventsLogIndex_Object = MibTableColumn
hpnicfEponDeviceEventsLogIndex = _HpnicfEponDeviceEventsLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 2, 1, 2),
    _HpnicfEponDeviceEventsLogIndex_Type()
)
hpnicfEponDeviceEventsLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEponDeviceEventsLogIndex.setStatus("current")


class _HpnicfEponDeviceEventsLogID_Type(ObjectIdentifier):
    """Custom type hpnicfEponDeviceEventsLogID based on ObjectIdentifier"""
    defaultValue = (0, 0)


_HpnicfEponDeviceEventsLogID_Object = MibTableColumn
hpnicfEponDeviceEventsLogID = _HpnicfEponDeviceEventsLogID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 2, 1, 3),
    _HpnicfEponDeviceEventsLogID_Type()
)
hpnicfEponDeviceEventsLogID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponDeviceEventsLogID.setStatus("current")
_HpnicfEponDeviceEventsLogFirstTime_Type = DateAndTime
_HpnicfEponDeviceEventsLogFirstTime_Object = MibTableColumn
hpnicfEponDeviceEventsLogFirstTime = _HpnicfEponDeviceEventsLogFirstTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 2, 1, 4),
    _HpnicfEponDeviceEventsLogFirstTime_Type()
)
hpnicfEponDeviceEventsLogFirstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceEventsLogFirstTime.setStatus("current")
_HpnicfEponDeviceEventsLogLastTime_Type = DateAndTime
_HpnicfEponDeviceEventsLogLastTime_Object = MibTableColumn
hpnicfEponDeviceEventsLogLastTime = _HpnicfEponDeviceEventsLogLastTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 2, 1, 5),
    _HpnicfEponDeviceEventsLogLastTime_Type()
)
hpnicfEponDeviceEventsLogLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceEventsLogLastTime.setStatus("current")
_HpnicfEponDeviceEventsLogCounts_Type = Counter32
_HpnicfEponDeviceEventsLogCounts_Object = MibTableColumn
hpnicfEponDeviceEventsLogCounts = _HpnicfEponDeviceEventsLogCounts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 2, 1, 6),
    _HpnicfEponDeviceEventsLogCounts_Type()
)
hpnicfEponDeviceEventsLogCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceEventsLogCounts.setStatus("current")


class _HpnicfEponDeviceEventsLogType_Type(Integer32):
    """Custom type hpnicfEponDeviceEventsLogType based on Integer32"""
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
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("hpnicfEponDeviceCriticalEventState", 2),
          ("hpnicfEponDeviceDyingGaspAlarmState", 1),
          ("hpnicfEponDeviceErroredFrameEventState", 8),
          ("hpnicfEponDeviceErroredFramePeriodEventState", 9),
          ("hpnicfEponDeviceErroredFrameSecondsSummaryEventState", 10),
          ("hpnicfEponDeviceErroredSymbolPeriodEventState", 7),
          ("hpnicfEponDeviceGlobalEventState", 6),
          ("hpnicfEponDeviceLocalLinkFaultAlarmState", 3),
          ("hpnicfEponDeviceOrganizationSpecificEventState", 11),
          ("hpnicfEponDevicePowerVoltageEventIndicationState", 5),
          ("hpnicfEponDeviceTemperatureEventIndicationState", 4))
    )


_HpnicfEponDeviceEventsLogType_Type.__name__ = "Integer32"
_HpnicfEponDeviceEventsLogType_Object = MibTableColumn
hpnicfEponDeviceEventsLogType = _HpnicfEponDeviceEventsLogType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 2, 1, 7),
    _HpnicfEponDeviceEventsLogType_Type()
)
hpnicfEponDeviceEventsLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponDeviceEventsLogType.setStatus("current")
_HpnicfEponDeviceEventsLogEntryStatus_Type = RowStatus
_HpnicfEponDeviceEventsLogEntryStatus_Object = MibTableColumn
hpnicfEponDeviceEventsLogEntryStatus = _HpnicfEponDeviceEventsLogEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 1, 3, 2, 1, 8),
    _HpnicfEponDeviceEventsLogEntryStatus_Type()
)
hpnicfEponDeviceEventsLogEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponDeviceEventsLogEntryStatus.setStatus("current")
_HpnicfEponDeviceConformance_ObjectIdentity = ObjectIdentity
hpnicfEponDeviceConformance = _HpnicfEponDeviceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 2)
)
_HpnicfEponDeviceGroups_ObjectIdentity = ObjectIdentity
hpnicfEponDeviceGroups = _HpnicfEponDeviceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 2, 1)
)
_HpnicfEponDeviceCompliances_ObjectIdentity = ObjectIdentity
hpnicfEponDeviceCompliances = _HpnicfEponDeviceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 2, 2)
)

# Managed Objects groups

hpnicfEponDeviceGroupControl = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 2, 1, 1)
)
hpnicfEponDeviceGroupControl.setObjects(
      *(("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceObjectReset"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceObjectModes"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceObjectFecEnabled"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceObjectOamMode"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceObjectDeviceReadyMode"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceObjectPowerDown"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceObjectNumberOfLLIDs"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceObjectReportThreshold"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceRemoteMACAddressLLIDControl"))
)
if mibBuilder.loadTexts:
    hpnicfEponDeviceGroupControl.setStatus("current")

hpnicfEponDeviceGroupRMadLTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 2, 1, 2)
)
hpnicfEponDeviceGroupRMadLTable.setObjects(
      *(("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceRMadlLLID"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceRMadlLogID"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceRMadlRemoteAddress"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceRMadlType"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceRMadlAction"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceRMadlEntryStatus"))
)
if mibBuilder.loadTexts:
    hpnicfEponDeviceGroupRMadLTable.setStatus("current")

hpnicfEponDeviceGroupStat = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 2, 1, 3)
)
hpnicfEponDeviceGroupStat.setObjects(
      *(("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceStatTxFramesQueue0"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceStatTxFramesQueue1"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceStatTxFramesQueue2"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceStatTxFramesQueue3"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceStatTxFramesQueue4"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceStatTxFramesQueue5"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceStatTxFramesQueue6"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceStatTxFramesQueue7"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceStatRxFramesQueue0"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceStatRxFramesQueue1"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceStatRxFramesQueue2"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceStatRxFramesQueue3"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceStatRxFramesQueue4"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceStatRxFramesQueue5"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceStatRxFramesQueue6"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceStatRxFramesQueue7"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceStatDroppedFramesQueue0"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceStatDroppedFramesQueue1"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceStatDroppedFramesQueue2"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceStatDroppedFramesQueue3"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceStatDroppedFramesQueue4"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceStatDroppedFramesQueue5"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceStatDroppedFramesQueue6"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceStatDroppedFramesQueue7"))
)
if mibBuilder.loadTexts:
    hpnicfEponDeviceGroupStat.setStatus("current")

hpnicfEponDeviceGroupEvent = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 2, 1, 4)
)
hpnicfEponDeviceGroupEvent.setObjects(
      *(("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceSampleMinimum"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceDyingGaspAlarmState"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceDyingGaspAlarmEnabled"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceCriticalEventState"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceCriticalEventEnabled"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceLocalLinkFaultAlarmState"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceLocalLinkFaultAlarmEnabled"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceTemperatureEventIndicationState"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceTemperatureEventIndicationEnabled"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDevicePowerVoltageEventIndicationState"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDevicePowerVoltageEventIndicationEnabled"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceGlobalEventState"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceGlobalEventEnabled"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceErroredSymbolPeriodEventState"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceErroredSymbolPeriodEventEnabled"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceErroredFrameEventState"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceErroredFrameEventEnabled"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceErroredFramePeriodEventState"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceErroredFramePeriodEventEnabled"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceErroredFrameSecondsSummaryEventState"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceErroredFrameSecondsSummaryEventEnabled"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceOrganizationSpecificEventState"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceOrganizationSpecificEventEnabled"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceEventControl"))
)
if mibBuilder.loadTexts:
    hpnicfEponDeviceGroupEvent.setStatus("current")

hpnicfEponDeviceGroupEventLog = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 2, 1, 5)
)
hpnicfEponDeviceGroupEventLog.setObjects(
      *(("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceEventsLogID"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceEventsLogFirstTime"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceEventsLogLastTime"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceEventsLogCounts"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceEventsLogType"),
        ("HPN-ICF-EPON-DEVICE-MIB", "hpnicfEponDeviceEventsLogEntryStatus"))
)
if mibBuilder.loadTexts:
    hpnicfEponDeviceGroupEventLog.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpnicfEponDeviceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 4, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfEponDeviceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-EPON-DEVICE-MIB",
    **{"hpnicfEponDeviceMIB": hpnicfEponDeviceMIB,
       "hpnicfEponDeviceObjectMIB": hpnicfEponDeviceObjectMIB,
       "hpnicfEponDeviceObjects": hpnicfEponDeviceObjects,
       "hpnicfEponDeviceControlObjects": hpnicfEponDeviceControlObjects,
       "hpnicfEponDeviceControlTable": hpnicfEponDeviceControlTable,
       "hpnicfEponDeviceControlEntry": hpnicfEponDeviceControlEntry,
       "hpnicfEponDeviceObjectReset": hpnicfEponDeviceObjectReset,
       "hpnicfEponDeviceObjectModes": hpnicfEponDeviceObjectModes,
       "hpnicfEponDeviceObjectFecEnabled": hpnicfEponDeviceObjectFecEnabled,
       "hpnicfEponDeviceObjectOamMode": hpnicfEponDeviceObjectOamMode,
       "hpnicfEponDeviceObjectDeviceReadyMode": hpnicfEponDeviceObjectDeviceReadyMode,
       "hpnicfEponDeviceObjectPowerDown": hpnicfEponDeviceObjectPowerDown,
       "hpnicfEponDeviceObjectNumberOfLLIDs": hpnicfEponDeviceObjectNumberOfLLIDs,
       "hpnicfEponDeviceObjectReportThreshold": hpnicfEponDeviceObjectReportThreshold,
       "hpnicfEponDeviceRemoteMACAddressLLIDControl": hpnicfEponDeviceRemoteMACAddressLLIDControl,
       "hpnicfEponDeviceRemoteMACAddressLLIDTable": hpnicfEponDeviceRemoteMACAddressLLIDTable,
       "hpnicfEponDeviceRemoteMACAddressLLIDEntry": hpnicfEponDeviceRemoteMACAddressLLIDEntry,
       "hpnicfEponDeviceRemoteMACAddressLLIDName": hpnicfEponDeviceRemoteMACAddressLLIDName,
       "hpnicfEponDeviceRMadlLLID": hpnicfEponDeviceRMadlLLID,
       "hpnicfEponDeviceRMadlLogID": hpnicfEponDeviceRMadlLogID,
       "hpnicfEponDeviceRMadlRemoteAddress": hpnicfEponDeviceRMadlRemoteAddress,
       "hpnicfEponDeviceRMadlType": hpnicfEponDeviceRMadlType,
       "hpnicfEponDeviceRMadlAction": hpnicfEponDeviceRMadlAction,
       "hpnicfEponDeviceRMadlEntryStatus": hpnicfEponDeviceRMadlEntryStatus,
       "hpnicfEponDeviceStatObjects": hpnicfEponDeviceStatObjects,
       "hpnicfEponDeviceStatTable": hpnicfEponDeviceStatTable,
       "hpnicfEponDeviceStatEntry": hpnicfEponDeviceStatEntry,
       "hpnicfEponDeviceStatTxFramesQueue0": hpnicfEponDeviceStatTxFramesQueue0,
       "hpnicfEponDeviceStatTxFramesQueue1": hpnicfEponDeviceStatTxFramesQueue1,
       "hpnicfEponDeviceStatTxFramesQueue2": hpnicfEponDeviceStatTxFramesQueue2,
       "hpnicfEponDeviceStatTxFramesQueue3": hpnicfEponDeviceStatTxFramesQueue3,
       "hpnicfEponDeviceStatTxFramesQueue4": hpnicfEponDeviceStatTxFramesQueue4,
       "hpnicfEponDeviceStatTxFramesQueue5": hpnicfEponDeviceStatTxFramesQueue5,
       "hpnicfEponDeviceStatTxFramesQueue6": hpnicfEponDeviceStatTxFramesQueue6,
       "hpnicfEponDeviceStatTxFramesQueue7": hpnicfEponDeviceStatTxFramesQueue7,
       "hpnicfEponDeviceStatRxFramesQueue0": hpnicfEponDeviceStatRxFramesQueue0,
       "hpnicfEponDeviceStatRxFramesQueue1": hpnicfEponDeviceStatRxFramesQueue1,
       "hpnicfEponDeviceStatRxFramesQueue2": hpnicfEponDeviceStatRxFramesQueue2,
       "hpnicfEponDeviceStatRxFramesQueue3": hpnicfEponDeviceStatRxFramesQueue3,
       "hpnicfEponDeviceStatRxFramesQueue4": hpnicfEponDeviceStatRxFramesQueue4,
       "hpnicfEponDeviceStatRxFramesQueue5": hpnicfEponDeviceStatRxFramesQueue5,
       "hpnicfEponDeviceStatRxFramesQueue6": hpnicfEponDeviceStatRxFramesQueue6,
       "hpnicfEponDeviceStatRxFramesQueue7": hpnicfEponDeviceStatRxFramesQueue7,
       "hpnicfEponDeviceStatDroppedFramesQueue0": hpnicfEponDeviceStatDroppedFramesQueue0,
       "hpnicfEponDeviceStatDroppedFramesQueue1": hpnicfEponDeviceStatDroppedFramesQueue1,
       "hpnicfEponDeviceStatDroppedFramesQueue2": hpnicfEponDeviceStatDroppedFramesQueue2,
       "hpnicfEponDeviceStatDroppedFramesQueue3": hpnicfEponDeviceStatDroppedFramesQueue3,
       "hpnicfEponDeviceStatDroppedFramesQueue4": hpnicfEponDeviceStatDroppedFramesQueue4,
       "hpnicfEponDeviceStatDroppedFramesQueue5": hpnicfEponDeviceStatDroppedFramesQueue5,
       "hpnicfEponDeviceStatDroppedFramesQueue6": hpnicfEponDeviceStatDroppedFramesQueue6,
       "hpnicfEponDeviceStatDroppedFramesQueue7": hpnicfEponDeviceStatDroppedFramesQueue7,
       "hpnicfEponDeviceEventObjects": hpnicfEponDeviceEventObjects,
       "hpnicfEponDeviceEventObjectTable": hpnicfEponDeviceEventObjectTable,
       "hpnicfEponDeviceEventObjectEntry": hpnicfEponDeviceEventObjectEntry,
       "hpnicfEponDeviceSampleMinimum": hpnicfEponDeviceSampleMinimum,
       "hpnicfEponDeviceDyingGaspAlarmState": hpnicfEponDeviceDyingGaspAlarmState,
       "hpnicfEponDeviceDyingGaspAlarmEnabled": hpnicfEponDeviceDyingGaspAlarmEnabled,
       "hpnicfEponDeviceCriticalEventState": hpnicfEponDeviceCriticalEventState,
       "hpnicfEponDeviceCriticalEventEnabled": hpnicfEponDeviceCriticalEventEnabled,
       "hpnicfEponDeviceLocalLinkFaultAlarmState": hpnicfEponDeviceLocalLinkFaultAlarmState,
       "hpnicfEponDeviceLocalLinkFaultAlarmEnabled": hpnicfEponDeviceLocalLinkFaultAlarmEnabled,
       "hpnicfEponDeviceTemperatureEventIndicationState": hpnicfEponDeviceTemperatureEventIndicationState,
       "hpnicfEponDeviceTemperatureEventIndicationEnabled": hpnicfEponDeviceTemperatureEventIndicationEnabled,
       "hpnicfEponDevicePowerVoltageEventIndicationState": hpnicfEponDevicePowerVoltageEventIndicationState,
       "hpnicfEponDevicePowerVoltageEventIndicationEnabled": hpnicfEponDevicePowerVoltageEventIndicationEnabled,
       "hpnicfEponDeviceGlobalEventState": hpnicfEponDeviceGlobalEventState,
       "hpnicfEponDeviceGlobalEventEnabled": hpnicfEponDeviceGlobalEventEnabled,
       "hpnicfEponDeviceErroredSymbolPeriodEventState": hpnicfEponDeviceErroredSymbolPeriodEventState,
       "hpnicfEponDeviceErroredSymbolPeriodEventEnabled": hpnicfEponDeviceErroredSymbolPeriodEventEnabled,
       "hpnicfEponDeviceErroredFrameEventState": hpnicfEponDeviceErroredFrameEventState,
       "hpnicfEponDeviceErroredFrameEventEnabled": hpnicfEponDeviceErroredFrameEventEnabled,
       "hpnicfEponDeviceErroredFramePeriodEventState": hpnicfEponDeviceErroredFramePeriodEventState,
       "hpnicfEponDeviceErroredFramePeriodEventEnabled": hpnicfEponDeviceErroredFramePeriodEventEnabled,
       "hpnicfEponDeviceErroredFrameSecondsSummaryEventState": hpnicfEponDeviceErroredFrameSecondsSummaryEventState,
       "hpnicfEponDeviceErroredFrameSecondsSummaryEventEnabled": hpnicfEponDeviceErroredFrameSecondsSummaryEventEnabled,
       "hpnicfEponDeviceOrganizationSpecificEventState": hpnicfEponDeviceOrganizationSpecificEventState,
       "hpnicfEponDeviceOrganizationSpecificEventEnabled": hpnicfEponDeviceOrganizationSpecificEventEnabled,
       "hpnicfEponDeviceEventControl": hpnicfEponDeviceEventControl,
       "hpnicfEponDeviceEventsLogTable": hpnicfEponDeviceEventsLogTable,
       "hpnicfEponDeviceEventsLogEntry": hpnicfEponDeviceEventsLogEntry,
       "hpnicfEponDeviceEventsLogName": hpnicfEponDeviceEventsLogName,
       "hpnicfEponDeviceEventsLogIndex": hpnicfEponDeviceEventsLogIndex,
       "hpnicfEponDeviceEventsLogID": hpnicfEponDeviceEventsLogID,
       "hpnicfEponDeviceEventsLogFirstTime": hpnicfEponDeviceEventsLogFirstTime,
       "hpnicfEponDeviceEventsLogLastTime": hpnicfEponDeviceEventsLogLastTime,
       "hpnicfEponDeviceEventsLogCounts": hpnicfEponDeviceEventsLogCounts,
       "hpnicfEponDeviceEventsLogType": hpnicfEponDeviceEventsLogType,
       "hpnicfEponDeviceEventsLogEntryStatus": hpnicfEponDeviceEventsLogEntryStatus,
       "hpnicfEponDeviceConformance": hpnicfEponDeviceConformance,
       "hpnicfEponDeviceGroups": hpnicfEponDeviceGroups,
       "hpnicfEponDeviceGroupControl": hpnicfEponDeviceGroupControl,
       "hpnicfEponDeviceGroupRMadLTable": hpnicfEponDeviceGroupRMadLTable,
       "hpnicfEponDeviceGroupStat": hpnicfEponDeviceGroupStat,
       "hpnicfEponDeviceGroupEvent": hpnicfEponDeviceGroupEvent,
       "hpnicfEponDeviceGroupEventLog": hpnicfEponDeviceGroupEventLog,
       "hpnicfEponDeviceCompliances": hpnicfEponDeviceCompliances,
       "hpnicfEponDeviceCompliance": hpnicfEponDeviceCompliance}
)
