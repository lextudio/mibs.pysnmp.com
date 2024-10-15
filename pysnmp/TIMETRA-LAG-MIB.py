# SNMP MIB module (TIMETRA-LAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-LAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:02:44 2024
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

(dot3adAggPortEntry,) = mibBuilder.importSymbols(
    "IEEE8023-LAG-MIB",
    "dot3adAggPortEntry")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(tmnxPortLagId,
 tmnxPortPortID) = mibBuilder.importSymbols(
    "TIMETRA-PORT-MIB",
    "tmnxPortLagId",
    "tmnxPortPortID")

(TItemLongDescription,
 TNamedItemOrEmpty,
 TmnxPortID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemLongDescription",
    "TNamedItemOrEmpty",
    "TmnxPortID")


# MODULE-IDENTITY

timetraLagMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 15)
)
timetraLagMIBModule.setRevisions(
        ("1912-04-06 00:00",
         "1911-02-01 00:00",
         "1909-02-28 00:00",
         "1908-07-01 00:00",
         "1908-01-01 00:00",
         "1907-01-01 00:00",
         "1906-03-15 00:00",
         "1905-08-31 00:00",
         "1905-01-24 00:00",
         "1904-01-15 00:00",
         "1903-08-15 00:00",
         "2003-01-20 00:00",
         "2001-02-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LAGInterfaceNumber(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )



class LAGSubgroup(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 8),
    )



# MIB Managed Objects in the order of their OIDs

_TmnxLagConformance_ObjectIdentity = ObjectIdentity
tmnxLagConformance = _TmnxLagConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15)
)
_TmnxLagCompliances_ObjectIdentity = ObjectIdentity
tmnxLagCompliances = _TmnxLagCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 1)
)
_TmnxLagGroups_ObjectIdentity = ObjectIdentity
tmnxLagGroups = _TmnxLagGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2)
)
_TLagObjects_ObjectIdentity = ObjectIdentity
tLagObjects = _TLagObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15)
)
_TLagConfigTable_Object = MibTable
tLagConfigTable = _TLagConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2)
)
if mibBuilder.loadTexts:
    tLagConfigTable.setStatus("current")
_TLagConfigEntry_Object = MibTableRow
tLagConfigEntry = _TLagConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1)
)
tLagConfigEntry.setIndexNames(
    (0, "TIMETRA-LAG-MIB", "tLagIndex"),
)
if mibBuilder.loadTexts:
    tLagConfigEntry.setStatus("current")
_TLagIndex_Type = LAGInterfaceNumber
_TLagIndex_Object = MibTableColumn
tLagIndex = _TLagIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 1),
    _TLagIndex_Type()
)
tLagIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tLagIndex.setStatus("current")
_TLagRowStatus_Type = RowStatus
_TLagRowStatus_Object = MibTableColumn
tLagRowStatus = _TLagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 2),
    _TLagRowStatus_Type()
)
tLagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagRowStatus.setStatus("current")


class _TLagPortThreshold_Type(Integer32):
    """Custom type tLagPortThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_TLagPortThreshold_Type.__name__ = "Integer32"
_TLagPortThreshold_Object = MibTableColumn
tLagPortThreshold = _TLagPortThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 3),
    _TLagPortThreshold_Type()
)
tLagPortThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagPortThreshold.setStatus("current")


class _TLagPortThresholdAction_Type(Integer32):
    """Custom type tLagPortThresholdAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("dynamicCost", 2))
    )


_TLagPortThresholdAction_Type.__name__ = "Integer32"
_TLagPortThresholdAction_Object = MibTableColumn
tLagPortThresholdAction = _TLagPortThresholdAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 4),
    _TLagPortThresholdAction_Type()
)
tLagPortThresholdAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagPortThresholdAction.setStatus("current")


class _TLagEnableMarkerGenerator_Type(TruthValue):
    """Custom type tLagEnableMarkerGenerator based on TruthValue"""


_TLagEnableMarkerGenerator_Object = MibTableColumn
tLagEnableMarkerGenerator = _TLagEnableMarkerGenerator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 5),
    _TLagEnableMarkerGenerator_Type()
)
tLagEnableMarkerGenerator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagEnableMarkerGenerator.setStatus("current")


class _TLagEnableLACP_Type(TruthValue):
    """Custom type tLagEnableLACP based on TruthValue"""


_TLagEnableLACP_Object = MibTableColumn
tLagEnableLACP = _TLagEnableLACP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 6),
    _TLagEnableLACP_Type()
)
tLagEnableLACP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagEnableLACP.setStatus("current")


class _TLagDescription_Type(TItemLongDescription):
    """Custom type tLagDescription based on TItemLongDescription"""
    defaultHexValue = ""


_TLagDescription_Object = MibTableColumn
tLagDescription = _TLagDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 7),
    _TLagDescription_Type()
)
tLagDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagDescription.setStatus("current")


class _TLagDynamicCosting_Type(TruthValue):
    """Custom type tLagDynamicCosting based on TruthValue"""


_TLagDynamicCosting_Object = MibTableColumn
tLagDynamicCosting = _TLagDynamicCosting_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 8),
    _TLagDynamicCosting_Type()
)
tLagDynamicCosting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagDynamicCosting.setStatus("current")


