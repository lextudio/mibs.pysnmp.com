# SNMP MIB module (H3C-EPON-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-EPON-DEVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:28 2024
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

(h3cEpon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cEpon")

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

h3cEponDeviceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4)
)
h3cEponDeviceMIB.setRevisions(
        ("2004-09-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cEponDeviceObjectMIB_ObjectIdentity = ObjectIdentity
h3cEponDeviceObjectMIB = _H3cEponDeviceObjectMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1)
)
_H3cEponDeviceObjects_ObjectIdentity = ObjectIdentity
h3cEponDeviceObjects = _H3cEponDeviceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1)
)
_H3cEponDeviceControlObjects_ObjectIdentity = ObjectIdentity
h3cEponDeviceControlObjects = _H3cEponDeviceControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 1)
)
_H3cEponDeviceControlTable_Object = MibTable
h3cEponDeviceControlTable = _H3cEponDeviceControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cEponDeviceControlTable.setStatus("current")
_H3cEponDeviceControlEntry_Object = MibTableRow
h3cEponDeviceControlEntry = _H3cEponDeviceControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 1, 1, 1)
)
h3cEponDeviceControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cEponDeviceControlEntry.setStatus("current")


class _H3cEponDeviceObjectReset_Type(Integer32):
    """Custom type h3cEponDeviceObjectReset based on Integer32"""
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


_H3cEponDeviceObjectReset_Type.__name__ = "Integer32"
_H3cEponDeviceObjectReset_Object = MibTableColumn
h3cEponDeviceObjectReset = _H3cEponDeviceObjectReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 1, 1, 1, 1),
    _H3cEponDeviceObjectReset_Type()
)
h3cEponDeviceObjectReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponDeviceObjectReset.setStatus("current")


class _H3cEponDeviceObjectModes_Type(Integer32):
    """Custom type h3cEponDeviceObjectModes based on Integer32"""
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


_H3cEponDeviceObjectModes_Type.__name__ = "Integer32"
_H3cEponDeviceObjectModes_Object = MibTableColumn
h3cEponDeviceObjectModes = _H3cEponDeviceObjectModes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 1, 1, 1, 2),
    _H3cEponDeviceObjectModes_Type()
)
h3cEponDeviceObjectModes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceObjectModes.setStatus("current")


class _H3cEponDeviceObjectFecEnabled_Type(Integer32):
    """Custom type h3cEponDeviceObjectFecEnabled based on Integer32"""
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


_H3cEponDeviceObjectFecEnabled_Type.__name__ = "Integer32"
_H3cEponDeviceObjectFecEnabled_Object = MibTableColumn
h3cEponDeviceObjectFecEnabled = _H3cEponDeviceObjectFecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 1, 1, 1, 4),
    _H3cEponDeviceObjectFecEnabled_Type()
)
h3cEponDeviceObjectFecEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponDeviceObjectFecEnabled.setStatus("current")


class _H3cEponDeviceObjectOamMode_Type(Integer32):
    """Custom type h3cEponDeviceObjectOamMode based on Integer32"""
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


_H3cEponDeviceObjectOamMode_Type.__name__ = "Integer32"
_H3cEponDeviceObjectOamMode_Object = MibTableColumn
h3cEponDeviceObjectOamMode = _H3cEponDeviceObjectOamMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 1, 1, 1, 5),
    _H3cEponDeviceObjectOamMode_Type()
)
h3cEponDeviceObjectOamMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponDeviceObjectOamMode.setStatus("current")


class _H3cEponDeviceObjectDeviceReadyMode_Type(Integer32):
    """Custom type h3cEponDeviceObjectDeviceReadyMode based on Integer32"""
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


_H3cEponDeviceObjectDeviceReadyMode_Type.__name__ = "Integer32"
_H3cEponDeviceObjectDeviceReadyMode_Object = MibTableColumn
h3cEponDeviceObjectDeviceReadyMode = _H3cEponDeviceObjectDeviceReadyMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 1, 1, 1, 6),
    _H3cEponDeviceObjectDeviceReadyMode_Type()
)
h3cEponDeviceObjectDeviceReadyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponDeviceObjectDeviceReadyMode.setStatus("current")


class _H3cEponDeviceObjectPowerDown_Type(TruthValue):
    """Custom type h3cEponDeviceObjectPowerDown based on TruthValue"""


_H3cEponDeviceObjectPowerDown_Object = MibTableColumn
h3cEponDeviceObjectPowerDown = _H3cEponDeviceObjectPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 1, 1, 1, 7),
    _H3cEponDeviceObjectPowerDown_Type()
)
h3cEponDeviceObjectPowerDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponDeviceObjectPowerDown.setStatus("current")
_H3cEponDeviceObjectNumberOfLLIDs_Type = Integer32
_H3cEponDeviceObjectNumberOfLLIDs_Object = MibTableColumn
h3cEponDeviceObjectNumberOfLLIDs = _H3cEponDeviceObjectNumberOfLLIDs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 1, 1, 1, 8),
    _H3cEponDeviceObjectNumberOfLLIDs_Type()
)
h3cEponDeviceObjectNumberOfLLIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceObjectNumberOfLLIDs.setStatus("current")


class _H3cEponDeviceObjectReportThreshold_Type(Integer32):
    """Custom type h3cEponDeviceObjectReportThreshold based on Integer32"""
    defaultValue = 0


_H3cEponDeviceObjectReportThreshold_Object = MibTableColumn
h3cEponDeviceObjectReportThreshold = _H3cEponDeviceObjectReportThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 1, 1, 1, 9),
    _H3cEponDeviceObjectReportThreshold_Type()
)
h3cEponDeviceObjectReportThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponDeviceObjectReportThreshold.setStatus("current")
if mibBuilder.loadTexts:
    h3cEponDeviceObjectReportThreshold.setUnits("TQ (16nsec)")


class _H3cEponDeviceRemoteMACAddressLLIDControl_Type(Integer32):
    """Custom type h3cEponDeviceRemoteMACAddressLLIDControl based on Integer32"""
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


_H3cEponDeviceRemoteMACAddressLLIDControl_Type.__name__ = "Integer32"
_H3cEponDeviceRemoteMACAddressLLIDControl_Object = MibTableColumn
h3cEponDeviceRemoteMACAddressLLIDControl = _H3cEponDeviceRemoteMACAddressLLIDControl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 1, 1, 1, 10),
    _H3cEponDeviceRemoteMACAddressLLIDControl_Type()
)
h3cEponDeviceRemoteMACAddressLLIDControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponDeviceRemoteMACAddressLLIDControl.setStatus("current")
_H3cEponDeviceRemoteMACAddressLLIDTable_Object = MibTable
h3cEponDeviceRemoteMACAddressLLIDTable = _H3cEponDeviceRemoteMACAddressLLIDTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    h3cEponDeviceRemoteMACAddressLLIDTable.setStatus("current")
_H3cEponDeviceRemoteMACAddressLLIDEntry_Object = MibTableRow
h3cEponDeviceRemoteMACAddressLLIDEntry = _H3cEponDeviceRemoteMACAddressLLIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 1, 2, 1)
)
h3cEponDeviceRemoteMACAddressLLIDEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cEponDeviceRemoteMACAddressLLIDEntry.setStatus("current")


