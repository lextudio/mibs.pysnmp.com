# SNMP MIB module (CISCO-C2900-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-C2900-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:29 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoC2900MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 87)
)
ciscoC2900MIB.setRevisions(
        ("2002-05-30 00:00",
         "2001-07-25 13:45",
         "1999-09-24 00:00",
         "1999-08-24 00:00",
         "1999-05-20 00:00",
         "1998-06-08 00:00",
         "1998-04-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_C2900MIBObjects_ObjectIdentity = ObjectIdentity
c2900MIBObjects = _C2900MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1)
)
_C2900SysInfo_ObjectIdentity = ObjectIdentity
c2900SysInfo = _C2900SysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 1)
)
_C2900InfoBoardRevision_Type = Gauge32
_C2900InfoBoardRevision_Object = MibScalar
c2900InfoBoardRevision = _C2900InfoBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 1, 1),
    _C2900InfoBoardRevision_Type()
)
c2900InfoBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900InfoBoardRevision.setStatus("current")
_C2900InfoPeakBuffersUsed_Type = Gauge32
_C2900InfoPeakBuffersUsed_Object = MibScalar
c2900InfoPeakBuffersUsed = _C2900InfoPeakBuffersUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 1, 2),
    _C2900InfoPeakBuffersUsed_Type()
)
c2900InfoPeakBuffersUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900InfoPeakBuffersUsed.setStatus("current")
if mibBuilder.loadTexts:
    c2900InfoPeakBuffersUsed.setUnits("buffers")
_C2900InfoTotalBufferDepth_Type = Gauge32
_C2900InfoTotalBufferDepth_Object = MibScalar
c2900InfoTotalBufferDepth = _C2900InfoTotalBufferDepth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 1, 3),
    _C2900InfoTotalBufferDepth_Type()
)
c2900InfoTotalBufferDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900InfoTotalBufferDepth.setStatus("current")
if mibBuilder.loadTexts:
    c2900InfoTotalBufferDepth.setUnits("buffers")
_C2900InfoAddrCapacity_Type = Gauge32
_C2900InfoAddrCapacity_Object = MibScalar
c2900InfoAddrCapacity = _C2900InfoAddrCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 1, 4),
    _C2900InfoAddrCapacity_Type()
)
c2900InfoAddrCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900InfoAddrCapacity.setStatus("current")
_C2900InfoRestrictedStaticAddrCapacity_Type = Gauge32
_C2900InfoRestrictedStaticAddrCapacity_Object = MibScalar
c2900InfoRestrictedStaticAddrCapacity = _C2900InfoRestrictedStaticAddrCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 1, 5),
    _C2900InfoRestrictedStaticAddrCapacity_Type()
)
c2900InfoRestrictedStaticAddrCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900InfoRestrictedStaticAddrCapacity.setStatus("current")


class _C2900InfoSelfTestFailed_Type(OctetString):
    """Custom type c2900InfoSelfTestFailed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_C2900InfoSelfTestFailed_Type.__name__ = "OctetString"
_C2900InfoSelfTestFailed_Object = MibScalar
c2900InfoSelfTestFailed = _C2900InfoSelfTestFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 1, 6),
    _C2900InfoSelfTestFailed_Type()
)
c2900InfoSelfTestFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900InfoSelfTestFailed.setStatus("current")
_C2900InfoUtilDisplay_Type = Gauge32
_C2900InfoUtilDisplay_Object = MibScalar
c2900InfoUtilDisplay = _C2900InfoUtilDisplay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 1, 7),
    _C2900InfoUtilDisplay_Type()
)
c2900InfoUtilDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900InfoUtilDisplay.setStatus("current")


class _C2900InfoVisualIndicatorMode_Type(Integer32):
    """Custom type c2900InfoVisualIndicatorMode based on Integer32"""
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
        *(("fullDuplex", 2),
          ("linkRate", 3),
          ("portStatus", 1),
          ("utilization", 4))
    )


_C2900InfoVisualIndicatorMode_Type.__name__ = "Integer32"
_C2900InfoVisualIndicatorMode_Object = MibScalar
c2900InfoVisualIndicatorMode = _C2900InfoVisualIndicatorMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 1, 8),
    _C2900InfoVisualIndicatorMode_Type()
)
c2900InfoVisualIndicatorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900InfoVisualIndicatorMode.setStatus("current")


class _C2900InfoRedunantPowerSupplyInfo_Type(Integer32):
    """Custom type c2900InfoRedunantPowerSupplyInfo based on Integer32"""
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
        *(("absent", 1),
          ("connectedFunctional", 2),
          ("connectedNotFunctional", 3),
          ("functionalPrimaryFailed", 4))
    )


_C2900InfoRedunantPowerSupplyInfo_Type.__name__ = "Integer32"
_C2900InfoRedunantPowerSupplyInfo_Object = MibScalar
c2900InfoRedunantPowerSupplyInfo = _C2900InfoRedunantPowerSupplyInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 1, 9),
    _C2900InfoRedunantPowerSupplyInfo_Type()
)
c2900InfoRedunantPowerSupplyInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900InfoRedunantPowerSupplyInfo.setStatus("current")
_C2900InfoBoardIdentifier_Type = Gauge32
_C2900InfoBoardIdentifier_Object = MibScalar
c2900InfoBoardIdentifier = _C2900InfoBoardIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 1, 10),
    _C2900InfoBoardIdentifier_Type()
)
c2900InfoBoardIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900InfoBoardIdentifier.setStatus("current")
_C2900SysConfig_ObjectIdentity = ObjectIdentity
c2900SysConfig = _C2900SysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 2)
)


class _C2900ConfigAddressViolationAction_Type(Integer32):
    """Custom type c2900ConfigAddressViolationAction based on Integer32"""
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
        *(("disablePort", 2),
          ("disablePortAndNotify", 4),
          ("doNothing", 1),
          ("sendNotify", 3))
    )


_C2900ConfigAddressViolationAction_Type.__name__ = "Integer32"
_C2900ConfigAddressViolationAction_Object = MibScalar
c2900ConfigAddressViolationAction = _C2900ConfigAddressViolationAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 2, 1),
    _C2900ConfigAddressViolationAction_Type()
)
c2900ConfigAddressViolationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2900ConfigAddressViolationAction.setStatus("deprecated")
_C2900ConfigBroadcastStormAlarm_Type = TruthValue
_C2900ConfigBroadcastStormAlarm_Object = MibScalar
c2900ConfigBroadcastStormAlarm = _C2900ConfigBroadcastStormAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 2, 2),
    _C2900ConfigBroadcastStormAlarm_Type()
)
c2900ConfigBroadcastStormAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2900ConfigBroadcastStormAlarm.setStatus("deprecated")
_C2900ModuleTable_Object = MibTable
c2900ModuleTable = _C2900ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 3)
)
if mibBuilder.loadTexts:
    c2900ModuleTable.setStatus("current")
_C2900ModuleEntry_Object = MibTableRow
c2900ModuleEntry = _C2900ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 3, 1)
)
c2900ModuleEntry.setIndexNames(
    (0, "CISCO-C2900-MIB", "c2900ModuleIndex"),
)
if mibBuilder.loadTexts:
    c2900ModuleEntry.setStatus("current")


class _C2900ModuleIndex_Type(Integer32):
    """Custom type c2900ModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_C2900ModuleIndex_Type.__name__ = "Integer32"
_C2900ModuleIndex_Object = MibTableColumn
c2900ModuleIndex = _C2900ModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 3, 1, 1),
    _C2900ModuleIndex_Type()
)
c2900ModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c2900ModuleIndex.setStatus("current")


class _C2900ModuleStatus_Type(Integer32):
    """Custom type c2900ModuleStatus based on Integer32"""
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
        *(("moduleFaulty", 4),
          ("moduleHealthy", 3),
          ("moduleInTest", 2),
          ("moduleNotInstalled", 1))
    )


_C2900ModuleStatus_Type.__name__ = "Integer32"
_C2900ModuleStatus_Object = MibTableColumn
c2900ModuleStatus = _C2900ModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 3, 1, 2),
    _C2900ModuleStatus_Type()
)
c2900ModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900ModuleStatus.setStatus("current")


class _C2900ModuleType_Type(Integer32):
    """Custom type c2900ModuleType based on Integer32"""
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
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("atm155MMFiber", 7),
          ("atm155SMLRFiber", 5),
          ("atm155SMMRFiber", 6),
          ("atm155UTP", 8),
          ("empty", 2),
          ("other", 1),
          ("wsx2914xl", 3),
          ("wsx2914xlv", 9),
          ("wsx2922xl", 4),
          ("wsx2922xlv", 10),
          ("wsx2924xlv", 11),
          ("wsx2931xl", 12),
          ("wsx2932xl", 13))
    )


_C2900ModuleType_Type.__name__ = "Integer32"
_C2900ModuleType_Object = MibTableColumn
c2900ModuleType = _C2900ModuleType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 3, 1, 3),
    _C2900ModuleType_Type()
)
c2900ModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900ModuleType.setStatus("current")


class _C2900ModuleHwVersion_Type(DisplayString):
    """Custom type c2900ModuleHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_C2900ModuleHwVersion_Type.__name__ = "DisplayString"
_C2900ModuleHwVersion_Object = MibTableColumn
c2900ModuleHwVersion = _C2900ModuleHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 3, 1, 4),
    _C2900ModuleHwVersion_Type()
)
c2900ModuleHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900ModuleHwVersion.setStatus("current")


class _C2900ModuleSwVersion_Type(DisplayString):
    """Custom type c2900ModuleSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_C2900ModuleSwVersion_Type.__name__ = "DisplayString"