class _TLagLACPMode_Type(Integer32):
    """Custom type tLagLACPMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("passive", 1))
    )


_TLagLACPMode_Type.__name__ = "Integer32"
_TLagLACPMode_Object = MibTableColumn
tLagLACPMode = _TLagLACPMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 9),
    _TLagLACPMode_Type()
)
tLagLACPMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagLACPMode.setStatus("current")


class _TLagLACPAdminKeyAutogen_Type(TruthValue):
    """Custom type tLagLACPAdminKeyAutogen based on TruthValue"""


_TLagLACPAdminKeyAutogen_Object = MibTableColumn
tLagLACPAdminKeyAutogen = _TLagLACPAdminKeyAutogen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 10),
    _TLagLACPAdminKeyAutogen_Type()
)
tLagLACPAdminKeyAutogen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagLACPAdminKeyAutogen.setStatus("current")


class _TLagLACPTransmitInterval_Type(Integer32):
    """Custom type tLagLACPTransmitInterval based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fast", 2),
          ("slow", 1))
    )


_TLagLACPTransmitInterval_Type.__name__ = "Integer32"
_TLagLACPTransmitInterval_Object = MibTableColumn
tLagLACPTransmitInterval = _TLagLACPTransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 11),
    _TLagLACPTransmitInterval_Type()
)
tLagLACPTransmitInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagLACPTransmitInterval.setStatus("current")


class _TLagAccessAdaptQos_Type(Integer32):
    """Custom type tLagAccessAdaptQos based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("distribute", 2),
          ("link", 1))
    )


_TLagAccessAdaptQos_Type.__name__ = "Integer32"
_TLagAccessAdaptQos_Object = MibTableColumn
tLagAccessAdaptQos = _TLagAccessAdaptQos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 12),
    _TLagAccessAdaptQos_Type()
)
tLagAccessAdaptQos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagAccessAdaptQos.setStatus("current")


class _TLagLACPXmitStdby_Type(TruthValue):
    """Custom type tLagLACPXmitStdby based on TruthValue"""


_TLagLACPXmitStdby_Object = MibTableColumn
tLagLACPXmitStdby = _TLagLACPXmitStdby_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 13),
    _TLagLACPXmitStdby_Type()
)
tLagLACPXmitStdby.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagLACPXmitStdby.setStatus("current")


class _TLagLACPSelCrit_Type(Integer32):
    """Custom type tLagLACPSelCrit based on Integer32"""
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
        *(("bestPort", 3),
          ("highest-count", 1),
          ("highest-weight", 2))
    )


_TLagLACPSelCrit_Type.__name__ = "Integer32"
_TLagLACPSelCrit_Object = MibTableColumn
tLagLACPSelCrit = _TLagLACPSelCrit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 14),
    _TLagLACPSelCrit_Type()
)
tLagLACPSelCrit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagLACPSelCrit.setStatus("current")


class _TLagLACPSelCritSlaveToPartner_Type(TruthValue):
    """Custom type tLagLACPSelCritSlaveToPartner based on TruthValue"""


_TLagLACPSelCritSlaveToPartner_Object = MibTableColumn
tLagLACPSelCritSlaveToPartner = _TLagLACPSelCritSlaveToPartner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 15),
    _TLagLACPSelCritSlaveToPartner_Type()
)
tLagLACPSelCritSlaveToPartner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagLACPSelCritSlaveToPartner.setStatus("current")
_TLagLACPNbrOfSubGroups_Type = Unsigned32
_TLagLACPNbrOfSubGroups_Object = MibTableColumn
tLagLACPNbrOfSubGroups = _TLagLACPNbrOfSubGroups_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 16),
    _TLagLACPNbrOfSubGroups_Type()
)
tLagLACPNbrOfSubGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagLACPNbrOfSubGroups.setStatus("current")


class _TLagholdTimeDown_Type(Unsigned32):
    """Custom type tLagholdTimeDown based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_TLagholdTimeDown_Type.__name__ = "Unsigned32"
_TLagholdTimeDown_Object = MibTableColumn
tLagholdTimeDown = _TLagholdTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 17),
    _TLagholdTimeDown_Type()
)
tLagholdTimeDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagholdTimeDown.setStatus("current")
if mibBuilder.loadTexts:
    tLagholdTimeDown.setUnits("100s of milliseconds")


class _TLagPortType_Type(Integer32):
    """Custom type tLagPortType based on Integer32"""
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
        *(("hsmda", 2),
          ("hsmdaV2", 3),
          ("standard", 1))
    )


_TLagPortType_Type.__name__ = "Integer32"
_TLagPortType_Object = MibTableColumn
tLagPortType = _TLagPortType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 18),
    _TLagPortType_Type()
)
tLagPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagPortType.setStatus("current")


class _TLagPerFpIngQueuing_Type(TruthValue):
    """Custom type tLagPerFpIngQueuing based on TruthValue"""


_TLagPerFpIngQueuing_Object = MibTableColumn
tLagPerFpIngQueuing = _TLagPerFpIngQueuing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 19),
    _TLagPerFpIngQueuing_Type()
)
tLagPerFpIngQueuing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagPerFpIngQueuing.setStatus("current")


class _TLagSystemId_Type(MacAddress):
    """Custom type tLagSystemId based on MacAddress"""
    defaultHexValue = "000000000000"