class _H3cEponDeviceRemoteMACAddressLLIDName_Type(SnmpAdminString):
    """Custom type h3cEponDeviceRemoteMACAddressLLIDName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_H3cEponDeviceRemoteMACAddressLLIDName_Type.__name__ = "SnmpAdminString"
_H3cEponDeviceRemoteMACAddressLLIDName_Object = MibTableColumn
h3cEponDeviceRemoteMACAddressLLIDName = _H3cEponDeviceRemoteMACAddressLLIDName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 1, 2, 1, 1),
    _H3cEponDeviceRemoteMACAddressLLIDName_Type()
)
h3cEponDeviceRemoteMACAddressLLIDName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponDeviceRemoteMACAddressLLIDName.setStatus("current")


class _H3cEponDeviceRMadlLLID_Type(Unsigned32):
    """Custom type h3cEponDeviceRMadlLLID based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_H3cEponDeviceRMadlLLID_Type.__name__ = "Unsigned32"
_H3cEponDeviceRMadlLLID_Object = MibTableColumn
h3cEponDeviceRMadlLLID = _H3cEponDeviceRMadlLLID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 1, 2, 1, 2),
    _H3cEponDeviceRMadlLLID_Type()
)
h3cEponDeviceRMadlLLID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponDeviceRMadlLLID.setStatus("current")


class _H3cEponDeviceRMadlLogID_Type(ObjectIdentifier):
    """Custom type h3cEponDeviceRMadlLogID based on ObjectIdentifier"""
    defaultValue = (0, 0)


_H3cEponDeviceRMadlLogID_Object = MibTableColumn
h3cEponDeviceRMadlLogID = _H3cEponDeviceRMadlLogID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 1, 2, 1, 3),
    _H3cEponDeviceRMadlLogID_Type()
)
h3cEponDeviceRMadlLogID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponDeviceRMadlLogID.setStatus("current")
_H3cEponDeviceRMadlRemoteAddress_Type = MacAddress
_H3cEponDeviceRMadlRemoteAddress_Object = MibTableColumn
h3cEponDeviceRMadlRemoteAddress = _H3cEponDeviceRMadlRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 1, 2, 1, 4),
    _H3cEponDeviceRMadlRemoteAddress_Type()
)
h3cEponDeviceRMadlRemoteAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponDeviceRMadlRemoteAddress.setStatus("current")


class _H3cEponDeviceRMadlType_Type(Integer32):
    """Custom type h3cEponDeviceRMadlType based on Integer32"""
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


_H3cEponDeviceRMadlType_Type.__name__ = "Integer32"
_H3cEponDeviceRMadlType_Object = MibTableColumn
h3cEponDeviceRMadlType = _H3cEponDeviceRMadlType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 1, 2, 1, 5),
    _H3cEponDeviceRMadlType_Type()
)
h3cEponDeviceRMadlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponDeviceRMadlType.setStatus("current")


class _H3cEponDeviceRMadlAction_Type(Integer32):
    """Custom type h3cEponDeviceRMadlAction based on Integer32"""
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


_H3cEponDeviceRMadlAction_Type.__name__ = "Integer32"
_H3cEponDeviceRMadlAction_Object = MibTableColumn
h3cEponDeviceRMadlAction = _H3cEponDeviceRMadlAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 1, 2, 1, 6),
    _H3cEponDeviceRMadlAction_Type()
)
h3cEponDeviceRMadlAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponDeviceRMadlAction.setStatus("current")
_H3cEponDeviceRMadlEntryStatus_Type = RowStatus
_H3cEponDeviceRMadlEntryStatus_Object = MibTableColumn
h3cEponDeviceRMadlEntryStatus = _H3cEponDeviceRMadlEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 1, 2, 1, 7),
    _H3cEponDeviceRMadlEntryStatus_Type()
)
h3cEponDeviceRMadlEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponDeviceRMadlEntryStatus.setStatus("current")
_H3cEponDeviceStatObjects_ObjectIdentity = ObjectIdentity
h3cEponDeviceStatObjects = _H3cEponDeviceStatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 2)
)
_H3cEponDeviceStatTable_Object = MibTable
h3cEponDeviceStatTable = _H3cEponDeviceStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cEponDeviceStatTable.setStatus("current")
_H3cEponDeviceStatEntry_Object = MibTableRow
h3cEponDeviceStatEntry = _H3cEponDeviceStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 2, 1, 1)
)
h3cEponDeviceStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cEponDeviceStatEntry.setStatus("current")
_H3cEponDeviceStatTxFramesQueue0_Type = Counter32
_H3cEponDeviceStatTxFramesQueue0_Object = MibTableColumn
h3cEponDeviceStatTxFramesQueue0 = _H3cEponDeviceStatTxFramesQueue0_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 2, 1, 1, 1),
    _H3cEponDeviceStatTxFramesQueue0_Type()
)
h3cEponDeviceStatTxFramesQueue0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceStatTxFramesQueue0.setStatus("current")
if mibBuilder.loadTexts:
    h3cEponDeviceStatTxFramesQueue0.setUnits("frames")
_H3cEponDeviceStatTxFramesQueue1_Type = Counter32
_H3cEponDeviceStatTxFramesQueue1_Object = MibTableColumn
h3cEponDeviceStatTxFramesQueue1 = _H3cEponDeviceStatTxFramesQueue1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 2, 1, 1, 2),
    _H3cEponDeviceStatTxFramesQueue1_Type()
)
h3cEponDeviceStatTxFramesQueue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceStatTxFramesQueue1.setStatus("current")
if mibBuilder.loadTexts:
    h3cEponDeviceStatTxFramesQueue1.setUnits("frames")
_H3cEponDeviceStatTxFramesQueue2_Type = Counter32
_H3cEponDeviceStatTxFramesQueue2_Object = MibTableColumn
h3cEponDeviceStatTxFramesQueue2 = _H3cEponDeviceStatTxFramesQueue2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 2, 1, 1, 3),
    _H3cEponDeviceStatTxFramesQueue2_Type()
)
h3cEponDeviceStatTxFramesQueue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceStatTxFramesQueue2.setStatus("current")
if mibBuilder.loadTexts:
    h3cEponDeviceStatTxFramesQueue2.setUnits("frames")
_H3cEponDeviceStatTxFramesQueue3_Type = Counter32
_H3cEponDeviceStatTxFramesQueue3_Object = MibTableColumn
h3cEponDeviceStatTxFramesQueue3 = _H3cEponDeviceStatTxFramesQueue3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 2, 1, 1, 4),
    _H3cEponDeviceStatTxFramesQueue3_Type()
)
h3cEponDeviceStatTxFramesQueue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceStatTxFramesQueue3.setStatus("current")
if mibBuilder.loadTexts:
    h3cEponDeviceStatTxFramesQueue3.setUnits("frames")
_H3cEponDeviceStatTxFramesQueue4_Type = Counter32
_H3cEponDeviceStatTxFramesQueue4_Object = MibTableColumn
h3cEponDeviceStatTxFramesQueue4 = _H3cEponDeviceStatTxFramesQueue4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 2, 1, 1, 5),
    _H3cEponDeviceStatTxFramesQueue4_Type()
)
h3cEponDeviceStatTxFramesQueue4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceStatTxFramesQueue4.setStatus("current")
if mibBuilder.loadTexts:
    h3cEponDeviceStatTxFramesQueue4.setUnits("frames")
_H3cEponDeviceStatTxFramesQueue5_Type = Counter32
_H3cEponDeviceStatTxFramesQueue5_Object = MibTableColumn
h3cEponDeviceStatTxFramesQueue5 = _H3cEponDeviceStatTxFramesQueue5_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 2, 1, 1, 6),
    _H3cEponDeviceStatTxFramesQueue5_Type()
)
h3cEponDeviceStatTxFramesQueue5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceStatTxFramesQueue5.setStatus("current")
if mibBuilder.loadTexts:
    h3cEponDeviceStatTxFramesQueue5.setUnits("frames")