_C2900ModuleSwVersion_Object = MibTableColumn
c2900ModuleSwVersion = _C2900ModuleSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 3, 1, 5),
    _C2900ModuleSwVersion_Type()
)
c2900ModuleSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900ModuleSwVersion.setStatus("current")
_C2900Port_ObjectIdentity = ObjectIdentity
c2900Port = _C2900Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4)
)
_C2900PortTable_Object = MibTable
c2900PortTable = _C2900PortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1)
)
if mibBuilder.loadTexts:
    c2900PortTable.setStatus("current")
_C2900PortEntry_Object = MibTableRow
c2900PortEntry = _C2900PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1)
)
c2900PortEntry.setIndexNames(
    (0, "CISCO-C2900-MIB", "c2900PortModuleIndex"),
    (0, "CISCO-C2900-MIB", "c2900PortIndex"),
)
if mibBuilder.loadTexts:
    c2900PortEntry.setStatus("current")


class _C2900PortModuleIndex_Type(Integer32):
    """Custom type c2900PortModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_C2900PortModuleIndex_Type.__name__ = "Integer32"
_C2900PortModuleIndex_Object = MibTableColumn
c2900PortModuleIndex = _C2900PortModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 1),
    _C2900PortModuleIndex_Type()
)
c2900PortModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c2900PortModuleIndex.setStatus("current")


class _C2900PortIndex_Type(Integer32):
    """Custom type c2900PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_C2900PortIndex_Type.__name__ = "Integer32"
_C2900PortIndex_Object = MibTableColumn
c2900PortIndex = _C2900PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 2),
    _C2900PortIndex_Type()
)
c2900PortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c2900PortIndex.setStatus("current")


class _C2900PortUsageApplication_Type(Integer32):
    """Custom type c2900PortUsageApplication based on Integer32"""
    defaultValue = 1

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
        *(("monitor", 3),
          ("network", 5),
          ("networkGroup", 6),
          ("portGroupDest", 7),
          ("portGrouping", 4),
          ("protected", 8),
          ("security", 2),
          ("standard", 1))
    )


_C2900PortUsageApplication_Type.__name__ = "Integer32"
_C2900PortUsageApplication_Object = MibTableColumn
c2900PortUsageApplication = _C2900PortUsageApplication_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 3),
    _C2900PortUsageApplication_Type()
)
c2900PortUsageApplication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2900PortUsageApplication.setStatus("current")


class _C2900PortGroupIndex_Type(Integer32):
    """Custom type c2900PortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_C2900PortGroupIndex_Type.__name__ = "Integer32"
_C2900PortGroupIndex_Object = MibTableColumn
c2900PortGroupIndex = _C2900PortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 4),
    _C2900PortGroupIndex_Type()
)
c2900PortGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2900PortGroupIndex.setStatus("current")


class _C2900PortMayLearnAddress_Type(TruthValue):
    """Custom type c2900PortMayLearnAddress based on TruthValue"""


_C2900PortMayLearnAddress_Object = MibTableColumn
c2900PortMayLearnAddress = _C2900PortMayLearnAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 5),
    _C2900PortMayLearnAddress_Type()
)
c2900PortMayLearnAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2900PortMayLearnAddress.setStatus("deprecated")


class _C2900PortMayForwardFrames_Type(TruthValue):
    """Custom type c2900PortMayForwardFrames based on TruthValue"""


_C2900PortMayForwardFrames_Object = MibTableColumn
c2900PortMayForwardFrames = _C2900PortMayForwardFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 6),
    _C2900PortMayForwardFrames_Type()
)
c2900PortMayForwardFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2900PortMayForwardFrames.setStatus("current")
_C2900PortBufferCongestionControl_Type = TruthValue
_C2900PortBufferCongestionControl_Object = MibTableColumn
c2900PortBufferCongestionControl = _C2900PortBufferCongestionControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 7),
    _C2900PortBufferCongestionControl_Type()
)
c2900PortBufferCongestionControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900PortBufferCongestionControl.setStatus("deprecated")


class _C2900PortBufferCongestionThreshholdPercent_Type(Integer32):
    """Custom type c2900PortBufferCongestionThreshholdPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_C2900PortBufferCongestionThreshholdPercent_Type.__name__ = "Integer32"
_C2900PortBufferCongestionThreshholdPercent_Object = MibTableColumn
c2900PortBufferCongestionThreshholdPercent = _C2900PortBufferCongestionThreshholdPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 8),
    _C2900PortBufferCongestionThreshholdPercent_Type()
)
c2900PortBufferCongestionThreshholdPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900PortBufferCongestionThreshholdPercent.setStatus("current")


class _C2900PortFrameAge_Type(Integer32):
    """Custom type c2900PortFrameAge based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 4000),
    )


_C2900PortFrameAge_Type.__name__ = "Integer32"
_C2900PortFrameAge_Object = MibTableColumn
c2900PortFrameAge = _C2900PortFrameAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 9),
    _C2900PortFrameAge_Type()
)
c2900PortFrameAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900PortFrameAge.setStatus("current")
if mibBuilder.loadTexts:
    c2900PortFrameAge.setUnits("milliseconds")


class _C2900PortAddrSecureMaxAddresses_Type(Integer32):
    """Custom type c2900PortAddrSecureMaxAddresses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 132),
    )


_C2900PortAddrSecureMaxAddresses_Type.__name__ = "Integer32"
_C2900PortAddrSecureMaxAddresses_Object = MibTableColumn
c2900PortAddrSecureMaxAddresses = _C2900PortAddrSecureMaxAddresses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 10),
    _C2900PortAddrSecureMaxAddresses_Type()
)
c2900PortAddrSecureMaxAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2900PortAddrSecureMaxAddresses.setStatus("current")
_C2900PortAddrSecureCurrentAddresses_Type = Gauge32
_C2900PortAddrSecureCurrentAddresses_Object = MibTableColumn
c2900PortAddrSecureCurrentAddresses = _C2900PortAddrSecureCurrentAddresses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 11),
    _C2900PortAddrSecureCurrentAddresses_Type()
)
c2900PortAddrSecureCurrentAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900PortAddrSecureCurrentAddresses.setStatus("current")
_C2900PortAddrSecureAddrViolations_Type = Counter32
_C2900PortAddrSecureAddrViolations_Object = MibTableColumn
c2900PortAddrSecureAddrViolations = _C2900PortAddrSecureAddrViolations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 12),
    _C2900PortAddrSecureAddrViolations_Type()
)
c2900PortAddrSecureAddrViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900PortAddrSecureAddrViolations.setStatus("current")
_C2900PortNumberOfLearnedAddresses_Type = Counter32
_C2900PortNumberOfLearnedAddresses_Object = MibTableColumn
c2900PortNumberOfLearnedAddresses = _C2900PortNumberOfLearnedAddresses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 13),
    _C2900PortNumberOfLearnedAddresses_Type()
)
c2900PortNumberOfLearnedAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900PortNumberOfLearnedAddresses.setStatus("current")
_C2900PortNumberOfDroppedAddresses_Type = Counter32
_C2900PortNumberOfDroppedAddresses_Object = MibTableColumn
c2900PortNumberOfDroppedAddresses = _C2900PortNumberOfDroppedAddresses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 14),
    _C2900PortNumberOfDroppedAddresses_Type()
)
c2900PortNumberOfDroppedAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900PortNumberOfDroppedAddresses.setStatus("current")
_C2900PortClearAddresses_Type = TruthValue
_C2900PortClearAddresses_Object = MibTableColumn
c2900PortClearAddresses = _C2900PortClearAddresses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 15),
    _C2900PortClearAddresses_Type()
)
c2900PortClearAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2900PortClearAddresses.setStatus("current")


class _C2900PortFloodUnknownMulticasts_Type(TruthValue):
    """Custom type c2900PortFloodUnknownMulticasts based on TruthValue"""


_C2900PortFloodUnknownMulticasts_Object = MibTableColumn
c2900PortFloodUnknownMulticasts = _C2900PortFloodUnknownMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 16),
    _C2900PortFloodUnknownMulticasts_Type()
)
c2900PortFloodUnknownMulticasts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2900PortFloodUnknownMulticasts.setStatus("current")
_C2900PortFloodUnknownUnicasts_Type = TruthValue
_C2900PortFloodUnknownUnicasts_Object = MibTableColumn
c2900PortFloodUnknownUnicasts = _C2900PortFloodUnknownUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 17),
    _C2900PortFloodUnknownUnicasts_Type()
)
c2900PortFloodUnknownUnicasts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2900PortFloodUnknownUnicasts.setStatus("current")


