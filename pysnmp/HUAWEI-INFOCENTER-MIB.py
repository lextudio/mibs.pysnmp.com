# SNMP MIB module (HUAWEI-INFOCENTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-INFOCENTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:03 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwInfoCenter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212)
)
hwInfoCenter.setRevisions(
        ("2015-08-17 15:44",
         "2014-08-05 11:50",
         "2014-12-16 17:06",
         "2013-07-11 16:40",
         "2013-07-05 17:10",
         "2011-08-08 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HWMessageLevel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alerts", 1),
          ("critical", 2),
          ("debugging", 7),
          ("emergencies", 0),
          ("errors", 3),
          ("informational", 6),
          ("notifications", 5),
          ("warnings", 4))
    )



class HWFacilityType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("local0", 16),
          ("local1", 17),
          ("local2", 18),
          ("local3", 19),
          ("local4", 20),
          ("local5", 21),
          ("local6", 22),
          ("local7", 23))
    )



# MIB Managed Objects in the order of their OIDs

_HwInfoCenterObjects_ObjectIdentity = ObjectIdentity
hwInfoCenterObjects = _HwInfoCenterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1)
)
_HwICEnable_Type = TruthValue
_HwICEnable_Object = MibScalar
hwICEnable = _HwICEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 1),
    _HwICEnable_Type()
)
hwICEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwICEnable.setStatus("current")
_HwICLoghost_ObjectIdentity = ObjectIdentity
hwICLoghost = _HwICLoghost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 2)
)


class _HwICLoghostSourceInterface_Type(DisplayString):
    """Custom type hwICLoghostSourceInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HwICLoghostSourceInterface_Type.__name__ = "DisplayString"
_HwICLoghostSourceInterface_Object = MibScalar
hwICLoghostSourceInterface = _HwICLoghostSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 2, 1),
    _HwICLoghostSourceInterface_Type()
)
hwICLoghostSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwICLoghostSourceInterface.setStatus("current")
_HwICLoghostTable_Object = MibTable
hwICLoghostTable = _HwICLoghostTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hwICLoghostTable.setStatus("current")
_HwICLoghostEntry_Object = MibTableRow
hwICLoghostEntry = _HwICLoghostEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 2, 2, 1)
)
hwICLoghostEntry.setIndexNames(
    (0, "HUAWEI-INFOCENTER-MIB", "hwICLoghostIpAddressType"),
    (0, "HUAWEI-INFOCENTER-MIB", "hwICLoghostIpAddress"),
    (1, "HUAWEI-INFOCENTER-MIB", "hwICLoghostVpnInstance"),
)
if mibBuilder.loadTexts:
    hwICLoghostEntry.setStatus("current")
_HwICLoghostIpAddressType_Type = InetAddressType
_HwICLoghostIpAddressType_Object = MibTableColumn
hwICLoghostIpAddressType = _HwICLoghostIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 2, 2, 1, 1),
    _HwICLoghostIpAddressType_Type()
)
hwICLoghostIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwICLoghostIpAddressType.setStatus("current")
_HwICLoghostIpAddress_Type = InetAddress
_HwICLoghostIpAddress_Object = MibTableColumn
hwICLoghostIpAddress = _HwICLoghostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 2, 2, 1, 2),
    _HwICLoghostIpAddress_Type()
)
hwICLoghostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwICLoghostIpAddress.setStatus("current")


class _HwICLoghostVpnInstance_Type(DisplayString):
    """Custom type hwICLoghostVpnInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwICLoghostVpnInstance_Type.__name__ = "DisplayString"
_HwICLoghostVpnInstance_Object = MibTableColumn
hwICLoghostVpnInstance = _HwICLoghostVpnInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 2, 2, 1, 3),
    _HwICLoghostVpnInstance_Type()
)
hwICLoghostVpnInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwICLoghostVpnInstance.setStatus("current")


class _HwICLoghostChannel_Type(Integer32):
    """Custom type hwICLoghostChannel based on Integer32"""
    defaultValue = 2


