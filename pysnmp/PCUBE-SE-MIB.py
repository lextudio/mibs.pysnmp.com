# SNMP MIB module (PCUBE-SE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PCUBE-SE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:57 2024
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

(pcubeModules,
 pcubeWorkgroup) = mibBuilder.importSymbols(
    "PCUBE-SMI",
    "pcubeModules",
    "pcubeWorkgroup")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

pcubeSeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 2, 3)
)
pcubeSeMIB.setRevisions(
        ("2006-11-07 00:00",
         "2006-05-10 00:00",
         "2006-02-12 00:00",
         "2005-08-16 00:00",
         "2004-12-12 00:00",
         "2004-07-01 00:00",
         "2003-07-02 00:00",
         "2003-01-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LinkModeType(Integer32, TextualConvention):
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
        *(("bypass", 2),
          ("cutoff", 4),
          ("forwarding", 3),
          ("other", 1),
          ("sniffing", 5))
    )



# MIB Managed Objects in the order of their OIDs

_PcubeSeConformance_ObjectIdentity = ObjectIdentity
pcubeSeConformance = _PcubeSeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 2, 3, 1)
)
_PcubeSeGroups_ObjectIdentity = ObjectIdentity
pcubeSeGroups = _PcubeSeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 2, 3, 1, 1)
)
_PcubeSeCompliances_ObjectIdentity = ObjectIdentity
pcubeSeCompliances = _PcubeSeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 2, 3, 1, 2)
)
_PcubeSeEvents_ObjectIdentity = ObjectIdentity
pcubeSeEvents = _PcubeSeEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0)
)
_PcubeSeEventGenericString1_Type = SnmpAdminString
_PcubeSeEventGenericString1_Object = MibScalar
pcubeSeEventGenericString1 = _PcubeSeEventGenericString1_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 23),
    _PcubeSeEventGenericString1_Type()
)
pcubeSeEventGenericString1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcubeSeEventGenericString1.setStatus("current")
_PcubeSeEventGenericString2_Type = SnmpAdminString
_PcubeSeEventGenericString2_Object = MibScalar
pcubeSeEventGenericString2 = _PcubeSeEventGenericString2_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 24),
    _PcubeSeEventGenericString2_Type()
)
pcubeSeEventGenericString2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcubeSeEventGenericString2.setStatus("current")


class _PullRequestNumber_Type(Integer32):
    """Custom type pullRequestNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PullRequestNumber_Type.__name__ = "Integer32"
_PullRequestNumber_Object = MibScalar
pullRequestNumber = _PullRequestNumber_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 46),
    _PullRequestNumber_Type()
)
pullRequestNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pullRequestNumber.setStatus("current")
_PcubeSEObjs_ObjectIdentity = ObjectIdentity
pcubeSEObjs = _PcubeSEObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1)
)
_SystemGrp_ObjectIdentity = ObjectIdentity
systemGrp = _SystemGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 1)
)


class _SysOperationalStatus_Type(Integer32):
    """Custom type sysOperationalStatus based on Integer32"""
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
        *(("boot", 2),
          ("failure", 5),
          ("operational", 3),
          ("other", 1),
          ("warning", 4))
    )


_SysOperationalStatus_Type.__name__ = "Integer32"
_SysOperationalStatus_Object = MibScalar
sysOperationalStatus = _SysOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 1, 1),
    _SysOperationalStatus_Type()
)
sysOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysOperationalStatus.setStatus("current")


class _SysFailureRecovery_Type(Integer32):
    """Custom type sysFailureRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonOperational", 3),
          ("operational", 2),
          ("other", 1))
    )


_SysFailureRecovery_Type.__name__ = "Integer32"
_SysFailureRecovery_Object = MibScalar
sysFailureRecovery = _SysFailureRecovery_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 1, 2),
    _SysFailureRecovery_Type()
)
sysFailureRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFailureRecovery.setStatus("current")
_SysVersion_Type = SnmpAdminString
_SysVersion_Object = MibScalar
sysVersion = _SysVersion_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 1, 3),
    _SysVersion_Type()
)
sysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVersion.setStatus("current")
_PchassisGrp_ObjectIdentity = ObjectIdentity
pchassisGrp = _PchassisGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 2)
)


class _PchassisSysType_Type(Integer32):
    """Custom type pchassisSysType based on Integer32"""
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
        *(("other", 1),
          ("sce1000", 2),
          ("sce2000", 4),
          ("se100", 3))
    )


_PchassisSysType_Type.__name__ = "Integer32"
_PchassisSysType_Object = MibScalar
pchassisSysType = _PchassisSysType_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 2, 1),
    _PchassisSysType_Type()
)
pchassisSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pchassisSysType.setStatus("current")


class _PchassisPowerSupplyAlarm_Type(Integer32):
    """Custom type pchassisPowerSupplyAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3),
          ("other", 1))
    )


_PchassisPowerSupplyAlarm_Type.__name__ = "Integer32"
_PchassisPowerSupplyAlarm_Object = MibScalar
pchassisPowerSupplyAlarm = _PchassisPowerSupplyAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 2, 2),
    _PchassisPowerSupplyAlarm_Type()
)
pchassisPowerSupplyAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pchassisPowerSupplyAlarm.setStatus("current")


class _PchassisFansAlarm_Type(Integer32):
    """Custom type pchassisFansAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3),
          ("other", 1))
    )


_PchassisFansAlarm_Type.__name__ = "Integer32"
_PchassisFansAlarm_Object = MibScalar
pchassisFansAlarm = _PchassisFansAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 2, 3),
    _PchassisFansAlarm_Type()
)
pchassisFansAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pchassisFansAlarm.setStatus("current")


class _PchassisTempAlarm_Type(Integer32):
    """Custom type pchassisTempAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3),
          ("other", 1))
    )


_PchassisTempAlarm_Type.__name__ = "Integer32"
_PchassisTempAlarm_Object = MibScalar
pchassisTempAlarm = _PchassisTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 2, 4),
    _PchassisTempAlarm_Type()
)
pchassisTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pchassisTempAlarm.setStatus("current")


class _PchassisVoltageAlarm_Type(Integer32):
    """Custom type pchassisVoltageAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3),
          ("other", 1))
    )


_PchassisVoltageAlarm_Type.__name__ = "Integer32"
_PchassisVoltageAlarm_Object = MibScalar
pchassisVoltageAlarm = _PchassisVoltageAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 2, 5),
    _PchassisVoltageAlarm_Type()
)
pchassisVoltageAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pchassisVoltageAlarm.setStatus("current")


class _PchassisNumSlots_Type(Integer32):
    """Custom type pchassisNumSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PchassisNumSlots_Type.__name__ = "Integer32"
_PchassisNumSlots_Object = MibScalar
pchassisNumSlots = _PchassisNumSlots_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 2, 6),
    _PchassisNumSlots_Type()
)
pchassisNumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pchassisNumSlots.setStatus("current")


class _PchassisSlotConfig_Type(Integer32):
    """Custom type pchassisSlotConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PchassisSlotConfig_Type.__name__ = "Integer32"
_PchassisSlotConfig_Object = MibScalar
pchassisSlotConfig = _PchassisSlotConfig_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 2, 7),
    _PchassisSlotConfig_Type()
)
pchassisSlotConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pchassisSlotConfig.setStatus("current")


class _PchassisPsuType_Type(Integer32):
    """Custom type pchassisPsuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ac", 2),
          ("dc", 3),
          ("other", 1))
    )


_PchassisPsuType_Type.__name__ = "Integer32"
_PchassisPsuType_Object = MibScalar
pchassisPsuType = _PchassisPsuType_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 2, 8),
    _PchassisPsuType_Type()
)
pchassisPsuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pchassisPsuType.setStatus("current")


class _PchassisLineFeedAlarm_Type(Integer32):
    """Custom type pchassisLineFeedAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3),
          ("other", 1))
    )


_PchassisLineFeedAlarm_Type.__name__ = "Integer32"
_PchassisLineFeedAlarm_Object = MibScalar
pchassisLineFeedAlarm = _PchassisLineFeedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 2, 10),
    _PchassisLineFeedAlarm_Type()
)
pchassisLineFeedAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pchassisLineFeedAlarm.setStatus("current")
_PmoduleGrp_ObjectIdentity = ObjectIdentity
pmoduleGrp = _PmoduleGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 3)
)
_PmoduleTable_Object = MibTable
pmoduleTable = _PmoduleTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    pmoduleTable.setStatus("current")
_PmoduleEntry_Object = MibTableRow
pmoduleEntry = _PmoduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 3, 1, 1)
)
pmoduleEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "pmoduleIndex"),
)
if mibBuilder.loadTexts:
    pmoduleEntry.setStatus("current")


class _PmoduleIndex_Type(Integer32):
    """Custom type pmoduleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PmoduleIndex_Type.__name__ = "Integer32"
_PmoduleIndex_Object = MibTableColumn
pmoduleIndex = _PmoduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 3, 1, 1, 1),
    _PmoduleIndex_Type()
)
pmoduleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoduleIndex.setStatus("current")


class _PmoduleType_Type(Integer32):
    """Custom type pmoduleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("fe2Module", 3),
          ("fe4Module", 5),
          ("fe8Module", 7),
          ("gbe2Module", 2),
          ("gbe4Module", 4),
          ("oc124Module", 6),
          ("other", 1))
    )


_PmoduleType_Type.__name__ = "Integer32"
_PmoduleType_Object = MibTableColumn
pmoduleType = _PmoduleType_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 3, 1, 1, 2),
    _PmoduleType_Type()
)
pmoduleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoduleType.setStatus("current")


class _PmoduleNumTrafficProcessors_Type(Integer32):
    """Custom type pmoduleNumTrafficProcessors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PmoduleNumTrafficProcessors_Type.__name__ = "Integer32"
_PmoduleNumTrafficProcessors_Object = MibTableColumn
pmoduleNumTrafficProcessors = _PmoduleNumTrafficProcessors_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 3, 1, 1, 3),
    _PmoduleNumTrafficProcessors_Type()
)
pmoduleNumTrafficProcessors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoduleNumTrafficProcessors.setStatus("current")


class _PmoduleSlotNum_Type(Integer32):
    """Custom type pmoduleSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PmoduleSlotNum_Type.__name__ = "Integer32"
_PmoduleSlotNum_Object = MibTableColumn
pmoduleSlotNum = _PmoduleSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 3, 1, 1, 4),
    _PmoduleSlotNum_Type()
)
pmoduleSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoduleSlotNum.setStatus("current")
_PmoduleHwVersion_Type = SnmpAdminString
_PmoduleHwVersion_Object = MibTableColumn
pmoduleHwVersion = _PmoduleHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 3, 1, 1, 5),
    _PmoduleHwVersion_Type()
)
pmoduleHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoduleHwVersion.setStatus("current")


class _PmoduleNumPorts_Type(Integer32):
    """Custom type pmoduleNumPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PmoduleNumPorts_Type.__name__ = "Integer32"
_PmoduleNumPorts_Object = MibTableColumn
pmoduleNumPorts = _PmoduleNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 3, 1, 1, 6),
    _PmoduleNumPorts_Type()
)
pmoduleNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoduleNumPorts.setStatus("current")


class _PmoduleNumLinks_Type(Integer32):
    """Custom type pmoduleNumLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PmoduleNumLinks_Type.__name__ = "Integer32"
_PmoduleNumLinks_Object = MibTableColumn
pmoduleNumLinks = _PmoduleNumLinks_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 3, 1, 1, 7),
    _PmoduleNumLinks_Type()
)
pmoduleNumLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoduleNumLinks.setStatus("current")


class _PmoduleConnectionMode_Type(Integer32):
    """Custom type pmoduleConnectionMode based on Integer32"""
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
        *(("inline", 2),
          ("inlineCascade", 4),
          ("other", 1),
          ("receiveOnly", 3),
          ("receiveOnlyCascade", 5))
    )


_PmoduleConnectionMode_Type.__name__ = "Integer32"
_PmoduleConnectionMode_Object = MibTableColumn
pmoduleConnectionMode = _PmoduleConnectionMode_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 3, 1, 1, 8),
    _PmoduleConnectionMode_Type()
)
pmoduleConnectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoduleConnectionMode.setStatus("current")
_PmoduleSerialNumber_Type = SnmpAdminString
_PmoduleSerialNumber_Object = MibTableColumn
pmoduleSerialNumber = _PmoduleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 3, 1, 1, 9),
    _PmoduleSerialNumber_Type()
)
pmoduleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoduleSerialNumber.setStatus("current")
_PmoduleUpStreamAttackFilteringTime_Type = TimeTicks
_PmoduleUpStreamAttackFilteringTime_Object = MibTableColumn
pmoduleUpStreamAttackFilteringTime = _PmoduleUpStreamAttackFilteringTime_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 3, 1, 1, 10),
    _PmoduleUpStreamAttackFilteringTime_Type()
)
pmoduleUpStreamAttackFilteringTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoduleUpStreamAttackFilteringTime.setStatus("current")
if mibBuilder.loadTexts:
    pmoduleUpStreamAttackFilteringTime.setUnits("milliseconds")
_PmoduleUpStreamLastAttackFilteringTime_Type = TimeTicks
_PmoduleUpStreamLastAttackFilteringTime_Object = MibTableColumn
pmoduleUpStreamLastAttackFilteringTime = _PmoduleUpStreamLastAttackFilteringTime_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 3, 1, 1, 11),
    _PmoduleUpStreamLastAttackFilteringTime_Type()
)
pmoduleUpStreamLastAttackFilteringTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoduleUpStreamLastAttackFilteringTime.setStatus("current")
if mibBuilder.loadTexts:
    pmoduleUpStreamLastAttackFilteringTime.setUnits("milliseconds")
_PmoduleDownStreamAttackFilteringTime_Type = TimeTicks
_PmoduleDownStreamAttackFilteringTime_Object = MibTableColumn
pmoduleDownStreamAttackFilteringTime = _PmoduleDownStreamAttackFilteringTime_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 3, 1, 1, 12),
    _PmoduleDownStreamAttackFilteringTime_Type()
)
pmoduleDownStreamAttackFilteringTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoduleDownStreamAttackFilteringTime.setStatus("current")
if mibBuilder.loadTexts:
    pmoduleDownStreamAttackFilteringTime.setUnits("milliseconds")
_PmoduleDownStreamLastAttackFilteringTime_Type = TimeTicks
_PmoduleDownStreamLastAttackFilteringTime_Object = MibTableColumn
pmoduleDownStreamLastAttackFilteringTime = _PmoduleDownStreamLastAttackFilteringTime_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 3, 1, 1, 13),
    _PmoduleDownStreamLastAttackFilteringTime_Type()
)
pmoduleDownStreamLastAttackFilteringTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoduleDownStreamLastAttackFilteringTime.setStatus("current")
if mibBuilder.loadTexts:
    pmoduleDownStreamLastAttackFilteringTime.setUnits("milliseconds")
_PmoduleAttackObjectsClearTime_Type = TimeTicks
_PmoduleAttackObjectsClearTime_Object = MibTableColumn
pmoduleAttackObjectsClearTime = _PmoduleAttackObjectsClearTime_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 3, 1, 1, 14),
    _PmoduleAttackObjectsClearTime_Type()
)
pmoduleAttackObjectsClearTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoduleAttackObjectsClearTime.setStatus("current")
if mibBuilder.loadTexts:
    pmoduleAttackObjectsClearTime.setUnits("milliseconds")


class _PmoduleAdminStatus_Type(Integer32):
    """Custom type pmoduleAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_PmoduleAdminStatus_Type.__name__ = "Integer32"
_PmoduleAdminStatus_Object = MibTableColumn
pmoduleAdminStatus = _PmoduleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 3, 1, 1, 15),
    _PmoduleAdminStatus_Type()
)
pmoduleAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoduleAdminStatus.setStatus("current")


class _PmoduleOperStatus_Type(Integer32):
    """Custom type pmoduleOperStatus based on Integer32"""
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
          ("other", 1),
          ("standby", 3))
    )


_PmoduleOperStatus_Type.__name__ = "Integer32"
_PmoduleOperStatus_Object = MibTableColumn
pmoduleOperStatus = _PmoduleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 3, 1, 1, 16),
    _PmoduleOperStatus_Type()
)
pmoduleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoduleOperStatus.setStatus("current")
_LinkGrp_ObjectIdentity = ObjectIdentity
linkGrp = _LinkGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 4)
)
_LinkTable_Object = MibTable
linkTable = _LinkTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 4, 1)
)
if mibBuilder.loadTexts:
    linkTable.setStatus("current")
_LinkEntry_Object = MibTableRow
linkEntry = _LinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 4, 1, 1)
)
linkEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "linkModuleIndex"),
    (0, "PCUBE-SE-MIB", "linkIndex"),
)
if mibBuilder.loadTexts:
    linkEntry.setStatus("current")


class _LinkModuleIndex_Type(Integer32):
    """Custom type linkModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LinkModuleIndex_Type.__name__ = "Integer32"
_LinkModuleIndex_Object = MibTableColumn
linkModuleIndex = _LinkModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 4, 1, 1, 1),
    _LinkModuleIndex_Type()
)
linkModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkModuleIndex.setStatus("current")


class _LinkIndex_Type(Integer32):
    """Custom type linkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LinkIndex_Type.__name__ = "Integer32"
_LinkIndex_Object = MibTableColumn
linkIndex = _LinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 4, 1, 1, 2),
    _LinkIndex_Type()
)
linkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkIndex.setStatus("current")
_LinkAdminModeOnActive_Type = LinkModeType
_LinkAdminModeOnActive_Object = MibTableColumn
linkAdminModeOnActive = _LinkAdminModeOnActive_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 4, 1, 1, 3),
    _LinkAdminModeOnActive_Type()
)
linkAdminModeOnActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAdminModeOnActive.setStatus("current")
_LinkAdminModeOnFailure_Type = LinkModeType
_LinkAdminModeOnFailure_Object = MibTableColumn
linkAdminModeOnFailure = _LinkAdminModeOnFailure_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 4, 1, 1, 4),
    _LinkAdminModeOnFailure_Type()
)
linkAdminModeOnFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAdminModeOnFailure.setStatus("current")
_LinkOperMode_Type = LinkModeType
_LinkOperMode_Object = MibTableColumn
linkOperMode = _LinkOperMode_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 4, 1, 1, 5),
    _LinkOperMode_Type()
)
linkOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkOperMode.setStatus("current")


class _LinkStatusReflectionEnable_Type(Integer32):
    """Custom type linkStatusReflectionEnable based on Integer32"""
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


_LinkStatusReflectionEnable_Type.__name__ = "Integer32"
_LinkStatusReflectionEnable_Object = MibTableColumn
linkStatusReflectionEnable = _LinkStatusReflectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 4, 1, 1, 6),
    _LinkStatusReflectionEnable_Type()
)
linkStatusReflectionEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusReflectionEnable.setStatus("current")


class _LinkSubscriberSidePortIndex_Type(Integer32):
    """Custom type linkSubscriberSidePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LinkSubscriberSidePortIndex_Type.__name__ = "Integer32"
_LinkSubscriberSidePortIndex_Object = MibTableColumn
linkSubscriberSidePortIndex = _LinkSubscriberSidePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 4, 1, 1, 7),
    _LinkSubscriberSidePortIndex_Type()
)
linkSubscriberSidePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkSubscriberSidePortIndex.setStatus("current")


class _LinkNetworkSidePortIndex_Type(Integer32):
    """Custom type linkNetworkSidePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LinkNetworkSidePortIndex_Type.__name__ = "Integer32"
_LinkNetworkSidePortIndex_Object = MibTableColumn
linkNetworkSidePortIndex = _LinkNetworkSidePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 4, 1, 1, 8),
    _LinkNetworkSidePortIndex_Type()
)
linkNetworkSidePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkNetworkSidePortIndex.setStatus("current")
_DiskGrp_ObjectIdentity = ObjectIdentity
diskGrp = _DiskGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 5)
)


class _DiskNumUsedBytes_Type(Unsigned32):
    """Custom type diskNumUsedBytes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DiskNumUsedBytes_Type.__name__ = "Unsigned32"
_DiskNumUsedBytes_Object = MibScalar
diskNumUsedBytes = _DiskNumUsedBytes_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 5, 1),
    _DiskNumUsedBytes_Type()
)
diskNumUsedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskNumUsedBytes.setStatus("current")
if mibBuilder.loadTexts:
    diskNumUsedBytes.setUnits("bytes")