class _C2900PortLinkbeatStatus_Type(Integer32):
    """Custom type c2900PortLinkbeatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("linkbeat", 2),
          ("nolinkbeat", 3),
          ("unknown", 1))
    )


_C2900PortLinkbeatStatus_Type.__name__ = "Integer32"
_C2900PortLinkbeatStatus_Object = MibTableColumn
c2900PortLinkbeatStatus = _C2900PortLinkbeatStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 18),
    _C2900PortLinkbeatStatus_Type()
)
c2900PortLinkbeatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900PortLinkbeatStatus.setStatus("current")


class _C2900PortBroadcastStormAction_Type(Integer32):
    """Custom type c2900PortBroadcastStormAction based on Integer32"""
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
        *(("disablePort", 3),
          ("forwardBroadcast", 2),
          ("stopBroadcastForwarding", 1))
    )


_C2900PortBroadcastStormAction_Type.__name__ = "Integer32"
_C2900PortBroadcastStormAction_Object = MibTableColumn
c2900PortBroadcastStormAction = _C2900PortBroadcastStormAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 19),
    _C2900PortBroadcastStormAction_Type()
)
c2900PortBroadcastStormAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2900PortBroadcastStormAction.setStatus("current")


class _C2900PortBroadcastRisingThreshold_Type(Gauge32):
    """Custom type c2900PortBroadcastRisingThreshold based on Gauge32"""
    defaultValue = 500


_C2900PortBroadcastRisingThreshold_Object = MibTableColumn
c2900PortBroadcastRisingThreshold = _C2900PortBroadcastRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 20),
    _C2900PortBroadcastRisingThreshold_Type()
)
c2900PortBroadcastRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2900PortBroadcastRisingThreshold.setStatus("current")


class _C2900PortBroadcastFallingThreshold_Type(Gauge32):
    """Custom type c2900PortBroadcastFallingThreshold based on Gauge32"""
    defaultValue = 250


_C2900PortBroadcastFallingThreshold_Object = MibTableColumn
c2900PortBroadcastFallingThreshold = _C2900PortBroadcastFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 21),
    _C2900PortBroadcastFallingThreshold_Type()
)
c2900PortBroadcastFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2900PortBroadcastFallingThreshold.setStatus("current")


class _C2900PortStatus_Type(Integer32):
    """Custom type c2900PortStatus based on Integer32"""
    defaultValue = 3

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
        *(("blocking", 3),
          ("broken", 10),
          ("disabled", 2),
          ("forwarding", 7),
          ("learning", 5),
          ("listening", 4),
          ("other", 1),
          ("preforwarding", 6),
          ("secureforwarding", 8),
          ("suspended", 9))
    )


_C2900PortStatus_Type.__name__ = "Integer32"
_C2900PortStatus_Object = MibTableColumn
c2900PortStatus = _C2900PortStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 22),
    _C2900PortStatus_Type()
)
c2900PortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900PortStatus.setStatus("current")
_C2900PortTestResult_Type = TruthValue
_C2900PortTestResult_Object = MibTableColumn
c2900PortTestResult = _C2900PortTestResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 23),
    _C2900PortTestResult_Type()
)
c2900PortTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900PortTestResult.setStatus("current")


class _C2900PortVisualIndicator_Type(Integer32):
    """Custom type c2900PortVisualIndicator based on Integer32"""
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
        *(("amber", 3),
          ("black", 2),
          ("green", 4),
          ("notused", 1))
    )


_C2900PortVisualIndicator_Type.__name__ = "Integer32"
_C2900PortVisualIndicator_Object = MibTableColumn
c2900PortVisualIndicator = _C2900PortVisualIndicator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 24),
    _C2900PortVisualIndicator_Type()
)
c2900PortVisualIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900PortVisualIndicator.setStatus("current")


class _C2900PortIfIndex_Type(InterfaceIndex):
    """Custom type c2900PortIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_C2900PortIfIndex_Type.__name__ = "InterfaceIndex"
_C2900PortIfIndex_Object = MibTableColumn
c2900PortIfIndex = _C2900PortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 25),
    _C2900PortIfIndex_Type()
)
c2900PortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900PortIfIndex.setStatus("current")


class _C2900PortAddressViolationAction_Type(Integer32):
    """Custom type c2900PortAddressViolationAction based on Integer32"""
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
        *(("disablePort", 2),
          ("disablePortAndNotify", 4),
          ("doNothing", 1),
          ("sendNotify", 3))
    )


_C2900PortAddressViolationAction_Type.__name__ = "Integer32"
_C2900PortAddressViolationAction_Object = MibTableColumn
c2900PortAddressViolationAction = _C2900PortAddressViolationAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 26),
    _C2900PortAddressViolationAction_Type()
)
c2900PortAddressViolationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2900PortAddressViolationAction.setStatus("current")


class _C2900PortBroadcastStormAlarm_Type(TruthValue):
    """Custom type c2900PortBroadcastStormAlarm based on TruthValue"""


_C2900PortBroadcastStormAlarm_Object = MibTableColumn
c2900PortBroadcastStormAlarm = _C2900PortBroadcastStormAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 27),
    _C2900PortBroadcastStormAlarm_Type()
)
c2900PortBroadcastStormAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2900PortBroadcastStormAlarm.setStatus("current")


class _C2900PortMonitorDestinationPort_Type(Integer32):
    """Custom type c2900PortMonitorDestinationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_C2900PortMonitorDestinationPort_Type.__name__ = "Integer32"
_C2900PortMonitorDestinationPort_Object = MibTableColumn
c2900PortMonitorDestinationPort = _C2900PortMonitorDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 28),
    _C2900PortMonitorDestinationPort_Type()
)
c2900PortMonitorDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2900PortMonitorDestinationPort.setStatus("current")


class _C2900PortSwitchPortIndex_Type(Integer32):
    """Custom type c2900PortSwitchPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_C2900PortSwitchPortIndex_Type.__name__ = "Integer32"
_C2900PortSwitchPortIndex_Object = MibTableColumn
c2900PortSwitchPortIndex = _C2900PortSwitchPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 29),
    _C2900PortSwitchPortIndex_Type()
)
c2900PortSwitchPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900PortSwitchPortIndex.setStatus("current")


class _C2900PortMonitoredPortMap_Type(OctetString):
    """Custom type c2900PortMonitoredPortMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_C2900PortMonitoredPortMap_Type.__name__ = "OctetString"
_C2900PortMonitoredPortMap_Object = MibTableColumn
c2900PortMonitoredPortMap = _C2900PortMonitoredPortMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 30),
    _C2900PortMonitoredPortMap_Type()
)
c2900PortMonitoredPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900PortMonitoredPortMap.setStatus("current")


class _C2900PortDuplexState_Type(Integer32):
    """Custom type c2900PortDuplexState based on Integer32"""
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
        *(("autoNegotiate", 3),
          ("fullduplex", 1),
          ("halfduplex", 2))
    )


_C2900PortDuplexState_Type.__name__ = "Integer32"
_C2900PortDuplexState_Object = MibTableColumn
c2900PortDuplexState = _C2900PortDuplexState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 31),
    _C2900PortDuplexState_Type()
)
c2900PortDuplexState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2900PortDuplexState.setStatus("current")


class _C2900PortDuplexStatus_Type(Integer32):
    """Custom type c2900PortDuplexStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullduplex", 1),
          ("halfduplex", 2))
    )


_C2900PortDuplexStatus_Type.__name__ = "Integer32"
_C2900PortDuplexStatus_Object = MibTableColumn
c2900PortDuplexStatus = _C2900PortDuplexStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 32),
    _C2900PortDuplexStatus_Type()
)
c2900PortDuplexStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900PortDuplexStatus.setStatus("current")


class _C2900PortAdminSpeed_Type(Integer32):
    """Custom type c2900PortAdminSpeed based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10000000,
              100000000,
              155520000)
        )
    )
    namedValues = NamedValues(
        *(("autoDetect", 1),
          ("s10000000", 10000000),
          ("s100000000", 100000000),
          ("s155520000", 155520000))
    )


_C2900PortAdminSpeed_Type.__name__ = "Integer32"
_C2900PortAdminSpeed_Object = MibTableColumn
c2900PortAdminSpeed = _C2900PortAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 33),
    _C2900PortAdminSpeed_Type()
)
c2900PortAdminSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2900PortAdminSpeed.setStatus("current")


class _C2900PortNoMonitorDestinationPort_Type(Integer32):
    """Custom type c2900PortNoMonitorDestinationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_C2900PortNoMonitorDestinationPort_Type.__name__ = "Integer32"
_C2900PortNoMonitorDestinationPort_Object = MibTableColumn
c2900PortNoMonitorDestinationPort = _C2900PortNoMonitorDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 34),
    _C2900PortNoMonitorDestinationPort_Type()
)
c2900PortNoMonitorDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2900PortNoMonitorDestinationPort.setStatus("current")


class _C2900Portdot1dBasePort_Type(Integer32):
    """Custom type c2900Portdot1dBasePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_C2900Portdot1dBasePort_Type.__name__ = "Integer32"
_C2900Portdot1dBasePort_Object = MibTableColumn
c2900Portdot1dBasePort = _C2900Portdot1dBasePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 35),
    _C2900Portdot1dBasePort_Type()
)
c2900Portdot1dBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900Portdot1dBasePort.setStatus("current")


class _C2900PortSpantreeFastStart_Type(Integer32):
    """Custom type c2900PortSpantreeFastStart based on Integer32"""
    defaultValue = 2

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


_C2900PortSpantreeFastStart_Type.__name__ = "Integer32"
_C2900PortSpantreeFastStart_Object = MibTableColumn
c2900PortSpantreeFastStart = _C2900PortSpantreeFastStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 36),
    _C2900PortSpantreeFastStart_Type()
)
c2900PortSpantreeFastStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2900PortSpantreeFastStart.setStatus("current")


class _C2900PortVoiceVlanId_Type(Integer32):
    """Custom type c2900PortVoiceVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000),
        ValueRangeConstraint(4095, 4095),
        ValueRangeConstraint(4096, 4096),
    )


_C2900PortVoiceVlanId_Type.__name__ = "Integer32"
_C2900PortVoiceVlanId_Object = MibTableColumn
c2900PortVoiceVlanId = _C2900PortVoiceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 37),
    _C2900PortVoiceVlanId_Type()
)
c2900PortVoiceVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2900PortVoiceVlanId.setStatus("current")