_H3cEponDeviceStatTxFramesQueue6_Type = Counter32
_H3cEponDeviceStatTxFramesQueue6_Object = MibTableColumn
h3cEponDeviceStatTxFramesQueue6 = _H3cEponDeviceStatTxFramesQueue6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 2, 1, 1, 7),
    _H3cEponDeviceStatTxFramesQueue6_Type()
)
h3cEponDeviceStatTxFramesQueue6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceStatTxFramesQueue6.setStatus("current")
if mibBuilder.loadTexts:
    h3cEponDeviceStatTxFramesQueue6.setUnits("frames")
_H3cEponDeviceStatTxFramesQueue7_Type = Counter32
_H3cEponDeviceStatTxFramesQueue7_Object = MibTableColumn
h3cEponDeviceStatTxFramesQueue7 = _H3cEponDeviceStatTxFramesQueue7_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 2, 1, 1, 8),
    _H3cEponDeviceStatTxFramesQueue7_Type()
)
h3cEponDeviceStatTxFramesQueue7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceStatTxFramesQueue7.setStatus("current")
if mibBuilder.loadTexts:
    h3cEponDeviceStatTxFramesQueue7.setUnits("frames")
_H3cEponDeviceStatRxFramesQueue0_Type = Counter32
_H3cEponDeviceStatRxFramesQueue0_Object = MibTableColumn
h3cEponDeviceStatRxFramesQueue0 = _H3cEponDeviceStatRxFramesQueue0_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 2, 1, 1, 9),
    _H3cEponDeviceStatRxFramesQueue0_Type()
)
h3cEponDeviceStatRxFramesQueue0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceStatRxFramesQueue0.setStatus("current")
if mibBuilder.loadTexts:
    h3cEponDeviceStatRxFramesQueue0.setUnits("frames")
_H3cEponDeviceStatRxFramesQueue1_Type = Counter32
_H3cEponDeviceStatRxFramesQueue1_Object = MibTableColumn
h3cEponDeviceStatRxFramesQueue1 = _H3cEponDeviceStatRxFramesQueue1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 2, 1, 1, 10),
    _H3cEponDeviceStatRxFramesQueue1_Type()
)
h3cEponDeviceStatRxFramesQueue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceStatRxFramesQueue1.setStatus("current")
if mibBuilder.loadTexts:
    h3cEponDeviceStatRxFramesQueue1.setUnits("frames")
_H3cEponDeviceStatRxFramesQueue2_Type = Counter32
_H3cEponDeviceStatRxFramesQueue2_Object = MibTableColumn
h3cEponDeviceStatRxFramesQueue2 = _H3cEponDeviceStatRxFramesQueue2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 2, 1, 1, 11),
    _H3cEponDeviceStatRxFramesQueue2_Type()
)
h3cEponDeviceStatRxFramesQueue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceStatRxFramesQueue2.setStatus("current")
if mibBuilder.loadTexts:
    h3cEponDeviceStatRxFramesQueue2.setUnits("frames")
_H3cEponDeviceStatRxFramesQueue3_Type = Counter32
_H3cEponDeviceStatRxFramesQueue3_Object = MibTableColumn
h3cEponDeviceStatRxFramesQueue3 = _H3cEponDeviceStatRxFramesQueue3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 2, 1, 1, 12),
    _H3cEponDeviceStatRxFramesQueue3_Type()
)
h3cEponDeviceStatRxFramesQueue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceStatRxFramesQueue3.setStatus("current")
if mibBuilder.loadTexts:
    h3cEponDeviceStatRxFramesQueue3.setUnits("frames")
_H3cEponDeviceStatRxFramesQueue4_Type = Counter32
_H3cEponDeviceStatRxFramesQueue4_Object = MibTableColumn
h3cEponDeviceStatRxFramesQueue4 = _H3cEponDeviceStatRxFramesQueue4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 2, 1, 1, 13),
    _H3cEponDeviceStatRxFramesQueue4_Type()
)
h3cEponDeviceStatRxFramesQueue4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceStatRxFramesQueue4.setStatus("current")
if mibBuilder.loadTexts:
    h3cEponDeviceStatRxFramesQueue4.setUnits("frames")
_H3cEponDeviceStatRxFramesQueue5_Type = Counter32
_H3cEponDeviceStatRxFramesQueue5_Object = MibTableColumn
h3cEponDeviceStatRxFramesQueue5 = _H3cEponDeviceStatRxFramesQueue5_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 2, 1, 1, 14),
    _H3cEponDeviceStatRxFramesQueue5_Type()
)
h3cEponDeviceStatRxFramesQueue5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceStatRxFramesQueue5.setStatus("current")
if mibBuilder.loadTexts:
    h3cEponDeviceStatRxFramesQueue5.setUnits("frames")
_H3cEponDeviceStatRxFramesQueue6_Type = Counter32
_H3cEponDeviceStatRxFramesQueue6_Object = MibTableColumn
h3cEponDeviceStatRxFramesQueue6 = _H3cEponDeviceStatRxFramesQueue6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 2, 1, 1, 15),
    _H3cEponDeviceStatRxFramesQueue6_Type()
)
h3cEponDeviceStatRxFramesQueue6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceStatRxFramesQueue6.setStatus("current")
if mibBuilder.loadTexts:
    h3cEponDeviceStatRxFramesQueue6.setUnits("frames")
_H3cEponDeviceStatRxFramesQueue7_Type = Counter32
_H3cEponDeviceStatRxFramesQueue7_Object = MibTableColumn
h3cEponDeviceStatRxFramesQueue7 = _H3cEponDeviceStatRxFramesQueue7_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 2, 1, 1, 16),
    _H3cEponDeviceStatRxFramesQueue7_Type()
)
h3cEponDeviceStatRxFramesQueue7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceStatRxFramesQueue7.setStatus("current")
if mibBuilder.loadTexts:
    h3cEponDeviceStatRxFramesQueue7.setUnits("frames")
_H3cEponDeviceStatDroppedFramesQueue0_Type = Counter32
_H3cEponDeviceStatDroppedFramesQueue0_Object = MibTableColumn
h3cEponDeviceStatDroppedFramesQueue0 = _H3cEponDeviceStatDroppedFramesQueue0_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 2, 1, 1, 17),
    _H3cEponDeviceStatDroppedFramesQueue0_Type()
)
h3cEponDeviceStatDroppedFramesQueue0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceStatDroppedFramesQueue0.setStatus("current")
if mibBuilder.loadTexts:
    h3cEponDeviceStatDroppedFramesQueue0.setUnits("frames")
_H3cEponDeviceStatDroppedFramesQueue1_Type = Counter32
_H3cEponDeviceStatDroppedFramesQueue1_Object = MibTableColumn
h3cEponDeviceStatDroppedFramesQueue1 = _H3cEponDeviceStatDroppedFramesQueue1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 2, 1, 1, 18),
    _H3cEponDeviceStatDroppedFramesQueue1_Type()
)
h3cEponDeviceStatDroppedFramesQueue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceStatDroppedFramesQueue1.setStatus("current")
if mibBuilder.loadTexts:
    h3cEponDeviceStatDroppedFramesQueue1.setUnits("frames")