class _DiskNumFreeBytes_Type(Unsigned32):
    """Custom type diskNumFreeBytes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DiskNumFreeBytes_Type.__name__ = "Unsigned32"
_DiskNumFreeBytes_Object = MibScalar
diskNumFreeBytes = _DiskNumFreeBytes_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 5, 2),
    _DiskNumFreeBytes_Type()
)
diskNumFreeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskNumFreeBytes.setStatus("current")
if mibBuilder.loadTexts:
    diskNumFreeBytes.setUnits("bytes")
_RdrFormatterGrp_ObjectIdentity = ObjectIdentity
rdrFormatterGrp = _RdrFormatterGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6)
)


class _RdrFormatterEnable_Type(Integer32):
    """Custom type rdrFormatterEnable based on Integer32"""
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


_RdrFormatterEnable_Type.__name__ = "Integer32"
_RdrFormatterEnable_Object = MibScalar
rdrFormatterEnable = _RdrFormatterEnable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 1),
    _RdrFormatterEnable_Type()
)
rdrFormatterEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrFormatterEnable.setStatus("current")
_RdrFormatterDestTable_Object = MibTable
rdrFormatterDestTable = _RdrFormatterDestTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 2)
)
if mibBuilder.loadTexts:
    rdrFormatterDestTable.setStatus("current")
_RdrFormatterDestEntry_Object = MibTableRow
rdrFormatterDestEntry = _RdrFormatterDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 2, 1)
)
rdrFormatterDestEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "rdrFormatterDestIPAddr"),
    (0, "PCUBE-SE-MIB", "rdrFormatterDestPort"),
)
if mibBuilder.loadTexts:
    rdrFormatterDestEntry.setStatus("current")
_RdrFormatterDestIPAddr_Type = IpAddress
_RdrFormatterDestIPAddr_Object = MibTableColumn
rdrFormatterDestIPAddr = _RdrFormatterDestIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 2, 1, 1),
    _RdrFormatterDestIPAddr_Type()
)
rdrFormatterDestIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrFormatterDestIPAddr.setStatus("current")


class _RdrFormatterDestPort_Type(Integer32):
    """Custom type rdrFormatterDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RdrFormatterDestPort_Type.__name__ = "Integer32"
_RdrFormatterDestPort_Object = MibTableColumn
rdrFormatterDestPort = _RdrFormatterDestPort_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 2, 1, 2),
    _RdrFormatterDestPort_Type()
)
rdrFormatterDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrFormatterDestPort.setStatus("current")


class _RdrFormatterDestPriority_Type(Integer32):
    """Custom type rdrFormatterDestPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RdrFormatterDestPriority_Type.__name__ = "Integer32"
_RdrFormatterDestPriority_Object = MibTableColumn
rdrFormatterDestPriority = _RdrFormatterDestPriority_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 2, 1, 3),
    _RdrFormatterDestPriority_Type()
)
rdrFormatterDestPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrFormatterDestPriority.setStatus("current")


class _RdrFormatterDestStatus_Type(Integer32):
    """Custom type rdrFormatterDestStatus based on Integer32"""
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
          ("other", 1),
          ("standby", 3))
    )


_RdrFormatterDestStatus_Type.__name__ = "Integer32"
_RdrFormatterDestStatus_Object = MibTableColumn
rdrFormatterDestStatus = _RdrFormatterDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 2, 1, 4),
    _RdrFormatterDestStatus_Type()
)
rdrFormatterDestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrFormatterDestStatus.setStatus("current")


class _RdrFormatterDestConnectionStatus_Type(Integer32):
    """Custom type rdrFormatterDestConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("other", 1),
          ("up", 2))
    )


_RdrFormatterDestConnectionStatus_Type.__name__ = "Integer32"
_RdrFormatterDestConnectionStatus_Object = MibTableColumn
rdrFormatterDestConnectionStatus = _RdrFormatterDestConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 2, 1, 5),
    _RdrFormatterDestConnectionStatus_Type()
)
rdrFormatterDestConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrFormatterDestConnectionStatus.setStatus("current")


class _RdrFormatterDestNumReportsSent_Type(Unsigned32):
    """Custom type rdrFormatterDestNumReportsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RdrFormatterDestNumReportsSent_Type.__name__ = "Unsigned32"
_RdrFormatterDestNumReportsSent_Object = MibTableColumn
rdrFormatterDestNumReportsSent = _RdrFormatterDestNumReportsSent_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 2, 1, 6),
    _RdrFormatterDestNumReportsSent_Type()
)
rdrFormatterDestNumReportsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrFormatterDestNumReportsSent.setStatus("current")


class _RdrFormatterDestNumReportsDiscarded_Type(Unsigned32):
    """Custom type rdrFormatterDestNumReportsDiscarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RdrFormatterDestNumReportsDiscarded_Type.__name__ = "Unsigned32"
_RdrFormatterDestNumReportsDiscarded_Object = MibTableColumn
rdrFormatterDestNumReportsDiscarded = _RdrFormatterDestNumReportsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 2, 1, 7),
    _RdrFormatterDestNumReportsDiscarded_Type()
)
rdrFormatterDestNumReportsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrFormatterDestNumReportsDiscarded.setStatus("current")


class _RdrFormatterDestReportRate_Type(Unsigned32):
    """Custom type rdrFormatterDestReportRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RdrFormatterDestReportRate_Type.__name__ = "Unsigned32"
_RdrFormatterDestReportRate_Object = MibTableColumn
rdrFormatterDestReportRate = _RdrFormatterDestReportRate_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 2, 1, 8),
    _RdrFormatterDestReportRate_Type()
)
rdrFormatterDestReportRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrFormatterDestReportRate.setStatus("current")


class _RdrFormatterDestReportRatePeak_Type(Unsigned32):
    """Custom type rdrFormatterDestReportRatePeak based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RdrFormatterDestReportRatePeak_Type.__name__ = "Unsigned32"
_RdrFormatterDestReportRatePeak_Object = MibTableColumn
rdrFormatterDestReportRatePeak = _RdrFormatterDestReportRatePeak_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 2, 1, 9),
    _RdrFormatterDestReportRatePeak_Type()
)
rdrFormatterDestReportRatePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrFormatterDestReportRatePeak.setStatus("current")
_RdrFormatterDestReportRatePeakTime_Type = TimeTicks
_RdrFormatterDestReportRatePeakTime_Object = MibTableColumn
rdrFormatterDestReportRatePeakTime = _RdrFormatterDestReportRatePeakTime_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 2, 1, 10),
    _RdrFormatterDestReportRatePeakTime_Type()
)
rdrFormatterDestReportRatePeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrFormatterDestReportRatePeakTime.setStatus("current")
if mibBuilder.loadTexts:
    rdrFormatterDestReportRatePeakTime.setUnits("milliseconds")


class _RdrFormatterNumReportsSent_Type(Unsigned32):
    """Custom type rdrFormatterNumReportsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RdrFormatterNumReportsSent_Type.__name__ = "Unsigned32"
_RdrFormatterNumReportsSent_Object = MibScalar
rdrFormatterNumReportsSent = _RdrFormatterNumReportsSent_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 3),
    _RdrFormatterNumReportsSent_Type()
)
rdrFormatterNumReportsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrFormatterNumReportsSent.setStatus("current")


class _RdrFormatterNumReportsDiscarded_Type(Unsigned32):
    """Custom type rdrFormatterNumReportsDiscarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RdrFormatterNumReportsDiscarded_Type.__name__ = "Unsigned32"
_RdrFormatterNumReportsDiscarded_Object = MibScalar
rdrFormatterNumReportsDiscarded = _RdrFormatterNumReportsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 4),
    _RdrFormatterNumReportsDiscarded_Type()
)
rdrFormatterNumReportsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrFormatterNumReportsDiscarded.setStatus("current")
_RdrFormatterClearCountersTime_Type = TimeTicks
_RdrFormatterClearCountersTime_Object = MibScalar
rdrFormatterClearCountersTime = _RdrFormatterClearCountersTime_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 5),
    _RdrFormatterClearCountersTime_Type()
)
rdrFormatterClearCountersTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdrFormatterClearCountersTime.setStatus("current")
if mibBuilder.loadTexts:
    rdrFormatterClearCountersTime.setUnits("milliseconds")


class _RdrFormatterReportRate_Type(Unsigned32):
    """Custom type rdrFormatterReportRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RdrFormatterReportRate_Type.__name__ = "Unsigned32"
_RdrFormatterReportRate_Object = MibScalar
rdrFormatterReportRate = _RdrFormatterReportRate_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 6),
    _RdrFormatterReportRate_Type()
)
rdrFormatterReportRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrFormatterReportRate.setStatus("current")


class _RdrFormatterReportRatePeak_Type(Unsigned32):
    """Custom type rdrFormatterReportRatePeak based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RdrFormatterReportRatePeak_Type.__name__ = "Unsigned32"
_RdrFormatterReportRatePeak_Object = MibScalar
rdrFormatterReportRatePeak = _RdrFormatterReportRatePeak_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 7),
    _RdrFormatterReportRatePeak_Type()
)
rdrFormatterReportRatePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrFormatterReportRatePeak.setStatus("current")
_RdrFormatterReportRatePeakTime_Type = TimeTicks
_RdrFormatterReportRatePeakTime_Object = MibScalar
rdrFormatterReportRatePeakTime = _RdrFormatterReportRatePeakTime_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 8),
    _RdrFormatterReportRatePeakTime_Type()
)
rdrFormatterReportRatePeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrFormatterReportRatePeakTime.setStatus("current")
if mibBuilder.loadTexts:
    rdrFormatterReportRatePeakTime.setUnits("milliseconds")


class _RdrFormatterProtocol_Type(Integer32):
    """Custom type rdrFormatterProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("rdrv1", 2),
          ("rdrv2", 3))
    )


_RdrFormatterProtocol_Type.__name__ = "Integer32"
_RdrFormatterProtocol_Object = MibScalar
rdrFormatterProtocol = _RdrFormatterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 9),
    _RdrFormatterProtocol_Type()
)
rdrFormatterProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrFormatterProtocol.setStatus("current")


class _RdrFormatterForwardingMode_Type(Integer32):
    """Custom type rdrFormatterForwardingMode based on Integer32"""
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
        *(("multicast", 4),
          ("other", 1),
          ("redundancy", 2),
          ("simpleLoadBalancing", 3))
    )


_RdrFormatterForwardingMode_Type.__name__ = "Integer32"
_RdrFormatterForwardingMode_Object = MibScalar
rdrFormatterForwardingMode = _RdrFormatterForwardingMode_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 10),
    _RdrFormatterForwardingMode_Type()
)
rdrFormatterForwardingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrFormatterForwardingMode.setStatus("current")
_RdrFormatterCategoryTable_Object = MibTable
rdrFormatterCategoryTable = _RdrFormatterCategoryTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 11)
)
if mibBuilder.loadTexts:
    rdrFormatterCategoryTable.setStatus("current")
_RdrFormatterCategoryEntry_Object = MibTableRow
rdrFormatterCategoryEntry = _RdrFormatterCategoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 11, 1)
)
rdrFormatterCategoryEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "rdrFormatterCategoryIndex"),
)
if mibBuilder.loadTexts:
    rdrFormatterCategoryEntry.setStatus("current")


class _RdrFormatterCategoryIndex_Type(Integer32):
    """Custom type rdrFormatterCategoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RdrFormatterCategoryIndex_Type.__name__ = "Integer32"
_RdrFormatterCategoryIndex_Object = MibTableColumn
rdrFormatterCategoryIndex = _RdrFormatterCategoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 11, 1, 1),
    _RdrFormatterCategoryIndex_Type()
)
rdrFormatterCategoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrFormatterCategoryIndex.setStatus("current")
_RdrFormatterCategoryName_Type = SnmpAdminString
_RdrFormatterCategoryName_Object = MibTableColumn
rdrFormatterCategoryName = _RdrFormatterCategoryName_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 11, 1, 2),
    _RdrFormatterCategoryName_Type()
)
rdrFormatterCategoryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrFormatterCategoryName.setStatus("current")


class _RdrFormatterCategoryNumReportsSent_Type(Unsigned32):
    """Custom type rdrFormatterCategoryNumReportsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RdrFormatterCategoryNumReportsSent_Type.__name__ = "Unsigned32"
_RdrFormatterCategoryNumReportsSent_Object = MibTableColumn
rdrFormatterCategoryNumReportsSent = _RdrFormatterCategoryNumReportsSent_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 11, 1, 3),
    _RdrFormatterCategoryNumReportsSent_Type()
)
rdrFormatterCategoryNumReportsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrFormatterCategoryNumReportsSent.setStatus("current")


class _RdrFormatterCategoryNumReportsDiscarded_Type(Unsigned32):
    """Custom type rdrFormatterCategoryNumReportsDiscarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RdrFormatterCategoryNumReportsDiscarded_Type.__name__ = "Unsigned32"
_RdrFormatterCategoryNumReportsDiscarded_Object = MibTableColumn
rdrFormatterCategoryNumReportsDiscarded = _RdrFormatterCategoryNumReportsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 11, 1, 4),
    _RdrFormatterCategoryNumReportsDiscarded_Type()
)
rdrFormatterCategoryNumReportsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrFormatterCategoryNumReportsDiscarded.setStatus("current")


class _RdrFormatterCategoryReportRate_Type(Unsigned32):
    """Custom type rdrFormatterCategoryReportRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RdrFormatterCategoryReportRate_Type.__name__ = "Unsigned32"
_RdrFormatterCategoryReportRate_Object = MibTableColumn
rdrFormatterCategoryReportRate = _RdrFormatterCategoryReportRate_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 11, 1, 5),
    _RdrFormatterCategoryReportRate_Type()
)
rdrFormatterCategoryReportRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrFormatterCategoryReportRate.setStatus("current")


class _RdrFormatterCategoryReportRatePeak_Type(Unsigned32):
    """Custom type rdrFormatterCategoryReportRatePeak based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RdrFormatterCategoryReportRatePeak_Type.__name__ = "Unsigned32"
_RdrFormatterCategoryReportRatePeak_Object = MibTableColumn
rdrFormatterCategoryReportRatePeak = _RdrFormatterCategoryReportRatePeak_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 11, 1, 6),
    _RdrFormatterCategoryReportRatePeak_Type()
)
rdrFormatterCategoryReportRatePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrFormatterCategoryReportRatePeak.setStatus("current")
_RdrFormatterCategoryReportRatePeakTime_Type = TimeTicks
_RdrFormatterCategoryReportRatePeakTime_Object = MibTableColumn
rdrFormatterCategoryReportRatePeakTime = _RdrFormatterCategoryReportRatePeakTime_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 11, 1, 7),
    _RdrFormatterCategoryReportRatePeakTime_Type()
)
rdrFormatterCategoryReportRatePeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrFormatterCategoryReportRatePeakTime.setStatus("current")
if mibBuilder.loadTexts:
    rdrFormatterCategoryReportRatePeakTime.setUnits("milliseconds")


class _RdrFormatterCategoryNumReportsQueued_Type(Unsigned32):
    """Custom type rdrFormatterCategoryNumReportsQueued based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RdrFormatterCategoryNumReportsQueued_Type.__name__ = "Unsigned32"
_RdrFormatterCategoryNumReportsQueued_Object = MibTableColumn
rdrFormatterCategoryNumReportsQueued = _RdrFormatterCategoryNumReportsQueued_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 11, 1, 8),
    _RdrFormatterCategoryNumReportsQueued_Type()
)
rdrFormatterCategoryNumReportsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrFormatterCategoryNumReportsQueued.setStatus("current")
_RdrFormatterCategoryDestTable_Object = MibTable
rdrFormatterCategoryDestTable = _RdrFormatterCategoryDestTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 12)
)
if mibBuilder.loadTexts:
    rdrFormatterCategoryDestTable.setStatus("current")
_RdrFormatterCategoryDestEntry_Object = MibTableRow
rdrFormatterCategoryDestEntry = _RdrFormatterCategoryDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 12, 1)
)
rdrFormatterCategoryDestEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "rdrFormatterCategoryIndex"),
    (0, "PCUBE-SE-MIB", "rdrFormatterDestIPAddr"),
    (0, "PCUBE-SE-MIB", "rdrFormatterDestPort"),
)
if mibBuilder.loadTexts:
    rdrFormatterCategoryDestEntry.setStatus("current")


class _RdrFormatterCategoryDestPriority_Type(Integer32):
    """Custom type rdrFormatterCategoryDestPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RdrFormatterCategoryDestPriority_Type.__name__ = "Integer32"
_RdrFormatterCategoryDestPriority_Object = MibTableColumn
rdrFormatterCategoryDestPriority = _RdrFormatterCategoryDestPriority_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 12, 1, 1),
    _RdrFormatterCategoryDestPriority_Type()
)
rdrFormatterCategoryDestPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrFormatterCategoryDestPriority.setStatus("current")


class _RdrFormatterCategoryDestStatus_Type(Integer32):
    """Custom type rdrFormatterCategoryDestStatus based on Integer32"""
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
          ("other", 1),
          ("standby", 3))
    )


_RdrFormatterCategoryDestStatus_Type.__name__ = "Integer32"
_RdrFormatterCategoryDestStatus_Object = MibTableColumn
rdrFormatterCategoryDestStatus = _RdrFormatterCategoryDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 6, 12, 1, 2),
    _RdrFormatterCategoryDestStatus_Type()
)
rdrFormatterCategoryDestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrFormatterCategoryDestStatus.setStatus("current")
_LoggerGrp_ObjectIdentity = ObjectIdentity
loggerGrp = _LoggerGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 7)
)


class _LoggerUserLogEnable_Type(Integer32):
    """Custom type loggerUserLogEnable based on Integer32"""
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


_LoggerUserLogEnable_Type.__name__ = "Integer32"
_LoggerUserLogEnable_Object = MibScalar
loggerUserLogEnable = _LoggerUserLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 7, 1),
    _LoggerUserLogEnable_Type()
)
loggerUserLogEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggerUserLogEnable.setStatus("current")


class _LoggerUserLogNumInfo_Type(Unsigned32):
    """Custom type loggerUserLogNumInfo based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LoggerUserLogNumInfo_Type.__name__ = "Unsigned32"
_LoggerUserLogNumInfo_Object = MibScalar
loggerUserLogNumInfo = _LoggerUserLogNumInfo_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 7, 2),
    _LoggerUserLogNumInfo_Type()
)
loggerUserLogNumInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggerUserLogNumInfo.setStatus("current")


class _LoggerUserLogNumWarning_Type(Unsigned32):
    """Custom type loggerUserLogNumWarning based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LoggerUserLogNumWarning_Type.__name__ = "Unsigned32"
_LoggerUserLogNumWarning_Object = MibScalar
loggerUserLogNumWarning = _LoggerUserLogNumWarning_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 7, 3),
    _LoggerUserLogNumWarning_Type()
)
loggerUserLogNumWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggerUserLogNumWarning.setStatus("current")


class _LoggerUserLogNumError_Type(Unsigned32):
    """Custom type loggerUserLogNumError based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LoggerUserLogNumError_Type.__name__ = "Unsigned32"
_LoggerUserLogNumError_Object = MibScalar
loggerUserLogNumError = _LoggerUserLogNumError_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 7, 4),
    _LoggerUserLogNumError_Type()
)
loggerUserLogNumError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggerUserLogNumError.setStatus("current")


class _LoggerUserLogNumFatal_Type(Unsigned32):
    """Custom type loggerUserLogNumFatal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LoggerUserLogNumFatal_Type.__name__ = "Unsigned32"
_LoggerUserLogNumFatal_Object = MibScalar
loggerUserLogNumFatal = _LoggerUserLogNumFatal_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 7, 5),
    _LoggerUserLogNumFatal_Type()
)
loggerUserLogNumFatal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggerUserLogNumFatal.setStatus("current")
_LoggerUserLogClearCountersTime_Type = TimeTicks
_LoggerUserLogClearCountersTime_Object = MibScalar
loggerUserLogClearCountersTime = _LoggerUserLogClearCountersTime_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 7, 6),
    _LoggerUserLogClearCountersTime_Type()
)
loggerUserLogClearCountersTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loggerUserLogClearCountersTime.setStatus("current")
if mibBuilder.loadTexts:
    loggerUserLogClearCountersTime.setUnits("milliseconds")
_SubscribersGrp_ObjectIdentity = ObjectIdentity
subscribersGrp = _SubscribersGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8)
)
_SubscribersInfoTable_Object = MibTable
subscribersInfoTable = _SubscribersInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 1)
)
if mibBuilder.loadTexts:
    subscribersInfoTable.setStatus("current")
_SubscribersInfoEntry_Object = MibTableRow
subscribersInfoEntry = _SubscribersInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 1, 1)
)
subscribersInfoEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "pmoduleIndex"),
)
if mibBuilder.loadTexts:
    subscribersInfoEntry.setStatus("current")


class _SubscribersNumIntroduced_Type(Unsigned32):
    """Custom type subscribersNumIntroduced based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SubscribersNumIntroduced_Type.__name__ = "Unsigned32"
_SubscribersNumIntroduced_Object = MibTableColumn
subscribersNumIntroduced = _SubscribersNumIntroduced_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 1, 1, 1),
    _SubscribersNumIntroduced_Type()
)
subscribersNumIntroduced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscribersNumIntroduced.setStatus("current")


class _SubscribersNumFree_Type(Unsigned32):
    """Custom type subscribersNumFree based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SubscribersNumFree_Type.__name__ = "Unsigned32"