class _C2900PortAddrSecureAgingTime_Type(Integer32):
    """Custom type c2900PortAddrSecureAgingTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_C2900PortAddrSecureAgingTime_Type.__name__ = "Integer32"
_C2900PortAddrSecureAgingTime_Object = MibTableColumn
c2900PortAddrSecureAgingTime = _C2900PortAddrSecureAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 38),
    _C2900PortAddrSecureAgingTime_Type()
)
c2900PortAddrSecureAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2900PortAddrSecureAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    c2900PortAddrSecureAgingTime.setUnits("minutes")


class _C2900PortAddrSecureAgingType_Type(Integer32):
    """Custom type c2900PortAddrSecureAgingType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("inactivity", 2))
    )


_C2900PortAddrSecureAgingType_Type.__name__ = "Integer32"
_C2900PortAddrSecureAgingType_Object = MibTableColumn
c2900PortAddrSecureAgingType = _C2900PortAddrSecureAgingType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 39),
    _C2900PortAddrSecureAgingType_Type()
)
c2900PortAddrSecureAgingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2900PortAddrSecureAgingType.setStatus("current")


class _C2900PortAddrSecureAgingStatic_Type(TruthValue):
    """Custom type c2900PortAddrSecureAgingStatic based on TruthValue"""


_C2900PortAddrSecureAgingStatic_Object = MibTableColumn
c2900PortAddrSecureAgingStatic = _C2900PortAddrSecureAgingStatic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 1, 1, 40),
    _C2900PortAddrSecureAgingStatic_Type()
)
c2900PortAddrSecureAgingStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2900PortAddrSecureAgingStatic.setStatus("current")
_C2900PortStatsTable_Object = MibTable
c2900PortStatsTable = _C2900PortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 2)
)
if mibBuilder.loadTexts:
    c2900PortStatsTable.setStatus("current")
_C2900PortStatsEntry_Object = MibTableRow
c2900PortStatsEntry = _C2900PortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 2, 1)
)
c2900PortStatsEntry.setIndexNames(
    (0, "CISCO-C2900-MIB", "c2900PortModuleIndex"),
    (0, "CISCO-C2900-MIB", "c2900PortIndex"),
)
if mibBuilder.loadTexts:
    c2900PortStatsEntry.setStatus("current")
_C2900PortRxNoBwFrames_Type = Counter32
_C2900PortRxNoBwFrames_Object = MibTableColumn
c2900PortRxNoBwFrames = _C2900PortRxNoBwFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 2, 1, 1),
    _C2900PortRxNoBwFrames_Type()
)
c2900PortRxNoBwFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900PortRxNoBwFrames.setStatus("current")
if mibBuilder.loadTexts:
    c2900PortRxNoBwFrames.setUnits("frames")
_C2900PortRxNoBufferFrames_Type = Counter32
_C2900PortRxNoBufferFrames_Object = MibTableColumn
c2900PortRxNoBufferFrames = _C2900PortRxNoBufferFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 2, 1, 2),
    _C2900PortRxNoBufferFrames_Type()
)
c2900PortRxNoBufferFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900PortRxNoBufferFrames.setStatus("current")
if mibBuilder.loadTexts:
    c2900PortRxNoBufferFrames.setUnits("frames")
_C2900PortRxNoDestUniFrames_Type = Counter32
_C2900PortRxNoDestUniFrames_Object = MibTableColumn
c2900PortRxNoDestUniFrames = _C2900PortRxNoDestUniFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 2, 1, 3),
    _C2900PortRxNoDestUniFrames_Type()
)
c2900PortRxNoDestUniFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900PortRxNoDestUniFrames.setStatus("current")
if mibBuilder.loadTexts:
    c2900PortRxNoDestUniFrames.setUnits("frames")
_C2900PortRxNoDestMultiFrames_Type = Counter32
_C2900PortRxNoDestMultiFrames_Object = MibTableColumn
c2900PortRxNoDestMultiFrames = _C2900PortRxNoDestMultiFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 2, 1, 4),
    _C2900PortRxNoDestMultiFrames_Type()
)
c2900PortRxNoDestMultiFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900PortRxNoDestMultiFrames.setStatus("current")
if mibBuilder.loadTexts:
    c2900PortRxNoDestMultiFrames.setUnits("frames")
_C2900PortRxSuppressBcastFrames_Type = Counter32
_C2900PortRxSuppressBcastFrames_Object = MibTableColumn
c2900PortRxSuppressBcastFrames = _C2900PortRxSuppressBcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 2, 1, 5),
    _C2900PortRxSuppressBcastFrames_Type()
)
c2900PortRxSuppressBcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900PortRxSuppressBcastFrames.setStatus("deprecated")
if mibBuilder.loadTexts:
    c2900PortRxSuppressBcastFrames.setUnits("frames")
_C2900PortRxFcsErrFrames_Type = Counter32
_C2900PortRxFcsErrFrames_Object = MibTableColumn
c2900PortRxFcsErrFrames = _C2900PortRxFcsErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 2, 1, 6),
    _C2900PortRxFcsErrFrames_Type()
)
c2900PortRxFcsErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900PortRxFcsErrFrames.setStatus("current")
if mibBuilder.loadTexts:
    c2900PortRxFcsErrFrames.setUnits("frames")
_C2900PortCollFragFrames_Type = Counter32
_C2900PortCollFragFrames_Object = MibTableColumn
c2900PortCollFragFrames = _C2900PortCollFragFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 2, 1, 7),
    _C2900PortCollFragFrames_Type()
)
c2900PortCollFragFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900PortCollFragFrames.setStatus("current")
if mibBuilder.loadTexts:
    c2900PortCollFragFrames.setUnits("frames")
_C2900PortTxMulticastFrames_Type = Counter32
_C2900PortTxMulticastFrames_Object = MibTableColumn
c2900PortTxMulticastFrames = _C2900PortTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 2, 1, 8),
    _C2900PortTxMulticastFrames_Type()
)
c2900PortTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900PortTxMulticastFrames.setStatus("current")
if mibBuilder.loadTexts:
    c2900PortTxMulticastFrames.setUnits("frames")
_C2900PortTxBroadcastFrames_Type = Counter32
_C2900PortTxBroadcastFrames_Object = MibTableColumn
c2900PortTxBroadcastFrames = _C2900PortTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 4, 2, 1, 9),
    _C2900PortTxBroadcastFrames_Type()
)
c2900PortTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900PortTxBroadcastFrames.setStatus("current")
if mibBuilder.loadTexts:
    c2900PortTxBroadcastFrames.setUnits("frames")
_C2900BandwidthUsage_ObjectIdentity = ObjectIdentity
c2900BandwidthUsage = _C2900BandwidthUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 5)
)
_C2900BandwidthUsageCurrent_Type = Gauge32
_C2900BandwidthUsageCurrent_Object = MibScalar
c2900BandwidthUsageCurrent = _C2900BandwidthUsageCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 5, 1),
    _C2900BandwidthUsageCurrent_Type()
)
c2900BandwidthUsageCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900BandwidthUsageCurrent.setStatus("current")
if mibBuilder.loadTexts:
    c2900BandwidthUsageCurrent.setUnits("megabits per second")
_C2900BandwidthUsageMaxPeakEntries_Type = Gauge32
_C2900BandwidthUsageMaxPeakEntries_Object = MibScalar
c2900BandwidthUsageMaxPeakEntries = _C2900BandwidthUsageMaxPeakEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 5, 2),
    _C2900BandwidthUsageMaxPeakEntries_Type()
)
c2900BandwidthUsageMaxPeakEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900BandwidthUsageMaxPeakEntries.setStatus("current")


class _C2900BandwidthUsagePeakInterval_Type(Integer32):
    """Custom type c2900BandwidthUsagePeakInterval based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              6,
              12,
              24,
              48,
              72,
              96,
              120,
              144,
              168)
        )
    )
    namedValues = NamedValues(
        *(("fivedays", 120),
          ("fourdays", 96),
          ("oneday", 24),
          ("onehour", 1),
          ("oneweek", 168),
          ("sixdays", 144),
          ("sixhours", 6),
          ("threedays", 72),
          ("threehours", 3),
          ("twelvehours", 12),
          ("twodays", 48))
    )


_C2900BandwidthUsagePeakInterval_Type.__name__ = "Integer32"
_C2900BandwidthUsagePeakInterval_Object = MibScalar
c2900BandwidthUsagePeakInterval = _C2900BandwidthUsagePeakInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 5, 3),
    _C2900BandwidthUsagePeakInterval_Type()
)
c2900BandwidthUsagePeakInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2900BandwidthUsagePeakInterval.setStatus("current")
_C2900BandwidthUsagePeakRestart_Type = TruthValue
_C2900BandwidthUsagePeakRestart_Object = MibScalar
c2900BandwidthUsagePeakRestart = _C2900BandwidthUsagePeakRestart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 5, 4),
    _C2900BandwidthUsagePeakRestart_Type()
)
c2900BandwidthUsagePeakRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c2900BandwidthUsagePeakRestart.setStatus("current")
_C2900BandwidthUsageCurrentPeakEntry_Type = Gauge32
_C2900BandwidthUsageCurrentPeakEntry_Object = MibScalar
c2900BandwidthUsageCurrentPeakEntry = _C2900BandwidthUsageCurrentPeakEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 5, 5),
    _C2900BandwidthUsageCurrentPeakEntry_Type()
)
c2900BandwidthUsageCurrentPeakEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900BandwidthUsageCurrentPeakEntry.setStatus("current")
_C2900BandwidthUsagePeakTable_Object = MibTable
c2900BandwidthUsagePeakTable = _C2900BandwidthUsagePeakTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 5, 6)
)
if mibBuilder.loadTexts:
    c2900BandwidthUsagePeakTable.setStatus("current")
_C2900BandwidthUsagePeakEntry_Object = MibTableRow
c2900BandwidthUsagePeakEntry = _C2900BandwidthUsagePeakEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 5, 6, 1)
)
c2900BandwidthUsagePeakEntry.setIndexNames(
    (0, "CISCO-C2900-MIB", "c2900BandwidthUsagePeakIndex"),
)
if mibBuilder.loadTexts:
    c2900BandwidthUsagePeakEntry.setStatus("current")


class _C2900BandwidthUsagePeakIndex_Type(Integer32):
    """Custom type c2900BandwidthUsagePeakIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_C2900BandwidthUsagePeakIndex_Type.__name__ = "Integer32"
