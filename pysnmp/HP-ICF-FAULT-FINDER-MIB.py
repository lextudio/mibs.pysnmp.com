# SNMP MIB module (HP-ICF-FAULT-FINDER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-FAULT-FINDER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:25 2024
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

(PhysicalClass,
 PhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalClass",
    "PhysicalIndex")

(hpicfCommon,
 hpicfCommonTrapsPrefix,
 hpicfObjectModules) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpicfCommon",
    "hpicfCommonTrapsPrefix",
    "hpicfObjectModules")

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


# MODULE-IDENTITY

hpicfFaultFinderMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12)
)
hpicfFaultFinderMib.setRevisions(
        ("2015-08-04 14:12",
         "2013-08-21 00:00",
         "2010-01-25 20:24",
         "2009-05-22 00:00",
         "2009-02-25 13:31",
         "2007-01-09 14:56",
         "2005-05-02 19:34",
         "2005-03-22 11:30",
         "2003-07-28 07:07",
         "2000-11-03 07:07",
         "1998-11-20 23:50",
         "1997-10-21 02:49")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpicfFaultType(Integer32, TextualConvention):
    status = "current"
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40)
        )
    )
    namedValues = NamedValues(
        *(("backupLinkTransition", 13),
          ("badCable", 3),
          ("badDriver", 1),
          ("badXcvr", 2),
          ("bcastStorm", 6),
          ("bcastStormPerPort", 38),
          ("crfBlocked", 28),
          ("crfNotify", 26),
          ("crfThrottled", 27),
          ("duplexMismatchFDX", 21),
          ("duplexMismatchHDX", 20),
          ("fanFault", 15),
          ("flowcntlJumbosFault", 22),
          ("hotSwapReboot", 19),
          ("intel82566dmportprotect", 34),
          ("linkFlap", 33),
          ("linkFlapPerPort", 39),
          ("lossOfLink", 11),
          ("lossOfStackMember", 18),
          ("meshingFault", 14),
          ("misconfiguredSQE", 8),
          ("networkLoop", 10),
          ("overBandwidth", 5),
          ("partition", 7),
          ("phyReadFailure", 32),
          ("polarityReversal", 9),
          ("portSecurityViolation", 12),
          ("portSelftestFailure", 23),
          ("rpsFault", 16),
          ("rxNonStdPreamble", 40),
          ("stuck10MbFault", 17),
          ("tooLongCable", 4),
          ("xcvrBRevOnly", 30),
          ("xcvrClone", 36),
          ("xcvrCloneReminder", 37),
          ("xcvrExceedQty", 35),
          ("xcvrNotSupportedOnPort", 31),
          ("xcvrNotYetSupported", 29),
          ("xcvrUnidentified", 24),
          ("xcvrUnsupported", 25))
    )



class HpicfFaultTolerance(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class HpicfFaultAction(Integer32, TextualConvention):
    status = "current"
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
        *(("none", 1),
          ("warn", 2),
          ("warnAndDisable", 3),
          ("warnAndSpeedReduce", 4),
          ("warnAndSpeedReduceAndDisable", 5))
    )



class HpicfUrlString(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_HpicfFaultFinderConformance_ObjectIdentity = ObjectIdentity
hpicfFaultFinderConformance = _HpicfFaultFinderConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1)
)
_HpicfFaultFinderCompliances_ObjectIdentity = ObjectIdentity
hpicfFaultFinderCompliances = _HpicfFaultFinderCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 1)
)
_HpicfFaultFinderGroups_ObjectIdentity = ObjectIdentity
hpicfFaultFinderGroups = _HpicfFaultFinderGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2)
)
_HpicfFaultFinder_ObjectIdentity = ObjectIdentity
hpicfFaultFinder = _HpicfFaultFinder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7)
)
_HpicfFfControlTable_Object = MibTable
hpicfFfControlTable = _HpicfFfControlTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hpicfFfControlTable.setStatus("current")
_HpicfFfControlEntry_Object = MibTableRow
hpicfFfControlEntry = _HpicfFfControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 1, 1)
)
hpicfFfControlEntry.setIndexNames(
    (0, "HP-ICF-FAULT-FINDER-MIB", "hpicfFfControlIndex"),
)
if mibBuilder.loadTexts:
    hpicfFfControlEntry.setStatus("current")