_SubscribersNumFree_Object = MibTableColumn
subscribersNumFree = _SubscribersNumFree_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 1, 1, 2),
    _SubscribersNumFree_Type()
)
subscribersNumFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscribersNumFree.setStatus("current")


class _SubscribersNumIpAddrMappings_Type(Unsigned32):
    """Custom type subscribersNumIpAddrMappings based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SubscribersNumIpAddrMappings_Type.__name__ = "Unsigned32"
_SubscribersNumIpAddrMappings_Object = MibTableColumn
subscribersNumIpAddrMappings = _SubscribersNumIpAddrMappings_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 1, 1, 3),
    _SubscribersNumIpAddrMappings_Type()
)
subscribersNumIpAddrMappings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscribersNumIpAddrMappings.setStatus("current")


class _SubscribersNumIpAddrMappingsFree_Type(Unsigned32):
    """Custom type subscribersNumIpAddrMappingsFree based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SubscribersNumIpAddrMappingsFree_Type.__name__ = "Unsigned32"
_SubscribersNumIpAddrMappingsFree_Object = MibTableColumn
subscribersNumIpAddrMappingsFree = _SubscribersNumIpAddrMappingsFree_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 1, 1, 4),
    _SubscribersNumIpAddrMappingsFree_Type()
)
subscribersNumIpAddrMappingsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscribersNumIpAddrMappingsFree.setStatus("current")


class _SubscribersNumIpRangeMappings_Type(Unsigned32):
    """Custom type subscribersNumIpRangeMappings based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SubscribersNumIpRangeMappings_Type.__name__ = "Unsigned32"
_SubscribersNumIpRangeMappings_Object = MibTableColumn
subscribersNumIpRangeMappings = _SubscribersNumIpRangeMappings_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 1, 1, 5),
    _SubscribersNumIpRangeMappings_Type()
)
subscribersNumIpRangeMappings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscribersNumIpRangeMappings.setStatus("current")


class _SubscribersNumIpRangeMappingsFree_Type(Unsigned32):
    """Custom type subscribersNumIpRangeMappingsFree based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SubscribersNumIpRangeMappingsFree_Type.__name__ = "Unsigned32"
_SubscribersNumIpRangeMappingsFree_Object = MibTableColumn
subscribersNumIpRangeMappingsFree = _SubscribersNumIpRangeMappingsFree_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 1, 1, 6),
    _SubscribersNumIpRangeMappingsFree_Type()
)
subscribersNumIpRangeMappingsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscribersNumIpRangeMappingsFree.setStatus("current")


class _SubscribersNumVlanMappings_Type(Unsigned32):
    """Custom type subscribersNumVlanMappings based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SubscribersNumVlanMappings_Type.__name__ = "Unsigned32"
_SubscribersNumVlanMappings_Object = MibTableColumn
subscribersNumVlanMappings = _SubscribersNumVlanMappings_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 1, 1, 7),
    _SubscribersNumVlanMappings_Type()
)
subscribersNumVlanMappings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscribersNumVlanMappings.setStatus("current")


class _SubscribersNumVlanMappingsFree_Type(Unsigned32):
    """Custom type subscribersNumVlanMappingsFree based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SubscribersNumVlanMappingsFree_Type.__name__ = "Unsigned32"
_SubscribersNumVlanMappingsFree_Object = MibTableColumn
subscribersNumVlanMappingsFree = _SubscribersNumVlanMappingsFree_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 1, 1, 8),
    _SubscribersNumVlanMappingsFree_Type()
)
subscribersNumVlanMappingsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscribersNumVlanMappingsFree.setStatus("current")


class _SubscribersNumActive_Type(Unsigned32):
    """Custom type subscribersNumActive based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SubscribersNumActive_Type.__name__ = "Unsigned32"
_SubscribersNumActive_Object = MibTableColumn
subscribersNumActive = _SubscribersNumActive_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 1, 1, 9),
    _SubscribersNumActive_Type()
)
subscribersNumActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscribersNumActive.setStatus("current")


class _SubscribersNumActivePeak_Type(Unsigned32):
    """Custom type subscribersNumActivePeak based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SubscribersNumActivePeak_Type.__name__ = "Unsigned32"
_SubscribersNumActivePeak_Object = MibTableColumn
subscribersNumActivePeak = _SubscribersNumActivePeak_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 1, 1, 10),
    _SubscribersNumActivePeak_Type()
)
subscribersNumActivePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscribersNumActivePeak.setStatus("current")
_SubscribersNumActivePeakTime_Type = TimeTicks
_SubscribersNumActivePeakTime_Object = MibTableColumn
subscribersNumActivePeakTime = _SubscribersNumActivePeakTime_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 1, 1, 11),
    _SubscribersNumActivePeakTime_Type()
)
subscribersNumActivePeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscribersNumActivePeakTime.setStatus("current")
if mibBuilder.loadTexts:
    subscribersNumActivePeakTime.setUnits("milliseconds")


class _SubscribersNumUpdates_Type(Unsigned32):
    """Custom type subscribersNumUpdates based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SubscribersNumUpdates_Type.__name__ = "Unsigned32"
_SubscribersNumUpdates_Object = MibTableColumn
subscribersNumUpdates = _SubscribersNumUpdates_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 1, 1, 12),
    _SubscribersNumUpdates_Type()
)
subscribersNumUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscribersNumUpdates.setStatus("current")
_SubscribersCountersClearTime_Type = TimeTicks
_SubscribersCountersClearTime_Object = MibTableColumn
subscribersCountersClearTime = _SubscribersCountersClearTime_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 1, 1, 13),
    _SubscribersCountersClearTime_Type()
)
subscribersCountersClearTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscribersCountersClearTime.setStatus("current")
if mibBuilder.loadTexts:
    subscribersCountersClearTime.setUnits("milliseconds")


class _SubscribersNumTpIpRanges_Type(Unsigned32):
    """Custom type subscribersNumTpIpRanges based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SubscribersNumTpIpRanges_Type.__name__ = "Unsigned32"
_SubscribersNumTpIpRanges_Object = MibTableColumn
subscribersNumTpIpRanges = _SubscribersNumTpIpRanges_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 1, 1, 14),
    _SubscribersNumTpIpRanges_Type()
)
subscribersNumTpIpRanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscribersNumTpIpRanges.setStatus("current")


class _SubscribersNumTpIpRangesFree_Type(Unsigned32):
    """Custom type subscribersNumTpIpRangesFree based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SubscribersNumTpIpRangesFree_Type.__name__ = "Unsigned32"
_SubscribersNumTpIpRangesFree_Object = MibTableColumn
subscribersNumTpIpRangesFree = _SubscribersNumTpIpRangesFree_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 1, 1, 15),
    _SubscribersNumTpIpRangesFree_Type()
)
subscribersNumTpIpRangesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscribersNumTpIpRangesFree.setStatus("current")


class _SubscribersNumAnonymous_Type(Unsigned32):
    """Custom type subscribersNumAnonymous based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SubscribersNumAnonymous_Type.__name__ = "Unsigned32"
_SubscribersNumAnonymous_Object = MibTableColumn
subscribersNumAnonymous = _SubscribersNumAnonymous_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 1, 1, 16),
    _SubscribersNumAnonymous_Type()
)
subscribersNumAnonymous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscribersNumAnonymous.setStatus("current")


class _SubscribersNumWithSessions_Type(Unsigned32):
    """Custom type subscribersNumWithSessions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SubscribersNumWithSessions_Type.__name__ = "Unsigned32"
_SubscribersNumWithSessions_Object = MibTableColumn
subscribersNumWithSessions = _SubscribersNumWithSessions_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 1, 1, 17),
    _SubscribersNumWithSessions_Type()
)
subscribersNumWithSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscribersNumWithSessions.setStatus("current")
_SubscribersPropertiesTable_Object = MibTable
subscribersPropertiesTable = _SubscribersPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 2)
)
if mibBuilder.loadTexts:
    subscribersPropertiesTable.setStatus("current")
_SubscribersPropertiesEntry_Object = MibTableRow
subscribersPropertiesEntry = _SubscribersPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 2, 1)
)
subscribersPropertiesEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "pmoduleIndex"),
    (0, "PCUBE-SE-MIB", "spIndex"),
)
if mibBuilder.loadTexts:
    subscribersPropertiesEntry.setStatus("current")


class _SpIndex_Type(Integer32):
    """Custom type spIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_SpIndex_Type.__name__ = "Integer32"
_SpIndex_Object = MibTableColumn
spIndex = _SpIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 2, 1, 1),
    _SpIndex_Type()
)
spIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spIndex.setStatus("current")


class _SpName_Type(SnmpAdminString):
    """Custom type spName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SpName_Type.__name__ = "SnmpAdminString"
_SpName_Object = MibTableColumn
spName = _SpName_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 2, 1, 2),
    _SpName_Type()
)
spName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spName.setStatus("current")
_SpType_Type = SnmpAdminString
_SpType_Object = MibTableColumn
spType = _SpType_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 2, 1, 3),
    _SpType_Type()
)
spType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spType.setStatus("current")
_SubscribersPropertiesValueTable_Object = MibTable
subscribersPropertiesValueTable = _SubscribersPropertiesValueTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 3)
)
if mibBuilder.loadTexts:
    subscribersPropertiesValueTable.setStatus("current")
_SubscribersPropertiesValueEntry_Object = MibTableRow
subscribersPropertiesValueEntry = _SubscribersPropertiesValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 3, 1)
)
subscribersPropertiesValueEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "pmoduleIndex"),
    (0, "PCUBE-SE-MIB", "spvIndex"),
)
if mibBuilder.loadTexts:
    subscribersPropertiesValueEntry.setStatus("current")


class _SpvIndex_Type(Integer32):
    """Custom type spvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_SpvIndex_Type.__name__ = "Integer32"
_SpvIndex_Object = MibTableColumn
spvIndex = _SpvIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 3, 1, 1),
    _SpvIndex_Type()
)
spvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    spvIndex.setStatus("current")


class _SpvSubName_Type(SnmpAdminString):
    """Custom type spvSubName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_SpvSubName_Type.__name__ = "SnmpAdminString"
_SpvSubName_Object = MibTableColumn
spvSubName = _SpvSubName_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 3, 1, 2),
    _SpvSubName_Type()
)
spvSubName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spvSubName.setStatus("current")


class _SpvPropertyName_Type(SnmpAdminString):
    """Custom type spvPropertyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SpvPropertyName_Type.__name__ = "SnmpAdminString"
_SpvPropertyName_Object = MibTableColumn
spvPropertyName = _SpvPropertyName_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 3, 1, 3),
    _SpvPropertyName_Type()
)
spvPropertyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spvPropertyName.setStatus("current")
_SpvRowStatus_Type = RowStatus
_SpvRowStatus_Object = MibTableColumn
spvRowStatus = _SpvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 3, 1, 4),
    _SpvRowStatus_Type()
)
spvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    spvRowStatus.setStatus("current")


class _SpvPropertyStringValue_Type(SnmpAdminString):
    """Custom type spvPropertyStringValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SpvPropertyStringValue_Type.__name__ = "SnmpAdminString"
_SpvPropertyStringValue_Object = MibTableColumn
spvPropertyStringValue = _SpvPropertyStringValue_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 3, 1, 5),
    _SpvPropertyStringValue_Type()
)
spvPropertyStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spvPropertyStringValue.setStatus("current")


class _SpvPropertyUintValue_Type(Unsigned32):
    """Custom type spvPropertyUintValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SpvPropertyUintValue_Type.__name__ = "Unsigned32"
_SpvPropertyUintValue_Object = MibTableColumn
spvPropertyUintValue = _SpvPropertyUintValue_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 3, 1, 6),
    _SpvPropertyUintValue_Type()
)
spvPropertyUintValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spvPropertyUintValue.setStatus("current")
_SpvPropertyCounter64Value_Type = Counter64
_SpvPropertyCounter64Value_Object = MibTableColumn
spvPropertyCounter64Value = _SpvPropertyCounter64Value_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 8, 3, 1, 7),
    _SpvPropertyCounter64Value_Type()
)
spvPropertyCounter64Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spvPropertyCounter64Value.setStatus("current")
_TrafficProcessorGrp_ObjectIdentity = ObjectIdentity
trafficProcessorGrp = _TrafficProcessorGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9)
)
_TpInfoTable_Object = MibTable
tpInfoTable = _TpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1)
)
if mibBuilder.loadTexts:
    tpInfoTable.setStatus("current")
_TpInfoEntry_Object = MibTableRow
tpInfoEntry = _TpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1)
)
tpInfoEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "tpModuleIndex"),
    (0, "PCUBE-SE-MIB", "tpIndex"),
)
if mibBuilder.loadTexts:
    tpInfoEntry.setStatus("current")


class _TpModuleIndex_Type(Integer32):
    """Custom type tpModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TpModuleIndex_Type.__name__ = "Integer32"
_TpModuleIndex_Object = MibTableColumn
tpModuleIndex = _TpModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 1),
    _TpModuleIndex_Type()
)
tpModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpModuleIndex.setStatus("current")


class _TpIndex_Type(Integer32):
    """Custom type tpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TpIndex_Type.__name__ = "Integer32"
_TpIndex_Object = MibTableColumn
tpIndex = _TpIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 2),
    _TpIndex_Type()
)
tpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIndex.setStatus("current")


class _TpTotalNumHandledPackets_Type(Unsigned32):
    """Custom type tpTotalNumHandledPackets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TpTotalNumHandledPackets_Type.__name__ = "Unsigned32"
_TpTotalNumHandledPackets_Object = MibTableColumn
tpTotalNumHandledPackets = _TpTotalNumHandledPackets_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 3),
    _TpTotalNumHandledPackets_Type()
)
tpTotalNumHandledPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpTotalNumHandledPackets.setStatus("current")


class _TpTotalNumHandledFlows_Type(Unsigned32):
    """Custom type tpTotalNumHandledFlows based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TpTotalNumHandledFlows_Type.__name__ = "Unsigned32"
_TpTotalNumHandledFlows_Object = MibTableColumn
tpTotalNumHandledFlows = _TpTotalNumHandledFlows_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 4),
    _TpTotalNumHandledFlows_Type()
)
tpTotalNumHandledFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpTotalNumHandledFlows.setStatus("current")


class _TpNumActiveFlows_Type(Unsigned32):
    """Custom type tpNumActiveFlows based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TpNumActiveFlows_Type.__name__ = "Unsigned32"
_TpNumActiveFlows_Object = MibTableColumn
tpNumActiveFlows = _TpNumActiveFlows_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 5),
    _TpNumActiveFlows_Type()
)
tpNumActiveFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpNumActiveFlows.setStatus("current")


class _TpNumActiveFlowsPeak_Type(Unsigned32):
    """Custom type tpNumActiveFlowsPeak based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TpNumActiveFlowsPeak_Type.__name__ = "Unsigned32"
_TpNumActiveFlowsPeak_Object = MibTableColumn
tpNumActiveFlowsPeak = _TpNumActiveFlowsPeak_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 6),
    _TpNumActiveFlowsPeak_Type()
)
tpNumActiveFlowsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpNumActiveFlowsPeak.setStatus("current")
_TpNumActiveFlowsPeakTime_Type = TimeTicks
_TpNumActiveFlowsPeakTime_Object = MibTableColumn
tpNumActiveFlowsPeakTime = _TpNumActiveFlowsPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 7),
    _TpNumActiveFlowsPeakTime_Type()
)
tpNumActiveFlowsPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpNumActiveFlowsPeakTime.setStatus("current")
if mibBuilder.loadTexts:
    tpNumActiveFlowsPeakTime.setUnits("milliseconds")


class _TpNumTcpActiveFlows_Type(Unsigned32):
    """Custom type tpNumTcpActiveFlows based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TpNumTcpActiveFlows_Type.__name__ = "Unsigned32"
_TpNumTcpActiveFlows_Object = MibTableColumn
tpNumTcpActiveFlows = _TpNumTcpActiveFlows_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 8),
    _TpNumTcpActiveFlows_Type()
)
tpNumTcpActiveFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpNumTcpActiveFlows.setStatus("current")


class _TpNumTcpActiveFlowsPeak_Type(Unsigned32):
    """Custom type tpNumTcpActiveFlowsPeak based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TpNumTcpActiveFlowsPeak_Type.__name__ = "Unsigned32"
_TpNumTcpActiveFlowsPeak_Object = MibTableColumn
tpNumTcpActiveFlowsPeak = _TpNumTcpActiveFlowsPeak_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 9),
    _TpNumTcpActiveFlowsPeak_Type()
)
tpNumTcpActiveFlowsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpNumTcpActiveFlowsPeak.setStatus("current")
_TpNumTcpActiveFlowsPeakTime_Type = TimeTicks
_TpNumTcpActiveFlowsPeakTime_Object = MibTableColumn
tpNumTcpActiveFlowsPeakTime = _TpNumTcpActiveFlowsPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 10),
    _TpNumTcpActiveFlowsPeakTime_Type()
)
tpNumTcpActiveFlowsPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpNumTcpActiveFlowsPeakTime.setStatus("current")
if mibBuilder.loadTexts:
    tpNumTcpActiveFlowsPeakTime.setUnits("milliseconds")


class _TpNumUdpActiveFlows_Type(Unsigned32):
    """Custom type tpNumUdpActiveFlows based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TpNumUdpActiveFlows_Type.__name__ = "Unsigned32"
_TpNumUdpActiveFlows_Object = MibTableColumn
tpNumUdpActiveFlows = _TpNumUdpActiveFlows_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 11),
    _TpNumUdpActiveFlows_Type()
)
tpNumUdpActiveFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpNumUdpActiveFlows.setStatus("current")


class _TpNumUdpActiveFlowsPeak_Type(Unsigned32):
    """Custom type tpNumUdpActiveFlowsPeak based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TpNumUdpActiveFlowsPeak_Type.__name__ = "Unsigned32"
_TpNumUdpActiveFlowsPeak_Object = MibTableColumn
tpNumUdpActiveFlowsPeak = _TpNumUdpActiveFlowsPeak_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 12),
    _TpNumUdpActiveFlowsPeak_Type()
)
tpNumUdpActiveFlowsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpNumUdpActiveFlowsPeak.setStatus("current")
_TpNumUdpActiveFlowsPeakTime_Type = TimeTicks
_TpNumUdpActiveFlowsPeakTime_Object = MibTableColumn
tpNumUdpActiveFlowsPeakTime = _TpNumUdpActiveFlowsPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 13),
    _TpNumUdpActiveFlowsPeakTime_Type()
)
tpNumUdpActiveFlowsPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpNumUdpActiveFlowsPeakTime.setStatus("current")
if mibBuilder.loadTexts:
    tpNumUdpActiveFlowsPeakTime.setUnits("milliseconds")


class _TpNumNonTcpUdpActiveFlows_Type(Unsigned32):
    """Custom type tpNumNonTcpUdpActiveFlows based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TpNumNonTcpUdpActiveFlows_Type.__name__ = "Unsigned32"
_TpNumNonTcpUdpActiveFlows_Object = MibTableColumn
tpNumNonTcpUdpActiveFlows = _TpNumNonTcpUdpActiveFlows_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 14),
    _TpNumNonTcpUdpActiveFlows_Type()
)
tpNumNonTcpUdpActiveFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpNumNonTcpUdpActiveFlows.setStatus("current")


class _TpNumNonTcpUdpActiveFlowsPeak_Type(Unsigned32):
    """Custom type tpNumNonTcpUdpActiveFlowsPeak based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TpNumNonTcpUdpActiveFlowsPeak_Type.__name__ = "Unsigned32"
_TpNumNonTcpUdpActiveFlowsPeak_Object = MibTableColumn
tpNumNonTcpUdpActiveFlowsPeak = _TpNumNonTcpUdpActiveFlowsPeak_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 15),
    _TpNumNonTcpUdpActiveFlowsPeak_Type()
)
tpNumNonTcpUdpActiveFlowsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpNumNonTcpUdpActiveFlowsPeak.setStatus("current")
_TpNumNonTcpUdpActiveFlowsPeakTime_Type = TimeTicks
_TpNumNonTcpUdpActiveFlowsPeakTime_Object = MibTableColumn
tpNumNonTcpUdpActiveFlowsPeakTime = _TpNumNonTcpUdpActiveFlowsPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 16),
    _TpNumNonTcpUdpActiveFlowsPeakTime_Type()
)
tpNumNonTcpUdpActiveFlowsPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpNumNonTcpUdpActiveFlowsPeakTime.setStatus("current")
if mibBuilder.loadTexts:
    tpNumNonTcpUdpActiveFlowsPeakTime.setUnits("milliseconds")