_C2900BandwidthUsagePeakIndex_Object = MibTableColumn
c2900BandwidthUsagePeakIndex = _C2900BandwidthUsagePeakIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 5, 6, 1, 1),
    _C2900BandwidthUsagePeakIndex_Type()
)
c2900BandwidthUsagePeakIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900BandwidthUsagePeakIndex.setStatus("current")
_C2900BandwidthUsageStartTime_Type = DateAndTime
_C2900BandwidthUsageStartTime_Object = MibTableColumn
c2900BandwidthUsageStartTime = _C2900BandwidthUsageStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 5, 6, 1, 2),
    _C2900BandwidthUsageStartTime_Type()
)
c2900BandwidthUsageStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900BandwidthUsageStartTime.setStatus("current")
_C2900BandwidthUsagePeak_Type = Gauge32
_C2900BandwidthUsagePeak_Object = MibTableColumn
c2900BandwidthUsagePeak = _C2900BandwidthUsagePeak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 5, 6, 1, 3),
    _C2900BandwidthUsagePeak_Type()
)
c2900BandwidthUsagePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900BandwidthUsagePeak.setStatus("current")
if mibBuilder.loadTexts:
    c2900BandwidthUsagePeak.setUnits("megabits per second")
_C2900BandwidthUsagePeakTime_Type = DateAndTime
_C2900BandwidthUsagePeakTime_Object = MibTableColumn
c2900BandwidthUsagePeakTime = _C2900BandwidthUsagePeakTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 1, 5, 6, 1, 4),
    _C2900BandwidthUsagePeakTime_Type()
)
c2900BandwidthUsagePeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c2900BandwidthUsagePeakTime.setStatus("current")
_C2900MibNotifications_ObjectIdentity = ObjectIdentity
c2900MibNotifications = _C2900MibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 2)
)
_C2900MibNotificationsPrefix_ObjectIdentity = ObjectIdentity
c2900MibNotificationsPrefix = _C2900MibNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 2, 0)
)
_C2900MIBConformance_ObjectIdentity = ObjectIdentity
c2900MIBConformance = _C2900MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 3)
)
_C2900MIBCompliances_ObjectIdentity = ObjectIdentity
c2900MIBCompliances = _C2900MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 3, 1)
)
_C2900MIBGroups_ObjectIdentity = ObjectIdentity
c2900MIBGroups = _C2900MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 3, 2)
)

# Managed Objects groups

c2900SysInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 3, 2, 1)
)
c2900SysInfoGroup.setObjects(
      *(("CISCO-C2900-MIB", "c2900InfoBoardRevision"),
        ("CISCO-C2900-MIB", "c2900InfoPeakBuffersUsed"),
        ("CISCO-C2900-MIB", "c2900InfoTotalBufferDepth"),
        ("CISCO-C2900-MIB", "c2900InfoAddrCapacity"),
        ("CISCO-C2900-MIB", "c2900InfoRestrictedStaticAddrCapacity"),
        ("CISCO-C2900-MIB", "c2900InfoSelfTestFailed"),
        ("CISCO-C2900-MIB", "c2900InfoUtilDisplay"),
        ("CISCO-C2900-MIB", "c2900InfoVisualIndicatorMode"),
        ("CISCO-C2900-MIB", "c2900InfoRedunantPowerSupplyInfo"),
        ("CISCO-C2900-MIB", "c2900InfoBoardIdentifier"))
)
if mibBuilder.loadTexts:
    c2900SysInfoGroup.setStatus("current")

c2900SysConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 3, 2, 2)
)
c2900SysConfigGroup.setObjects(
      *(("CISCO-C2900-MIB", "c2900ConfigAddressViolationAction"),
        ("CISCO-C2900-MIB", "c2900ConfigBroadcastStormAlarm"))
)
if mibBuilder.loadTexts:
    c2900SysConfigGroup.setStatus("deprecated")

c2900ModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 3, 2, 3)
)
c2900ModuleGroup.setObjects(
      *(("CISCO-C2900-MIB", "c2900ModuleStatus"),
        ("CISCO-C2900-MIB", "c2900ModuleType"),
        ("CISCO-C2900-MIB", "c2900ModuleHwVersion"),
        ("CISCO-C2900-MIB", "c2900ModuleSwVersion"))
)
if mibBuilder.loadTexts:
    c2900ModuleGroup.setStatus("current")

c2900PortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 3, 2, 4)
)
c2900PortGroup.setObjects(
      *(("CISCO-C2900-MIB", "c2900PortUsageApplication"),
        ("CISCO-C2900-MIB", "c2900PortGroupIndex"),
        ("CISCO-C2900-MIB", "c2900PortMayLearnAddress"),
        ("CISCO-C2900-MIB", "c2900PortMayForwardFrames"),
        ("CISCO-C2900-MIB", "c2900PortBufferCongestionControl"),
        ("CISCO-C2900-MIB", "c2900PortBufferCongestionThreshholdPercent"),
        ("CISCO-C2900-MIB", "c2900PortFrameAge"),
        ("CISCO-C2900-MIB", "c2900PortAddrSecureMaxAddresses"),
        ("CISCO-C2900-MIB", "c2900PortAddrSecureCurrentAddresses"),
        ("CISCO-C2900-MIB", "c2900PortAddrSecureAddrViolations"),
        ("CISCO-C2900-MIB", "c2900PortNumberOfLearnedAddresses"),
        ("CISCO-C2900-MIB", "c2900PortNumberOfDroppedAddresses"),
        ("CISCO-C2900-MIB", "c2900PortClearAddresses"),
        ("CISCO-C2900-MIB", "c2900PortFloodUnknownMulticasts"),
        ("CISCO-C2900-MIB", "c2900PortFloodUnknownUnicasts"),
        ("CISCO-C2900-MIB", "c2900PortLinkbeatStatus"),
        ("CISCO-C2900-MIB", "c2900PortBroadcastStormAction"),
        ("CISCO-C2900-MIB", "c2900PortBroadcastRisingThreshold"),
        ("CISCO-C2900-MIB", "c2900PortBroadcastFallingThreshold"),
        ("CISCO-C2900-MIB", "c2900PortStatus"),
        ("CISCO-C2900-MIB", "c2900PortTestResult"),
        ("CISCO-C2900-MIB", "c2900PortVisualIndicator"),
        ("CISCO-C2900-MIB", "c2900PortIfIndex"),
        ("CISCO-C2900-MIB", "c2900PortAddressViolationAction"),
        ("CISCO-C2900-MIB", "c2900PortBroadcastStormAlarm"),
        ("CISCO-C2900-MIB", "c2900PortMonitorDestinationPort"),
        ("CISCO-C2900-MIB", "c2900PortSwitchPortIndex"),
        ("CISCO-C2900-MIB", "c2900PortMonitoredPortMap"),
        ("CISCO-C2900-MIB", "c2900PortDuplexState"),
        ("CISCO-C2900-MIB", "c2900PortDuplexStatus"),
        ("CISCO-C2900-MIB", "c2900PortAdminSpeed"),
        ("CISCO-C2900-MIB", "c2900PortNoMonitorDestinationPort"))
)
if mibBuilder.loadTexts:
    c2900PortGroup.setStatus("deprecated")

c2900PortStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 3, 2, 5)
)
c2900PortStatsGroup.setObjects(
      *(("CISCO-C2900-MIB", "c2900PortRxNoBwFrames"),
        ("CISCO-C2900-MIB", "c2900PortRxNoBufferFrames"),
        ("CISCO-C2900-MIB", "c2900PortRxNoDestUniFrames"),
        ("CISCO-C2900-MIB", "c2900PortRxNoDestMultiFrames"),
        ("CISCO-C2900-MIB", "c2900PortRxSuppressBcastFrames"),
        ("CISCO-C2900-MIB", "c2900PortRxFcsErrFrames"),
        ("CISCO-C2900-MIB", "c2900PortCollFragFrames"),
        ("CISCO-C2900-MIB", "c2900PortTxMulticastFrames"),
        ("CISCO-C2900-MIB", "c2900PortTxBroadcastFrames"))
)
if mibBuilder.loadTexts:
    c2900PortStatsGroup.setStatus("deprecated")