_TLagSystemId_Object = MibTableColumn
tLagSystemId = _TLagSystemId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 20),
    _TLagSystemId_Type()
)
tLagSystemId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagSystemId.setStatus("current")


class _TLagSystemPriority_Type(Integer32):
    """Custom type tLagSystemPriority based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_TLagSystemPriority_Type.__name__ = "Integer32"
_TLagSystemPriority_Object = MibTableColumn
tLagSystemPriority = _TLagSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 21),
    _TLagSystemPriority_Type()
)
tLagSystemPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagSystemPriority.setStatus("current")


class _TLagStandbySignaling_Type(Integer32):
    """Custom type tLagStandbySignaling based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lacp", 1),
          ("powerOff", 2))
    )


_TLagStandbySignaling_Type.__name__ = "Integer32"
_TLagStandbySignaling_Object = MibTableColumn
tLagStandbySignaling = _TLagStandbySignaling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 2, 1, 22),
    _TLagStandbySignaling_Type()
)
tLagStandbySignaling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tLagStandbySignaling.setStatus("current")
_TLagOperationTable_Object = MibTable
tLagOperationTable = _TLagOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 3)
)
if mibBuilder.loadTexts:
    tLagOperationTable.setStatus("current")
_TLagOperationEntry_Object = MibTableRow
tLagOperationEntry = _TLagOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 3, 1)
)
if mibBuilder.loadTexts:
    tLagOperationEntry.setStatus("current")
_TLagIfIndex_Type = InterfaceIndexOrZero
_TLagIfIndex_Object = MibTableColumn
tLagIfIndex = _TLagIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 3, 1, 1),
    _TLagIfIndex_Type()
)
tLagIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagIfIndex.setStatus("current")
_TLagConfigLastChange_Type = TimeStamp
_TLagConfigLastChange_Object = MibTableColumn
tLagConfigLastChange = _TLagConfigLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 3, 1, 2),
    _TLagConfigLastChange_Type()
)
tLagConfigLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagConfigLastChange.setStatus("current")
_TLagPortThresholdFalling_Type = Counter32
_TLagPortThresholdFalling_Object = MibTableColumn
tLagPortThresholdFalling = _TLagPortThresholdFalling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 3, 1, 3),
    _TLagPortThresholdFalling_Type()
)
tLagPortThresholdFalling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagPortThresholdFalling.setStatus("current")
_TLagPortThresholdRising_Type = Counter32
_TLagPortThresholdRising_Object = MibTableColumn
tLagPortThresholdRising = _TLagPortThresholdRising_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 3, 1, 4),
    _TLagPortThresholdRising_Type()
)
tLagPortThresholdRising.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagPortThresholdRising.setStatus("current")
_TLagLACPPrimaryPort_Type = TmnxPortID
_TLagLACPPrimaryPort_Object = MibTableColumn
tLagLACPPrimaryPort = _TLagLACPPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 3, 1, 5),
    _TLagLACPPrimaryPort_Type()
)
tLagLACPPrimaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagLACPPrimaryPort.setStatus("obsolete")


class _TLagPortReasonDownFlags_Type(Bits):
    """Custom type tLagPortReasonDownFlags based on Bits"""
    namedValues = NamedValues(
        *(("linklossFwd", 1),
          ("unknown", 0))
    )

_TLagPortReasonDownFlags_Type.__name__ = "Bits"
_TLagPortReasonDownFlags_Object = MibTableColumn
tLagPortReasonDownFlags = _TLagPortReasonDownFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 3, 1, 6),
    _TLagPortReasonDownFlags_Type()
)
tLagPortReasonDownFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagPortReasonDownFlags.setStatus("obsolete")
_TLagNotificationObjects_ObjectIdentity = ObjectIdentity
tLagNotificationObjects = _TLagNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 4)
)