class _TpTotalNumBlockedPackets_Type(Unsigned32):
    """Custom type tpTotalNumBlockedPackets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TpTotalNumBlockedPackets_Type.__name__ = "Unsigned32"
_TpTotalNumBlockedPackets_Object = MibTableColumn
tpTotalNumBlockedPackets = _TpTotalNumBlockedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 17),
    _TpTotalNumBlockedPackets_Type()
)
tpTotalNumBlockedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpTotalNumBlockedPackets.setStatus("current")


class _TpTotalNumBlockedFlows_Type(Unsigned32):
    """Custom type tpTotalNumBlockedFlows based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TpTotalNumBlockedFlows_Type.__name__ = "Unsigned32"
_TpTotalNumBlockedFlows_Object = MibTableColumn
tpTotalNumBlockedFlows = _TpTotalNumBlockedFlows_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 18),
    _TpTotalNumBlockedFlows_Type()
)
tpTotalNumBlockedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpTotalNumBlockedFlows.setStatus("current")


class _TpTotalNumDiscardedPacketsDueToBwLimit_Type(Unsigned32):
    """Custom type tpTotalNumDiscardedPacketsDueToBwLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TpTotalNumDiscardedPacketsDueToBwLimit_Type.__name__ = "Unsigned32"
_TpTotalNumDiscardedPacketsDueToBwLimit_Object = MibTableColumn
tpTotalNumDiscardedPacketsDueToBwLimit = _TpTotalNumDiscardedPacketsDueToBwLimit_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 19),
    _TpTotalNumDiscardedPacketsDueToBwLimit_Type()
)
tpTotalNumDiscardedPacketsDueToBwLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpTotalNumDiscardedPacketsDueToBwLimit.setStatus("current")


class _TpTotalNumWredDiscardedPackets_Type(Unsigned32):
    """Custom type tpTotalNumWredDiscardedPackets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TpTotalNumWredDiscardedPackets_Type.__name__ = "Unsigned32"
_TpTotalNumWredDiscardedPackets_Object = MibTableColumn
tpTotalNumWredDiscardedPackets = _TpTotalNumWredDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 20),
    _TpTotalNumWredDiscardedPackets_Type()
)
tpTotalNumWredDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpTotalNumWredDiscardedPackets.setStatus("current")


class _TpTotalNumFragments_Type(Unsigned32):
    """Custom type tpTotalNumFragments based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TpTotalNumFragments_Type.__name__ = "Unsigned32"
_TpTotalNumFragments_Object = MibTableColumn
tpTotalNumFragments = _TpTotalNumFragments_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 21),
    _TpTotalNumFragments_Type()
)
tpTotalNumFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpTotalNumFragments.setStatus("current")


class _TpTotalNumNonIpPackets_Type(Unsigned32):
    """Custom type tpTotalNumNonIpPackets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TpTotalNumNonIpPackets_Type.__name__ = "Unsigned32"
_TpTotalNumNonIpPackets_Object = MibTableColumn
tpTotalNumNonIpPackets = _TpTotalNumNonIpPackets_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 22),
    _TpTotalNumNonIpPackets_Type()
)
tpTotalNumNonIpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpTotalNumNonIpPackets.setStatus("current")


class _TpTotalNumIpCrcErrPackets_Type(Unsigned32):
    """Custom type tpTotalNumIpCrcErrPackets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TpTotalNumIpCrcErrPackets_Type.__name__ = "Unsigned32"
_TpTotalNumIpCrcErrPackets_Object = MibTableColumn
tpTotalNumIpCrcErrPackets = _TpTotalNumIpCrcErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 23),
    _TpTotalNumIpCrcErrPackets_Type()
)
tpTotalNumIpCrcErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpTotalNumIpCrcErrPackets.setStatus("current")


class _TpTotalNumIpLengthErrPackets_Type(Unsigned32):
    """Custom type tpTotalNumIpLengthErrPackets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TpTotalNumIpLengthErrPackets_Type.__name__ = "Unsigned32"
_TpTotalNumIpLengthErrPackets_Object = MibTableColumn
tpTotalNumIpLengthErrPackets = _TpTotalNumIpLengthErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 24),
    _TpTotalNumIpLengthErrPackets_Type()
)
tpTotalNumIpLengthErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpTotalNumIpLengthErrPackets.setStatus("current")


class _TpTotalNumIpBroadcastPackets_Type(Unsigned32):
    """Custom type tpTotalNumIpBroadcastPackets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TpTotalNumIpBroadcastPackets_Type.__name__ = "Unsigned32"
_TpTotalNumIpBroadcastPackets_Object = MibTableColumn
tpTotalNumIpBroadcastPackets = _TpTotalNumIpBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 25),
    _TpTotalNumIpBroadcastPackets_Type()
)
tpTotalNumIpBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpTotalNumIpBroadcastPackets.setStatus("current")


class _TpTotalNumTtlErrPackets_Type(Unsigned32):
    """Custom type tpTotalNumTtlErrPackets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TpTotalNumTtlErrPackets_Type.__name__ = "Unsigned32"
_TpTotalNumTtlErrPackets_Object = MibTableColumn
tpTotalNumTtlErrPackets = _TpTotalNumTtlErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 26),
    _TpTotalNumTtlErrPackets_Type()
)
tpTotalNumTtlErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpTotalNumTtlErrPackets.setStatus("current")


class _TpTotalNumTcpUdpCrcErrPackets_Type(Unsigned32):
    """Custom type tpTotalNumTcpUdpCrcErrPackets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TpTotalNumTcpUdpCrcErrPackets_Type.__name__ = "Unsigned32"
_TpTotalNumTcpUdpCrcErrPackets_Object = MibTableColumn
tpTotalNumTcpUdpCrcErrPackets = _TpTotalNumTcpUdpCrcErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 27),
    _TpTotalNumTcpUdpCrcErrPackets_Type()
)
tpTotalNumTcpUdpCrcErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpTotalNumTcpUdpCrcErrPackets.setStatus("current")
_TpClearCountersTime_Type = TimeTicks
_TpClearCountersTime_Object = MibTableColumn
tpClearCountersTime = _TpClearCountersTime_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 28),
    _TpClearCountersTime_Type()
)
tpClearCountersTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpClearCountersTime.setStatus("current")
if mibBuilder.loadTexts:
    tpClearCountersTime.setUnits("milliseconds")


class _TpHandledPacketsRate_Type(Unsigned32):
    """Custom type tpHandledPacketsRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TpHandledPacketsRate_Type.__name__ = "Unsigned32"
_TpHandledPacketsRate_Object = MibTableColumn
tpHandledPacketsRate = _TpHandledPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 29),
    _TpHandledPacketsRate_Type()
)
tpHandledPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpHandledPacketsRate.setStatus("current")


class _TpHandledPacketsRatePeak_Type(Unsigned32):
    """Custom type tpHandledPacketsRatePeak based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TpHandledPacketsRatePeak_Type.__name__ = "Unsigned32"
_TpHandledPacketsRatePeak_Object = MibTableColumn
tpHandledPacketsRatePeak = _TpHandledPacketsRatePeak_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 30),
    _TpHandledPacketsRatePeak_Type()
)
tpHandledPacketsRatePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpHandledPacketsRatePeak.setStatus("current")
_TpHandledPacketsRatePeakTime_Type = TimeTicks
_TpHandledPacketsRatePeakTime_Object = MibTableColumn
tpHandledPacketsRatePeakTime = _TpHandledPacketsRatePeakTime_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 31),
    _TpHandledPacketsRatePeakTime_Type()
)
tpHandledPacketsRatePeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpHandledPacketsRatePeakTime.setStatus("current")
if mibBuilder.loadTexts:
    tpHandledPacketsRatePeakTime.setUnits("milliseconds")


class _TpHandledFlowsRate_Type(Unsigned32):
    """Custom type tpHandledFlowsRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TpHandledFlowsRate_Type.__name__ = "Unsigned32"
_TpHandledFlowsRate_Object = MibTableColumn
tpHandledFlowsRate = _TpHandledFlowsRate_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 32),
    _TpHandledFlowsRate_Type()
)
tpHandledFlowsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpHandledFlowsRate.setStatus("current")


class _TpHandledFlowsRatePeak_Type(Unsigned32):
    """Custom type tpHandledFlowsRatePeak based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TpHandledFlowsRatePeak_Type.__name__ = "Unsigned32"
_TpHandledFlowsRatePeak_Object = MibTableColumn
tpHandledFlowsRatePeak = _TpHandledFlowsRatePeak_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 33),
    _TpHandledFlowsRatePeak_Type()
)
tpHandledFlowsRatePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpHandledFlowsRatePeak.setStatus("current")
_TpHandledFlowsRatePeakTime_Type = TimeTicks
_TpHandledFlowsRatePeakTime_Object = MibTableColumn
tpHandledFlowsRatePeakTime = _TpHandledFlowsRatePeakTime_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 34),
    _TpHandledFlowsRatePeakTime_Type()
)
tpHandledFlowsRatePeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpHandledFlowsRatePeakTime.setStatus("current")
if mibBuilder.loadTexts:
    tpHandledFlowsRatePeakTime.setUnits("milliseconds")


class _TpCpuUtilization_Type(Integer32):
    """Custom type tpCpuUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TpCpuUtilization_Type.__name__ = "Integer32"
_TpCpuUtilization_Object = MibTableColumn
tpCpuUtilization = _TpCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 35),
    _TpCpuUtilization_Type()
)
tpCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpCpuUtilization.setStatus("current")


class _TpCpuUtilizationPeak_Type(Integer32):
    """Custom type tpCpuUtilizationPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TpCpuUtilizationPeak_Type.__name__ = "Integer32"
_TpCpuUtilizationPeak_Object = MibTableColumn
tpCpuUtilizationPeak = _TpCpuUtilizationPeak_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 36),
    _TpCpuUtilizationPeak_Type()
)
tpCpuUtilizationPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpCpuUtilizationPeak.setStatus("current")
_TpCpuUtilizationPeakTime_Type = TimeTicks
_TpCpuUtilizationPeakTime_Object = MibTableColumn
tpCpuUtilizationPeakTime = _TpCpuUtilizationPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 37),
    _TpCpuUtilizationPeakTime_Type()
)
tpCpuUtilizationPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpCpuUtilizationPeakTime.setStatus("current")
if mibBuilder.loadTexts:
    tpCpuUtilizationPeakTime.setUnits("milliseconds")


class _TpFlowsCapacityUtilization_Type(Integer32):
    """Custom type tpFlowsCapacityUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TpFlowsCapacityUtilization_Type.__name__ = "Integer32"
_TpFlowsCapacityUtilization_Object = MibTableColumn
tpFlowsCapacityUtilization = _TpFlowsCapacityUtilization_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 38),
    _TpFlowsCapacityUtilization_Type()
)
tpFlowsCapacityUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpFlowsCapacityUtilization.setStatus("current")


class _TpFlowsCapacityUtilizationPeak_Type(Integer32):
    """Custom type tpFlowsCapacityUtilizationPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TpFlowsCapacityUtilizationPeak_Type.__name__ = "Integer32"
_TpFlowsCapacityUtilizationPeak_Object = MibTableColumn
tpFlowsCapacityUtilizationPeak = _TpFlowsCapacityUtilizationPeak_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 39),
    _TpFlowsCapacityUtilizationPeak_Type()
)
tpFlowsCapacityUtilizationPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpFlowsCapacityUtilizationPeak.setStatus("current")
_TpFlowsCapacityUtilizationPeakTime_Type = TimeTicks
_TpFlowsCapacityUtilizationPeakTime_Object = MibTableColumn
tpFlowsCapacityUtilizationPeakTime = _TpFlowsCapacityUtilizationPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 40),
    _TpFlowsCapacityUtilizationPeakTime_Type()
)
tpFlowsCapacityUtilizationPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpFlowsCapacityUtilizationPeakTime.setStatus("current")
if mibBuilder.loadTexts:
    tpFlowsCapacityUtilizationPeakTime.setUnits("milliseconds")


class _TpServiceLoss_Type(Integer32):
    """Custom type tpServiceLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TpServiceLoss_Type.__name__ = "Integer32"
_TpServiceLoss_Object = MibTableColumn
tpServiceLoss = _TpServiceLoss_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 9, 1, 1, 41),
    _TpServiceLoss_Type()
)
tpServiceLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpServiceLoss.setStatus("current")
_PportGrp_ObjectIdentity = ObjectIdentity
pportGrp = _PportGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 10)
)
_PportTable_Object = MibTable
pportTable = _PportTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 10, 1)
)
if mibBuilder.loadTexts:
    pportTable.setStatus("current")
_PportEntry_Object = MibTableRow
pportEntry = _PportEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 10, 1, 1)
)
pportEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "pportModuleIndex"),
    (0, "PCUBE-SE-MIB", "pportIndex"),
)
if mibBuilder.loadTexts:
    pportEntry.setStatus("current")


class _PportModuleIndex_Type(Integer32):
    """Custom type pportModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PportModuleIndex_Type.__name__ = "Integer32"
_PportModuleIndex_Object = MibTableColumn
pportModuleIndex = _PportModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 10, 1, 1, 1),
    _PportModuleIndex_Type()
)
pportModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportModuleIndex.setStatus("current")


class _PportIndex_Type(Integer32):
    """Custom type pportIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PportIndex_Type.__name__ = "Integer32"
_PportIndex_Object = MibTableColumn
pportIndex = _PportIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 10, 1, 1, 2),
    _PportIndex_Type()
)
pportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportIndex.setStatus("current")


class _PportType_Type(Integer32):
    """Custom type pportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              11,
              15,
              28)
        )
    )
    namedValues = NamedValues(
        *(("e1000BaseSX", 28),
          ("e1000BaseT", 15),
          ("e100BaseTX", 11),
          ("other", 1))
    )


_PportType_Type.__name__ = "Integer32"
_PportType_Object = MibTableColumn
pportType = _PportType_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 10, 1, 1, 3),
    _PportType_Type()
)
pportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportType.setStatus("current")


class _PportNumTxQueues_Type(Integer32):
    """Custom type pportNumTxQueues based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PportNumTxQueues_Type.__name__ = "Integer32"
_PportNumTxQueues_Object = MibTableColumn
pportNumTxQueues = _PportNumTxQueues_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 10, 1, 1, 4),
    _PportNumTxQueues_Type()
)
pportNumTxQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportNumTxQueues.setStatus("current")


class _PportIfIndex_Type(Integer32):
    """Custom type pportIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PportIfIndex_Type.__name__ = "Integer32"
_PportIfIndex_Object = MibTableColumn
pportIfIndex = _PportIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 10, 1, 1, 5),
    _PportIfIndex_Type()
)
pportIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportIfIndex.setStatus("current")


class _PportAdminSpeed_Type(Integer32):
    """Custom type pportAdminSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10000000,
              100000000,
              1000000000)
        )
    )
    namedValues = NamedValues(
        *(("autoNegotiation", 1),
          ("s10000000", 10000000),
          ("s100000000", 100000000),
          ("s1000000000", 1000000000))
    )


_PportAdminSpeed_Type.__name__ = "Integer32"
_PportAdminSpeed_Object = MibTableColumn
pportAdminSpeed = _PportAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 10, 1, 1, 6),
    _PportAdminSpeed_Type()
)
pportAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportAdminSpeed.setStatus("current")


class _PportAdminDuplex_Type(Integer32):
    """Custom type pportAdminDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("auto", 4),
          ("full", 2),
          ("half", 1))
    )


_PportAdminDuplex_Type.__name__ = "Integer32"
_PportAdminDuplex_Object = MibTableColumn
pportAdminDuplex = _PportAdminDuplex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 10, 1, 1, 7),
    _PportAdminDuplex_Type()
)
pportAdminDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportAdminDuplex.setStatus("current")


class _PportOperDuplex_Type(Integer32):
    """Custom type pportOperDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1))
    )


_PportOperDuplex_Type.__name__ = "Integer32"
_PportOperDuplex_Object = MibTableColumn
pportOperDuplex = _PportOperDuplex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 10, 1, 1, 8),
    _PportOperDuplex_Type()
)
pportOperDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportOperDuplex.setStatus("current")


class _PportLinkIndex_Type(Integer32):
    """Custom type pportLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_PportLinkIndex_Type.__name__ = "Integer32"
_PportLinkIndex_Object = MibTableColumn
pportLinkIndex = _PportLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 10, 1, 1, 9),
    _PportLinkIndex_Type()
)
pportLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportLinkIndex.setStatus("current")


class _PportOperStatus_Type(Integer32):
    """Custom type pportOperStatus based on Integer32"""
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
        *(("other", 1),
          ("otherDown", 5),
          ("redundancyForcingDown", 4),
          ("reflectionForcingDown", 3),
          ("up", 2))
    )


_PportOperStatus_Type.__name__ = "Integer32"
_PportOperStatus_Object = MibTableColumn
pportOperStatus = _PportOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 10, 1, 1, 10),
    _PportOperStatus_Type()
)
pportOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportOperStatus.setStatus("current")
_TxQueuesGrp_ObjectIdentity = ObjectIdentity
txQueuesGrp = _TxQueuesGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 11)
)
_TxQueuesTable_Object = MibTable
txQueuesTable = _TxQueuesTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 11, 1)
)
if mibBuilder.loadTexts:
    txQueuesTable.setStatus("current")
_TxQueuesEntry_Object = MibTableRow
txQueuesEntry = _TxQueuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 11, 1, 1)
)
txQueuesEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "txQueuesModuleIndex"),
    (0, "PCUBE-SE-MIB", "txQueuesPortIndex"),
    (0, "PCUBE-SE-MIB", "txQueuesQueueIndex"),
)
if mibBuilder.loadTexts:
    txQueuesEntry.setStatus("current")


class _TxQueuesModuleIndex_Type(Integer32):
    """Custom type txQueuesModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TxQueuesModuleIndex_Type.__name__ = "Integer32"
_TxQueuesModuleIndex_Object = MibTableColumn
txQueuesModuleIndex = _TxQueuesModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 11, 1, 1, 1),
    _TxQueuesModuleIndex_Type()
)
txQueuesModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txQueuesModuleIndex.setStatus("current")


class _TxQueuesPortIndex_Type(Integer32):
    """Custom type txQueuesPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TxQueuesPortIndex_Type.__name__ = "Integer32"
_TxQueuesPortIndex_Object = MibTableColumn
txQueuesPortIndex = _TxQueuesPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 11, 1, 1, 2),
    _TxQueuesPortIndex_Type()
)
txQueuesPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txQueuesPortIndex.setStatus("current")


class _TxQueuesQueueIndex_Type(Integer32):
    """Custom type txQueuesQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TxQueuesQueueIndex_Type.__name__ = "Integer32"
_TxQueuesQueueIndex_Object = MibTableColumn
txQueuesQueueIndex = _TxQueuesQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 11, 1, 1, 3),
    _TxQueuesQueueIndex_Type()
)
txQueuesQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txQueuesQueueIndex.setStatus("current")
_TxQueuesDescription_Type = SnmpAdminString
_TxQueuesDescription_Object = MibTableColumn
txQueuesDescription = _TxQueuesDescription_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 11, 1, 1, 4),
    _TxQueuesDescription_Type()
)
txQueuesDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txQueuesDescription.setStatus("current")


class _TxQueuesBandwidth_Type(Integer32):
    """Custom type txQueuesBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_TxQueuesBandwidth_Type.__name__ = "Integer32"
_TxQueuesBandwidth_Object = MibTableColumn
txQueuesBandwidth = _TxQueuesBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 11, 1, 1, 5),
    _TxQueuesBandwidth_Type()
)
txQueuesBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txQueuesBandwidth.setStatus("current")


class _TxQueuesUtilization_Type(Integer32):
    """Custom type txQueuesUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TxQueuesUtilization_Type.__name__ = "Integer32"
_TxQueuesUtilization_Object = MibTableColumn
txQueuesUtilization = _TxQueuesUtilization_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 11, 1, 1, 6),
    _TxQueuesUtilization_Type()
)
txQueuesUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txQueuesUtilization.setStatus("current")