c2900BandwidthUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 3, 2, 6)
)
c2900BandwidthUsageGroup.setObjects(
      *(("CISCO-C2900-MIB", "c2900BandwidthUsageCurrent"),
        ("CISCO-C2900-MIB", "c2900BandwidthUsageMaxPeakEntries"),
        ("CISCO-C2900-MIB", "c2900BandwidthUsagePeakInterval"),
        ("CISCO-C2900-MIB", "c2900BandwidthUsagePeakRestart"),
        ("CISCO-C2900-MIB", "c2900BandwidthUsagePeakIndex"),
        ("CISCO-C2900-MIB", "c2900BandwidthUsageStartTime"),
        ("CISCO-C2900-MIB", "c2900BandwidthUsagePeak"),
        ("CISCO-C2900-MIB", "c2900BandwidthUsagePeakTime"),
        ("CISCO-C2900-MIB", "c2900BandwidthUsageCurrentPeakEntry"))
)
if mibBuilder.loadTexts:
    c2900BandwidthUsageGroup.setStatus("current")

c2900PortGroupSA3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 3, 2, 7)
)
c2900PortGroupSA3.setObjects(
      *(("CISCO-C2900-MIB", "c2900PortUsageApplication"),
        ("CISCO-C2900-MIB", "c2900PortGroupIndex"),
        ("CISCO-C2900-MIB", "c2900PortMayLearnAddress"),
        ("CISCO-C2900-MIB", "c2900PortMayForwardFrames"),
        ("CISCO-C2900-MIB", "c2900PortBufferCongestionThreshholdPercent"),
        ("CISCO-C2900-MIB", "c2900PortFrameAge"),
        ("CISCO-C2900-MIB", "c2900PortAddrSecureMaxAddresses"),
        ("CISCO-C2900-MIB", "c2900PortAddrSecureCurrentAddresses"),
        ("CISCO-C2900-MIB", "c2900PortAddrSecureAddrViolations"),
        ("CISCO-C2900-MIB", "c2900PortNumberOfLearnedAddresses"),
        ("CISCO-C2900-MIB", "c2900PortNumberOfDroppedAddresses"),
        ("CISCO-C2900-MIB", "c2900PortClearAddresses"),
        ("CISCO-C2900-MIB", "c2900PortFloodUnknownMulticasts"),
        ("CISCO-C2900-MIB", "c2900PortFloodUnknownUnicasts"),
        ("CISCO-C2900-MIB", "c2900PortLinkbeatStatus"),
        ("CISCO-C2900-MIB", "c2900PortBroadcastStormAction"),
        ("CISCO-C2900-MIB", "c2900PortBroadcastRisingThreshold"),
        ("CISCO-C2900-MIB", "c2900PortBroadcastFallingThreshold"),
        ("CISCO-C2900-MIB", "c2900PortStatus"),
        ("CISCO-C2900-MIB", "c2900PortTestResult"),
        ("CISCO-C2900-MIB", "c2900PortVisualIndicator"),
        ("CISCO-C2900-MIB", "c2900PortIfIndex"),
        ("CISCO-C2900-MIB", "c2900PortAddressViolationAction"),
        ("CISCO-C2900-MIB", "c2900PortBroadcastStormAlarm"),
        ("CISCO-C2900-MIB", "c2900PortMonitorDestinationPort"),
        ("CISCO-C2900-MIB", "c2900PortSwitchPortIndex"),
        ("CISCO-C2900-MIB", "c2900PortMonitoredPortMap"),
        ("CISCO-C2900-MIB", "c2900PortDuplexState"),
        ("CISCO-C2900-MIB", "c2900PortDuplexStatus"),
        ("CISCO-C2900-MIB", "c2900PortAdminSpeed"),
        ("CISCO-C2900-MIB", "c2900PortNoMonitorDestinationPort"))
)
if mibBuilder.loadTexts:
    c2900PortGroupSA3.setStatus("deprecated")

c2900PortStatsGroupSA3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 3, 2, 8)
)
c2900PortStatsGroupSA3.setObjects(
      *(("CISCO-C2900-MIB", "c2900PortRxNoBwFrames"),
        ("CISCO-C2900-MIB", "c2900PortRxNoBufferFrames"),
        ("CISCO-C2900-MIB", "c2900PortRxNoDestUniFrames"),
        ("CISCO-C2900-MIB", "c2900PortRxNoDestMultiFrames"),
        ("CISCO-C2900-MIB", "c2900PortRxFcsErrFrames"),
        ("CISCO-C2900-MIB", "c2900PortCollFragFrames"),
        ("CISCO-C2900-MIB", "c2900PortTxMulticastFrames"),
        ("CISCO-C2900-MIB", "c2900PortTxBroadcastFrames"))
)
if mibBuilder.loadTexts:
    c2900PortStatsGroupSA3.setStatus("deprecated")

c2900PortGroupSA5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 3, 2, 9)
)
c2900PortGroupSA5.setObjects(
      *(("CISCO-C2900-MIB", "c2900PortUsageApplication"),
        ("CISCO-C2900-MIB", "c2900PortGroupIndex"),
        ("CISCO-C2900-MIB", "c2900PortMayForwardFrames"),
        ("CISCO-C2900-MIB", "c2900PortBufferCongestionThreshholdPercent"),
        ("CISCO-C2900-MIB", "c2900PortFrameAge"),
        ("CISCO-C2900-MIB", "c2900PortAddrSecureMaxAddresses"),
        ("CISCO-C2900-MIB", "c2900PortAddrSecureCurrentAddresses"),
        ("CISCO-C2900-MIB", "c2900PortAddrSecureAddrViolations"),
        ("CISCO-C2900-MIB", "c2900PortNumberOfLearnedAddresses"),
        ("CISCO-C2900-MIB", "c2900PortNumberOfDroppedAddresses"),
        ("CISCO-C2900-MIB", "c2900PortClearAddresses"),
        ("CISCO-C2900-MIB", "c2900PortFloodUnknownMulticasts"),
        ("CISCO-C2900-MIB", "c2900PortFloodUnknownUnicasts"),
        ("CISCO-C2900-MIB", "c2900PortLinkbeatStatus"),
        ("CISCO-C2900-MIB", "c2900PortBroadcastStormAction"),
        ("CISCO-C2900-MIB", "c2900PortBroadcastRisingThreshold"),
        ("CISCO-C2900-MIB", "c2900PortBroadcastFallingThreshold"),
        ("CISCO-C2900-MIB", "c2900PortStatus"),
        ("CISCO-C2900-MIB", "c2900PortTestResult"),
        ("CISCO-C2900-MIB", "c2900PortVisualIndicator"),
        ("CISCO-C2900-MIB", "c2900PortIfIndex"),
        ("CISCO-C2900-MIB", "c2900PortAddressViolationAction"),
        ("CISCO-C2900-MIB", "c2900PortBroadcastStormAlarm"),
        ("CISCO-C2900-MIB", "c2900PortMonitorDestinationPort"),
        ("CISCO-C2900-MIB", "c2900PortSwitchPortIndex"),
        ("CISCO-C2900-MIB", "c2900PortMonitoredPortMap"),
        ("CISCO-C2900-MIB", "c2900PortDuplexState"),
        ("CISCO-C2900-MIB", "c2900PortDuplexStatus"),
        ("CISCO-C2900-MIB", "c2900PortAdminSpeed"),
        ("CISCO-C2900-MIB", "c2900PortNoMonitorDestinationPort"),
        ("CISCO-C2900-MIB", "c2900Portdot1dBasePort"))
)
if mibBuilder.loadTexts:
    c2900PortGroupSA5.setStatus("deprecated")

c2900PortGroupSA7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 3, 2, 10)
)
c2900PortGroupSA7.setObjects(
      *(("CISCO-C2900-MIB", "c2900PortUsageApplication"),
        ("CISCO-C2900-MIB", "c2900PortGroupIndex"),
        ("CISCO-C2900-MIB", "c2900PortMayForwardFrames"),
        ("CISCO-C2900-MIB", "c2900PortBufferCongestionThreshholdPercent"),
        ("CISCO-C2900-MIB", "c2900PortFrameAge"),
        ("CISCO-C2900-MIB", "c2900PortAddrSecureMaxAddresses"),
        ("CISCO-C2900-MIB", "c2900PortAddrSecureCurrentAddresses"),
        ("CISCO-C2900-MIB", "c2900PortAddrSecureAddrViolations"),
        ("CISCO-C2900-MIB", "c2900PortNumberOfLearnedAddresses"),
        ("CISCO-C2900-MIB", "c2900PortNumberOfDroppedAddresses"),
        ("CISCO-C2900-MIB", "c2900PortClearAddresses"),
        ("CISCO-C2900-MIB", "c2900PortFloodUnknownMulticasts"),
        ("CISCO-C2900-MIB", "c2900PortFloodUnknownUnicasts"),
        ("CISCO-C2900-MIB", "c2900PortLinkbeatStatus"),
        ("CISCO-C2900-MIB", "c2900PortBroadcastStormAction"),
        ("CISCO-C2900-MIB", "c2900PortBroadcastRisingThreshold"),
        ("CISCO-C2900-MIB", "c2900PortBroadcastFallingThreshold"),
        ("CISCO-C2900-MIB", "c2900PortStatus"),
        ("CISCO-C2900-MIB", "c2900PortTestResult"),
        ("CISCO-C2900-MIB", "c2900PortVisualIndicator"),
        ("CISCO-C2900-MIB", "c2900PortIfIndex"),
        ("CISCO-C2900-MIB", "c2900PortAddressViolationAction"),
        ("CISCO-C2900-MIB", "c2900PortBroadcastStormAlarm"),
        ("CISCO-C2900-MIB", "c2900PortMonitorDestinationPort"),
        ("CISCO-C2900-MIB", "c2900PortSwitchPortIndex"),
        ("CISCO-C2900-MIB", "c2900PortMonitoredPortMap"),
        ("CISCO-C2900-MIB", "c2900PortDuplexState"),
        ("CISCO-C2900-MIB", "c2900PortDuplexStatus"),
        ("CISCO-C2900-MIB", "c2900PortAdminSpeed"),
        ("CISCO-C2900-MIB", "c2900PortNoMonitorDestinationPort"),
        ("CISCO-C2900-MIB", "c2900Portdot1dBasePort"),
        ("CISCO-C2900-MIB", "c2900PortSpantreeFastStart"))
)
if mibBuilder.loadTexts:
    c2900PortGroupSA7.setStatus("deprecated")