_HwICLoghostChannel_Object = MibTableColumn
hwICLoghostChannel = _HwICLoghostChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 2, 2, 1, 4),
    _HwICLoghostChannel_Type()
)
hwICLoghostChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwICLoghostChannel.setStatus("current")


class _HwICLoghostFacility_Type(HWFacilityType):
    """Custom type hwICLoghostFacility based on HWFacilityType"""


_HwICLoghostFacility_Object = MibTableColumn
hwICLoghostFacility = _HwICLoghostFacility_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 2, 2, 1, 5),
    _HwICLoghostFacility_Type()
)
hwICLoghostFacility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwICLoghostFacility.setStatus("current")


class _HwICLoghostLanguage_Type(Integer32):
    """Custom type hwICLoghostLanguage based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chinese", 1),
          ("english", 2))
    )


_HwICLoghostLanguage_Type.__name__ = "Integer32"
_HwICLoghostLanguage_Object = MibTableColumn
hwICLoghostLanguage = _HwICLoghostLanguage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 2, 2, 1, 6),
    _HwICLoghostLanguage_Type()
)
hwICLoghostLanguage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwICLoghostLanguage.setStatus("current")
_HwICLoghostRowStatus_Type = RowStatus
_HwICLoghostRowStatus_Object = MibTableColumn
hwICLoghostRowStatus = _HwICLoghostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 2, 2, 1, 7),
    _HwICLoghostRowStatus_Type()
)
hwICLoghostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwICLoghostRowStatus.setStatus("current")
_HwICChannel_ObjectIdentity = ObjectIdentity
hwICChannel = _HwICChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 3)
)
_HwICChannelTable_Object = MibTable
hwICChannelTable = _HwICChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hwICChannelTable.setStatus("current")
_HwICChannelEntry_Object = MibTableRow
hwICChannelEntry = _HwICChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 3, 1, 1)
)
hwICChannelEntry.setIndexNames(
    (0, "HUAWEI-INFOCENTER-MIB", "hwICChannelIndex"),
)
if mibBuilder.loadTexts:
    hwICChannelEntry.setStatus("current")
_HwICChannelIndex_Type = Integer32
_HwICChannelIndex_Object = MibTableColumn
hwICChannelIndex = _HwICChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 3, 1, 1, 1),
    _HwICChannelIndex_Type()
)
hwICChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwICChannelIndex.setStatus("current")


class _HwICChannelName_Type(DisplayString):
    """Custom type hwICChannelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_HwICChannelName_Type.__name__ = "DisplayString"
_HwICChannelName_Object = MibTableColumn
hwICChannelName = _HwICChannelName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 3, 1, 1, 2),
    _HwICChannelName_Type()
)
hwICChannelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwICChannelName.setStatus("current")
_HwICModule_ObjectIdentity = ObjectIdentity
hwICModule = _HwICModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 4)
)
_HwICModuleTable_Object = MibTable
hwICModuleTable = _HwICModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hwICModuleTable.setStatus("current")
_HwICModuleEntry_Object = MibTableRow
hwICModuleEntry = _HwICModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 4, 1, 1)
)
hwICModuleEntry.setIndexNames(
    (0, "HUAWEI-INFOCENTER-MIB", "hwICModuleIndex"),
)
if mibBuilder.loadTexts:
    hwICModuleEntry.setStatus("current")
_HwICModuleIndex_Type = Integer32
_HwICModuleIndex_Object = MibTableColumn
hwICModuleIndex = _HwICModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 4, 1, 1, 1),
    _HwICModuleIndex_Type()
)
hwICModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwICModuleIndex.setStatus("current")


