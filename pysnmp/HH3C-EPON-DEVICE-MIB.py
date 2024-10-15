# SNMP MIB module (HH3C-EPON-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-EPON-DEVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:08 2024
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

(hh3cEpon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cEpon")

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

hh3cEponDeviceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4)
)
hh3cEponDeviceMIB.setRevisions(
        ("2004-09-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cEponDeviceObjectMIB_ObjectIdentity = ObjectIdentity
hh3cEponDeviceObjectMIB = _Hh3cEponDeviceObjectMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1)
)
_Hh3cEponDeviceObjects_ObjectIdentity = ObjectIdentity
hh3cEponDeviceObjects = _Hh3cEponDeviceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1)
)
_Hh3cEponDeviceControlObjects_ObjectIdentity = ObjectIdentity
hh3cEponDeviceControlObjects = _Hh3cEponDeviceControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 1)
)
_Hh3cEponDeviceControlTable_Object = MibTable
hh3cEponDeviceControlTable = _Hh3cEponDeviceControlTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cEponDeviceControlTable.setStatus("current")
_Hh3cEponDeviceControlEntry_Object = MibTableRow
hh3cEponDeviceControlEntry = _Hh3cEponDeviceControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 1, 1, 1)
)
hh3cEponDeviceControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponDeviceControlEntry.setStatus("current")


class _Hh3cEponDeviceObjectReset_Type(Integer32):
    """Custom type hh3cEponDeviceObjectReset based on Integer32"""
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


_Hh3cEponDeviceObjectReset_Type.__name__ = "Integer32"
_Hh3cEponDeviceObjectReset_Object = MibTableColumn
hh3cEponDeviceObjectReset = _Hh3cEponDeviceObjectReset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 1, 1, 1, 1),
    _Hh3cEponDeviceObjectReset_Type()
)
hh3cEponDeviceObjectReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponDeviceObjectReset.setStatus("current")


class _Hh3cEponDeviceObjectModes_Type(Integer32):
    """Custom type hh3cEponDeviceObjectModes based on Integer32"""
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


_Hh3cEponDeviceObjectModes_Type.__name__ = "Integer32"
_Hh3cEponDeviceObjectModes_Object = MibTableColumn
hh3cEponDeviceObjectModes = _Hh3cEponDeviceObjectModes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 1, 1, 1, 2),
    _Hh3cEponDeviceObjectModes_Type()
)
hh3cEponDeviceObjectModes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceObjectModes.setStatus("current")


class _Hh3cEponDeviceObjectFecEnabled_Type(Integer32):
    """Custom type hh3cEponDeviceObjectFecEnabled based on Integer32"""
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


_Hh3cEponDeviceObjectFecEnabled_Type.__name__ = "Integer32"
_Hh3cEponDeviceObjectFecEnabled_Object = MibTableColumn
hh3cEponDeviceObjectFecEnabled = _Hh3cEponDeviceObjectFecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 1, 1, 1, 4),
    _Hh3cEponDeviceObjectFecEnabled_Type()
)
hh3cEponDeviceObjectFecEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponDeviceObjectFecEnabled.setStatus("current")


class _Hh3cEponDeviceObjectOamMode_Type(Integer32):
    """Custom type hh3cEponDeviceObjectOamMode based on Integer32"""
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


_Hh3cEponDeviceObjectOamMode_Type.__name__ = "Integer32"
_Hh3cEponDeviceObjectOamMode_Object = MibTableColumn
hh3cEponDeviceObjectOamMode = _Hh3cEponDeviceObjectOamMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 1, 1, 1, 5),
    _Hh3cEponDeviceObjectOamMode_Type()
)
hh3cEponDeviceObjectOamMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponDeviceObjectOamMode.setStatus("current")


class _Hh3cEponDeviceObjectDeviceReadyMode_Type(Integer32):
    """Custom type hh3cEponDeviceObjectDeviceReadyMode based on Integer32"""
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


_Hh3cEponDeviceObjectDeviceReadyMode_Type.__name__ = "Integer32"
_Hh3cEponDeviceObjectDeviceReadyMode_Object = MibTableColumn
hh3cEponDeviceObjectDeviceReadyMode = _Hh3cEponDeviceObjectDeviceReadyMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 1, 1, 1, 6),
    _Hh3cEponDeviceObjectDeviceReadyMode_Type()
)
hh3cEponDeviceObjectDeviceReadyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponDeviceObjectDeviceReadyMode.setStatus("current")


class _Hh3cEponDeviceObjectPowerDown_Type(TruthValue):
    """Custom type hh3cEponDeviceObjectPowerDown based on TruthValue"""


_Hh3cEponDeviceObjectPowerDown_Object = MibTableColumn
hh3cEponDeviceObjectPowerDown = _Hh3cEponDeviceObjectPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 1, 1, 1, 7),
    _Hh3cEponDeviceObjectPowerDown_Type()
)
hh3cEponDeviceObjectPowerDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponDeviceObjectPowerDown.setStatus("current")
_Hh3cEponDeviceObjectNumberOfLLIDs_Type = Integer32
_Hh3cEponDeviceObjectNumberOfLLIDs_Object = MibTableColumn
hh3cEponDeviceObjectNumberOfLLIDs = _Hh3cEponDeviceObjectNumberOfLLIDs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 1, 1, 1, 8),
    _Hh3cEponDeviceObjectNumberOfLLIDs_Type()
)
hh3cEponDeviceObjectNumberOfLLIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceObjectNumberOfLLIDs.setStatus("current")


class _Hh3cEponDeviceObjectReportThreshold_Type(Integer32):
    """Custom type hh3cEponDeviceObjectReportThreshold based on Integer32"""
    defaultValue = 0


_Hh3cEponDeviceObjectReportThreshold_Object = MibTableColumn
hh3cEponDeviceObjectReportThreshold = _Hh3cEponDeviceObjectReportThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 1, 1, 1, 9),
    _Hh3cEponDeviceObjectReportThreshold_Type()
)
hh3cEponDeviceObjectReportThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponDeviceObjectReportThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEponDeviceObjectReportThreshold.setUnits("TQ (16nsec)")


class _Hh3cEponDeviceRemoteMACAddressLLIDControl_Type(Integer32):
    """Custom type hh3cEponDeviceRemoteMACAddressLLIDControl based on Integer32"""
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


_Hh3cEponDeviceRemoteMACAddressLLIDControl_Type.__name__ = "Integer32"
_Hh3cEponDeviceRemoteMACAddressLLIDControl_Object = MibTableColumn
hh3cEponDeviceRemoteMACAddressLLIDControl = _Hh3cEponDeviceRemoteMACAddressLLIDControl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 1, 1, 1, 10),
    _Hh3cEponDeviceRemoteMACAddressLLIDControl_Type()
)
hh3cEponDeviceRemoteMACAddressLLIDControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponDeviceRemoteMACAddressLLIDControl.setStatus("current")
_Hh3cEponDeviceRemoteMACAddressLLIDTable_Object = MibTable
hh3cEponDeviceRemoteMACAddressLLIDTable = _Hh3cEponDeviceRemoteMACAddressLLIDTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cEponDeviceRemoteMACAddressLLIDTable.setStatus("current")
_Hh3cEponDeviceRemoteMACAddressLLIDEntry_Object = MibTableRow
hh3cEponDeviceRemoteMACAddressLLIDEntry = _Hh3cEponDeviceRemoteMACAddressLLIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 1, 2, 1)
)
hh3cEponDeviceRemoteMACAddressLLIDEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponDeviceRemoteMACAddressLLIDEntry.setStatus("current")