class _TLagNotifyPortAddFailReason_Type(Integer32):
    """Custom type tLagNotifyPortAddFailReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("adminkey-mismatch", 1),
          ("lacp-passive-both-ends", 3),
          ("link-down", 4),
          ("sysid-mismatch", 2),
          ("unknown", 0))
    )


_TLagNotifyPortAddFailReason_Type.__name__ = "Integer32"
_TLagNotifyPortAddFailReason_Object = MibScalar
tLagNotifyPortAddFailReason = _TLagNotifyPortAddFailReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 4, 1),
    _TLagNotifyPortAddFailReason_Type()
)
tLagNotifyPortAddFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tLagNotifyPortAddFailReason.setStatus("current")
_TLagNotifySubGroupSelected_Type = DisplayString
_TLagNotifySubGroupSelected_Object = MibScalar
tLagNotifySubGroupSelected = _TLagNotifySubGroupSelected_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 4, 2),
    _TLagNotifySubGroupSelected_Type()
)
tLagNotifySubGroupSelected.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tLagNotifySubGroupSelected.setStatus("current")
_TLagNotifyAdditionalInfo_Type = DisplayString
_TLagNotifyAdditionalInfo_Object = MibScalar
tLagNotifyAdditionalInfo = _TLagNotifyAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 4, 3),
    _TLagNotifyAdditionalInfo_Type()
)
tLagNotifyAdditionalInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tLagNotifyAdditionalInfo.setStatus("current")


class _TLagNotifyStateChangedReason_Type(Integer32):
    """Custom type tLagNotifyStateChangedReason based on Integer32"""
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
        *(("dot1ag-state-changed", 5),
          ("efm-oam-state-changed", 4),
          ("lacp-expired", 2),
          ("lacp-rx-state-machine", 3),
          ("partner-oper-state-changed", 1))
    )


_TLagNotifyStateChangedReason_Type.__name__ = "Integer32"
_TLagNotifyStateChangedReason_Object = MibScalar
tLagNotifyStateChangedReason = _TLagNotifyStateChangedReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 4, 4),
    _TLagNotifyStateChangedReason_Type()
)
tLagNotifyStateChangedReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tLagNotifyStateChangedReason.setStatus("current")
_TLagMemberTable_Object = MibTable
tLagMemberTable = _TLagMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 5)
)
if mibBuilder.loadTexts:
    tLagMemberTable.setStatus("current")
_TLagMemberEntry_Object = MibTableRow
tLagMemberEntry = _TLagMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 5, 1)
)
tLagMemberEntry.setIndexNames(
    (0, "TIMETRA-LAG-MIB", "tLagIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tLagMemberEntry.setStatus("current")
_TLagMemberPortName_Type = TNamedItemOrEmpty
_TLagMemberPortName_Object = MibTableColumn
tLagMemberPortName = _TLagMemberPortName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 5, 1, 1),
    _TLagMemberPortName_Type()
)
tLagMemberPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagMemberPortName.setStatus("current")
_TLagMemberPortIsPrimary_Type = TruthValue
_TLagMemberPortIsPrimary_Object = MibTableColumn
tLagMemberPortIsPrimary = _TLagMemberPortIsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 5, 1, 2),
    _TLagMemberPortIsPrimary_Type()
)
tLagMemberPortIsPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagMemberPortIsPrimary.setStatus("current")
_TLagPortTable_Object = MibTable
tLagPortTable = _TLagPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 6)
)
if mibBuilder.loadTexts:
    tLagPortTable.setStatus("current")
_TLagPortEntry_Object = MibTableRow
tLagPortEntry = _TLagPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 6, 1)
)
if mibBuilder.loadTexts:
    tLagPortEntry.setStatus("current")


class _TLagPortSubgroup_Type(LAGSubgroup):
    """Custom type tLagPortSubgroup based on LAGSubgroup"""
    defaultValue = 1


_TLagPortSubgroup_Object = MibTableColumn
tLagPortSubgroup = _TLagPortSubgroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 6, 1, 1),
    _TLagPortSubgroup_Type()
)
tLagPortSubgroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tLagPortSubgroup.setStatus("current")


class _TLagPortActiveStdby_Type(Integer32):
    """Custom type tLagPortActiveStdby based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("stand-by", 2))
    )


_TLagPortActiveStdby_Type.__name__ = "Integer32"
_TLagPortActiveStdby_Object = MibTableColumn
tLagPortActiveStdby = _TLagPortActiveStdby_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 15, 6, 1, 2),
    _TLagPortActiveStdby_Type()
)
tLagPortActiveStdby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLagPortActiveStdby.setStatus("current")
_TLagNotifyPrefix_ObjectIdentity = ObjectIdentity
tLagNotifyPrefix = _TLagNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 15)
)
_TLagNotifications_ObjectIdentity = ObjectIdentity
tLagNotifications = _TLagNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 15, 0)
)
tLagConfigEntry.registerAugmentions(
    ("TIMETRA-LAG-MIB",
     "tLagOperationEntry")
)
tLagOperationEntry.setIndexNames(*tLagConfigEntry.getIndexNames())
dot3adAggPortEntry.registerAugmentions(
    ("TIMETRA-LAG-MIB",
     "tLagPortEntry")
)
tLagPortEntry.setIndexNames(*dot3adAggPortEntry.getIndexNames())

# Managed Objects groups

tmnxLagNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 2)
)
tmnxLagNotifyObjsGroup.setObjects(
    ("TIMETRA-LAG-MIB", "tLagNotifyPortAddFailReason")
)
if mibBuilder.loadTexts:
    tmnxLagNotifyObjsGroup.setStatus("obsolete")

tmnxLagInstanceV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 5)
)
tmnxLagInstanceV4v0Group.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagRowStatus"),
        ("TIMETRA-LAG-MIB", "tLagPortThreshold"),
        ("TIMETRA-LAG-MIB", "tLagPortThresholdAction"),
        ("TIMETRA-LAG-MIB", "tLagEnableMarkerGenerator"),
        ("TIMETRA-LAG-MIB", "tLagEnableLACP"),
        ("TIMETRA-LAG-MIB", "tLagDescription"),
        ("TIMETRA-LAG-MIB", "tLagDynamicCosting"),
        ("TIMETRA-LAG-MIB", "tLagLACPMode"),
        ("TIMETRA-LAG-MIB", "tLagLACPAdminKeyAutogen"),
        ("TIMETRA-LAG-MIB", "tLagLACPTransmitInterval"),
        ("TIMETRA-LAG-MIB", "tLagAccessAdaptQos"),
        ("TIMETRA-LAG-MIB", "tLagLACPXmitStdby"),
        ("TIMETRA-LAG-MIB", "tLagLACPSelCrit"),
        ("TIMETRA-LAG-MIB", "tLagLACPSelCritSlaveToPartner"),
        ("TIMETRA-LAG-MIB", "tLagLACPNbrOfSubGroups"),
        ("TIMETRA-LAG-MIB", "tLagholdTimeDown"),
        ("TIMETRA-LAG-MIB", "tLagIfIndex"),
        ("TIMETRA-LAG-MIB", "tLagConfigLastChange"),
        ("TIMETRA-LAG-MIB", "tLagPortThresholdFalling"),
        ("TIMETRA-LAG-MIB", "tLagPortThresholdRising"),
        ("TIMETRA-LAG-MIB", "tLagMemberPortName"),
        ("TIMETRA-LAG-MIB", "tLagMemberPortIsPrimary"),
        ("TIMETRA-LAG-MIB", "tLagPortSubgroup"),
        ("TIMETRA-LAG-MIB", "tLagPortActiveStdby"))
)
if mibBuilder.loadTexts:
    tmnxLagInstanceV4v0Group.setStatus("obsolete")