_HpicfFfControlIndex_Type = HpicfFaultType
_HpicfFfControlIndex_Object = MibTableColumn
hpicfFfControlIndex = _HpicfFfControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 1, 1, 1),
    _HpicfFfControlIndex_Type()
)
hpicfFfControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfFfControlIndex.setStatus("current")
_HpicfFfAction_Type = HpicfFaultAction
_HpicfFfAction_Object = MibTableColumn
hpicfFfAction = _HpicfFfAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 1, 1, 2),
    _HpicfFfAction_Type()
)
hpicfFfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfFfAction.setStatus("current")
_HpicfFfWarnTolerance_Type = HpicfFaultTolerance
_HpicfFfWarnTolerance_Object = MibTableColumn
hpicfFfWarnTolerance = _HpicfFfWarnTolerance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 1, 1, 3),
    _HpicfFfWarnTolerance_Type()
)
hpicfFfWarnTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfFfWarnTolerance.setStatus("current")
_HpicfFfDisablePortTolerance_Type = HpicfFaultTolerance
_HpicfFfDisablePortTolerance_Object = MibTableColumn
hpicfFfDisablePortTolerance = _HpicfFfDisablePortTolerance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 1, 1, 4),
    _HpicfFfDisablePortTolerance_Type()
)
hpicfFfDisablePortTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfFfDisablePortTolerance.setStatus("current")
_HpicfFfSpeedReduceTolerance_Type = HpicfFaultTolerance
_HpicfFfSpeedReduceTolerance_Object = MibTableColumn
hpicfFfSpeedReduceTolerance = _HpicfFfSpeedReduceTolerance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 1, 1, 5),
    _HpicfFfSpeedReduceTolerance_Type()
)
hpicfFfSpeedReduceTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfFfSpeedReduceTolerance.setStatus("current")
_HpicfFfLogTable_Object = MibTable
hpicfFfLogTable = _HpicfFfLogTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2)
)
if mibBuilder.loadTexts:
    hpicfFfLogTable.setStatus("current")
_HpicfFfLogEntry_Object = MibTableRow
hpicfFfLogEntry = _HpicfFfLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1)
)
hpicfFfLogEntry.setIndexNames(
    (0, "HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogIndex"),
)
if mibBuilder.loadTexts:
    hpicfFfLogEntry.setStatus("current")


class _HpicfFfLogIndex_Type(Integer32):
    """Custom type hpicfFfLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpicfFfLogIndex_Type.__name__ = "Integer32"
_HpicfFfLogIndex_Object = MibTableColumn
hpicfFfLogIndex = _HpicfFfLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 1),
    _HpicfFfLogIndex_Type()
)
hpicfFfLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfFfLogIndex.setStatus("current")
_HpicfFfLogCreateTime_Type = TimeStamp
_HpicfFfLogCreateTime_Object = MibTableColumn
hpicfFfLogCreateTime = _HpicfFfLogCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 2),
    _HpicfFfLogCreateTime_Type()
)
hpicfFfLogCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfFfLogCreateTime.setStatus("current")
_HpicfFfLogPhysEntity_Type = PhysicalIndex
_HpicfFfLogPhysEntity_Object = MibTableColumn
hpicfFfLogPhysEntity = _HpicfFfLogPhysEntity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 3),
    _HpicfFfLogPhysEntity_Type()
)
hpicfFfLogPhysEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfFfLogPhysEntity.setStatus("current")
_HpicfFfLogFaultType_Type = HpicfFaultType
_HpicfFfLogFaultType_Object = MibTableColumn
hpicfFfLogFaultType = _HpicfFfLogFaultType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 4),
    _HpicfFfLogFaultType_Type()
)
hpicfFfLogFaultType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfFfLogFaultType.setStatus("current")
_HpicfFfLogAction_Type = HpicfFaultAction
_HpicfFfLogAction_Object = MibTableColumn
hpicfFfLogAction = _HpicfFfLogAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 5),
    _HpicfFfLogAction_Type()
)
hpicfFfLogAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfFfLogAction.setStatus("current")


class _HpicfFfLogSeverity_Type(Integer32):
    """Custom type hpicfFfLogSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("informational", 1),
          ("medium", 2))
    )