class _Hh3cEponDeviceRemoteMACAddressLLIDName_Type(SnmpAdminString):
    """Custom type hh3cEponDeviceRemoteMACAddressLLIDName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cEponDeviceRemoteMACAddressLLIDName_Type.__name__ = "SnmpAdminString"
_Hh3cEponDeviceRemoteMACAddressLLIDName_Object = MibTableColumn
hh3cEponDeviceRemoteMACAddressLLIDName = _Hh3cEponDeviceRemoteMACAddressLLIDName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 1, 2, 1, 1),
    _Hh3cEponDeviceRemoteMACAddressLLIDName_Type()
)
hh3cEponDeviceRemoteMACAddressLLIDName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponDeviceRemoteMACAddressLLIDName.setStatus("current")


class _Hh3cEponDeviceRMadlLLID_Type(Unsigned32):
    """Custom type hh3cEponDeviceRMadlLLID based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cEponDeviceRMadlLLID_Type.__name__ = "Unsigned32"
_Hh3cEponDeviceRMadlLLID_Object = MibTableColumn
hh3cEponDeviceRMadlLLID = _Hh3cEponDeviceRMadlLLID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 1, 2, 1, 2),
    _Hh3cEponDeviceRMadlLLID_Type()
)
hh3cEponDeviceRMadlLLID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponDeviceRMadlLLID.setStatus("current")


class _Hh3cEponDeviceRMadlLogID_Type(ObjectIdentifier):
    """Custom type hh3cEponDeviceRMadlLogID based on ObjectIdentifier"""
    defaultValue = (0, 0)


_Hh3cEponDeviceRMadlLogID_Object = MibTableColumn
hh3cEponDeviceRMadlLogID = _Hh3cEponDeviceRMadlLogID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 1, 2, 1, 3),
    _Hh3cEponDeviceRMadlLogID_Type()
)
hh3cEponDeviceRMadlLogID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponDeviceRMadlLogID.setStatus("current")
_Hh3cEponDeviceRMadlRemoteAddress_Type = MacAddress
_Hh3cEponDeviceRMadlRemoteAddress_Object = MibTableColumn
hh3cEponDeviceRMadlRemoteAddress = _Hh3cEponDeviceRMadlRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 1, 2, 1, 4),
    _Hh3cEponDeviceRMadlRemoteAddress_Type()
)
hh3cEponDeviceRMadlRemoteAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponDeviceRMadlRemoteAddress.setStatus("current")


class _Hh3cEponDeviceRMadlType_Type(Integer32):
    """Custom type hh3cEponDeviceRMadlType based on Integer32"""
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


_Hh3cEponDeviceRMadlType_Type.__name__ = "Integer32"
_Hh3cEponDeviceRMadlType_Object = MibTableColumn
hh3cEponDeviceRMadlType = _Hh3cEponDeviceRMadlType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 1, 2, 1, 5),
    _Hh3cEponDeviceRMadlType_Type()
)
hh3cEponDeviceRMadlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponDeviceRMadlType.setStatus("current")


class _Hh3cEponDeviceRMadlAction_Type(Integer32):
    """Custom type hh3cEponDeviceRMadlAction based on Integer32"""
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