_H3cEponDeviceStatDroppedFramesQueue2_Type = Counter32
_H3cEponDeviceStatDroppedFramesQueue2_Object = MibTableColumn
h3cEponDeviceStatDroppedFramesQueue2 = _H3cEponDeviceStatDroppedFramesQueue2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 2, 1, 1, 19),
    _H3cEponDeviceStatDroppedFramesQueue2_Type()
)
h3cEponDeviceStatDroppedFramesQueue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceStatDroppedFramesQueue2.setStatus("current")
if mibBuilder.loadTexts:
    h3cEponDeviceStatDroppedFramesQueue2.setUnits("frames")
_H3cEponDeviceStatDroppedFramesQueue3_Type = Counter32
_H3cEponDeviceStatDroppedFramesQueue3_Object = MibTableColumn
h3cEponDeviceStatDroppedFramesQueue3 = _H3cEponDeviceStatDroppedFramesQueue3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 2, 1, 1, 20),
    _H3cEponDeviceStatDroppedFramesQueue3_Type()
)
h3cEponDeviceStatDroppedFramesQueue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceStatDroppedFramesQueue3.setStatus("current")
if mibBuilder.loadTexts:
    h3cEponDeviceStatDroppedFramesQueue3.setUnits("frames")
_H3cEponDeviceStatDroppedFramesQueue4_Type = Counter32
_H3cEponDeviceStatDroppedFramesQueue4_Object = MibTableColumn
h3cEponDeviceStatDroppedFramesQueue4 = _H3cEponDeviceStatDroppedFramesQueue4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 2, 1, 1, 21),
    _H3cEponDeviceStatDroppedFramesQueue4_Type()
)
h3cEponDeviceStatDroppedFramesQueue4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceStatDroppedFramesQueue4.setStatus("current")
if mibBuilder.loadTexts:
    h3cEponDeviceStatDroppedFramesQueue4.setUnits("frames")
_H3cEponDeviceStatDroppedFramesQueue5_Type = Counter32
_H3cEponDeviceStatDroppedFramesQueue5_Object = MibTableColumn
h3cEponDeviceStatDroppedFramesQueue5 = _H3cEponDeviceStatDroppedFramesQueue5_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 2, 1, 1, 22),
    _H3cEponDeviceStatDroppedFramesQueue5_Type()
)
h3cEponDeviceStatDroppedFramesQueue5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceStatDroppedFramesQueue5.setStatus("current")
if mibBuilder.loadTexts:
    h3cEponDeviceStatDroppedFramesQueue5.setUnits("frames")
_H3cEponDeviceStatDroppedFramesQueue6_Type = Counter32
_H3cEponDeviceStatDroppedFramesQueue6_Object = MibTableColumn
h3cEponDeviceStatDroppedFramesQueue6 = _H3cEponDeviceStatDroppedFramesQueue6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 2, 1, 1, 23),
    _H3cEponDeviceStatDroppedFramesQueue6_Type()
)
h3cEponDeviceStatDroppedFramesQueue6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceStatDroppedFramesQueue6.setStatus("current")
if mibBuilder.loadTexts:
    h3cEponDeviceStatDroppedFramesQueue6.setUnits("frames")
_H3cEponDeviceStatDroppedFramesQueue7_Type = Counter32
_H3cEponDeviceStatDroppedFramesQueue7_Object = MibTableColumn
h3cEponDeviceStatDroppedFramesQueue7 = _H3cEponDeviceStatDroppedFramesQueue7_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 2, 1, 1, 24),
    _H3cEponDeviceStatDroppedFramesQueue7_Type()
)
h3cEponDeviceStatDroppedFramesQueue7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceStatDroppedFramesQueue7.setStatus("current")
if mibBuilder.loadTexts:
    h3cEponDeviceStatDroppedFramesQueue7.setUnits("frames")
_H3cEponDeviceEventObjects_ObjectIdentity = ObjectIdentity
h3cEponDeviceEventObjects = _H3cEponDeviceEventObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3)
)
_H3cEponDeviceEventObjectTable_Object = MibTable
h3cEponDeviceEventObjectTable = _H3cEponDeviceEventObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    h3cEponDeviceEventObjectTable.setStatus("current")
_H3cEponDeviceEventObjectEntry_Object = MibTableRow
h3cEponDeviceEventObjectEntry = _H3cEponDeviceEventObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 1, 1)
)
h3cEponDeviceEventObjectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cEponDeviceEventObjectEntry.setStatus("current")