tmnxObsoletedObjectsV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 6)
)
tmnxObsoletedObjectsV4v0Group.setObjects(
    ("TIMETRA-LAG-MIB", "tLagLACPPrimaryPort")
)
if mibBuilder.loadTexts:
    tmnxObsoletedObjectsV4v0Group.setStatus("current")

tmnxLagInstanceV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 7)
)
tmnxLagInstanceV5v0Group.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagRowStatus"),
        ("TIMETRA-LAG-MIB", "tLagPortThreshold"),
        ("TIMETRA-LAG-MIB", "tLagPortThresholdAction"),
        ("TIMETRA-LAG-MIB", "tLagEnableMarkerGenerator"),
        ("TIMETRA-LAG-MIB", "tLagEnableLACP"),
        ("TIMETRA-LAG-MIB", "tLagDescription"),
        ("TIMETRA-LAG-MIB", "tLagDynamicCosting"),
        ("TIMETRA-LAG-MIB", "tLagLACPMode"),
        ("TIMETRA-LAG-MIB", "tLagLACPAdminKeyAutogen"),
        ("TIMETRA-LAG-MIB", "tLagLACPTransmitInterval"),
        ("TIMETRA-LAG-MIB", "tLagAccessAdaptQos"),
        ("TIMETRA-LAG-MIB", "tLagLACPXmitStdby"),
        ("TIMETRA-LAG-MIB", "tLagLACPSelCrit"),
        ("TIMETRA-LAG-MIB", "tLagLACPSelCritSlaveToPartner"),
        ("TIMETRA-LAG-MIB", "tLagLACPNbrOfSubGroups"),
        ("TIMETRA-LAG-MIB", "tLagholdTimeDown"),
        ("TIMETRA-LAG-MIB", "tLagIfIndex"),
        ("TIMETRA-LAG-MIB", "tLagConfigLastChange"),
        ("TIMETRA-LAG-MIB", "tLagPortThresholdFalling"),
        ("TIMETRA-LAG-MIB", "tLagPortThresholdRising"),
        ("TIMETRA-LAG-MIB", "tLagMemberPortName"),
        ("TIMETRA-LAG-MIB", "tLagMemberPortIsPrimary"),
        ("TIMETRA-LAG-MIB", "tLagPortSubgroup"),
        ("TIMETRA-LAG-MIB", "tLagPortActiveStdby"))
)
if mibBuilder.loadTexts:
    tmnxLagInstanceV5v0Group.setStatus("obsolete")

tmnxLagNotifyObjsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 9)
)
tmnxLagNotifyObjsV5v0Group.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagNotifyPortAddFailReason"),
        ("TIMETRA-LAG-MIB", "tLagNotifySubGroupSelected"))
)
if mibBuilder.loadTexts:
    tmnxLagNotifyObjsV5v0Group.setStatus("obsolete")

tmnxLagHsmdaV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 10)
)
tmnxLagHsmdaV6v0Group.setObjects(
    ("TIMETRA-LAG-MIB", "tLagPortType")
)
if mibBuilder.loadTexts:
    tmnxLagHsmdaV6v0Group.setStatus("current")

tmnxLagInstanceV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 11)
)
tmnxLagInstanceV6v0Group.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagRowStatus"),
        ("TIMETRA-LAG-MIB", "tLagPortThreshold"),
        ("TIMETRA-LAG-MIB", "tLagPortThresholdAction"),
        ("TIMETRA-LAG-MIB", "tLagEnableMarkerGenerator"),
        ("TIMETRA-LAG-MIB", "tLagEnableLACP"),
        ("TIMETRA-LAG-MIB", "tLagDescription"),
        ("TIMETRA-LAG-MIB", "tLagDynamicCosting"),
        ("TIMETRA-LAG-MIB", "tLagLACPMode"),
        ("TIMETRA-LAG-MIB", "tLagLACPAdminKeyAutogen"),
        ("TIMETRA-LAG-MIB", "tLagLACPTransmitInterval"),
        ("TIMETRA-LAG-MIB", "tLagAccessAdaptQos"),
        ("TIMETRA-LAG-MIB", "tLagLACPXmitStdby"),
        ("TIMETRA-LAG-MIB", "tLagLACPSelCrit"),
        ("TIMETRA-LAG-MIB", "tLagLACPSelCritSlaveToPartner"),
        ("TIMETRA-LAG-MIB", "tLagLACPNbrOfSubGroups"),
        ("TIMETRA-LAG-MIB", "tLagholdTimeDown"),
        ("TIMETRA-LAG-MIB", "tLagIfIndex"),
        ("TIMETRA-LAG-MIB", "tLagConfigLastChange"),
        ("TIMETRA-LAG-MIB", "tLagPortThresholdFalling"),
        ("TIMETRA-LAG-MIB", "tLagPortThresholdRising"),
        ("TIMETRA-LAG-MIB", "tLagMemberPortName"),
        ("TIMETRA-LAG-MIB", "tLagMemberPortIsPrimary"),
        ("TIMETRA-LAG-MIB", "tLagPortSubgroup"),
        ("TIMETRA-LAG-MIB", "tLagPortActiveStdby"),
        ("TIMETRA-LAG-MIB", "tLagPortReasonDownFlags"))
)
if mibBuilder.loadTexts:
    tmnxLagInstanceV6v0Group.setStatus("obsolete")