class _HwICModuleName_Type(DisplayString):
    """Custom type hwICModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_HwICModuleName_Type.__name__ = "DisplayString"
_HwICModuleName_Object = MibTableColumn
hwICModuleName = _HwICModuleName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 4, 1, 1, 2),
    _HwICModuleName_Type()
)
hwICModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwICModuleName.setStatus("current")
_HwICLogFilter_ObjectIdentity = ObjectIdentity
hwICLogFilter = _HwICLogFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 5)
)
_HwICLogFilterTable_Object = MibTable
hwICLogFilterTable = _HwICLogFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hwICLogFilterTable.setStatus("current")
_HwICLogFilterEntry_Object = MibTableRow
hwICLogFilterEntry = _HwICLogFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 5, 1, 1)
)
hwICLogFilterEntry.setIndexNames(
    (0, "HUAWEI-INFOCENTER-MIB", "hwICChannelIndex"),
    (1, "HUAWEI-INFOCENTER-MIB", "hwICModuleName"),
)
if mibBuilder.loadTexts:
    hwICLogFilterEntry.setStatus("current")


class _HwICLogFilterState_Type(Integer32):
    """Custom type hwICLogFilterState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_HwICLogFilterState_Type.__name__ = "Integer32"
_HwICLogFilterState_Object = MibTableColumn
hwICLogFilterState = _HwICLogFilterState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 5, 1, 1, 1),
    _HwICLogFilterState_Type()
)
hwICLogFilterState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwICLogFilterState.setStatus("current")
_HwICLogFilterLevel_Type = HWMessageLevel
_HwICLogFilterLevel_Object = MibTableColumn
hwICLogFilterLevel = _HwICLogFilterLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 5, 1, 1, 2),
    _HwICLogFilterLevel_Type()
)
hwICLogFilterLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwICLogFilterLevel.setStatus("current")
_HwICLogFilterRowStatus_Type = RowStatus
_HwICLogFilterRowStatus_Object = MibTableColumn
hwICLogFilterRowStatus = _HwICLogFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 5, 1, 1, 3),
    _HwICLogFilterRowStatus_Type()
)
hwICLogFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwICLogFilterRowStatus.setStatus("current")
_HwICLogFile_ObjectIdentity = ObjectIdentity
hwICLogFile = _HwICLogFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 6)
)


class _HwICLogFileType_Type(Integer32):
    """Custom type hwICLogFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("diag", 2),
          ("log", 1))
    )


_HwICLogFileType_Type.__name__ = "Integer32"
_HwICLogFileType_Object = MibScalar
hwICLogFileType = _HwICLogFileType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 6, 1),
    _HwICLogFileType_Type()
)
hwICLogFileType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwICLogFileType.setStatus("current")


class _HwICLogFileName_Type(DisplayString):
    """Custom type hwICLogFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_HwICLogFileName_Type.__name__ = "DisplayString"
_HwICLogFileName_Object = MibScalar
hwICLogFileName = _HwICLogFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 1, 6, 2),
    _HwICLogFileName_Type()
)
hwICLogFileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwICLogFileName.setStatus("current")
_HwInfoCenterNotifications_ObjectIdentity = ObjectIdentity
hwInfoCenterNotifications = _HwInfoCenterNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 2)
)
_HwInfoCenterConformance_ObjectIdentity = ObjectIdentity
hwInfoCenterConformance = _HwInfoCenterConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 3)
)
_HwInfoCenterCompliances_ObjectIdentity = ObjectIdentity
hwInfoCenterCompliances = _HwInfoCenterCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 3, 1)
)
_HwInfoCenterGroups_ObjectIdentity = ObjectIdentity
hwInfoCenterGroups = _HwInfoCenterGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 3, 2)
)

# Managed Objects groups

hwInfoCenterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 3, 2, 1)
)
hwInfoCenterGroup.setObjects(
      *(("HUAWEI-INFOCENTER-MIB", "hwICEnable"),
        ("HUAWEI-INFOCENTER-MIB", "hwICLoghostSourceInterface"),
        ("HUAWEI-INFOCENTER-MIB", "hwICLogFileType"),
        ("HUAWEI-INFOCENTER-MIB", "hwICLogFileName"))
)
if mibBuilder.loadTexts:
    hwInfoCenterGroup.setStatus("current")


# Notification objects

hwICLogFileStorageThrd = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 2, 1)
)
hwICLogFileStorageThrd.setObjects(
    ("HUAWEI-INFOCENTER-MIB", "hwICLogFileType")
)
if mibBuilder.loadTexts:
    hwICLogFileStorageThrd.setStatus(
        "current"
    )