class _H3cEponDeviceSampleMinimum_Type(Integer32):
    """Custom type h3cEponDeviceSampleMinimum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cEponDeviceSampleMinimum_Type.__name__ = "Integer32"
_H3cEponDeviceSampleMinimum_Object = MibTableColumn
h3cEponDeviceSampleMinimum = _H3cEponDeviceSampleMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 1, 1, 1),
    _H3cEponDeviceSampleMinimum_Type()
)
h3cEponDeviceSampleMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponDeviceSampleMinimum.setStatus("current")
if mibBuilder.loadTexts:
    h3cEponDeviceSampleMinimum.setUnits("seconds")
_H3cEponDeviceDyingGaspAlarmState_Type = TruthValue
_H3cEponDeviceDyingGaspAlarmState_Object = MibTableColumn
h3cEponDeviceDyingGaspAlarmState = _H3cEponDeviceDyingGaspAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 1, 1, 2),
    _H3cEponDeviceDyingGaspAlarmState_Type()
)
h3cEponDeviceDyingGaspAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceDyingGaspAlarmState.setStatus("current")


class _H3cEponDeviceDyingGaspAlarmEnabled_Type(TruthValue):
    """Custom type h3cEponDeviceDyingGaspAlarmEnabled based on TruthValue"""


_H3cEponDeviceDyingGaspAlarmEnabled_Object = MibTableColumn
h3cEponDeviceDyingGaspAlarmEnabled = _H3cEponDeviceDyingGaspAlarmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 1, 1, 3),
    _H3cEponDeviceDyingGaspAlarmEnabled_Type()
)
h3cEponDeviceDyingGaspAlarmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponDeviceDyingGaspAlarmEnabled.setStatus("current")
_H3cEponDeviceCriticalEventState_Type = TruthValue
_H3cEponDeviceCriticalEventState_Object = MibTableColumn
h3cEponDeviceCriticalEventState = _H3cEponDeviceCriticalEventState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 1, 1, 4),
    _H3cEponDeviceCriticalEventState_Type()
)
h3cEponDeviceCriticalEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceCriticalEventState.setStatus("current")


class _H3cEponDeviceCriticalEventEnabled_Type(TruthValue):
    """Custom type h3cEponDeviceCriticalEventEnabled based on TruthValue"""


_H3cEponDeviceCriticalEventEnabled_Object = MibTableColumn
h3cEponDeviceCriticalEventEnabled = _H3cEponDeviceCriticalEventEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 1, 1, 5),
    _H3cEponDeviceCriticalEventEnabled_Type()
)
h3cEponDeviceCriticalEventEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponDeviceCriticalEventEnabled.setStatus("current")
_H3cEponDeviceLocalLinkFaultAlarmState_Type = TruthValue
_H3cEponDeviceLocalLinkFaultAlarmState_Object = MibTableColumn
h3cEponDeviceLocalLinkFaultAlarmState = _H3cEponDeviceLocalLinkFaultAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 1, 1, 6),
    _H3cEponDeviceLocalLinkFaultAlarmState_Type()
)
h3cEponDeviceLocalLinkFaultAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceLocalLinkFaultAlarmState.setStatus("current")


class _H3cEponDeviceLocalLinkFaultAlarmEnabled_Type(TruthValue):
    """Custom type h3cEponDeviceLocalLinkFaultAlarmEnabled based on TruthValue"""


_H3cEponDeviceLocalLinkFaultAlarmEnabled_Object = MibTableColumn
h3cEponDeviceLocalLinkFaultAlarmEnabled = _H3cEponDeviceLocalLinkFaultAlarmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 1, 1, 7),
    _H3cEponDeviceLocalLinkFaultAlarmEnabled_Type()
)
h3cEponDeviceLocalLinkFaultAlarmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponDeviceLocalLinkFaultAlarmEnabled.setStatus("current")
_H3cEponDeviceTemperatureEventIndicationState_Type = TruthValue
_H3cEponDeviceTemperatureEventIndicationState_Object = MibTableColumn
h3cEponDeviceTemperatureEventIndicationState = _H3cEponDeviceTemperatureEventIndicationState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 1, 1, 8),
    _H3cEponDeviceTemperatureEventIndicationState_Type()
)
h3cEponDeviceTemperatureEventIndicationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceTemperatureEventIndicationState.setStatus("current")


class _H3cEponDeviceTemperatureEventIndicationEnabled_Type(TruthValue):
    """Custom type h3cEponDeviceTemperatureEventIndicationEnabled based on TruthValue"""


_H3cEponDeviceTemperatureEventIndicationEnabled_Object = MibTableColumn
h3cEponDeviceTemperatureEventIndicationEnabled = _H3cEponDeviceTemperatureEventIndicationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 1, 1, 9),
    _H3cEponDeviceTemperatureEventIndicationEnabled_Type()
)
h3cEponDeviceTemperatureEventIndicationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponDeviceTemperatureEventIndicationEnabled.setStatus("current")
_H3cEponDevicePowerVoltageEventIndicationState_Type = TruthValue
_H3cEponDevicePowerVoltageEventIndicationState_Object = MibTableColumn
h3cEponDevicePowerVoltageEventIndicationState = _H3cEponDevicePowerVoltageEventIndicationState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 1, 1, 10),
    _H3cEponDevicePowerVoltageEventIndicationState_Type()
)
h3cEponDevicePowerVoltageEventIndicationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDevicePowerVoltageEventIndicationState.setStatus("current")


class _H3cEponDevicePowerVoltageEventIndicationEnabled_Type(TruthValue):
    """Custom type h3cEponDevicePowerVoltageEventIndicationEnabled based on TruthValue"""


_H3cEponDevicePowerVoltageEventIndicationEnabled_Object = MibTableColumn
h3cEponDevicePowerVoltageEventIndicationEnabled = _H3cEponDevicePowerVoltageEventIndicationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 1, 1, 11),
    _H3cEponDevicePowerVoltageEventIndicationEnabled_Type()
)
h3cEponDevicePowerVoltageEventIndicationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponDevicePowerVoltageEventIndicationEnabled.setStatus("current")
_H3cEponDeviceGlobalEventState_Type = TruthValue
_H3cEponDeviceGlobalEventState_Object = MibTableColumn
h3cEponDeviceGlobalEventState = _H3cEponDeviceGlobalEventState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 1, 1, 12),
    _H3cEponDeviceGlobalEventState_Type()
)
h3cEponDeviceGlobalEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceGlobalEventState.setStatus("current")


class _H3cEponDeviceGlobalEventEnabled_Type(TruthValue):
    """Custom type h3cEponDeviceGlobalEventEnabled based on TruthValue"""


_H3cEponDeviceGlobalEventEnabled_Object = MibTableColumn
h3cEponDeviceGlobalEventEnabled = _H3cEponDeviceGlobalEventEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 1, 1, 13),
    _H3cEponDeviceGlobalEventEnabled_Type()
)
h3cEponDeviceGlobalEventEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponDeviceGlobalEventEnabled.setStatus("current")
_H3cEponDeviceErroredSymbolPeriodEventState_Type = TruthValue
_H3cEponDeviceErroredSymbolPeriodEventState_Object = MibTableColumn
h3cEponDeviceErroredSymbolPeriodEventState = _H3cEponDeviceErroredSymbolPeriodEventState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 1, 1, 14),
    _H3cEponDeviceErroredSymbolPeriodEventState_Type()
)
h3cEponDeviceErroredSymbolPeriodEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceErroredSymbolPeriodEventState.setStatus("current")


class _H3cEponDeviceErroredSymbolPeriodEventEnabled_Type(TruthValue):
    """Custom type h3cEponDeviceErroredSymbolPeriodEventEnabled based on TruthValue"""


_H3cEponDeviceErroredSymbolPeriodEventEnabled_Object = MibTableColumn
h3cEponDeviceErroredSymbolPeriodEventEnabled = _H3cEponDeviceErroredSymbolPeriodEventEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 1, 1, 15),
    _H3cEponDeviceErroredSymbolPeriodEventEnabled_Type()
)
h3cEponDeviceErroredSymbolPeriodEventEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponDeviceErroredSymbolPeriodEventEnabled.setStatus("current")
_H3cEponDeviceErroredFrameEventState_Type = TruthValue
_H3cEponDeviceErroredFrameEventState_Object = MibTableColumn
h3cEponDeviceErroredFrameEventState = _H3cEponDeviceErroredFrameEventState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 1, 1, 16),
    _H3cEponDeviceErroredFrameEventState_Type()
)
h3cEponDeviceErroredFrameEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceErroredFrameEventState.setStatus("current")


class _H3cEponDeviceErroredFrameEventEnabled_Type(TruthValue):
    """Custom type h3cEponDeviceErroredFrameEventEnabled based on TruthValue"""


_H3cEponDeviceErroredFrameEventEnabled_Object = MibTableColumn
h3cEponDeviceErroredFrameEventEnabled = _H3cEponDeviceErroredFrameEventEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 1, 1, 17),
    _H3cEponDeviceErroredFrameEventEnabled_Type()
)
h3cEponDeviceErroredFrameEventEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponDeviceErroredFrameEventEnabled.setStatus("current")
_H3cEponDeviceErroredFramePeriodEventState_Type = TruthValue
_H3cEponDeviceErroredFramePeriodEventState_Object = MibTableColumn
h3cEponDeviceErroredFramePeriodEventState = _H3cEponDeviceErroredFramePeriodEventState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 1, 1, 18),
    _H3cEponDeviceErroredFramePeriodEventState_Type()
)
h3cEponDeviceErroredFramePeriodEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceErroredFramePeriodEventState.setStatus("current")


class _H3cEponDeviceErroredFramePeriodEventEnabled_Type(TruthValue):
    """Custom type h3cEponDeviceErroredFramePeriodEventEnabled based on TruthValue"""


_H3cEponDeviceErroredFramePeriodEventEnabled_Object = MibTableColumn
h3cEponDeviceErroredFramePeriodEventEnabled = _H3cEponDeviceErroredFramePeriodEventEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 1, 1, 19),
    _H3cEponDeviceErroredFramePeriodEventEnabled_Type()
)
h3cEponDeviceErroredFramePeriodEventEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponDeviceErroredFramePeriodEventEnabled.setStatus("current")
_H3cEponDeviceErroredFrameSecondsSummaryEventState_Type = TruthValue
_H3cEponDeviceErroredFrameSecondsSummaryEventState_Object = MibTableColumn
h3cEponDeviceErroredFrameSecondsSummaryEventState = _H3cEponDeviceErroredFrameSecondsSummaryEventState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 1, 1, 20),
    _H3cEponDeviceErroredFrameSecondsSummaryEventState_Type()
)
h3cEponDeviceErroredFrameSecondsSummaryEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceErroredFrameSecondsSummaryEventState.setStatus("current")


class _H3cEponDeviceErroredFrameSecondsSummaryEventEnabled_Type(TruthValue):
    """Custom type h3cEponDeviceErroredFrameSecondsSummaryEventEnabled based on TruthValue"""


_H3cEponDeviceErroredFrameSecondsSummaryEventEnabled_Object = MibTableColumn
h3cEponDeviceErroredFrameSecondsSummaryEventEnabled = _H3cEponDeviceErroredFrameSecondsSummaryEventEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 1, 1, 21),
    _H3cEponDeviceErroredFrameSecondsSummaryEventEnabled_Type()
)
h3cEponDeviceErroredFrameSecondsSummaryEventEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponDeviceErroredFrameSecondsSummaryEventEnabled.setStatus("current")
_H3cEponDeviceOrganizationSpecificEventState_Type = TruthValue
_H3cEponDeviceOrganizationSpecificEventState_Object = MibTableColumn
h3cEponDeviceOrganizationSpecificEventState = _H3cEponDeviceOrganizationSpecificEventState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 1, 1, 22),
    _H3cEponDeviceOrganizationSpecificEventState_Type()
)
h3cEponDeviceOrganizationSpecificEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceOrganizationSpecificEventState.setStatus("current")


class _H3cEponDeviceOrganizationSpecificEventEnabled_Type(TruthValue):
    """Custom type h3cEponDeviceOrganizationSpecificEventEnabled based on TruthValue"""


_H3cEponDeviceOrganizationSpecificEventEnabled_Object = MibTableColumn
h3cEponDeviceOrganizationSpecificEventEnabled = _H3cEponDeviceOrganizationSpecificEventEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 1, 1, 23),
    _H3cEponDeviceOrganizationSpecificEventEnabled_Type()
)
h3cEponDeviceOrganizationSpecificEventEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponDeviceOrganizationSpecificEventEnabled.setStatus("current")


class _H3cEponDeviceEventControl_Type(Integer32):
    """Custom type h3cEponDeviceEventControl based on Integer32"""
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


_H3cEponDeviceEventControl_Type.__name__ = "Integer32"
_H3cEponDeviceEventControl_Object = MibTableColumn
h3cEponDeviceEventControl = _H3cEponDeviceEventControl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 1, 1, 24),
    _H3cEponDeviceEventControl_Type()
)
h3cEponDeviceEventControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponDeviceEventControl.setStatus("current")
_H3cEponDeviceEventsLogTable_Object = MibTable
h3cEponDeviceEventsLogTable = _H3cEponDeviceEventsLogTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    h3cEponDeviceEventsLogTable.setStatus("current")
_H3cEponDeviceEventsLogEntry_Object = MibTableRow
h3cEponDeviceEventsLogEntry = _H3cEponDeviceEventsLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 2, 1)
)
h3cEponDeviceEventsLogEntry.setIndexNames(
    (0, "H3C-EPON-DEVICE-MIB", "h3cEponDeviceEventsLogName"),
    (0, "H3C-EPON-DEVICE-MIB", "h3cEponDeviceEventsLogIndex"),
)
if mibBuilder.loadTexts:
    h3cEponDeviceEventsLogEntry.setStatus("current")


class _H3cEponDeviceEventsLogName_Type(SnmpAdminString):
    """Custom type h3cEponDeviceEventsLogName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_H3cEponDeviceEventsLogName_Type.__name__ = "SnmpAdminString"