class _TxQueuesUtilizationPeak_Type(Integer32):
    """Custom type txQueuesUtilizationPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TxQueuesUtilizationPeak_Type.__name__ = "Integer32"
_TxQueuesUtilizationPeak_Object = MibTableColumn
txQueuesUtilizationPeak = _TxQueuesUtilizationPeak_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 11, 1, 1, 7),
    _TxQueuesUtilizationPeak_Type()
)
txQueuesUtilizationPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txQueuesUtilizationPeak.setStatus("current")
_TxQueuesUtilizationPeakTime_Type = TimeTicks
_TxQueuesUtilizationPeakTime_Object = MibTableColumn
txQueuesUtilizationPeakTime = _TxQueuesUtilizationPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 11, 1, 1, 8),
    _TxQueuesUtilizationPeakTime_Type()
)
txQueuesUtilizationPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txQueuesUtilizationPeakTime.setStatus("current")
if mibBuilder.loadTexts:
    txQueuesUtilizationPeakTime.setUnits("milliseconds")
_TxQueuesClearCountersTime_Type = TimeTicks
_TxQueuesClearCountersTime_Object = MibTableColumn
txQueuesClearCountersTime = _TxQueuesClearCountersTime_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 11, 1, 1, 9),
    _TxQueuesClearCountersTime_Type()
)
txQueuesClearCountersTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txQueuesClearCountersTime.setStatus("current")
if mibBuilder.loadTexts:
    txQueuesClearCountersTime.setUnits("milliseconds")
_TxQueuesDroppedBytes_Type = Counter64
_TxQueuesDroppedBytes_Object = MibTableColumn
txQueuesDroppedBytes = _TxQueuesDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 11, 1, 1, 10),
    _TxQueuesDroppedBytes_Type()
)
txQueuesDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txQueuesDroppedBytes.setStatus("current")
if mibBuilder.loadTexts:
    txQueuesDroppedBytes.setUnits("bytes")
_GlobalControllersGrp_ObjectIdentity = ObjectIdentity
globalControllersGrp = _GlobalControllersGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 12)
)
_GlobalControllersTable_Object = MibTable
globalControllersTable = _GlobalControllersTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 12, 1)
)
if mibBuilder.loadTexts:
    globalControllersTable.setStatus("current")
_GlobalControllersEntry_Object = MibTableRow
globalControllersEntry = _GlobalControllersEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 12, 1, 1)
)
globalControllersEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "globalControllersModuleIndex"),
    (0, "PCUBE-SE-MIB", "globalControllersPortIndex"),
    (0, "PCUBE-SE-MIB", "globalControllersIndex"),
)
if mibBuilder.loadTexts:
    globalControllersEntry.setStatus("current")


class _GlobalControllersModuleIndex_Type(Integer32):
    """Custom type globalControllersModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GlobalControllersModuleIndex_Type.__name__ = "Integer32"
_GlobalControllersModuleIndex_Object = MibTableColumn
globalControllersModuleIndex = _GlobalControllersModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 12, 1, 1, 1),
    _GlobalControllersModuleIndex_Type()
)
globalControllersModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalControllersModuleIndex.setStatus("current")


class _GlobalControllersPortIndex_Type(Integer32):
    """Custom type globalControllersPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GlobalControllersPortIndex_Type.__name__ = "Integer32"
_GlobalControllersPortIndex_Object = MibTableColumn
globalControllersPortIndex = _GlobalControllersPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 12, 1, 1, 2),
    _GlobalControllersPortIndex_Type()
)
globalControllersPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalControllersPortIndex.setStatus("current")


class _GlobalControllersIndex_Type(Integer32):
    """Custom type globalControllersIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GlobalControllersIndex_Type.__name__ = "Integer32"
_GlobalControllersIndex_Object = MibTableColumn
globalControllersIndex = _GlobalControllersIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 12, 1, 1, 3),
    _GlobalControllersIndex_Type()
)
globalControllersIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalControllersIndex.setStatus("current")
_GlobalControllersDescription_Type = SnmpAdminString
_GlobalControllersDescription_Object = MibTableColumn
globalControllersDescription = _GlobalControllersDescription_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 12, 1, 1, 4),
    _GlobalControllersDescription_Type()
)
globalControllersDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalControllersDescription.setStatus("current")


class _GlobalControllersBandwidth_Type(Integer32):
    """Custom type globalControllersBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_GlobalControllersBandwidth_Type.__name__ = "Integer32"
_GlobalControllersBandwidth_Object = MibTableColumn
globalControllersBandwidth = _GlobalControllersBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 12, 1, 1, 5),
    _GlobalControllersBandwidth_Type()
)
globalControllersBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalControllersBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    globalControllersBandwidth.setUnits("Kbps")


class _GlobalControllersUtilization_Type(Integer32):
    """Custom type globalControllersUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GlobalControllersUtilization_Type.__name__ = "Integer32"
_GlobalControllersUtilization_Object = MibTableColumn
globalControllersUtilization = _GlobalControllersUtilization_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 12, 1, 1, 6),
    _GlobalControllersUtilization_Type()
)
globalControllersUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalControllersUtilization.setStatus("current")


class _GlobalControllersUtilizationPeak_Type(Integer32):
    """Custom type globalControllersUtilizationPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GlobalControllersUtilizationPeak_Type.__name__ = "Integer32"
_GlobalControllersUtilizationPeak_Object = MibTableColumn
globalControllersUtilizationPeak = _GlobalControllersUtilizationPeak_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 12, 1, 1, 7),
    _GlobalControllersUtilizationPeak_Type()
)
globalControllersUtilizationPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalControllersUtilizationPeak.setStatus("current")
_GlobalControllersUtilizationPeakTime_Type = TimeTicks
_GlobalControllersUtilizationPeakTime_Object = MibTableColumn
globalControllersUtilizationPeakTime = _GlobalControllersUtilizationPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 12, 1, 1, 8),
    _GlobalControllersUtilizationPeakTime_Type()
)
globalControllersUtilizationPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalControllersUtilizationPeakTime.setStatus("current")
if mibBuilder.loadTexts:
    globalControllersUtilizationPeakTime.setUnits("milliseconds")
_GlobalControllersClearCountersTime_Type = TimeTicks
_GlobalControllersClearCountersTime_Object = MibTableColumn
globalControllersClearCountersTime = _GlobalControllersClearCountersTime_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 12, 1, 1, 9),
    _GlobalControllersClearCountersTime_Type()
)
globalControllersClearCountersTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalControllersClearCountersTime.setStatus("current")
if mibBuilder.loadTexts:
    globalControllersClearCountersTime.setUnits("milliseconds")
_GlobalControllersDroppedBytes_Type = Counter64
_GlobalControllersDroppedBytes_Object = MibTableColumn
globalControllersDroppedBytes = _GlobalControllersDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 12, 1, 1, 10),
    _GlobalControllersDroppedBytes_Type()
)
globalControllersDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalControllersDroppedBytes.setStatus("current")
if mibBuilder.loadTexts:
    globalControllersDroppedBytes.setUnits("bytes")
_ApplicationGrp_ObjectIdentity = ObjectIdentity
applicationGrp = _ApplicationGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 13)
)
_AppInfoTable_Object = MibTable
appInfoTable = _AppInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 13, 1)
)
if mibBuilder.loadTexts:
    appInfoTable.setStatus("current")
_AppInfoEntry_Object = MibTableRow
appInfoEntry = _AppInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 13, 1, 1)
)
appInfoEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "pmoduleIndex"),
)
if mibBuilder.loadTexts:
    appInfoEntry.setStatus("current")
_AppName_Type = SnmpAdminString
_AppName_Object = MibTableColumn
appName = _AppName_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 13, 1, 1, 1),
    _AppName_Type()
)
appName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appName.setStatus("current")
_AppDescription_Type = SnmpAdminString
_AppDescription_Object = MibTableColumn
appDescription = _AppDescription_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 13, 1, 1, 2),
    _AppDescription_Type()
)
appDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDescription.setStatus("current")
_AppVersion_Type = SnmpAdminString
_AppVersion_Object = MibTableColumn
appVersion = _AppVersion_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 13, 1, 1, 3),
    _AppVersion_Type()
)
appVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appVersion.setStatus("current")
_AppPropertiesTable_Object = MibTable
appPropertiesTable = _AppPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 13, 2)
)
if mibBuilder.loadTexts:
    appPropertiesTable.setStatus("current")
_AppPropertiesEntry_Object = MibTableRow
appPropertiesEntry = _AppPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 13, 2, 1)
)
appPropertiesEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "pmoduleIndex"),
    (0, "PCUBE-SE-MIB", "apIndex"),
)
if mibBuilder.loadTexts:
    appPropertiesEntry.setStatus("current")


class _ApIndex_Type(Integer32):
    """Custom type apIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_ApIndex_Type.__name__ = "Integer32"
_ApIndex_Object = MibTableColumn
apIndex = _ApIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 13, 2, 1, 1),
    _ApIndex_Type()
)
apIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIndex.setStatus("current")


class _ApName_Type(SnmpAdminString):
    """Custom type apName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ApName_Type.__name__ = "SnmpAdminString"
_ApName_Object = MibTableColumn
apName = _ApName_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 13, 2, 1, 2),
    _ApName_Type()
)
apName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apName.setStatus("current")
_ApType_Type = SnmpAdminString
_ApType_Object = MibTableColumn
apType = _ApType_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 13, 2, 1, 3),
    _ApType_Type()
)
apType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apType.setStatus("current")
_AppPropertiesValueTable_Object = MibTable
appPropertiesValueTable = _AppPropertiesValueTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 13, 3)
)
if mibBuilder.loadTexts:
    appPropertiesValueTable.setStatus("current")
_AppPropertiesValueEntry_Object = MibTableRow
appPropertiesValueEntry = _AppPropertiesValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 13, 3, 1)
)
appPropertiesValueEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "pmoduleIndex"),
    (0, "PCUBE-SE-MIB", "apvIndex"),
)
if mibBuilder.loadTexts:
    appPropertiesValueEntry.setStatus("current")


class _ApvIndex_Type(Integer32):
    """Custom type apvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ApvIndex_Type.__name__ = "Integer32"
_ApvIndex_Object = MibTableColumn
apvIndex = _ApvIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 13, 3, 1, 1),
    _ApvIndex_Type()
)
apvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apvIndex.setStatus("current")


class _ApvPropertyName_Type(SnmpAdminString):
    """Custom type apvPropertyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ApvPropertyName_Type.__name__ = "SnmpAdminString"
_ApvPropertyName_Object = MibTableColumn
apvPropertyName = _ApvPropertyName_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 13, 3, 1, 2),
    _ApvPropertyName_Type()
)
apvPropertyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apvPropertyName.setStatus("current")
_ApvRowStatus_Type = RowStatus
_ApvRowStatus_Object = MibTableColumn
apvRowStatus = _ApvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 13, 3, 1, 3),
    _ApvRowStatus_Type()
)
apvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apvRowStatus.setStatus("current")


class _ApvPropertyStringValue_Type(SnmpAdminString):
    """Custom type apvPropertyStringValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ApvPropertyStringValue_Type.__name__ = "SnmpAdminString"
_ApvPropertyStringValue_Object = MibTableColumn
apvPropertyStringValue = _ApvPropertyStringValue_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 13, 3, 1, 4),
    _ApvPropertyStringValue_Type()
)
apvPropertyStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apvPropertyStringValue.setStatus("current")


class _ApvPropertyUintValue_Type(Unsigned32):
    """Custom type apvPropertyUintValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ApvPropertyUintValue_Type.__name__ = "Unsigned32"
_ApvPropertyUintValue_Object = MibTableColumn
apvPropertyUintValue = _ApvPropertyUintValue_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 13, 3, 1, 5),
    _ApvPropertyUintValue_Type()
)
apvPropertyUintValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apvPropertyUintValue.setStatus("current")
_ApvPropertyCounter64Value_Type = Counter64
_ApvPropertyCounter64Value_Object = MibTableColumn
apvPropertyCounter64Value = _ApvPropertyCounter64Value_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 13, 3, 1, 6),
    _ApvPropertyCounter64Value_Type()
)
apvPropertyCounter64Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apvPropertyCounter64Value.setStatus("current")
_TrafficCountersGrp_ObjectIdentity = ObjectIdentity
trafficCountersGrp = _TrafficCountersGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 14)
)
_TrafficCountersTable_Object = MibTable
trafficCountersTable = _TrafficCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 14, 1)
)
if mibBuilder.loadTexts:
    trafficCountersTable.setStatus("current")
_TrafficCountersEntry_Object = MibTableRow
trafficCountersEntry = _TrafficCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 14, 1, 1)
)
trafficCountersEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "pmoduleIndex"),
    (0, "PCUBE-SE-MIB", "trafficCounterIndex"),
)
if mibBuilder.loadTexts:
    trafficCountersEntry.setStatus("current")


class _TrafficCounterIndex_Type(Integer32):
    """Custom type trafficCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TrafficCounterIndex_Type.__name__ = "Integer32"
_TrafficCounterIndex_Object = MibTableColumn
trafficCounterIndex = _TrafficCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 14, 1, 1, 1),
    _TrafficCounterIndex_Type()
)
trafficCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficCounterIndex.setStatus("current")
_TrafficCounterValue_Type = Counter64
_TrafficCounterValue_Object = MibTableColumn
trafficCounterValue = _TrafficCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 14, 1, 1, 2),
    _TrafficCounterValue_Type()
)
trafficCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficCounterValue.setStatus("current")
_TrafficCounterName_Type = SnmpAdminString
_TrafficCounterName_Object = MibTableColumn
trafficCounterName = _TrafficCounterName_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 14, 1, 1, 3),
    _TrafficCounterName_Type()
)
trafficCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficCounterName.setStatus("current")


class _TrafficCounterType_Type(Integer32):
    """Custom type trafficCounterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bytes", 2),
          ("other", 1),
          ("packets", 3))
    )


_TrafficCounterType_Type.__name__ = "Integer32"
_TrafficCounterType_Object = MibTableColumn
trafficCounterType = _TrafficCounterType_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 14, 1, 1, 4),
    _TrafficCounterType_Type()
)
trafficCounterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficCounterType.setStatus("current")
_AttackGrp_ObjectIdentity = ObjectIdentity
attackGrp = _AttackGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 15)
)
_AttackTypeTable_Object = MibTable
attackTypeTable = _AttackTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 15, 1)
)
if mibBuilder.loadTexts:
    attackTypeTable.setStatus("current")
_AttackTypeEntry_Object = MibTableRow
attackTypeEntry = _AttackTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 15, 1, 1)
)
attackTypeEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "pmoduleIndex"),
    (0, "PCUBE-SE-MIB", "attackTypeIndex"),
)
if mibBuilder.loadTexts:
    attackTypeEntry.setStatus("current")


class _AttackTypeIndex_Type(Integer32):
    """Custom type attackTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AttackTypeIndex_Type.__name__ = "Integer32"
_AttackTypeIndex_Object = MibTableColumn
attackTypeIndex = _AttackTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 15, 1, 1, 1),
    _AttackTypeIndex_Type()
)
attackTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attackTypeIndex.setStatus("current")
_AttackTypeName_Type = SnmpAdminString
_AttackTypeName_Object = MibTableColumn
attackTypeName = _AttackTypeName_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 15, 1, 1, 2),
    _AttackTypeName_Type()
)
attackTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attackTypeName.setStatus("current")


class _AttackTypeCurrentNumAttacks_Type(Unsigned32):
    """Custom type attackTypeCurrentNumAttacks based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AttackTypeCurrentNumAttacks_Type.__name__ = "Unsigned32"
_AttackTypeCurrentNumAttacks_Object = MibTableColumn
attackTypeCurrentNumAttacks = _AttackTypeCurrentNumAttacks_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 15, 1, 1, 3),
    _AttackTypeCurrentNumAttacks_Type()
)
attackTypeCurrentNumAttacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attackTypeCurrentNumAttacks.setStatus("current")


class _AttackTypeTotalNumAttacks_Type(Unsigned32):
    """Custom type attackTypeTotalNumAttacks based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AttackTypeTotalNumAttacks_Type.__name__ = "Unsigned32"
_AttackTypeTotalNumAttacks_Object = MibTableColumn
attackTypeTotalNumAttacks = _AttackTypeTotalNumAttacks_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 15, 1, 1, 4),
    _AttackTypeTotalNumAttacks_Type()
)
attackTypeTotalNumAttacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attackTypeTotalNumAttacks.setStatus("current")
_AttackTypeTotalNumFlows_Type = Counter64
_AttackTypeTotalNumFlows_Object = MibTableColumn
attackTypeTotalNumFlows = _AttackTypeTotalNumFlows_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 15, 1, 1, 5),
    _AttackTypeTotalNumFlows_Type()
)
attackTypeTotalNumFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attackTypeTotalNumFlows.setStatus("current")


class _AttackTypeTotalNumSeconds_Type(Unsigned32):
    """Custom type attackTypeTotalNumSeconds based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AttackTypeTotalNumSeconds_Type.__name__ = "Unsigned32"
_AttackTypeTotalNumSeconds_Object = MibTableColumn
attackTypeTotalNumSeconds = _AttackTypeTotalNumSeconds_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 15, 1, 1, 6),
    _AttackTypeTotalNumSeconds_Type()
)
attackTypeTotalNumSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attackTypeTotalNumSeconds.setStatus("current")
if mibBuilder.loadTexts:
    attackTypeTotalNumSeconds.setUnits("Seconds")
_VasTrafficForwardingGrp_ObjectIdentity = ObjectIdentity
vasTrafficForwardingGrp = _VasTrafficForwardingGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 16)
)
_VasServerTable_Object = MibTable
vasServerTable = _VasServerTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 16, 1)
)
if mibBuilder.loadTexts:
    vasServerTable.setStatus("current")
_VasServerEntry_Object = MibTableRow
vasServerEntry = _VasServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 16, 1, 1)
)
vasServerEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "pmoduleIndex"),
    (0, "PCUBE-SE-MIB", "vasServerIndex"),
)
if mibBuilder.loadTexts:
    vasServerEntry.setStatus("current")


class _VasServerIndex_Type(Integer32):
    """Custom type vasServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VasServerIndex_Type.__name__ = "Integer32"
_VasServerIndex_Object = MibTableColumn
vasServerIndex = _VasServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 16, 1, 1, 1),
    _VasServerIndex_Type()
)
vasServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasServerIndex.setStatus("current")


class _VasServerId_Type(Integer32):
    """Custom type vasServerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VasServerId_Type.__name__ = "Integer32"
_VasServerId_Object = MibTableColumn
vasServerId = _VasServerId_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 16, 1, 1, 2),
    _VasServerId_Type()
)
vasServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasServerId.setStatus("current")


class _VasServerAdminStatus_Type(Integer32):
    """Custom type vasServerAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("other", 1),
          ("up", 2))
    )


_VasServerAdminStatus_Type.__name__ = "Integer32"
_VasServerAdminStatus_Object = MibTableColumn
vasServerAdminStatus = _VasServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 16, 1, 1, 3),
    _VasServerAdminStatus_Type()
)
vasServerAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasServerAdminStatus.setStatus("current")


class _VasServerOperStatus_Type(Integer32):
    """Custom type vasServerOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("other", 1),
          ("up", 2))
    )


_VasServerOperStatus_Type.__name__ = "Integer32"
_VasServerOperStatus_Object = MibTableColumn
vasServerOperStatus = _VasServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 16, 1, 1, 4),
    _VasServerOperStatus_Type()
)
vasServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasServerOperStatus.setStatus("current")
_MplsVpnAutoLearnGrp_ObjectIdentity = ObjectIdentity
mplsVpnAutoLearnGrp = _MplsVpnAutoLearnGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 17)
)
_MplsVpnSoftwareCountersTable_Object = MibTable
mplsVpnSoftwareCountersTable = _MplsVpnSoftwareCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 17, 1)
)
if mibBuilder.loadTexts:
    mplsVpnSoftwareCountersTable.setStatus("current")
_MplsVpnSoftwareCountersEntry_Object = MibTableRow
mplsVpnSoftwareCountersEntry = _MplsVpnSoftwareCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 17, 1, 1)
)
mplsVpnSoftwareCountersEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "pmoduleIndex"),
)
if mibBuilder.loadTexts:
    mplsVpnSoftwareCountersEntry.setStatus("current")


class _MplsVpnMaxHWMappings_Type(Integer32):
    """Custom type mplsVpnMaxHWMappings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_MplsVpnMaxHWMappings_Type.__name__ = "Integer32"
_MplsVpnMaxHWMappings_Object = MibTableColumn
mplsVpnMaxHWMappings = _MplsVpnMaxHWMappings_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 17, 1, 1, 1),
    _MplsVpnMaxHWMappings_Type()
)
mplsVpnMaxHWMappings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnMaxHWMappings.setStatus("current")