c2900PortGroupWC2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 3, 2, 11)
)
c2900PortGroupWC2.setObjects(
      *(("CISCO-C2900-MIB", "c2900PortUsageApplication"),
        ("CISCO-C2900-MIB", "c2900PortGroupIndex"),
        ("CISCO-C2900-MIB", "c2900PortMayForwardFrames"),
        ("CISCO-C2900-MIB", "c2900PortBufferCongestionThreshholdPercent"),
        ("CISCO-C2900-MIB", "c2900PortFrameAge"),
        ("CISCO-C2900-MIB", "c2900PortAddrSecureMaxAddresses"),
        ("CISCO-C2900-MIB", "c2900PortAddrSecureCurrentAddresses"),
        ("CISCO-C2900-MIB", "c2900PortAddrSecureAddrViolations"),
        ("CISCO-C2900-MIB", "c2900PortNumberOfLearnedAddresses"),
        ("CISCO-C2900-MIB", "c2900PortNumberOfDroppedAddresses"),
        ("CISCO-C2900-MIB", "c2900PortClearAddresses"),
        ("CISCO-C2900-MIB", "c2900PortFloodUnknownMulticasts"),
        ("CISCO-C2900-MIB", "c2900PortFloodUnknownUnicasts"),
        ("CISCO-C2900-MIB", "c2900PortLinkbeatStatus"),
        ("CISCO-C2900-MIB", "c2900PortBroadcastStormAction"),
        ("CISCO-C2900-MIB", "c2900PortBroadcastRisingThreshold"),
        ("CISCO-C2900-MIB", "c2900PortBroadcastFallingThreshold"),
        ("CISCO-C2900-MIB", "c2900PortStatus"),
        ("CISCO-C2900-MIB", "c2900PortTestResult"),
        ("CISCO-C2900-MIB", "c2900PortVisualIndicator"),
        ("CISCO-C2900-MIB", "c2900PortIfIndex"),
        ("CISCO-C2900-MIB", "c2900PortAddressViolationAction"),
        ("CISCO-C2900-MIB", "c2900PortBroadcastStormAlarm"),
        ("CISCO-C2900-MIB", "c2900PortMonitorDestinationPort"),
        ("CISCO-C2900-MIB", "c2900PortSwitchPortIndex"),
        ("CISCO-C2900-MIB", "c2900PortMonitoredPortMap"),
        ("CISCO-C2900-MIB", "c2900PortDuplexState"),
        ("CISCO-C2900-MIB", "c2900PortDuplexStatus"),
        ("CISCO-C2900-MIB", "c2900PortAdminSpeed"),
        ("CISCO-C2900-MIB", "c2900PortNoMonitorDestinationPort"),
        ("CISCO-C2900-MIB", "c2900Portdot1dBasePort"),
        ("CISCO-C2900-MIB", "c2900PortSpantreeFastStart"),
        ("CISCO-C2900-MIB", "c2900PortVoiceVlanId"))
)
if mibBuilder.loadTexts:
    c2900PortGroupWC2.setStatus("deprecated")

c2900PortGroupWC4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 3, 2, 12)
)
c2900PortGroupWC4.setObjects(
      *(("CISCO-C2900-MIB", "c2900PortUsageApplication"),
        ("CISCO-C2900-MIB", "c2900PortGroupIndex"),
        ("CISCO-C2900-MIB", "c2900PortMayForwardFrames"),
        ("CISCO-C2900-MIB", "c2900PortBufferCongestionThreshholdPercent"),
        ("CISCO-C2900-MIB", "c2900PortFrameAge"),
        ("CISCO-C2900-MIB", "c2900PortAddrSecureMaxAddresses"),
        ("CISCO-C2900-MIB", "c2900PortAddrSecureCurrentAddresses"),
        ("CISCO-C2900-MIB", "c2900PortAddrSecureAddrViolations"),
        ("CISCO-C2900-MIB", "c2900PortNumberOfLearnedAddresses"),
        ("CISCO-C2900-MIB", "c2900PortNumberOfDroppedAddresses"),
        ("CISCO-C2900-MIB", "c2900PortClearAddresses"),
        ("CISCO-C2900-MIB", "c2900PortFloodUnknownMulticasts"),
        ("CISCO-C2900-MIB", "c2900PortFloodUnknownUnicasts"),
        ("CISCO-C2900-MIB", "c2900PortLinkbeatStatus"),
        ("CISCO-C2900-MIB", "c2900PortBroadcastStormAction"),
        ("CISCO-C2900-MIB", "c2900PortBroadcastRisingThreshold"),
        ("CISCO-C2900-MIB", "c2900PortBroadcastFallingThreshold"),
        ("CISCO-C2900-MIB", "c2900PortStatus"),
        ("CISCO-C2900-MIB", "c2900PortTestResult"),
        ("CISCO-C2900-MIB", "c2900PortVisualIndicator"),
        ("CISCO-C2900-MIB", "c2900PortIfIndex"),
        ("CISCO-C2900-MIB", "c2900PortAddressViolationAction"),
        ("CISCO-C2900-MIB", "c2900PortBroadcastStormAlarm"),
        ("CISCO-C2900-MIB", "c2900PortMonitorDestinationPort"),
        ("CISCO-C2900-MIB", "c2900PortSwitchPortIndex"),
        ("CISCO-C2900-MIB", "c2900PortMonitoredPortMap"),
        ("CISCO-C2900-MIB", "c2900PortDuplexState"),
        ("CISCO-C2900-MIB", "c2900PortDuplexStatus"),
        ("CISCO-C2900-MIB", "c2900PortAdminSpeed"),
        ("CISCO-C2900-MIB", "c2900PortNoMonitorDestinationPort"),
        ("CISCO-C2900-MIB", "c2900Portdot1dBasePort"),
        ("CISCO-C2900-MIB", "c2900PortSpantreeFastStart"),
        ("CISCO-C2900-MIB", "c2900PortVoiceVlanId"),
        ("CISCO-C2900-MIB", "c2900PortAddrSecureAgingTime"),
        ("CISCO-C2900-MIB", "c2900PortAddrSecureAgingType"),
        ("CISCO-C2900-MIB", "c2900PortAddrSecureAgingStatic"))
)
if mibBuilder.loadTexts:
    c2900PortGroupWC4.setStatus("current")

c2900PortStatsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 3, 2, 14)
)
c2900PortStatsGroupRev1.setObjects(
      *(("CISCO-C2900-MIB", "c2900PortRxNoBwFrames"),
        ("CISCO-C2900-MIB", "c2900PortRxNoBufferFrames"),
        ("CISCO-C2900-MIB", "c2900PortRxNoDestUniFrames"),
        ("CISCO-C2900-MIB", "c2900PortRxNoDestMultiFrames"),
        ("CISCO-C2900-MIB", "c2900PortRxFcsErrFrames"),
        ("CISCO-C2900-MIB", "c2900PortCollFragFrames"),
        ("CISCO-C2900-MIB", "c2900PortTxMulticastFrames"),
        ("CISCO-C2900-MIB", "c2900PortTxBroadcastFrames"))
)
if mibBuilder.loadTexts:
    c2900PortStatsGroupRev1.setStatus("current")


# Notification objects

c2900AddressViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 2, 0, 1)
)
c2900AddressViolation.setObjects(
    ("CISCO-C2900-MIB", "c2900PortIfIndex")
)
if mibBuilder.loadTexts:
    c2900AddressViolation.setStatus(
        "current"
    )

c2900BroadcastStorm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 2, 0, 2)
)
c2900BroadcastStorm.setObjects(
    ("CISCO-C2900-MIB", "c2900PortBroadcastRisingThreshold")
)
if mibBuilder.loadTexts:
    c2900BroadcastStorm.setStatus(
        "current"
    )

c2900RpsFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 2, 0, 3)
)
c2900RpsFailed.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    c2900RpsFailed.setStatus(
        "current"
    )


# Notifications groups

c2900NotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 3, 2, 13)
)
c2900NotificationsGroup.setObjects(
      *(("CISCO-C2900-MIB", "c2900AddressViolation"),
        ("CISCO-C2900-MIB", "c2900BroadcastStorm"),
        ("CISCO-C2900-MIB", "c2900RpsFailed"))
)
if mibBuilder.loadTexts:
    c2900NotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

c2900MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 3, 1, 1)
)
if mibBuilder.loadTexts:
    c2900MIBCompliance.setStatus(
        "deprecated"
    )

c2900MIBComplianceSA5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 3, 1, 2)
)
if mibBuilder.loadTexts:
    c2900MIBComplianceSA5.setStatus(
        "deprecated"
    )

c2900MIBComplianceSA3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 3, 1, 3)
)
if mibBuilder.loadTexts:
    c2900MIBComplianceSA3.setStatus(
        "deprecated"
    )