hwICLogFileAging = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 2, 2)
)
hwICLogFileAging.setObjects(
    ("HUAWEI-INFOCENTER-MIB", "hwICLogFileName")
)
if mibBuilder.loadTexts:
    hwICLogFileAging.setStatus(
        "current"
    )

hwICInsufficientSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 2, 3)
)
if mibBuilder.loadTexts:
    hwICInsufficientSpace.setStatus(
        "current"
    )

hwICLogBufferLose = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 2, 4)
)
if mibBuilder.loadTexts:
    hwICLogBufferLose.setStatus(
        "current"
    )


# Notifications groups

hwInfoCenterTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 3, 2, 2)
)
hwInfoCenterTrapGroup.setObjects(
      *(("HUAWEI-INFOCENTER-MIB", "hwICLogFileStorageThrd"),
        ("HUAWEI-INFOCENTER-MIB", "hwICLogFileAging"),
        ("HUAWEI-INFOCENTER-MIB", "hwICLogBufferLose"))
)
if mibBuilder.loadTexts:
    hwInfoCenterTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwInfoCenterCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 212, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwInfoCenterCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-INFOCENTER-MIB",
    **{"HWMessageLevel": HWMessageLevel,
       "HWFacilityType": HWFacilityType,
       "hwInfoCenter": hwInfoCenter,
       "hwInfoCenterObjects": hwInfoCenterObjects,
       "hwICEnable": hwICEnable,
       "hwICLoghost": hwICLoghost,
       "hwICLoghostSourceInterface": hwICLoghostSourceInterface,
       "hwICLoghostTable": hwICLoghostTable,
       "hwICLoghostEntry": hwICLoghostEntry,
       "hwICLoghostIpAddressType": hwICLoghostIpAddressType,
       "hwICLoghostIpAddress": hwICLoghostIpAddress,
       "hwICLoghostVpnInstance": hwICLoghostVpnInstance,
       "hwICLoghostChannel": hwICLoghostChannel,
       "hwICLoghostFacility": hwICLoghostFacility,
       "hwICLoghostLanguage": hwICLoghostLanguage,
       "hwICLoghostRowStatus": hwICLoghostRowStatus,
       "hwICChannel": hwICChannel,
       "hwICChannelTable": hwICChannelTable,
       "hwICChannelEntry": hwICChannelEntry,
       "hwICChannelIndex": hwICChannelIndex,
       "hwICChannelName": hwICChannelName,
       "hwICModule": hwICModule,
       "hwICModuleTable": hwICModuleTable,
       "hwICModuleEntry": hwICModuleEntry,
       "hwICModuleIndex": hwICModuleIndex,
       "hwICModuleName": hwICModuleName,
       "hwICLogFilter": hwICLogFilter,
       "hwICLogFilterTable": hwICLogFilterTable,
       "hwICLogFilterEntry": hwICLogFilterEntry,
       "hwICLogFilterState": hwICLogFilterState,
       "hwICLogFilterLevel": hwICLogFilterLevel,
       "hwICLogFilterRowStatus": hwICLogFilterRowStatus,
       "hwICLogFile": hwICLogFile,
       "hwICLogFileType": hwICLogFileType,
       "hwICLogFileName": hwICLogFileName,
       "hwInfoCenterNotifications": hwInfoCenterNotifications,
       "hwICLogFileStorageThrd": hwICLogFileStorageThrd,
       "hwICLogFileAging": hwICLogFileAging,
       "hwICInsufficientSpace": hwICInsufficientSpace,
       "hwICLogBufferLose": hwICLogBufferLose,
       "hwInfoCenterConformance": hwInfoCenterConformance,
       "hwInfoCenterCompliances": hwInfoCenterCompliances,
       "hwInfoCenterCompliance": hwInfoCenterCompliance,
       "hwInfoCenterGroups": hwInfoCenterGroups,
       "hwInfoCenterGroup": hwInfoCenterGroup,
       "hwInfoCenterTrapGroup": hwInfoCenterTrapGroup}
)