class _MplsVpnCurrentHWMappings_Type(Integer32):
    """Custom type mplsVpnCurrentHWMappings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_MplsVpnCurrentHWMappings_Type.__name__ = "Integer32"
_MplsVpnCurrentHWMappings_Object = MibTableColumn
mplsVpnCurrentHWMappings = _MplsVpnCurrentHWMappings_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 1, 17, 1, 1, 2),
    _MplsVpnCurrentHWMappings_Type()
)
mplsVpnCurrentHWMappings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnCurrentHWMappings.setStatus("current")

# Managed Objects groups

pcubeSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5655, 2, 3, 1, 1, 1)
)
pcubeSystemGroup.setObjects(
      *(("PCUBE-SE-MIB", "sysOperationalStatus"),
        ("PCUBE-SE-MIB", "sysFailureRecovery"),
        ("PCUBE-SE-MIB", "sysVersion"))
)
if mibBuilder.loadTexts:
    pcubeSystemGroup.setStatus("current")

pcubeChassisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5655, 2, 3, 1, 1, 2)
)
pcubeChassisGroup.setObjects(
      *(("PCUBE-SE-MIB", "pchassisSysType"),
        ("PCUBE-SE-MIB", "pchassisPowerSupplyAlarm"),
        ("PCUBE-SE-MIB", "pchassisFansAlarm"),
        ("PCUBE-SE-MIB", "pchassisTempAlarm"),
        ("PCUBE-SE-MIB", "pchassisVoltageAlarm"),
        ("PCUBE-SE-MIB", "pchassisNumSlots"),
        ("PCUBE-SE-MIB", "pchassisSlotConfig"),
        ("PCUBE-SE-MIB", "pchassisPsuType"),
        ("PCUBE-SE-MIB", "pchassisLineFeedAlarm"))
)
if mibBuilder.loadTexts:
    pcubeChassisGroup.setStatus("current")

pcuebModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5655, 2, 3, 1, 1, 3)
)
pcuebModuleGroup.setObjects(
      *(("PCUBE-SE-MIB", "pmoduleIndex"),
        ("PCUBE-SE-MIB", "pmoduleType"),
        ("PCUBE-SE-MIB", "pmoduleNumTrafficProcessors"),
        ("PCUBE-SE-MIB", "pmoduleSlotNum"),
        ("PCUBE-SE-MIB", "pmoduleHwVersion"),
        ("PCUBE-SE-MIB", "pmoduleNumPorts"),
        ("PCUBE-SE-MIB", "pmoduleNumLinks"),
        ("PCUBE-SE-MIB", "pmoduleConnectionMode"),
        ("PCUBE-SE-MIB", "pmoduleSerialNumber"),
        ("PCUBE-SE-MIB", "pmoduleUpStreamAttackFilteringTime"),
        ("PCUBE-SE-MIB", "pmoduleUpStreamLastAttackFilteringTime"),
        ("PCUBE-SE-MIB", "pmoduleDownStreamAttackFilteringTime"),
        ("PCUBE-SE-MIB", "pmoduleDownStreamLastAttackFilteringTime"),
        ("PCUBE-SE-MIB", "pmoduleAttackObjectsClearTime"),
        ("PCUBE-SE-MIB", "pmoduleAdminStatus"),
        ("PCUBE-SE-MIB", "pmoduleOperStatus"))
)
if mibBuilder.loadTexts:
    pcuebModuleGroup.setStatus("current")

pcubeLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5655, 2, 3, 1, 1, 4)
)
pcubeLinkGroup.setObjects(
      *(("PCUBE-SE-MIB", "linkModuleIndex"),
        ("PCUBE-SE-MIB", "linkIndex"),
        ("PCUBE-SE-MIB", "linkAdminModeOnActive"),
        ("PCUBE-SE-MIB", "linkAdminModeOnFailure"),
        ("PCUBE-SE-MIB", "linkOperMode"),
        ("PCUBE-SE-MIB", "linkStatusReflectionEnable"),
        ("PCUBE-SE-MIB", "linkSubscriberSidePortIndex"),
        ("PCUBE-SE-MIB", "linkNetworkSidePortIndex"))
)
if mibBuilder.loadTexts:
    pcubeLinkGroup.setStatus("current")

pcubeDiskGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5655, 2, 3, 1, 1, 5)
)
pcubeDiskGroup.setObjects(
      *(("PCUBE-SE-MIB", "diskNumUsedBytes"),
        ("PCUBE-SE-MIB", "diskNumFreeBytes"))
)
if mibBuilder.loadTexts:
    pcubeDiskGroup.setStatus("current")

pcubeRdrFormatterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5655, 2, 3, 1, 1, 6)
)
pcubeRdrFormatterGroup.setObjects(
      *(("PCUBE-SE-MIB", "rdrFormatterEnable"),
        ("PCUBE-SE-MIB", "rdrFormatterDestIPAddr"),
        ("PCUBE-SE-MIB", "rdrFormatterDestPort"),
        ("PCUBE-SE-MIB", "rdrFormatterDestPriority"),
        ("PCUBE-SE-MIB", "rdrFormatterDestStatus"),
        ("PCUBE-SE-MIB", "rdrFormatterDestConnectionStatus"),
        ("PCUBE-SE-MIB", "rdrFormatterDestNumReportsSent"),
        ("PCUBE-SE-MIB", "rdrFormatterDestNumReportsDiscarded"),
        ("PCUBE-SE-MIB", "rdrFormatterDestReportRate"),
        ("PCUBE-SE-MIB", "rdrFormatterDestReportRatePeak"),
        ("PCUBE-SE-MIB", "rdrFormatterDestReportRatePeakTime"),
        ("PCUBE-SE-MIB", "rdrFormatterNumReportsSent"),
        ("PCUBE-SE-MIB", "rdrFormatterNumReportsDiscarded"),
        ("PCUBE-SE-MIB", "rdrFormatterClearCountersTime"),
        ("PCUBE-SE-MIB", "rdrFormatterReportRate"),
        ("PCUBE-SE-MIB", "rdrFormatterReportRatePeak"),
        ("PCUBE-SE-MIB", "rdrFormatterReportRatePeakTime"),
        ("PCUBE-SE-MIB", "rdrFormatterProtocol"),
        ("PCUBE-SE-MIB", "rdrFormatterForwardingMode"),
        ("PCUBE-SE-MIB", "rdrFormatterCategoryDestPriority"),
        ("PCUBE-SE-MIB", "rdrFormatterCategoryDestStatus"),
        ("PCUBE-SE-MIB", "rdrFormatterCategoryIndex"),
        ("PCUBE-SE-MIB", "rdrFormatterCategoryName"),
        ("PCUBE-SE-MIB", "rdrFormatterCategoryNumReportsSent"),
        ("PCUBE-SE-MIB", "rdrFormatterCategoryNumReportsDiscarded"),
        ("PCUBE-SE-MIB", "rdrFormatterCategoryReportRate"),
        ("PCUBE-SE-MIB", "rdrFormatterCategoryReportRatePeak"),
        ("PCUBE-SE-MIB", "rdrFormatterCategoryReportRatePeakTime"),
        ("PCUBE-SE-MIB", "rdrFormatterCategoryNumReportsQueued"))
)
if mibBuilder.loadTexts:
    pcubeRdrFormatterGroup.setStatus("current")

pcubeLoggerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5655, 2, 3, 1, 1, 7)
)
pcubeLoggerGroup.setObjects(
      *(("PCUBE-SE-MIB", "loggerUserLogEnable"),
        ("PCUBE-SE-MIB", "loggerUserLogNumInfo"),
        ("PCUBE-SE-MIB", "loggerUserLogNumWarning"),
        ("PCUBE-SE-MIB", "loggerUserLogNumError"),
        ("PCUBE-SE-MIB", "loggerUserLogNumFatal"),
        ("PCUBE-SE-MIB", "loggerUserLogClearCountersTime"))
)
if mibBuilder.loadTexts:
    pcubeLoggerGroup.setStatus("current")

pcubeSubscribersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5655, 2, 3, 1, 1, 8)
)
pcubeSubscribersGroup.setObjects(
      *(("PCUBE-SE-MIB", "subscribersNumIntroduced"),
        ("PCUBE-SE-MIB", "subscribersNumFree"),
        ("PCUBE-SE-MIB", "subscribersNumIpAddrMappings"),
        ("PCUBE-SE-MIB", "subscribersNumIpAddrMappingsFree"),
        ("PCUBE-SE-MIB", "subscribersNumIpRangeMappings"),
        ("PCUBE-SE-MIB", "subscribersNumIpRangeMappingsFree"),
        ("PCUBE-SE-MIB", "subscribersNumVlanMappings"),
        ("PCUBE-SE-MIB", "subscribersNumVlanMappingsFree"),
        ("PCUBE-SE-MIB", "subscribersNumActive"),
        ("PCUBE-SE-MIB", "subscribersNumActivePeak"),
        ("PCUBE-SE-MIB", "subscribersNumActivePeakTime"),
        ("PCUBE-SE-MIB", "subscribersNumUpdates"),
        ("PCUBE-SE-MIB", "subscribersCountersClearTime"),
        ("PCUBE-SE-MIB", "subscribersNumTpIpRanges"),
        ("PCUBE-SE-MIB", "subscribersNumTpIpRangesFree"),
        ("PCUBE-SE-MIB", "subscribersNumAnonymous"),
        ("PCUBE-SE-MIB", "subscribersNumWithSessions"),
        ("PCUBE-SE-MIB", "spIndex"),
        ("PCUBE-SE-MIB", "spName"),
        ("PCUBE-SE-MIB", "spType"),
        ("PCUBE-SE-MIB", "spvSubName"),
        ("PCUBE-SE-MIB", "spvPropertyName"),
        ("PCUBE-SE-MIB", "spvRowStatus"),
        ("PCUBE-SE-MIB", "spvPropertyStringValue"),
        ("PCUBE-SE-MIB", "spvPropertyUintValue"),
        ("PCUBE-SE-MIB", "spvPropertyCounter64Value"))
)
if mibBuilder.loadTexts:
    pcubeSubscribersGroup.setStatus("current")

pcubeTrafficProcessorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5655, 2, 3, 1, 1, 9)
)
pcubeTrafficProcessorGroup.setObjects(
      *(("PCUBE-SE-MIB", "tpModuleIndex"),
        ("PCUBE-SE-MIB", "tpIndex"),
        ("PCUBE-SE-MIB", "tpTotalNumHandledPackets"),
        ("PCUBE-SE-MIB", "tpTotalNumHandledFlows"),
        ("PCUBE-SE-MIB", "tpNumActiveFlows"),
        ("PCUBE-SE-MIB", "tpNumActiveFlowsPeak"),
        ("PCUBE-SE-MIB", "tpNumActiveFlowsPeakTime"),
        ("PCUBE-SE-MIB", "tpNumTcpActiveFlows"),
        ("PCUBE-SE-MIB", "tpNumTcpActiveFlowsPeak"),
        ("PCUBE-SE-MIB", "tpNumTcpActiveFlowsPeakTime"),
        ("PCUBE-SE-MIB", "tpNumUdpActiveFlows"),
        ("PCUBE-SE-MIB", "tpNumUdpActiveFlowsPeak"),
        ("PCUBE-SE-MIB", "tpNumUdpActiveFlowsPeakTime"),
        ("PCUBE-SE-MIB", "tpNumNonTcpUdpActiveFlows"),
        ("PCUBE-SE-MIB", "tpNumNonTcpUdpActiveFlowsPeak"),
        ("PCUBE-SE-MIB", "tpNumNonTcpUdpActiveFlowsPeakTime"),
        ("PCUBE-SE-MIB", "tpTotalNumBlockedPackets"),
        ("PCUBE-SE-MIB", "tpTotalNumBlockedFlows"),
        ("PCUBE-SE-MIB", "tpTotalNumDiscardedPacketsDueToBwLimit"),
        ("PCUBE-SE-MIB", "tpTotalNumWredDiscardedPackets"),
        ("PCUBE-SE-MIB", "tpTotalNumFragments"),
        ("PCUBE-SE-MIB", "tpTotalNumNonIpPackets"),
        ("PCUBE-SE-MIB", "tpTotalNumIpCrcErrPackets"),
        ("PCUBE-SE-MIB", "tpTotalNumIpLengthErrPackets"),
        ("PCUBE-SE-MIB", "tpTotalNumIpBroadcastPackets"),
        ("PCUBE-SE-MIB", "tpTotalNumTtlErrPackets"),
        ("PCUBE-SE-MIB", "tpTotalNumTcpUdpCrcErrPackets"),
        ("PCUBE-SE-MIB", "tpClearCountersTime"),
        ("PCUBE-SE-MIB", "tpHandledPacketsRate"),
        ("PCUBE-SE-MIB", "tpHandledPacketsRatePeak"),
        ("PCUBE-SE-MIB", "tpHandledPacketsRatePeakTime"),
        ("PCUBE-SE-MIB", "tpHandledFlowsRate"),
        ("PCUBE-SE-MIB", "tpHandledFlowsRatePeak"),
        ("PCUBE-SE-MIB", "tpHandledFlowsRatePeakTime"),
        ("PCUBE-SE-MIB", "tpCpuUtilization"),
        ("PCUBE-SE-MIB", "tpCpuUtilizationPeak"),
        ("PCUBE-SE-MIB", "tpCpuUtilizationPeakTime"),
        ("PCUBE-SE-MIB", "tpFlowsCapacityUtilization"),
        ("PCUBE-SE-MIB", "tpFlowsCapacityUtilizationPeak"),
        ("PCUBE-SE-MIB", "tpFlowsCapacityUtilizationPeakTime"),
        ("PCUBE-SE-MIB", "tpServiceLoss"))
)
if mibBuilder.loadTexts:
    pcubeTrafficProcessorGroup.setStatus("current")

pcubePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5655, 2, 3, 1, 1, 10)
)
pcubePortGroup.setObjects(
      *(("PCUBE-SE-MIB", "pportModuleIndex"),
        ("PCUBE-SE-MIB", "pportIndex"),
        ("PCUBE-SE-MIB", "pportType"),
        ("PCUBE-SE-MIB", "pportNumTxQueues"),
        ("PCUBE-SE-MIB", "pportIfIndex"),
        ("PCUBE-SE-MIB", "pportAdminSpeed"),
        ("PCUBE-SE-MIB", "pportAdminDuplex"),
        ("PCUBE-SE-MIB", "pportOperDuplex"),
        ("PCUBE-SE-MIB", "pportLinkIndex"),
        ("PCUBE-SE-MIB", "pportOperStatus"))
)
if mibBuilder.loadTexts:
    pcubePortGroup.setStatus("current")

pcubeTxQueuesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5655, 2, 3, 1, 1, 11)
)
pcubeTxQueuesGroup.setObjects(
      *(("PCUBE-SE-MIB", "txQueuesModuleIndex"),
        ("PCUBE-SE-MIB", "txQueuesPortIndex"),
        ("PCUBE-SE-MIB", "txQueuesQueueIndex"),
        ("PCUBE-SE-MIB", "txQueuesDescription"),
        ("PCUBE-SE-MIB", "txQueuesBandwidth"),
        ("PCUBE-SE-MIB", "txQueuesUtilization"),
        ("PCUBE-SE-MIB", "txQueuesUtilizationPeak"),
        ("PCUBE-SE-MIB", "txQueuesUtilizationPeakTime"),
        ("PCUBE-SE-MIB", "txQueuesClearCountersTime"),
        ("PCUBE-SE-MIB", "txQueuesDroppedBytes"))
)
if mibBuilder.loadTexts:
    pcubeTxQueuesGroup.setStatus("current")

pcubeGlobalControllersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5655, 2, 3, 1, 1, 12)
)
pcubeGlobalControllersGroup.setObjects(
      *(("PCUBE-SE-MIB", "globalControllersModuleIndex"),
        ("PCUBE-SE-MIB", "globalControllersPortIndex"),
        ("PCUBE-SE-MIB", "globalControllersIndex"),
        ("PCUBE-SE-MIB", "globalControllersDescription"),
        ("PCUBE-SE-MIB", "globalControllersBandwidth"),
        ("PCUBE-SE-MIB", "globalControllersUtilization"),
        ("PCUBE-SE-MIB", "globalControllersUtilizationPeak"),
        ("PCUBE-SE-MIB", "globalControllersUtilizationPeakTime"),
        ("PCUBE-SE-MIB", "globalControllersClearCountersTime"),
        ("PCUBE-SE-MIB", "globalControllersDroppedBytes"))
)
if mibBuilder.loadTexts:
    pcubeGlobalControllersGroup.setStatus("current")

pcubeApplicationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5655, 2, 3, 1, 1, 13)
)
pcubeApplicationGroup.setObjects(
      *(("PCUBE-SE-MIB", "appName"),
        ("PCUBE-SE-MIB", "appDescription"),
        ("PCUBE-SE-MIB", "appVersion"),
        ("PCUBE-SE-MIB", "apIndex"),
        ("PCUBE-SE-MIB", "apName"),
        ("PCUBE-SE-MIB", "apType"),
        ("PCUBE-SE-MIB", "apvPropertyName"),
        ("PCUBE-SE-MIB", "apvRowStatus"),
        ("PCUBE-SE-MIB", "apvPropertyStringValue"),
        ("PCUBE-SE-MIB", "apvPropertyUintValue"),
        ("PCUBE-SE-MIB", "apvPropertyCounter64Value"))
)
if mibBuilder.loadTexts:
    pcubeApplicationGroup.setStatus("current")

pcubeTrafficCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5655, 2, 3, 1, 1, 14)
)
pcubeTrafficCountersGroup.setObjects(
      *(("PCUBE-SE-MIB", "trafficCounterIndex"),
        ("PCUBE-SE-MIB", "trafficCounterValue"),
        ("PCUBE-SE-MIB", "trafficCounterName"),
        ("PCUBE-SE-MIB", "trafficCounterType"))
)
if mibBuilder.loadTexts:
    pcubeTrafficCountersGroup.setStatus("current")

pcubeAttackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5655, 2, 3, 1, 1, 15)
)
pcubeAttackGroup.setObjects(
      *(("PCUBE-SE-MIB", "attackTypeIndex"),
        ("PCUBE-SE-MIB", "attackTypeName"),
        ("PCUBE-SE-MIB", "attackTypeCurrentNumAttacks"),
        ("PCUBE-SE-MIB", "attackTypeTotalNumAttacks"),
        ("PCUBE-SE-MIB", "attackTypeTotalNumFlows"),
        ("PCUBE-SE-MIB", "attackTypeTotalNumSeconds"))
)
if mibBuilder.loadTexts:
    pcubeAttackGroup.setStatus("current")

pcubeVasTrafficForwardingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5655, 2, 3, 1, 1, 16)
)
pcubeVasTrafficForwardingGroup.setObjects(
      *(("PCUBE-SE-MIB", "vasServerIndex"),
        ("PCUBE-SE-MIB", "vasServerId"),
        ("PCUBE-SE-MIB", "vasServerAdminStatus"),
        ("PCUBE-SE-MIB", "vasServerOperStatus"))
)
if mibBuilder.loadTexts:
    pcubeVasTrafficForwardingGroup.setStatus("current")

pcubeMplsVpnAutoLearnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5655, 2, 3, 1, 1, 17)
)
pcubeMplsVpnAutoLearnGroup.setObjects(
      *(("PCUBE-SE-MIB", "mplsVpnMaxHWMappings"),
        ("PCUBE-SE-MIB", "mplsVpnCurrentHWMappings"))
)
if mibBuilder.loadTexts:
    pcubeMplsVpnAutoLearnGroup.setStatus("current")

pcubeTrapObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5655, 2, 3, 1, 1, 18)
)
pcubeTrapObjectsGroup.setObjects(
      *(("PCUBE-SE-MIB", "pcubeSeEventGenericString1"),
        ("PCUBE-SE-MIB", "pcubeSeEventGenericString2"),
        ("PCUBE-SE-MIB", "pullRequestNumber"))
)
if mibBuilder.loadTexts:
    pcubeTrapObjectsGroup.setStatus("current")


# Notification objects

operationalStatusOperationalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 1)
)
operationalStatusOperationalTrap.setObjects(
    ("PCUBE-SE-MIB", "sysOperationalStatus")
)
if mibBuilder.loadTexts:
    operationalStatusOperationalTrap.setStatus(
        "current"
    )

operationalStatusWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 2)
)
operationalStatusWarningTrap.setObjects(
    ("PCUBE-SE-MIB", "sysOperationalStatus")
)
if mibBuilder.loadTexts:
    operationalStatusWarningTrap.setStatus(
        "current"
    )

operationalStatusFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 3)
)
operationalStatusFailureTrap.setObjects(
    ("PCUBE-SE-MIB", "sysOperationalStatus")
)
if mibBuilder.loadTexts:
    operationalStatusFailureTrap.setStatus(
        "current"
    )

systemResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 4)
)
if mibBuilder.loadTexts:
    systemResetTrap.setStatus(
        "current"
    )

chassisTempAlarmOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 5)
)
chassisTempAlarmOnTrap.setObjects(
    ("PCUBE-SE-MIB", "pchassisTempAlarm")
)
if mibBuilder.loadTexts:
    chassisTempAlarmOnTrap.setStatus(
        "current"
    )

chassisTempAlarmOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 6)
)
chassisTempAlarmOffTrap.setObjects(
    ("PCUBE-SE-MIB", "pchassisTempAlarm")
)
if mibBuilder.loadTexts:
    chassisTempAlarmOffTrap.setStatus(
        "current"
    )

chassisVoltageAlarmOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 7)
)
chassisVoltageAlarmOnTrap.setObjects(
    ("PCUBE-SE-MIB", "pchassisVoltageAlarm")
)
if mibBuilder.loadTexts:
    chassisVoltageAlarmOnTrap.setStatus(
        "current"
    )

chassisFansAlarmOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 8)
)
chassisFansAlarmOnTrap.setObjects(
    ("PCUBE-SE-MIB", "pchassisFansAlarm")
)
if mibBuilder.loadTexts:
    chassisFansAlarmOnTrap.setStatus(
        "current"
    )

chassisPowerSupplyAlarmOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 9)
)
chassisPowerSupplyAlarmOnTrap.setObjects(
    ("PCUBE-SE-MIB", "pchassisPowerSupplyAlarm")
)
if mibBuilder.loadTexts:
    chassisPowerSupplyAlarmOnTrap.setStatus(
        "current"
    )

rdrActiveConnectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 10)
)
rdrActiveConnectionTrap.setObjects(
      *(("PCUBE-SE-MIB", "rdrFormatterDestIPAddr"),
        ("PCUBE-SE-MIB", "rdrFormatterDestStatus"))
)
if mibBuilder.loadTexts:
    rdrActiveConnectionTrap.setStatus(
        "current"
    )

rdrNoActiveConnectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 11)
)
if mibBuilder.loadTexts:
    rdrNoActiveConnectionTrap.setStatus(
        "current"
    )

rdrConnectionUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 12)
)
rdrConnectionUpTrap.setObjects(
      *(("PCUBE-SE-MIB", "rdrFormatterDestIPAddr"),
        ("PCUBE-SE-MIB", "rdrFormatterDestConnectionStatus"))
)
if mibBuilder.loadTexts:
    rdrConnectionUpTrap.setStatus(
        "current"
    )

rdrConnectionDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 13)
)
rdrConnectionDownTrap.setObjects(
      *(("PCUBE-SE-MIB", "rdrFormatterDestIPAddr"),
        ("PCUBE-SE-MIB", "rdrFormatterDestConnectionStatus"))
)
if mibBuilder.loadTexts:
    rdrConnectionDownTrap.setStatus(
        "current"
    )

telnetSessionStartedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 14)
)
if mibBuilder.loadTexts:
    telnetSessionStartedTrap.setStatus(
        "deprecated"
    )

telnetSessionEndedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 15)
)
if mibBuilder.loadTexts:
    telnetSessionEndedTrap.setStatus(
        "deprecated"
    )

telnetSessionDeniedAccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 16)
)
if mibBuilder.loadTexts:
    telnetSessionDeniedAccessTrap.setStatus(
        "deprecated"
    )

telnetSessionBadLoginTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 17)
)
if mibBuilder.loadTexts:
    telnetSessionBadLoginTrap.setStatus(
        "deprecated"
    )

loggerUserLogIsFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 18)
)
if mibBuilder.loadTexts:
    loggerUserLogIsFullTrap.setStatus(
        "current"
    )

sntpClockDriftWarnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 19)
)
if mibBuilder.loadTexts:
    sntpClockDriftWarnTrap.setStatus(
        "current"
    )

linkModeBypassTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 20)
)
linkModeBypassTrap.setObjects(
    ("PCUBE-SE-MIB", "linkOperMode")
)
if mibBuilder.loadTexts:
    linkModeBypassTrap.setStatus(
        "current"
    )

linkModeForwardingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 21)
)
linkModeForwardingTrap.setObjects(
    ("PCUBE-SE-MIB", "linkOperMode")
)
if mibBuilder.loadTexts:
    linkModeForwardingTrap.setStatus(
        "current"
    )

linkModeCutoffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 22)
)
linkModeCutoffTrap.setObjects(
    ("PCUBE-SE-MIB", "linkOperMode")
)
if mibBuilder.loadTexts:
    linkModeCutoffTrap.setStatus(
        "current"
    )

moduleAttackFilterActivatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 25)
)
moduleAttackFilterActivatedTrap.setObjects(
      *(("PCUBE-SE-MIB", "pmoduleIndex"),
        ("PCUBE-SE-MIB", "pcubeSeEventGenericString1"))
)
if mibBuilder.loadTexts:
    moduleAttackFilterActivatedTrap.setStatus(
        "current"
    )

moduleAttackFilterDeactivatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 26)
)
moduleAttackFilterDeactivatedTrap.setObjects(
      *(("PCUBE-SE-MIB", "pmoduleIndex"),
        ("PCUBE-SE-MIB", "pcubeSeEventGenericString1"),
        ("PCUBE-SE-MIB", "pcubeSeEventGenericString2"))
)
if mibBuilder.loadTexts:
    moduleAttackFilterDeactivatedTrap.setStatus(
        "current"
    )

moduleEmAgentGenericTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 27)
)
moduleEmAgentGenericTrap.setObjects(
      *(("PCUBE-SE-MIB", "pmoduleIndex"),
        ("PCUBE-SE-MIB", "pcubeSeEventGenericString1"),
        ("PCUBE-SE-MIB", "pcubeSeEventGenericString2"))
)
if mibBuilder.loadTexts:
    moduleEmAgentGenericTrap.setStatus(
        "current"
    )

linkModeSniffingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 28)
)
linkModeSniffingTrap.setObjects(
    ("PCUBE-SE-MIB", "linkOperMode")
)
if mibBuilder.loadTexts:
    linkModeSniffingTrap.setStatus(
        "current"
    )

moduleRedundancyReadyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 29)
)
moduleRedundancyReadyTrap.setObjects(
      *(("PCUBE-SE-MIB", "pmoduleIndex"),
        ("PCUBE-SE-MIB", "pmoduleOperStatus"))
)
if mibBuilder.loadTexts:
    moduleRedundancyReadyTrap.setStatus(
        "current"
    )

moduleRedundantConfigurationMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 30)
)
moduleRedundantConfigurationMismatchTrap.setObjects(
    ("PCUBE-SE-MIB", "pmoduleIndex")
)
if mibBuilder.loadTexts:
    moduleRedundantConfigurationMismatchTrap.setStatus(
        "current"
    )

moduleLostRedundancyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 31)
)
moduleLostRedundancyTrap.setObjects(
      *(("PCUBE-SE-MIB", "pmoduleIndex"),
        ("PCUBE-SE-MIB", "pmoduleOperStatus"))
)
if mibBuilder.loadTexts:
    moduleLostRedundancyTrap.setStatus(
        "current"
    )

moduleSmConnectionDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 32)
)
moduleSmConnectionDownTrap.setObjects(
    ("PCUBE-SE-MIB", "pmoduleIndex")
)
if mibBuilder.loadTexts:
    moduleSmConnectionDownTrap.setStatus(
        "current"
    )

moduleSmConnectionUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 33)
)
moduleSmConnectionUpTrap.setObjects(
    ("PCUBE-SE-MIB", "pmoduleIndex")
)
if mibBuilder.loadTexts:
    moduleSmConnectionUpTrap.setStatus(
        "current"
    )

moduleOperStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 34)
)
moduleOperStatusChangeTrap.setObjects(
      *(("PCUBE-SE-MIB", "pmoduleIndex"),
        ("PCUBE-SE-MIB", "pmoduleOperStatus"))
)
if mibBuilder.loadTexts:
    moduleOperStatusChangeTrap.setStatus(
        "current"
    )

portOperStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 35)
)
portOperStatusChangeTrap.setObjects(
      *(("PCUBE-SE-MIB", "pmoduleIndex"),
        ("PCUBE-SE-MIB", "pportIndex"),
        ("PCUBE-SE-MIB", "pportOperStatus"))
)
if mibBuilder.loadTexts:
    portOperStatusChangeTrap.setStatus(
        "current"
    )

chassisLineFeedAlarmOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 36)
)
chassisLineFeedAlarmOnTrap.setObjects(
    ("PCUBE-SE-MIB", "pchassisLineFeedAlarm")
)
if mibBuilder.loadTexts:
    chassisLineFeedAlarmOnTrap.setStatus(
        "current"
    )

rdrFormatterCategoryDiscardingReportsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 37)
)
rdrFormatterCategoryDiscardingReportsTrap.setObjects(
    ("PCUBE-SE-MIB", "rdrFormatterCategoryIndex")
)
if mibBuilder.loadTexts:
    rdrFormatterCategoryDiscardingReportsTrap.setStatus(
        "current"
    )

rdrFormatterCategoryStoppedDiscardingReportsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 38)
)
rdrFormatterCategoryStoppedDiscardingReportsTrap.setObjects(
    ("PCUBE-SE-MIB", "rdrFormatterCategoryIndex")
)
if mibBuilder.loadTexts:
    rdrFormatterCategoryStoppedDiscardingReportsTrap.setStatus(
        "current"
    )

sessionStartedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 39)
)
sessionStartedTrap.setObjects(
    ("PCUBE-SE-MIB", "pcubeSeEventGenericString1")
)
if mibBuilder.loadTexts:
    sessionStartedTrap.setStatus(
        "current"
    )

sessionEndedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 40)
)
sessionEndedTrap.setObjects(
    ("PCUBE-SE-MIB", "pcubeSeEventGenericString1")
)
if mibBuilder.loadTexts:
    sessionEndedTrap.setStatus(
        "current"
    )

sessionDeniedAccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 41)
)
if mibBuilder.loadTexts:
    sessionDeniedAccessTrap.setStatus(
        "current"
    )

sessionBadLoginTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 42)
)
if mibBuilder.loadTexts:
    sessionBadLoginTrap.setStatus(
        "current"
    )

illegalSubscriberMappingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 43)
)
illegalSubscriberMappingTrap.setObjects(
      *(("PCUBE-SE-MIB", "pmoduleIndex"),
        ("PCUBE-SE-MIB", "pcubeSeEventGenericString1"))
)
if mibBuilder.loadTexts:
    illegalSubscriberMappingTrap.setStatus(
        "current"
    )

loggerLineAttackLogFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 44)
)
if mibBuilder.loadTexts:
    loggerLineAttackLogFullTrap.setStatus(
        "current"
    )

vasServerOpertionalStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 45)
)
vasServerOpertionalStatusChangeTrap.setObjects(
      *(("PCUBE-SE-MIB", "pmoduleIndex"),
        ("PCUBE-SE-MIB", "vasServerIndex"),
        ("PCUBE-SE-MIB", "vasServerId"),
        ("PCUBE-SE-MIB", "vasServerOperStatus"))
)
if mibBuilder.loadTexts:
    vasServerOpertionalStatusChangeTrap.setStatus(
        "current"
    )

pullRequestRetryFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 47)
)
pullRequestRetryFailedTrap.setObjects(
      *(("PCUBE-SE-MIB", "pcubeSeEventGenericString1"),
        ("PCUBE-SE-MIB", "pullRequestNumber"))
)
if mibBuilder.loadTexts:
    pullRequestRetryFailedTrap.setStatus(
        "current"
    )

mplsVpnTotalHWMappingsThresholdExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5655, 4, 0, 48)
)
mplsVpnTotalHWMappingsThresholdExceededTrap.setObjects(
    ("PCUBE-SE-MIB", "mplsVpnCurrentHWMappings")
)
if mibBuilder.loadTexts:
    mplsVpnTotalHWMappingsThresholdExceededTrap.setStatus(
        "current"
    )


# Notifications groups

pcubeSeEventsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5655, 2, 3, 1, 3)
)
pcubeSeEventsGroup.setObjects(
      *(("PCUBE-SE-MIB", "operationalStatusOperationalTrap"),
        ("PCUBE-SE-MIB", "operationalStatusWarningTrap"),
        ("PCUBE-SE-MIB", "operationalStatusFailureTrap"),
        ("PCUBE-SE-MIB", "systemResetTrap"),
        ("PCUBE-SE-MIB", "chassisTempAlarmOnTrap"),
        ("PCUBE-SE-MIB", "chassisTempAlarmOffTrap"),
        ("PCUBE-SE-MIB", "chassisVoltageAlarmOnTrap"),
        ("PCUBE-SE-MIB", "chassisFansAlarmOnTrap"),
        ("PCUBE-SE-MIB", "chassisPowerSupplyAlarmOnTrap"),
        ("PCUBE-SE-MIB", "rdrActiveConnectionTrap"),
        ("PCUBE-SE-MIB", "rdrNoActiveConnectionTrap"),
        ("PCUBE-SE-MIB", "rdrConnectionUpTrap"),
        ("PCUBE-SE-MIB", "rdrConnectionDownTrap"),
        ("PCUBE-SE-MIB", "telnetSessionStartedTrap"),
        ("PCUBE-SE-MIB", "telnetSessionEndedTrap"),
        ("PCUBE-SE-MIB", "telnetSessionDeniedAccessTrap"),
        ("PCUBE-SE-MIB", "telnetSessionBadLoginTrap"),
        ("PCUBE-SE-MIB", "loggerUserLogIsFullTrap"),
        ("PCUBE-SE-MIB", "sntpClockDriftWarnTrap"),
        ("PCUBE-SE-MIB", "linkModeBypassTrap"),
        ("PCUBE-SE-MIB", "linkModeForwardingTrap"),
        ("PCUBE-SE-MIB", "linkModeCutoffTrap"),
        ("PCUBE-SE-MIB", "moduleAttackFilterActivatedTrap"),
        ("PCUBE-SE-MIB", "moduleAttackFilterDeactivatedTrap"),
        ("PCUBE-SE-MIB", "moduleEmAgentGenericTrap"),
        ("PCUBE-SE-MIB", "linkModeSniffingTrap"),
        ("PCUBE-SE-MIB", "moduleRedundancyReadyTrap"),
        ("PCUBE-SE-MIB", "moduleRedundantConfigurationMismatchTrap"),
        ("PCUBE-SE-MIB", "moduleLostRedundancyTrap"),
        ("PCUBE-SE-MIB", "moduleSmConnectionDownTrap"),
        ("PCUBE-SE-MIB", "moduleSmConnectionUpTrap"),
        ("PCUBE-SE-MIB", "moduleOperStatusChangeTrap"),
        ("PCUBE-SE-MIB", "portOperStatusChangeTrap"),
        ("PCUBE-SE-MIB", "chassisLineFeedAlarmOnTrap"),
        ("PCUBE-SE-MIB", "rdrFormatterCategoryDiscardingReportsTrap"),
        ("PCUBE-SE-MIB", "rdrFormatterCategoryStoppedDiscardingReportsTrap"),
        ("PCUBE-SE-MIB", "sessionStartedTrap"),
        ("PCUBE-SE-MIB", "sessionEndedTrap"),
        ("PCUBE-SE-MIB", "sessionDeniedAccessTrap"),
        ("PCUBE-SE-MIB", "sessionBadLoginTrap"),
        ("PCUBE-SE-MIB", "illegalSubscriberMappingTrap"),
        ("PCUBE-SE-MIB", "loggerLineAttackLogFullTrap"),
        ("PCUBE-SE-MIB", "vasServerOpertionalStatusChangeTrap"),
        ("PCUBE-SE-MIB", "pullRequestRetryFailedTrap"),
        ("PCUBE-SE-MIB", "mplsVpnTotalHWMappingsThresholdExceededTrap"))
)
if mibBuilder.loadTexts:
    pcubeSeEventsGroup.setStatus(
        "deprecated"
    )

pcubeSeEventsGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5655, 2, 3, 1, 4)
)
pcubeSeEventsGroupRev1.setObjects(
      *(("PCUBE-SE-MIB", "operationalStatusOperationalTrap"),
        ("PCUBE-SE-MIB", "operationalStatusWarningTrap"),
        ("PCUBE-SE-MIB", "operationalStatusFailureTrap"),
        ("PCUBE-SE-MIB", "systemResetTrap"),
        ("PCUBE-SE-MIB", "chassisTempAlarmOnTrap"),
        ("PCUBE-SE-MIB", "chassisTempAlarmOffTrap"),
        ("PCUBE-SE-MIB", "chassisVoltageAlarmOnTrap"),
        ("PCUBE-SE-MIB", "chassisFansAlarmOnTrap"),
        ("PCUBE-SE-MIB", "chassisPowerSupplyAlarmOnTrap"),
        ("PCUBE-SE-MIB", "rdrActiveConnectionTrap"),
        ("PCUBE-SE-MIB", "rdrNoActiveConnectionTrap"),
        ("PCUBE-SE-MIB", "rdrConnectionUpTrap"),
        ("PCUBE-SE-MIB", "rdrConnectionDownTrap"),
        ("PCUBE-SE-MIB", "loggerUserLogIsFullTrap"),
        ("PCUBE-SE-MIB", "sntpClockDriftWarnTrap"),
        ("PCUBE-SE-MIB", "linkModeBypassTrap"),
        ("PCUBE-SE-MIB", "linkModeForwardingTrap"),
        ("PCUBE-SE-MIB", "linkModeCutoffTrap"),
        ("PCUBE-SE-MIB", "moduleAttackFilterActivatedTrap"),
        ("PCUBE-SE-MIB", "moduleAttackFilterDeactivatedTrap"),
        ("PCUBE-SE-MIB", "moduleEmAgentGenericTrap"),
        ("PCUBE-SE-MIB", "linkModeSniffingTrap"),
        ("PCUBE-SE-MIB", "moduleRedundancyReadyTrap"),
        ("PCUBE-SE-MIB", "moduleRedundantConfigurationMismatchTrap"),
        ("PCUBE-SE-MIB", "moduleLostRedundancyTrap"),
        ("PCUBE-SE-MIB", "moduleSmConnectionDownTrap"),
        ("PCUBE-SE-MIB", "moduleSmConnectionUpTrap"),
        ("PCUBE-SE-MIB", "moduleOperStatusChangeTrap"),
        ("PCUBE-SE-MIB", "portOperStatusChangeTrap"),
        ("PCUBE-SE-MIB", "chassisLineFeedAlarmOnTrap"),
        ("PCUBE-SE-MIB", "rdrFormatterCategoryDiscardingReportsTrap"),
        ("PCUBE-SE-MIB", "rdrFormatterCategoryStoppedDiscardingReportsTrap"),
        ("PCUBE-SE-MIB", "sessionStartedTrap"),
        ("PCUBE-SE-MIB", "sessionEndedTrap"),
        ("PCUBE-SE-MIB", "sessionDeniedAccessTrap"),
        ("PCUBE-SE-MIB", "sessionBadLoginTrap"),
        ("PCUBE-SE-MIB", "illegalSubscriberMappingTrap"),
        ("PCUBE-SE-MIB", "loggerLineAttackLogFullTrap"),
        ("PCUBE-SE-MIB", "vasServerOpertionalStatusChangeTrap"),
        ("PCUBE-SE-MIB", "pullRequestRetryFailedTrap"),
        ("PCUBE-SE-MIB", "mplsVpnTotalHWMappingsThresholdExceededTrap"))
)
if mibBuilder.loadTexts:
    pcubeSeEventsGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

pcubeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5655, 2, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pcubeCompliance.setStatus(
        "deprecated"
    )

pcubeComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5655, 2, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    pcubeComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PCUBE-SE-MIB",
    **{"LinkModeType": LinkModeType,
       "pcubeSeMIB": pcubeSeMIB,
       "pcubeSeConformance": pcubeSeConformance,
       "pcubeSeGroups": pcubeSeGroups,
       "pcubeSystemGroup": pcubeSystemGroup,
       "pcubeChassisGroup": pcubeChassisGroup,
       "pcuebModuleGroup": pcuebModuleGroup,
       "pcubeLinkGroup": pcubeLinkGroup,
       "pcubeDiskGroup": pcubeDiskGroup,
       "pcubeRdrFormatterGroup": pcubeRdrFormatterGroup,
       "pcubeLoggerGroup": pcubeLoggerGroup,
       "pcubeSubscribersGroup": pcubeSubscribersGroup,
       "pcubeTrafficProcessorGroup": pcubeTrafficProcessorGroup,
       "pcubePortGroup": pcubePortGroup,
       "pcubeTxQueuesGroup": pcubeTxQueuesGroup,
       "pcubeGlobalControllersGroup": pcubeGlobalControllersGroup,
       "pcubeApplicationGroup": pcubeApplicationGroup,
       "pcubeTrafficCountersGroup": pcubeTrafficCountersGroup,
       "pcubeAttackGroup": pcubeAttackGroup,
       "pcubeVasTrafficForwardingGroup": pcubeVasTrafficForwardingGroup,
       "pcubeMplsVpnAutoLearnGroup": pcubeMplsVpnAutoLearnGroup,
       "pcubeTrapObjectsGroup": pcubeTrapObjectsGroup,
       "pcubeSeCompliances": pcubeSeCompliances,
       "pcubeCompliance": pcubeCompliance,
       "pcubeComplianceRev1": pcubeComplianceRev1,
       "pcubeSeEventsGroup": pcubeSeEventsGroup,
       "pcubeSeEventsGroupRev1": pcubeSeEventsGroupRev1,
       "pcubeSeEvents": pcubeSeEvents,
       "operationalStatusOperationalTrap": operationalStatusOperationalTrap,
       "operationalStatusWarningTrap": operationalStatusWarningTrap,
       "operationalStatusFailureTrap": operationalStatusFailureTrap,
       "systemResetTrap": systemResetTrap,
       "chassisTempAlarmOnTrap": chassisTempAlarmOnTrap,
       "chassisTempAlarmOffTrap": chassisTempAlarmOffTrap,
       "chassisVoltageAlarmOnTrap": chassisVoltageAlarmOnTrap,
       "chassisFansAlarmOnTrap": chassisFansAlarmOnTrap,
       "chassisPowerSupplyAlarmOnTrap": chassisPowerSupplyAlarmOnTrap,
       "rdrActiveConnectionTrap": rdrActiveConnectionTrap,
       "rdrNoActiveConnectionTrap": rdrNoActiveConnectionTrap,
       "rdrConnectionUpTrap": rdrConnectionUpTrap,
       "rdrConnectionDownTrap": rdrConnectionDownTrap,
       "telnetSessionStartedTrap": telnetSessionStartedTrap,
       "telnetSessionEndedTrap": telnetSessionEndedTrap,
       "telnetSessionDeniedAccessTrap": telnetSessionDeniedAccessTrap,
       "telnetSessionBadLoginTrap": telnetSessionBadLoginTrap,
       "loggerUserLogIsFullTrap": loggerUserLogIsFullTrap,
       "sntpClockDriftWarnTrap": sntpClockDriftWarnTrap,
       "linkModeBypassTrap": linkModeBypassTrap,
       "linkModeForwardingTrap": linkModeForwardingTrap,
       "linkModeCutoffTrap": linkModeCutoffTrap,
       "pcubeSeEventGenericString1": pcubeSeEventGenericString1,
       "pcubeSeEventGenericString2": pcubeSeEventGenericString2,
       "moduleAttackFilterActivatedTrap": moduleAttackFilterActivatedTrap,
       "moduleAttackFilterDeactivatedTrap": moduleAttackFilterDeactivatedTrap,
       "moduleEmAgentGenericTrap": moduleEmAgentGenericTrap,
       "linkModeSniffingTrap": linkModeSniffingTrap,
       "moduleRedundancyReadyTrap": moduleRedundancyReadyTrap,
       "moduleRedundantConfigurationMismatchTrap": moduleRedundantConfigurationMismatchTrap,
       "moduleLostRedundancyTrap": moduleLostRedundancyTrap,
       "moduleSmConnectionDownTrap": moduleSmConnectionDownTrap,
       "moduleSmConnectionUpTrap": moduleSmConnectionUpTrap,
       "moduleOperStatusChangeTrap": moduleOperStatusChangeTrap,
       "portOperStatusChangeTrap": portOperStatusChangeTrap,
       "chassisLineFeedAlarmOnTrap": chassisLineFeedAlarmOnTrap,
       "rdrFormatterCategoryDiscardingReportsTrap": rdrFormatterCategoryDiscardingReportsTrap,
       "rdrFormatterCategoryStoppedDiscardingReportsTrap": rdrFormatterCategoryStoppedDiscardingReportsTrap,
       "sessionStartedTrap": sessionStartedTrap,
       "sessionEndedTrap": sessionEndedTrap,
       "sessionDeniedAccessTrap": sessionDeniedAccessTrap,
       "sessionBadLoginTrap": sessionBadLoginTrap,
       "illegalSubscriberMappingTrap": illegalSubscriberMappingTrap,
       "loggerLineAttackLogFullTrap": loggerLineAttackLogFullTrap,
       "vasServerOpertionalStatusChangeTrap": vasServerOpertionalStatusChangeTrap,
       "pullRequestNumber": pullRequestNumber,
       "pullRequestRetryFailedTrap": pullRequestRetryFailedTrap,
       "mplsVpnTotalHWMappingsThresholdExceededTrap": mplsVpnTotalHWMappingsThresholdExceededTrap,
       "pcubeSEObjs": pcubeSEObjs,
       "systemGrp": systemGrp,
       "sysOperationalStatus": sysOperationalStatus,
       "sysFailureRecovery": sysFailureRecovery,
       "sysVersion": sysVersion,
       "pchassisGrp": pchassisGrp,
       "pchassisSysType": pchassisSysType,
       "pchassisPowerSupplyAlarm": pchassisPowerSupplyAlarm,
       "pchassisFansAlarm": pchassisFansAlarm,
       "pchassisTempAlarm": pchassisTempAlarm,
       "pchassisVoltageAlarm": pchassisVoltageAlarm,
       "pchassisNumSlots": pchassisNumSlots,
       "pchassisSlotConfig": pchassisSlotConfig,
       "pchassisPsuType": pchassisPsuType,
       "pchassisLineFeedAlarm": pchassisLineFeedAlarm,
       "pmoduleGrp": pmoduleGrp,
       "pmoduleTable": pmoduleTable,
       "pmoduleEntry": pmoduleEntry,
       "pmoduleIndex": pmoduleIndex,
       "pmoduleType": pmoduleType,
       "pmoduleNumTrafficProcessors": pmoduleNumTrafficProcessors,
       "pmoduleSlotNum": pmoduleSlotNum,
       "pmoduleHwVersion": pmoduleHwVersion,
       "pmoduleNumPorts": pmoduleNumPorts,
       "pmoduleNumLinks": pmoduleNumLinks,
       "pmoduleConnectionMode": pmoduleConnectionMode,
       "pmoduleSerialNumber": pmoduleSerialNumber,
       "pmoduleUpStreamAttackFilteringTime": pmoduleUpStreamAttackFilteringTime,
       "pmoduleUpStreamLastAttackFilteringTime": pmoduleUpStreamLastAttackFilteringTime,
       "pmoduleDownStreamAttackFilteringTime": pmoduleDownStreamAttackFilteringTime,
       "pmoduleDownStreamLastAttackFilteringTime": pmoduleDownStreamLastAttackFilteringTime,
       "pmoduleAttackObjectsClearTime": pmoduleAttackObjectsClearTime,
       "pmoduleAdminStatus": pmoduleAdminStatus,
       "pmoduleOperStatus": pmoduleOperStatus,
       "linkGrp": linkGrp,
       "linkTable": linkTable,
       "linkEntry": linkEntry,
       "linkModuleIndex": linkModuleIndex,
       "linkIndex": linkIndex,
       "linkAdminModeOnActive": linkAdminModeOnActive,
       "linkAdminModeOnFailure": linkAdminModeOnFailure,
       "linkOperMode": linkOperMode,
       "linkStatusReflectionEnable": linkStatusReflectionEnable,
       "linkSubscriberSidePortIndex": linkSubscriberSidePortIndex,
       "linkNetworkSidePortIndex": linkNetworkSidePortIndex,
       "diskGrp": diskGrp,
       "diskNumUsedBytes": diskNumUsedBytes,
       "diskNumFreeBytes": diskNumFreeBytes,
       "rdrFormatterGrp": rdrFormatterGrp,
       "rdrFormatterEnable": rdrFormatterEnable,
       "rdrFormatterDestTable": rdrFormatterDestTable,
       "rdrFormatterDestEntry": rdrFormatterDestEntry,
       "rdrFormatterDestIPAddr": rdrFormatterDestIPAddr,
       "rdrFormatterDestPort": rdrFormatterDestPort,
       "rdrFormatterDestPriority": rdrFormatterDestPriority,
       "rdrFormatterDestStatus": rdrFormatterDestStatus,
       "rdrFormatterDestConnectionStatus": rdrFormatterDestConnectionStatus,
       "rdrFormatterDestNumReportsSent": rdrFormatterDestNumReportsSent,
       "rdrFormatterDestNumReportsDiscarded": rdrFormatterDestNumReportsDiscarded,
       "rdrFormatterDestReportRate": rdrFormatterDestReportRate,
       "rdrFormatterDestReportRatePeak": rdrFormatterDestReportRatePeak,
       "rdrFormatterDestReportRatePeakTime": rdrFormatterDestReportRatePeakTime,
       "rdrFormatterNumReportsSent": rdrFormatterNumReportsSent,
       "rdrFormatterNumReportsDiscarded": rdrFormatterNumReportsDiscarded,
       "rdrFormatterClearCountersTime": rdrFormatterClearCountersTime,
       "rdrFormatterReportRate": rdrFormatterReportRate,
       "rdrFormatterReportRatePeak": rdrFormatterReportRatePeak,
       "rdrFormatterReportRatePeakTime": rdrFormatterReportRatePeakTime,
       "rdrFormatterProtocol": rdrFormatterProtocol,
       "rdrFormatterForwardingMode": rdrFormatterForwardingMode,
       "rdrFormatterCategoryTable": rdrFormatterCategoryTable,
       "rdrFormatterCategoryEntry": rdrFormatterCategoryEntry,
       "rdrFormatterCategoryIndex": rdrFormatterCategoryIndex,
       "rdrFormatterCategoryName": rdrFormatterCategoryName,
       "rdrFormatterCategoryNumReportsSent": rdrFormatterCategoryNumReportsSent,
       "rdrFormatterCategoryNumReportsDiscarded": rdrFormatterCategoryNumReportsDiscarded,
       "rdrFormatterCategoryReportRate": rdrFormatterCategoryReportRate,
       "rdrFormatterCategoryReportRatePeak": rdrFormatterCategoryReportRatePeak,
       "rdrFormatterCategoryReportRatePeakTime": rdrFormatterCategoryReportRatePeakTime,
       "rdrFormatterCategoryNumReportsQueued": rdrFormatterCategoryNumReportsQueued,
       "rdrFormatterCategoryDestTable": rdrFormatterCategoryDestTable,
       "rdrFormatterCategoryDestEntry": rdrFormatterCategoryDestEntry,
       "rdrFormatterCategoryDestPriority": rdrFormatterCategoryDestPriority,
       "rdrFormatterCategoryDestStatus": rdrFormatterCategoryDestStatus,
       "loggerGrp": loggerGrp,
       "loggerUserLogEnable": loggerUserLogEnable,
       "loggerUserLogNumInfo": loggerUserLogNumInfo,
       "loggerUserLogNumWarning": loggerUserLogNumWarning,
       "loggerUserLogNumError": loggerUserLogNumError,
       "loggerUserLogNumFatal": loggerUserLogNumFatal,
       "loggerUserLogClearCountersTime": loggerUserLogClearCountersTime,
       "subscribersGrp": subscribersGrp,
       "subscribersInfoTable": subscribersInfoTable,
       "subscribersInfoEntry": subscribersInfoEntry,
       "subscribersNumIntroduced": subscribersNumIntroduced,
       "subscribersNumFree": subscribersNumFree,
       "subscribersNumIpAddrMappings": subscribersNumIpAddrMappings,
       "subscribersNumIpAddrMappingsFree": subscribersNumIpAddrMappingsFree,
       "subscribersNumIpRangeMappings": subscribersNumIpRangeMappings,
       "subscribersNumIpRangeMappingsFree": subscribersNumIpRangeMappingsFree,
       "subscribersNumVlanMappings": subscribersNumVlanMappings,
       "subscribersNumVlanMappingsFree": subscribersNumVlanMappingsFree,
       "subscribersNumActive": subscribersNumActive,
       "subscribersNumActivePeak": subscribersNumActivePeak,
       "subscribersNumActivePeakTime": subscribersNumActivePeakTime,
       "subscribersNumUpdates": subscribersNumUpdates,
       "subscribersCountersClearTime": subscribersCountersClearTime,
       "subscribersNumTpIpRanges": subscribersNumTpIpRanges,
       "subscribersNumTpIpRangesFree": subscribersNumTpIpRangesFree,
       "subscribersNumAnonymous": subscribersNumAnonymous,
       "subscribersNumWithSessions": subscribersNumWithSessions,
       "subscribersPropertiesTable": subscribersPropertiesTable,
       "subscribersPropertiesEntry": subscribersPropertiesEntry,
       "spIndex": spIndex,
       "spName": spName,
       "spType": spType,
       "subscribersPropertiesValueTable": subscribersPropertiesValueTable,
       "subscribersPropertiesValueEntry": subscribersPropertiesValueEntry,
       "spvIndex": spvIndex,
       "spvSubName": spvSubName,
       "spvPropertyName": spvPropertyName,
       "spvRowStatus": spvRowStatus,
       "spvPropertyStringValue": spvPropertyStringValue,
       "spvPropertyUintValue": spvPropertyUintValue,
       "spvPropertyCounter64Value": spvPropertyCounter64Value,
       "trafficProcessorGrp": trafficProcessorGrp,
       "tpInfoTable": tpInfoTable,
       "tpInfoEntry": tpInfoEntry,
       "tpModuleIndex": tpModuleIndex,
       "tpIndex": tpIndex,
       "tpTotalNumHandledPackets": tpTotalNumHandledPackets,
       "tpTotalNumHandledFlows": tpTotalNumHandledFlows,
       "tpNumActiveFlows": tpNumActiveFlows,
       "tpNumActiveFlowsPeak": tpNumActiveFlowsPeak,
       "tpNumActiveFlowsPeakTime": tpNumActiveFlowsPeakTime,
       "tpNumTcpActiveFlows": tpNumTcpActiveFlows,
       "tpNumTcpActiveFlowsPeak": tpNumTcpActiveFlowsPeak,
       "tpNumTcpActiveFlowsPeakTime": tpNumTcpActiveFlowsPeakTime,
       "tpNumUdpActiveFlows": tpNumUdpActiveFlows,
       "tpNumUdpActiveFlowsPeak": tpNumUdpActiveFlowsPeak,
       "tpNumUdpActiveFlowsPeakTime": tpNumUdpActiveFlowsPeakTime,
       "tpNumNonTcpUdpActiveFlows": tpNumNonTcpUdpActiveFlows,
       "tpNumNonTcpUdpActiveFlowsPeak": tpNumNonTcpUdpActiveFlowsPeak,
       "tpNumNonTcpUdpActiveFlowsPeakTime": tpNumNonTcpUdpActiveFlowsPeakTime,
       "tpTotalNumBlockedPackets": tpTotalNumBlockedPackets,
       "tpTotalNumBlockedFlows": tpTotalNumBlockedFlows,
       "tpTotalNumDiscardedPacketsDueToBwLimit": tpTotalNumDiscardedPacketsDueToBwLimit,
       "tpTotalNumWredDiscardedPackets": tpTotalNumWredDiscardedPackets,
       "tpTotalNumFragments": tpTotalNumFragments,
       "tpTotalNumNonIpPackets": tpTotalNumNonIpPackets,
       "tpTotalNumIpCrcErrPackets": tpTotalNumIpCrcErrPackets,
       "tpTotalNumIpLengthErrPackets": tpTotalNumIpLengthErrPackets,
       "tpTotalNumIpBroadcastPackets": tpTotalNumIpBroadcastPackets,
       "tpTotalNumTtlErrPackets": tpTotalNumTtlErrPackets,
       "tpTotalNumTcpUdpCrcErrPackets": tpTotalNumTcpUdpCrcErrPackets,
       "tpClearCountersTime": tpClearCountersTime,
       "tpHandledPacketsRate": tpHandledPacketsRate,
       "tpHandledPacketsRatePeak": tpHandledPacketsRatePeak,
       "tpHandledPacketsRatePeakTime": tpHandledPacketsRatePeakTime,
       "tpHandledFlowsRate": tpHandledFlowsRate,
       "tpHandledFlowsRatePeak": tpHandledFlowsRatePeak,
       "tpHandledFlowsRatePeakTime": tpHandledFlowsRatePeakTime,
       "tpCpuUtilization": tpCpuUtilization,
       "tpCpuUtilizationPeak": tpCpuUtilizationPeak,
       "tpCpuUtilizationPeakTime": tpCpuUtilizationPeakTime,
       "tpFlowsCapacityUtilization": tpFlowsCapacityUtilization,
       "tpFlowsCapacityUtilizationPeak": tpFlowsCapacityUtilizationPeak,
       "tpFlowsCapacityUtilizationPeakTime": tpFlowsCapacityUtilizationPeakTime,
       "tpServiceLoss": tpServiceLoss,
       "pportGrp": pportGrp,
       "pportTable": pportTable,
       "pportEntry": pportEntry,
       "pportModuleIndex": pportModuleIndex,
       "pportIndex": pportIndex,
       "pportType": pportType,
       "pportNumTxQueues": pportNumTxQueues,
       "pportIfIndex": pportIfIndex,
       "pportAdminSpeed": pportAdminSpeed,
       "pportAdminDuplex": pportAdminDuplex,
       "pportOperDuplex": pportOperDuplex,
       "pportLinkIndex": pportLinkIndex,
       "pportOperStatus": pportOperStatus,
       "txQueuesGrp": txQueuesGrp,
       "txQueuesTable": txQueuesTable,
       "txQueuesEntry": txQueuesEntry,
       "txQueuesModuleIndex": txQueuesModuleIndex,
       "txQueuesPortIndex": txQueuesPortIndex,
       "txQueuesQueueIndex": txQueuesQueueIndex,
       "txQueuesDescription": txQueuesDescription,
       "txQueuesBandwidth": txQueuesBandwidth,
       "txQueuesUtilization": txQueuesUtilization,
       "txQueuesUtilizationPeak": txQueuesUtilizationPeak,
       "txQueuesUtilizationPeakTime": txQueuesUtilizationPeakTime,
       "txQueuesClearCountersTime": txQueuesClearCountersTime,
       "txQueuesDroppedBytes": txQueuesDroppedBytes,
       "globalControllersGrp": globalControllersGrp,
       "globalControllersTable": globalControllersTable,
       "globalControllersEntry": globalControllersEntry,
       "globalControllersModuleIndex": globalControllersModuleIndex,
       "globalControllersPortIndex": globalControllersPortIndex,
       "globalControllersIndex": globalControllersIndex,
       "globalControllersDescription": globalControllersDescription,
       "globalControllersBandwidth": globalControllersBandwidth,
       "globalControllersUtilization": globalControllersUtilization,
       "globalControllersUtilizationPeak": globalControllersUtilizationPeak,
       "globalControllersUtilizationPeakTime": globalControllersUtilizationPeakTime,
       "globalControllersClearCountersTime": globalControllersClearCountersTime,
       "globalControllersDroppedBytes": globalControllersDroppedBytes,
       "applicationGrp": applicationGrp,
       "appInfoTable": appInfoTable,
       "appInfoEntry": appInfoEntry,
       "appName": appName,
       "appDescription": appDescription,
       "appVersion": appVersion,
       "appPropertiesTable": appPropertiesTable,
       "appPropertiesEntry": appPropertiesEntry,
       "apIndex": apIndex,
       "apName": apName,
       "apType": apType,
       "appPropertiesValueTable": appPropertiesValueTable,
       "appPropertiesValueEntry": appPropertiesValueEntry,
       "apvIndex": apvIndex,
       "apvPropertyName": apvPropertyName,
       "apvRowStatus": apvRowStatus,
       "apvPropertyStringValue": apvPropertyStringValue,
       "apvPropertyUintValue": apvPropertyUintValue,
       "apvPropertyCounter64Value": apvPropertyCounter64Value,
       "trafficCountersGrp": trafficCountersGrp,
       "trafficCountersTable": trafficCountersTable,
       "trafficCountersEntry": trafficCountersEntry,
       "trafficCounterIndex": trafficCounterIndex,
       "trafficCounterValue": trafficCounterValue,
       "trafficCounterName": trafficCounterName,
       "trafficCounterType": trafficCounterType,
       "attackGrp": attackGrp,
       "attackTypeTable": attackTypeTable,
       "attackTypeEntry": attackTypeEntry,
       "attackTypeIndex": attackTypeIndex,
       "attackTypeName": attackTypeName,
       "attackTypeCurrentNumAttacks": attackTypeCurrentNumAttacks,
       "attackTypeTotalNumAttacks": attackTypeTotalNumAttacks,
       "attackTypeTotalNumFlows": attackTypeTotalNumFlows,
       "attackTypeTotalNumSeconds": attackTypeTotalNumSeconds,
       "vasTrafficForwardingGrp": vasTrafficForwardingGrp,
       "vasServerTable": vasServerTable,
       "vasServerEntry": vasServerEntry,
       "vasServerIndex": vasServerIndex,
       "vasServerId": vasServerId,
       "vasServerAdminStatus": vasServerAdminStatus,
       "vasServerOperStatus": vasServerOperStatus,
       "mplsVpnAutoLearnGrp": mplsVpnAutoLearnGrp,
       "mplsVpnSoftwareCountersTable": mplsVpnSoftwareCountersTable,
       "mplsVpnSoftwareCountersEntry": mplsVpnSoftwareCountersEntry,
       "mplsVpnMaxHWMappings": mplsVpnMaxHWMappings,
       "mplsVpnCurrentHWMappings": mplsVpnCurrentHWMappings}
)