_H3cEponDeviceEventsLogName_Object = MibTableColumn
h3cEponDeviceEventsLogName = _H3cEponDeviceEventsLogName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 2, 1, 1),
    _H3cEponDeviceEventsLogName_Type()
)
h3cEponDeviceEventsLogName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEponDeviceEventsLogName.setStatus("current")


class _H3cEponDeviceEventsLogIndex_Type(Unsigned32):
    """Custom type h3cEponDeviceEventsLogIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_H3cEponDeviceEventsLogIndex_Type.__name__ = "Unsigned32"
_H3cEponDeviceEventsLogIndex_Object = MibTableColumn
h3cEponDeviceEventsLogIndex = _H3cEponDeviceEventsLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 2, 1, 2),
    _H3cEponDeviceEventsLogIndex_Type()
)
h3cEponDeviceEventsLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEponDeviceEventsLogIndex.setStatus("current")


class _H3cEponDeviceEventsLogID_Type(ObjectIdentifier):
    """Custom type h3cEponDeviceEventsLogID based on ObjectIdentifier"""
    defaultValue = (0, 0)


_H3cEponDeviceEventsLogID_Object = MibTableColumn
h3cEponDeviceEventsLogID = _H3cEponDeviceEventsLogID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 2, 1, 3),
    _H3cEponDeviceEventsLogID_Type()
)
h3cEponDeviceEventsLogID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponDeviceEventsLogID.setStatus("current")
_H3cEponDeviceEventsLogFirstTime_Type = DateAndTime
_H3cEponDeviceEventsLogFirstTime_Object = MibTableColumn
h3cEponDeviceEventsLogFirstTime = _H3cEponDeviceEventsLogFirstTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 2, 1, 4),
    _H3cEponDeviceEventsLogFirstTime_Type()
)
h3cEponDeviceEventsLogFirstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceEventsLogFirstTime.setStatus("current")
_H3cEponDeviceEventsLogLastTime_Type = DateAndTime
_H3cEponDeviceEventsLogLastTime_Object = MibTableColumn
h3cEponDeviceEventsLogLastTime = _H3cEponDeviceEventsLogLastTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 2, 1, 5),
    _H3cEponDeviceEventsLogLastTime_Type()
)
h3cEponDeviceEventsLogLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceEventsLogLastTime.setStatus("current")
_H3cEponDeviceEventsLogCounts_Type = Counter32
_H3cEponDeviceEventsLogCounts_Object = MibTableColumn
h3cEponDeviceEventsLogCounts = _H3cEponDeviceEventsLogCounts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 2, 1, 6),
    _H3cEponDeviceEventsLogCounts_Type()
)
h3cEponDeviceEventsLogCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceEventsLogCounts.setStatus("current")


class _H3cEponDeviceEventsLogType_Type(Integer32):
    """Custom type h3cEponDeviceEventsLogType based on Integer32"""
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
        *(("h3cEponDeviceCriticalEventState", 2),
          ("h3cEponDeviceDyingGaspAlarmState", 1),
          ("h3cEponDeviceErroredFrameEventState", 8),
          ("h3cEponDeviceErroredFramePeriodEventState", 9),
          ("h3cEponDeviceErroredFrameSecondsSummaryEventState", 10),
          ("h3cEponDeviceErroredSymbolPeriodEventState", 7),
          ("h3cEponDeviceGlobalEventState", 6),
          ("h3cEponDeviceLocalLinkFaultAlarmState", 3),
          ("h3cEponDeviceOrganizationSpecificEventState", 11),
          ("h3cEponDevicePowerVoltageEventIndicationState", 5),
          ("h3cEponDeviceTemperatureEventIndicationState", 4))
    )


_H3cEponDeviceEventsLogType_Type.__name__ = "Integer32"
_H3cEponDeviceEventsLogType_Object = MibTableColumn
h3cEponDeviceEventsLogType = _H3cEponDeviceEventsLogType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 2, 1, 7),
    _H3cEponDeviceEventsLogType_Type()
)
h3cEponDeviceEventsLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponDeviceEventsLogType.setStatus("current")
_H3cEponDeviceEventsLogEntryStatus_Type = RowStatus
_H3cEponDeviceEventsLogEntryStatus_Object = MibTableColumn
h3cEponDeviceEventsLogEntryStatus = _H3cEponDeviceEventsLogEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 1, 3, 2, 1, 8),
    _H3cEponDeviceEventsLogEntryStatus_Type()
)
h3cEponDeviceEventsLogEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponDeviceEventsLogEntryStatus.setStatus("current")
_H3cEponDeviceConformance_ObjectIdentity = ObjectIdentity
h3cEponDeviceConformance = _H3cEponDeviceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 2)
)
_H3cEponDeviceGroups_ObjectIdentity = ObjectIdentity
h3cEponDeviceGroups = _H3cEponDeviceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 2, 1)
)
_H3cEponDeviceCompliances_ObjectIdentity = ObjectIdentity
h3cEponDeviceCompliances = _H3cEponDeviceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 2, 2)
)

# Managed Objects groups

h3cEponDeviceGroupControl = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 2, 1, 1)
)
h3cEponDeviceGroupControl.setObjects(
      *(("H3C-EPON-DEVICE-MIB", "h3cEponDeviceObjectReset"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceObjectModes"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceObjectFecEnabled"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceObjectOamMode"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceObjectDeviceReadyMode"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceObjectPowerDown"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceObjectNumberOfLLIDs"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceObjectReportThreshold"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceRemoteMACAddressLLIDControl"))
)
if mibBuilder.loadTexts:
    h3cEponDeviceGroupControl.setStatus("current")

h3cEponDeviceGroupRMadLTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 2, 1, 2)
)
h3cEponDeviceGroupRMadLTable.setObjects(
      *(("H3C-EPON-DEVICE-MIB", "h3cEponDeviceRMadlLLID"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceRMadlLogID"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceRMadlRemoteAddress"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceRMadlType"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceRMadlAction"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceRMadlEntryStatus"))
)
if mibBuilder.loadTexts:
    h3cEponDeviceGroupRMadLTable.setStatus("current")

h3cEponDeviceGroupStat = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 2, 1, 3)
)
h3cEponDeviceGroupStat.setObjects(
      *(("H3C-EPON-DEVICE-MIB", "h3cEponDeviceStatTxFramesQueue0"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceStatTxFramesQueue1"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceStatTxFramesQueue2"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceStatTxFramesQueue3"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceStatTxFramesQueue4"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceStatTxFramesQueue5"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceStatTxFramesQueue6"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceStatTxFramesQueue7"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceStatRxFramesQueue0"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceStatRxFramesQueue1"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceStatRxFramesQueue2"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceStatRxFramesQueue3"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceStatRxFramesQueue4"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceStatRxFramesQueue5"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceStatRxFramesQueue6"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceStatRxFramesQueue7"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceStatDroppedFramesQueue0"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceStatDroppedFramesQueue1"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceStatDroppedFramesQueue2"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceStatDroppedFramesQueue3"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceStatDroppedFramesQueue4"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceStatDroppedFramesQueue5"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceStatDroppedFramesQueue6"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceStatDroppedFramesQueue7"))
)
if mibBuilder.loadTexts:
    h3cEponDeviceGroupStat.setStatus("current")

h3cEponDeviceGroupEvent = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 2, 1, 4)
)
h3cEponDeviceGroupEvent.setObjects(
      *(("H3C-EPON-DEVICE-MIB", "h3cEponDeviceSampleMinimum"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceDyingGaspAlarmState"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceDyingGaspAlarmEnabled"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceCriticalEventState"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceCriticalEventEnabled"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceLocalLinkFaultAlarmState"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceLocalLinkFaultAlarmEnabled"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceTemperatureEventIndicationState"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceTemperatureEventIndicationEnabled"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDevicePowerVoltageEventIndicationState"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDevicePowerVoltageEventIndicationEnabled"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceGlobalEventState"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceGlobalEventEnabled"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceErroredSymbolPeriodEventState"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceErroredSymbolPeriodEventEnabled"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceErroredFrameEventState"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceErroredFrameEventEnabled"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceErroredFramePeriodEventState"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceErroredFramePeriodEventEnabled"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceErroredFrameSecondsSummaryEventState"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceErroredFrameSecondsSummaryEventEnabled"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceOrganizationSpecificEventState"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceOrganizationSpecificEventEnabled"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceEventControl"))
)
if mibBuilder.loadTexts:
    h3cEponDeviceGroupEvent.setStatus("current")

h3cEponDeviceGroupEventLog = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 2, 1, 5)
)
h3cEponDeviceGroupEventLog.setObjects(
      *(("H3C-EPON-DEVICE-MIB", "h3cEponDeviceEventsLogID"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceEventsLogFirstTime"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceEventsLogLastTime"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceEventsLogCounts"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceEventsLogType"),
        ("H3C-EPON-DEVICE-MIB", "h3cEponDeviceEventsLogEntryStatus"))
)
if mibBuilder.loadTexts:
    h3cEponDeviceGroupEventLog.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

h3cEponDeviceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 4, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    h3cEponDeviceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-EPON-DEVICE-MIB",
    **{"h3cEponDeviceMIB": h3cEponDeviceMIB,
       "h3cEponDeviceObjectMIB": h3cEponDeviceObjectMIB,
       "h3cEponDeviceObjects": h3cEponDeviceObjects,
       "h3cEponDeviceControlObjects": h3cEponDeviceControlObjects,
       "h3cEponDeviceControlTable": h3cEponDeviceControlTable,
       "h3cEponDeviceControlEntry": h3cEponDeviceControlEntry,
       "h3cEponDeviceObjectReset": h3cEponDeviceObjectReset,
       "h3cEponDeviceObjectModes": h3cEponDeviceObjectModes,
       "h3cEponDeviceObjectFecEnabled": h3cEponDeviceObjectFecEnabled,
       "h3cEponDeviceObjectOamMode": h3cEponDeviceObjectOamMode,
       "h3cEponDeviceObjectDeviceReadyMode": h3cEponDeviceObjectDeviceReadyMode,
       "h3cEponDeviceObjectPowerDown": h3cEponDeviceObjectPowerDown,
       "h3cEponDeviceObjectNumberOfLLIDs": h3cEponDeviceObjectNumberOfLLIDs,
       "h3cEponDeviceObjectReportThreshold": h3cEponDeviceObjectReportThreshold,
       "h3cEponDeviceRemoteMACAddressLLIDControl": h3cEponDeviceRemoteMACAddressLLIDControl,
       "h3cEponDeviceRemoteMACAddressLLIDTable": h3cEponDeviceRemoteMACAddressLLIDTable,
       "h3cEponDeviceRemoteMACAddressLLIDEntry": h3cEponDeviceRemoteMACAddressLLIDEntry,
       "h3cEponDeviceRemoteMACAddressLLIDName": h3cEponDeviceRemoteMACAddressLLIDName,
       "h3cEponDeviceRMadlLLID": h3cEponDeviceRMadlLLID,
       "h3cEponDeviceRMadlLogID": h3cEponDeviceRMadlLogID,
       "h3cEponDeviceRMadlRemoteAddress": h3cEponDeviceRMadlRemoteAddress,
       "h3cEponDeviceRMadlType": h3cEponDeviceRMadlType,
       "h3cEponDeviceRMadlAction": h3cEponDeviceRMadlAction,
       "h3cEponDeviceRMadlEntryStatus": h3cEponDeviceRMadlEntryStatus,
       "h3cEponDeviceStatObjects": h3cEponDeviceStatObjects,
       "h3cEponDeviceStatTable": h3cEponDeviceStatTable,
       "h3cEponDeviceStatEntry": h3cEponDeviceStatEntry,
       "h3cEponDeviceStatTxFramesQueue0": h3cEponDeviceStatTxFramesQueue0,
       "h3cEponDeviceStatTxFramesQueue1": h3cEponDeviceStatTxFramesQueue1,
       "h3cEponDeviceStatTxFramesQueue2": h3cEponDeviceStatTxFramesQueue2,
       "h3cEponDeviceStatTxFramesQueue3": h3cEponDeviceStatTxFramesQueue3,
       "h3cEponDeviceStatTxFramesQueue4": h3cEponDeviceStatTxFramesQueue4,
       "h3cEponDeviceStatTxFramesQueue5": h3cEponDeviceStatTxFramesQueue5,
       "h3cEponDeviceStatTxFramesQueue6": h3cEponDeviceStatTxFramesQueue6,
       "h3cEponDeviceStatTxFramesQueue7": h3cEponDeviceStatTxFramesQueue7,
       "h3cEponDeviceStatRxFramesQueue0": h3cEponDeviceStatRxFramesQueue0,
       "h3cEponDeviceStatRxFramesQueue1": h3cEponDeviceStatRxFramesQueue1,
       "h3cEponDeviceStatRxFramesQueue2": h3cEponDeviceStatRxFramesQueue2,
       "h3cEponDeviceStatRxFramesQueue3": h3cEponDeviceStatRxFramesQueue3,
       "h3cEponDeviceStatRxFramesQueue4": h3cEponDeviceStatRxFramesQueue4,
       "h3cEponDeviceStatRxFramesQueue5": h3cEponDeviceStatRxFramesQueue5,
       "h3cEponDeviceStatRxFramesQueue6": h3cEponDeviceStatRxFramesQueue6,
       "h3cEponDeviceStatRxFramesQueue7": h3cEponDeviceStatRxFramesQueue7,
       "h3cEponDeviceStatDroppedFramesQueue0": h3cEponDeviceStatDroppedFramesQueue0,
       "h3cEponDeviceStatDroppedFramesQueue1": h3cEponDeviceStatDroppedFramesQueue1,
       "h3cEponDeviceStatDroppedFramesQueue2": h3cEponDeviceStatDroppedFramesQueue2,
       "h3cEponDeviceStatDroppedFramesQueue3": h3cEponDeviceStatDroppedFramesQueue3,
       "h3cEponDeviceStatDroppedFramesQueue4": h3cEponDeviceStatDroppedFramesQueue4,
       "h3cEponDeviceStatDroppedFramesQueue5": h3cEponDeviceStatDroppedFramesQueue5,
       "h3cEponDeviceStatDroppedFramesQueue6": h3cEponDeviceStatDroppedFramesQueue6,
       "h3cEponDeviceStatDroppedFramesQueue7": h3cEponDeviceStatDroppedFramesQueue7,
       "h3cEponDeviceEventObjects": h3cEponDeviceEventObjects,
       "h3cEponDeviceEventObjectTable": h3cEponDeviceEventObjectTable,
       "h3cEponDeviceEventObjectEntry": h3cEponDeviceEventObjectEntry,
       "h3cEponDeviceSampleMinimum": h3cEponDeviceSampleMinimum,
       "h3cEponDeviceDyingGaspAlarmState": h3cEponDeviceDyingGaspAlarmState,
       "h3cEponDeviceDyingGaspAlarmEnabled": h3cEponDeviceDyingGaspAlarmEnabled,
       "h3cEponDeviceCriticalEventState": h3cEponDeviceCriticalEventState,
       "h3cEponDeviceCriticalEventEnabled": h3cEponDeviceCriticalEventEnabled,
       "h3cEponDeviceLocalLinkFaultAlarmState": h3cEponDeviceLocalLinkFaultAlarmState,
       "h3cEponDeviceLocalLinkFaultAlarmEnabled": h3cEponDeviceLocalLinkFaultAlarmEnabled,
       "h3cEponDeviceTemperatureEventIndicationState": h3cEponDeviceTemperatureEventIndicationState,
       "h3cEponDeviceTemperatureEventIndicationEnabled": h3cEponDeviceTemperatureEventIndicationEnabled,
       "h3cEponDevicePowerVoltageEventIndicationState": h3cEponDevicePowerVoltageEventIndicationState,
       "h3cEponDevicePowerVoltageEventIndicationEnabled": h3cEponDevicePowerVoltageEventIndicationEnabled,
       "h3cEponDeviceGlobalEventState": h3cEponDeviceGlobalEventState,
       "h3cEponDeviceGlobalEventEnabled": h3cEponDeviceGlobalEventEnabled,
       "h3cEponDeviceErroredSymbolPeriodEventState": h3cEponDeviceErroredSymbolPeriodEventState,
       "h3cEponDeviceErroredSymbolPeriodEventEnabled": h3cEponDeviceErroredSymbolPeriodEventEnabled,
       "h3cEponDeviceErroredFrameEventState": h3cEponDeviceErroredFrameEventState,
       "h3cEponDeviceErroredFrameEventEnabled": h3cEponDeviceErroredFrameEventEnabled,
       "h3cEponDeviceErroredFramePeriodEventState": h3cEponDeviceErroredFramePeriodEventState,
       "h3cEponDeviceErroredFramePeriodEventEnabled": h3cEponDeviceErroredFramePeriodEventEnabled,
       "h3cEponDeviceErroredFrameSecondsSummaryEventState": h3cEponDeviceErroredFrameSecondsSummaryEventState,
       "h3cEponDeviceErroredFrameSecondsSummaryEventEnabled": h3cEponDeviceErroredFrameSecondsSummaryEventEnabled,
       "h3cEponDeviceOrganizationSpecificEventState": h3cEponDeviceOrganizationSpecificEventState,
       "h3cEponDeviceOrganizationSpecificEventEnabled": h3cEponDeviceOrganizationSpecificEventEnabled,
       "h3cEponDeviceEventControl": h3cEponDeviceEventControl,
       "h3cEponDeviceEventsLogTable": h3cEponDeviceEventsLogTable,
       "h3cEponDeviceEventsLogEntry": h3cEponDeviceEventsLogEntry,
       "h3cEponDeviceEventsLogName": h3cEponDeviceEventsLogName,
       "h3cEponDeviceEventsLogIndex": h3cEponDeviceEventsLogIndex,
       "h3cEponDeviceEventsLogID": h3cEponDeviceEventsLogID,
       "h3cEponDeviceEventsLogFirstTime": h3cEponDeviceEventsLogFirstTime,
       "h3cEponDeviceEventsLogLastTime": h3cEponDeviceEventsLogLastTime,
       "h3cEponDeviceEventsLogCounts": h3cEponDeviceEventsLogCounts,
       "h3cEponDeviceEventsLogType": h3cEponDeviceEventsLogType,
       "h3cEponDeviceEventsLogEntryStatus": h3cEponDeviceEventsLogEntryStatus,
       "h3cEponDeviceConformance": h3cEponDeviceConformance,
       "h3cEponDeviceGroups": h3cEponDeviceGroups,
       "h3cEponDeviceGroupControl": h3cEponDeviceGroupControl,
       "h3cEponDeviceGroupRMadLTable": h3cEponDeviceGroupRMadLTable,
       "h3cEponDeviceGroupStat": h3cEponDeviceGroupStat,
       "h3cEponDeviceGroupEvent": h3cEponDeviceGroupEvent,
       "h3cEponDeviceGroupEventLog": h3cEponDeviceGroupEventLog,
       "h3cEponDeviceCompliances": h3cEponDeviceCompliances,
       "h3cEponDeviceCompliance": h3cEponDeviceCompliance}
)