_Hh3cEponDeviceRMadlAction_Type.__name__ = "Integer32"
_Hh3cEponDeviceRMadlAction_Object = MibTableColumn
hh3cEponDeviceRMadlAction = _Hh3cEponDeviceRMadlAction_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 1, 2, 1, 6),
    _Hh3cEponDeviceRMadlAction_Type()
)
hh3cEponDeviceRMadlAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponDeviceRMadlAction.setStatus("current")
_Hh3cEponDeviceRMadlEntryStatus_Type = RowStatus
_Hh3cEponDeviceRMadlEntryStatus_Object = MibTableColumn
hh3cEponDeviceRMadlEntryStatus = _Hh3cEponDeviceRMadlEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 1, 2, 1, 7),
    _Hh3cEponDeviceRMadlEntryStatus_Type()
)
hh3cEponDeviceRMadlEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponDeviceRMadlEntryStatus.setStatus("current")
_Hh3cEponDeviceStatObjects_ObjectIdentity = ObjectIdentity
hh3cEponDeviceStatObjects = _Hh3cEponDeviceStatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 2)
)
_Hh3cEponDeviceStatTable_Object = MibTable
hh3cEponDeviceStatTable = _Hh3cEponDeviceStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cEponDeviceStatTable.setStatus("current")
_Hh3cEponDeviceStatEntry_Object = MibTableRow
hh3cEponDeviceStatEntry = _Hh3cEponDeviceStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 2, 1, 1)
)
hh3cEponDeviceStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponDeviceStatEntry.setStatus("current")
_Hh3cEponDeviceStatTxFramesQueue0_Type = Counter32
_Hh3cEponDeviceStatTxFramesQueue0_Object = MibTableColumn
hh3cEponDeviceStatTxFramesQueue0 = _Hh3cEponDeviceStatTxFramesQueue0_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 2, 1, 1, 1),
    _Hh3cEponDeviceStatTxFramesQueue0_Type()
)
hh3cEponDeviceStatTxFramesQueue0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatTxFramesQueue0.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatTxFramesQueue0.setUnits("frames")
_Hh3cEponDeviceStatTxFramesQueue1_Type = Counter32
_Hh3cEponDeviceStatTxFramesQueue1_Object = MibTableColumn
hh3cEponDeviceStatTxFramesQueue1 = _Hh3cEponDeviceStatTxFramesQueue1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 2, 1, 1, 2),
    _Hh3cEponDeviceStatTxFramesQueue1_Type()
)
hh3cEponDeviceStatTxFramesQueue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatTxFramesQueue1.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatTxFramesQueue1.setUnits("frames")
_Hh3cEponDeviceStatTxFramesQueue2_Type = Counter32
_Hh3cEponDeviceStatTxFramesQueue2_Object = MibTableColumn
hh3cEponDeviceStatTxFramesQueue2 = _Hh3cEponDeviceStatTxFramesQueue2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 2, 1, 1, 3),
    _Hh3cEponDeviceStatTxFramesQueue2_Type()
)
hh3cEponDeviceStatTxFramesQueue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatTxFramesQueue2.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatTxFramesQueue2.setUnits("frames")
_Hh3cEponDeviceStatTxFramesQueue3_Type = Counter32
_Hh3cEponDeviceStatTxFramesQueue3_Object = MibTableColumn
hh3cEponDeviceStatTxFramesQueue3 = _Hh3cEponDeviceStatTxFramesQueue3_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 2, 1, 1, 4),
    _Hh3cEponDeviceStatTxFramesQueue3_Type()
)
hh3cEponDeviceStatTxFramesQueue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatTxFramesQueue3.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatTxFramesQueue3.setUnits("frames")
_Hh3cEponDeviceStatTxFramesQueue4_Type = Counter32
_Hh3cEponDeviceStatTxFramesQueue4_Object = MibTableColumn
hh3cEponDeviceStatTxFramesQueue4 = _Hh3cEponDeviceStatTxFramesQueue4_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 2, 1, 1, 5),
    _Hh3cEponDeviceStatTxFramesQueue4_Type()
)
hh3cEponDeviceStatTxFramesQueue4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatTxFramesQueue4.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatTxFramesQueue4.setUnits("frames")
_Hh3cEponDeviceStatTxFramesQueue5_Type = Counter32
_Hh3cEponDeviceStatTxFramesQueue5_Object = MibTableColumn
hh3cEponDeviceStatTxFramesQueue5 = _Hh3cEponDeviceStatTxFramesQueue5_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 2, 1, 1, 6),
    _Hh3cEponDeviceStatTxFramesQueue5_Type()
)
hh3cEponDeviceStatTxFramesQueue5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatTxFramesQueue5.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatTxFramesQueue5.setUnits("frames")
_Hh3cEponDeviceStatTxFramesQueue6_Type = Counter32
_Hh3cEponDeviceStatTxFramesQueue6_Object = MibTableColumn
hh3cEponDeviceStatTxFramesQueue6 = _Hh3cEponDeviceStatTxFramesQueue6_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 2, 1, 1, 7),
    _Hh3cEponDeviceStatTxFramesQueue6_Type()
)
hh3cEponDeviceStatTxFramesQueue6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatTxFramesQueue6.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatTxFramesQueue6.setUnits("frames")
_Hh3cEponDeviceStatTxFramesQueue7_Type = Counter32
_Hh3cEponDeviceStatTxFramesQueue7_Object = MibTableColumn
hh3cEponDeviceStatTxFramesQueue7 = _Hh3cEponDeviceStatTxFramesQueue7_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 2, 1, 1, 8),
    _Hh3cEponDeviceStatTxFramesQueue7_Type()
)
hh3cEponDeviceStatTxFramesQueue7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatTxFramesQueue7.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatTxFramesQueue7.setUnits("frames")
_Hh3cEponDeviceStatRxFramesQueue0_Type = Counter32
_Hh3cEponDeviceStatRxFramesQueue0_Object = MibTableColumn
hh3cEponDeviceStatRxFramesQueue0 = _Hh3cEponDeviceStatRxFramesQueue0_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 2, 1, 1, 9),
    _Hh3cEponDeviceStatRxFramesQueue0_Type()
)
hh3cEponDeviceStatRxFramesQueue0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatRxFramesQueue0.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatRxFramesQueue0.setUnits("frames")
_Hh3cEponDeviceStatRxFramesQueue1_Type = Counter32
_Hh3cEponDeviceStatRxFramesQueue1_Object = MibTableColumn
hh3cEponDeviceStatRxFramesQueue1 = _Hh3cEponDeviceStatRxFramesQueue1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 2, 1, 1, 10),
    _Hh3cEponDeviceStatRxFramesQueue1_Type()
)
hh3cEponDeviceStatRxFramesQueue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatRxFramesQueue1.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatRxFramesQueue1.setUnits("frames")
_Hh3cEponDeviceStatRxFramesQueue2_Type = Counter32
_Hh3cEponDeviceStatRxFramesQueue2_Object = MibTableColumn
hh3cEponDeviceStatRxFramesQueue2 = _Hh3cEponDeviceStatRxFramesQueue2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 2, 1, 1, 11),
    _Hh3cEponDeviceStatRxFramesQueue2_Type()
)
hh3cEponDeviceStatRxFramesQueue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatRxFramesQueue2.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatRxFramesQueue2.setUnits("frames")
_Hh3cEponDeviceStatRxFramesQueue3_Type = Counter32
_Hh3cEponDeviceStatRxFramesQueue3_Object = MibTableColumn
hh3cEponDeviceStatRxFramesQueue3 = _Hh3cEponDeviceStatRxFramesQueue3_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 2, 1, 1, 12),
    _Hh3cEponDeviceStatRxFramesQueue3_Type()
)
hh3cEponDeviceStatRxFramesQueue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatRxFramesQueue3.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatRxFramesQueue3.setUnits("frames")
_Hh3cEponDeviceStatRxFramesQueue4_Type = Counter32
_Hh3cEponDeviceStatRxFramesQueue4_Object = MibTableColumn
hh3cEponDeviceStatRxFramesQueue4 = _Hh3cEponDeviceStatRxFramesQueue4_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 2, 1, 1, 13),
    _Hh3cEponDeviceStatRxFramesQueue4_Type()
)
hh3cEponDeviceStatRxFramesQueue4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatRxFramesQueue4.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatRxFramesQueue4.setUnits("frames")
_Hh3cEponDeviceStatRxFramesQueue5_Type = Counter32
_Hh3cEponDeviceStatRxFramesQueue5_Object = MibTableColumn
hh3cEponDeviceStatRxFramesQueue5 = _Hh3cEponDeviceStatRxFramesQueue5_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 2, 1, 1, 14),
    _Hh3cEponDeviceStatRxFramesQueue5_Type()
)
hh3cEponDeviceStatRxFramesQueue5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatRxFramesQueue5.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatRxFramesQueue5.setUnits("frames")
_Hh3cEponDeviceStatRxFramesQueue6_Type = Counter32
_Hh3cEponDeviceStatRxFramesQueue6_Object = MibTableColumn
hh3cEponDeviceStatRxFramesQueue6 = _Hh3cEponDeviceStatRxFramesQueue6_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 2, 1, 1, 15),
    _Hh3cEponDeviceStatRxFramesQueue6_Type()
)
hh3cEponDeviceStatRxFramesQueue6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatRxFramesQueue6.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatRxFramesQueue6.setUnits("frames")
_Hh3cEponDeviceStatRxFramesQueue7_Type = Counter32
_Hh3cEponDeviceStatRxFramesQueue7_Object = MibTableColumn
hh3cEponDeviceStatRxFramesQueue7 = _Hh3cEponDeviceStatRxFramesQueue7_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 2, 1, 1, 16),
    _Hh3cEponDeviceStatRxFramesQueue7_Type()
)
hh3cEponDeviceStatRxFramesQueue7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatRxFramesQueue7.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatRxFramesQueue7.setUnits("frames")
_Hh3cEponDeviceStatDroppedFramesQueue0_Type = Counter32
_Hh3cEponDeviceStatDroppedFramesQueue0_Object = MibTableColumn
hh3cEponDeviceStatDroppedFramesQueue0 = _Hh3cEponDeviceStatDroppedFramesQueue0_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 2, 1, 1, 17),
    _Hh3cEponDeviceStatDroppedFramesQueue0_Type()
)
hh3cEponDeviceStatDroppedFramesQueue0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatDroppedFramesQueue0.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatDroppedFramesQueue0.setUnits("frames")
_Hh3cEponDeviceStatDroppedFramesQueue1_Type = Counter32
_Hh3cEponDeviceStatDroppedFramesQueue1_Object = MibTableColumn
hh3cEponDeviceStatDroppedFramesQueue1 = _Hh3cEponDeviceStatDroppedFramesQueue1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 2, 1, 1, 18),
    _Hh3cEponDeviceStatDroppedFramesQueue1_Type()
)
hh3cEponDeviceStatDroppedFramesQueue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatDroppedFramesQueue1.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatDroppedFramesQueue1.setUnits("frames")
_Hh3cEponDeviceStatDroppedFramesQueue2_Type = Counter32
_Hh3cEponDeviceStatDroppedFramesQueue2_Object = MibTableColumn
hh3cEponDeviceStatDroppedFramesQueue2 = _Hh3cEponDeviceStatDroppedFramesQueue2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 2, 1, 1, 19),
    _Hh3cEponDeviceStatDroppedFramesQueue2_Type()
)
hh3cEponDeviceStatDroppedFramesQueue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatDroppedFramesQueue2.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatDroppedFramesQueue2.setUnits("frames")
_Hh3cEponDeviceStatDroppedFramesQueue3_Type = Counter32
_Hh3cEponDeviceStatDroppedFramesQueue3_Object = MibTableColumn
hh3cEponDeviceStatDroppedFramesQueue3 = _Hh3cEponDeviceStatDroppedFramesQueue3_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 2, 1, 1, 20),
    _Hh3cEponDeviceStatDroppedFramesQueue3_Type()
)
hh3cEponDeviceStatDroppedFramesQueue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatDroppedFramesQueue3.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatDroppedFramesQueue3.setUnits("frames")
_Hh3cEponDeviceStatDroppedFramesQueue4_Type = Counter32
_Hh3cEponDeviceStatDroppedFramesQueue4_Object = MibTableColumn
hh3cEponDeviceStatDroppedFramesQueue4 = _Hh3cEponDeviceStatDroppedFramesQueue4_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 2, 1, 1, 21),
    _Hh3cEponDeviceStatDroppedFramesQueue4_Type()
)
hh3cEponDeviceStatDroppedFramesQueue4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatDroppedFramesQueue4.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatDroppedFramesQueue4.setUnits("frames")
_Hh3cEponDeviceStatDroppedFramesQueue5_Type = Counter32
_Hh3cEponDeviceStatDroppedFramesQueue5_Object = MibTableColumn
hh3cEponDeviceStatDroppedFramesQueue5 = _Hh3cEponDeviceStatDroppedFramesQueue5_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 2, 1, 1, 22),
    _Hh3cEponDeviceStatDroppedFramesQueue5_Type()
)
hh3cEponDeviceStatDroppedFramesQueue5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatDroppedFramesQueue5.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatDroppedFramesQueue5.setUnits("frames")
_Hh3cEponDeviceStatDroppedFramesQueue6_Type = Counter32
_Hh3cEponDeviceStatDroppedFramesQueue6_Object = MibTableColumn
hh3cEponDeviceStatDroppedFramesQueue6 = _Hh3cEponDeviceStatDroppedFramesQueue6_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 2, 1, 1, 23),
    _Hh3cEponDeviceStatDroppedFramesQueue6_Type()
)
hh3cEponDeviceStatDroppedFramesQueue6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatDroppedFramesQueue6.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatDroppedFramesQueue6.setUnits("frames")
_Hh3cEponDeviceStatDroppedFramesQueue7_Type = Counter32
_Hh3cEponDeviceStatDroppedFramesQueue7_Object = MibTableColumn
hh3cEponDeviceStatDroppedFramesQueue7 = _Hh3cEponDeviceStatDroppedFramesQueue7_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 2, 1, 1, 24),
    _Hh3cEponDeviceStatDroppedFramesQueue7_Type()
)
hh3cEponDeviceStatDroppedFramesQueue7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatDroppedFramesQueue7.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEponDeviceStatDroppedFramesQueue7.setUnits("frames")
_Hh3cEponDeviceEventObjects_ObjectIdentity = ObjectIdentity
hh3cEponDeviceEventObjects = _Hh3cEponDeviceEventObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3)
)
_Hh3cEponDeviceEventObjectTable_Object = MibTable
hh3cEponDeviceEventObjectTable = _Hh3cEponDeviceEventObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cEponDeviceEventObjectTable.setStatus("current")
_Hh3cEponDeviceEventObjectEntry_Object = MibTableRow
hh3cEponDeviceEventObjectEntry = _Hh3cEponDeviceEventObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 1, 1)
)
hh3cEponDeviceEventObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponDeviceEventObjectEntry.setStatus("current")