tmnxLagV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 13)
)
tmnxLagV7v0Group.setObjects(
    ("TIMETRA-LAG-MIB", "tLagPerFpIngQueuing")
)
if mibBuilder.loadTexts:
    tmnxLagV7v0Group.setStatus("obsolete")

tmnxObsoletedObjectsV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 14)
)
tmnxObsoletedObjectsV7v0Group.setObjects(
    ("TIMETRA-LAG-MIB", "tLagPortReasonDownFlags")
)
if mibBuilder.loadTexts:
    tmnxObsoletedObjectsV7v0Group.setStatus("current")

tmnxLagInstanceV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 15)
)
tmnxLagInstanceV7v0Group.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagRowStatus"),
        ("TIMETRA-LAG-MIB", "tLagPortThreshold"),
        ("TIMETRA-LAG-MIB", "tLagPortThresholdAction"),
        ("TIMETRA-LAG-MIB", "tLagEnableMarkerGenerator"),
        ("TIMETRA-LAG-MIB", "tLagEnableLACP"),
        ("TIMETRA-LAG-MIB", "tLagDescription"),
        ("TIMETRA-LAG-MIB", "tLagDynamicCosting"),
        ("TIMETRA-LAG-MIB", "tLagLACPMode"),
        ("TIMETRA-LAG-MIB", "tLagLACPAdminKeyAutogen"),
        ("TIMETRA-LAG-MIB", "tLagLACPTransmitInterval"),
        ("TIMETRA-LAG-MIB", "tLagAccessAdaptQos"),
        ("TIMETRA-LAG-MIB", "tLagLACPXmitStdby"),
        ("TIMETRA-LAG-MIB", "tLagLACPSelCrit"),
        ("TIMETRA-LAG-MIB", "tLagLACPSelCritSlaveToPartner"),
        ("TIMETRA-LAG-MIB", "tLagLACPNbrOfSubGroups"),
        ("TIMETRA-LAG-MIB", "tLagholdTimeDown"),
        ("TIMETRA-LAG-MIB", "tLagIfIndex"),
        ("TIMETRA-LAG-MIB", "tLagConfigLastChange"),
        ("TIMETRA-LAG-MIB", "tLagPortThresholdFalling"),
        ("TIMETRA-LAG-MIB", "tLagPortThresholdRising"),
        ("TIMETRA-LAG-MIB", "tLagMemberPortName"),
        ("TIMETRA-LAG-MIB", "tLagMemberPortIsPrimary"),
        ("TIMETRA-LAG-MIB", "tLagPortSubgroup"),
        ("TIMETRA-LAG-MIB", "tLagPortActiveStdby"))
)
if mibBuilder.loadTexts:
    tmnxLagInstanceV7v0Group.setStatus("current")

tmnxLagV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 16)
)
tmnxLagV8v0Group.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagPerFpIngQueuing"),
        ("TIMETRA-LAG-MIB", "tLagSystemId"),
        ("TIMETRA-LAG-MIB", "tLagSystemPriority"))
)
if mibBuilder.loadTexts:
    tmnxLagV8v0Group.setStatus("current")

tmnxLagInstanceV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 17)
)
tmnxLagInstanceV9v0Group.setObjects(
    ("TIMETRA-LAG-MIB", "tLagStandbySignaling")
)
if mibBuilder.loadTexts:
    tmnxLagInstanceV9v0Group.setStatus("current")

tmnxLagNotifyObjsV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 18)
)
tmnxLagNotifyObjsV10v0Group.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagNotifyPortAddFailReason"),
        ("TIMETRA-LAG-MIB", "tLagNotifySubGroupSelected"),
        ("TIMETRA-LAG-MIB", "tLagNotifyAdditionalInfo"),
        ("TIMETRA-LAG-MIB", "tLagNotifyStateChangedReason"))
)
if mibBuilder.loadTexts:
    tmnxLagNotifyObjsV10v0Group.setStatus("current")


# Notification objects

tLagDynamicCostOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 15, 0, 1)
)
tLagDynamicCostOn.setObjects(
    ("TIMETRA-LAG-MIB", "tLagPortThreshold")
)
if mibBuilder.loadTexts:
    tLagDynamicCostOn.setStatus(
        "current"
    )

tLagDynamicCostOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 15, 0, 2)
)
tLagDynamicCostOff.setObjects(
    ("TIMETRA-LAG-MIB", "tLagPortThreshold")
)
if mibBuilder.loadTexts:
    tLagDynamicCostOff.setStatus(
        "current"
    )

tLagPortAddFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 15, 0, 3)
)
tLagPortAddFailed.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortLagId"),
        ("TIMETRA-LAG-MIB", "tLagNotifyPortAddFailReason"))
)
if mibBuilder.loadTexts:
    tLagPortAddFailed.setStatus(
        "current"
    )

tLagSubGroupSelected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 15, 0, 4)
)
tLagSubGroupSelected.setObjects(
    ("TIMETRA-LAG-MIB", "tLagNotifySubGroupSelected")
)
if mibBuilder.loadTexts:
    tLagSubGroupSelected.setStatus(
        "current"
    )

tLagPortAddFailureCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 15, 0, 5)
)
tLagPortAddFailureCleared.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortLagId"),
        ("TIMETRA-LAG-MIB", "tLagNotifyPortAddFailReason"))
)
if mibBuilder.loadTexts:
    tLagPortAddFailureCleared.setStatus(
        "current"
    )

tLagStateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 15, 0, 6)
)
tLagStateEvent.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagRowStatus"),
        ("TIMETRA-LAG-MIB", "tLagNotifyAdditionalInfo"))
)
if mibBuilder.loadTexts:
    tLagStateEvent.setStatus(
        "current"
    )

tLagMemberStateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 15, 0, 7)
)
tLagMemberStateEvent.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortLagId"),
        ("TIMETRA-LAG-MIB", "tLagNotifyAdditionalInfo"),
        ("TIMETRA-LAG-MIB", "tLagNotifyStateChangedReason"))
)
if mibBuilder.loadTexts:
    tLagMemberStateEvent.setStatus(
        "current"
    )


# Notifications groups

tmnxLagNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 3)
)
tmnxLagNotificationsGroup.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagDynamicCostOn"),
        ("TIMETRA-LAG-MIB", "tLagDynamicCostOff"),
        ("TIMETRA-LAG-MIB", "tLagPortAddFailed"))
)
if mibBuilder.loadTexts:
    tmnxLagNotificationsGroup.setStatus(
        "obsolete"
    )

tmnxLagV5v0NotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 8)
)
tmnxLagV5v0NotifGroup.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagDynamicCostOn"),
        ("TIMETRA-LAG-MIB", "tLagDynamicCostOff"),
        ("TIMETRA-LAG-MIB", "tLagPortAddFailed"),
        ("TIMETRA-LAG-MIB", "tLagSubGroupSelected"))
)
if mibBuilder.loadTexts:
    tmnxLagV5v0NotifGroup.setStatus(
        "obsolete"
    )

tmnxLagV6v0NotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 12)
)
tmnxLagV6v0NotifGroup.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagDynamicCostOn"),
        ("TIMETRA-LAG-MIB", "tLagDynamicCostOff"),
        ("TIMETRA-LAG-MIB", "tLagPortAddFailed"),
        ("TIMETRA-LAG-MIB", "tLagSubGroupSelected"),
        ("TIMETRA-LAG-MIB", "tLagPortAddFailureCleared"))
)
if mibBuilder.loadTexts:
    tmnxLagV6v0NotifGroup.setStatus(
        "current"
    )

tmnxLagV10v0NotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 2, 19)
)
tmnxLagV10v0NotifGroup.setObjects(
      *(("TIMETRA-LAG-MIB", "tLagStateEvent"),
        ("TIMETRA-LAG-MIB", "tLagMemberStateEvent"))
)
if mibBuilder.loadTexts:
    tmnxLagV10v0NotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxLagV4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxLagV4v0Compliance.setStatus(
        "obsolete"
    )

tmnxLagV5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxLagV5v0Compliance.setStatus(
        "obsolete"
    )

tmnxLagV6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxLagV6v0Compliance.setStatus(
        "obsolete"
    )

tmnxLagV6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxLagV6v1Compliance.setStatus(
        "obsolete"
    )

tmnxLagV7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxLagV7v0Compliance.setStatus(
        "obsolete"
    )

tmnxLagV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxLagV8v0Compliance.setStatus(
        "obsolete"
    )

tmnxLagV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxLagV9v0Compliance.setStatus(
        "obsolete"
    )