_HpicfFfLogSeverity_Type.__name__ = "Integer32"
_HpicfFfLogSeverity_Object = MibTableColumn
hpicfFfLogSeverity = _HpicfFfLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 6),
    _HpicfFfLogSeverity_Type()
)
hpicfFfLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfFfLogSeverity.setStatus("current")


class _HpicfFfLogStatus_Type(Integer32):
    """Custom type hpicfFfLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("new", 1),
          ("old", 3))
    )


_HpicfFfLogStatus_Type.__name__ = "Integer32"
_HpicfFfLogStatus_Object = MibTableColumn
hpicfFfLogStatus = _HpicfFfLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 7),
    _HpicfFfLogStatus_Type()
)
hpicfFfLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfFfLogStatus.setStatus("current")
_HpicfFfLogPhysClass_Type = PhysicalClass
_HpicfFfLogPhysClass_Object = MibTableColumn
hpicfFfLogPhysClass = _HpicfFfLogPhysClass_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 8),
    _HpicfFfLogPhysClass_Type()
)
hpicfFfLogPhysClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfFfLogPhysClass.setStatus("current")


class _HpicfFfLogInfoType_Type(Integer32):
    """Custom type hpicfFfLogInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("displayString", 2),
          ("ipv4Address", 1))
    )


_HpicfFfLogInfoType_Type.__name__ = "Integer32"
_HpicfFfLogInfoType_Object = MibTableColumn
hpicfFfLogInfoType = _HpicfFfLogInfoType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 9),
    _HpicfFfLogInfoType_Type()
)
hpicfFfLogInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfFfLogInfoType.setStatus("current")


class _HpicfFfLogInfo_Type(OctetString):
    """Custom type hpicfFfLogInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfFfLogInfo_Type.__name__ = "OctetString"
_HpicfFfLogInfo_Object = MibTableColumn
hpicfFfLogInfo = _HpicfFfLogInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 10),
    _HpicfFfLogInfo_Type()
)
hpicfFfLogInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfFfLogInfo.setStatus("current")
_HpicfFfFaultInfoURL_Type = HpicfUrlString
_HpicfFfFaultInfoURL_Object = MibScalar
hpicfFfFaultInfoURL = _HpicfFfFaultInfoURL_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 3),
    _HpicfFfFaultInfoURL_Type()
)
hpicfFfFaultInfoURL.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfFfFaultInfoURL.setStatus("current")


class _HpicfFfFaultLightStatus_Type(Integer32):
    """Custom type hpicfFfFaultLightStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("faultLightOff", 1),
          ("faultLightOn", 2))
    )


_HpicfFfFaultLightStatus_Type.__name__ = "Integer32"
_HpicfFfFaultLightStatus_Object = MibScalar
hpicfFfFaultLightStatus = _HpicfFfFaultLightStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 4),
    _HpicfFfFaultLightStatus_Type()
)
hpicfFfFaultLightStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfFfFaultLightStatus.setStatus("current")
_HpicfFfBcastStormControlPortConfig_ObjectIdentity = ObjectIdentity
hpicfFfBcastStormControlPortConfig = _HpicfFfBcastStormControlPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 5)
)
_HpicfFfBcastStormControlPortConfigTable_Object = MibTable
hpicfFfBcastStormControlPortConfigTable = _HpicfFfBcastStormControlPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 5, 1)
)
if mibBuilder.loadTexts:
    hpicfFfBcastStormControlPortConfigTable.setStatus("current")