class _Hh3cEponDeviceSampleMinimum_Type(Integer32):
    """Custom type hh3cEponDeviceSampleMinimum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cEponDeviceSampleMinimum_Type.__name__ = "Integer32"
_Hh3cEponDeviceSampleMinimum_Object = MibTableColumn
hh3cEponDeviceSampleMinimum = _Hh3cEponDeviceSampleMinimum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 1, 1, 1),
    _Hh3cEponDeviceSampleMinimum_Type()
)
hh3cEponDeviceSampleMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponDeviceSampleMinimum.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEponDeviceSampleMinimum.setUnits("seconds")
_Hh3cEponDeviceDyingGaspAlarmState_Type = TruthValue
_Hh3cEponDeviceDyingGaspAlarmState_Object = MibTableColumn
hh3cEponDeviceDyingGaspAlarmState = _Hh3cEponDeviceDyingGaspAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 1, 1, 2),
    _Hh3cEponDeviceDyingGaspAlarmState_Type()
)
hh3cEponDeviceDyingGaspAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceDyingGaspAlarmState.setStatus("current")


class _Hh3cEponDeviceDyingGaspAlarmEnabled_Type(TruthValue):
    """Custom type hh3cEponDeviceDyingGaspAlarmEnabled based on TruthValue"""


_Hh3cEponDeviceDyingGaspAlarmEnabled_Object = MibTableColumn
hh3cEponDeviceDyingGaspAlarmEnabled = _Hh3cEponDeviceDyingGaspAlarmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 1, 1, 3),
    _Hh3cEponDeviceDyingGaspAlarmEnabled_Type()
)
hh3cEponDeviceDyingGaspAlarmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponDeviceDyingGaspAlarmEnabled.setStatus("current")
_Hh3cEponDeviceCriticalEventState_Type = TruthValue
_Hh3cEponDeviceCriticalEventState_Object = MibTableColumn
hh3cEponDeviceCriticalEventState = _Hh3cEponDeviceCriticalEventState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 1, 1, 4),
    _Hh3cEponDeviceCriticalEventState_Type()
)
hh3cEponDeviceCriticalEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceCriticalEventState.setStatus("current")


class _Hh3cEponDeviceCriticalEventEnabled_Type(TruthValue):
    """Custom type hh3cEponDeviceCriticalEventEnabled based on TruthValue"""


_Hh3cEponDeviceCriticalEventEnabled_Object = MibTableColumn
hh3cEponDeviceCriticalEventEnabled = _Hh3cEponDeviceCriticalEventEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 1, 1, 5),
    _Hh3cEponDeviceCriticalEventEnabled_Type()
)
hh3cEponDeviceCriticalEventEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponDeviceCriticalEventEnabled.setStatus("current")
_Hh3cEponDeviceLocalLinkFaultAlarmState_Type = TruthValue
_Hh3cEponDeviceLocalLinkFaultAlarmState_Object = MibTableColumn
hh3cEponDeviceLocalLinkFaultAlarmState = _Hh3cEponDeviceLocalLinkFaultAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 1, 1, 6),
    _Hh3cEponDeviceLocalLinkFaultAlarmState_Type()
)
hh3cEponDeviceLocalLinkFaultAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceLocalLinkFaultAlarmState.setStatus("current")


class _Hh3cEponDeviceLocalLinkFaultAlarmEnabled_Type(TruthValue):
    """Custom type hh3cEponDeviceLocalLinkFaultAlarmEnabled based on TruthValue"""


_Hh3cEponDeviceLocalLinkFaultAlarmEnabled_Object = MibTableColumn
hh3cEponDeviceLocalLinkFaultAlarmEnabled = _Hh3cEponDeviceLocalLinkFaultAlarmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 1, 1, 7),
    _Hh3cEponDeviceLocalLinkFaultAlarmEnabled_Type()
)
hh3cEponDeviceLocalLinkFaultAlarmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponDeviceLocalLinkFaultAlarmEnabled.setStatus("current")
_Hh3cEponDeviceTemperatureEventIndicationState_Type = TruthValue
_Hh3cEponDeviceTemperatureEventIndicationState_Object = MibTableColumn
hh3cEponDeviceTemperatureEventIndicationState = _Hh3cEponDeviceTemperatureEventIndicationState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 1, 1, 8),
    _Hh3cEponDeviceTemperatureEventIndicationState_Type()
)
hh3cEponDeviceTemperatureEventIndicationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceTemperatureEventIndicationState.setStatus("current")


class _Hh3cEponDeviceTemperatureEventIndicationEnabled_Type(TruthValue):
    """Custom type hh3cEponDeviceTemperatureEventIndicationEnabled based on TruthValue"""


_Hh3cEponDeviceTemperatureEventIndicationEnabled_Object = MibTableColumn
hh3cEponDeviceTemperatureEventIndicationEnabled = _Hh3cEponDeviceTemperatureEventIndicationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 1, 1, 9),
    _Hh3cEponDeviceTemperatureEventIndicationEnabled_Type()
)
hh3cEponDeviceTemperatureEventIndicationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponDeviceTemperatureEventIndicationEnabled.setStatus("current")
_Hh3cEponDevicePowerVoltageEventIndicationState_Type = TruthValue
_Hh3cEponDevicePowerVoltageEventIndicationState_Object = MibTableColumn
hh3cEponDevicePowerVoltageEventIndicationState = _Hh3cEponDevicePowerVoltageEventIndicationState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 1, 1, 10),
    _Hh3cEponDevicePowerVoltageEventIndicationState_Type()
)
hh3cEponDevicePowerVoltageEventIndicationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDevicePowerVoltageEventIndicationState.setStatus("current")


class _Hh3cEponDevicePowerVoltageEventIndicationEnabled_Type(TruthValue):
    """Custom type hh3cEponDevicePowerVoltageEventIndicationEnabled based on TruthValue"""


_Hh3cEponDevicePowerVoltageEventIndicationEnabled_Object = MibTableColumn
hh3cEponDevicePowerVoltageEventIndicationEnabled = _Hh3cEponDevicePowerVoltageEventIndicationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 1, 1, 11),
    _Hh3cEponDevicePowerVoltageEventIndicationEnabled_Type()
)
hh3cEponDevicePowerVoltageEventIndicationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponDevicePowerVoltageEventIndicationEnabled.setStatus("current")
_Hh3cEponDeviceGlobalEventState_Type = TruthValue
_Hh3cEponDeviceGlobalEventState_Object = MibTableColumn
hh3cEponDeviceGlobalEventState = _Hh3cEponDeviceGlobalEventState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 1, 1, 12),
    _Hh3cEponDeviceGlobalEventState_Type()
)
hh3cEponDeviceGlobalEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceGlobalEventState.setStatus("current")


class _Hh3cEponDeviceGlobalEventEnabled_Type(TruthValue):
    """Custom type hh3cEponDeviceGlobalEventEnabled based on TruthValue"""


_Hh3cEponDeviceGlobalEventEnabled_Object = MibTableColumn
hh3cEponDeviceGlobalEventEnabled = _Hh3cEponDeviceGlobalEventEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 1, 1, 13),
    _Hh3cEponDeviceGlobalEventEnabled_Type()
)
hh3cEponDeviceGlobalEventEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponDeviceGlobalEventEnabled.setStatus("current")
_Hh3cEponDeviceErroredSymbolPeriodEventState_Type = TruthValue
_Hh3cEponDeviceErroredSymbolPeriodEventState_Object = MibTableColumn
hh3cEponDeviceErroredSymbolPeriodEventState = _Hh3cEponDeviceErroredSymbolPeriodEventState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 1, 1, 14),
    _Hh3cEponDeviceErroredSymbolPeriodEventState_Type()
)
hh3cEponDeviceErroredSymbolPeriodEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceErroredSymbolPeriodEventState.setStatus("current")


class _Hh3cEponDeviceErroredSymbolPeriodEventEnabled_Type(TruthValue):
    """Custom type hh3cEponDeviceErroredSymbolPeriodEventEnabled based on TruthValue"""


_Hh3cEponDeviceErroredSymbolPeriodEventEnabled_Object = MibTableColumn
hh3cEponDeviceErroredSymbolPeriodEventEnabled = _Hh3cEponDeviceErroredSymbolPeriodEventEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 1, 1, 15),
    _Hh3cEponDeviceErroredSymbolPeriodEventEnabled_Type()
)
hh3cEponDeviceErroredSymbolPeriodEventEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponDeviceErroredSymbolPeriodEventEnabled.setStatus("current")
_Hh3cEponDeviceErroredFrameEventState_Type = TruthValue
_Hh3cEponDeviceErroredFrameEventState_Object = MibTableColumn
hh3cEponDeviceErroredFrameEventState = _Hh3cEponDeviceErroredFrameEventState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 1, 1, 16),
    _Hh3cEponDeviceErroredFrameEventState_Type()
)
hh3cEponDeviceErroredFrameEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceErroredFrameEventState.setStatus("current")


class _Hh3cEponDeviceErroredFrameEventEnabled_Type(TruthValue):
    """Custom type hh3cEponDeviceErroredFrameEventEnabled based on TruthValue"""


_Hh3cEponDeviceErroredFrameEventEnabled_Object = MibTableColumn
hh3cEponDeviceErroredFrameEventEnabled = _Hh3cEponDeviceErroredFrameEventEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 1, 1, 17),
    _Hh3cEponDeviceErroredFrameEventEnabled_Type()
)
hh3cEponDeviceErroredFrameEventEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponDeviceErroredFrameEventEnabled.setStatus("current")
_Hh3cEponDeviceErroredFramePeriodEventState_Type = TruthValue
_Hh3cEponDeviceErroredFramePeriodEventState_Object = MibTableColumn
hh3cEponDeviceErroredFramePeriodEventState = _Hh3cEponDeviceErroredFramePeriodEventState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 1, 1, 18),
    _Hh3cEponDeviceErroredFramePeriodEventState_Type()
)
hh3cEponDeviceErroredFramePeriodEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceErroredFramePeriodEventState.setStatus("current")


class _Hh3cEponDeviceErroredFramePeriodEventEnabled_Type(TruthValue):
    """Custom type hh3cEponDeviceErroredFramePeriodEventEnabled based on TruthValue"""


_Hh3cEponDeviceErroredFramePeriodEventEnabled_Object = MibTableColumn
hh3cEponDeviceErroredFramePeriodEventEnabled = _Hh3cEponDeviceErroredFramePeriodEventEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 1, 1, 19),
    _Hh3cEponDeviceErroredFramePeriodEventEnabled_Type()
)
hh3cEponDeviceErroredFramePeriodEventEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponDeviceErroredFramePeriodEventEnabled.setStatus("current")
_Hh3cEponDeviceErroredFrameSecondsSummaryEventState_Type = TruthValue
_Hh3cEponDeviceErroredFrameSecondsSummaryEventState_Object = MibTableColumn
hh3cEponDeviceErroredFrameSecondsSummaryEventState = _Hh3cEponDeviceErroredFrameSecondsSummaryEventState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 1, 1, 20),
    _Hh3cEponDeviceErroredFrameSecondsSummaryEventState_Type()
)
hh3cEponDeviceErroredFrameSecondsSummaryEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceErroredFrameSecondsSummaryEventState.setStatus("current")


class _Hh3cEponDeviceErroredFrameSecondsSummaryEventEnabled_Type(TruthValue):
    """Custom type hh3cEponDeviceErroredFrameSecondsSummaryEventEnabled based on TruthValue"""


_Hh3cEponDeviceErroredFrameSecondsSummaryEventEnabled_Object = MibTableColumn
hh3cEponDeviceErroredFrameSecondsSummaryEventEnabled = _Hh3cEponDeviceErroredFrameSecondsSummaryEventEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 1, 1, 21),
    _Hh3cEponDeviceErroredFrameSecondsSummaryEventEnabled_Type()
)
hh3cEponDeviceErroredFrameSecondsSummaryEventEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponDeviceErroredFrameSecondsSummaryEventEnabled.setStatus("current")
_Hh3cEponDeviceOrganizationSpecificEventState_Type = TruthValue
_Hh3cEponDeviceOrganizationSpecificEventState_Object = MibTableColumn
hh3cEponDeviceOrganizationSpecificEventState = _Hh3cEponDeviceOrganizationSpecificEventState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 1, 1, 22),
    _Hh3cEponDeviceOrganizationSpecificEventState_Type()
)
hh3cEponDeviceOrganizationSpecificEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceOrganizationSpecificEventState.setStatus("current")


class _Hh3cEponDeviceOrganizationSpecificEventEnabled_Type(TruthValue):
    """Custom type hh3cEponDeviceOrganizationSpecificEventEnabled based on TruthValue"""


_Hh3cEponDeviceOrganizationSpecificEventEnabled_Object = MibTableColumn
hh3cEponDeviceOrganizationSpecificEventEnabled = _Hh3cEponDeviceOrganizationSpecificEventEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 1, 1, 23),
    _Hh3cEponDeviceOrganizationSpecificEventEnabled_Type()
)
hh3cEponDeviceOrganizationSpecificEventEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponDeviceOrganizationSpecificEventEnabled.setStatus("current")


class _Hh3cEponDeviceEventControl_Type(Integer32):
    """Custom type hh3cEponDeviceEventControl based on Integer32"""
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


_Hh3cEponDeviceEventControl_Type.__name__ = "Integer32"
_Hh3cEponDeviceEventControl_Object = MibTableColumn
hh3cEponDeviceEventControl = _Hh3cEponDeviceEventControl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 1, 1, 24),
    _Hh3cEponDeviceEventControl_Type()
)
hh3cEponDeviceEventControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponDeviceEventControl.setStatus("current")
_Hh3cEponDeviceEventsLogTable_Object = MibTable
hh3cEponDeviceEventsLogTable = _Hh3cEponDeviceEventsLogTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cEponDeviceEventsLogTable.setStatus("current")
_Hh3cEponDeviceEventsLogEntry_Object = MibTableRow
hh3cEponDeviceEventsLogEntry = _Hh3cEponDeviceEventsLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 2, 1)
)
hh3cEponDeviceEventsLogEntry.setIndexNames(
    (0, "HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceEventsLogName"),
    (0, "HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceEventsLogIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponDeviceEventsLogEntry.setStatus("current")


class _Hh3cEponDeviceEventsLogName_Type(SnmpAdminString):
    """Custom type hh3cEponDeviceEventsLogName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cEponDeviceEventsLogName_Type.__name__ = "SnmpAdminString"