c2900MIBComplianceSA7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 3, 1, 4)
)
if mibBuilder.loadTexts:
    c2900MIBComplianceSA7.setStatus(
        "deprecated"
    )

c2900MIBComplianceWC2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 3, 1, 5)
)
if mibBuilder.loadTexts:
    c2900MIBComplianceWC2.setStatus(
        "deprecated"
    )

c2900MIBComplianceWC4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 87, 3, 1, 6)
)
if mibBuilder.loadTexts:
    c2900MIBComplianceWC4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-C2900-MIB",
    **{"ciscoC2900MIB": ciscoC2900MIB,
       "c2900MIBObjects": c2900MIBObjects,
       "c2900SysInfo": c2900SysInfo,
       "c2900InfoBoardRevision": c2900InfoBoardRevision,
       "c2900InfoPeakBuffersUsed": c2900InfoPeakBuffersUsed,
       "c2900InfoTotalBufferDepth": c2900InfoTotalBufferDepth,
       "c2900InfoAddrCapacity": c2900InfoAddrCapacity,
       "c2900InfoRestrictedStaticAddrCapacity": c2900InfoRestrictedStaticAddrCapacity,
       "c2900InfoSelfTestFailed": c2900InfoSelfTestFailed,
       "c2900InfoUtilDisplay": c2900InfoUtilDisplay,
       "c2900InfoVisualIndicatorMode": c2900InfoVisualIndicatorMode,
       "c2900InfoRedunantPowerSupplyInfo": c2900InfoRedunantPowerSupplyInfo,
       "c2900InfoBoardIdentifier": c2900InfoBoardIdentifier,
       "c2900SysConfig": c2900SysConfig,
       "c2900ConfigAddressViolationAction": c2900ConfigAddressViolationAction,
       "c2900ConfigBroadcastStormAlarm": c2900ConfigBroadcastStormAlarm,
       "c2900ModuleTable": c2900ModuleTable,
       "c2900ModuleEntry": c2900ModuleEntry,
       "c2900ModuleIndex": c2900ModuleIndex,
       "c2900ModuleStatus": c2900ModuleStatus,
       "c2900ModuleType": c2900ModuleType,
       "c2900ModuleHwVersion": c2900ModuleHwVersion,
       "c2900ModuleSwVersion": c2900ModuleSwVersion,
       "c2900Port": c2900Port,
       "c2900PortTable": c2900PortTable,
       "c2900PortEntry": c2900PortEntry,
       "c2900PortModuleIndex": c2900PortModuleIndex,
       "c2900PortIndex": c2900PortIndex,
       "c2900PortUsageApplication": c2900PortUsageApplication,
       "c2900PortGroupIndex": c2900PortGroupIndex,
       "c2900PortMayLearnAddress": c2900PortMayLearnAddress,
       "c2900PortMayForwardFrames": c2900PortMayForwardFrames,
       "c2900PortBufferCongestionControl": c2900PortBufferCongestionControl,
       "c2900PortBufferCongestionThreshholdPercent": c2900PortBufferCongestionThreshholdPercent,
       "c2900PortFrameAge": c2900PortFrameAge,
       "c2900PortAddrSecureMaxAddresses": c2900PortAddrSecureMaxAddresses,
       "c2900PortAddrSecureCurrentAddresses": c2900PortAddrSecureCurrentAddresses,
       "c2900PortAddrSecureAddrViolations": c2900PortAddrSecureAddrViolations,
       "c2900PortNumberOfLearnedAddresses": c2900PortNumberOfLearnedAddresses,
       "c2900PortNumberOfDroppedAddresses": c2900PortNumberOfDroppedAddresses,
       "c2900PortClearAddresses": c2900PortClearAddresses,
       "c2900PortFloodUnknownMulticasts": c2900PortFloodUnknownMulticasts,
       "c2900PortFloodUnknownUnicasts": c2900PortFloodUnknownUnicasts,
       "c2900PortLinkbeatStatus": c2900PortLinkbeatStatus,
       "c2900PortBroadcastStormAction": c2900PortBroadcastStormAction,
       "c2900PortBroadcastRisingThreshold": c2900PortBroadcastRisingThreshold,
       "c2900PortBroadcastFallingThreshold": c2900PortBroadcastFallingThreshold,
       "c2900PortStatus": c2900PortStatus,
       "c2900PortTestResult": c2900PortTestResult,
       "c2900PortVisualIndicator": c2900PortVisualIndicator,
       "c2900PortIfIndex": c2900PortIfIndex,
       "c2900PortAddressViolationAction": c2900PortAddressViolationAction,
       "c2900PortBroadcastStormAlarm": c2900PortBroadcastStormAlarm,
       "c2900PortMonitorDestinationPort": c2900PortMonitorDestinationPort,
       "c2900PortSwitchPortIndex": c2900PortSwitchPortIndex,
       "c2900PortMonitoredPortMap": c2900PortMonitoredPortMap,
       "c2900PortDuplexState": c2900PortDuplexState,
       "c2900PortDuplexStatus": c2900PortDuplexStatus,
       "c2900PortAdminSpeed": c2900PortAdminSpeed,
       "c2900PortNoMonitorDestinationPort": c2900PortNoMonitorDestinationPort,
       "c2900Portdot1dBasePort": c2900Portdot1dBasePort,
       "c2900PortSpantreeFastStart": c2900PortSpantreeFastStart,
       "c2900PortVoiceVlanId": c2900PortVoiceVlanId,
       "c2900PortAddrSecureAgingTime": c2900PortAddrSecureAgingTime,
       "c2900PortAddrSecureAgingType": c2900PortAddrSecureAgingType,
       "c2900PortAddrSecureAgingStatic": c2900PortAddrSecureAgingStatic,
       "c2900PortStatsTable": c2900PortStatsTable,
       "c2900PortStatsEntry": c2900PortStatsEntry,
       "c2900PortRxNoBwFrames": c2900PortRxNoBwFrames,
       "c2900PortRxNoBufferFrames": c2900PortRxNoBufferFrames,
       "c2900PortRxNoDestUniFrames": c2900PortRxNoDestUniFrames,
       "c2900PortRxNoDestMultiFrames": c2900PortRxNoDestMultiFrames,
       "c2900PortRxSuppressBcastFrames": c2900PortRxSuppressBcastFrames,
       "c2900PortRxFcsErrFrames": c2900PortRxFcsErrFrames,
       "c2900PortCollFragFrames": c2900PortCollFragFrames,
       "c2900PortTxMulticastFrames": c2900PortTxMulticastFrames,
       "c2900PortTxBroadcastFrames": c2900PortTxBroadcastFrames,
       "c2900BandwidthUsage": c2900BandwidthUsage,
       "c2900BandwidthUsageCurrent": c2900BandwidthUsageCurrent,
       "c2900BandwidthUsageMaxPeakEntries": c2900BandwidthUsageMaxPeakEntries,
       "c2900BandwidthUsagePeakInterval": c2900BandwidthUsagePeakInterval,
       "c2900BandwidthUsagePeakRestart": c2900BandwidthUsagePeakRestart,
       "c2900BandwidthUsageCurrentPeakEntry": c2900BandwidthUsageCurrentPeakEntry,
       "c2900BandwidthUsagePeakTable": c2900BandwidthUsagePeakTable,
       "c2900BandwidthUsagePeakEntry": c2900BandwidthUsagePeakEntry,
       "c2900BandwidthUsagePeakIndex": c2900BandwidthUsagePeakIndex,
       "c2900BandwidthUsageStartTime": c2900BandwidthUsageStartTime,
       "c2900BandwidthUsagePeak": c2900BandwidthUsagePeak,
       "c2900BandwidthUsagePeakTime": c2900BandwidthUsagePeakTime,
       "c2900MibNotifications": c2900MibNotifications,
       "c2900MibNotificationsPrefix": c2900MibNotificationsPrefix,
       "c2900AddressViolation": c2900AddressViolation,
       "c2900BroadcastStorm": c2900BroadcastStorm,
       "c2900RpsFailed": c2900RpsFailed,
       "c2900MIBConformance": c2900MIBConformance,
       "c2900MIBCompliances": c2900MIBCompliances,
       "c2900MIBCompliance": c2900MIBCompliance,
       "c2900MIBComplianceSA5": c2900MIBComplianceSA5,
       "c2900MIBComplianceSA3": c2900MIBComplianceSA3,
       "c2900MIBComplianceSA7": c2900MIBComplianceSA7,
       "c2900MIBComplianceWC2": c2900MIBComplianceWC2,
       "c2900MIBComplianceWC4": c2900MIBComplianceWC4,
       "c2900MIBGroups": c2900MIBGroups,
       "c2900SysInfoGroup": c2900SysInfoGroup,
       "c2900SysConfigGroup": c2900SysConfigGroup,
       "c2900ModuleGroup": c2900ModuleGroup,
       "c2900PortGroup": c2900PortGroup,
       "c2900PortStatsGroup": c2900PortStatsGroup,
       "c2900BandwidthUsageGroup": c2900BandwidthUsageGroup,
       "c2900PortGroupSA3": c2900PortGroupSA3,
       "c2900PortStatsGroupSA3": c2900PortStatsGroupSA3,
       "c2900PortGroupSA5": c2900PortGroupSA5,
       "c2900PortGroupSA7": c2900PortGroupSA7,
       "c2900PortGroupWC2": c2900PortGroupWC2,
       "c2900PortGroupWC4": c2900PortGroupWC4,
       "c2900NotificationsGroup": c2900NotificationsGroup,
       "c2900PortStatsGroupRev1": c2900PortStatsGroupRev1}
)