_HpicfFfBcastStormControlPortConfigEntry_Object = MibTableRow
hpicfFfBcastStormControlPortConfigEntry = _HpicfFfBcastStormControlPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 5, 1, 1)
)
hpicfFfBcastStormControlPortConfigEntry.setIndexNames(
    (0, "HP-ICF-FAULT-FINDER-MIB", "hpicfFfBcastStormControlPortIndex"),
)
if mibBuilder.loadTexts:
    hpicfFfBcastStormControlPortConfigEntry.setStatus("current")
_HpicfFfBcastStormControlPortIndex_Type = InterfaceIndex
_HpicfFfBcastStormControlPortIndex_Object = MibTableColumn
hpicfFfBcastStormControlPortIndex = _HpicfFfBcastStormControlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 5, 1, 1, 1),
    _HpicfFfBcastStormControlPortIndex_Type()
)
hpicfFfBcastStormControlPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfFfBcastStormControlPortIndex.setStatus("current")


class _HpicfFfBcastStormControlMode_Type(Integer32):
    """Custom type hpicfFfBcastStormControlMode based on Integer32"""
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
        *(("bcastRisingLevelpercent", 2),
          ("bcastRisingLevelpps", 3),
          ("disabled", 1))
    )


_HpicfFfBcastStormControlMode_Type.__name__ = "Integer32"
_HpicfFfBcastStormControlMode_Object = MibTableColumn
hpicfFfBcastStormControlMode = _HpicfFfBcastStormControlMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 5, 1, 1, 2),
    _HpicfFfBcastStormControlMode_Type()
)
hpicfFfBcastStormControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfFfBcastStormControlMode.setStatus("current")


class _HpicfFfBcastStormControlRisingpercent_Type(Integer32):
    """Custom type hpicfFfBcastStormControlRisingpercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HpicfFfBcastStormControlRisingpercent_Type.__name__ = "Integer32"
_HpicfFfBcastStormControlRisingpercent_Object = MibTableColumn
hpicfFfBcastStormControlRisingpercent = _HpicfFfBcastStormControlRisingpercent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 5, 1, 1, 3),
    _HpicfFfBcastStormControlRisingpercent_Type()
)
hpicfFfBcastStormControlRisingpercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfFfBcastStormControlRisingpercent.setStatus("current")


class _HpicfFfBcastStormControlRisingpps_Type(Integer32):
    """Custom type hpicfFfBcastStormControlRisingpps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000000),
    )


_HpicfFfBcastStormControlRisingpps_Type.__name__ = "Integer32"
_HpicfFfBcastStormControlRisingpps_Object = MibTableColumn
hpicfFfBcastStormControlRisingpps = _HpicfFfBcastStormControlRisingpps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 5, 1, 1, 4),
    _HpicfFfBcastStormControlRisingpps_Type()
)
hpicfFfBcastStormControlRisingpps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfFfBcastStormControlRisingpps.setStatus("current")


class _HpicfFfBcastStormControlAction_Type(Integer32):
    """Custom type hpicfFfBcastStormControlAction based on Integer32"""
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
        *(("none", 1),
          ("warn", 2),
          ("warnAndDisable", 3))
    )


_HpicfFfBcastStormControlAction_Type.__name__ = "Integer32"
_HpicfFfBcastStormControlAction_Object = MibTableColumn
hpicfFfBcastStormControlAction = _HpicfFfBcastStormControlAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 5, 1, 1, 5),
    _HpicfFfBcastStormControlAction_Type()
)
hpicfFfBcastStormControlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfFfBcastStormControlAction.setStatus("current")