_Hh3cEponDeviceEventsLogName_Object = MibTableColumn
hh3cEponDeviceEventsLogName = _Hh3cEponDeviceEventsLogName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 2, 1, 1),
    _Hh3cEponDeviceEventsLogName_Type()
)
hh3cEponDeviceEventsLogName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEponDeviceEventsLogName.setStatus("current")


class _Hh3cEponDeviceEventsLogIndex_Type(Unsigned32):
    """Custom type hh3cEponDeviceEventsLogIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cEponDeviceEventsLogIndex_Type.__name__ = "Unsigned32"
_Hh3cEponDeviceEventsLogIndex_Object = MibTableColumn
hh3cEponDeviceEventsLogIndex = _Hh3cEponDeviceEventsLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 2, 1, 2),
    _Hh3cEponDeviceEventsLogIndex_Type()
)
hh3cEponDeviceEventsLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEponDeviceEventsLogIndex.setStatus("current")


class _Hh3cEponDeviceEventsLogID_Type(ObjectIdentifier):
    """Custom type hh3cEponDeviceEventsLogID based on ObjectIdentifier"""
    defaultValue = (0, 0)


_Hh3cEponDeviceEventsLogID_Object = MibTableColumn
hh3cEponDeviceEventsLogID = _Hh3cEponDeviceEventsLogID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 2, 1, 3),
    _Hh3cEponDeviceEventsLogID_Type()
)
hh3cEponDeviceEventsLogID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponDeviceEventsLogID.setStatus("current")
_Hh3cEponDeviceEventsLogFirstTime_Type = DateAndTime
_Hh3cEponDeviceEventsLogFirstTime_Object = MibTableColumn
hh3cEponDeviceEventsLogFirstTime = _Hh3cEponDeviceEventsLogFirstTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 2, 1, 4),
    _Hh3cEponDeviceEventsLogFirstTime_Type()
)
hh3cEponDeviceEventsLogFirstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceEventsLogFirstTime.setStatus("current")
_Hh3cEponDeviceEventsLogLastTime_Type = DateAndTime
_Hh3cEponDeviceEventsLogLastTime_Object = MibTableColumn
hh3cEponDeviceEventsLogLastTime = _Hh3cEponDeviceEventsLogLastTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 2, 1, 5),
    _Hh3cEponDeviceEventsLogLastTime_Type()
)
hh3cEponDeviceEventsLogLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceEventsLogLastTime.setStatus("current")
_Hh3cEponDeviceEventsLogCounts_Type = Counter32
_Hh3cEponDeviceEventsLogCounts_Object = MibTableColumn
hh3cEponDeviceEventsLogCounts = _Hh3cEponDeviceEventsLogCounts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 2, 1, 6),
    _Hh3cEponDeviceEventsLogCounts_Type()
)
hh3cEponDeviceEventsLogCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceEventsLogCounts.setStatus("current")


class _Hh3cEponDeviceEventsLogType_Type(Integer32):
    """Custom type hh3cEponDeviceEventsLogType based on Integer32"""
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
        *(("hh3cEponDeviceCriticalEventState", 2),
          ("hh3cEponDeviceDyingGaspAlarmState", 1),
          ("hh3cEponDeviceErroredFrameEventState", 8),
          ("hh3cEponDeviceErroredFramePeriodEventState", 9),
          ("hh3cEponDeviceErroredFrameSecondsSummaryEventState", 10),
          ("hh3cEponDeviceErroredSymbolPeriodEventState", 7),
          ("hh3cEponDeviceGlobalEventState", 6),
          ("hh3cEponDeviceLocalLinkFaultAlarmState", 3),
          ("hh3cEponDeviceOrganizationSpecificEventState", 11),
          ("hh3cEponDevicePowerVoltageEventIndicationState", 5),
          ("hh3cEponDeviceTemperatureEventIndicationState", 4))
    )


_Hh3cEponDeviceEventsLogType_Type.__name__ = "Integer32"
_Hh3cEponDeviceEventsLogType_Object = MibTableColumn
hh3cEponDeviceEventsLogType = _Hh3cEponDeviceEventsLogType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 2, 1, 7),
    _Hh3cEponDeviceEventsLogType_Type()
)
hh3cEponDeviceEventsLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponDeviceEventsLogType.setStatus("current")
_Hh3cEponDeviceEventsLogEntryStatus_Type = RowStatus
_Hh3cEponDeviceEventsLogEntryStatus_Object = MibTableColumn
hh3cEponDeviceEventsLogEntryStatus = _Hh3cEponDeviceEventsLogEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 1, 3, 2, 1, 8),
    _Hh3cEponDeviceEventsLogEntryStatus_Type()
)
hh3cEponDeviceEventsLogEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponDeviceEventsLogEntryStatus.setStatus("current")
_Hh3cEponDeviceConformance_ObjectIdentity = ObjectIdentity
hh3cEponDeviceConformance = _Hh3cEponDeviceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 2)
)
_Hh3cEponDeviceGroups_ObjectIdentity = ObjectIdentity
hh3cEponDeviceGroups = _Hh3cEponDeviceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 2, 1)
)
_Hh3cEponDeviceCompliances_ObjectIdentity = ObjectIdentity
hh3cEponDeviceCompliances = _Hh3cEponDeviceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 2, 2)
)

# Managed Objects groups

hh3cEponDeviceGroupControl = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 2, 1, 1)
)
hh3cEponDeviceGroupControl.setObjects(
      *(("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceObjectReset"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceObjectModes"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceObjectFecEnabled"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceObjectOamMode"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceObjectDeviceReadyMode"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceObjectPowerDown"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceObjectNumberOfLLIDs"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceObjectReportThreshold"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceRemoteMACAddressLLIDControl"))
)
if mibBuilder.loadTexts:
    hh3cEponDeviceGroupControl.setStatus("current")

hh3cEponDeviceGroupRMadLTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 2, 1, 2)
)
hh3cEponDeviceGroupRMadLTable.setObjects(
      *(("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceRMadlLLID"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceRMadlLogID"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceRMadlRemoteAddress"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceRMadlType"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceRMadlAction"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceRMadlEntryStatus"))
)
if mibBuilder.loadTexts:
    hh3cEponDeviceGroupRMadLTable.setStatus("current")

hh3cEponDeviceGroupStat = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 2, 1, 3)
)
hh3cEponDeviceGroupStat.setObjects(
      *(("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceStatTxFramesQueue0"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceStatTxFramesQueue1"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceStatTxFramesQueue2"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceStatTxFramesQueue3"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceStatTxFramesQueue4"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceStatTxFramesQueue5"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceStatTxFramesQueue6"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceStatTxFramesQueue7"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceStatRxFramesQueue0"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceStatRxFramesQueue1"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceStatRxFramesQueue2"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceStatRxFramesQueue3"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceStatRxFramesQueue4"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceStatRxFramesQueue5"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceStatRxFramesQueue6"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceStatRxFramesQueue7"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceStatDroppedFramesQueue0"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceStatDroppedFramesQueue1"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceStatDroppedFramesQueue2"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceStatDroppedFramesQueue3"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceStatDroppedFramesQueue4"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceStatDroppedFramesQueue5"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceStatDroppedFramesQueue6"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceStatDroppedFramesQueue7"))
)
if mibBuilder.loadTexts:
    hh3cEponDeviceGroupStat.setStatus("current")

hh3cEponDeviceGroupEvent = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 2, 1, 4)
)
hh3cEponDeviceGroupEvent.setObjects(
      *(("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceSampleMinimum"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceDyingGaspAlarmState"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceDyingGaspAlarmEnabled"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceCriticalEventState"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceCriticalEventEnabled"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceLocalLinkFaultAlarmState"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceLocalLinkFaultAlarmEnabled"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceTemperatureEventIndicationState"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceTemperatureEventIndicationEnabled"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDevicePowerVoltageEventIndicationState"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDevicePowerVoltageEventIndicationEnabled"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceGlobalEventState"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceGlobalEventEnabled"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceErroredSymbolPeriodEventState"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceErroredSymbolPeriodEventEnabled"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceErroredFrameEventState"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceErroredFrameEventEnabled"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceErroredFramePeriodEventState"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceErroredFramePeriodEventEnabled"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceErroredFrameSecondsSummaryEventState"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceErroredFrameSecondsSummaryEventEnabled"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceOrganizationSpecificEventState"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceOrganizationSpecificEventEnabled"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceEventControl"))
)
if mibBuilder.loadTexts:
    hh3cEponDeviceGroupEvent.setStatus("current")

hh3cEponDeviceGroupEventLog = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 2, 1, 5)
)
hh3cEponDeviceGroupEventLog.setObjects(
      *(("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceEventsLogID"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceEventsLogFirstTime"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceEventsLogLastTime"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceEventsLogCounts"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceEventsLogType"),
        ("HH3C-EPON-DEVICE-MIB", "hh3cEponDeviceEventsLogEntryStatus"))
)
if mibBuilder.loadTexts:
    hh3cEponDeviceGroupEventLog.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hh3cEponDeviceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 4, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cEponDeviceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-EPON-DEVICE-MIB",
    **{"hh3cEponDeviceMIB": hh3cEponDeviceMIB,
       "hh3cEponDeviceObjectMIB": hh3cEponDeviceObjectMIB,
       "hh3cEponDeviceObjects": hh3cEponDeviceObjects,
       "hh3cEponDeviceControlObjects": hh3cEponDeviceControlObjects,
       "hh3cEponDeviceControlTable": hh3cEponDeviceControlTable,
       "hh3cEponDeviceControlEntry": hh3cEponDeviceControlEntry,
       "hh3cEponDeviceObjectReset": hh3cEponDeviceObjectReset,
       "hh3cEponDeviceObjectModes": hh3cEponDeviceObjectModes,
       "hh3cEponDeviceObjectFecEnabled": hh3cEponDeviceObjectFecEnabled,
       "hh3cEponDeviceObjectOamMode": hh3cEponDeviceObjectOamMode,
       "hh3cEponDeviceObjectDeviceReadyMode": hh3cEponDeviceObjectDeviceReadyMode,
       "hh3cEponDeviceObjectPowerDown": hh3cEponDeviceObjectPowerDown,
       "hh3cEponDeviceObjectNumberOfLLIDs": hh3cEponDeviceObjectNumberOfLLIDs,
       "hh3cEponDeviceObjectReportThreshold": hh3cEponDeviceObjectReportThreshold,
       "hh3cEponDeviceRemoteMACAddressLLIDControl": hh3cEponDeviceRemoteMACAddressLLIDControl,
       "hh3cEponDeviceRemoteMACAddressLLIDTable": hh3cEponDeviceRemoteMACAddressLLIDTable,
       "hh3cEponDeviceRemoteMACAddressLLIDEntry": hh3cEponDeviceRemoteMACAddressLLIDEntry,
       "hh3cEponDeviceRemoteMACAddressLLIDName": hh3cEponDeviceRemoteMACAddressLLIDName,
       "hh3cEponDeviceRMadlLLID": hh3cEponDeviceRMadlLLID,
       "hh3cEponDeviceRMadlLogID": hh3cEponDeviceRMadlLogID,
       "hh3cEponDeviceRMadlRemoteAddress": hh3cEponDeviceRMadlRemoteAddress,
       "hh3cEponDeviceRMadlType": hh3cEponDeviceRMadlType,
       "hh3cEponDeviceRMadlAction": hh3cEponDeviceRMadlAction,
       "hh3cEponDeviceRMadlEntryStatus": hh3cEponDeviceRMadlEntryStatus,
       "hh3cEponDeviceStatObjects": hh3cEponDeviceStatObjects,
       "hh3cEponDeviceStatTable": hh3cEponDeviceStatTable,
       "hh3cEponDeviceStatEntry": hh3cEponDeviceStatEntry,
       "hh3cEponDeviceStatTxFramesQueue0": hh3cEponDeviceStatTxFramesQueue0,
       "hh3cEponDeviceStatTxFramesQueue1": hh3cEponDeviceStatTxFramesQueue1,
       "hh3cEponDeviceStatTxFramesQueue2": hh3cEponDeviceStatTxFramesQueue2,
       "hh3cEponDeviceStatTxFramesQueue3": hh3cEponDeviceStatTxFramesQueue3,
       "hh3cEponDeviceStatTxFramesQueue4": hh3cEponDeviceStatTxFramesQueue4,
       "hh3cEponDeviceStatTxFramesQueue5": hh3cEponDeviceStatTxFramesQueue5,
       "hh3cEponDeviceStatTxFramesQueue6": hh3cEponDeviceStatTxFramesQueue6,
       "hh3cEponDeviceStatTxFramesQueue7": hh3cEponDeviceStatTxFramesQueue7,
       "hh3cEponDeviceStatRxFramesQueue0": hh3cEponDeviceStatRxFramesQueue0,
       "hh3cEponDeviceStatRxFramesQueue1": hh3cEponDeviceStatRxFramesQueue1,
       "hh3cEponDeviceStatRxFramesQueue2": hh3cEponDeviceStatRxFramesQueue2,
       "hh3cEponDeviceStatRxFramesQueue3": hh3cEponDeviceStatRxFramesQueue3,
       "hh3cEponDeviceStatRxFramesQueue4": hh3cEponDeviceStatRxFramesQueue4,
       "hh3cEponDeviceStatRxFramesQueue5": hh3cEponDeviceStatRxFramesQueue5,
       "hh3cEponDeviceStatRxFramesQueue6": hh3cEponDeviceStatRxFramesQueue6,
       "hh3cEponDeviceStatRxFramesQueue7": hh3cEponDeviceStatRxFramesQueue7,
       "hh3cEponDeviceStatDroppedFramesQueue0": hh3cEponDeviceStatDroppedFramesQueue0,
       "hh3cEponDeviceStatDroppedFramesQueue1": hh3cEponDeviceStatDroppedFramesQueue1,
       "hh3cEponDeviceStatDroppedFramesQueue2": hh3cEponDeviceStatDroppedFramesQueue2,
       "hh3cEponDeviceStatDroppedFramesQueue3": hh3cEponDeviceStatDroppedFramesQueue3,
       "hh3cEponDeviceStatDroppedFramesQueue4": hh3cEponDeviceStatDroppedFramesQueue4,
       "hh3cEponDeviceStatDroppedFramesQueue5": hh3cEponDeviceStatDroppedFramesQueue5,
       "hh3cEponDeviceStatDroppedFramesQueue6": hh3cEponDeviceStatDroppedFramesQueue6,
       "hh3cEponDeviceStatDroppedFramesQueue7": hh3cEponDeviceStatDroppedFramesQueue7,
       "hh3cEponDeviceEventObjects": hh3cEponDeviceEventObjects,
       "hh3cEponDeviceEventObjectTable": hh3cEponDeviceEventObjectTable,
       "hh3cEponDeviceEventObjectEntry": hh3cEponDeviceEventObjectEntry,
       "hh3cEponDeviceSampleMinimum": hh3cEponDeviceSampleMinimum,
       "hh3cEponDeviceDyingGaspAlarmState": hh3cEponDeviceDyingGaspAlarmState,
       "hh3cEponDeviceDyingGaspAlarmEnabled": hh3cEponDeviceDyingGaspAlarmEnabled,
       "hh3cEponDeviceCriticalEventState": hh3cEponDeviceCriticalEventState,
       "hh3cEponDeviceCriticalEventEnabled": hh3cEponDeviceCriticalEventEnabled,
       "hh3cEponDeviceLocalLinkFaultAlarmState": hh3cEponDeviceLocalLinkFaultAlarmState,
       "hh3cEponDeviceLocalLinkFaultAlarmEnabled": hh3cEponDeviceLocalLinkFaultAlarmEnabled,
       "hh3cEponDeviceTemperatureEventIndicationState": hh3cEponDeviceTemperatureEventIndicationState,
       "hh3cEponDeviceTemperatureEventIndicationEnabled": hh3cEponDeviceTemperatureEventIndicationEnabled,
       "hh3cEponDevicePowerVoltageEventIndicationState": hh3cEponDevicePowerVoltageEventIndicationState,
       "hh3cEponDevicePowerVoltageEventIndicationEnabled": hh3cEponDevicePowerVoltageEventIndicationEnabled,
       "hh3cEponDeviceGlobalEventState": hh3cEponDeviceGlobalEventState,
       "hh3cEponDeviceGlobalEventEnabled": hh3cEponDeviceGlobalEventEnabled,
       "hh3cEponDeviceErroredSymbolPeriodEventState": hh3cEponDeviceErroredSymbolPeriodEventState,
       "hh3cEponDeviceErroredSymbolPeriodEventEnabled": hh3cEponDeviceErroredSymbolPeriodEventEnabled,
       "hh3cEponDeviceErroredFrameEventState": hh3cEponDeviceErroredFrameEventState,
       "hh3cEponDeviceErroredFrameEventEnabled": hh3cEponDeviceErroredFrameEventEnabled,
       "hh3cEponDeviceErroredFramePeriodEventState": hh3cEponDeviceErroredFramePeriodEventState,
       "hh3cEponDeviceErroredFramePeriodEventEnabled": hh3cEponDeviceErroredFramePeriodEventEnabled,
       "hh3cEponDeviceErroredFrameSecondsSummaryEventState": hh3cEponDeviceErroredFrameSecondsSummaryEventState,
       "hh3cEponDeviceErroredFrameSecondsSummaryEventEnabled": hh3cEponDeviceErroredFrameSecondsSummaryEventEnabled,
       "hh3cEponDeviceOrganizationSpecificEventState": hh3cEponDeviceOrganizationSpecificEventState,
       "hh3cEponDeviceOrganizationSpecificEventEnabled": hh3cEponDeviceOrganizationSpecificEventEnabled,
       "hh3cEponDeviceEventControl": hh3cEponDeviceEventControl,
       "hh3cEponDeviceEventsLogTable": hh3cEponDeviceEventsLogTable,
       "hh3cEponDeviceEventsLogEntry": hh3cEponDeviceEventsLogEntry,
       "hh3cEponDeviceEventsLogName": hh3cEponDeviceEventsLogName,
       "hh3cEponDeviceEventsLogIndex": hh3cEponDeviceEventsLogIndex,
       "hh3cEponDeviceEventsLogID": hh3cEponDeviceEventsLogID,
       "hh3cEponDeviceEventsLogFirstTime": hh3cEponDeviceEventsLogFirstTime,
       "hh3cEponDeviceEventsLogLastTime": hh3cEponDeviceEventsLogLastTime,
       "hh3cEponDeviceEventsLogCounts": hh3cEponDeviceEventsLogCounts,
       "hh3cEponDeviceEventsLogType": hh3cEponDeviceEventsLogType,
       "hh3cEponDeviceEventsLogEntryStatus": hh3cEponDeviceEventsLogEntryStatus,
       "hh3cEponDeviceConformance": hh3cEponDeviceConformance,
       "hh3cEponDeviceGroups": hh3cEponDeviceGroups,
       "hh3cEponDeviceGroupControl": hh3cEponDeviceGroupControl,
       "hh3cEponDeviceGroupRMadLTable": hh3cEponDeviceGroupRMadLTable,
       "hh3cEponDeviceGroupStat": hh3cEponDeviceGroupStat,
       "hh3cEponDeviceGroupEvent": hh3cEponDeviceGroupEvent,
       "hh3cEponDeviceGroupEventLog": hh3cEponDeviceGroupEventLog,
       "hh3cEponDeviceCompliances": hh3cEponDeviceCompliances,
       "hh3cEponDeviceCompliance": hh3cEponDeviceCompliance}
)