tmnxLagV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 15, 1, 10)
)
if mibBuilder.loadTexts:
    tmnxLagV10v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-LAG-MIB",
    **{"LAGInterfaceNumber": LAGInterfaceNumber,
       "LAGSubgroup": LAGSubgroup,
       "timetraLagMIBModule": timetraLagMIBModule,
       "tmnxLagConformance": tmnxLagConformance,
       "tmnxLagCompliances": tmnxLagCompliances,
       "tmnxLagV4v0Compliance": tmnxLagV4v0Compliance,
       "tmnxLagV5v0Compliance": tmnxLagV5v0Compliance,
       "tmnxLagV6v0Compliance": tmnxLagV6v0Compliance,
       "tmnxLagV6v1Compliance": tmnxLagV6v1Compliance,
       "tmnxLagV7v0Compliance": tmnxLagV7v0Compliance,
       "tmnxLagV8v0Compliance": tmnxLagV8v0Compliance,
       "tmnxLagV9v0Compliance": tmnxLagV9v0Compliance,
       "tmnxLagV10v0Compliance": tmnxLagV10v0Compliance,
       "tmnxLagGroups": tmnxLagGroups,
       "tmnxLagNotifyObjsGroup": tmnxLagNotifyObjsGroup,
       "tmnxLagNotificationsGroup": tmnxLagNotificationsGroup,
       "tmnxLagInstanceV4v0Group": tmnxLagInstanceV4v0Group,
       "tmnxObsoletedObjectsV4v0Group": tmnxObsoletedObjectsV4v0Group,
       "tmnxLagInstanceV5v0Group": tmnxLagInstanceV5v0Group,
       "tmnxLagV5v0NotifGroup": tmnxLagV5v0NotifGroup,
       "tmnxLagNotifyObjsV5v0Group": tmnxLagNotifyObjsV5v0Group,
       "tmnxLagHsmdaV6v0Group": tmnxLagHsmdaV6v0Group,
       "tmnxLagInstanceV6v0Group": tmnxLagInstanceV6v0Group,
       "tmnxLagV6v0NotifGroup": tmnxLagV6v0NotifGroup,
       "tmnxLagV7v0Group": tmnxLagV7v0Group,
       "tmnxObsoletedObjectsV7v0Group": tmnxObsoletedObjectsV7v0Group,
       "tmnxLagInstanceV7v0Group": tmnxLagInstanceV7v0Group,
       "tmnxLagV8v0Group": tmnxLagV8v0Group,
       "tmnxLagInstanceV9v0Group": tmnxLagInstanceV9v0Group,
       "tmnxLagNotifyObjsV10v0Group": tmnxLagNotifyObjsV10v0Group,
       "tmnxLagV10v0NotifGroup": tmnxLagV10v0NotifGroup,
       "tLagObjects": tLagObjects,
       "tLagConfigTable": tLagConfigTable,
       "tLagConfigEntry": tLagConfigEntry,
       "tLagIndex": tLagIndex,
       "tLagRowStatus": tLagRowStatus,
       "tLagPortThreshold": tLagPortThreshold,
       "tLagPortThresholdAction": tLagPortThresholdAction,
       "tLagEnableMarkerGenerator": tLagEnableMarkerGenerator,
       "tLagEnableLACP": tLagEnableLACP,
       "tLagDescription": tLagDescription,
       "tLagDynamicCosting": tLagDynamicCosting,
       "tLagLACPMode": tLagLACPMode,
       "tLagLACPAdminKeyAutogen": tLagLACPAdminKeyAutogen,
       "tLagLACPTransmitInterval": tLagLACPTransmitInterval,
       "tLagAccessAdaptQos": tLagAccessAdaptQos,
       "tLagLACPXmitStdby": tLagLACPXmitStdby,
       "tLagLACPSelCrit": tLagLACPSelCrit,
       "tLagLACPSelCritSlaveToPartner": tLagLACPSelCritSlaveToPartner,
       "tLagLACPNbrOfSubGroups": tLagLACPNbrOfSubGroups,
       "tLagholdTimeDown": tLagholdTimeDown,
       "tLagPortType": tLagPortType,
       "tLagPerFpIngQueuing": tLagPerFpIngQueuing,
       "tLagSystemId": tLagSystemId,
       "tLagSystemPriority": tLagSystemPriority,
       "tLagStandbySignaling": tLagStandbySignaling,
       "tLagOperationTable": tLagOperationTable,
       "tLagOperationEntry": tLagOperationEntry,
       "tLagIfIndex": tLagIfIndex,
       "tLagConfigLastChange": tLagConfigLastChange,
       "tLagPortThresholdFalling": tLagPortThresholdFalling,
       "tLagPortThresholdRising": tLagPortThresholdRising,
       "tLagLACPPrimaryPort": tLagLACPPrimaryPort,
       "tLagPortReasonDownFlags": tLagPortReasonDownFlags,
       "tLagNotificationObjects": tLagNotificationObjects,
       "tLagNotifyPortAddFailReason": tLagNotifyPortAddFailReason,
       "tLagNotifySubGroupSelected": tLagNotifySubGroupSelected,
       "tLagNotifyAdditionalInfo": tLagNotifyAdditionalInfo,
       "tLagNotifyStateChangedReason": tLagNotifyStateChangedReason,
       "tLagMemberTable": tLagMemberTable,
       "tLagMemberEntry": tLagMemberEntry,
       "tLagMemberPortName": tLagMemberPortName,
       "tLagMemberPortIsPrimary": tLagMemberPortIsPrimary,
       "tLagPortTable": tLagPortTable,
       "tLagPortEntry": tLagPortEntry,
       "tLagPortSubgroup": tLagPortSubgroup,
       "tLagPortActiveStdby": tLagPortActiveStdby,
       "tLagNotifyPrefix": tLagNotifyPrefix,
       "tLagNotifications": tLagNotifications,
       "tLagDynamicCostOn": tLagDynamicCostOn,
       "tLagDynamicCostOff": tLagDynamicCostOff,
       "tLagPortAddFailed": tLagPortAddFailed,
       "tLagSubGroupSelected": tLagSubGroupSelected,
       "tLagPortAddFailureCleared": tLagPortAddFailureCleared,
       "tLagStateEvent": tLagStateEvent,
       "tLagMemberStateEvent": tLagMemberStateEvent}
)