class _HpicfFfBcastStormControlPortDisableTimer_Type(Unsigned32):
    """Custom type hpicfFfBcastStormControlPortDisableTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_HpicfFfBcastStormControlPortDisableTimer_Type.__name__ = "Unsigned32"
_HpicfFfBcastStormControlPortDisableTimer_Object = MibTableColumn
hpicfFfBcastStormControlPortDisableTimer = _HpicfFfBcastStormControlPortDisableTimer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 5, 1, 1, 6),
    _HpicfFfBcastStormControlPortDisableTimer_Type()
)
hpicfFfBcastStormControlPortDisableTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfFfBcastStormControlPortDisableTimer.setStatus("current")
if mibBuilder.loadTexts:
    hpicfFfBcastStormControlPortDisableTimer.setUnits("seconds")
_HpicfFfLinkFlapControlPortConfig_ObjectIdentity = ObjectIdentity
hpicfFfLinkFlapControlPortConfig = _HpicfFfLinkFlapControlPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 6)
)
_HpicfFfLinkFlapControlPortConfigTable_Object = MibTable
hpicfFfLinkFlapControlPortConfigTable = _HpicfFfLinkFlapControlPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 6, 1)
)
if mibBuilder.loadTexts:
    hpicfFfLinkFlapControlPortConfigTable.setStatus("current")
_HpicfFfLinkFlapControlPortConfigEntry_Object = MibTableRow
hpicfFfLinkFlapControlPortConfigEntry = _HpicfFfLinkFlapControlPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 6, 1, 1)
)
hpicfFfLinkFlapControlPortConfigEntry.setIndexNames(
    (0, "HP-ICF-FAULT-FINDER-MIB", "hpicfFfLinkFlapControlPortIndex"),
)
if mibBuilder.loadTexts:
    hpicfFfLinkFlapControlPortConfigEntry.setStatus("current")
_HpicfFfLinkFlapControlPortIndex_Type = InterfaceIndex
_HpicfFfLinkFlapControlPortIndex_Object = MibTableColumn
hpicfFfLinkFlapControlPortIndex = _HpicfFfLinkFlapControlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 6, 1, 1, 1),
    _HpicfFfLinkFlapControlPortIndex_Type()
)
hpicfFfLinkFlapControlPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfFfLinkFlapControlPortIndex.setStatus("current")


class _HpicfFfLinkFlapControlSensitivity_Type(Integer32):
    """Custom type hpicfFfLinkFlapControlSensitivity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              6,
              10)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 10),
          ("medium", 6),
          ("none", 0))
    )


_HpicfFfLinkFlapControlSensitivity_Type.__name__ = "Integer32"
_HpicfFfLinkFlapControlSensitivity_Object = MibTableColumn
hpicfFfLinkFlapControlSensitivity = _HpicfFfLinkFlapControlSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 6, 1, 1, 2),
    _HpicfFfLinkFlapControlSensitivity_Type()
)
hpicfFfLinkFlapControlSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfFfLinkFlapControlSensitivity.setStatus("current")


class _HpicfFfLinkFlapControlAction_Type(Integer32):
    """Custom type hpicfFfLinkFlapControlAction based on Integer32"""
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
        *(("none", 1),
          ("warn", 2),
          ("warnAndDisable", 3))
    )


_HpicfFfLinkFlapControlAction_Type.__name__ = "Integer32"
_HpicfFfLinkFlapControlAction_Object = MibTableColumn
hpicfFfLinkFlapControlAction = _HpicfFfLinkFlapControlAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 6, 1, 1, 3),
    _HpicfFfLinkFlapControlAction_Type()
)
hpicfFfLinkFlapControlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfFfLinkFlapControlAction.setStatus("current")


class _HpicfFfLinkFlapControlPortDisableTimer_Type(Unsigned32):
    """Custom type hpicfFfLinkFlapControlPortDisableTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_HpicfFfLinkFlapControlPortDisableTimer_Type.__name__ = "Unsigned32"
_HpicfFfLinkFlapControlPortDisableTimer_Object = MibTableColumn
hpicfFfLinkFlapControlPortDisableTimer = _HpicfFfLinkFlapControlPortDisableTimer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 6, 1, 1, 4),
    _HpicfFfLinkFlapControlPortDisableTimer_Type()
)
hpicfFfLinkFlapControlPortDisableTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfFfLinkFlapControlPortDisableTimer.setStatus("current")
if mibBuilder.loadTexts:
    hpicfFfLinkFlapControlPortDisableTimer.setUnits("seconds")

# Managed Objects groups

hpicfFaultConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2, 1)
)
hpicfFaultConfigGroup.setObjects(
      *(("HP-ICF-FAULT-FINDER-MIB", "hpicfFfAction"),
        ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfWarnTolerance"),
        ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfDisablePortTolerance"))
)
if mibBuilder.loadTexts:
    hpicfFaultConfigGroup.setStatus("current")

hpicfFaultLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2, 2)
)
hpicfFaultLogGroup.setObjects(
      *(("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogCreateTime"),
        ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogPhysEntity"),
        ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogFaultType"),
        ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogAction"),
        ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogSeverity"),
        ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogStatus"),
        ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfFaultInfoURL"),
        ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogPhysClass"),
        ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogInfoType"),
        ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogInfo"))
)
if mibBuilder.loadTexts:
    hpicfFaultLogGroup.setStatus("current")

hpicfFaultConfig2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2, 4)
)
hpicfFaultConfig2Group.setObjects(
      *(("HP-ICF-FAULT-FINDER-MIB", "hpicfFfAction"),
        ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfWarnTolerance"),
        ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfDisablePortTolerance"),
        ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfSpeedReduceTolerance"))
)
if mibBuilder.loadTexts:
    hpicfFaultConfig2Group.setStatus("current")

hpicfFaultStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2, 5)
)
hpicfFaultStatusGroup.setObjects(
    ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfFaultLightStatus")
)
if mibBuilder.loadTexts:
    hpicfFaultStatusGroup.setStatus("current")

hpicfFaultConfig3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2, 6)
)
hpicfFaultConfig3Group.setObjects(
      *(("HP-ICF-FAULT-FINDER-MIB", "hpicfFfBcastStormControlMode"),
        ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfBcastStormControlRisingpercent"),
        ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfBcastStormControlRisingpps"),
        ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfBcastStormControlAction"),
        ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfBcastStormControlPortDisableTimer"))
)
if mibBuilder.loadTexts:
    hpicfFaultConfig3Group.setStatus("current")

hpicfFaultConfig4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2, 7)
)
hpicfFaultConfig4Group.setObjects(
      *(("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLinkFlapControlSensitivity"),
        ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLinkFlapControlAction"),
        ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLinkFlapControlPortDisableTimer"))
)
if mibBuilder.loadTexts:
    hpicfFaultConfig4Group.setStatus("current")


# Notification objects

hpicfFaultFinderTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 1, 0, 5)
)
hpicfFaultFinderTrap.setObjects(
      *(("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogFaultType"),
        ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogAction"),
        ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogSeverity"),
        ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfFaultInfoURL"),
        ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogPhysEntity"))
)
if mibBuilder.loadTexts:
    hpicfFaultFinderTrap.setStatus(
        "current"
    )


# Notifications groups

hpicfFaultNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2, 3)
)
hpicfFaultNotifyGroup.setObjects(
    ("HP-ICF-FAULT-FINDER-MIB", "hpicfFaultFinderTrap")
)
if mibBuilder.loadTexts:
    hpicfFaultNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfFaultFinderCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfFaultFinderCompliance.setStatus(
        "current"
    )

hpicfFaultFinder2Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfFaultFinder2Compliance.setStatus(
        "current"
    )

hpicfFaultStatusCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfFaultStatusCompliance.setStatus(
        "current"
    )

hpicfFaultFinder3Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfFaultFinder3Compliance.setStatus(
        "current"
    )

hpicfFaultFinder4Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfFaultFinder4Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-FAULT-FINDER-MIB",
    **{"HpicfFaultType": HpicfFaultType,
       "HpicfFaultTolerance": HpicfFaultTolerance,
       "HpicfFaultAction": HpicfFaultAction,
       "HpicfUrlString": HpicfUrlString,
       "hpicfFaultFinderMib": hpicfFaultFinderMib,
       "hpicfFaultFinderConformance": hpicfFaultFinderConformance,
       "hpicfFaultFinderCompliances": hpicfFaultFinderCompliances,
       "hpicfFaultFinderCompliance": hpicfFaultFinderCompliance,
       "hpicfFaultFinder2Compliance": hpicfFaultFinder2Compliance,
       "hpicfFaultStatusCompliance": hpicfFaultStatusCompliance,
       "hpicfFaultFinder3Compliance": hpicfFaultFinder3Compliance,
       "hpicfFaultFinder4Compliance": hpicfFaultFinder4Compliance,
       "hpicfFaultFinderGroups": hpicfFaultFinderGroups,
       "hpicfFaultConfigGroup": hpicfFaultConfigGroup,
       "hpicfFaultLogGroup": hpicfFaultLogGroup,
       "hpicfFaultNotifyGroup": hpicfFaultNotifyGroup,
       "hpicfFaultConfig2Group": hpicfFaultConfig2Group,
       "hpicfFaultStatusGroup": hpicfFaultStatusGroup,
       "hpicfFaultConfig3Group": hpicfFaultConfig3Group,
       "hpicfFaultConfig4Group": hpicfFaultConfig4Group,
       "hpicfFaultFinder": hpicfFaultFinder,
       "hpicfFfControlTable": hpicfFfControlTable,
       "hpicfFfControlEntry": hpicfFfControlEntry,
       "hpicfFfControlIndex": hpicfFfControlIndex,
       "hpicfFfAction": hpicfFfAction,
       "hpicfFfWarnTolerance": hpicfFfWarnTolerance,
       "hpicfFfDisablePortTolerance": hpicfFfDisablePortTolerance,
       "hpicfFfSpeedReduceTolerance": hpicfFfSpeedReduceTolerance,
       "hpicfFfLogTable": hpicfFfLogTable,
       "hpicfFfLogEntry": hpicfFfLogEntry,
       "hpicfFfLogIndex": hpicfFfLogIndex,
       "hpicfFfLogCreateTime": hpicfFfLogCreateTime,
       "hpicfFfLogPhysEntity": hpicfFfLogPhysEntity,
       "hpicfFfLogFaultType": hpicfFfLogFaultType,
       "hpicfFfLogAction": hpicfFfLogAction,
       "hpicfFfLogSeverity": hpicfFfLogSeverity,
       "hpicfFfLogStatus": hpicfFfLogStatus,
       "hpicfFfLogPhysClass": hpicfFfLogPhysClass,
       "hpicfFfLogInfoType": hpicfFfLogInfoType,
       "hpicfFfLogInfo": hpicfFfLogInfo,
       "hpicfFfFaultInfoURL": hpicfFfFaultInfoURL,
       "hpicfFfFaultLightStatus": hpicfFfFaultLightStatus,
       "hpicfFfBcastStormControlPortConfig": hpicfFfBcastStormControlPortConfig,
       "hpicfFfBcastStormControlPortConfigTable": hpicfFfBcastStormControlPortConfigTable,
       "hpicfFfBcastStormControlPortConfigEntry": hpicfFfBcastStormControlPortConfigEntry,
       "hpicfFfBcastStormControlPortIndex": hpicfFfBcastStormControlPortIndex,
       "hpicfFfBcastStormControlMode": hpicfFfBcastStormControlMode,
       "hpicfFfBcastStormControlRisingpercent": hpicfFfBcastStormControlRisingpercent,
       "hpicfFfBcastStormControlRisingpps": hpicfFfBcastStormControlRisingpps,
       "hpicfFfBcastStormControlAction": hpicfFfBcastStormControlAction,
       "hpicfFfBcastStormControlPortDisableTimer": hpicfFfBcastStormControlPortDisableTimer,
       "hpicfFfLinkFlapControlPortConfig": hpicfFfLinkFlapControlPortConfig,
       "hpicfFfLinkFlapControlPortConfigTable": hpicfFfLinkFlapControlPortConfigTable,
       "hpicfFfLinkFlapControlPortConfigEntry": hpicfFfLinkFlapControlPortConfigEntry,
       "hpicfFfLinkFlapControlPortIndex": hpicfFfLinkFlapControlPortIndex,
       "hpicfFfLinkFlapControlSensitivity": hpicfFfLinkFlapControlSensitivity,
       "hpicfFfLinkFlapControlAction": hpicfFfLinkFlapControlAction,
       "hpicfFfLinkFlapControlPortDisableTimer": hpicfFfLinkFlapControlPortDisableTimer,
       "hpicfFaultFinderTrap": hpicfFaultFinderTrap}
)
