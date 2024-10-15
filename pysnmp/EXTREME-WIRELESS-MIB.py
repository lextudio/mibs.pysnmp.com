# SNMP MIB module (EXTREME-WIRELESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:20 2024
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

(ClientAuthType,
 ExtremeDeviceId,
 WPACipherSet,
 WPAKeyMgmtSet,
 WirelessRemoteConnectBindingType,
 extremeAP,
 extremeAgent,
 extremeLAC,
 extremeV2Traps) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "ClientAuthType",
    "ExtremeDeviceId",
    "WPACipherSet",
    "WPAKeyMgmtSet",
    "WirelessRemoteConnectBindingType",
    "extremeAP",
    "extremeAgent",
    "extremeLAC",
    "extremeV2Traps")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

extremeWireless = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Dot11Type(Integer32, TextualConvention):
    status = "current"
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
        *(("a", 1),
          ("b", 2),
          ("bg", 4),
          ("g", 3))
    )



class Dot11Speed(Bits, TextualConvention):
    status = "current"


class Dot11AChannel(Bits, TextualConvention):
    status = "current"


class Dot11AuthMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("shared", 1))
    )



class NetworkAuthMode(Integer32, TextualConvention):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("macRadius", 2),
          ("none", 0),
          ("webNetlogin", 1),
          ("wpa2Only", 6),
          ("wpa2PlusWPA", 5),
          ("wpaOnly", 4),
          ("wpaPlusLegacy", 3))
    )



class ExtremeWirelessCountryCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              8,
              12,
              31,
              32,
              36,
              40,
              48,
              51,
              56,
              68,
              76,
              84,
              96,
              100,
              112,
              124,
              152,
              156,
              158,
              170,
              188,
              191,
              196,
              203,
              208,
              214,
              218,
              222,
              233,
              234,
              246,
              250,
              268,
              276,
              300,
              320,
              340,
              344,
              348,
              352,
              356,
              360,
              364,
              368,
              372,
              376,
              380,
              388,
              392,
              393,
              394,
              395,
              398,
              400,
              404,
              408,
              410,
              411,
              414,
              422,
              428,
              434,
              438,
              440,
              442,
              446,
              458,
              484,
              492,
              504,
              512,
              528,
              554,
              558,
              578,
              586,
              591,
              600,
              604,
              608,
              616,
              620,
              630,
              634,
              642,
              643,
              682,
              702,
              703,
              704,
              705,
              710,
              716,
              724,
              752,
              756,
              760,
              764,
              780,
              784,
              788,
              792,
              804,
              807,
              818,
              826,
              840,
              858,
              860,
              862,
              887,
              998,
              999)
        )
    )
    namedValues = NamedValues(
        *(("albania", 8),
          ("algeria", 12),
          ("argentina", 32),
          ("armenia", 51),
          ("australia", 36),
          ("austria", 40),
          ("azerbaijan", 31),
          ("bahrain", 48),
          ("belarus", 112),
          ("belgium", 56),
          ("belize", 84),
          ("bolivia", 68),
          ("brazil", 76),
          ("bruneiDarussalam", 96),
          ("bulgaria", 100),
          ("canada", 124),
          ("chile", 152),
          ("china", 156),
          ("colombia", 170),
          ("costaRica", 188),
          ("croatia", 191),
          ("cyprus", 196),
          ("czech", 203),
          ("denmark", 208),
          ("dominicanRepublic", 214),
          ("ecuador", 218),
          ("egypt", 818),
          ("elSalvador", 222),
          ("estonia", 233),
          ("extremeDefault", 998),
          ("faeroeIslands", 234),
          ("finland", 246),
          ("france", 250),
          ("georgia", 268),
          ("germany", 276),
          ("greece", 300),
          ("guatemala", 320),
          ("honduras", 340),
          ("hongKong", 344),
          ("hungary", 348),
          ("iceland", 352),
          ("india", 356),
          ("indonesia", 360),
          ("iran", 364),
          ("iraq", 368),
          ("ireland", 372),
          ("israel", 376),
          ("italy", 380),
          ("jamaica", 388),
          ("japan", 392),
          ("japan1", 393),
          ("japan2", 394),
          ("japan3", 395),
          ("jordan", 400),
          ("kazakhstan", 398),
          ("kenya", 404),
          ("koreaNorth", 408),
          ("koreaRoc", 410),
          ("koreaRoc2", 411),
          ("kuwait", 414),
          ("latvia", 428),
          ("lebanon", 422),
          ("libya", 434),
          ("liechtenstein", 438),
          ("lithuania", 440),
          ("luxembourg", 442),
          ("macau", 446),
          ("macedonia", 807),
          ("malaysia", 458),
          ("mexico", 484),
          ("monaco", 492),
          ("morocco", 504),
          ("netherlands", 528),
          ("newZealand", 554),
          ("nicaragua", 558),
          ("norway", 578),
          ("oman", 512),
          ("pakistan", 586),
          ("panama", 591),
          ("paraguay", 600),
          ("peru", 604),
          ("philippines", 608),
          ("poland", 616),
          ("portugal", 620),
          ("puertoRico", 630),
          ("qatar", 634),
          ("restOfTheWorld", 0),
          ("romania", 642),
          ("russia", 643),
          ("saudiArabia", 682),
          ("singapore", 702),
          ("slovakia", 703),
          ("slovenia", 705),
          ("southAfrica", 710),
          ("spain", 724),
          ("sweden", 752),
          ("switzerland", 756),
          ("syria", 760),
          ("taiwan", 158),
          ("thailand", 764),
          ("trinidadTYobago", 780),
          ("tunisia", 788),
          ("turkey", 792),
          ("uae", 784),
          ("ukraine", 804),
          ("unitedKingdom", 826),
          ("unitedStates", 840),
          ("unknown", 999),
          ("uruguay", 858),
          ("uzbekistan", 860),
          ("venezuela", 862),
          ("vietNam", 704),
          ("yemen", 887),
          ("zimbabwe", 716))
    )



class ExtremeWirelessAntennaType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detachable15901", 1),
          ("detachable15902", 2),
          ("integrated", 0))
    )



class ExtremeWirelessAntennaLocation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("indoor", 0),
          ("outdoor", 1))
    )



class ExtremeWirelessPhysInterfaceIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class ExtremeWirelessVirtInterfaceIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class ExtremeWirelessChannelAutoSelectStatus(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_ExtremeWirelessPortStatusTable_Object = MibTable
extremeWirelessPortStatusTable = _ExtremeWirelessPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1)
)
if mibBuilder.loadTexts:
    extremeWirelessPortStatusTable.setStatus("current")
_ExtremeWirelessPortStatusEntry_Object = MibTableRow
extremeWirelessPortStatusEntry = _ExtremeWirelessPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1)
)
extremeWirelessPortStatusEntry.setIndexNames(
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessPortIfIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessPortStatusEntry.setStatus("current")
_ExtremeWirelessPortIpAddress_Type = IpAddress
_ExtremeWirelessPortIpAddress_Object = MibTableColumn
extremeWirelessPortIpAddress = _ExtremeWirelessPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 1),
    _ExtremeWirelessPortIpAddress_Type()
)
extremeWirelessPortIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortIpAddress.setStatus("current")
_ExtremeWirelessPortNetmask_Type = IpAddress
_ExtremeWirelessPortNetmask_Object = MibTableColumn
extremeWirelessPortNetmask = _ExtremeWirelessPortNetmask_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 2),
    _ExtremeWirelessPortNetmask_Type()
)
extremeWirelessPortNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortNetmask.setStatus("current")
_ExtremeWirelessPortGateway_Type = IpAddress
_ExtremeWirelessPortGateway_Object = MibTableColumn
extremeWirelessPortGateway = _ExtremeWirelessPortGateway_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 3),
    _ExtremeWirelessPortGateway_Type()
)
extremeWirelessPortGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortGateway.setStatus("current")
_ExtremeWirelessPortManagementIP_Type = IpAddress
_ExtremeWirelessPortManagementIP_Object = MibTableColumn
extremeWirelessPortManagementIP = _ExtremeWirelessPortManagementIP_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 4),
    _ExtremeWirelessPortManagementIP_Type()
)
extremeWirelessPortManagementIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortManagementIP.setStatus("current")
_ExtremeWirelessPortEnableWirelessTraps_Type = TruthValue
_ExtremeWirelessPortEnableWirelessTraps_Object = MibTableColumn
extremeWirelessPortEnableWirelessTraps = _ExtremeWirelessPortEnableWirelessTraps_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 5),
    _ExtremeWirelessPortEnableWirelessTraps_Type()
)
extremeWirelessPortEnableWirelessTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortEnableWirelessTraps.setStatus("current")
_ExtremeWirelessPortLocation_Type = DisplayString
_ExtremeWirelessPortLocation_Object = MibTableColumn
extremeWirelessPortLocation = _ExtremeWirelessPortLocation_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 6),
    _ExtremeWirelessPortLocation_Type()
)
extremeWirelessPortLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortLocation.setStatus("current")
_ExtremeWirelessPortDetectedMaxAge_Type = TimeTicks
_ExtremeWirelessPortDetectedMaxAge_Object = MibTableColumn
extremeWirelessPortDetectedMaxAge = _ExtremeWirelessPortDetectedMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 7),
    _ExtremeWirelessPortDetectedMaxAge_Type()
)
extremeWirelessPortDetectedMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortDetectedMaxAge.setStatus("current")
_ExtremeWirelessPortMgmtVLAN_Type = Integer32
_ExtremeWirelessPortMgmtVLAN_Object = MibTableColumn
extremeWirelessPortMgmtVLAN = _ExtremeWirelessPortMgmtVLAN_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 8),
    _ExtremeWirelessPortMgmtVLAN_Type()
)
extremeWirelessPortMgmtVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessPortMgmtVLAN.setStatus("current")
_ExtremeWirelessPortBootromVersion_Type = DisplayString
_ExtremeWirelessPortBootromVersion_Object = MibTableColumn
extremeWirelessPortBootromVersion = _ExtremeWirelessPortBootromVersion_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 9),
    _ExtremeWirelessPortBootromVersion_Type()
)
extremeWirelessPortBootromVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessPortBootromVersion.setStatus("current")
_ExtremeWirelessPortSWVersion_Type = DisplayString
_ExtremeWirelessPortSWVersion_Object = MibTableColumn
extremeWirelessPortSWVersion = _ExtremeWirelessPortSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 10),
    _ExtremeWirelessPortSWVersion_Type()
)
extremeWirelessPortSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessPortSWVersion.setStatus("current")
_ExtremeWirelessPortSysDescr_Type = DisplayString
_ExtremeWirelessPortSysDescr_Object = MibTableColumn
extremeWirelessPortSysDescr = _ExtremeWirelessPortSysDescr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 11),
    _ExtremeWirelessPortSysDescr_Type()
)
extremeWirelessPortSysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessPortSysDescr.setStatus("current")
_ExtremeWirelessPortManufacturerName_Type = DisplayString
_ExtremeWirelessPortManufacturerName_Object = MibTableColumn
extremeWirelessPortManufacturerName = _ExtremeWirelessPortManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 12),
    _ExtremeWirelessPortManufacturerName_Type()
)
extremeWirelessPortManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessPortManufacturerName.setStatus("current")
_ExtremeWirelessPortProductName_Type = DisplayString
_ExtremeWirelessPortProductName_Object = MibTableColumn
extremeWirelessPortProductName = _ExtremeWirelessPortProductName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 13),
    _ExtremeWirelessPortProductName_Type()
)
extremeWirelessPortProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessPortProductName.setStatus("current")
_ExtremeWirelessPortSerialNumber_Type = DisplayString
_ExtremeWirelessPortSerialNumber_Object = MibTableColumn
extremeWirelessPortSerialNumber = _ExtremeWirelessPortSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 14),
    _ExtremeWirelessPortSerialNumber_Type()
)
extremeWirelessPortSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessPortSerialNumber.setStatus("current")
_ExtremeWirelessPortEdpNeighborId_Type = ExtremeDeviceId
_ExtremeWirelessPortEdpNeighborId_Object = MibTableColumn
extremeWirelessPortEdpNeighborId = _ExtremeWirelessPortEdpNeighborId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 15),
    _ExtremeWirelessPortEdpNeighborId_Type()
)
extremeWirelessPortEdpNeighborId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessPortEdpNeighborId.setStatus("current")
_ExtremeWirelessPortClearCounters_Type = TruthValue
_ExtremeWirelessPortClearCounters_Object = MibTableColumn
extremeWirelessPortClearCounters = _ExtremeWirelessPortClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 16),
    _ExtremeWirelessPortClearCounters_Type()
)
extremeWirelessPortClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortClearCounters.setStatus("current")
_ExtremeWirelessPortClearLog_Type = TruthValue
_ExtremeWirelessPortClearLog_Object = MibTableColumn
extremeWirelessPortClearLog = _ExtremeWirelessPortClearLog_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 17),
    _ExtremeWirelessPortClearLog_Type()
)
extremeWirelessPortClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortClearLog.setStatus("current")
_ExtremeWirelessPortWatchdogReset_Type = TruthValue
_ExtremeWirelessPortWatchdogReset_Object = MibTableColumn
extremeWirelessPortWatchdogReset = _ExtremeWirelessPortWatchdogReset_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 18),
    _ExtremeWirelessPortWatchdogReset_Type()
)
extremeWirelessPortWatchdogReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortWatchdogReset.setStatus("current")
_ExtremeWirelessPortNumPhysInterfaces_Type = Integer32
_ExtremeWirelessPortNumPhysInterfaces_Object = MibTableColumn
extremeWirelessPortNumPhysInterfaces = _ExtremeWirelessPortNumPhysInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 19),
    _ExtremeWirelessPortNumPhysInterfaces_Type()
)
extremeWirelessPortNumPhysInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessPortNumPhysInterfaces.setStatus("current")
_ExtremeWirelessPortHWVersion_Type = DisplayString
_ExtremeWirelessPortHWVersion_Object = MibTableColumn
extremeWirelessPortHWVersion = _ExtremeWirelessPortHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 20),
    _ExtremeWirelessPortHWVersion_Type()
)
extremeWirelessPortHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessPortHWVersion.setStatus("current")
_ExtremeWirelessPortMacAddress_Type = MacAddress
_ExtremeWirelessPortMacAddress_Object = MibTableColumn
extremeWirelessPortMacAddress = _ExtremeWirelessPortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 21),
    _ExtremeWirelessPortMacAddress_Type()
)
extremeWirelessPortMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessPortMacAddress.setStatus("current")
_ExtremeWirelessPortRadiusPortID_Type = DisplayString
_ExtremeWirelessPortRadiusPortID_Object = MibTableColumn
extremeWirelessPortRadiusPortID = _ExtremeWirelessPortRadiusPortID_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 22),
    _ExtremeWirelessPortRadiusPortID_Type()
)
extremeWirelessPortRadiusPortID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortRadiusPortID.setStatus("current")
_ExtremeWirelessPortBootUpTime_Type = TimeTicks
_ExtremeWirelessPortBootUpTime_Object = MibTableColumn
extremeWirelessPortBootUpTime = _ExtremeWirelessPortBootUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 23),
    _ExtremeWirelessPortBootUpTime_Type()
)
extremeWirelessPortBootUpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortBootUpTime.setStatus("current")
_ExtremeWirelessPortCountryCode_Type = ExtremeWirelessCountryCode
_ExtremeWirelessPortCountryCode_Object = MibTableColumn
extremeWirelessPortCountryCode = _ExtremeWirelessPortCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 24),
    _ExtremeWirelessPortCountryCode_Type()
)
extremeWirelessPortCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortCountryCode.setStatus("current")
_ExtremeWirelessPortWallclockTime_Type = Integer32
_ExtremeWirelessPortWallclockTime_Object = MibTableColumn
extremeWirelessPortWallclockTime = _ExtremeWirelessPortWallclockTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 25),
    _ExtremeWirelessPortWallclockTime_Type()
)
extremeWirelessPortWallclockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortWallclockTime.setStatus("current")
_ExtremeWirelessPortPartNumber_Type = DisplayString
_ExtremeWirelessPortPartNumber_Object = MibTableColumn
extremeWirelessPortPartNumber = _ExtremeWirelessPortPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 26),
    _ExtremeWirelessPortPartNumber_Type()
)
extremeWirelessPortPartNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortPartNumber.setStatus("current")
_ExtremeWirelessPortPartRevision_Type = DisplayString
_ExtremeWirelessPortPartRevision_Object = MibTableColumn
extremeWirelessPortPartRevision = _ExtremeWirelessPortPartRevision_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 27),
    _ExtremeWirelessPortPartRevision_Type()
)
extremeWirelessPortPartRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortPartRevision.setStatus("current")
_ExtremeWirelessPortUpTime_Type = TimeTicks
_ExtremeWirelessPortUpTime_Object = MibTableColumn
extremeWirelessPortUpTime = _ExtremeWirelessPortUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 28),
    _ExtremeWirelessPortUpTime_Type()
)
extremeWirelessPortUpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortUpTime.setStatus("current")
_ExtremeWirelessPortStatusAntennaType_Type = ExtremeWirelessAntennaType
_ExtremeWirelessPortStatusAntennaType_Object = MibTableColumn
extremeWirelessPortStatusAntennaType = _ExtremeWirelessPortStatusAntennaType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 29),
    _ExtremeWirelessPortStatusAntennaType_Type()
)
extremeWirelessPortStatusAntennaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortStatusAntennaType.setStatus("current")
_ExtremeWirelessPortStatusAntennaLocation_Type = ExtremeWirelessAntennaLocation
_ExtremeWirelessPortStatusAntennaLocation_Object = MibTableColumn
extremeWirelessPortStatusAntennaLocation = _ExtremeWirelessPortStatusAntennaLocation_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 30),
    _ExtremeWirelessPortStatusAntennaLocation_Type()
)
extremeWirelessPortStatusAntennaLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortStatusAntennaLocation.setStatus("current")
_ExtremeWirelessPortStatusAntenna2point4GHZGain_Type = Integer32
_ExtremeWirelessPortStatusAntenna2point4GHZGain_Object = MibTableColumn
extremeWirelessPortStatusAntenna2point4GHZGain = _ExtremeWirelessPortStatusAntenna2point4GHZGain_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 31),
    _ExtremeWirelessPortStatusAntenna2point4GHZGain_Type()
)
extremeWirelessPortStatusAntenna2point4GHZGain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeWirelessPortStatusAntenna2point4GHZGain.setStatus("current")
_ExtremeWirelessPortStatusAntenna5GHZGain_Type = Integer32
_ExtremeWirelessPortStatusAntenna5GHZGain_Object = MibTableColumn
extremeWirelessPortStatusAntenna5GHZGain = _ExtremeWirelessPortStatusAntenna5GHZGain_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 32),
    _ExtremeWirelessPortStatusAntenna5GHZGain_Type()
)
extremeWirelessPortStatusAntenna5GHZGain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeWirelessPortStatusAntenna5GHZGain.setStatus("current")
_ExtremeWirelessPortPrimaryBootloaderVersion_Type = DisplayString
_ExtremeWirelessPortPrimaryBootloaderVersion_Object = MibTableColumn
extremeWirelessPortPrimaryBootloaderVersion = _ExtremeWirelessPortPrimaryBootloaderVersion_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 33),
    _ExtremeWirelessPortPrimaryBootloaderVersion_Type()
)
extremeWirelessPortPrimaryBootloaderVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessPortPrimaryBootloaderVersion.setStatus("current")
_ExtremeWirelessPortSecondaryBootloaderVersion_Type = DisplayString
_ExtremeWirelessPortSecondaryBootloaderVersion_Object = MibTableColumn
extremeWirelessPortSecondaryBootloaderVersion = _ExtremeWirelessPortSecondaryBootloaderVersion_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 34),
    _ExtremeWirelessPortSecondaryBootloaderVersion_Type()
)
extremeWirelessPortSecondaryBootloaderVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessPortSecondaryBootloaderVersion.setStatus("current")


class _ExtremeWirelessPortCurrentBootloaderInUse_Type(Integer32):
    """Custom type extremeWirelessPortCurrentBootloaderInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_ExtremeWirelessPortCurrentBootloaderInUse_Type.__name__ = "Integer32"
_ExtremeWirelessPortCurrentBootloaderInUse_Object = MibTableColumn
extremeWirelessPortCurrentBootloaderInUse = _ExtremeWirelessPortCurrentBootloaderInUse_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 1, 1, 35),
    _ExtremeWirelessPortCurrentBootloaderInUse_Type()
)
extremeWirelessPortCurrentBootloaderInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessPortCurrentBootloaderInUse.setStatus("current")
_ExtremeWirelessPortLogStatusTable_Object = MibTable
extremeWirelessPortLogStatusTable = _ExtremeWirelessPortLogStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 2)
)
if mibBuilder.loadTexts:
    extremeWirelessPortLogStatusTable.setStatus("current")
_ExtremeWirelessPortLogStatusEntry_Object = MibTableRow
extremeWirelessPortLogStatusEntry = _ExtremeWirelessPortLogStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 2, 1)
)
extremeWirelessPortLogStatusEntry.setIndexNames(
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessPortIfIndex"),
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessPortLogStatusIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessPortLogStatusEntry.setStatus("current")


class _ExtremeWirelessPortLogStatusIndex_Type(Integer32):
    """Custom type extremeWirelessPortLogStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_ExtremeWirelessPortLogStatusIndex_Type.__name__ = "Integer32"
_ExtremeWirelessPortLogStatusIndex_Object = MibTableColumn
extremeWirelessPortLogStatusIndex = _ExtremeWirelessPortLogStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 2, 1, 1),
    _ExtremeWirelessPortLogStatusIndex_Type()
)
extremeWirelessPortLogStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeWirelessPortLogStatusIndex.setStatus("current")
_ExtremeWirelessPortLogStatusDestIp_Type = InetAddress
_ExtremeWirelessPortLogStatusDestIp_Object = MibTableColumn
extremeWirelessPortLogStatusDestIp = _ExtremeWirelessPortLogStatusDestIp_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 2, 1, 2),
    _ExtremeWirelessPortLogStatusDestIp_Type()
)
extremeWirelessPortLogStatusDestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortLogStatusDestIp.setStatus("current")


class _ExtremeWirelessPortLogStatusDestIpType_Type(InetAddressType):
    """Custom type extremeWirelessPortLogStatusDestIpType based on InetAddressType"""


_ExtremeWirelessPortLogStatusDestIpType_Object = MibTableColumn
extremeWirelessPortLogStatusDestIpType = _ExtremeWirelessPortLogStatusDestIpType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 2, 1, 3),
    _ExtremeWirelessPortLogStatusDestIpType_Type()
)
extremeWirelessPortLogStatusDestIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortLogStatusDestIpType.setStatus("current")
_ExtremeWirelessPortLogStatusPort_Type = Integer32
_ExtremeWirelessPortLogStatusPort_Object = MibTableColumn
extremeWirelessPortLogStatusPort = _ExtremeWirelessPortLogStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 2, 1, 4),
    _ExtremeWirelessPortLogStatusPort_Type()
)
extremeWirelessPortLogStatusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortLogStatusPort.setStatus("current")


class _ExtremeWirelessPortLogStatusFacility_Type(Integer32):
    """Custom type extremeWirelessPortLogStatusFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ExtremeWirelessPortLogStatusFacility_Type.__name__ = "Integer32"
_ExtremeWirelessPortLogStatusFacility_Object = MibTableColumn
extremeWirelessPortLogStatusFacility = _ExtremeWirelessPortLogStatusFacility_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 2, 1, 5),
    _ExtremeWirelessPortLogStatusFacility_Type()
)
extremeWirelessPortLogStatusFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortLogStatusFacility.setStatus("current")


class _ExtremeWirelessPortLogStatusSeverity_Type(Integer32):
    """Custom type extremeWirelessPortLogStatusSeverity based on Integer32"""
    defaultValue = 7

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
        *(("critical", 0),
          ("debugData", 7),
          ("debugSummary", 5),
          ("debugVerbose", 6),
          ("error", 1),
          ("info", 4),
          ("notice", 3),
          ("warning", 2))
    )


_ExtremeWirelessPortLogStatusSeverity_Type.__name__ = "Integer32"
_ExtremeWirelessPortLogStatusSeverity_Object = MibTableColumn
extremeWirelessPortLogStatusSeverity = _ExtremeWirelessPortLogStatusSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 2, 1, 6),
    _ExtremeWirelessPortLogStatusSeverity_Type()
)
extremeWirelessPortLogStatusSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortLogStatusSeverity.setStatus("current")
_ExtremeWirelessPortLogStatusStatus_Type = TruthValue
_ExtremeWirelessPortLogStatusStatus_Object = MibTableColumn
extremeWirelessPortLogStatusStatus = _ExtremeWirelessPortLogStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 2, 1, 7),
    _ExtremeWirelessPortLogStatusStatus_Type()
)
extremeWirelessPortLogStatusStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortLogStatusStatus.setStatus("current")
_ExtremeWirelessPortLogTable_Object = MibTable
extremeWirelessPortLogTable = _ExtremeWirelessPortLogTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 3)
)
if mibBuilder.loadTexts:
    extremeWirelessPortLogTable.setStatus("current")
_ExtremeWirelessPortLogEntry_Object = MibTableRow
extremeWirelessPortLogEntry = _ExtremeWirelessPortLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 3, 1)
)
extremeWirelessPortLogEntry.setIndexNames(
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessPortIfIndex"),
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessPortLogIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessPortLogEntry.setStatus("current")


class _ExtremeWirelessPortLogIndex_Type(Integer32):
    """Custom type extremeWirelessPortLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeWirelessPortLogIndex_Type.__name__ = "Integer32"
_ExtremeWirelessPortLogIndex_Object = MibTableColumn
extremeWirelessPortLogIndex = _ExtremeWirelessPortLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 3, 1, 1),
    _ExtremeWirelessPortLogIndex_Type()
)
extremeWirelessPortLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeWirelessPortLogIndex.setStatus("current")
_ExtremeWirelessPortLogMessage_Type = DisplayString
_ExtremeWirelessPortLogMessage_Object = MibTableColumn
extremeWirelessPortLogMessage = _ExtremeWirelessPortLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 3, 1, 2),
    _ExtremeWirelessPortLogMessage_Type()
)
extremeWirelessPortLogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessPortLogMessage.setStatus("current")
_ExtremeWirelessPhysInterfaceCtlTable_Object = MibTable
extremeWirelessPhysInterfaceCtlTable = _ExtremeWirelessPhysInterfaceCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 4)
)
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfaceCtlTable.setStatus("current")
_ExtremeWirelessPhysInterfaceCtlEntry_Object = MibTableRow
extremeWirelessPhysInterfaceCtlEntry = _ExtremeWirelessPhysInterfaceCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 4, 1)
)
extremeWirelessPhysInterfaceCtlEntry.setIndexNames(
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessPhysInterfaceIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfaceCtlEntry.setStatus("current")
_ExtremeWirelessPhysInterfaceIndex_Type = ExtremeWirelessPhysInterfaceIndex
_ExtremeWirelessPhysInterfaceIndex_Object = MibTableColumn
extremeWirelessPhysInterfaceIndex = _ExtremeWirelessPhysInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 4, 1, 1),
    _ExtremeWirelessPhysInterfaceIndex_Type()
)
extremeWirelessPhysInterfaceIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfaceIndex.setStatus("current")


class _ExtremeWirelessPhysInterfacePHYChannel_Type(Integer32):
    """Custom type extremeWirelessPhysInterfacePHYChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_ExtremeWirelessPhysInterfacePHYChannel_Type.__name__ = "Integer32"
_ExtremeWirelessPhysInterfacePHYChannel_Object = MibTableColumn
extremeWirelessPhysInterfacePHYChannel = _ExtremeWirelessPhysInterfacePHYChannel_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 4, 1, 2),
    _ExtremeWirelessPhysInterfacePHYChannel_Type()
)
extremeWirelessPhysInterfacePHYChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfacePHYChannel.setStatus("current")
_ExtremeWirelessPhysInterfaceSpeed_Type = Dot11Speed
_ExtremeWirelessPhysInterfaceSpeed_Object = MibTableColumn
extremeWirelessPhysInterfaceSpeed = _ExtremeWirelessPhysInterfaceSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 4, 1, 3),
    _ExtremeWirelessPhysInterfaceSpeed_Type()
)
extremeWirelessPhysInterfaceSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfaceSpeed.setStatus("current")
_ExtremeWirelessPhysInterfaceNumVirtInterfaces_Type = Integer32
_ExtremeWirelessPhysInterfaceNumVirtInterfaces_Object = MibTableColumn
extremeWirelessPhysInterfaceNumVirtInterfaces = _ExtremeWirelessPhysInterfaceNumVirtInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 4, 1, 4),
    _ExtremeWirelessPhysInterfaceNumVirtInterfaces_Type()
)
extremeWirelessPhysInterfaceNumVirtInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfaceNumVirtInterfaces.setStatus("current")
_ExtremeWirelessPhysInterfaceChannelAutoSelectStatus_Type = ExtremeWirelessChannelAutoSelectStatus
_ExtremeWirelessPhysInterfaceChannelAutoSelectStatus_Object = MibTableColumn
extremeWirelessPhysInterfaceChannelAutoSelectStatus = _ExtremeWirelessPhysInterfaceChannelAutoSelectStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 4, 1, 5),
    _ExtremeWirelessPhysInterfaceChannelAutoSelectStatus_Type()
)
extremeWirelessPhysInterfaceChannelAutoSelectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfaceChannelAutoSelectStatus.setStatus("current")
_ExtremeWirelessPhysInterfaceRadarInterfaceChannelList_Type = Dot11AChannel
_ExtremeWirelessPhysInterfaceRadarInterfaceChannelList_Object = MibTableColumn
extremeWirelessPhysInterfaceRadarInterfaceChannelList = _ExtremeWirelessPhysInterfaceRadarInterfaceChannelList_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 4, 1, 6),
    _ExtremeWirelessPhysInterfaceRadarInterfaceChannelList_Type()
)
extremeWirelessPhysInterfaceRadarInterfaceChannelList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfaceRadarInterfaceChannelList.setStatus("current")
_ExtremeWirelessInterfaceStatusTable_Object = MibTable
extremeWirelessInterfaceStatusTable = _ExtremeWirelessInterfaceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 5)
)
if mibBuilder.loadTexts:
    extremeWirelessInterfaceStatusTable.setStatus("current")
_ExtremeWirelessInterfaceStatusEntry_Object = MibTableRow
extremeWirelessInterfaceStatusEntry = _ExtremeWirelessInterfaceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 5, 1)
)
extremeWirelessInterfaceStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessInterfaceStatusEntry.setStatus("current")
_ExtremeWirelessIntfTotalDetected_Type = Unsigned32
_ExtremeWirelessIntfTotalDetected_Object = MibTableColumn
extremeWirelessIntfTotalDetected = _ExtremeWirelessIntfTotalDetected_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 5, 1, 1),
    _ExtremeWirelessIntfTotalDetected_Type()
)
extremeWirelessIntfTotalDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfTotalDetected.setStatus("current")
_ExtremeWirelessIntfTotalAuthed_Type = Unsigned32
_ExtremeWirelessIntfTotalAuthed_Object = MibTableColumn
extremeWirelessIntfTotalAuthed = _ExtremeWirelessIntfTotalAuthed_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 5, 1, 2),
    _ExtremeWirelessIntfTotalAuthed_Type()
)
extremeWirelessIntfTotalAuthed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfTotalAuthed.setStatus("current")
_ExtremeWirelessIntfTotalAuthFailed_Type = Unsigned32
_ExtremeWirelessIntfTotalAuthFailed_Object = MibTableColumn
extremeWirelessIntfTotalAuthFailed = _ExtremeWirelessIntfTotalAuthFailed_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 5, 1, 3),
    _ExtremeWirelessIntfTotalAuthFailed_Type()
)
extremeWirelessIntfTotalAuthFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfTotalAuthFailed.setStatus("current")
_ExtremeWirelessIntfTotalAssoc_Type = Unsigned32
_ExtremeWirelessIntfTotalAssoc_Object = MibTableColumn
extremeWirelessIntfTotalAssoc = _ExtremeWirelessIntfTotalAssoc_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 5, 1, 4),
    _ExtremeWirelessIntfTotalAssoc_Type()
)
extremeWirelessIntfTotalAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfTotalAssoc.setStatus("current")
_ExtremeWirelessIntfTotalAssocFailed_Type = Unsigned32
_ExtremeWirelessIntfTotalAssocFailed_Object = MibTableColumn
extremeWirelessIntfTotalAssocFailed = _ExtremeWirelessIntfTotalAssocFailed_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 5, 1, 5),
    _ExtremeWirelessIntfTotalAssocFailed_Type()
)
extremeWirelessIntfTotalAssocFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfTotalAssocFailed.setStatus("current")
_ExtremeWirelessIntfRateDetected_Type = Unsigned32
_ExtremeWirelessIntfRateDetected_Object = MibTableColumn
extremeWirelessIntfRateDetected = _ExtremeWirelessIntfRateDetected_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 5, 1, 6),
    _ExtremeWirelessIntfRateDetected_Type()
)
extremeWirelessIntfRateDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfRateDetected.setStatus("current")
_ExtremeWirelessIntfRateAuthed_Type = Unsigned32
_ExtremeWirelessIntfRateAuthed_Object = MibTableColumn
extremeWirelessIntfRateAuthed = _ExtremeWirelessIntfRateAuthed_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 5, 1, 7),
    _ExtremeWirelessIntfRateAuthed_Type()
)
extremeWirelessIntfRateAuthed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfRateAuthed.setStatus("current")
_ExtremeWirelessIntfRateAuthFailed_Type = Unsigned32
_ExtremeWirelessIntfRateAuthFailed_Object = MibTableColumn
extremeWirelessIntfRateAuthFailed = _ExtremeWirelessIntfRateAuthFailed_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 5, 1, 8),
    _ExtremeWirelessIntfRateAuthFailed_Type()
)
extremeWirelessIntfRateAuthFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfRateAuthFailed.setStatus("current")
_ExtremeWirelessIntfRateAssoc_Type = Unsigned32
_ExtremeWirelessIntfRateAssoc_Object = MibTableColumn
extremeWirelessIntfRateAssoc = _ExtremeWirelessIntfRateAssoc_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 5, 1, 9),
    _ExtremeWirelessIntfRateAssoc_Type()
)
extremeWirelessIntfRateAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfRateAssoc.setStatus("current")
_ExtremeWirelessIntfRateAssocFailed_Type = Unsigned32
_ExtremeWirelessIntfRateAssocFailed_Object = MibTableColumn
extremeWirelessIntfRateAssocFailed = _ExtremeWirelessIntfRateAssocFailed_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 5, 1, 10),
    _ExtremeWirelessIntfRateAssocFailed_Type()
)
extremeWirelessIntfRateAssocFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfRateAssocFailed.setStatus("current")
_ExtremeWirelessIntfBlockTime_Type = Unsigned32
_ExtremeWirelessIntfBlockTime_Object = MibTableColumn
extremeWirelessIntfBlockTime = _ExtremeWirelessIntfBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 5, 1, 11),
    _ExtremeWirelessIntfBlockTime_Type()
)
extremeWirelessIntfBlockTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfBlockTime.setStatus("current")
_ExtremeWirelessIntfCurrentDetected_Type = Unsigned32
_ExtremeWirelessIntfCurrentDetected_Object = MibTableColumn
extremeWirelessIntfCurrentDetected = _ExtremeWirelessIntfCurrentDetected_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 5, 1, 12),
    _ExtremeWirelessIntfCurrentDetected_Type()
)
extremeWirelessIntfCurrentDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfCurrentDetected.setStatus("current")
_ExtremeWirelessIntfCurrentAuthed_Type = Unsigned32
_ExtremeWirelessIntfCurrentAuthed_Object = MibTableColumn
extremeWirelessIntfCurrentAuthed = _ExtremeWirelessIntfCurrentAuthed_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 5, 1, 13),
    _ExtremeWirelessIntfCurrentAuthed_Type()
)
extremeWirelessIntfCurrentAuthed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfCurrentAuthed.setStatus("current")
_ExtremeWirelessIntfCurrentAssoc_Type = Unsigned32
_ExtremeWirelessIntfCurrentAssoc_Object = MibTableColumn
extremeWirelessIntfCurrentAssoc = _ExtremeWirelessIntfCurrentAssoc_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 5, 1, 14),
    _ExtremeWirelessIntfCurrentAssoc_Type()
)
extremeWirelessIntfCurrentAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfCurrentAssoc.setStatus("current")
_ExtremeWirelessIntfCurrentForwarding_Type = Unsigned32
_ExtremeWirelessIntfCurrentForwarding_Object = MibTableColumn
extremeWirelessIntfCurrentForwarding = _ExtremeWirelessIntfCurrentForwarding_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 5, 1, 15),
    _ExtremeWirelessIntfCurrentForwarding_Type()
)
extremeWirelessIntfCurrentForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfCurrentForwarding.setStatus("current")
_ExtremeWirelessVirtInterfaceCtlTable_Object = MibTable
extremeWirelessVirtInterfaceCtlTable = _ExtremeWirelessVirtInterfaceCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 6)
)
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceCtlTable.setStatus("current")
_ExtremeWirelessVirtInterfaceCtlEntry_Object = MibTableRow
extremeWirelessVirtInterfaceCtlEntry = _ExtremeWirelessVirtInterfaceCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 6, 1)
)
extremeWirelessVirtInterfaceCtlEntry.setIndexNames(
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessVirtInterfaceIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceCtlEntry.setStatus("current")
_ExtremeWirelessVirtInterfaceIndex_Type = ExtremeWirelessVirtInterfaceIndex
_ExtremeWirelessVirtInterfaceIndex_Object = MibTableColumn
extremeWirelessVirtInterfaceIndex = _ExtremeWirelessVirtInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 6, 1, 1),
    _ExtremeWirelessVirtInterfaceIndex_Type()
)
extremeWirelessVirtInterfaceIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceIndex.setStatus("current")
_ExtremeWirelessVirtInterfaceMacAddress_Type = MacAddress
_ExtremeWirelessVirtInterfaceMacAddress_Object = MibTableColumn
extremeWirelessVirtInterfaceMacAddress = _ExtremeWirelessVirtInterfaceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 6, 1, 2),
    _ExtremeWirelessVirtInterfaceMacAddress_Type()
)
extremeWirelessVirtInterfaceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceMacAddress.setStatus("current")


class _ExtremeWirelessVirtInterfaceMaxClients_Type(Integer32):
    """Custom type extremeWirelessVirtInterfaceMaxClients based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_ExtremeWirelessVirtInterfaceMaxClients_Type.__name__ = "Integer32"
_ExtremeWirelessVirtInterfaceMaxClients_Object = MibTableColumn
extremeWirelessVirtInterfaceMaxClients = _ExtremeWirelessVirtInterfaceMaxClients_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 6, 1, 3),
    _ExtremeWirelessVirtInterfaceMaxClients_Type()
)
extremeWirelessVirtInterfaceMaxClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceMaxClients.setStatus("current")
_ExtremeWirelessVirtInterfaceWirelessBridging_Type = TruthValue
_ExtremeWirelessVirtInterfaceWirelessBridging_Object = MibTableColumn
extremeWirelessVirtInterfaceWirelessBridging = _ExtremeWirelessVirtInterfaceWirelessBridging_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 6, 1, 4),
    _ExtremeWirelessVirtInterfaceWirelessBridging_Type()
)
extremeWirelessVirtInterfaceWirelessBridging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceWirelessBridging.setStatus("current")
_ExtremeWirelessVirtInterfaceLastStateChange_Type = TimeTicks
_ExtremeWirelessVirtInterfaceLastStateChange_Object = MibTableColumn
extremeWirelessVirtInterfaceLastStateChange = _ExtremeWirelessVirtInterfaceLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 6, 1, 5),
    _ExtremeWirelessVirtInterfaceLastStateChange_Type()
)
extremeWirelessVirtInterfaceLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceLastStateChange.setStatus("current")


class _ExtremeWirelessVirtInterfaceState_Type(Integer32):
    """Custom type extremeWirelessVirtInterfaceState based on Integer32"""
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


_ExtremeWirelessVirtInterfaceState_Type.__name__ = "Integer32"
_ExtremeWirelessVirtInterfaceState_Object = MibTableColumn
extremeWirelessVirtInterfaceState = _ExtremeWirelessVirtInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 6, 1, 6),
    _ExtremeWirelessVirtInterfaceState_Type()
)
extremeWirelessVirtInterfaceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceState.setStatus("current")
_ExtremeWirelessVirtInterfaceIappEnabled_Type = TruthValue
_ExtremeWirelessVirtInterfaceIappEnabled_Object = MibTableColumn
extremeWirelessVirtInterfaceIappEnabled = _ExtremeWirelessVirtInterfaceIappEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 6, 1, 7),
    _ExtremeWirelessVirtInterfaceIappEnabled_Type()
)
extremeWirelessVirtInterfaceIappEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceIappEnabled.setStatus("current")
_ExtremeWirelessVirtInterfaceSvpEnabled_Type = TruthValue
_ExtremeWirelessVirtInterfaceSvpEnabled_Object = MibTableColumn
extremeWirelessVirtInterfaceSvpEnabled = _ExtremeWirelessVirtInterfaceSvpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 6, 1, 8),
    _ExtremeWirelessVirtInterfaceSvpEnabled_Type()
)
extremeWirelessVirtInterfaceSvpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceSvpEnabled.setStatus("current")
_ExtremeWirelessVirtInterfaceSecurityCtlTable_Object = MibTable
extremeWirelessVirtInterfaceSecurityCtlTable = _ExtremeWirelessVirtInterfaceSecurityCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 7)
)
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceSecurityCtlTable.setStatus("current")
_ExtremeWirelessVirtInterfaceSecurityCtlEntry_Object = MibTableRow
extremeWirelessVirtInterfaceSecurityCtlEntry = _ExtremeWirelessVirtInterfaceSecurityCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 7, 1)
)
extremeWirelessVirtInterfaceSecurityCtlEntry.setIndexNames(
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessVirtInterfaceIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceSecurityCtlEntry.setStatus("current")
_ExtremeWirelessVirtInterfaceESSName_Type = OctetString
_ExtremeWirelessVirtInterfaceESSName_Object = MibTableColumn
extremeWirelessVirtInterfaceESSName = _ExtremeWirelessVirtInterfaceESSName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 7, 1, 1),
    _ExtremeWirelessVirtInterfaceESSName_Type()
)
extremeWirelessVirtInterfaceESSName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceESSName.setStatus("current")
_ExtremeWirelessVirtInterfaceSSIDInBeacon_Type = TruthValue
_ExtremeWirelessVirtInterfaceSSIDInBeacon_Object = MibTableColumn
extremeWirelessVirtInterfaceSSIDInBeacon = _ExtremeWirelessVirtInterfaceSSIDInBeacon_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 7, 1, 2),
    _ExtremeWirelessVirtInterfaceSSIDInBeacon_Type()
)
extremeWirelessVirtInterfaceSSIDInBeacon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceSSIDInBeacon.setStatus("current")
_ExtremeWirelessVirtInterfaceDot11AuthMode_Type = Dot11AuthMode
_ExtremeWirelessVirtInterfaceDot11AuthMode_Object = MibTableColumn
extremeWirelessVirtInterfaceDot11AuthMode = _ExtremeWirelessVirtInterfaceDot11AuthMode_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 7, 1, 3),
    _ExtremeWirelessVirtInterfaceDot11AuthMode_Type()
)
extremeWirelessVirtInterfaceDot11AuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceDot11AuthMode.setStatus("current")
_ExtremeWirelessVirtInterfaceNetworkAuthMode_Type = NetworkAuthMode
_ExtremeWirelessVirtInterfaceNetworkAuthMode_Object = MibTableColumn
extremeWirelessVirtInterfaceNetworkAuthMode = _ExtremeWirelessVirtInterfaceNetworkAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 7, 1, 4),
    _ExtremeWirelessVirtInterfaceNetworkAuthMode_Type()
)
extremeWirelessVirtInterfaceNetworkAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceNetworkAuthMode.setStatus("current")
_ExtremeWirelessVirtInterfaceDataVlan_Type = Integer32
_ExtremeWirelessVirtInterfaceDataVlan_Object = MibTableColumn
extremeWirelessVirtInterfaceDataVlan = _ExtremeWirelessVirtInterfaceDataVlan_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 7, 1, 5),
    _ExtremeWirelessVirtInterfaceDataVlan_Type()
)
extremeWirelessVirtInterfaceDataVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceDataVlan.setStatus("current")
_ExtremeWirelessVirtInterfaceIgnoreVSAVlan_Type = TruthValue
_ExtremeWirelessVirtInterfaceIgnoreVSAVlan_Object = MibTableColumn
extremeWirelessVirtInterfaceIgnoreVSAVlan = _ExtremeWirelessVirtInterfaceIgnoreVSAVlan_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 7, 1, 6),
    _ExtremeWirelessVirtInterfaceIgnoreVSAVlan_Type()
)
extremeWirelessVirtInterfaceIgnoreVSAVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceIgnoreVSAVlan.setStatus("current")
_ExtremeWirelessVirtInterfaceWEPDefaultKey_Type = Integer32
_ExtremeWirelessVirtInterfaceWEPDefaultKey_Object = MibTableColumn
extremeWirelessVirtInterfaceWEPDefaultKey = _ExtremeWirelessVirtInterfaceWEPDefaultKey_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 7, 1, 7),
    _ExtremeWirelessVirtInterfaceWEPDefaultKey_Type()
)
extremeWirelessVirtInterfaceWEPDefaultKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceWEPDefaultKey.setStatus("current")


class _ExtremeWirelessVirtInterfaceEncryptionLength_Type(Integer32):
    """Custom type extremeWirelessVirtInterfaceEncryptionLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("onetwentyeight", 128),
          ("sixtyfour", 64))
    )


_ExtremeWirelessVirtInterfaceEncryptionLength_Type.__name__ = "Integer32"
_ExtremeWirelessVirtInterfaceEncryptionLength_Object = MibTableColumn
extremeWirelessVirtInterfaceEncryptionLength = _ExtremeWirelessVirtInterfaceEncryptionLength_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 7, 1, 8),
    _ExtremeWirelessVirtInterfaceEncryptionLength_Type()
)
extremeWirelessVirtInterfaceEncryptionLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceEncryptionLength.setStatus("current")
_ExtremeWirelessVirtInterfaceDot1xCtlTable_Object = MibTable
extremeWirelessVirtInterfaceDot1xCtlTable = _ExtremeWirelessVirtInterfaceDot1xCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 8)
)
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceDot1xCtlTable.setStatus("current")
_ExtremeWirelessVirtInterfaceDot1xCtlEntry_Object = MibTableRow
extremeWirelessVirtInterfaceDot1xCtlEntry = _ExtremeWirelessVirtInterfaceDot1xCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 8, 1)
)
extremeWirelessVirtInterfaceDot1xCtlEntry.setIndexNames(
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessVirtInterfaceIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceDot1xCtlEntry.setStatus("current")
_ExtremeWirelessVirtInterfaceKeyMgmtSuite_Type = WPAKeyMgmtSet
_ExtremeWirelessVirtInterfaceKeyMgmtSuite_Object = MibTableColumn
extremeWirelessVirtInterfaceKeyMgmtSuite = _ExtremeWirelessVirtInterfaceKeyMgmtSuite_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 8, 1, 1),
    _ExtremeWirelessVirtInterfaceKeyMgmtSuite_Type()
)
extremeWirelessVirtInterfaceKeyMgmtSuite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceKeyMgmtSuite.setStatus("current")
_ExtremeWirelessVirtInterfaceMcastCipherSuite_Type = WPACipherSet
_ExtremeWirelessVirtInterfaceMcastCipherSuite_Object = MibTableColumn
extremeWirelessVirtInterfaceMcastCipherSuite = _ExtremeWirelessVirtInterfaceMcastCipherSuite_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 8, 1, 2),
    _ExtremeWirelessVirtInterfaceMcastCipherSuite_Type()
)
extremeWirelessVirtInterfaceMcastCipherSuite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceMcastCipherSuite.setStatus("current")


class _ExtremeWirelessVirtInterfaceDot1xPSKValue_Type(OctetString):
    """Custom type extremeWirelessVirtInterfaceDot1xPSKValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_ExtremeWirelessVirtInterfaceDot1xPSKValue_Type.__name__ = "OctetString"
_ExtremeWirelessVirtInterfaceDot1xPSKValue_Object = MibTableColumn
extremeWirelessVirtInterfaceDot1xPSKValue = _ExtremeWirelessVirtInterfaceDot1xPSKValue_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 8, 1, 3),
    _ExtremeWirelessVirtInterfaceDot1xPSKValue_Type()
)
extremeWirelessVirtInterfaceDot1xPSKValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceDot1xPSKValue.setStatus("current")
_ExtremeWirelessVirtInterfaceDot1xPSKPassPhrase_Type = DisplayString
_ExtremeWirelessVirtInterfaceDot1xPSKPassPhrase_Object = MibTableColumn
extremeWirelessVirtInterfaceDot1xPSKPassPhrase = _ExtremeWirelessVirtInterfaceDot1xPSKPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 8, 1, 4),
    _ExtremeWirelessVirtInterfaceDot1xPSKPassPhrase_Type()
)
extremeWirelessVirtInterfaceDot1xPSKPassPhrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceDot1xPSKPassPhrase.setStatus("current")
_ExtremeWirelessVirtInterfaceDot1xReAuthPeriod_Type = Integer32
_ExtremeWirelessVirtInterfaceDot1xReAuthPeriod_Object = MibTableColumn
extremeWirelessVirtInterfaceDot1xReAuthPeriod = _ExtremeWirelessVirtInterfaceDot1xReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 8, 1, 5),
    _ExtremeWirelessVirtInterfaceDot1xReAuthPeriod_Type()
)
extremeWirelessVirtInterfaceDot1xReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceDot1xReAuthPeriod.setStatus("current")


class _ExtremeWirelessVirtInterfaceGroupUpdateTimeOut_Type(Unsigned32):
    """Custom type extremeWirelessVirtInterfaceGroupUpdateTimeOut based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_ExtremeWirelessVirtInterfaceGroupUpdateTimeOut_Type.__name__ = "Unsigned32"
_ExtremeWirelessVirtInterfaceGroupUpdateTimeOut_Object = MibTableColumn
extremeWirelessVirtInterfaceGroupUpdateTimeOut = _ExtremeWirelessVirtInterfaceGroupUpdateTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 8, 1, 6),
    _ExtremeWirelessVirtInterfaceGroupUpdateTimeOut_Type()
)
extremeWirelessVirtInterfaceGroupUpdateTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceGroupUpdateTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceGroupUpdateTimeOut.setUnits("minutes")


class _ExtremeWirelessVirtInterfacePairwiseUpdateTimeOut_Type(Unsigned32):
    """Custom type extremeWirelessVirtInterfacePairwiseUpdateTimeOut based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_ExtremeWirelessVirtInterfacePairwiseUpdateTimeOut_Type.__name__ = "Unsigned32"
_ExtremeWirelessVirtInterfacePairwiseUpdateTimeOut_Object = MibTableColumn
extremeWirelessVirtInterfacePairwiseUpdateTimeOut = _ExtremeWirelessVirtInterfacePairwiseUpdateTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 8, 1, 7),
    _ExtremeWirelessVirtInterfacePairwiseUpdateTimeOut_Type()
)
extremeWirelessVirtInterfacePairwiseUpdateTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfacePairwiseUpdateTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfacePairwiseUpdateTimeOut.setUnits("minutes")
_ExtremeWirelessVirtInterfaceDot11iPreauthEnable_Type = TruthValue
_ExtremeWirelessVirtInterfaceDot11iPreauthEnable_Object = MibTableColumn
extremeWirelessVirtInterfaceDot11iPreauthEnable = _ExtremeWirelessVirtInterfaceDot11iPreauthEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 8, 1, 8),
    _ExtremeWirelessVirtInterfaceDot11iPreauthEnable_Type()
)
extremeWirelessVirtInterfaceDot11iPreauthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceDot11iPreauthEnable.setStatus("current")
_ExtremeWirelessVirtInterfaceWEPKeyTable_Object = MibTable
extremeWirelessVirtInterfaceWEPKeyTable = _ExtremeWirelessVirtInterfaceWEPKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 9)
)
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceWEPKeyTable.setStatus("current")
_ExtremeWirelessVirtInterfaceWEPKeyEntry_Object = MibTableRow
extremeWirelessVirtInterfaceWEPKeyEntry = _ExtremeWirelessVirtInterfaceWEPKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 9, 1)
)
extremeWirelessVirtInterfaceWEPKeyEntry.setIndexNames(
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessVirtInterfaceIndex"),
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessVirtInterfaceWEPKeyIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceWEPKeyEntry.setStatus("current")


class _ExtremeWirelessVirtInterfaceWEPKeyIndex_Type(Integer32):
    """Custom type extremeWirelessVirtInterfaceWEPKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ExtremeWirelessVirtInterfaceWEPKeyIndex_Type.__name__ = "Integer32"
_ExtremeWirelessVirtInterfaceWEPKeyIndex_Object = MibTableColumn
extremeWirelessVirtInterfaceWEPKeyIndex = _ExtremeWirelessVirtInterfaceWEPKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 9, 1, 1),
    _ExtremeWirelessVirtInterfaceWEPKeyIndex_Type()
)
extremeWirelessVirtInterfaceWEPKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceWEPKeyIndex.setStatus("current")


class _ExtremeWirelessVirtInterfaceWEPKey_Type(OctetString):
    """Custom type extremeWirelessVirtInterfaceWEPKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_ExtremeWirelessVirtInterfaceWEPKey_Type.__name__ = "OctetString"
_ExtremeWirelessVirtInterfaceWEPKey_Object = MibTableColumn
extremeWirelessVirtInterfaceWEPKey = _ExtremeWirelessVirtInterfaceWEPKey_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 9, 1, 2),
    _ExtremeWirelessVirtInterfaceWEPKey_Type()
)
extremeWirelessVirtInterfaceWEPKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceWEPKey.setStatus("current")
_ExtremeWirelessVirtInterfaceWEPKeyStatus_Type = TruthValue
_ExtremeWirelessVirtInterfaceWEPKeyStatus_Object = MibTableColumn
extremeWirelessVirtInterfaceWEPKeyStatus = _ExtremeWirelessVirtInterfaceWEPKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 9, 1, 3),
    _ExtremeWirelessVirtInterfaceWEPKeyStatus_Type()
)
extremeWirelessVirtInterfaceWEPKeyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceWEPKeyStatus.setStatus("current")
_ExtremeWirelessPhysInterfaceRFCtlTable_Object = MibTable
extremeWirelessPhysInterfaceRFCtlTable = _ExtremeWirelessPhysInterfaceRFCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 10)
)
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfaceRFCtlTable.setStatus("current")
_ExtremeWirelessPhysInterfaceRFCtlEntry_Object = MibTableRow
extremeWirelessPhysInterfaceRFCtlEntry = _ExtremeWirelessPhysInterfaceRFCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 10, 1)
)
extremeWirelessPhysInterfaceRFCtlEntry.setIndexNames(
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessPhysInterfaceIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfaceRFCtlEntry.setStatus("current")
_ExtremeWirelessPhysInterfaceBeaconPeriod_Type = Integer32
_ExtremeWirelessPhysInterfaceBeaconPeriod_Object = MibTableColumn
extremeWirelessPhysInterfaceBeaconPeriod = _ExtremeWirelessPhysInterfaceBeaconPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 10, 1, 1),
    _ExtremeWirelessPhysInterfaceBeaconPeriod_Type()
)
extremeWirelessPhysInterfaceBeaconPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfaceBeaconPeriod.setStatus("current")


class _ExtremeWirelessPhysInterfaceTxPowerLevel_Type(Integer32):
    """Custom type extremeWirelessPhysInterfaceTxPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ExtremeWirelessPhysInterfaceTxPowerLevel_Type.__name__ = "Integer32"
_ExtremeWirelessPhysInterfaceTxPowerLevel_Object = MibTableColumn
extremeWirelessPhysInterfaceTxPowerLevel = _ExtremeWirelessPhysInterfaceTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 10, 1, 2),
    _ExtremeWirelessPhysInterfaceTxPowerLevel_Type()
)
extremeWirelessPhysInterfaceTxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfaceTxPowerLevel.setStatus("current")
_ExtremeWirelessPhysInterfaceDTIMPeriod_Type = Integer32
_ExtremeWirelessPhysInterfaceDTIMPeriod_Object = MibTableColumn
extremeWirelessPhysInterfaceDTIMPeriod = _ExtremeWirelessPhysInterfaceDTIMPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 10, 1, 3),
    _ExtremeWirelessPhysInterfaceDTIMPeriod_Type()
)
extremeWirelessPhysInterfaceDTIMPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfaceDTIMPeriod.setStatus("current")
_ExtremeWirelessPhysInterfaceFragLength_Type = Integer32
_ExtremeWirelessPhysInterfaceFragLength_Object = MibTableColumn
extremeWirelessPhysInterfaceFragLength = _ExtremeWirelessPhysInterfaceFragLength_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 10, 1, 4),
    _ExtremeWirelessPhysInterfaceFragLength_Type()
)
extremeWirelessPhysInterfaceFragLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfaceFragLength.setStatus("current")


class _ExtremeWirelessPhysInterfaceLongRetry_Type(Integer32):
    """Custom type extremeWirelessPhysInterfaceLongRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ExtremeWirelessPhysInterfaceLongRetry_Type.__name__ = "Integer32"
_ExtremeWirelessPhysInterfaceLongRetry_Object = MibTableColumn
extremeWirelessPhysInterfaceLongRetry = _ExtremeWirelessPhysInterfaceLongRetry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 10, 1, 5),
    _ExtremeWirelessPhysInterfaceLongRetry_Type()
)
extremeWirelessPhysInterfaceLongRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfaceLongRetry.setStatus("current")


class _ExtremeWirelessPhysInterfaceShortRetry_Type(Integer32):
    """Custom type extremeWirelessPhysInterfaceShortRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ExtremeWirelessPhysInterfaceShortRetry_Type.__name__ = "Integer32"
_ExtremeWirelessPhysInterfaceShortRetry_Object = MibTableColumn
extremeWirelessPhysInterfaceShortRetry = _ExtremeWirelessPhysInterfaceShortRetry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 10, 1, 6),
    _ExtremeWirelessPhysInterfaceShortRetry_Type()
)
extremeWirelessPhysInterfaceShortRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfaceShortRetry.setStatus("current")
_ExtremeWirelessPhysInterfaceRTSThreshold_Type = Integer32
_ExtremeWirelessPhysInterfaceRTSThreshold_Object = MibTableColumn
extremeWirelessPhysInterfaceRTSThreshold = _ExtremeWirelessPhysInterfaceRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 10, 1, 7),
    _ExtremeWirelessPhysInterfaceRTSThreshold_Type()
)
extremeWirelessPhysInterfaceRTSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfaceRTSThreshold.setStatus("current")
_ExtremeWirelessPhysInterfaceSupportedDataRatesRxValue_Type = Dot11Speed
_ExtremeWirelessPhysInterfaceSupportedDataRatesRxValue_Object = MibTableColumn
extremeWirelessPhysInterfaceSupportedDataRatesRxValue = _ExtremeWirelessPhysInterfaceSupportedDataRatesRxValue_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 10, 1, 8),
    _ExtremeWirelessPhysInterfaceSupportedDataRatesRxValue_Type()
)
extremeWirelessPhysInterfaceSupportedDataRatesRxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfaceSupportedDataRatesRxValue.setStatus("current")
_ExtremeWirelessPhysInterfaceSupportedDataRatesTxValue_Type = Dot11Speed
_ExtremeWirelessPhysInterfaceSupportedDataRatesTxValue_Object = MibTableColumn
extremeWirelessPhysInterfaceSupportedDataRatesTxValue = _ExtremeWirelessPhysInterfaceSupportedDataRatesTxValue_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 10, 1, 9),
    _ExtremeWirelessPhysInterfaceSupportedDataRatesTxValue_Type()
)
extremeWirelessPhysInterfaceSupportedDataRatesTxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfaceSupportedDataRatesTxValue.setStatus("current")
_ExtremeWirelessPhysInterfacePHYType_Type = Dot11Type
_ExtremeWirelessPhysInterfacePHYType_Object = MibTableColumn
extremeWirelessPhysInterfacePHYType = _ExtremeWirelessPhysInterfacePHYType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 10, 1, 10),
    _ExtremeWirelessPhysInterfacePHYType_Type()
)
extremeWirelessPhysInterfacePHYType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfacePHYType.setStatus("current")


class _ExtremeWirelessPhysInterfacePHYSupportedTypes_Type(Bits):
    """Custom type extremeWirelessPhysInterfacePHYSupportedTypes based on Bits"""
    namedValues = NamedValues(
        *(("asupported", 1),
          ("bsupported", 0),
          ("gsupported", 2))
    )

_ExtremeWirelessPhysInterfacePHYSupportedTypes_Type.__name__ = "Bits"
_ExtremeWirelessPhysInterfacePHYSupportedTypes_Object = MibTableColumn
extremeWirelessPhysInterfacePHYSupportedTypes = _ExtremeWirelessPhysInterfacePHYSupportedTypes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 10, 1, 11),
    _ExtremeWirelessPhysInterfacePHYSupportedTypes_Type()
)
extremeWirelessPhysInterfacePHYSupportedTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfacePHYSupportedTypes.setStatus("current")


class _ExtremeWirelessPhysInterfacePreamble_Type(Integer32):
    """Custom type extremeWirelessPhysInterfacePreamble based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("long", 1),
          ("short", 0))
    )


_ExtremeWirelessPhysInterfacePreamble_Type.__name__ = "Integer32"
_ExtremeWirelessPhysInterfacePreamble_Object = MibTableColumn
extremeWirelessPhysInterfacePreamble = _ExtremeWirelessPhysInterfacePreamble_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 10, 1, 12),
    _ExtremeWirelessPhysInterfacePreamble_Type()
)
extremeWirelessPhysInterfacePreamble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfacePreamble.setStatus("current")
_ExtremeWirelessPhysInterfaceAbsTxPowerLevel_Type = Integer32
_ExtremeWirelessPhysInterfaceAbsTxPowerLevel_Object = MibTableColumn
extremeWirelessPhysInterfaceAbsTxPowerLevel = _ExtremeWirelessPhysInterfaceAbsTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 10, 1, 13),
    _ExtremeWirelessPhysInterfaceAbsTxPowerLevel_Type()
)
extremeWirelessPhysInterfaceAbsTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfaceAbsTxPowerLevel.setStatus("current")
_ExtremeWirelessClientTable_Object = MibTable
extremeWirelessClientTable = _ExtremeWirelessClientTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 11)
)
if mibBuilder.loadTexts:
    extremeWirelessClientTable.setStatus("current")
_ExtremeWirelessClientEntry_Object = MibTableRow
extremeWirelessClientEntry = _ExtremeWirelessClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 11, 1)
)
extremeWirelessClientEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessClientID"),
)
if mibBuilder.loadTexts:
    extremeWirelessClientEntry.setStatus("current")
_ExtremeWirelessClientID_Type = MacAddress
_ExtremeWirelessClientID_Object = MibTableColumn
extremeWirelessClientID = _ExtremeWirelessClientID_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 11, 1, 1),
    _ExtremeWirelessClientID_Type()
)
extremeWirelessClientID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientID.setStatus("current")


class _ExtremeWirelessClientState_Type(Integer32):
    """Custom type extremeWirelessClientState based on Integer32"""
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
        *(("associated", 3),
          ("authenticated", 2),
          ("data-forwarding", 4),
          ("detected", 1))
    )


_ExtremeWirelessClientState_Type.__name__ = "Integer32"
_ExtremeWirelessClientState_Object = MibTableColumn
extremeWirelessClientState = _ExtremeWirelessClientState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 11, 1, 2),
    _ExtremeWirelessClientState_Type()
)
extremeWirelessClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientState.setStatus("current")
_ExtremeWirelessClientEncryption_Type = WPACipherSet
_ExtremeWirelessClientEncryption_Object = MibTableColumn
extremeWirelessClientEncryption = _ExtremeWirelessClientEncryption_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 11, 1, 3),
    _ExtremeWirelessClientEncryption_Type()
)
extremeWirelessClientEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientEncryption.setStatus("current")


class _ExtremeWirelessClientSignalStrength_Type(Integer32):
    """Custom type extremeWirelessClientSignalStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ExtremeWirelessClientSignalStrength_Type.__name__ = "Integer32"
_ExtremeWirelessClientSignalStrength_Object = MibTableColumn
extremeWirelessClientSignalStrength = _ExtremeWirelessClientSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 11, 1, 4),
    _ExtremeWirelessClientSignalStrength_Type()
)
extremeWirelessClientSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSignalStrength.setStatus("current")


class _ExtremeWirelessClientLinkQuality_Type(Integer32):
    """Custom type extremeWirelessClientLinkQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ExtremeWirelessClientLinkQuality_Type.__name__ = "Integer32"
_ExtremeWirelessClientLinkQuality_Object = MibTableColumn
extremeWirelessClientLinkQuality = _ExtremeWirelessClientLinkQuality_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 11, 1, 5),
    _ExtremeWirelessClientLinkQuality_Type()
)
extremeWirelessClientLinkQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientLinkQuality.setStatus("current")
_ExtremeWirelessClientVLAN_Type = Integer32
_ExtremeWirelessClientVLAN_Object = MibTableColumn
extremeWirelessClientVLAN = _ExtremeWirelessClientVLAN_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 11, 1, 6),
    _ExtremeWirelessClientVLAN_Type()
)
extremeWirelessClientVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientVLAN.setStatus("current")
_ExtremeWirelessClientPriority_Type = Integer32
_ExtremeWirelessClientPriority_Object = MibTableColumn
extremeWirelessClientPriority = _ExtremeWirelessClientPriority_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 11, 1, 7),
    _ExtremeWirelessClientPriority_Type()
)
extremeWirelessClientPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientPriority.setStatus("current")
_ExtremeWirelessClientAuthType_Type = ClientAuthType
_ExtremeWirelessClientAuthType_Object = MibTableColumn
extremeWirelessClientAuthType = _ExtremeWirelessClientAuthType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 11, 1, 8),
    _ExtremeWirelessClientAuthType_Type()
)
extremeWirelessClientAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAuthType.setStatus("current")
_ExtremeWirelessClientLastStateChangeTime_Type = TimeTicks
_ExtremeWirelessClientLastStateChangeTime_Object = MibTableColumn
extremeWirelessClientLastStateChangeTime = _ExtremeWirelessClientLastStateChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 11, 1, 9),
    _ExtremeWirelessClientLastStateChangeTime_Type()
)
extremeWirelessClientLastStateChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientLastStateChangeTime.setStatus("current")
_ExtremeWirelessClientTxFrames_Type = Counter32
_ExtremeWirelessClientTxFrames_Object = MibTableColumn
extremeWirelessClientTxFrames = _ExtremeWirelessClientTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 11, 1, 10),
    _ExtremeWirelessClientTxFrames_Type()
)
extremeWirelessClientTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientTxFrames.setStatus("current")
_ExtremeWirelessClientRxFrames_Type = Counter32
_ExtremeWirelessClientRxFrames_Object = MibTableColumn
extremeWirelessClientRxFrames = _ExtremeWirelessClientRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 11, 1, 11),
    _ExtremeWirelessClientRxFrames_Type()
)
extremeWirelessClientRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientRxFrames.setStatus("current")
_ExtremeWirelessClientTxBytes_Type = Counter64
_ExtremeWirelessClientTxBytes_Object = MibTableColumn
extremeWirelessClientTxBytes = _ExtremeWirelessClientTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 11, 1, 12),
    _ExtremeWirelessClientTxBytes_Type()
)
extremeWirelessClientTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientTxBytes.setStatus("current")
_ExtremeWirelessClientRxBytes_Type = Counter64
_ExtremeWirelessClientRxBytes_Object = MibTableColumn
extremeWirelessClientRxBytes = _ExtremeWirelessClientRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 11, 1, 13),
    _ExtremeWirelessClientRxBytes_Type()
)
extremeWirelessClientRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientRxBytes.setStatus("current")


class _ExtremeWirelessClientLastPacketType_Type(Integer32):
    """Custom type extremeWirelessClientLastPacketType based on Integer32"""
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
        *(("association", 5),
          ("authentication", 7),
          ("data", 0),
          ("deauthentication", 4),
          ("disassociation", 3),
          ("probeRequest", 2),
          ("psPoll", 1),
          ("reassociation", 6))
    )


_ExtremeWirelessClientLastPacketType_Type.__name__ = "Integer32"
_ExtremeWirelessClientLastPacketType_Object = MibTableColumn
extremeWirelessClientLastPacketType = _ExtremeWirelessClientLastPacketType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 11, 1, 14),
    _ExtremeWirelessClientLastPacketType_Type()
)
extremeWirelessClientLastPacketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientLastPacketType.setStatus("current")
_ExtremeWirelessClientSSID_Type = OctetString
_ExtremeWirelessClientSSID_Object = MibTableColumn
extremeWirelessClientSSID = _ExtremeWirelessClientSSID_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 11, 1, 15),
    _ExtremeWirelessClientSSID_Type()
)
extremeWirelessClientSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSSID.setStatus("current")
_ExtremeWirelessClientStatus_Type = RowStatus
_ExtremeWirelessClientStatus_Object = MibTableColumn
extremeWirelessClientStatus = _ExtremeWirelessClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 11, 1, 16),
    _ExtremeWirelessClientStatus_Type()
)
extremeWirelessClientStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessClientStatus.setStatus("current")
_ExtremeWirelessClientIP_Type = IpAddress
_ExtremeWirelessClientIP_Object = MibTableColumn
extremeWirelessClientIP = _ExtremeWirelessClientIP_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 11, 1, 17),
    _ExtremeWirelessClientIP_Type()
)
extremeWirelessClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientIP.setStatus("current")
_ExtremeWirelessClientUsername_Type = DisplayString
_ExtremeWirelessClientUsername_Object = MibTableColumn
extremeWirelessClientUsername = _ExtremeWirelessClientUsername_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 11, 1, 18),
    _ExtremeWirelessClientUsername_Type()
)
extremeWirelessClientUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientUsername.setStatus("current")
_ExtremeWirelessClientDecryptionFailures_Type = Counter32
_ExtremeWirelessClientDecryptionFailures_Object = MibTableColumn
extremeWirelessClientDecryptionFailures = _ExtremeWirelessClientDecryptionFailures_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 11, 1, 19),
    _ExtremeWirelessClientDecryptionFailures_Type()
)
extremeWirelessClientDecryptionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDecryptionFailures.setStatus("current")
_ExtremeWirelessClientMICFailures_Type = Counter32
_ExtremeWirelessClientMICFailures_Object = MibTableColumn
extremeWirelessClientMICFailures = _ExtremeWirelessClientMICFailures_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 11, 1, 20),
    _ExtremeWirelessClientMICFailures_Type()
)
extremeWirelessClientMICFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientMICFailures.setStatus("current")
_ExtremeAPAuthServerTable_Object = MibTable
extremeAPAuthServerTable = _ExtremeAPAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 12)
)
if mibBuilder.loadTexts:
    extremeAPAuthServerTable.setStatus("current")
_ExtremeAPAuthServerEntry_Object = MibTableRow
extremeAPAuthServerEntry = _ExtremeAPAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 12, 1)
)
extremeAPAuthServerEntry.setIndexNames(
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessPortIfIndex"),
    (0, "EXTREME-WIRELESS-MIB", "extremeAPAuthServerIndex"),
)
if mibBuilder.loadTexts:
    extremeAPAuthServerEntry.setStatus("current")


class _ExtremeAPAuthServerIndex_Type(Integer32):
    """Custom type extremeAPAuthServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ExtremeAPAuthServerIndex_Type.__name__ = "Integer32"
_ExtremeAPAuthServerIndex_Object = MibTableColumn
extremeAPAuthServerIndex = _ExtremeAPAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 12, 1, 1),
    _ExtremeAPAuthServerIndex_Type()
)
extremeAPAuthServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeAPAuthServerIndex.setStatus("current")


class _ExtremeAPAuthServerAddressType_Type(InetAddressType):
    """Custom type extremeAPAuthServerAddressType based on InetAddressType"""


_ExtremeAPAuthServerAddressType_Object = MibTableColumn
extremeAPAuthServerAddressType = _ExtremeAPAuthServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 12, 1, 2),
    _ExtremeAPAuthServerAddressType_Type()
)
extremeAPAuthServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeAPAuthServerAddressType.setStatus("current")
_ExtremeAPAuthServerAddress_Type = InetAddress
_ExtremeAPAuthServerAddress_Object = MibTableColumn
extremeAPAuthServerAddress = _ExtremeAPAuthServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 12, 1, 3),
    _ExtremeAPAuthServerAddress_Type()
)
extremeAPAuthServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeAPAuthServerAddress.setStatus("current")


class _ExtremeAPAuthServerPort_Type(Integer32):
    """Custom type extremeAPAuthServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeAPAuthServerPort_Type.__name__ = "Integer32"
_ExtremeAPAuthServerPort_Object = MibTableColumn
extremeAPAuthServerPort = _ExtremeAPAuthServerPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 12, 1, 4),
    _ExtremeAPAuthServerPort_Type()
)
extremeAPAuthServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeAPAuthServerPort.setStatus("current")
_ExtremeAPAuthServerSecret_Type = OctetString
_ExtremeAPAuthServerSecret_Object = MibTableColumn
extremeAPAuthServerSecret = _ExtremeAPAuthServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 12, 1, 5),
    _ExtremeAPAuthServerSecret_Type()
)
extremeAPAuthServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeAPAuthServerSecret.setStatus("current")
_ExtremeAPAuthServerReTransmit_Type = Integer32
_ExtremeAPAuthServerReTransmit_Object = MibTableColumn
extremeAPAuthServerReTransmit = _ExtremeAPAuthServerReTransmit_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 12, 1, 6),
    _ExtremeAPAuthServerReTransmit_Type()
)
extremeAPAuthServerReTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeAPAuthServerReTransmit.setStatus("current")
_ExtremeAPAuthServerStatus_Type = TruthValue
_ExtremeAPAuthServerStatus_Object = MibTableColumn
extremeAPAuthServerStatus = _ExtremeAPAuthServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 12, 1, 7),
    _ExtremeAPAuthServerStatus_Type()
)
extremeAPAuthServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeAPAuthServerStatus.setStatus("current")
_ExtremeWirelessScanCfgTable_Object = MibTable
extremeWirelessScanCfgTable = _ExtremeWirelessScanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 24)
)
if mibBuilder.loadTexts:
    extremeWirelessScanCfgTable.setStatus("current")
_ExtremeWirelessScanCfgEntry_Object = MibTableRow
extremeWirelessScanCfgEntry = _ExtremeWirelessScanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 24, 1)
)
extremeWirelessScanCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessScanCfgEntry.setStatus("current")


class _ExtremeWirelessScanEnable_Type(TruthValue):
    """Custom type extremeWirelessScanEnable based on TruthValue"""


_ExtremeWirelessScanEnable_Object = MibTableColumn
extremeWirelessScanEnable = _ExtremeWirelessScanEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 24, 1, 1),
    _ExtremeWirelessScanEnable_Type()
)
extremeWirelessScanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessScanEnable.setStatus("current")


class _ExtremeWirelessScanSendProbe_Type(TruthValue):
    """Custom type extremeWirelessScanSendProbe based on TruthValue"""


_ExtremeWirelessScanSendProbe_Object = MibTableColumn
extremeWirelessScanSendProbe = _ExtremeWirelessScanSendProbe_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 24, 1, 2),
    _ExtremeWirelessScanSendProbe_Type()
)
extremeWirelessScanSendProbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessScanSendProbe.setStatus("current")


class _ExtremeWirelessScanProbeInterval_Type(Unsigned32):
    """Custom type extremeWirelessScanProbeInterval based on Unsigned32"""
    defaultValue = 100


_ExtremeWirelessScanProbeInterval_Object = MibTableColumn
extremeWirelessScanProbeInterval = _ExtremeWirelessScanProbeInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 24, 1, 3),
    _ExtremeWirelessScanProbeInterval_Type()
)
extremeWirelessScanProbeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessScanProbeInterval.setStatus("current")
if mibBuilder.loadTexts:
    extremeWirelessScanProbeInterval.setUnits("milliseconds")


class _ExtremeWirelessScanResultTableSize_Type(Unsigned32):
    """Custom type extremeWirelessScanResultTableSize based on Unsigned32"""
    defaultValue = 1024


_ExtremeWirelessScanResultTableSize_Object = MibTableColumn
extremeWirelessScanResultTableSize = _ExtremeWirelessScanResultTableSize_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 24, 1, 4),
    _ExtremeWirelessScanResultTableSize_Type()
)
extremeWirelessScanResultTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessScanResultTableSize.setStatus("current")


class _ExtremeWirelessScanResultTimeout_Type(Unsigned32):
    """Custom type extremeWirelessScanResultTimeout based on Unsigned32"""
    defaultValue = 3600


_ExtremeWirelessScanResultTimeout_Object = MibTableColumn
extremeWirelessScanResultTimeout = _ExtremeWirelessScanResultTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 24, 1, 5),
    _ExtremeWirelessScanResultTimeout_Type()
)
extremeWirelessScanResultTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessScanResultTimeout.setStatus("current")
if mibBuilder.loadTexts:
    extremeWirelessScanResultTimeout.setUnits("seconds")
_ExtremeWirelessScanResetStats_Type = TruthValue
_ExtremeWirelessScanResetStats_Object = MibTableColumn
extremeWirelessScanResetStats = _ExtremeWirelessScanResetStats_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 24, 1, 6),
    _ExtremeWirelessScanResetStats_Type()
)
extremeWirelessScanResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessScanResetStats.setStatus("current")
_ExtremeWirelessScanClearTable_Type = TruthValue
_ExtremeWirelessScanClearTable_Object = MibTableColumn
extremeWirelessScanClearTable = _ExtremeWirelessScanClearTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 24, 1, 7),
    _ExtremeWirelessScanClearTable_Type()
)
extremeWirelessScanClearTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessScanClearTable.setStatus("current")


class _ExtremeWirelessScanSendAPAddedTrap_Type(TruthValue):
    """Custom type extremeWirelessScanSendAPAddedTrap based on TruthValue"""


_ExtremeWirelessScanSendAPAddedTrap_Object = MibTableColumn
extremeWirelessScanSendAPAddedTrap = _ExtremeWirelessScanSendAPAddedTrap_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 24, 1, 8),
    _ExtremeWirelessScanSendAPAddedTrap_Type()
)
extremeWirelessScanSendAPAddedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessScanSendAPAddedTrap.setStatus("current")


class _ExtremeWirelessScanSendAPRemovedTrap_Type(TruthValue):
    """Custom type extremeWirelessScanSendAPRemovedTrap based on TruthValue"""


_ExtremeWirelessScanSendAPRemovedTrap_Object = MibTableColumn
extremeWirelessScanSendAPRemovedTrap = _ExtremeWirelessScanSendAPRemovedTrap_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 24, 1, 9),
    _ExtremeWirelessScanSendAPRemovedTrap_Type()
)
extremeWirelessScanSendAPRemovedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessScanSendAPRemovedTrap.setStatus("current")


class _ExtremeWirelessScanSendAPUpdatedTrap_Type(TruthValue):
    """Custom type extremeWirelessScanSendAPUpdatedTrap based on TruthValue"""


_ExtremeWirelessScanSendAPUpdatedTrap_Object = MibTableColumn
extremeWirelessScanSendAPUpdatedTrap = _ExtremeWirelessScanSendAPUpdatedTrap_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 24, 1, 10),
    _ExtremeWirelessScanSendAPUpdatedTrap_Type()
)
extremeWirelessScanSendAPUpdatedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessScanSendAPUpdatedTrap.setStatus("current")
_ExtremeWirelessOffChannelScanCfgTable_Object = MibTable
extremeWirelessOffChannelScanCfgTable = _ExtremeWirelessOffChannelScanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 25)
)
if mibBuilder.loadTexts:
    extremeWirelessOffChannelScanCfgTable.setStatus("current")
_ExtremeWirelessOffChannelScanCfgEntry_Object = MibTableRow
extremeWirelessOffChannelScanCfgEntry = _ExtremeWirelessOffChannelScanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 25, 1)
)
extremeWirelessOffChannelScanCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessOffChannelScanCfgEntry.setStatus("current")
_ExtremeWirelessOffChannelScanStart_Type = TruthValue
_ExtremeWirelessOffChannelScanStart_Object = MibTableColumn
extremeWirelessOffChannelScanStart = _ExtremeWirelessOffChannelScanStart_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 25, 1, 1),
    _ExtremeWirelessOffChannelScanStart_Type()
)
extremeWirelessOffChannelScanStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessOffChannelScanStart.setStatus("current")


class _ExtremeWirelessOffChannelScanList_Type(Bits):
    """Custom type extremeWirelessOffChannelScanList based on Bits"""
    namedValues = NamedValues(
        *(("scanAll", 0),
          ("scanChannel1", 2),
          ("scanChannel10", 11),
          ("scanChannel100", 25),
          ("scanChannel104", 26),
          ("scanChannel108", 27),
          ("scanChannel11", 12),
          ("scanChannel113", 28),
          ("scanChannel116", 29),
          ("scanChannel12", 13),
          ("scanChannel120", 30),
          ("scanChannel124", 31),
          ("scanChannel128", 32),
          ("scanChannel13", 14),
          ("scanChannel132", 33),
          ("scanChannel14", 15),
          ("scanChannel140", 34),
          ("scanChannel149", 35),
          ("scanChannel153", 36),
          ("scanChannel157", 37),
          ("scanChannel161", 38),
          ("scanChannel165", 39),
          ("scanChannel2", 3),
          ("scanChannel3", 4),
          ("scanChannel34", 16),
          ("scanChannel36", 17),
          ("scanChannel4", 5),
          ("scanChannel40", 18),
          ("scanChannel44", 19),
          ("scanChannel48", 20),
          ("scanChannel5", 6),
          ("scanChannel52", 21),
          ("scanChannel56", 22),
          ("scanChannel6", 7),
          ("scanChannel60", 23),
          ("scanChannel64", 24),
          ("scanChannel7", 8),
          ("scanChannel8", 9),
          ("scanChannel9", 10),
          ("scanEvery", 1))
    )

_ExtremeWirelessOffChannelScanList_Type.__name__ = "Bits"
_ExtremeWirelessOffChannelScanList_Object = MibTableColumn
extremeWirelessOffChannelScanList = _ExtremeWirelessOffChannelScanList_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 25, 1, 2),
    _ExtremeWirelessOffChannelScanList_Type()
)
extremeWirelessOffChannelScanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessOffChannelScanList.setStatus("current")


class _ExtremeWirelessOffChannelScanMinWait_Type(Unsigned32):
    """Custom type extremeWirelessOffChannelScanMinWait based on Unsigned32"""
    defaultValue = 1


_ExtremeWirelessOffChannelScanMinWait_Object = MibTableColumn
extremeWirelessOffChannelScanMinWait = _ExtremeWirelessOffChannelScanMinWait_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 25, 1, 3),
    _ExtremeWirelessOffChannelScanMinWait_Type()
)
extremeWirelessOffChannelScanMinWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessOffChannelScanMinWait.setStatus("current")
if mibBuilder.loadTexts:
    extremeWirelessOffChannelScanMinWait.setUnits("milliseconds")


class _ExtremeWirelessOffChannelScanMaxWait_Type(Unsigned32):
    """Custom type extremeWirelessOffChannelScanMaxWait based on Unsigned32"""
    defaultValue = 10


_ExtremeWirelessOffChannelScanMaxWait_Object = MibTableColumn
extremeWirelessOffChannelScanMaxWait = _ExtremeWirelessOffChannelScanMaxWait_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 25, 1, 4),
    _ExtremeWirelessOffChannelScanMaxWait_Type()
)
extremeWirelessOffChannelScanMaxWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessOffChannelScanMaxWait.setStatus("current")
if mibBuilder.loadTexts:
    extremeWirelessOffChannelScanMaxWait.setUnits("milliseconds")


class _ExtremeWirelessOffChannelContinuous_Type(TruthValue):
    """Custom type extremeWirelessOffChannelContinuous based on TruthValue"""


_ExtremeWirelessOffChannelContinuous_Object = MibTableColumn
extremeWirelessOffChannelContinuous = _ExtremeWirelessOffChannelContinuous_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 25, 1, 5),
    _ExtremeWirelessOffChannelContinuous_Type()
)
extremeWirelessOffChannelContinuous.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessOffChannelContinuous.setStatus("current")
_ExtremeWirelessScanStatusTable_Object = MibTable
extremeWirelessScanStatusTable = _ExtremeWirelessScanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 26)
)
if mibBuilder.loadTexts:
    extremeWirelessScanStatusTable.setStatus("current")
_ExtremeWirelessScanStatusEntry_Object = MibTableRow
extremeWirelessScanStatusEntry = _ExtremeWirelessScanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 26, 1)
)
extremeWirelessScanStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessScanStatusEntry.setStatus("current")
_ExtremeWirelessScanCurrentTableSize_Type = Unsigned32
_ExtremeWirelessScanCurrentTableSize_Object = MibTableColumn
extremeWirelessScanCurrentTableSize = _ExtremeWirelessScanCurrentTableSize_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 26, 1, 1),
    _ExtremeWirelessScanCurrentTableSize_Type()
)
extremeWirelessScanCurrentTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanCurrentTableSize.setStatus("current")
_ExtremeWirelessScanTableWatermark_Type = Unsigned32
_ExtremeWirelessScanTableWatermark_Object = MibTableColumn
extremeWirelessScanTableWatermark = _ExtremeWirelessScanTableWatermark_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 26, 1, 2),
    _ExtremeWirelessScanTableWatermark_Type()
)
extremeWirelessScanTableWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanTableWatermark.setStatus("current")
_ExtremeWirelessScanTotalOverflows_Type = Unsigned32
_ExtremeWirelessScanTotalOverflows_Object = MibTableColumn
extremeWirelessScanTotalOverflows = _ExtremeWirelessScanTotalOverflows_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 26, 1, 3),
    _ExtremeWirelessScanTotalOverflows_Type()
)
extremeWirelessScanTotalOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanTotalOverflows.setStatus("current")
_ExtremeWirelessScanTotalTimeouts_Type = Unsigned32
_ExtremeWirelessScanTotalTimeouts_Object = MibTableColumn
extremeWirelessScanTotalTimeouts = _ExtremeWirelessScanTotalTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 26, 1, 4),
    _ExtremeWirelessScanTotalTimeouts_Type()
)
extremeWirelessScanTotalTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanTotalTimeouts.setStatus("current")
_ExtremeWirelessScanOffChannelRunning_Type = TruthValue
_ExtremeWirelessScanOffChannelRunning_Object = MibTableColumn
extremeWirelessScanOffChannelRunning = _ExtremeWirelessScanOffChannelRunning_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 26, 1, 5),
    _ExtremeWirelessScanOffChannelRunning_Type()
)
extremeWirelessScanOffChannelRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanOffChannelRunning.setStatus("current")
_ExtremeWirelessScanCurrentChannel_Type = Unsigned32
_ExtremeWirelessScanCurrentChannel_Object = MibTableColumn
extremeWirelessScanCurrentChannel = _ExtremeWirelessScanCurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 26, 1, 6),
    _ExtremeWirelessScanCurrentChannel_Type()
)
extremeWirelessScanCurrentChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanCurrentChannel.setStatus("current")
_ExtremeWirelessScanLastElement_Type = TimeTicks
_ExtremeWirelessScanLastElement_Object = MibTableColumn
extremeWirelessScanLastElement = _ExtremeWirelessScanLastElement_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 26, 1, 7),
    _ExtremeWirelessScanLastElement_Type()
)
extremeWirelessScanLastElement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanLastElement.setStatus("current")
_ExtremeWirelessScanNumProbes_Type = Unsigned32
_ExtremeWirelessScanNumProbes_Object = MibTableColumn
extremeWirelessScanNumProbes = _ExtremeWirelessScanNumProbes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 26, 1, 8),
    _ExtremeWirelessScanNumProbes_Type()
)
extremeWirelessScanNumProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanNumProbes.setStatus("current")
_ExtremeWirelessScanResultsTable_Object = MibTable
extremeWirelessScanResultsTable = _ExtremeWirelessScanResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27)
)
if mibBuilder.loadTexts:
    extremeWirelessScanResultsTable.setStatus("current")
_ExtremeWirelessScanResultsEntry_Object = MibTableRow
extremeWirelessScanResultsEntry = _ExtremeWirelessScanResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1)
)
extremeWirelessScanResultsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessScanResultsStationId"),
)
if mibBuilder.loadTexts:
    extremeWirelessScanResultsEntry.setStatus("current")
_ExtremeWirelessScanResultsStationId_Type = MacAddress
_ExtremeWirelessScanResultsStationId_Object = MibTableColumn
extremeWirelessScanResultsStationId = _ExtremeWirelessScanResultsStationId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 1),
    _ExtremeWirelessScanResultsStationId_Type()
)
extremeWirelessScanResultsStationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsStationId.setStatus("current")
_ExtremeWirelessScanResultsFirstSeen_Type = TimeTicks
_ExtremeWirelessScanResultsFirstSeen_Object = MibTableColumn
extremeWirelessScanResultsFirstSeen = _ExtremeWirelessScanResultsFirstSeen_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 2),
    _ExtremeWirelessScanResultsFirstSeen_Type()
)
extremeWirelessScanResultsFirstSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsFirstSeen.setStatus("current")
_ExtremeWirelessScanResultsLastChange_Type = TimeTicks
_ExtremeWirelessScanResultsLastChange_Object = MibTableColumn
extremeWirelessScanResultsLastChange = _ExtremeWirelessScanResultsLastChange_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 3),
    _ExtremeWirelessScanResultsLastChange_Type()
)
extremeWirelessScanResultsLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsLastChange.setStatus("current")
_ExtremeWirelessScanResultsPacketTime_Type = Integer32
_ExtremeWirelessScanResultsPacketTime_Object = MibTableColumn
extremeWirelessScanResultsPacketTime = _ExtremeWirelessScanResultsPacketTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 4),
    _ExtremeWirelessScanResultsPacketTime_Type()
)
extremeWirelessScanResultsPacketTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsPacketTime.setStatus("current")
_ExtremeWirelessScanResultsPacketRate_Type = Integer32
_ExtremeWirelessScanResultsPacketRate_Object = MibTableColumn
extremeWirelessScanResultsPacketRate = _ExtremeWirelessScanResultsPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 5),
    _ExtremeWirelessScanResultsPacketRate_Type()
)
extremeWirelessScanResultsPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsPacketRate.setStatus("current")
_ExtremeWirelessScanResultsChannel_Type = Integer32
_ExtremeWirelessScanResultsChannel_Object = MibTableColumn
extremeWirelessScanResultsChannel = _ExtremeWirelessScanResultsChannel_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 6),
    _ExtremeWirelessScanResultsChannel_Type()
)
extremeWirelessScanResultsChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsChannel.setStatus("current")
_ExtremeWirelessScanResultsMinRSS_Type = Integer32
_ExtremeWirelessScanResultsMinRSS_Object = MibTableColumn
extremeWirelessScanResultsMinRSS = _ExtremeWirelessScanResultsMinRSS_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 7),
    _ExtremeWirelessScanResultsMinRSS_Type()
)
extremeWirelessScanResultsMinRSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsMinRSS.setStatus("current")
_ExtremeWirelessScanResultsMaxRSS_Type = Integer32
_ExtremeWirelessScanResultsMaxRSS_Object = MibTableColumn
extremeWirelessScanResultsMaxRSS = _ExtremeWirelessScanResultsMaxRSS_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 8),
    _ExtremeWirelessScanResultsMaxRSS_Type()
)
extremeWirelessScanResultsMaxRSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsMaxRSS.setStatus("current")
_ExtremeWirelessScanResultsAvgRSS_Type = Integer32
_ExtremeWirelessScanResultsAvgRSS_Object = MibTableColumn
extremeWirelessScanResultsAvgRSS = _ExtremeWirelessScanResultsAvgRSS_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 9),
    _ExtremeWirelessScanResultsAvgRSS_Type()
)
extremeWirelessScanResultsAvgRSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsAvgRSS.setStatus("current")
_ExtremeWirelessScanResultsTotalBeacons_Type = Unsigned32
_ExtremeWirelessScanResultsTotalBeacons_Object = MibTableColumn
extremeWirelessScanResultsTotalBeacons = _ExtremeWirelessScanResultsTotalBeacons_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 10),
    _ExtremeWirelessScanResultsTotalBeacons_Type()
)
extremeWirelessScanResultsTotalBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsTotalBeacons.setStatus("current")
_ExtremeWirelessScanResultsTotalProbes_Type = Unsigned32
_ExtremeWirelessScanResultsTotalProbes_Object = MibTableColumn
extremeWirelessScanResultsTotalProbes = _ExtremeWirelessScanResultsTotalProbes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 11),
    _ExtremeWirelessScanResultsTotalProbes_Type()
)
extremeWirelessScanResultsTotalProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsTotalProbes.setStatus("current")


class _ExtremeWirelessScanResultsDiscoveredBy_Type(Integer32):
    """Custom type extremeWirelessScanResultsDiscoveredBy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("beacon", 2),
          ("probe", 1))
    )


_ExtremeWirelessScanResultsDiscoveredBy_Type.__name__ = "Integer32"
_ExtremeWirelessScanResultsDiscoveredBy_Object = MibTableColumn
extremeWirelessScanResultsDiscoveredBy = _ExtremeWirelessScanResultsDiscoveredBy_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 12),
    _ExtremeWirelessScanResultsDiscoveredBy_Type()
)
extremeWirelessScanResultsDiscoveredBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsDiscoveredBy.setStatus("current")
_ExtremeWirelessScanResultsDSSOFDM_Type = TruthValue
_ExtremeWirelessScanResultsDSSOFDM_Object = MibTableColumn
extremeWirelessScanResultsDSSOFDM = _ExtremeWirelessScanResultsDSSOFDM_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 13),
    _ExtremeWirelessScanResultsDSSOFDM_Type()
)
extremeWirelessScanResultsDSSOFDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsDSSOFDM.setStatus("current")
_ExtremeWirelessScanResultsRSNEnabled_Type = TruthValue
_ExtremeWirelessScanResultsRSNEnabled_Object = MibTableColumn
extremeWirelessScanResultsRSNEnabled = _ExtremeWirelessScanResultsRSNEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 14),
    _ExtremeWirelessScanResultsRSNEnabled_Type()
)
extremeWirelessScanResultsRSNEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsRSNEnabled.setStatus("current")
_ExtremeWirelessScanResultsGShortSlot_Type = TruthValue
_ExtremeWirelessScanResultsGShortSlot_Object = MibTableColumn
extremeWirelessScanResultsGShortSlot = _ExtremeWirelessScanResultsGShortSlot_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 15),
    _ExtremeWirelessScanResultsGShortSlot_Type()
)
extremeWirelessScanResultsGShortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsGShortSlot.setStatus("current")
_ExtremeWirelessScanResultsChannelAgility_Type = TruthValue
_ExtremeWirelessScanResultsChannelAgility_Object = MibTableColumn
extremeWirelessScanResultsChannelAgility = _ExtremeWirelessScanResultsChannelAgility_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 16),
    _ExtremeWirelessScanResultsChannelAgility_Type()
)
extremeWirelessScanResultsChannelAgility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsChannelAgility.setStatus("current")
_ExtremeWirelessScanResultsPBCC_Type = TruthValue
_ExtremeWirelessScanResultsPBCC_Object = MibTableColumn
extremeWirelessScanResultsPBCC = _ExtremeWirelessScanResultsPBCC_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 17),
    _ExtremeWirelessScanResultsPBCC_Type()
)
extremeWirelessScanResultsPBCC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsPBCC.setStatus("current")
_ExtremeWirelessScanResultsPreamble_Type = TruthValue
_ExtremeWirelessScanResultsPreamble_Object = MibTableColumn
extremeWirelessScanResultsPreamble = _ExtremeWirelessScanResultsPreamble_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 18),
    _ExtremeWirelessScanResultsPreamble_Type()
)
extremeWirelessScanResultsPreamble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsPreamble.setStatus("current")
_ExtremeWirelessScanResultsPrivacy_Type = TruthValue
_ExtremeWirelessScanResultsPrivacy_Object = MibTableColumn
extremeWirelessScanResultsPrivacy = _ExtremeWirelessScanResultsPrivacy_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 19),
    _ExtremeWirelessScanResultsPrivacy_Type()
)
extremeWirelessScanResultsPrivacy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsPrivacy.setStatus("current")
_ExtremeWirelessScanResultsCFPollReq_Type = TruthValue
_ExtremeWirelessScanResultsCFPollReq_Object = MibTableColumn
extremeWirelessScanResultsCFPollReq = _ExtremeWirelessScanResultsCFPollReq_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 20),
    _ExtremeWirelessScanResultsCFPollReq_Type()
)
extremeWirelessScanResultsCFPollReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsCFPollReq.setStatus("current")
_ExtremeWirelessScanResultsCFPollable_Type = TruthValue
_ExtremeWirelessScanResultsCFPollable_Object = MibTableColumn
extremeWirelessScanResultsCFPollable = _ExtremeWirelessScanResultsCFPollable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 21),
    _ExtremeWirelessScanResultsCFPollable_Type()
)
extremeWirelessScanResultsCFPollable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsCFPollable.setStatus("current")


class _ExtremeWirelessScanResultsNetworkType_Type(Integer32):
    """Custom type extremeWirelessScanResultsNetworkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bss", 2),
          ("ibss", 1))
    )


_ExtremeWirelessScanResultsNetworkType_Type.__name__ = "Integer32"
_ExtremeWirelessScanResultsNetworkType_Object = MibTableColumn
extremeWirelessScanResultsNetworkType = _ExtremeWirelessScanResultsNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 22),
    _ExtremeWirelessScanResultsNetworkType_Type()
)
extremeWirelessScanResultsNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsNetworkType.setStatus("current")
_ExtremeWirelessScanResultsSSID_Type = OctetString
_ExtremeWirelessScanResultsSSID_Object = MibTableColumn
extremeWirelessScanResultsSSID = _ExtremeWirelessScanResultsSSID_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 23),
    _ExtremeWirelessScanResultsSSID_Type()
)
extremeWirelessScanResultsSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsSSID.setStatus("current")
_ExtremeWirelessScanResultsRateSet_Type = OctetString
_ExtremeWirelessScanResultsRateSet_Object = MibTableColumn
extremeWirelessScanResultsRateSet = _ExtremeWirelessScanResultsRateSet_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 24),
    _ExtremeWirelessScanResultsRateSet_Type()
)
extremeWirelessScanResultsRateSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsRateSet.setStatus("current")
_ExtremeWirelessScanResultsExtRateSet_Type = OctetString
_ExtremeWirelessScanResultsExtRateSet_Object = MibTableColumn
extremeWirelessScanResultsExtRateSet = _ExtremeWirelessScanResultsExtRateSet_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 25),
    _ExtremeWirelessScanResultsExtRateSet_Type()
)
extremeWirelessScanResultsExtRateSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsExtRateSet.setStatus("current")
_ExtremeWirelessScanResultsDSSParameter_Type = Integer32
_ExtremeWirelessScanResultsDSSParameter_Object = MibTableColumn
extremeWirelessScanResultsDSSParameter = _ExtremeWirelessScanResultsDSSParameter_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 26),
    _ExtremeWirelessScanResultsDSSParameter_Type()
)
extremeWirelessScanResultsDSSParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsDSSParameter.setStatus("current")
_ExtremeWirelessScanResultsTIMCount_Type = Integer32
_ExtremeWirelessScanResultsTIMCount_Object = MibTableColumn
extremeWirelessScanResultsTIMCount = _ExtremeWirelessScanResultsTIMCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 27),
    _ExtremeWirelessScanResultsTIMCount_Type()
)
extremeWirelessScanResultsTIMCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsTIMCount.setStatus("current")
_ExtremeWirelessScanResultsTIMPeriod_Type = Integer32
_ExtremeWirelessScanResultsTIMPeriod_Object = MibTableColumn
extremeWirelessScanResultsTIMPeriod = _ExtremeWirelessScanResultsTIMPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 28),
    _ExtremeWirelessScanResultsTIMPeriod_Type()
)
extremeWirelessScanResultsTIMPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsTIMPeriod.setStatus("current")
_ExtremeWirelessScanResultsTIMTrafficInd_Type = TruthValue
_ExtremeWirelessScanResultsTIMTrafficInd_Object = MibTableColumn
extremeWirelessScanResultsTIMTrafficInd = _ExtremeWirelessScanResultsTIMTrafficInd_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 29),
    _ExtremeWirelessScanResultsTIMTrafficInd_Type()
)
extremeWirelessScanResultsTIMTrafficInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsTIMTrafficInd.setStatus("current")
_ExtremeWirelessScanResultsCountryCode_Type = OctetString
_ExtremeWirelessScanResultsCountryCode_Object = MibTableColumn
extremeWirelessScanResultsCountryCode = _ExtremeWirelessScanResultsCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 30),
    _ExtremeWirelessScanResultsCountryCode_Type()
)
extremeWirelessScanResultsCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsCountryCode.setStatus("current")
_ExtremeWirelessScanWPAIEPresent_Type = TruthValue
_ExtremeWirelessScanWPAIEPresent_Object = MibTableColumn
extremeWirelessScanWPAIEPresent = _ExtremeWirelessScanWPAIEPresent_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 31),
    _ExtremeWirelessScanWPAIEPresent_Type()
)
extremeWirelessScanWPAIEPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanWPAIEPresent.setStatus("current")
_ExtremeWirelessScanWPAVersion_Type = Unsigned32
_ExtremeWirelessScanWPAVersion_Object = MibTableColumn
extremeWirelessScanWPAVersion = _ExtremeWirelessScanWPAVersion_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 32),
    _ExtremeWirelessScanWPAVersion_Type()
)
extremeWirelessScanWPAVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanWPAVersion.setStatus("current")
_ExtremeWirelessScanWPAIEMcastCipher_Type = WPACipherSet
_ExtremeWirelessScanWPAIEMcastCipher_Object = MibTableColumn
extremeWirelessScanWPAIEMcastCipher = _ExtremeWirelessScanWPAIEMcastCipher_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 33),
    _ExtremeWirelessScanWPAIEMcastCipher_Type()
)
extremeWirelessScanWPAIEMcastCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanWPAIEMcastCipher.setStatus("current")
_ExtremeWirelessScanWPAUcastCipherCount_Type = Unsigned32
_ExtremeWirelessScanWPAUcastCipherCount_Object = MibTableColumn
extremeWirelessScanWPAUcastCipherCount = _ExtremeWirelessScanWPAUcastCipherCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 34),
    _ExtremeWirelessScanWPAUcastCipherCount_Type()
)
extremeWirelessScanWPAUcastCipherCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanWPAUcastCipherCount.setStatus("current")
_ExtremeWirelessScanWPAUcastCipher_Type = WPACipherSet
_ExtremeWirelessScanWPAUcastCipher_Object = MibTableColumn
extremeWirelessScanWPAUcastCipher = _ExtremeWirelessScanWPAUcastCipher_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 35),
    _ExtremeWirelessScanWPAUcastCipher_Type()
)
extremeWirelessScanWPAUcastCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanWPAUcastCipher.setStatus("current")
_ExtremeWirelessScanWPAKeyMgmtCount_Type = Unsigned32
_ExtremeWirelessScanWPAKeyMgmtCount_Object = MibTableColumn
extremeWirelessScanWPAKeyMgmtCount = _ExtremeWirelessScanWPAKeyMgmtCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 36),
    _ExtremeWirelessScanWPAKeyMgmtCount_Type()
)
extremeWirelessScanWPAKeyMgmtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanWPAKeyMgmtCount.setStatus("current")
_ExtremeWirelessScanWPAKeyMgmtSuite_Type = WPAKeyMgmtSet
_ExtremeWirelessScanWPAKeyMgmtSuite_Object = MibTableColumn
extremeWirelessScanWPAKeyMgmtSuite = _ExtremeWirelessScanWPAKeyMgmtSuite_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 37),
    _ExtremeWirelessScanWPAKeyMgmtSuite_Type()
)
extremeWirelessScanWPAKeyMgmtSuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanWPAKeyMgmtSuite.setStatus("current")
_ExtremeWirelessScanResultsIEBlob_Type = OctetString
_ExtremeWirelessScanResultsIEBlob_Object = MibTableColumn
extremeWirelessScanResultsIEBlob = _ExtremeWirelessScanResultsIEBlob_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 27, 1, 38),
    _ExtremeWirelessScanResultsIEBlob_Type()
)
extremeWirelessScanResultsIEBlob.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsIEBlob.setStatus("current")
_ExtremeWirelessProbeInfoCfgTable_Object = MibTable
extremeWirelessProbeInfoCfgTable = _ExtremeWirelessProbeInfoCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 28)
)
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoCfgTable.setStatus("current")
_ExtremeWirelessProbeInfoCfgEntry_Object = MibTableRow
extremeWirelessProbeInfoCfgEntry = _ExtremeWirelessProbeInfoCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 28, 1)
)
extremeWirelessProbeInfoCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoCfgEntry.setStatus("current")


class _ExtremeWirelessProbeInfoEnable_Type(TruthValue):
    """Custom type extremeWirelessProbeInfoEnable based on TruthValue"""


_ExtremeWirelessProbeInfoEnable_Object = MibTableColumn
extremeWirelessProbeInfoEnable = _ExtremeWirelessProbeInfoEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 28, 1, 1),
    _ExtremeWirelessProbeInfoEnable_Type()
)
extremeWirelessProbeInfoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoEnable.setStatus("current")


class _ExtremeWirelessProbeInfoKeepIEs_Type(TruthValue):
    """Custom type extremeWirelessProbeInfoKeepIEs based on TruthValue"""


_ExtremeWirelessProbeInfoKeepIEs_Object = MibTableColumn
extremeWirelessProbeInfoKeepIEs = _ExtremeWirelessProbeInfoKeepIEs_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 28, 1, 2),
    _ExtremeWirelessProbeInfoKeepIEs_Type()
)
extremeWirelessProbeInfoKeepIEs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoKeepIEs.setStatus("current")


class _ExtremeWirelessProbeInfoTableSize_Type(Unsigned32):
    """Custom type extremeWirelessProbeInfoTableSize based on Unsigned32"""
    defaultValue = 128


_ExtremeWirelessProbeInfoTableSize_Object = MibTableColumn
extremeWirelessProbeInfoTableSize = _ExtremeWirelessProbeInfoTableSize_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 28, 1, 3),
    _ExtremeWirelessProbeInfoTableSize_Type()
)
extremeWirelessProbeInfoTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoTableSize.setStatus("current")


class _ExtremeWirelessProbeInfoTimeout_Type(Unsigned32):
    """Custom type extremeWirelessProbeInfoTimeout based on Unsigned32"""
    defaultValue = 3600


_ExtremeWirelessProbeInfoTimeout_Object = MibTableColumn
extremeWirelessProbeInfoTimeout = _ExtremeWirelessProbeInfoTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 28, 1, 4),
    _ExtremeWirelessProbeInfoTimeout_Type()
)
extremeWirelessProbeInfoTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoTimeout.setStatus("current")
_ExtremeWirelessProbeInfoTableClear_Type = TruthValue
_ExtremeWirelessProbeInfoTableClear_Object = MibTableColumn
extremeWirelessProbeInfoTableClear = _ExtremeWirelessProbeInfoTableClear_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 28, 1, 5),
    _ExtremeWirelessProbeInfoTableClear_Type()
)
extremeWirelessProbeInfoTableClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoTableClear.setStatus("current")
_ExtremeWirelessProbeInfoSourceClear_Type = MacAddress
_ExtremeWirelessProbeInfoSourceClear_Object = MibTableColumn
extremeWirelessProbeInfoSourceClear = _ExtremeWirelessProbeInfoSourceClear_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 28, 1, 6),
    _ExtremeWirelessProbeInfoSourceClear_Type()
)
extremeWirelessProbeInfoSourceClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoSourceClear.setStatus("current")
_ExtremeWirelessProbeInfoTableStatsClear_Type = TruthValue
_ExtremeWirelessProbeInfoTableStatsClear_Object = MibTableColumn
extremeWirelessProbeInfoTableStatsClear = _ExtremeWirelessProbeInfoTableStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 28, 1, 7),
    _ExtremeWirelessProbeInfoTableStatsClear_Type()
)
extremeWirelessProbeInfoTableStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoTableStatsClear.setStatus("current")
_ExtremeWirelessProbeInfoSourceStatsClear_Type = MacAddress
_ExtremeWirelessProbeInfoSourceStatsClear_Object = MibTableColumn
extremeWirelessProbeInfoSourceStatsClear = _ExtremeWirelessProbeInfoSourceStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 28, 1, 8),
    _ExtremeWirelessProbeInfoSourceStatsClear_Type()
)
extremeWirelessProbeInfoSourceStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoSourceStatsClear.setStatus("current")


class _ExtremeWirelessProbeInfoSendAddedTrap_Type(TruthValue):
    """Custom type extremeWirelessProbeInfoSendAddedTrap based on TruthValue"""


_ExtremeWirelessProbeInfoSendAddedTrap_Object = MibTableColumn
extremeWirelessProbeInfoSendAddedTrap = _ExtremeWirelessProbeInfoSendAddedTrap_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 28, 1, 9),
    _ExtremeWirelessProbeInfoSendAddedTrap_Type()
)
extremeWirelessProbeInfoSendAddedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoSendAddedTrap.setStatus("current")


class _ExtremeWirelessProbeInfoSendRemovedTrap_Type(TruthValue):
    """Custom type extremeWirelessProbeInfoSendRemovedTrap based on TruthValue"""


_ExtremeWirelessProbeInfoSendRemovedTrap_Object = MibTableColumn
extremeWirelessProbeInfoSendRemovedTrap = _ExtremeWirelessProbeInfoSendRemovedTrap_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 28, 1, 10),
    _ExtremeWirelessProbeInfoSendRemovedTrap_Type()
)
extremeWirelessProbeInfoSendRemovedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoSendRemovedTrap.setStatus("current")
_ExtremeWirelessProbeInfoStatusTable_Object = MibTable
extremeWirelessProbeInfoStatusTable = _ExtremeWirelessProbeInfoStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 29)
)
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoStatusTable.setStatus("current")
_ExtremeWirelessProbeInfoStatusEntry_Object = MibTableRow
extremeWirelessProbeInfoStatusEntry = _ExtremeWirelessProbeInfoStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 29, 1)
)
extremeWirelessProbeInfoStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoStatusEntry.setStatus("current")
_ExtremeWirelessProbeInfoStatusCurrentTableSize_Type = Unsigned32
_ExtremeWirelessProbeInfoStatusCurrentTableSize_Object = MibTableColumn
extremeWirelessProbeInfoStatusCurrentTableSize = _ExtremeWirelessProbeInfoStatusCurrentTableSize_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 29, 1, 1),
    _ExtremeWirelessProbeInfoStatusCurrentTableSize_Type()
)
extremeWirelessProbeInfoStatusCurrentTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoStatusCurrentTableSize.setStatus("current")
_ExtremeWirelessProbeInfoStatusWatermark_Type = Unsigned32
_ExtremeWirelessProbeInfoStatusWatermark_Object = MibTableColumn
extremeWirelessProbeInfoStatusWatermark = _ExtremeWirelessProbeInfoStatusWatermark_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 29, 1, 2),
    _ExtremeWirelessProbeInfoStatusWatermark_Type()
)
extremeWirelessProbeInfoStatusWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoStatusWatermark.setStatus("current")
_ExtremeWirelessProbeInfoStatusTotalOverflows_Type = Unsigned32
_ExtremeWirelessProbeInfoStatusTotalOverflows_Object = MibTableColumn
extremeWirelessProbeInfoStatusTotalOverflows = _ExtremeWirelessProbeInfoStatusTotalOverflows_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 29, 1, 3),
    _ExtremeWirelessProbeInfoStatusTotalOverflows_Type()
)
extremeWirelessProbeInfoStatusTotalOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoStatusTotalOverflows.setStatus("current")
_ExtremeWirelessProbeInfoStatusTotalTimeouts_Type = Unsigned32
_ExtremeWirelessProbeInfoStatusTotalTimeouts_Object = MibTableColumn
extremeWirelessProbeInfoStatusTotalTimeouts = _ExtremeWirelessProbeInfoStatusTotalTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 29, 1, 4),
    _ExtremeWirelessProbeInfoStatusTotalTimeouts_Type()
)
extremeWirelessProbeInfoStatusTotalTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoStatusTotalTimeouts.setStatus("current")
_ExtremeWirelessProbeInfoStatusLastElement_Type = TimeTicks
_ExtremeWirelessProbeInfoStatusLastElement_Object = MibTableColumn
extremeWirelessProbeInfoStatusLastElement = _ExtremeWirelessProbeInfoStatusLastElement_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 29, 1, 5),
    _ExtremeWirelessProbeInfoStatusLastElement_Type()
)
extremeWirelessProbeInfoStatusLastElement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoStatusLastElement.setStatus("current")
_ExtremeWirelessProbeInfoStatusTotalProbes_Type = Unsigned32
_ExtremeWirelessProbeInfoStatusTotalProbes_Object = MibTableColumn
extremeWirelessProbeInfoStatusTotalProbes = _ExtremeWirelessProbeInfoStatusTotalProbes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 29, 1, 6),
    _ExtremeWirelessProbeInfoStatusTotalProbes_Type()
)
extremeWirelessProbeInfoStatusTotalProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoStatusTotalProbes.setStatus("current")
_ExtremeWirelessProbeInfoTable_Object = MibTable
extremeWirelessProbeInfoTable = _ExtremeWirelessProbeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 30)
)
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoTable.setStatus("current")
_ExtremeWirelessProbeInfoEntry_Object = MibTableRow
extremeWirelessProbeInfoEntry = _ExtremeWirelessProbeInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 30, 1)
)
extremeWirelessProbeInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessProbeInfoSource"),
)
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoEntry.setStatus("current")
_ExtremeWirelessProbeInfoSource_Type = MacAddress
_ExtremeWirelessProbeInfoSource_Object = MibTableColumn
extremeWirelessProbeInfoSource = _ExtremeWirelessProbeInfoSource_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 30, 1, 1),
    _ExtremeWirelessProbeInfoSource_Type()
)
extremeWirelessProbeInfoSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoSource.setStatus("current")
_ExtremeWirelessProbeInfoTotalProbes_Type = Unsigned32
_ExtremeWirelessProbeInfoTotalProbes_Object = MibTableColumn
extremeWirelessProbeInfoTotalProbes = _ExtremeWirelessProbeInfoTotalProbes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 30, 1, 2),
    _ExtremeWirelessProbeInfoTotalProbes_Type()
)
extremeWirelessProbeInfoTotalProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoTotalProbes.setStatus("current")
_ExtremeWirelessProbeInfoTotalProbeResp_Type = Unsigned32
_ExtremeWirelessProbeInfoTotalProbeResp_Object = MibTableColumn
extremeWirelessProbeInfoTotalProbeResp = _ExtremeWirelessProbeInfoTotalProbeResp_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 30, 1, 3),
    _ExtremeWirelessProbeInfoTotalProbeResp_Type()
)
extremeWirelessProbeInfoTotalProbeResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoTotalProbeResp.setStatus("current")
_ExtremeWirelessProbeInfoRateIESize_Type = Unsigned32
_ExtremeWirelessProbeInfoRateIESize_Object = MibTableColumn
extremeWirelessProbeInfoRateIESize = _ExtremeWirelessProbeInfoRateIESize_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 30, 1, 4),
    _ExtremeWirelessProbeInfoRateIESize_Type()
)
extremeWirelessProbeInfoRateIESize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoRateIESize.setStatus("current")
_ExtremeWirelessProbeInfoRateIE_Type = OctetString
_ExtremeWirelessProbeInfoRateIE_Object = MibTableColumn
extremeWirelessProbeInfoRateIE = _ExtremeWirelessProbeInfoRateIE_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 30, 1, 5),
    _ExtremeWirelessProbeInfoRateIE_Type()
)
extremeWirelessProbeInfoRateIE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoRateIE.setStatus("current")
_ExtremeWirelessProbeInfoFirstSeen_Type = TimeTicks
_ExtremeWirelessProbeInfoFirstSeen_Object = MibTableColumn
extremeWirelessProbeInfoFirstSeen = _ExtremeWirelessProbeInfoFirstSeen_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 30, 1, 6),
    _ExtremeWirelessProbeInfoFirstSeen_Type()
)
extremeWirelessProbeInfoFirstSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoFirstSeen.setStatus("current")
_ExtremeWirelessProbeInfoLastChange_Type = TimeTicks
_ExtremeWirelessProbeInfoLastChange_Object = MibTableColumn
extremeWirelessProbeInfoLastChange = _ExtremeWirelessProbeInfoLastChange_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 30, 1, 7),
    _ExtremeWirelessProbeInfoLastChange_Type()
)
extremeWirelessProbeInfoLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoLastChange.setStatus("current")
_ExtremeWirelessProbeInfoLastRSS_Type = Integer32
_ExtremeWirelessProbeInfoLastRSS_Object = MibTableColumn
extremeWirelessProbeInfoLastRSS = _ExtremeWirelessProbeInfoLastRSS_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 30, 1, 8),
    _ExtremeWirelessProbeInfoLastRSS_Type()
)
extremeWirelessProbeInfoLastRSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoLastRSS.setStatus("current")
_ExtremeWirelessProbeInfoLastRate_Type = Integer32
_ExtremeWirelessProbeInfoLastRate_Object = MibTableColumn
extremeWirelessProbeInfoLastRate = _ExtremeWirelessProbeInfoLastRate_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 30, 1, 9),
    _ExtremeWirelessProbeInfoLastRate_Type()
)
extremeWirelessProbeInfoLastRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoLastRate.setStatus("current")
_ExtremeWirelessProbeInfoLastChannel_Type = Integer32
_ExtremeWirelessProbeInfoLastChannel_Object = MibTableColumn
extremeWirelessProbeInfoLastChannel = _ExtremeWirelessProbeInfoLastChannel_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 30, 1, 10),
    _ExtremeWirelessProbeInfoLastChannel_Type()
)
extremeWirelessProbeInfoLastChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoLastChannel.setStatus("current")
_ExtremeWirelessClientDiagCfgTable_Object = MibTable
extremeWirelessClientDiagCfgTable = _ExtremeWirelessClientDiagCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 31)
)
if mibBuilder.loadTexts:
    extremeWirelessClientDiagCfgTable.setStatus("current")
_ExtremeWirelessClientDiagCfgEntry_Object = MibTableRow
extremeWirelessClientDiagCfgEntry = _ExtremeWirelessClientDiagCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 31, 1)
)
extremeWirelessClientDiagCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessClientDiagCfgEntry.setStatus("current")


class _ExtremeWirelessClientDiagCfgEnable_Type(TruthValue):
    """Custom type extremeWirelessClientDiagCfgEnable based on TruthValue"""


_ExtremeWirelessClientDiagCfgEnable_Object = MibTableColumn
extremeWirelessClientDiagCfgEnable = _ExtremeWirelessClientDiagCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 31, 1, 1),
    _ExtremeWirelessClientDiagCfgEnable_Type()
)
extremeWirelessClientDiagCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagCfgEnable.setStatus("current")
_ExtremeWirelessClientDiagCfgClearClient_Type = MacAddress
_ExtremeWirelessClientDiagCfgClearClient_Object = MibTableColumn
extremeWirelessClientDiagCfgClearClient = _ExtremeWirelessClientDiagCfgClearClient_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 31, 1, 2),
    _ExtremeWirelessClientDiagCfgClearClient_Type()
)
extremeWirelessClientDiagCfgClearClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagCfgClearClient.setStatus("current")


class _ExtremeWirelessClientDiagCfgTableSize_Type(Unsigned32):
    """Custom type extremeWirelessClientDiagCfgTableSize based on Unsigned32"""
    defaultValue = 128


_ExtremeWirelessClientDiagCfgTableSize_Object = MibTableColumn
extremeWirelessClientDiagCfgTableSize = _ExtremeWirelessClientDiagCfgTableSize_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 31, 1, 3),
    _ExtremeWirelessClientDiagCfgTableSize_Type()
)
extremeWirelessClientDiagCfgTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagCfgTableSize.setStatus("current")


class _ExtremeWirelessClientDiagCfgTimeout_Type(Unsigned32):
    """Custom type extremeWirelessClientDiagCfgTimeout based on Unsigned32"""
    defaultValue = 3600


_ExtremeWirelessClientDiagCfgTimeout_Object = MibTableColumn
extremeWirelessClientDiagCfgTimeout = _ExtremeWirelessClientDiagCfgTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 31, 1, 4),
    _ExtremeWirelessClientDiagCfgTimeout_Type()
)
extremeWirelessClientDiagCfgTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagCfgTimeout.setStatus("current")
_ExtremeWirelessClientDiagStatusTable_Object = MibTable
extremeWirelessClientDiagStatusTable = _ExtremeWirelessClientDiagStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 32)
)
if mibBuilder.loadTexts:
    extremeWirelessClientDiagStatusTable.setStatus("current")
_ExtremeWirelessClientDiagStatusEntry_Object = MibTableRow
extremeWirelessClientDiagStatusEntry = _ExtremeWirelessClientDiagStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 32, 1)
)
extremeWirelessClientDiagStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessClientDiagStatusEntry.setStatus("current")
_ExtremeWirelessClientDiagCurrentTableSize_Type = Unsigned32
_ExtremeWirelessClientDiagCurrentTableSize_Object = MibTableColumn
extremeWirelessClientDiagCurrentTableSize = _ExtremeWirelessClientDiagCurrentTableSize_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 32, 1, 1),
    _ExtremeWirelessClientDiagCurrentTableSize_Type()
)
extremeWirelessClientDiagCurrentTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagCurrentTableSize.setStatus("current")
_ExtremeWirelessClientDiagTableWatermark_Type = Unsigned32
_ExtremeWirelessClientDiagTableWatermark_Object = MibTableColumn
extremeWirelessClientDiagTableWatermark = _ExtremeWirelessClientDiagTableWatermark_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 32, 1, 2),
    _ExtremeWirelessClientDiagTableWatermark_Type()
)
extremeWirelessClientDiagTableWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagTableWatermark.setStatus("current")
_ExtremeWirelessClientDiagTotalOverflows_Type = Unsigned32
_ExtremeWirelessClientDiagTotalOverflows_Object = MibTableColumn
extremeWirelessClientDiagTotalOverflows = _ExtremeWirelessClientDiagTotalOverflows_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 32, 1, 3),
    _ExtremeWirelessClientDiagTotalOverflows_Type()
)
extremeWirelessClientDiagTotalOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagTotalOverflows.setStatus("current")
_ExtremeWirelessClientDiagTotalTimeouts_Type = Unsigned32
_ExtremeWirelessClientDiagTotalTimeouts_Object = MibTableColumn
extremeWirelessClientDiagTotalTimeouts = _ExtremeWirelessClientDiagTotalTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 32, 1, 4),
    _ExtremeWirelessClientDiagTotalTimeouts_Type()
)
extremeWirelessClientDiagTotalTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagTotalTimeouts.setStatus("current")
_ExtremeWirelessClientDiagLastElement_Type = TimeTicks
_ExtremeWirelessClientDiagLastElement_Object = MibTableColumn
extremeWirelessClientDiagLastElement = _ExtremeWirelessClientDiagLastElement_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 32, 1, 5),
    _ExtremeWirelessClientDiagLastElement_Type()
)
extremeWirelessClientDiagLastElement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagLastElement.setStatus("current")
_ExtremeWirelessClientDiagSupportsSpeedCounters_Type = TruthValue
_ExtremeWirelessClientDiagSupportsSpeedCounters_Object = MibTableColumn
extremeWirelessClientDiagSupportsSpeedCounters = _ExtremeWirelessClientDiagSupportsSpeedCounters_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 32, 1, 6),
    _ExtremeWirelessClientDiagSupportsSpeedCounters_Type()
)
extremeWirelessClientDiagSupportsSpeedCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagSupportsSpeedCounters.setStatus("current")
_ExtremeWirelessClientDiagSupportsSizeCounters_Type = TruthValue
_ExtremeWirelessClientDiagSupportsSizeCounters_Object = MibTableColumn
extremeWirelessClientDiagSupportsSizeCounters = _ExtremeWirelessClientDiagSupportsSizeCounters_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 32, 1, 7),
    _ExtremeWirelessClientDiagSupportsSizeCounters_Type()
)
extremeWirelessClientDiagSupportsSizeCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagSupportsSizeCounters.setStatus("current")
_ExtremeWirelessClientDiagSupportsPacketCounters_Type = TruthValue
_ExtremeWirelessClientDiagSupportsPacketCounters_Object = MibTableColumn
extremeWirelessClientDiagSupportsPacketCounters = _ExtremeWirelessClientDiagSupportsPacketCounters_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 32, 1, 8),
    _ExtremeWirelessClientDiagSupportsPacketCounters_Type()
)
extremeWirelessClientDiagSupportsPacketCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagSupportsPacketCounters.setStatus("current")
_ExtremeWirelessClientDiagTable_Object = MibTable
extremeWirelessClientDiagTable = _ExtremeWirelessClientDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 33)
)
if mibBuilder.loadTexts:
    extremeWirelessClientDiagTable.setStatus("current")
_ExtremeWirelessClientDiagEntry_Object = MibTableRow
extremeWirelessClientDiagEntry = _ExtremeWirelessClientDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 33, 1)
)
extremeWirelessClientDiagEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessClientDiagMac"),
)
if mibBuilder.loadTexts:
    extremeWirelessClientDiagEntry.setStatus("current")
_ExtremeWirelessClientDiagMac_Type = MacAddress
_ExtremeWirelessClientDiagMac_Object = MibTableColumn
extremeWirelessClientDiagMac = _ExtremeWirelessClientDiagMac_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 33, 1, 1),
    _ExtremeWirelessClientDiagMac_Type()
)
extremeWirelessClientDiagMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagMac.setStatus("current")
_ExtremeWirelessClientDiagStateWatermark_Type = Integer32
_ExtremeWirelessClientDiagStateWatermark_Object = MibTableColumn
extremeWirelessClientDiagStateWatermark = _ExtremeWirelessClientDiagStateWatermark_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 33, 1, 2),
    _ExtremeWirelessClientDiagStateWatermark_Type()
)
extremeWirelessClientDiagStateWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagStateWatermark.setStatus("current")
_ExtremeWirelessClientDiagEntersInDetected_Type = Unsigned32
_ExtremeWirelessClientDiagEntersInDetected_Object = MibTableColumn
extremeWirelessClientDiagEntersInDetected = _ExtremeWirelessClientDiagEntersInDetected_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 33, 1, 3),
    _ExtremeWirelessClientDiagEntersInDetected_Type()
)
extremeWirelessClientDiagEntersInDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagEntersInDetected.setStatus("current")
_ExtremeWirelessClientDiagErrorsInDetected_Type = Unsigned32
_ExtremeWirelessClientDiagErrorsInDetected_Object = MibTableColumn
extremeWirelessClientDiagErrorsInDetected = _ExtremeWirelessClientDiagErrorsInDetected_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 33, 1, 4),
    _ExtremeWirelessClientDiagErrorsInDetected_Type()
)
extremeWirelessClientDiagErrorsInDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagErrorsInDetected.setStatus("current")
_ExtremeWirelessClientDiagAuthReqInDetected_Type = Unsigned32
_ExtremeWirelessClientDiagAuthReqInDetected_Object = MibTableColumn
extremeWirelessClientDiagAuthReqInDetected = _ExtremeWirelessClientDiagAuthReqInDetected_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 33, 1, 5),
    _ExtremeWirelessClientDiagAuthReqInDetected_Type()
)
extremeWirelessClientDiagAuthReqInDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagAuthReqInDetected.setStatus("current")
_ExtremeWirelessClientDiagOtherReqInDetected_Type = Unsigned32
_ExtremeWirelessClientDiagOtherReqInDetected_Object = MibTableColumn
extremeWirelessClientDiagOtherReqInDetected = _ExtremeWirelessClientDiagOtherReqInDetected_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 33, 1, 6),
    _ExtremeWirelessClientDiagOtherReqInDetected_Type()
)
extremeWirelessClientDiagOtherReqInDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagOtherReqInDetected.setStatus("current")
_ExtremeWirelessClientDiagMgmtActionInDetected_Type = Unsigned32
_ExtremeWirelessClientDiagMgmtActionInDetected_Object = MibTableColumn
extremeWirelessClientDiagMgmtActionInDetected = _ExtremeWirelessClientDiagMgmtActionInDetected_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 33, 1, 7),
    _ExtremeWirelessClientDiagMgmtActionInDetected_Type()
)
extremeWirelessClientDiagMgmtActionInDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagMgmtActionInDetected.setStatus("current")
_ExtremeWirelessClientDiagTimeOutInDetected_Type = Unsigned32
_ExtremeWirelessClientDiagTimeOutInDetected_Object = MibTableColumn
extremeWirelessClientDiagTimeOutInDetected = _ExtremeWirelessClientDiagTimeOutInDetected_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 33, 1, 8),
    _ExtremeWirelessClientDiagTimeOutInDetected_Type()
)
extremeWirelessClientDiagTimeOutInDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagTimeOutInDetected.setStatus("current")
_ExtremeWirelessClientDiagEntersInAuth_Type = Unsigned32
_ExtremeWirelessClientDiagEntersInAuth_Object = MibTableColumn
extremeWirelessClientDiagEntersInAuth = _ExtremeWirelessClientDiagEntersInAuth_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 33, 1, 9),
    _ExtremeWirelessClientDiagEntersInAuth_Type()
)
extremeWirelessClientDiagEntersInAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagEntersInAuth.setStatus("current")
_ExtremeWirelessClientDiagErrorsInAuth_Type = Unsigned32
_ExtremeWirelessClientDiagErrorsInAuth_Object = MibTableColumn
extremeWirelessClientDiagErrorsInAuth = _ExtremeWirelessClientDiagErrorsInAuth_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 33, 1, 10),
    _ExtremeWirelessClientDiagErrorsInAuth_Type()
)
extremeWirelessClientDiagErrorsInAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagErrorsInAuth.setStatus("current")
_ExtremeWirelessClientDiagAssocReqInAuth_Type = Unsigned32
_ExtremeWirelessClientDiagAssocReqInAuth_Object = MibTableColumn
extremeWirelessClientDiagAssocReqInAuth = _ExtremeWirelessClientDiagAssocReqInAuth_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 33, 1, 11),
    _ExtremeWirelessClientDiagAssocReqInAuth_Type()
)
extremeWirelessClientDiagAssocReqInAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagAssocReqInAuth.setStatus("current")
_ExtremeWirelessClientDiagOtherReqInAuth_Type = Unsigned32
_ExtremeWirelessClientDiagOtherReqInAuth_Object = MibTableColumn
extremeWirelessClientDiagOtherReqInAuth = _ExtremeWirelessClientDiagOtherReqInAuth_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 33, 1, 12),
    _ExtremeWirelessClientDiagOtherReqInAuth_Type()
)
extremeWirelessClientDiagOtherReqInAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagOtherReqInAuth.setStatus("current")
_ExtremeWirelessClientDiagMgmtActionInAuth_Type = Unsigned32
_ExtremeWirelessClientDiagMgmtActionInAuth_Object = MibTableColumn
extremeWirelessClientDiagMgmtActionInAuth = _ExtremeWirelessClientDiagMgmtActionInAuth_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 33, 1, 13),
    _ExtremeWirelessClientDiagMgmtActionInAuth_Type()
)
extremeWirelessClientDiagMgmtActionInAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagMgmtActionInAuth.setStatus("current")
_ExtremeWirelessClientDiagTimeOutInAuth_Type = Unsigned32
_ExtremeWirelessClientDiagTimeOutInAuth_Object = MibTableColumn
extremeWirelessClientDiagTimeOutInAuth = _ExtremeWirelessClientDiagTimeOutInAuth_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 33, 1, 14),
    _ExtremeWirelessClientDiagTimeOutInAuth_Type()
)
extremeWirelessClientDiagTimeOutInAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagTimeOutInAuth.setStatus("current")
_ExtremeWirelessClientDiagEntersInAssoc_Type = Unsigned32
_ExtremeWirelessClientDiagEntersInAssoc_Object = MibTableColumn
extremeWirelessClientDiagEntersInAssoc = _ExtremeWirelessClientDiagEntersInAssoc_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 33, 1, 15),
    _ExtremeWirelessClientDiagEntersInAssoc_Type()
)
extremeWirelessClientDiagEntersInAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagEntersInAssoc.setStatus("current")
_ExtremeWirelessClientDiagErrorsInAssoc_Type = Unsigned32
_ExtremeWirelessClientDiagErrorsInAssoc_Object = MibTableColumn
extremeWirelessClientDiagErrorsInAssoc = _ExtremeWirelessClientDiagErrorsInAssoc_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 33, 1, 16),
    _ExtremeWirelessClientDiagErrorsInAssoc_Type()
)
extremeWirelessClientDiagErrorsInAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagErrorsInAssoc.setStatus("current")
_ExtremeWirelessClientDiagMgmtActionInAssoc_Type = Unsigned32
_ExtremeWirelessClientDiagMgmtActionInAssoc_Object = MibTableColumn
extremeWirelessClientDiagMgmtActionInAssoc = _ExtremeWirelessClientDiagMgmtActionInAssoc_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 33, 1, 17),
    _ExtremeWirelessClientDiagMgmtActionInAssoc_Type()
)
extremeWirelessClientDiagMgmtActionInAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagMgmtActionInAssoc.setStatus("current")
_ExtremeWirelessClientDiagTimeOutInAssoc_Type = Unsigned32
_ExtremeWirelessClientDiagTimeOutInAssoc_Object = MibTableColumn
extremeWirelessClientDiagTimeOutInAssoc = _ExtremeWirelessClientDiagTimeOutInAssoc_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 33, 1, 18),
    _ExtremeWirelessClientDiagTimeOutInAssoc_Type()
)
extremeWirelessClientDiagTimeOutInAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagTimeOutInAssoc.setStatus("current")
_ExtremeWirelessClientDiagEntersInForward_Type = Unsigned32
_ExtremeWirelessClientDiagEntersInForward_Object = MibTableColumn
extremeWirelessClientDiagEntersInForward = _ExtremeWirelessClientDiagEntersInForward_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 33, 1, 19),
    _ExtremeWirelessClientDiagEntersInForward_Type()
)
extremeWirelessClientDiagEntersInForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagEntersInForward.setStatus("current")
_ExtremeWirelessClientDiagMgmtActionInForward_Type = Unsigned32
_ExtremeWirelessClientDiagMgmtActionInForward_Object = MibTableColumn
extremeWirelessClientDiagMgmtActionInForward = _ExtremeWirelessClientDiagMgmtActionInForward_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 33, 1, 20),
    _ExtremeWirelessClientDiagMgmtActionInForward_Type()
)
extremeWirelessClientDiagMgmtActionInForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagMgmtActionInForward.setStatus("current")
_ExtremeWirelessClientDiagTimeOutInForward_Type = Unsigned32
_ExtremeWirelessClientDiagTimeOutInForward_Object = MibTableColumn
extremeWirelessClientDiagTimeOutInForward = _ExtremeWirelessClientDiagTimeOutInForward_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 33, 1, 21),
    _ExtremeWirelessClientDiagTimeOutInForward_Type()
)
extremeWirelessClientDiagTimeOutInForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagTimeOutInForward.setStatus("current")
_ExtremeWirelessClientDiagTotal802Auths_Type = Unsigned32
_ExtremeWirelessClientDiagTotal802Auths_Object = MibTableColumn
extremeWirelessClientDiagTotal802Auths = _ExtremeWirelessClientDiagTotal802Auths_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 33, 1, 22),
    _ExtremeWirelessClientDiagTotal802Auths_Type()
)
extremeWirelessClientDiagTotal802Auths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagTotal802Auths.setStatus("current")
_ExtremeWirelessClientDiagTotalNetLoginAuths_Type = Unsigned32
_ExtremeWirelessClientDiagTotalNetLoginAuths_Object = MibTableColumn
extremeWirelessClientDiagTotalNetLoginAuths = _ExtremeWirelessClientDiagTotalNetLoginAuths_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 33, 1, 23),
    _ExtremeWirelessClientDiagTotalNetLoginAuths_Type()
)
extremeWirelessClientDiagTotalNetLoginAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagTotalNetLoginAuths.setStatus("current")
_ExtremeWirelessClientAssocInfoTable_Object = MibTable
extremeWirelessClientAssocInfoTable = _ExtremeWirelessClientAssocInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34)
)
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoTable.setStatus("current")
_ExtremeWirelessClientAssocInfoEntry_Object = MibTableRow
extremeWirelessClientAssocInfoEntry = _ExtremeWirelessClientAssocInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1)
)
extremeWirelessClientAssocInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessClientDiagMac"),
)
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoEntry.setStatus("current")
_ExtremeWirelessClientAssocInfoAssociated_Type = TruthValue
_ExtremeWirelessClientAssocInfoAssociated_Object = MibTableColumn
extremeWirelessClientAssocInfoAssociated = _ExtremeWirelessClientAssocInfoAssociated_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 1),
    _ExtremeWirelessClientAssocInfoAssociated_Type()
)
extremeWirelessClientAssocInfoAssociated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoAssociated.setStatus("current")
_ExtremeWirelessClientAssocInfoTotalAssocReq_Type = Unsigned32
_ExtremeWirelessClientAssocInfoTotalAssocReq_Object = MibTableColumn
extremeWirelessClientAssocInfoTotalAssocReq = _ExtremeWirelessClientAssocInfoTotalAssocReq_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 2),
    _ExtremeWirelessClientAssocInfoTotalAssocReq_Type()
)
extremeWirelessClientAssocInfoTotalAssocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoTotalAssocReq.setStatus("current")
_ExtremeWirelessClientAssocInfoTotalReAssocReq_Type = Unsigned32
_ExtremeWirelessClientAssocInfoTotalReAssocReq_Object = MibTableColumn
extremeWirelessClientAssocInfoTotalReAssocReq = _ExtremeWirelessClientAssocInfoTotalReAssocReq_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 3),
    _ExtremeWirelessClientAssocInfoTotalReAssocReq_Type()
)
extremeWirelessClientAssocInfoTotalReAssocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoTotalReAssocReq.setStatus("current")
_ExtremeWirelessClientAssocInfoTotalAssocResp_Type = Unsigned32
_ExtremeWirelessClientAssocInfoTotalAssocResp_Object = MibTableColumn
extremeWirelessClientAssocInfoTotalAssocResp = _ExtremeWirelessClientAssocInfoTotalAssocResp_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 4),
    _ExtremeWirelessClientAssocInfoTotalAssocResp_Type()
)
extremeWirelessClientAssocInfoTotalAssocResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoTotalAssocResp.setStatus("current")
_ExtremeWirelessClientAssocInfoTotalAssocOK_Type = Unsigned32
_ExtremeWirelessClientAssocInfoTotalAssocOK_Object = MibTableColumn
extremeWirelessClientAssocInfoTotalAssocOK = _ExtremeWirelessClientAssocInfoTotalAssocOK_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 5),
    _ExtremeWirelessClientAssocInfoTotalAssocOK_Type()
)
extremeWirelessClientAssocInfoTotalAssocOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoTotalAssocOK.setStatus("current")
_ExtremeWirelessClientAssocInfoTotalAssocFail_Type = Unsigned32
_ExtremeWirelessClientAssocInfoTotalAssocFail_Object = MibTableColumn
extremeWirelessClientAssocInfoTotalAssocFail = _ExtremeWirelessClientAssocInfoTotalAssocFail_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 6),
    _ExtremeWirelessClientAssocInfoTotalAssocFail_Type()
)
extremeWirelessClientAssocInfoTotalAssocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoTotalAssocFail.setStatus("current")
_ExtremeWirelessClientAssocInfoTotalDisassocReq_Type = Unsigned32
_ExtremeWirelessClientAssocInfoTotalDisassocReq_Object = MibTableColumn
extremeWirelessClientAssocInfoTotalDisassocReq = _ExtremeWirelessClientAssocInfoTotalDisassocReq_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 7),
    _ExtremeWirelessClientAssocInfoTotalDisassocReq_Type()
)
extremeWirelessClientAssocInfoTotalDisassocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoTotalDisassocReq.setStatus("current")
_ExtremeWirelessClientAssocInfoTotalDisassocResp_Type = Unsigned32
_ExtremeWirelessClientAssocInfoTotalDisassocResp_Object = MibTableColumn
extremeWirelessClientAssocInfoTotalDisassocResp = _ExtremeWirelessClientAssocInfoTotalDisassocResp_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 8),
    _ExtremeWirelessClientAssocInfoTotalDisassocResp_Type()
)
extremeWirelessClientAssocInfoTotalDisassocResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoTotalDisassocResp.setStatus("current")
_ExtremeWirelessClientAssocInfoRateIE_Type = OctetString
_ExtremeWirelessClientAssocInfoRateIE_Object = MibTableColumn
extremeWirelessClientAssocInfoRateIE = _ExtremeWirelessClientAssocInfoRateIE_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 9),
    _ExtremeWirelessClientAssocInfoRateIE_Type()
)
extremeWirelessClientAssocInfoRateIE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoRateIE.setStatus("current")
_ExtremeWirelessClientAssocInfoLastAssoc_Type = TimeTicks
_ExtremeWirelessClientAssocInfoLastAssoc_Object = MibTableColumn
extremeWirelessClientAssocInfoLastAssoc = _ExtremeWirelessClientAssocInfoLastAssoc_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 10),
    _ExtremeWirelessClientAssocInfoLastAssoc_Type()
)
extremeWirelessClientAssocInfoLastAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoLastAssoc.setStatus("current")
_ExtremeWirelessClientAssocInfoLastError_Type = TimeTicks
_ExtremeWirelessClientAssocInfoLastError_Object = MibTableColumn
extremeWirelessClientAssocInfoLastError = _ExtremeWirelessClientAssocInfoLastError_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 11),
    _ExtremeWirelessClientAssocInfoLastError_Type()
)
extremeWirelessClientAssocInfoLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoLastError.setStatus("current")


class _ExtremeWirelessClientAssocInfoLastErrorType_Type(Integer32):
    """Custom type extremeWirelessClientAssocInfoLastErrorType based on Integer32"""
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("badCapability", 3),
          ("badState", 2),
          ("couterMeasure", 4),
          ("maxAssoc", 6),
          ("mcastCipher", 5),
          ("noError", 0),
          ("otherError", 9),
          ("rateMismatch", 1),
          ("rsnMismatch", 8),
          ("rsnRequired", 7))
    )


_ExtremeWirelessClientAssocInfoLastErrorType_Type.__name__ = "Integer32"
_ExtremeWirelessClientAssocInfoLastErrorType_Object = MibTableColumn
extremeWirelessClientAssocInfoLastErrorType = _ExtremeWirelessClientAssocInfoLastErrorType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 12),
    _ExtremeWirelessClientAssocInfoLastErrorType_Type()
)
extremeWirelessClientAssocInfoLastErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoLastErrorType.setStatus("current")
_ExtremeWirelessClientAssocInfoErrorRateMismatch_Type = Unsigned32
_ExtremeWirelessClientAssocInfoErrorRateMismatch_Object = MibTableColumn
extremeWirelessClientAssocInfoErrorRateMismatch = _ExtremeWirelessClientAssocInfoErrorRateMismatch_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 13),
    _ExtremeWirelessClientAssocInfoErrorRateMismatch_Type()
)
extremeWirelessClientAssocInfoErrorRateMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoErrorRateMismatch.setStatus("current")
_ExtremeWirelessClientAssocInfoErrorBadState_Type = Unsigned32
_ExtremeWirelessClientAssocInfoErrorBadState_Object = MibTableColumn
extremeWirelessClientAssocInfoErrorBadState = _ExtremeWirelessClientAssocInfoErrorBadState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 14),
    _ExtremeWirelessClientAssocInfoErrorBadState_Type()
)
extremeWirelessClientAssocInfoErrorBadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoErrorBadState.setStatus("current")
_ExtremeWirelessClientAssocInfoErrorBadCapability_Type = Unsigned32
_ExtremeWirelessClientAssocInfoErrorBadCapability_Object = MibTableColumn
extremeWirelessClientAssocInfoErrorBadCapability = _ExtremeWirelessClientAssocInfoErrorBadCapability_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 15),
    _ExtremeWirelessClientAssocInfoErrorBadCapability_Type()
)
extremeWirelessClientAssocInfoErrorBadCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoErrorBadCapability.setStatus("current")
_ExtremeWirelessClientAssocInfoErrorCounterMeasure_Type = Unsigned32
_ExtremeWirelessClientAssocInfoErrorCounterMeasure_Object = MibTableColumn
extremeWirelessClientAssocInfoErrorCounterMeasure = _ExtremeWirelessClientAssocInfoErrorCounterMeasure_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 16),
    _ExtremeWirelessClientAssocInfoErrorCounterMeasure_Type()
)
extremeWirelessClientAssocInfoErrorCounterMeasure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoErrorCounterMeasure.setStatus("current")
_ExtremeWirelessClientAssocInfoErrorMcastCipher_Type = Unsigned32
_ExtremeWirelessClientAssocInfoErrorMcastCipher_Object = MibTableColumn
extremeWirelessClientAssocInfoErrorMcastCipher = _ExtremeWirelessClientAssocInfoErrorMcastCipher_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 17),
    _ExtremeWirelessClientAssocInfoErrorMcastCipher_Type()
)
extremeWirelessClientAssocInfoErrorMcastCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoErrorMcastCipher.setStatus("current")
_ExtremeWirelessClientAssocInfoErrorMaxAssoc_Type = Unsigned32
_ExtremeWirelessClientAssocInfoErrorMaxAssoc_Object = MibTableColumn
extremeWirelessClientAssocInfoErrorMaxAssoc = _ExtremeWirelessClientAssocInfoErrorMaxAssoc_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 18),
    _ExtremeWirelessClientAssocInfoErrorMaxAssoc_Type()
)
extremeWirelessClientAssocInfoErrorMaxAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoErrorMaxAssoc.setStatus("current")
_ExtremeWirelessClientAssocInfoErrorRSNRequired_Type = Unsigned32
_ExtremeWirelessClientAssocInfoErrorRSNRequired_Object = MibTableColumn
extremeWirelessClientAssocInfoErrorRSNRequired = _ExtremeWirelessClientAssocInfoErrorRSNRequired_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 19),
    _ExtremeWirelessClientAssocInfoErrorRSNRequired_Type()
)
extremeWirelessClientAssocInfoErrorRSNRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoErrorRSNRequired.setStatus("current")
_ExtremeWirelessClientAssocInfoErrorRSNMismatch_Type = Unsigned32
_ExtremeWirelessClientAssocInfoErrorRSNMismatch_Object = MibTableColumn
extremeWirelessClientAssocInfoErrorRSNMismatch = _ExtremeWirelessClientAssocInfoErrorRSNMismatch_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 20),
    _ExtremeWirelessClientAssocInfoErrorRSNMismatch_Type()
)
extremeWirelessClientAssocInfoErrorRSNMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoErrorRSNMismatch.setStatus("current")
_ExtremeWirelessClientAssocInfoErrorOther_Type = Unsigned32
_ExtremeWirelessClientAssocInfoErrorOther_Object = MibTableColumn
extremeWirelessClientAssocInfoErrorOther = _ExtremeWirelessClientAssocInfoErrorOther_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 21),
    _ExtremeWirelessClientAssocInfoErrorOther_Type()
)
extremeWirelessClientAssocInfoErrorOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoErrorOther.setStatus("current")
_ExtremeWirelessClientAssocInfoWPAIEPresent_Type = TruthValue
_ExtremeWirelessClientAssocInfoWPAIEPresent_Object = MibTableColumn
extremeWirelessClientAssocInfoWPAIEPresent = _ExtremeWirelessClientAssocInfoWPAIEPresent_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 22),
    _ExtremeWirelessClientAssocInfoWPAIEPresent_Type()
)
extremeWirelessClientAssocInfoWPAIEPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoWPAIEPresent.setStatus("current")
_ExtremeWirelessClientAssocInfoWPAVersion_Type = Unsigned32
_ExtremeWirelessClientAssocInfoWPAVersion_Object = MibTableColumn
extremeWirelessClientAssocInfoWPAVersion = _ExtremeWirelessClientAssocInfoWPAVersion_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 23),
    _ExtremeWirelessClientAssocInfoWPAVersion_Type()
)
extremeWirelessClientAssocInfoWPAVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoWPAVersion.setStatus("current")
_ExtremeWirelessClientAssocInfoWPAIEMcastCipher_Type = WPACipherSet
_ExtremeWirelessClientAssocInfoWPAIEMcastCipher_Object = MibTableColumn
extremeWirelessClientAssocInfoWPAIEMcastCipher = _ExtremeWirelessClientAssocInfoWPAIEMcastCipher_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 24),
    _ExtremeWirelessClientAssocInfoWPAIEMcastCipher_Type()
)
extremeWirelessClientAssocInfoWPAIEMcastCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoWPAIEMcastCipher.setStatus("current")
_ExtremeWirelessClientAssocInfoWPAUcastCipherCount_Type = Unsigned32
_ExtremeWirelessClientAssocInfoWPAUcastCipherCount_Object = MibTableColumn
extremeWirelessClientAssocInfoWPAUcastCipherCount = _ExtremeWirelessClientAssocInfoWPAUcastCipherCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 25),
    _ExtremeWirelessClientAssocInfoWPAUcastCipherCount_Type()
)
extremeWirelessClientAssocInfoWPAUcastCipherCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoWPAUcastCipherCount.setStatus("current")
_ExtremeWirelessClientAssocInfoWPAUcastCipher_Type = WPACipherSet
_ExtremeWirelessClientAssocInfoWPAUcastCipher_Object = MibTableColumn
extremeWirelessClientAssocInfoWPAUcastCipher = _ExtremeWirelessClientAssocInfoWPAUcastCipher_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 26),
    _ExtremeWirelessClientAssocInfoWPAUcastCipher_Type()
)
extremeWirelessClientAssocInfoWPAUcastCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoWPAUcastCipher.setStatus("current")
_ExtremeWirelessClientAssocInfoWPAKeyMgmtCount_Type = Unsigned32
_ExtremeWirelessClientAssocInfoWPAKeyMgmtCount_Object = MibTableColumn
extremeWirelessClientAssocInfoWPAKeyMgmtCount = _ExtremeWirelessClientAssocInfoWPAKeyMgmtCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 27),
    _ExtremeWirelessClientAssocInfoWPAKeyMgmtCount_Type()
)
extremeWirelessClientAssocInfoWPAKeyMgmtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoWPAKeyMgmtCount.setStatus("current")
_ExtremeWirelessClientAssocInfoWPAKeyMgmtSuite_Type = WPAKeyMgmtSet
_ExtremeWirelessClientAssocInfoWPAKeyMgmtSuite_Object = MibTableColumn
extremeWirelessClientAssocInfoWPAKeyMgmtSuite = _ExtremeWirelessClientAssocInfoWPAKeyMgmtSuite_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 28),
    _ExtremeWirelessClientAssocInfoWPAKeyMgmtSuite_Type()
)
extremeWirelessClientAssocInfoWPAKeyMgmtSuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocInfoWPAKeyMgmtSuite.setStatus("current")
_ExtremeWirelessClientAssocIEBlob_Type = OctetString
_ExtremeWirelessClientAssocIEBlob_Object = MibTableColumn
extremeWirelessClientAssocIEBlob = _ExtremeWirelessClientAssocIEBlob_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 34, 1, 29),
    _ExtremeWirelessClientAssocIEBlob_Type()
)
extremeWirelessClientAssocIEBlob.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocIEBlob.setStatus("current")
_ExtremeWirelessClientAuthInfoTable_Object = MibTable
extremeWirelessClientAuthInfoTable = _ExtremeWirelessClientAuthInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 35)
)
if mibBuilder.loadTexts:
    extremeWirelessClientAuthInfoTable.setStatus("current")
_ExtremeWirelessClientAuthInfoEntry_Object = MibTableRow
extremeWirelessClientAuthInfoEntry = _ExtremeWirelessClientAuthInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 35, 1)
)
extremeWirelessClientAuthInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessClientDiagMac"),
)
if mibBuilder.loadTexts:
    extremeWirelessClientAuthInfoEntry.setStatus("current")
_ExtremeWirelessClientAuthInfoCurrentAuth_Type = TruthValue
_ExtremeWirelessClientAuthInfoCurrentAuth_Object = MibTableColumn
extremeWirelessClientAuthInfoCurrentAuth = _ExtremeWirelessClientAuthInfoCurrentAuth_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 35, 1, 1),
    _ExtremeWirelessClientAuthInfoCurrentAuth_Type()
)
extremeWirelessClientAuthInfoCurrentAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAuthInfoCurrentAuth.setStatus("current")
_ExtremeWirelessClientAuthInfoTotalAuths_Type = Unsigned32
_ExtremeWirelessClientAuthInfoTotalAuths_Object = MibTableColumn
extremeWirelessClientAuthInfoTotalAuths = _ExtremeWirelessClientAuthInfoTotalAuths_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 35, 1, 2),
    _ExtremeWirelessClientAuthInfoTotalAuths_Type()
)
extremeWirelessClientAuthInfoTotalAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAuthInfoTotalAuths.setStatus("current")
_ExtremeWirelessClientAuthInfoTotalAuthResp_Type = Unsigned32
_ExtremeWirelessClientAuthInfoTotalAuthResp_Object = MibTableColumn
extremeWirelessClientAuthInfoTotalAuthResp = _ExtremeWirelessClientAuthInfoTotalAuthResp_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 35, 1, 3),
    _ExtremeWirelessClientAuthInfoTotalAuthResp_Type()
)
extremeWirelessClientAuthInfoTotalAuthResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAuthInfoTotalAuthResp.setStatus("current")
_ExtremeWirelessClientAuthInfoTotalAuthsOK_Type = Unsigned32
_ExtremeWirelessClientAuthInfoTotalAuthsOK_Object = MibTableColumn
extremeWirelessClientAuthInfoTotalAuthsOK = _ExtremeWirelessClientAuthInfoTotalAuthsOK_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 35, 1, 4),
    _ExtremeWirelessClientAuthInfoTotalAuthsOK_Type()
)
extremeWirelessClientAuthInfoTotalAuthsOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAuthInfoTotalAuthsOK.setStatus("current")
_ExtremeWirelessClientAuthInfoTotalAuthsFailed_Type = Unsigned32
_ExtremeWirelessClientAuthInfoTotalAuthsFailed_Object = MibTableColumn
extremeWirelessClientAuthInfoTotalAuthsFailed = _ExtremeWirelessClientAuthInfoTotalAuthsFailed_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 35, 1, 5),
    _ExtremeWirelessClientAuthInfoTotalAuthsFailed_Type()
)
extremeWirelessClientAuthInfoTotalAuthsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAuthInfoTotalAuthsFailed.setStatus("current")
_ExtremeWirelessClientAuthInfoTotalDeauthReq_Type = Unsigned32
_ExtremeWirelessClientAuthInfoTotalDeauthReq_Object = MibTableColumn
extremeWirelessClientAuthInfoTotalDeauthReq = _ExtremeWirelessClientAuthInfoTotalDeauthReq_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 35, 1, 6),
    _ExtremeWirelessClientAuthInfoTotalDeauthReq_Type()
)
extremeWirelessClientAuthInfoTotalDeauthReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAuthInfoTotalDeauthReq.setStatus("current")
_ExtremeWirelessClientAuthInfoTotalDeauthResp_Type = Unsigned32
_ExtremeWirelessClientAuthInfoTotalDeauthResp_Object = MibTableColumn
extremeWirelessClientAuthInfoTotalDeauthResp = _ExtremeWirelessClientAuthInfoTotalDeauthResp_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 35, 1, 7),
    _ExtremeWirelessClientAuthInfoTotalDeauthResp_Type()
)
extremeWirelessClientAuthInfoTotalDeauthResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAuthInfoTotalDeauthResp.setStatus("current")
_ExtremeWirelessClientAuthInfoTotalOpen_Type = Unsigned32
_ExtremeWirelessClientAuthInfoTotalOpen_Object = MibTableColumn
extremeWirelessClientAuthInfoTotalOpen = _ExtremeWirelessClientAuthInfoTotalOpen_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 35, 1, 8),
    _ExtremeWirelessClientAuthInfoTotalOpen_Type()
)
extremeWirelessClientAuthInfoTotalOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAuthInfoTotalOpen.setStatus("current")
_ExtremeWirelessClientAuthInfoTotalShared_Type = Unsigned32
_ExtremeWirelessClientAuthInfoTotalShared_Object = MibTableColumn
extremeWirelessClientAuthInfoTotalShared = _ExtremeWirelessClientAuthInfoTotalShared_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 35, 1, 9),
    _ExtremeWirelessClientAuthInfoTotalShared_Type()
)
extremeWirelessClientAuthInfoTotalShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAuthInfoTotalShared.setStatus("current")
_ExtremeWirelessClientAuthInfoLastAuth_Type = TimeTicks
_ExtremeWirelessClientAuthInfoLastAuth_Object = MibTableColumn
extremeWirelessClientAuthInfoLastAuth = _ExtremeWirelessClientAuthInfoLastAuth_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 35, 1, 10),
    _ExtremeWirelessClientAuthInfoLastAuth_Type()
)
extremeWirelessClientAuthInfoLastAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAuthInfoLastAuth.setStatus("current")


class _ExtremeWirelessClientAuthInfoLastAuthType_Type(Integer32):
    """Custom type extremeWirelessClientAuthInfoLastAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("shared", 2))
    )


_ExtremeWirelessClientAuthInfoLastAuthType_Type.__name__ = "Integer32"
_ExtremeWirelessClientAuthInfoLastAuthType_Object = MibTableColumn
extremeWirelessClientAuthInfoLastAuthType = _ExtremeWirelessClientAuthInfoLastAuthType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 35, 1, 11),
    _ExtremeWirelessClientAuthInfoLastAuthType_Type()
)
extremeWirelessClientAuthInfoLastAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAuthInfoLastAuthType.setStatus("current")
_ExtremeWirelessClientAuthInfoLastError_Type = TimeTicks
_ExtremeWirelessClientAuthInfoLastError_Object = MibTableColumn
extremeWirelessClientAuthInfoLastError = _ExtremeWirelessClientAuthInfoLastError_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 35, 1, 12),
    _ExtremeWirelessClientAuthInfoLastError_Type()
)
extremeWirelessClientAuthInfoLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAuthInfoLastError.setStatus("current")


class _ExtremeWirelessClientAuthInfoLastErrorType_Type(Integer32):
    """Custom type extremeWirelessClientAuthInfoLastErrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("algorithmMismatch", 4),
          ("challengeText", 3),
          ("keyIndex", 5),
          ("noError", 0),
          ("otherError", 6),
          ("resourceFailure", 1),
          ("sequenceNumber", 2))
    )


_ExtremeWirelessClientAuthInfoLastErrorType_Type.__name__ = "Integer32"
_ExtremeWirelessClientAuthInfoLastErrorType_Object = MibTableColumn
extremeWirelessClientAuthInfoLastErrorType = _ExtremeWirelessClientAuthInfoLastErrorType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 35, 1, 13),
    _ExtremeWirelessClientAuthInfoLastErrorType_Type()
)
extremeWirelessClientAuthInfoLastErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAuthInfoLastErrorType.setStatus("current")
_ExtremeWirelessClientAuthInfoErrorResourceFailure_Type = Unsigned32
_ExtremeWirelessClientAuthInfoErrorResourceFailure_Object = MibTableColumn
extremeWirelessClientAuthInfoErrorResourceFailure = _ExtremeWirelessClientAuthInfoErrorResourceFailure_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 35, 1, 14),
    _ExtremeWirelessClientAuthInfoErrorResourceFailure_Type()
)
extremeWirelessClientAuthInfoErrorResourceFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAuthInfoErrorResourceFailure.setStatus("current")
_ExtremeWirelessClientAuthInfoErrorSequenceNum_Type = Unsigned32
_ExtremeWirelessClientAuthInfoErrorSequenceNum_Object = MibTableColumn
extremeWirelessClientAuthInfoErrorSequenceNum = _ExtremeWirelessClientAuthInfoErrorSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 35, 1, 15),
    _ExtremeWirelessClientAuthInfoErrorSequenceNum_Type()
)
extremeWirelessClientAuthInfoErrorSequenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAuthInfoErrorSequenceNum.setStatus("current")
_ExtremeWirelessClientAuthInfoErrorChallengeText_Type = Unsigned32
_ExtremeWirelessClientAuthInfoErrorChallengeText_Object = MibTableColumn
extremeWirelessClientAuthInfoErrorChallengeText = _ExtremeWirelessClientAuthInfoErrorChallengeText_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 35, 1, 16),
    _ExtremeWirelessClientAuthInfoErrorChallengeText_Type()
)
extremeWirelessClientAuthInfoErrorChallengeText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAuthInfoErrorChallengeText.setStatus("current")
_ExtremeWirelessClientAuthInfoErrorTypeMismatch_Type = Unsigned32
_ExtremeWirelessClientAuthInfoErrorTypeMismatch_Object = MibTableColumn
extremeWirelessClientAuthInfoErrorTypeMismatch = _ExtremeWirelessClientAuthInfoErrorTypeMismatch_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 35, 1, 17),
    _ExtremeWirelessClientAuthInfoErrorTypeMismatch_Type()
)
extremeWirelessClientAuthInfoErrorTypeMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAuthInfoErrorTypeMismatch.setStatus("current")
_ExtremeWirelessClientAuthInfoErrorKeyIndex_Type = Unsigned32
_ExtremeWirelessClientAuthInfoErrorKeyIndex_Object = MibTableColumn
extremeWirelessClientAuthInfoErrorKeyIndex = _ExtremeWirelessClientAuthInfoErrorKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 35, 1, 18),
    _ExtremeWirelessClientAuthInfoErrorKeyIndex_Type()
)
extremeWirelessClientAuthInfoErrorKeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAuthInfoErrorKeyIndex.setStatus("current")
_ExtremeWirelessClientAuthInfoErrorOther_Type = Unsigned32
_ExtremeWirelessClientAuthInfoErrorOther_Object = MibTableColumn
extremeWirelessClientAuthInfoErrorOther = _ExtremeWirelessClientAuthInfoErrorOther_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 35, 1, 19),
    _ExtremeWirelessClientAuthInfoErrorOther_Type()
)
extremeWirelessClientAuthInfoErrorOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAuthInfoErrorOther.setStatus("current")
_ExtremeWirelessClientMACInfoTable_Object = MibTable
extremeWirelessClientMACInfoTable = _ExtremeWirelessClientMACInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 36)
)
if mibBuilder.loadTexts:
    extremeWirelessClientMACInfoTable.setStatus("current")
_ExtremeWirelessClientMACInfoEntry_Object = MibTableRow
extremeWirelessClientMACInfoEntry = _ExtremeWirelessClientMACInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 36, 1)
)
extremeWirelessClientMACInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessClientDiagMac"),
)
if mibBuilder.loadTexts:
    extremeWirelessClientMACInfoEntry.setStatus("current")
_ExtremeWirelessClientMACInfoMinRSS_Type = Integer32
_ExtremeWirelessClientMACInfoMinRSS_Object = MibTableColumn
extremeWirelessClientMACInfoMinRSS = _ExtremeWirelessClientMACInfoMinRSS_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 36, 1, 1),
    _ExtremeWirelessClientMACInfoMinRSS_Type()
)
extremeWirelessClientMACInfoMinRSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientMACInfoMinRSS.setStatus("current")
_ExtremeWirelessClientMACInfoMaxRSS_Type = Integer32
_ExtremeWirelessClientMACInfoMaxRSS_Object = MibTableColumn
extremeWirelessClientMACInfoMaxRSS = _ExtremeWirelessClientMACInfoMaxRSS_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 36, 1, 2),
    _ExtremeWirelessClientMACInfoMaxRSS_Type()
)
extremeWirelessClientMACInfoMaxRSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientMACInfoMaxRSS.setStatus("current")
_ExtremeWirelessClientMACInfoAvgRSS_Type = Integer32
_ExtremeWirelessClientMACInfoAvgRSS_Object = MibTableColumn
extremeWirelessClientMACInfoAvgRSS = _ExtremeWirelessClientMACInfoAvgRSS_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 36, 1, 3),
    _ExtremeWirelessClientMACInfoAvgRSS_Type()
)
extremeWirelessClientMACInfoAvgRSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientMACInfoAvgRSS.setStatus("current")
_ExtremeWirelessClientMACInfoTotalProbeReq_Type = Unsigned32
_ExtremeWirelessClientMACInfoTotalProbeReq_Object = MibTableColumn
extremeWirelessClientMACInfoTotalProbeReq = _ExtremeWirelessClientMACInfoTotalProbeReq_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 36, 1, 4),
    _ExtremeWirelessClientMACInfoTotalProbeReq_Type()
)
extremeWirelessClientMACInfoTotalProbeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientMACInfoTotalProbeReq.setStatus("current")
_ExtremeWirelessClientMACInfoTotalAuthReq_Type = Unsigned32
_ExtremeWirelessClientMACInfoTotalAuthReq_Object = MibTableColumn
extremeWirelessClientMACInfoTotalAuthReq = _ExtremeWirelessClientMACInfoTotalAuthReq_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 36, 1, 5),
    _ExtremeWirelessClientMACInfoTotalAuthReq_Type()
)
extremeWirelessClientMACInfoTotalAuthReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientMACInfoTotalAuthReq.setStatus("current")
_ExtremeWirelessClientMACInfoTotalAssocReq_Type = Unsigned32
_ExtremeWirelessClientMACInfoTotalAssocReq_Object = MibTableColumn
extremeWirelessClientMACInfoTotalAssocReq = _ExtremeWirelessClientMACInfoTotalAssocReq_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 36, 1, 6),
    _ExtremeWirelessClientMACInfoTotalAssocReq_Type()
)
extremeWirelessClientMACInfoTotalAssocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientMACInfoTotalAssocReq.setStatus("current")
_ExtremeWirelessClientMACInfoTotalReAssocReq_Type = Unsigned32
_ExtremeWirelessClientMACInfoTotalReAssocReq_Object = MibTableColumn
extremeWirelessClientMACInfoTotalReAssocReq = _ExtremeWirelessClientMACInfoTotalReAssocReq_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 36, 1, 7),
    _ExtremeWirelessClientMACInfoTotalReAssocReq_Type()
)
extremeWirelessClientMACInfoTotalReAssocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientMACInfoTotalReAssocReq.setStatus("current")
_ExtremeWirelessClientMACInfoTotalDeAssocReq_Type = Unsigned32
_ExtremeWirelessClientMACInfoTotalDeAssocReq_Object = MibTableColumn
extremeWirelessClientMACInfoTotalDeAssocReq = _ExtremeWirelessClientMACInfoTotalDeAssocReq_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 36, 1, 8),
    _ExtremeWirelessClientMACInfoTotalDeAssocReq_Type()
)
extremeWirelessClientMACInfoTotalDeAssocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientMACInfoTotalDeAssocReq.setStatus("current")
_ExtremeWirelessClientMACInfoTotalDeAuthReq_Type = Unsigned32
_ExtremeWirelessClientMACInfoTotalDeAuthReq_Object = MibTableColumn
extremeWirelessClientMACInfoTotalDeAuthReq = _ExtremeWirelessClientMACInfoTotalDeAuthReq_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 36, 1, 9),
    _ExtremeWirelessClientMACInfoTotalDeAuthReq_Type()
)
extremeWirelessClientMACInfoTotalDeAuthReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientMACInfoTotalDeAuthReq.setStatus("current")
_ExtremeWirelessClientMACInfoTotalPsPoll_Type = Unsigned32
_ExtremeWirelessClientMACInfoTotalPsPoll_Object = MibTableColumn
extremeWirelessClientMACInfoTotalPsPoll = _ExtremeWirelessClientMACInfoTotalPsPoll_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 36, 1, 10),
    _ExtremeWirelessClientMACInfoTotalPsPoll_Type()
)
extremeWirelessClientMACInfoTotalPsPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientMACInfoTotalPsPoll.setStatus("current")
_ExtremeWirelessClientMACInfoTotalData_Type = Unsigned32
_ExtremeWirelessClientMACInfoTotalData_Object = MibTableColumn
extremeWirelessClientMACInfoTotalData = _ExtremeWirelessClientMACInfoTotalData_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 36, 1, 11),
    _ExtremeWirelessClientMACInfoTotalData_Type()
)
extremeWirelessClientMACInfoTotalData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientMACInfoTotalData.setStatus("current")
_ExtremeWirelessClientMACInfoNavValue_Type = Unsigned32
_ExtremeWirelessClientMACInfoNavValue_Object = MibTableColumn
extremeWirelessClientMACInfoNavValue = _ExtremeWirelessClientMACInfoNavValue_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 36, 1, 12),
    _ExtremeWirelessClientMACInfoNavValue_Type()
)
extremeWirelessClientMACInfoNavValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientMACInfoNavValue.setStatus("current")
_ExtremeWirelessClientSizeCounterTable_Object = MibTable
extremeWirelessClientSizeCounterTable = _ExtremeWirelessClientSizeCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37)
)
if mibBuilder.loadTexts:
    extremeWirelessClientSizeCounterTable.setStatus("current")
_ExtremeWirelessClientSizeCounterEntry_Object = MibTableRow
extremeWirelessClientSizeCounterEntry = _ExtremeWirelessClientSizeCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1)
)
extremeWirelessClientSizeCounterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessClientDiagMac"),
)
if mibBuilder.loadTexts:
    extremeWirelessClientSizeCounterEntry.setStatus("current")
_ExtremeWirelessClientFrameSizeReXmit64_Type = Unsigned32
_ExtremeWirelessClientFrameSizeReXmit64_Object = MibTableColumn
extremeWirelessClientFrameSizeReXmit64 = _ExtremeWirelessClientFrameSizeReXmit64_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 1),
    _ExtremeWirelessClientFrameSizeReXmit64_Type()
)
extremeWirelessClientFrameSizeReXmit64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeReXmit64.setStatus("current")
_ExtremeWirelessClientFrameSizeReXmit128_Type = Unsigned32
_ExtremeWirelessClientFrameSizeReXmit128_Object = MibTableColumn
extremeWirelessClientFrameSizeReXmit128 = _ExtremeWirelessClientFrameSizeReXmit128_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 2),
    _ExtremeWirelessClientFrameSizeReXmit128_Type()
)
extremeWirelessClientFrameSizeReXmit128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeReXmit128.setStatus("current")
_ExtremeWirelessClientFrameSizeReXmit256_Type = Unsigned32
_ExtremeWirelessClientFrameSizeReXmit256_Object = MibTableColumn
extremeWirelessClientFrameSizeReXmit256 = _ExtremeWirelessClientFrameSizeReXmit256_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 3),
    _ExtremeWirelessClientFrameSizeReXmit256_Type()
)
extremeWirelessClientFrameSizeReXmit256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeReXmit256.setStatus("current")
_ExtremeWirelessClientFrameSizeReXmit512_Type = Unsigned32
_ExtremeWirelessClientFrameSizeReXmit512_Object = MibTableColumn
extremeWirelessClientFrameSizeReXmit512 = _ExtremeWirelessClientFrameSizeReXmit512_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 4),
    _ExtremeWirelessClientFrameSizeReXmit512_Type()
)
extremeWirelessClientFrameSizeReXmit512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeReXmit512.setStatus("current")
_ExtremeWirelessClientFrameSizeReXmit1024_Type = Unsigned32
_ExtremeWirelessClientFrameSizeReXmit1024_Object = MibTableColumn
extremeWirelessClientFrameSizeReXmit1024 = _ExtremeWirelessClientFrameSizeReXmit1024_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 5),
    _ExtremeWirelessClientFrameSizeReXmit1024_Type()
)
extremeWirelessClientFrameSizeReXmit1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeReXmit1024.setStatus("current")
_ExtremeWirelessClientFrameSizeReXmit2048_Type = Unsigned32
_ExtremeWirelessClientFrameSizeReXmit2048_Object = MibTableColumn
extremeWirelessClientFrameSizeReXmit2048 = _ExtremeWirelessClientFrameSizeReXmit2048_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 6),
    _ExtremeWirelessClientFrameSizeReXmit2048_Type()
)
extremeWirelessClientFrameSizeReXmit2048.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeReXmit2048.setStatus("current")
_ExtremeWirelessClientFrameSizeTX64_Type = Unsigned32
_ExtremeWirelessClientFrameSizeTX64_Object = MibTableColumn
extremeWirelessClientFrameSizeTX64 = _ExtremeWirelessClientFrameSizeTX64_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 7),
    _ExtremeWirelessClientFrameSizeTX64_Type()
)
extremeWirelessClientFrameSizeTX64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeTX64.setStatus("current")
_ExtremeWirelessClientFrameSizeTX128_Type = Unsigned32
_ExtremeWirelessClientFrameSizeTX128_Object = MibTableColumn
extremeWirelessClientFrameSizeTX128 = _ExtremeWirelessClientFrameSizeTX128_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 8),
    _ExtremeWirelessClientFrameSizeTX128_Type()
)
extremeWirelessClientFrameSizeTX128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeTX128.setStatus("current")
_ExtremeWirelessClientFrameSizeTX256_Type = Unsigned32
_ExtremeWirelessClientFrameSizeTX256_Object = MibTableColumn
extremeWirelessClientFrameSizeTX256 = _ExtremeWirelessClientFrameSizeTX256_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 9),
    _ExtremeWirelessClientFrameSizeTX256_Type()
)
extremeWirelessClientFrameSizeTX256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeTX256.setStatus("current")
_ExtremeWirelessClientFrameSizeTX512_Type = Unsigned32
_ExtremeWirelessClientFrameSizeTX512_Object = MibTableColumn
extremeWirelessClientFrameSizeTX512 = _ExtremeWirelessClientFrameSizeTX512_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 10),
    _ExtremeWirelessClientFrameSizeTX512_Type()
)
extremeWirelessClientFrameSizeTX512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeTX512.setStatus("current")
_ExtremeWirelessClientFrameSizeTX1024_Type = Unsigned32
_ExtremeWirelessClientFrameSizeTX1024_Object = MibTableColumn
extremeWirelessClientFrameSizeTX1024 = _ExtremeWirelessClientFrameSizeTX1024_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 11),
    _ExtremeWirelessClientFrameSizeTX1024_Type()
)
extremeWirelessClientFrameSizeTX1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeTX1024.setStatus("current")
_ExtremeWirelessClientFrameSizeTX2048_Type = Unsigned32
_ExtremeWirelessClientFrameSizeTX2048_Object = MibTableColumn
extremeWirelessClientFrameSizeTX2048 = _ExtremeWirelessClientFrameSizeTX2048_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 12),
    _ExtremeWirelessClientFrameSizeTX2048_Type()
)
extremeWirelessClientFrameSizeTX2048.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeTX2048.setStatus("current")
_ExtremeWirelessClientFrameSizeRX64_Type = Unsigned32
_ExtremeWirelessClientFrameSizeRX64_Object = MibTableColumn
extremeWirelessClientFrameSizeRX64 = _ExtremeWirelessClientFrameSizeRX64_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 13),
    _ExtremeWirelessClientFrameSizeRX64_Type()
)
extremeWirelessClientFrameSizeRX64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeRX64.setStatus("current")
_ExtremeWirelessClientFrameSizeRX128_Type = Unsigned32
_ExtremeWirelessClientFrameSizeRX128_Object = MibTableColumn
extremeWirelessClientFrameSizeRX128 = _ExtremeWirelessClientFrameSizeRX128_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 14),
    _ExtremeWirelessClientFrameSizeRX128_Type()
)
extremeWirelessClientFrameSizeRX128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeRX128.setStatus("current")
_ExtremeWirelessClientFrameSizeRX256_Type = Unsigned32
_ExtremeWirelessClientFrameSizeRX256_Object = MibTableColumn
extremeWirelessClientFrameSizeRX256 = _ExtremeWirelessClientFrameSizeRX256_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 15),
    _ExtremeWirelessClientFrameSizeRX256_Type()
)
extremeWirelessClientFrameSizeRX256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeRX256.setStatus("current")
_ExtremeWirelessClientFrameSizeRX512_Type = Unsigned32
_ExtremeWirelessClientFrameSizeRX512_Object = MibTableColumn
extremeWirelessClientFrameSizeRX512 = _ExtremeWirelessClientFrameSizeRX512_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 16),
    _ExtremeWirelessClientFrameSizeRX512_Type()
)
extremeWirelessClientFrameSizeRX512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeRX512.setStatus("current")
_ExtremeWirelessClientFrameSizeRX1024_Type = Unsigned32
_ExtremeWirelessClientFrameSizeRX1024_Object = MibTableColumn
extremeWirelessClientFrameSizeRX1024 = _ExtremeWirelessClientFrameSizeRX1024_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 17),
    _ExtremeWirelessClientFrameSizeRX1024_Type()
)
extremeWirelessClientFrameSizeRX1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeRX1024.setStatus("current")
_ExtremeWirelessClientFrameSizeRX2048_Type = Unsigned32
_ExtremeWirelessClientFrameSizeRX2048_Object = MibTableColumn
extremeWirelessClientFrameSizeRX2048 = _ExtremeWirelessClientFrameSizeRX2048_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 18),
    _ExtremeWirelessClientFrameSizeRX2048_Type()
)
extremeWirelessClientFrameSizeRX2048.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeRX2048.setStatus("current")
_ExtremeWirelessClientFrameSizeErrorTX64_Type = Unsigned32
_ExtremeWirelessClientFrameSizeErrorTX64_Object = MibTableColumn
extremeWirelessClientFrameSizeErrorTX64 = _ExtremeWirelessClientFrameSizeErrorTX64_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 19),
    _ExtremeWirelessClientFrameSizeErrorTX64_Type()
)
extremeWirelessClientFrameSizeErrorTX64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeErrorTX64.setStatus("current")
_ExtremeWirelessClientFrameSizeErrorTX128_Type = Unsigned32
_ExtremeWirelessClientFrameSizeErrorTX128_Object = MibTableColumn
extremeWirelessClientFrameSizeErrorTX128 = _ExtremeWirelessClientFrameSizeErrorTX128_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 20),
    _ExtremeWirelessClientFrameSizeErrorTX128_Type()
)
extremeWirelessClientFrameSizeErrorTX128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeErrorTX128.setStatus("current")
_ExtremeWirelessClientFrameSizeErrorTX256_Type = Unsigned32
_ExtremeWirelessClientFrameSizeErrorTX256_Object = MibTableColumn
extremeWirelessClientFrameSizeErrorTX256 = _ExtremeWirelessClientFrameSizeErrorTX256_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 21),
    _ExtremeWirelessClientFrameSizeErrorTX256_Type()
)
extremeWirelessClientFrameSizeErrorTX256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeErrorTX256.setStatus("current")
_ExtremeWirelessClientFrameSizeErrorTX512_Type = Unsigned32
_ExtremeWirelessClientFrameSizeErrorTX512_Object = MibTableColumn
extremeWirelessClientFrameSizeErrorTX512 = _ExtremeWirelessClientFrameSizeErrorTX512_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 22),
    _ExtremeWirelessClientFrameSizeErrorTX512_Type()
)
extremeWirelessClientFrameSizeErrorTX512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeErrorTX512.setStatus("current")
_ExtremeWirelessClientFrameSizeErrorTX1024_Type = Unsigned32
_ExtremeWirelessClientFrameSizeErrorTX1024_Object = MibTableColumn
extremeWirelessClientFrameSizeErrorTX1024 = _ExtremeWirelessClientFrameSizeErrorTX1024_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 23),
    _ExtremeWirelessClientFrameSizeErrorTX1024_Type()
)
extremeWirelessClientFrameSizeErrorTX1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeErrorTX1024.setStatus("current")
_ExtremeWirelessClientFrameSizeErrorTX2048_Type = Unsigned32
_ExtremeWirelessClientFrameSizeErrorTX2048_Object = MibTableColumn
extremeWirelessClientFrameSizeErrorTX2048 = _ExtremeWirelessClientFrameSizeErrorTX2048_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 24),
    _ExtremeWirelessClientFrameSizeErrorTX2048_Type()
)
extremeWirelessClientFrameSizeErrorTX2048.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeErrorTX2048.setStatus("current")
_ExtremeWirelessClientFrameSizeErrorRX64_Type = Unsigned32
_ExtremeWirelessClientFrameSizeErrorRX64_Object = MibTableColumn
extremeWirelessClientFrameSizeErrorRX64 = _ExtremeWirelessClientFrameSizeErrorRX64_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 25),
    _ExtremeWirelessClientFrameSizeErrorRX64_Type()
)
extremeWirelessClientFrameSizeErrorRX64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeErrorRX64.setStatus("current")
_ExtremeWirelessClientFrameSizeErrorRX128_Type = Unsigned32
_ExtremeWirelessClientFrameSizeErrorRX128_Object = MibTableColumn
extremeWirelessClientFrameSizeErrorRX128 = _ExtremeWirelessClientFrameSizeErrorRX128_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 26),
    _ExtremeWirelessClientFrameSizeErrorRX128_Type()
)
extremeWirelessClientFrameSizeErrorRX128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeErrorRX128.setStatus("current")
_ExtremeWirelessClientFrameSizeErrorRX256_Type = Unsigned32
_ExtremeWirelessClientFrameSizeErrorRX256_Object = MibTableColumn
extremeWirelessClientFrameSizeErrorRX256 = _ExtremeWirelessClientFrameSizeErrorRX256_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 27),
    _ExtremeWirelessClientFrameSizeErrorRX256_Type()
)
extremeWirelessClientFrameSizeErrorRX256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeErrorRX256.setStatus("current")
_ExtremeWirelessClientFrameSizeErrorRX512_Type = Unsigned32
_ExtremeWirelessClientFrameSizeErrorRX512_Object = MibTableColumn
extremeWirelessClientFrameSizeErrorRX512 = _ExtremeWirelessClientFrameSizeErrorRX512_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 28),
    _ExtremeWirelessClientFrameSizeErrorRX512_Type()
)
extremeWirelessClientFrameSizeErrorRX512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeErrorRX512.setStatus("current")
_ExtremeWirelessClientFrameSizeErrorRX1024_Type = Unsigned32
_ExtremeWirelessClientFrameSizeErrorRX1024_Object = MibTableColumn
extremeWirelessClientFrameSizeErrorRX1024 = _ExtremeWirelessClientFrameSizeErrorRX1024_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 29),
    _ExtremeWirelessClientFrameSizeErrorRX1024_Type()
)
extremeWirelessClientFrameSizeErrorRX1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeErrorRX1024.setStatus("current")
_ExtremeWirelessClientFrameSizeErrorRX2048_Type = Unsigned32
_ExtremeWirelessClientFrameSizeErrorRX2048_Object = MibTableColumn
extremeWirelessClientFrameSizeErrorRX2048 = _ExtremeWirelessClientFrameSizeErrorRX2048_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 30),
    _ExtremeWirelessClientFrameSizeErrorRX2048_Type()
)
extremeWirelessClientFrameSizeErrorRX2048.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientFrameSizeErrorRX2048.setStatus("current")
_ExtremeWirelessClientPacketSizeTX64_Type = Unsigned32
_ExtremeWirelessClientPacketSizeTX64_Object = MibTableColumn
extremeWirelessClientPacketSizeTX64 = _ExtremeWirelessClientPacketSizeTX64_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 31),
    _ExtremeWirelessClientPacketSizeTX64_Type()
)
extremeWirelessClientPacketSizeTX64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientPacketSizeTX64.setStatus("current")
_ExtremeWirelessClientPacketSizeTX128_Type = Unsigned32
_ExtremeWirelessClientPacketSizeTX128_Object = MibTableColumn
extremeWirelessClientPacketSizeTX128 = _ExtremeWirelessClientPacketSizeTX128_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 32),
    _ExtremeWirelessClientPacketSizeTX128_Type()
)
extremeWirelessClientPacketSizeTX128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientPacketSizeTX128.setStatus("current")
_ExtremeWirelessClientPacketSizeTX256_Type = Unsigned32
_ExtremeWirelessClientPacketSizeTX256_Object = MibTableColumn
extremeWirelessClientPacketSizeTX256 = _ExtremeWirelessClientPacketSizeTX256_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 33),
    _ExtremeWirelessClientPacketSizeTX256_Type()
)
extremeWirelessClientPacketSizeTX256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientPacketSizeTX256.setStatus("current")
_ExtremeWirelessClientPacketSizeTX512_Type = Unsigned32
_ExtremeWirelessClientPacketSizeTX512_Object = MibTableColumn
extremeWirelessClientPacketSizeTX512 = _ExtremeWirelessClientPacketSizeTX512_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 34),
    _ExtremeWirelessClientPacketSizeTX512_Type()
)
extremeWirelessClientPacketSizeTX512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientPacketSizeTX512.setStatus("current")
_ExtremeWirelessClientPacketSizeTX1024_Type = Unsigned32
_ExtremeWirelessClientPacketSizeTX1024_Object = MibTableColumn
extremeWirelessClientPacketSizeTX1024 = _ExtremeWirelessClientPacketSizeTX1024_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 35),
    _ExtremeWirelessClientPacketSizeTX1024_Type()
)
extremeWirelessClientPacketSizeTX1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientPacketSizeTX1024.setStatus("current")
_ExtremeWirelessClientPacketSizeTX2048_Type = Unsigned32
_ExtremeWirelessClientPacketSizeTX2048_Object = MibTableColumn
extremeWirelessClientPacketSizeTX2048 = _ExtremeWirelessClientPacketSizeTX2048_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 36),
    _ExtremeWirelessClientPacketSizeTX2048_Type()
)
extremeWirelessClientPacketSizeTX2048.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientPacketSizeTX2048.setStatus("current")
_ExtremeWirelessClientPacketSizeRX64_Type = Unsigned32
_ExtremeWirelessClientPacketSizeRX64_Object = MibTableColumn
extremeWirelessClientPacketSizeRX64 = _ExtremeWirelessClientPacketSizeRX64_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 37),
    _ExtremeWirelessClientPacketSizeRX64_Type()
)
extremeWirelessClientPacketSizeRX64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientPacketSizeRX64.setStatus("current")
_ExtremeWirelessClientPacketSizeRX128_Type = Unsigned32
_ExtremeWirelessClientPacketSizeRX128_Object = MibTableColumn
extremeWirelessClientPacketSizeRX128 = _ExtremeWirelessClientPacketSizeRX128_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 38),
    _ExtremeWirelessClientPacketSizeRX128_Type()
)
extremeWirelessClientPacketSizeRX128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientPacketSizeRX128.setStatus("current")
_ExtremeWirelessClientPacketSizeRX256_Type = Unsigned32
_ExtremeWirelessClientPacketSizeRX256_Object = MibTableColumn
extremeWirelessClientPacketSizeRX256 = _ExtremeWirelessClientPacketSizeRX256_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 39),
    _ExtremeWirelessClientPacketSizeRX256_Type()
)
extremeWirelessClientPacketSizeRX256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientPacketSizeRX256.setStatus("current")
_ExtremeWirelessClientPacketSizeRX512_Type = Unsigned32
_ExtremeWirelessClientPacketSizeRX512_Object = MibTableColumn
extremeWirelessClientPacketSizeRX512 = _ExtremeWirelessClientPacketSizeRX512_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 40),
    _ExtremeWirelessClientPacketSizeRX512_Type()
)
extremeWirelessClientPacketSizeRX512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientPacketSizeRX512.setStatus("current")
_ExtremeWirelessClientPacketSizeRX1024_Type = Unsigned32
_ExtremeWirelessClientPacketSizeRX1024_Object = MibTableColumn
extremeWirelessClientPacketSizeRX1024 = _ExtremeWirelessClientPacketSizeRX1024_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 41),
    _ExtremeWirelessClientPacketSizeRX1024_Type()
)
extremeWirelessClientPacketSizeRX1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientPacketSizeRX1024.setStatus("current")
_ExtremeWirelessClientPacketSizeRX2048_Type = Unsigned32
_ExtremeWirelessClientPacketSizeRX2048_Object = MibTableColumn
extremeWirelessClientPacketSizeRX2048 = _ExtremeWirelessClientPacketSizeRX2048_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 37, 1, 42),
    _ExtremeWirelessClientPacketSizeRX2048_Type()
)
extremeWirelessClientPacketSizeRX2048.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientPacketSizeRX2048.setStatus("current")
_ExtremeWirelessClientSpeedCounterTable_Object = MibTable
extremeWirelessClientSpeedCounterTable = _ExtremeWirelessClientSpeedCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38)
)
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedCounterTable.setStatus("current")
_ExtremeWirelessClientSpeedCounterEntry_Object = MibTableRow
extremeWirelessClientSpeedCounterEntry = _ExtremeWirelessClientSpeedCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1)
)
extremeWirelessClientSpeedCounterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessClientDiagMac"),
)
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedCounterEntry.setStatus("current")
_ExtremeWirelessClientSpeedReXmit1_Type = Unsigned32
_ExtremeWirelessClientSpeedReXmit1_Object = MibTableColumn
extremeWirelessClientSpeedReXmit1 = _ExtremeWirelessClientSpeedReXmit1_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 1),
    _ExtremeWirelessClientSpeedReXmit1_Type()
)
extremeWirelessClientSpeedReXmit1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedReXmit1.setStatus("current")
_ExtremeWirelessClientSpeedReXmit2_Type = Unsigned32
_ExtremeWirelessClientSpeedReXmit2_Object = MibTableColumn
extremeWirelessClientSpeedReXmit2 = _ExtremeWirelessClientSpeedReXmit2_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 2),
    _ExtremeWirelessClientSpeedReXmit2_Type()
)
extremeWirelessClientSpeedReXmit2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedReXmit2.setStatus("current")
_ExtremeWirelessClientSpeedReXmit5p5_Type = Unsigned32
_ExtremeWirelessClientSpeedReXmit5p5_Object = MibTableColumn
extremeWirelessClientSpeedReXmit5p5 = _ExtremeWirelessClientSpeedReXmit5p5_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 3),
    _ExtremeWirelessClientSpeedReXmit5p5_Type()
)
extremeWirelessClientSpeedReXmit5p5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedReXmit5p5.setStatus("current")
_ExtremeWirelessClientSpeedReXmit6_Type = Unsigned32
_ExtremeWirelessClientSpeedReXmit6_Object = MibTableColumn
extremeWirelessClientSpeedReXmit6 = _ExtremeWirelessClientSpeedReXmit6_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 4),
    _ExtremeWirelessClientSpeedReXmit6_Type()
)
extremeWirelessClientSpeedReXmit6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedReXmit6.setStatus("current")
_ExtremeWirelessClientSpeedReXmit9_Type = Unsigned32
_ExtremeWirelessClientSpeedReXmit9_Object = MibTableColumn
extremeWirelessClientSpeedReXmit9 = _ExtremeWirelessClientSpeedReXmit9_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 5),
    _ExtremeWirelessClientSpeedReXmit9_Type()
)
extremeWirelessClientSpeedReXmit9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedReXmit9.setStatus("current")
_ExtremeWirelessClientSpeedReXmit12_Type = Unsigned32
_ExtremeWirelessClientSpeedReXmit12_Object = MibTableColumn
extremeWirelessClientSpeedReXmit12 = _ExtremeWirelessClientSpeedReXmit12_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 6),
    _ExtremeWirelessClientSpeedReXmit12_Type()
)
extremeWirelessClientSpeedReXmit12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedReXmit12.setStatus("current")
_ExtremeWirelessClientSpeedReXmit18_Type = Unsigned32
_ExtremeWirelessClientSpeedReXmit18_Object = MibTableColumn
extremeWirelessClientSpeedReXmit18 = _ExtremeWirelessClientSpeedReXmit18_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 7),
    _ExtremeWirelessClientSpeedReXmit18_Type()
)
extremeWirelessClientSpeedReXmit18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedReXmit18.setStatus("current")
_ExtremeWirelessClientSpeedReXmit24_Type = Unsigned32
_ExtremeWirelessClientSpeedReXmit24_Object = MibTableColumn
extremeWirelessClientSpeedReXmit24 = _ExtremeWirelessClientSpeedReXmit24_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 8),
    _ExtremeWirelessClientSpeedReXmit24_Type()
)
extremeWirelessClientSpeedReXmit24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedReXmit24.setStatus("current")
_ExtremeWirelessClientSpeedReXmit36_Type = Unsigned32
_ExtremeWirelessClientSpeedReXmit36_Object = MibTableColumn
extremeWirelessClientSpeedReXmit36 = _ExtremeWirelessClientSpeedReXmit36_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 9),
    _ExtremeWirelessClientSpeedReXmit36_Type()
)
extremeWirelessClientSpeedReXmit36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedReXmit36.setStatus("current")
_ExtremeWirelessClientSpeedReXmit48_Type = Unsigned32
_ExtremeWirelessClientSpeedReXmit48_Object = MibTableColumn
extremeWirelessClientSpeedReXmit48 = _ExtremeWirelessClientSpeedReXmit48_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 10),
    _ExtremeWirelessClientSpeedReXmit48_Type()
)
extremeWirelessClientSpeedReXmit48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedReXmit48.setStatus("current")
_ExtremeWirelessClientSpeedReXmit54_Type = Unsigned32
_ExtremeWirelessClientSpeedReXmit54_Object = MibTableColumn
extremeWirelessClientSpeedReXmit54 = _ExtremeWirelessClientSpeedReXmit54_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 11),
    _ExtremeWirelessClientSpeedReXmit54_Type()
)
extremeWirelessClientSpeedReXmit54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedReXmit54.setStatus("current")
_ExtremeWirelessClientSpeedTX1_Type = Unsigned32
_ExtremeWirelessClientSpeedTX1_Object = MibTableColumn
extremeWirelessClientSpeedTX1 = _ExtremeWirelessClientSpeedTX1_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 12),
    _ExtremeWirelessClientSpeedTX1_Type()
)
extremeWirelessClientSpeedTX1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedTX1.setStatus("current")
_ExtremeWirelessClientSpeedTX2_Type = Unsigned32
_ExtremeWirelessClientSpeedTX2_Object = MibTableColumn
extremeWirelessClientSpeedTX2 = _ExtremeWirelessClientSpeedTX2_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 13),
    _ExtremeWirelessClientSpeedTX2_Type()
)
extremeWirelessClientSpeedTX2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedTX2.setStatus("current")
_ExtremeWirelessClientSpeedTX5p5_Type = Unsigned32
_ExtremeWirelessClientSpeedTX5p5_Object = MibTableColumn
extremeWirelessClientSpeedTX5p5 = _ExtremeWirelessClientSpeedTX5p5_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 14),
    _ExtremeWirelessClientSpeedTX5p5_Type()
)
extremeWirelessClientSpeedTX5p5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedTX5p5.setStatus("current")
_ExtremeWirelessClientSpeedTX6_Type = Unsigned32
_ExtremeWirelessClientSpeedTX6_Object = MibTableColumn
extremeWirelessClientSpeedTX6 = _ExtremeWirelessClientSpeedTX6_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 15),
    _ExtremeWirelessClientSpeedTX6_Type()
)
extremeWirelessClientSpeedTX6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedTX6.setStatus("current")
_ExtremeWirelessClientSpeedTX9_Type = Unsigned32
_ExtremeWirelessClientSpeedTX9_Object = MibTableColumn
extremeWirelessClientSpeedTX9 = _ExtremeWirelessClientSpeedTX9_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 16),
    _ExtremeWirelessClientSpeedTX9_Type()
)
extremeWirelessClientSpeedTX9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedTX9.setStatus("current")
_ExtremeWirelessClientSpeedTX12_Type = Unsigned32
_ExtremeWirelessClientSpeedTX12_Object = MibTableColumn
extremeWirelessClientSpeedTX12 = _ExtremeWirelessClientSpeedTX12_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 17),
    _ExtremeWirelessClientSpeedTX12_Type()
)
extremeWirelessClientSpeedTX12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedTX12.setStatus("current")
_ExtremeWirelessClientSpeedTX18_Type = Unsigned32
_ExtremeWirelessClientSpeedTX18_Object = MibTableColumn
extremeWirelessClientSpeedTX18 = _ExtremeWirelessClientSpeedTX18_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 18),
    _ExtremeWirelessClientSpeedTX18_Type()
)
extremeWirelessClientSpeedTX18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedTX18.setStatus("current")
_ExtremeWirelessClientSpeedTX24_Type = Unsigned32
_ExtremeWirelessClientSpeedTX24_Object = MibTableColumn
extremeWirelessClientSpeedTX24 = _ExtremeWirelessClientSpeedTX24_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 19),
    _ExtremeWirelessClientSpeedTX24_Type()
)
extremeWirelessClientSpeedTX24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedTX24.setStatus("current")
_ExtremeWirelessClientSpeedTX36_Type = Unsigned32
_ExtremeWirelessClientSpeedTX36_Object = MibTableColumn
extremeWirelessClientSpeedTX36 = _ExtremeWirelessClientSpeedTX36_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 20),
    _ExtremeWirelessClientSpeedTX36_Type()
)
extremeWirelessClientSpeedTX36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedTX36.setStatus("current")
_ExtremeWirelessClientSpeedTX48_Type = Unsigned32
_ExtremeWirelessClientSpeedTX48_Object = MibTableColumn
extremeWirelessClientSpeedTX48 = _ExtremeWirelessClientSpeedTX48_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 21),
    _ExtremeWirelessClientSpeedTX48_Type()
)
extremeWirelessClientSpeedTX48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedTX48.setStatus("current")
_ExtremeWirelessClientSpeedTX54_Type = Unsigned32
_ExtremeWirelessClientSpeedTX54_Object = MibTableColumn
extremeWirelessClientSpeedTX54 = _ExtremeWirelessClientSpeedTX54_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 22),
    _ExtremeWirelessClientSpeedTX54_Type()
)
extremeWirelessClientSpeedTX54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedTX54.setStatus("current")
_ExtremeWirelessClientSpeedRX1_Type = Unsigned32
_ExtremeWirelessClientSpeedRX1_Object = MibTableColumn
extremeWirelessClientSpeedRX1 = _ExtremeWirelessClientSpeedRX1_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 23),
    _ExtremeWirelessClientSpeedRX1_Type()
)
extremeWirelessClientSpeedRX1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedRX1.setStatus("current")
_ExtremeWirelessClientSpeedRX2_Type = Unsigned32
_ExtremeWirelessClientSpeedRX2_Object = MibTableColumn
extremeWirelessClientSpeedRX2 = _ExtremeWirelessClientSpeedRX2_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 24),
    _ExtremeWirelessClientSpeedRX2_Type()
)
extremeWirelessClientSpeedRX2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedRX2.setStatus("current")
_ExtremeWirelessClientSpeedRX5p5_Type = Unsigned32
_ExtremeWirelessClientSpeedRX5p5_Object = MibTableColumn
extremeWirelessClientSpeedRX5p5 = _ExtremeWirelessClientSpeedRX5p5_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 25),
    _ExtremeWirelessClientSpeedRX5p5_Type()
)
extremeWirelessClientSpeedRX5p5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedRX5p5.setStatus("current")
_ExtremeWirelessClientSpeedRX6_Type = Unsigned32
_ExtremeWirelessClientSpeedRX6_Object = MibTableColumn
extremeWirelessClientSpeedRX6 = _ExtremeWirelessClientSpeedRX6_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 26),
    _ExtremeWirelessClientSpeedRX6_Type()
)
extremeWirelessClientSpeedRX6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedRX6.setStatus("current")
_ExtremeWirelessClientSpeedRX9_Type = Unsigned32
_ExtremeWirelessClientSpeedRX9_Object = MibTableColumn
extremeWirelessClientSpeedRX9 = _ExtremeWirelessClientSpeedRX9_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 27),
    _ExtremeWirelessClientSpeedRX9_Type()
)
extremeWirelessClientSpeedRX9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedRX9.setStatus("current")
_ExtremeWirelessClientSpeedRX12_Type = Unsigned32
_ExtremeWirelessClientSpeedRX12_Object = MibTableColumn
extremeWirelessClientSpeedRX12 = _ExtremeWirelessClientSpeedRX12_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 28),
    _ExtremeWirelessClientSpeedRX12_Type()
)
extremeWirelessClientSpeedRX12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedRX12.setStatus("current")
_ExtremeWirelessClientSpeedRX18_Type = Unsigned32
_ExtremeWirelessClientSpeedRX18_Object = MibTableColumn
extremeWirelessClientSpeedRX18 = _ExtremeWirelessClientSpeedRX18_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 29),
    _ExtremeWirelessClientSpeedRX18_Type()
)
extremeWirelessClientSpeedRX18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedRX18.setStatus("current")
_ExtremeWirelessClientSpeedRX24_Type = Unsigned32
_ExtremeWirelessClientSpeedRX24_Object = MibTableColumn
extremeWirelessClientSpeedRX24 = _ExtremeWirelessClientSpeedRX24_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 30),
    _ExtremeWirelessClientSpeedRX24_Type()
)
extremeWirelessClientSpeedRX24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedRX24.setStatus("current")
_ExtremeWirelessClientSpeedRX36_Type = Unsigned32
_ExtremeWirelessClientSpeedRX36_Object = MibTableColumn
extremeWirelessClientSpeedRX36 = _ExtremeWirelessClientSpeedRX36_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 31),
    _ExtremeWirelessClientSpeedRX36_Type()
)
extremeWirelessClientSpeedRX36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedRX36.setStatus("current")
_ExtremeWirelessClientSpeedRX48_Type = Unsigned32
_ExtremeWirelessClientSpeedRX48_Object = MibTableColumn
extremeWirelessClientSpeedRX48 = _ExtremeWirelessClientSpeedRX48_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 32),
    _ExtremeWirelessClientSpeedRX48_Type()
)
extremeWirelessClientSpeedRX48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedRX48.setStatus("current")
_ExtremeWirelessClientSpeedRX54_Type = Unsigned32
_ExtremeWirelessClientSpeedRX54_Object = MibTableColumn
extremeWirelessClientSpeedRX54 = _ExtremeWirelessClientSpeedRX54_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 38, 1, 33),
    _ExtremeWirelessClientSpeedRX54_Type()
)
extremeWirelessClientSpeedRX54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientSpeedRX54.setStatus("current")
_ExtremeWirelessIntfFrameSizeTable_Object = MibTable
extremeWirelessIntfFrameSizeTable = _ExtremeWirelessIntfFrameSizeTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39)
)
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeTable.setStatus("current")
_ExtremeWirelessIntfFrameSizeEntry_Object = MibTableRow
extremeWirelessIntfFrameSizeEntry = _ExtremeWirelessIntfFrameSizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1)
)
extremeWirelessIntfFrameSizeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeEntry.setStatus("current")
_ExtremeWirelessIntfFrameSizeMgmtTX64_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeMgmtTX64_Object = MibTableColumn
extremeWirelessIntfFrameSizeMgmtTX64 = _ExtremeWirelessIntfFrameSizeMgmtTX64_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 1),
    _ExtremeWirelessIntfFrameSizeMgmtTX64_Type()
)
extremeWirelessIntfFrameSizeMgmtTX64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeMgmtTX64.setStatus("current")
_ExtremeWirelessIntfFrameSizeMgmtTX128_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeMgmtTX128_Object = MibTableColumn
extremeWirelessIntfFrameSizeMgmtTX128 = _ExtremeWirelessIntfFrameSizeMgmtTX128_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 2),
    _ExtremeWirelessIntfFrameSizeMgmtTX128_Type()
)
extremeWirelessIntfFrameSizeMgmtTX128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeMgmtTX128.setStatus("current")
_ExtremeWirelessIntfFrameSizeMgmtTX256_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeMgmtTX256_Object = MibTableColumn
extremeWirelessIntfFrameSizeMgmtTX256 = _ExtremeWirelessIntfFrameSizeMgmtTX256_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 3),
    _ExtremeWirelessIntfFrameSizeMgmtTX256_Type()
)
extremeWirelessIntfFrameSizeMgmtTX256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeMgmtTX256.setStatus("current")
_ExtremeWirelessIntfFrameSizeMgmtTX512_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeMgmtTX512_Object = MibTableColumn
extremeWirelessIntfFrameSizeMgmtTX512 = _ExtremeWirelessIntfFrameSizeMgmtTX512_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 4),
    _ExtremeWirelessIntfFrameSizeMgmtTX512_Type()
)
extremeWirelessIntfFrameSizeMgmtTX512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeMgmtTX512.setStatus("current")
_ExtremeWirelessIntfFrameSizeMgmtTX1024_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeMgmtTX1024_Object = MibTableColumn
extremeWirelessIntfFrameSizeMgmtTX1024 = _ExtremeWirelessIntfFrameSizeMgmtTX1024_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 5),
    _ExtremeWirelessIntfFrameSizeMgmtTX1024_Type()
)
extremeWirelessIntfFrameSizeMgmtTX1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeMgmtTX1024.setStatus("current")
_ExtremeWirelessIntfFrameSizeMgmtTX2048_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeMgmtTX2048_Object = MibTableColumn
extremeWirelessIntfFrameSizeMgmtTX2048 = _ExtremeWirelessIntfFrameSizeMgmtTX2048_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 6),
    _ExtremeWirelessIntfFrameSizeMgmtTX2048_Type()
)
extremeWirelessIntfFrameSizeMgmtTX2048.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeMgmtTX2048.setStatus("current")
_ExtremeWirelessIntfFrameSizeMgmtRX64_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeMgmtRX64_Object = MibTableColumn
extremeWirelessIntfFrameSizeMgmtRX64 = _ExtremeWirelessIntfFrameSizeMgmtRX64_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 7),
    _ExtremeWirelessIntfFrameSizeMgmtRX64_Type()
)
extremeWirelessIntfFrameSizeMgmtRX64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeMgmtRX64.setStatus("current")
_ExtremeWirelessIntfFrameSizeMgmtRX128_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeMgmtRX128_Object = MibTableColumn
extremeWirelessIntfFrameSizeMgmtRX128 = _ExtremeWirelessIntfFrameSizeMgmtRX128_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 8),
    _ExtremeWirelessIntfFrameSizeMgmtRX128_Type()
)
extremeWirelessIntfFrameSizeMgmtRX128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeMgmtRX128.setStatus("current")
_ExtremeWirelessIntfFrameSizeMgmtRX256_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeMgmtRX256_Object = MibTableColumn
extremeWirelessIntfFrameSizeMgmtRX256 = _ExtremeWirelessIntfFrameSizeMgmtRX256_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 9),
    _ExtremeWirelessIntfFrameSizeMgmtRX256_Type()
)
extremeWirelessIntfFrameSizeMgmtRX256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeMgmtRX256.setStatus("current")
_ExtremeWirelessIntfFrameSizeMgmtRX512_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeMgmtRX512_Object = MibTableColumn
extremeWirelessIntfFrameSizeMgmtRX512 = _ExtremeWirelessIntfFrameSizeMgmtRX512_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 10),
    _ExtremeWirelessIntfFrameSizeMgmtRX512_Type()
)
extremeWirelessIntfFrameSizeMgmtRX512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeMgmtRX512.setStatus("current")
_ExtremeWirelessIntfFrameSizeMgmtRX1024_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeMgmtRX1024_Object = MibTableColumn
extremeWirelessIntfFrameSizeMgmtRX1024 = _ExtremeWirelessIntfFrameSizeMgmtRX1024_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 11),
    _ExtremeWirelessIntfFrameSizeMgmtRX1024_Type()
)
extremeWirelessIntfFrameSizeMgmtRX1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeMgmtRX1024.setStatus("current")
_ExtremeWirelessIntfFrameSizeMgmtRX2048_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeMgmtRX2048_Object = MibTableColumn
extremeWirelessIntfFrameSizeMgmtRX2048 = _ExtremeWirelessIntfFrameSizeMgmtRX2048_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 12),
    _ExtremeWirelessIntfFrameSizeMgmtRX2048_Type()
)
extremeWirelessIntfFrameSizeMgmtRX2048.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeMgmtRX2048.setStatus("current")
_ExtremeWirelessIntfFrameSizeCtlTX64_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeCtlTX64_Object = MibTableColumn
extremeWirelessIntfFrameSizeCtlTX64 = _ExtremeWirelessIntfFrameSizeCtlTX64_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 13),
    _ExtremeWirelessIntfFrameSizeCtlTX64_Type()
)
extremeWirelessIntfFrameSizeCtlTX64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeCtlTX64.setStatus("current")
_ExtremeWirelessIntfFrameSizeCtlTX128_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeCtlTX128_Object = MibTableColumn
extremeWirelessIntfFrameSizeCtlTX128 = _ExtremeWirelessIntfFrameSizeCtlTX128_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 14),
    _ExtremeWirelessIntfFrameSizeCtlTX128_Type()
)
extremeWirelessIntfFrameSizeCtlTX128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeCtlTX128.setStatus("current")
_ExtremeWirelessIntfFrameSizeCtlTX256_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeCtlTX256_Object = MibTableColumn
extremeWirelessIntfFrameSizeCtlTX256 = _ExtremeWirelessIntfFrameSizeCtlTX256_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 15),
    _ExtremeWirelessIntfFrameSizeCtlTX256_Type()
)
extremeWirelessIntfFrameSizeCtlTX256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeCtlTX256.setStatus("current")
_ExtremeWirelessIntfFrameSizeCtlTX512_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeCtlTX512_Object = MibTableColumn
extremeWirelessIntfFrameSizeCtlTX512 = _ExtremeWirelessIntfFrameSizeCtlTX512_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 16),
    _ExtremeWirelessIntfFrameSizeCtlTX512_Type()
)
extremeWirelessIntfFrameSizeCtlTX512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeCtlTX512.setStatus("current")
_ExtremeWirelessIntfFrameSizeCtlTX1024_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeCtlTX1024_Object = MibTableColumn
extremeWirelessIntfFrameSizeCtlTX1024 = _ExtremeWirelessIntfFrameSizeCtlTX1024_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 17),
    _ExtremeWirelessIntfFrameSizeCtlTX1024_Type()
)
extremeWirelessIntfFrameSizeCtlTX1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeCtlTX1024.setStatus("current")
_ExtremeWirelessIntfFrameSizeCtlTX2048_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeCtlTX2048_Object = MibTableColumn
extremeWirelessIntfFrameSizeCtlTX2048 = _ExtremeWirelessIntfFrameSizeCtlTX2048_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 18),
    _ExtremeWirelessIntfFrameSizeCtlTX2048_Type()
)
extremeWirelessIntfFrameSizeCtlTX2048.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeCtlTX2048.setStatus("current")
_ExtremeWirelessIntfFrameSizeCtlRX64_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeCtlRX64_Object = MibTableColumn
extremeWirelessIntfFrameSizeCtlRX64 = _ExtremeWirelessIntfFrameSizeCtlRX64_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 19),
    _ExtremeWirelessIntfFrameSizeCtlRX64_Type()
)
extremeWirelessIntfFrameSizeCtlRX64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeCtlRX64.setStatus("current")
_ExtremeWirelessIntfFrameSizeCtlRX128_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeCtlRX128_Object = MibTableColumn
extremeWirelessIntfFrameSizeCtlRX128 = _ExtremeWirelessIntfFrameSizeCtlRX128_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 20),
    _ExtremeWirelessIntfFrameSizeCtlRX128_Type()
)
extremeWirelessIntfFrameSizeCtlRX128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeCtlRX128.setStatus("current")
_ExtremeWirelessIntfFrameSizeCtlRX256_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeCtlRX256_Object = MibTableColumn
extremeWirelessIntfFrameSizeCtlRX256 = _ExtremeWirelessIntfFrameSizeCtlRX256_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 21),
    _ExtremeWirelessIntfFrameSizeCtlRX256_Type()
)
extremeWirelessIntfFrameSizeCtlRX256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeCtlRX256.setStatus("current")
_ExtremeWirelessIntfFrameSizeCtlRX512_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeCtlRX512_Object = MibTableColumn
extremeWirelessIntfFrameSizeCtlRX512 = _ExtremeWirelessIntfFrameSizeCtlRX512_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 22),
    _ExtremeWirelessIntfFrameSizeCtlRX512_Type()
)
extremeWirelessIntfFrameSizeCtlRX512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeCtlRX512.setStatus("current")
_ExtremeWirelessIntfFrameSizeCtlRX1024_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeCtlRX1024_Object = MibTableColumn
extremeWirelessIntfFrameSizeCtlRX1024 = _ExtremeWirelessIntfFrameSizeCtlRX1024_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 23),
    _ExtremeWirelessIntfFrameSizeCtlRX1024_Type()
)
extremeWirelessIntfFrameSizeCtlRX1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeCtlRX1024.setStatus("current")
_ExtremeWirelessIntfFrameSizeCtlRX2048_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeCtlRX2048_Object = MibTableColumn
extremeWirelessIntfFrameSizeCtlRX2048 = _ExtremeWirelessIntfFrameSizeCtlRX2048_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 24),
    _ExtremeWirelessIntfFrameSizeCtlRX2048_Type()
)
extremeWirelessIntfFrameSizeCtlRX2048.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeCtlRX2048.setStatus("current")
_ExtremeWirelessIntfFrameSizeDataTX64_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeDataTX64_Object = MibTableColumn
extremeWirelessIntfFrameSizeDataTX64 = _ExtremeWirelessIntfFrameSizeDataTX64_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 25),
    _ExtremeWirelessIntfFrameSizeDataTX64_Type()
)
extremeWirelessIntfFrameSizeDataTX64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeDataTX64.setStatus("current")
_ExtremeWirelessIntfFrameSizeDataTX128_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeDataTX128_Object = MibTableColumn
extremeWirelessIntfFrameSizeDataTX128 = _ExtremeWirelessIntfFrameSizeDataTX128_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 26),
    _ExtremeWirelessIntfFrameSizeDataTX128_Type()
)
extremeWirelessIntfFrameSizeDataTX128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeDataTX128.setStatus("current")
_ExtremeWirelessIntfFrameSizeDataTX256_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeDataTX256_Object = MibTableColumn
extremeWirelessIntfFrameSizeDataTX256 = _ExtremeWirelessIntfFrameSizeDataTX256_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 27),
    _ExtremeWirelessIntfFrameSizeDataTX256_Type()
)
extremeWirelessIntfFrameSizeDataTX256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeDataTX256.setStatus("current")
_ExtremeWirelessIntfFrameSizeDataTX512_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeDataTX512_Object = MibTableColumn
extremeWirelessIntfFrameSizeDataTX512 = _ExtremeWirelessIntfFrameSizeDataTX512_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 28),
    _ExtremeWirelessIntfFrameSizeDataTX512_Type()
)
extremeWirelessIntfFrameSizeDataTX512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeDataTX512.setStatus("current")
_ExtremeWirelessIntfFrameSizeDataTX1024_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeDataTX1024_Object = MibTableColumn
extremeWirelessIntfFrameSizeDataTX1024 = _ExtremeWirelessIntfFrameSizeDataTX1024_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 29),
    _ExtremeWirelessIntfFrameSizeDataTX1024_Type()
)
extremeWirelessIntfFrameSizeDataTX1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeDataTX1024.setStatus("current")
_ExtremeWirelessIntfFrameSizeDataTX2048_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeDataTX2048_Object = MibTableColumn
extremeWirelessIntfFrameSizeDataTX2048 = _ExtremeWirelessIntfFrameSizeDataTX2048_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 30),
    _ExtremeWirelessIntfFrameSizeDataTX2048_Type()
)
extremeWirelessIntfFrameSizeDataTX2048.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeDataTX2048.setStatus("current")
_ExtremeWirelessIntfFrameSizeDataRX64_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeDataRX64_Object = MibTableColumn
extremeWirelessIntfFrameSizeDataRX64 = _ExtremeWirelessIntfFrameSizeDataRX64_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 31),
    _ExtremeWirelessIntfFrameSizeDataRX64_Type()
)
extremeWirelessIntfFrameSizeDataRX64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeDataRX64.setStatus("current")
_ExtremeWirelessIntfFrameSizeDataRX128_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeDataRX128_Object = MibTableColumn
extremeWirelessIntfFrameSizeDataRX128 = _ExtremeWirelessIntfFrameSizeDataRX128_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 32),
    _ExtremeWirelessIntfFrameSizeDataRX128_Type()
)
extremeWirelessIntfFrameSizeDataRX128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeDataRX128.setStatus("current")
_ExtremeWirelessIntfFrameSizeDataRX256_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeDataRX256_Object = MibTableColumn
extremeWirelessIntfFrameSizeDataRX256 = _ExtremeWirelessIntfFrameSizeDataRX256_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 33),
    _ExtremeWirelessIntfFrameSizeDataRX256_Type()
)
extremeWirelessIntfFrameSizeDataRX256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeDataRX256.setStatus("current")
_ExtremeWirelessIntfFrameSizeDataRX512_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeDataRX512_Object = MibTableColumn
extremeWirelessIntfFrameSizeDataRX512 = _ExtremeWirelessIntfFrameSizeDataRX512_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 34),
    _ExtremeWirelessIntfFrameSizeDataRX512_Type()
)
extremeWirelessIntfFrameSizeDataRX512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeDataRX512.setStatus("current")
_ExtremeWirelessIntfFrameSizeDataRX1024_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeDataRX1024_Object = MibTableColumn
extremeWirelessIntfFrameSizeDataRX1024 = _ExtremeWirelessIntfFrameSizeDataRX1024_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 35),
    _ExtremeWirelessIntfFrameSizeDataRX1024_Type()
)
extremeWirelessIntfFrameSizeDataRX1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeDataRX1024.setStatus("current")
_ExtremeWirelessIntfFrameSizeDataRX2048_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeDataRX2048_Object = MibTableColumn
extremeWirelessIntfFrameSizeDataRX2048 = _ExtremeWirelessIntfFrameSizeDataRX2048_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 39, 1, 36),
    _ExtremeWirelessIntfFrameSizeDataRX2048_Type()
)
extremeWirelessIntfFrameSizeDataRX2048.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeDataRX2048.setStatus("current")
_ExtremeWirelessIntfFrameSizeErrorTable_Object = MibTable
extremeWirelessIntfFrameSizeErrorTable = _ExtremeWirelessIntfFrameSizeErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 40)
)
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeErrorTable.setStatus("current")
_ExtremeWirelessIntfFrameSizeErrorEntry_Object = MibTableRow
extremeWirelessIntfFrameSizeErrorEntry = _ExtremeWirelessIntfFrameSizeErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 40, 1)
)
extremeWirelessIntfFrameSizeErrorEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeErrorEntry.setStatus("current")
_ExtremeWirelessIntfFrameSizeReXmit64_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeReXmit64_Object = MibTableColumn
extremeWirelessIntfFrameSizeReXmit64 = _ExtremeWirelessIntfFrameSizeReXmit64_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 40, 1, 1),
    _ExtremeWirelessIntfFrameSizeReXmit64_Type()
)
extremeWirelessIntfFrameSizeReXmit64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeReXmit64.setStatus("current")
_ExtremeWirelessIntfFrameSizeReXmit128_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeReXmit128_Object = MibTableColumn
extremeWirelessIntfFrameSizeReXmit128 = _ExtremeWirelessIntfFrameSizeReXmit128_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 40, 1, 2),
    _ExtremeWirelessIntfFrameSizeReXmit128_Type()
)
extremeWirelessIntfFrameSizeReXmit128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeReXmit128.setStatus("current")
_ExtremeWirelessIntfFrameSizeReXmit256_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeReXmit256_Object = MibTableColumn
extremeWirelessIntfFrameSizeReXmit256 = _ExtremeWirelessIntfFrameSizeReXmit256_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 40, 1, 3),
    _ExtremeWirelessIntfFrameSizeReXmit256_Type()
)
extremeWirelessIntfFrameSizeReXmit256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeReXmit256.setStatus("current")
_ExtremeWirelessIntfFrameSizeReXmit512_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeReXmit512_Object = MibTableColumn
extremeWirelessIntfFrameSizeReXmit512 = _ExtremeWirelessIntfFrameSizeReXmit512_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 40, 1, 4),
    _ExtremeWirelessIntfFrameSizeReXmit512_Type()
)
extremeWirelessIntfFrameSizeReXmit512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeReXmit512.setStatus("current")
_ExtremeWirelessIntfFrameSizeReXmit1024_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeReXmit1024_Object = MibTableColumn
extremeWirelessIntfFrameSizeReXmit1024 = _ExtremeWirelessIntfFrameSizeReXmit1024_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 40, 1, 5),
    _ExtremeWirelessIntfFrameSizeReXmit1024_Type()
)
extremeWirelessIntfFrameSizeReXmit1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeReXmit1024.setStatus("current")
_ExtremeWirelessIntfFrameSizeReXmit2048_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeReXmit2048_Object = MibTableColumn
extremeWirelessIntfFrameSizeReXmit2048 = _ExtremeWirelessIntfFrameSizeReXmit2048_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 40, 1, 6),
    _ExtremeWirelessIntfFrameSizeReXmit2048_Type()
)
extremeWirelessIntfFrameSizeReXmit2048.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeReXmit2048.setStatus("current")
_ExtremeWirelessIntfFrameSizeErrorTX64_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeErrorTX64_Object = MibTableColumn
extremeWirelessIntfFrameSizeErrorTX64 = _ExtremeWirelessIntfFrameSizeErrorTX64_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 40, 1, 7),
    _ExtremeWirelessIntfFrameSizeErrorTX64_Type()
)
extremeWirelessIntfFrameSizeErrorTX64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeErrorTX64.setStatus("current")
_ExtremeWirelessIntfFrameSizeErrorTX128_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeErrorTX128_Object = MibTableColumn
extremeWirelessIntfFrameSizeErrorTX128 = _ExtremeWirelessIntfFrameSizeErrorTX128_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 40, 1, 8),
    _ExtremeWirelessIntfFrameSizeErrorTX128_Type()
)
extremeWirelessIntfFrameSizeErrorTX128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeErrorTX128.setStatus("current")
_ExtremeWirelessIntfFrameSizeErrorTX256_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeErrorTX256_Object = MibTableColumn
extremeWirelessIntfFrameSizeErrorTX256 = _ExtremeWirelessIntfFrameSizeErrorTX256_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 40, 1, 9),
    _ExtremeWirelessIntfFrameSizeErrorTX256_Type()
)
extremeWirelessIntfFrameSizeErrorTX256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeErrorTX256.setStatus("current")
_ExtremeWirelessIntfFrameSizeErrorTX512_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeErrorTX512_Object = MibTableColumn
extremeWirelessIntfFrameSizeErrorTX512 = _ExtremeWirelessIntfFrameSizeErrorTX512_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 40, 1, 10),
    _ExtremeWirelessIntfFrameSizeErrorTX512_Type()
)
extremeWirelessIntfFrameSizeErrorTX512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeErrorTX512.setStatus("current")
_ExtremeWirelessIntfFrameSizeErrorTX1024_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeErrorTX1024_Object = MibTableColumn
extremeWirelessIntfFrameSizeErrorTX1024 = _ExtremeWirelessIntfFrameSizeErrorTX1024_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 40, 1, 11),
    _ExtremeWirelessIntfFrameSizeErrorTX1024_Type()
)
extremeWirelessIntfFrameSizeErrorTX1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeErrorTX1024.setStatus("current")
_ExtremeWirelessIntfFrameSizeErrorTX2048_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeErrorTX2048_Object = MibTableColumn
extremeWirelessIntfFrameSizeErrorTX2048 = _ExtremeWirelessIntfFrameSizeErrorTX2048_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 40, 1, 12),
    _ExtremeWirelessIntfFrameSizeErrorTX2048_Type()
)
extremeWirelessIntfFrameSizeErrorTX2048.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeErrorTX2048.setStatus("current")
_ExtremeWirelessIntfFrameSizeErrorRX64_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeErrorRX64_Object = MibTableColumn
extremeWirelessIntfFrameSizeErrorRX64 = _ExtremeWirelessIntfFrameSizeErrorRX64_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 40, 1, 13),
    _ExtremeWirelessIntfFrameSizeErrorRX64_Type()
)
extremeWirelessIntfFrameSizeErrorRX64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeErrorRX64.setStatus("current")
_ExtremeWirelessIntfFrameSizeErrorRX128_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeErrorRX128_Object = MibTableColumn
extremeWirelessIntfFrameSizeErrorRX128 = _ExtremeWirelessIntfFrameSizeErrorRX128_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 40, 1, 14),
    _ExtremeWirelessIntfFrameSizeErrorRX128_Type()
)
extremeWirelessIntfFrameSizeErrorRX128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeErrorRX128.setStatus("current")
_ExtremeWirelessIntfFrameSizeErrorRX256_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeErrorRX256_Object = MibTableColumn
extremeWirelessIntfFrameSizeErrorRX256 = _ExtremeWirelessIntfFrameSizeErrorRX256_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 40, 1, 15),
    _ExtremeWirelessIntfFrameSizeErrorRX256_Type()
)
extremeWirelessIntfFrameSizeErrorRX256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeErrorRX256.setStatus("current")
_ExtremeWirelessIntfFrameSizeErrorRX512_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeErrorRX512_Object = MibTableColumn
extremeWirelessIntfFrameSizeErrorRX512 = _ExtremeWirelessIntfFrameSizeErrorRX512_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 40, 1, 16),
    _ExtremeWirelessIntfFrameSizeErrorRX512_Type()
)
extremeWirelessIntfFrameSizeErrorRX512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeErrorRX512.setStatus("current")
_ExtremeWirelessIntfFrameSizeErrorRX1024_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeErrorRX1024_Object = MibTableColumn
extremeWirelessIntfFrameSizeErrorRX1024 = _ExtremeWirelessIntfFrameSizeErrorRX1024_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 40, 1, 17),
    _ExtremeWirelessIntfFrameSizeErrorRX1024_Type()
)
extremeWirelessIntfFrameSizeErrorRX1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeErrorRX1024.setStatus("current")
_ExtremeWirelessIntfFrameSizeErrorRX2048_Type = Unsigned32
_ExtremeWirelessIntfFrameSizeErrorRX2048_Object = MibTableColumn
extremeWirelessIntfFrameSizeErrorRX2048 = _ExtremeWirelessIntfFrameSizeErrorRX2048_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 40, 1, 18),
    _ExtremeWirelessIntfFrameSizeErrorRX2048_Type()
)
extremeWirelessIntfFrameSizeErrorRX2048.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSizeErrorRX2048.setStatus("current")
_ExtremeWirelessIntfFrameSpeedTable_Object = MibTable
extremeWirelessIntfFrameSpeedTable = _ExtremeWirelessIntfFrameSpeedTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41)
)
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSpeedTable.setStatus("current")
_ExtremeWirelessIntfFrameSpeedEntry_Object = MibTableRow
extremeWirelessIntfFrameSpeedEntry = _ExtremeWirelessIntfFrameSpeedEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1)
)
extremeWirelessIntfFrameSpeedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSpeedEntry.setStatus("current")
_ExtremeWirelessIntfSpeedMgmtTX1_Type = Unsigned32
_ExtremeWirelessIntfSpeedMgmtTX1_Object = MibTableColumn
extremeWirelessIntfSpeedMgmtTX1 = _ExtremeWirelessIntfSpeedMgmtTX1_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 1),
    _ExtremeWirelessIntfSpeedMgmtTX1_Type()
)
extremeWirelessIntfSpeedMgmtTX1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedMgmtTX1.setStatus("current")
_ExtremeWirelessIntfSpeedMgmtTX2_Type = Unsigned32
_ExtremeWirelessIntfSpeedMgmtTX2_Object = MibTableColumn
extremeWirelessIntfSpeedMgmtTX2 = _ExtremeWirelessIntfSpeedMgmtTX2_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 2),
    _ExtremeWirelessIntfSpeedMgmtTX2_Type()
)
extremeWirelessIntfSpeedMgmtTX2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedMgmtTX2.setStatus("current")
_ExtremeWirelessIntfSpeedMgmtTX5p5_Type = Unsigned32
_ExtremeWirelessIntfSpeedMgmtTX5p5_Object = MibTableColumn
extremeWirelessIntfSpeedMgmtTX5p5 = _ExtremeWirelessIntfSpeedMgmtTX5p5_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 3),
    _ExtremeWirelessIntfSpeedMgmtTX5p5_Type()
)
extremeWirelessIntfSpeedMgmtTX5p5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedMgmtTX5p5.setStatus("current")
_ExtremeWirelessIntfSpeedMgmtTX6_Type = Unsigned32
_ExtremeWirelessIntfSpeedMgmtTX6_Object = MibTableColumn
extremeWirelessIntfSpeedMgmtTX6 = _ExtremeWirelessIntfSpeedMgmtTX6_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 4),
    _ExtremeWirelessIntfSpeedMgmtTX6_Type()
)
extremeWirelessIntfSpeedMgmtTX6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedMgmtTX6.setStatus("current")
_ExtremeWirelessIntfSpeedMgmtTX9_Type = Unsigned32
_ExtremeWirelessIntfSpeedMgmtTX9_Object = MibTableColumn
extremeWirelessIntfSpeedMgmtTX9 = _ExtremeWirelessIntfSpeedMgmtTX9_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 5),
    _ExtremeWirelessIntfSpeedMgmtTX9_Type()
)
extremeWirelessIntfSpeedMgmtTX9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedMgmtTX9.setStatus("current")
_ExtremeWirelessIntfSpeedMgmtTX11_Type = Unsigned32
_ExtremeWirelessIntfSpeedMgmtTX11_Object = MibTableColumn
extremeWirelessIntfSpeedMgmtTX11 = _ExtremeWirelessIntfSpeedMgmtTX11_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 6),
    _ExtremeWirelessIntfSpeedMgmtTX11_Type()
)
extremeWirelessIntfSpeedMgmtTX11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedMgmtTX11.setStatus("current")
_ExtremeWirelessIntfSpeedMgmtTX12_Type = Unsigned32
_ExtremeWirelessIntfSpeedMgmtTX12_Object = MibTableColumn
extremeWirelessIntfSpeedMgmtTX12 = _ExtremeWirelessIntfSpeedMgmtTX12_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 7),
    _ExtremeWirelessIntfSpeedMgmtTX12_Type()
)
extremeWirelessIntfSpeedMgmtTX12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedMgmtTX12.setStatus("current")
_ExtremeWirelessIntfSpeedMgmtTX18_Type = Unsigned32
_ExtremeWirelessIntfSpeedMgmtTX18_Object = MibTableColumn
extremeWirelessIntfSpeedMgmtTX18 = _ExtremeWirelessIntfSpeedMgmtTX18_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 8),
    _ExtremeWirelessIntfSpeedMgmtTX18_Type()
)
extremeWirelessIntfSpeedMgmtTX18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedMgmtTX18.setStatus("current")
_ExtremeWirelessIntfSpeedMgmtTX24_Type = Unsigned32
_ExtremeWirelessIntfSpeedMgmtTX24_Object = MibTableColumn
extremeWirelessIntfSpeedMgmtTX24 = _ExtremeWirelessIntfSpeedMgmtTX24_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 9),
    _ExtremeWirelessIntfSpeedMgmtTX24_Type()
)
extremeWirelessIntfSpeedMgmtTX24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedMgmtTX24.setStatus("current")
_ExtremeWirelessIntfSpeedMgmtTX36_Type = Unsigned32
_ExtremeWirelessIntfSpeedMgmtTX36_Object = MibTableColumn
extremeWirelessIntfSpeedMgmtTX36 = _ExtremeWirelessIntfSpeedMgmtTX36_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 10),
    _ExtremeWirelessIntfSpeedMgmtTX36_Type()
)
extremeWirelessIntfSpeedMgmtTX36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedMgmtTX36.setStatus("current")
_ExtremeWirelessIntfSpeedMgmtTX48_Type = Unsigned32
_ExtremeWirelessIntfSpeedMgmtTX48_Object = MibTableColumn
extremeWirelessIntfSpeedMgmtTX48 = _ExtremeWirelessIntfSpeedMgmtTX48_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 11),
    _ExtremeWirelessIntfSpeedMgmtTX48_Type()
)
extremeWirelessIntfSpeedMgmtTX48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedMgmtTX48.setStatus("current")
_ExtremeWirelessIntfSpeedMgmtTX54_Type = Unsigned32
_ExtremeWirelessIntfSpeedMgmtTX54_Object = MibTableColumn
extremeWirelessIntfSpeedMgmtTX54 = _ExtremeWirelessIntfSpeedMgmtTX54_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 12),
    _ExtremeWirelessIntfSpeedMgmtTX54_Type()
)
extremeWirelessIntfSpeedMgmtTX54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedMgmtTX54.setStatus("current")
_ExtremeWirelessIntfSpeedMgmtRX1_Type = Unsigned32
_ExtremeWirelessIntfSpeedMgmtRX1_Object = MibTableColumn
extremeWirelessIntfSpeedMgmtRX1 = _ExtremeWirelessIntfSpeedMgmtRX1_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 13),
    _ExtremeWirelessIntfSpeedMgmtRX1_Type()
)
extremeWirelessIntfSpeedMgmtRX1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedMgmtRX1.setStatus("current")
_ExtremeWirelessIntfSpeedMgmtRX2_Type = Unsigned32
_ExtremeWirelessIntfSpeedMgmtRX2_Object = MibTableColumn
extremeWirelessIntfSpeedMgmtRX2 = _ExtremeWirelessIntfSpeedMgmtRX2_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 14),
    _ExtremeWirelessIntfSpeedMgmtRX2_Type()
)
extremeWirelessIntfSpeedMgmtRX2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedMgmtRX2.setStatus("current")
_ExtremeWirelessIntfSpeedMgmtRX5p5_Type = Unsigned32
_ExtremeWirelessIntfSpeedMgmtRX5p5_Object = MibTableColumn
extremeWirelessIntfSpeedMgmtRX5p5 = _ExtremeWirelessIntfSpeedMgmtRX5p5_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 15),
    _ExtremeWirelessIntfSpeedMgmtRX5p5_Type()
)
extremeWirelessIntfSpeedMgmtRX5p5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedMgmtRX5p5.setStatus("current")
_ExtremeWirelessIntfSpeedMgmtRX6_Type = Unsigned32
_ExtremeWirelessIntfSpeedMgmtRX6_Object = MibTableColumn
extremeWirelessIntfSpeedMgmtRX6 = _ExtremeWirelessIntfSpeedMgmtRX6_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 16),
    _ExtremeWirelessIntfSpeedMgmtRX6_Type()
)
extremeWirelessIntfSpeedMgmtRX6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedMgmtRX6.setStatus("current")
_ExtremeWirelessIntfSpeedMgmtRX9_Type = Unsigned32
_ExtremeWirelessIntfSpeedMgmtRX9_Object = MibTableColumn
extremeWirelessIntfSpeedMgmtRX9 = _ExtremeWirelessIntfSpeedMgmtRX9_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 17),
    _ExtremeWirelessIntfSpeedMgmtRX9_Type()
)
extremeWirelessIntfSpeedMgmtRX9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedMgmtRX9.setStatus("current")
_ExtremeWirelessIntfSpeedMgmtRX11_Type = Unsigned32
_ExtremeWirelessIntfSpeedMgmtRX11_Object = MibTableColumn
extremeWirelessIntfSpeedMgmtRX11 = _ExtremeWirelessIntfSpeedMgmtRX11_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 18),
    _ExtremeWirelessIntfSpeedMgmtRX11_Type()
)
extremeWirelessIntfSpeedMgmtRX11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedMgmtRX11.setStatus("current")
_ExtremeWirelessIntfSpeedMgmtRX12_Type = Unsigned32
_ExtremeWirelessIntfSpeedMgmtRX12_Object = MibTableColumn
extremeWirelessIntfSpeedMgmtRX12 = _ExtremeWirelessIntfSpeedMgmtRX12_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 19),
    _ExtremeWirelessIntfSpeedMgmtRX12_Type()
)
extremeWirelessIntfSpeedMgmtRX12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedMgmtRX12.setStatus("current")
_ExtremeWirelessIntfSpeedMgmtRX18_Type = Unsigned32
_ExtremeWirelessIntfSpeedMgmtRX18_Object = MibTableColumn
extremeWirelessIntfSpeedMgmtRX18 = _ExtremeWirelessIntfSpeedMgmtRX18_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 20),
    _ExtremeWirelessIntfSpeedMgmtRX18_Type()
)
extremeWirelessIntfSpeedMgmtRX18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedMgmtRX18.setStatus("current")
_ExtremeWirelessIntfSpeedMgmtRX24_Type = Unsigned32
_ExtremeWirelessIntfSpeedMgmtRX24_Object = MibTableColumn
extremeWirelessIntfSpeedMgmtRX24 = _ExtremeWirelessIntfSpeedMgmtRX24_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 21),
    _ExtremeWirelessIntfSpeedMgmtRX24_Type()
)
extremeWirelessIntfSpeedMgmtRX24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedMgmtRX24.setStatus("current")
_ExtremeWirelessIntfSpeedMgmtRX36_Type = Unsigned32
_ExtremeWirelessIntfSpeedMgmtRX36_Object = MibTableColumn
extremeWirelessIntfSpeedMgmtRX36 = _ExtremeWirelessIntfSpeedMgmtRX36_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 22),
    _ExtremeWirelessIntfSpeedMgmtRX36_Type()
)
extremeWirelessIntfSpeedMgmtRX36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedMgmtRX36.setStatus("current")
_ExtremeWirelessIntfSpeedMgmtRX48_Type = Unsigned32
_ExtremeWirelessIntfSpeedMgmtRX48_Object = MibTableColumn
extremeWirelessIntfSpeedMgmtRX48 = _ExtremeWirelessIntfSpeedMgmtRX48_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 23),
    _ExtremeWirelessIntfSpeedMgmtRX48_Type()
)
extremeWirelessIntfSpeedMgmtRX48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedMgmtRX48.setStatus("current")
_ExtremeWirelessIntfSpeedMgmtRX54_Type = Unsigned32
_ExtremeWirelessIntfSpeedMgmtRX54_Object = MibTableColumn
extremeWirelessIntfSpeedMgmtRX54 = _ExtremeWirelessIntfSpeedMgmtRX54_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 24),
    _ExtremeWirelessIntfSpeedMgmtRX54_Type()
)
extremeWirelessIntfSpeedMgmtRX54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedMgmtRX54.setStatus("current")
_ExtremeWirelessIntfSpeedCtlTX1_Type = Unsigned32
_ExtremeWirelessIntfSpeedCtlTX1_Object = MibTableColumn
extremeWirelessIntfSpeedCtlTX1 = _ExtremeWirelessIntfSpeedCtlTX1_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 25),
    _ExtremeWirelessIntfSpeedCtlTX1_Type()
)
extremeWirelessIntfSpeedCtlTX1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedCtlTX1.setStatus("current")
_ExtremeWirelessIntfSpeedCtlTX2_Type = Unsigned32
_ExtremeWirelessIntfSpeedCtlTX2_Object = MibTableColumn
extremeWirelessIntfSpeedCtlTX2 = _ExtremeWirelessIntfSpeedCtlTX2_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 26),
    _ExtremeWirelessIntfSpeedCtlTX2_Type()
)
extremeWirelessIntfSpeedCtlTX2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedCtlTX2.setStatus("current")
_ExtremeWirelessIntfSpeedCtlTX5p5_Type = Unsigned32
_ExtremeWirelessIntfSpeedCtlTX5p5_Object = MibTableColumn
extremeWirelessIntfSpeedCtlTX5p5 = _ExtremeWirelessIntfSpeedCtlTX5p5_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 27),
    _ExtremeWirelessIntfSpeedCtlTX5p5_Type()
)
extremeWirelessIntfSpeedCtlTX5p5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedCtlTX5p5.setStatus("current")
_ExtremeWirelessIntfSpeedCtlTX6_Type = Unsigned32
_ExtremeWirelessIntfSpeedCtlTX6_Object = MibTableColumn
extremeWirelessIntfSpeedCtlTX6 = _ExtremeWirelessIntfSpeedCtlTX6_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 28),
    _ExtremeWirelessIntfSpeedCtlTX6_Type()
)
extremeWirelessIntfSpeedCtlTX6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedCtlTX6.setStatus("current")
_ExtremeWirelessIntfSpeedCtlTX9_Type = Unsigned32
_ExtremeWirelessIntfSpeedCtlTX9_Object = MibTableColumn
extremeWirelessIntfSpeedCtlTX9 = _ExtremeWirelessIntfSpeedCtlTX9_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 29),
    _ExtremeWirelessIntfSpeedCtlTX9_Type()
)
extremeWirelessIntfSpeedCtlTX9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedCtlTX9.setStatus("current")
_ExtremeWirelessIntfSpeedCtlTX11_Type = Unsigned32
_ExtremeWirelessIntfSpeedCtlTX11_Object = MibTableColumn
extremeWirelessIntfSpeedCtlTX11 = _ExtremeWirelessIntfSpeedCtlTX11_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 30),
    _ExtremeWirelessIntfSpeedCtlTX11_Type()
)
extremeWirelessIntfSpeedCtlTX11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedCtlTX11.setStatus("current")
_ExtremeWirelessIntfSpeedCtlTX12_Type = Unsigned32
_ExtremeWirelessIntfSpeedCtlTX12_Object = MibTableColumn
extremeWirelessIntfSpeedCtlTX12 = _ExtremeWirelessIntfSpeedCtlTX12_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 31),
    _ExtremeWirelessIntfSpeedCtlTX12_Type()
)
extremeWirelessIntfSpeedCtlTX12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedCtlTX12.setStatus("current")
_ExtremeWirelessIntfSpeedCtlTX18_Type = Unsigned32
_ExtremeWirelessIntfSpeedCtlTX18_Object = MibTableColumn
extremeWirelessIntfSpeedCtlTX18 = _ExtremeWirelessIntfSpeedCtlTX18_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 32),
    _ExtremeWirelessIntfSpeedCtlTX18_Type()
)
extremeWirelessIntfSpeedCtlTX18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedCtlTX18.setStatus("current")
_ExtremeWirelessIntfSpeedCtlTX24_Type = Unsigned32
_ExtremeWirelessIntfSpeedCtlTX24_Object = MibTableColumn
extremeWirelessIntfSpeedCtlTX24 = _ExtremeWirelessIntfSpeedCtlTX24_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 33),
    _ExtremeWirelessIntfSpeedCtlTX24_Type()
)
extremeWirelessIntfSpeedCtlTX24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedCtlTX24.setStatus("current")
_ExtremeWirelessIntfSpeedCtlTX36_Type = Unsigned32
_ExtremeWirelessIntfSpeedCtlTX36_Object = MibTableColumn
extremeWirelessIntfSpeedCtlTX36 = _ExtremeWirelessIntfSpeedCtlTX36_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 34),
    _ExtremeWirelessIntfSpeedCtlTX36_Type()
)
extremeWirelessIntfSpeedCtlTX36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedCtlTX36.setStatus("current")
_ExtremeWirelessIntfSpeedCtlTX48_Type = Unsigned32
_ExtremeWirelessIntfSpeedCtlTX48_Object = MibTableColumn
extremeWirelessIntfSpeedCtlTX48 = _ExtremeWirelessIntfSpeedCtlTX48_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 35),
    _ExtremeWirelessIntfSpeedCtlTX48_Type()
)
extremeWirelessIntfSpeedCtlTX48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedCtlTX48.setStatus("current")
_ExtremeWirelessIntfSpeedCtlTX54_Type = Unsigned32
_ExtremeWirelessIntfSpeedCtlTX54_Object = MibTableColumn
extremeWirelessIntfSpeedCtlTX54 = _ExtremeWirelessIntfSpeedCtlTX54_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 36),
    _ExtremeWirelessIntfSpeedCtlTX54_Type()
)
extremeWirelessIntfSpeedCtlTX54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedCtlTX54.setStatus("current")
_ExtremeWirelessIntfSpeedCtlRX1_Type = Unsigned32
_ExtremeWirelessIntfSpeedCtlRX1_Object = MibTableColumn
extremeWirelessIntfSpeedCtlRX1 = _ExtremeWirelessIntfSpeedCtlRX1_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 37),
    _ExtremeWirelessIntfSpeedCtlRX1_Type()
)
extremeWirelessIntfSpeedCtlRX1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedCtlRX1.setStatus("current")
_ExtremeWirelessIntfSpeedCtlRX2_Type = Unsigned32
_ExtremeWirelessIntfSpeedCtlRX2_Object = MibTableColumn
extremeWirelessIntfSpeedCtlRX2 = _ExtremeWirelessIntfSpeedCtlRX2_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 38),
    _ExtremeWirelessIntfSpeedCtlRX2_Type()
)
extremeWirelessIntfSpeedCtlRX2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedCtlRX2.setStatus("current")
_ExtremeWirelessIntfSpeedCtlRX5p5_Type = Unsigned32
_ExtremeWirelessIntfSpeedCtlRX5p5_Object = MibTableColumn
extremeWirelessIntfSpeedCtlRX5p5 = _ExtremeWirelessIntfSpeedCtlRX5p5_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 39),
    _ExtremeWirelessIntfSpeedCtlRX5p5_Type()
)
extremeWirelessIntfSpeedCtlRX5p5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedCtlRX5p5.setStatus("current")
_ExtremeWirelessIntfSpeedCtlRX6_Type = Unsigned32
_ExtremeWirelessIntfSpeedCtlRX6_Object = MibTableColumn
extremeWirelessIntfSpeedCtlRX6 = _ExtremeWirelessIntfSpeedCtlRX6_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 40),
    _ExtremeWirelessIntfSpeedCtlRX6_Type()
)
extremeWirelessIntfSpeedCtlRX6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedCtlRX6.setStatus("current")
_ExtremeWirelessIntfSpeedCtlRX9_Type = Unsigned32
_ExtremeWirelessIntfSpeedCtlRX9_Object = MibTableColumn
extremeWirelessIntfSpeedCtlRX9 = _ExtremeWirelessIntfSpeedCtlRX9_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 41),
    _ExtremeWirelessIntfSpeedCtlRX9_Type()
)
extremeWirelessIntfSpeedCtlRX9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedCtlRX9.setStatus("current")
_ExtremeWirelessIntfSpeedCtlRX11_Type = Unsigned32
_ExtremeWirelessIntfSpeedCtlRX11_Object = MibTableColumn
extremeWirelessIntfSpeedCtlRX11 = _ExtremeWirelessIntfSpeedCtlRX11_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 42),
    _ExtremeWirelessIntfSpeedCtlRX11_Type()
)
extremeWirelessIntfSpeedCtlRX11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedCtlRX11.setStatus("current")
_ExtremeWirelessIntfSpeedCtlRX12_Type = Unsigned32
_ExtremeWirelessIntfSpeedCtlRX12_Object = MibTableColumn
extremeWirelessIntfSpeedCtlRX12 = _ExtremeWirelessIntfSpeedCtlRX12_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 43),
    _ExtremeWirelessIntfSpeedCtlRX12_Type()
)
extremeWirelessIntfSpeedCtlRX12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedCtlRX12.setStatus("current")
_ExtremeWirelessIntfSpeedCtlRX18_Type = Unsigned32
_ExtremeWirelessIntfSpeedCtlRX18_Object = MibTableColumn
extremeWirelessIntfSpeedCtlRX18 = _ExtremeWirelessIntfSpeedCtlRX18_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 44),
    _ExtremeWirelessIntfSpeedCtlRX18_Type()
)
extremeWirelessIntfSpeedCtlRX18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedCtlRX18.setStatus("current")
_ExtremeWirelessIntfSpeedCtlRX24_Type = Unsigned32
_ExtremeWirelessIntfSpeedCtlRX24_Object = MibTableColumn
extremeWirelessIntfSpeedCtlRX24 = _ExtremeWirelessIntfSpeedCtlRX24_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 45),
    _ExtremeWirelessIntfSpeedCtlRX24_Type()
)
extremeWirelessIntfSpeedCtlRX24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedCtlRX24.setStatus("current")
_ExtremeWirelessIntfSpeedCtlRX36_Type = Unsigned32
_ExtremeWirelessIntfSpeedCtlRX36_Object = MibTableColumn
extremeWirelessIntfSpeedCtlRX36 = _ExtremeWirelessIntfSpeedCtlRX36_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 46),
    _ExtremeWirelessIntfSpeedCtlRX36_Type()
)
extremeWirelessIntfSpeedCtlRX36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedCtlRX36.setStatus("current")
_ExtremeWirelessIntfSpeedCtlRX48_Type = Unsigned32
_ExtremeWirelessIntfSpeedCtlRX48_Object = MibTableColumn
extremeWirelessIntfSpeedCtlRX48 = _ExtremeWirelessIntfSpeedCtlRX48_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 47),
    _ExtremeWirelessIntfSpeedCtlRX48_Type()
)
extremeWirelessIntfSpeedCtlRX48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedCtlRX48.setStatus("current")
_ExtremeWirelessIntfSpeedCtlRX54_Type = Unsigned32
_ExtremeWirelessIntfSpeedCtlRX54_Object = MibTableColumn
extremeWirelessIntfSpeedCtlRX54 = _ExtremeWirelessIntfSpeedCtlRX54_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 48),
    _ExtremeWirelessIntfSpeedCtlRX54_Type()
)
extremeWirelessIntfSpeedCtlRX54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedCtlRX54.setStatus("current")
_ExtremeWirelessIntfSpeedDataTX1_Type = Unsigned32
_ExtremeWirelessIntfSpeedDataTX1_Object = MibTableColumn
extremeWirelessIntfSpeedDataTX1 = _ExtremeWirelessIntfSpeedDataTX1_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 49),
    _ExtremeWirelessIntfSpeedDataTX1_Type()
)
extremeWirelessIntfSpeedDataTX1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedDataTX1.setStatus("current")
_ExtremeWirelessIntfSpeedDataTX2_Type = Unsigned32
_ExtremeWirelessIntfSpeedDataTX2_Object = MibTableColumn
extremeWirelessIntfSpeedDataTX2 = _ExtremeWirelessIntfSpeedDataTX2_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 50),
    _ExtremeWirelessIntfSpeedDataTX2_Type()
)
extremeWirelessIntfSpeedDataTX2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedDataTX2.setStatus("current")
_ExtremeWirelessIntfSpeedDataTX5p5_Type = Unsigned32
_ExtremeWirelessIntfSpeedDataTX5p5_Object = MibTableColumn
extremeWirelessIntfSpeedDataTX5p5 = _ExtremeWirelessIntfSpeedDataTX5p5_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 51),
    _ExtremeWirelessIntfSpeedDataTX5p5_Type()
)
extremeWirelessIntfSpeedDataTX5p5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedDataTX5p5.setStatus("current")
_ExtremeWirelessIntfSpeedDataTX6_Type = Unsigned32
_ExtremeWirelessIntfSpeedDataTX6_Object = MibTableColumn
extremeWirelessIntfSpeedDataTX6 = _ExtremeWirelessIntfSpeedDataTX6_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 52),
    _ExtremeWirelessIntfSpeedDataTX6_Type()
)
extremeWirelessIntfSpeedDataTX6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedDataTX6.setStatus("current")
_ExtremeWirelessIntfSpeedDataTX9_Type = Unsigned32
_ExtremeWirelessIntfSpeedDataTX9_Object = MibTableColumn
extremeWirelessIntfSpeedDataTX9 = _ExtremeWirelessIntfSpeedDataTX9_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 53),
    _ExtremeWirelessIntfSpeedDataTX9_Type()
)
extremeWirelessIntfSpeedDataTX9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedDataTX9.setStatus("current")
_ExtremeWirelessIntfSpeedDataTX11_Type = Unsigned32
_ExtremeWirelessIntfSpeedDataTX11_Object = MibTableColumn
extremeWirelessIntfSpeedDataTX11 = _ExtremeWirelessIntfSpeedDataTX11_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 54),
    _ExtremeWirelessIntfSpeedDataTX11_Type()
)
extremeWirelessIntfSpeedDataTX11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedDataTX11.setStatus("current")
_ExtremeWirelessIntfSpeedDataTX12_Type = Unsigned32
_ExtremeWirelessIntfSpeedDataTX12_Object = MibTableColumn
extremeWirelessIntfSpeedDataTX12 = _ExtremeWirelessIntfSpeedDataTX12_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 55),
    _ExtremeWirelessIntfSpeedDataTX12_Type()
)
extremeWirelessIntfSpeedDataTX12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedDataTX12.setStatus("current")
_ExtremeWirelessIntfSpeedDataTX18_Type = Unsigned32
_ExtremeWirelessIntfSpeedDataTX18_Object = MibTableColumn
extremeWirelessIntfSpeedDataTX18 = _ExtremeWirelessIntfSpeedDataTX18_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 56),
    _ExtremeWirelessIntfSpeedDataTX18_Type()
)
extremeWirelessIntfSpeedDataTX18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedDataTX18.setStatus("current")
_ExtremeWirelessIntfSpeedDataTX24_Type = Unsigned32
_ExtremeWirelessIntfSpeedDataTX24_Object = MibTableColumn
extremeWirelessIntfSpeedDataTX24 = _ExtremeWirelessIntfSpeedDataTX24_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 57),
    _ExtremeWirelessIntfSpeedDataTX24_Type()
)
extremeWirelessIntfSpeedDataTX24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedDataTX24.setStatus("current")
_ExtremeWirelessIntfSpeedDataTX36_Type = Unsigned32
_ExtremeWirelessIntfSpeedDataTX36_Object = MibTableColumn
extremeWirelessIntfSpeedDataTX36 = _ExtremeWirelessIntfSpeedDataTX36_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 58),
    _ExtremeWirelessIntfSpeedDataTX36_Type()
)
extremeWirelessIntfSpeedDataTX36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedDataTX36.setStatus("current")
_ExtremeWirelessIntfSpeedDataTX48_Type = Unsigned32
_ExtremeWirelessIntfSpeedDataTX48_Object = MibTableColumn
extremeWirelessIntfSpeedDataTX48 = _ExtremeWirelessIntfSpeedDataTX48_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 59),
    _ExtremeWirelessIntfSpeedDataTX48_Type()
)
extremeWirelessIntfSpeedDataTX48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedDataTX48.setStatus("current")
_ExtremeWirelessIntfSpeedDataTX54_Type = Unsigned32
_ExtremeWirelessIntfSpeedDataTX54_Object = MibTableColumn
extremeWirelessIntfSpeedDataTX54 = _ExtremeWirelessIntfSpeedDataTX54_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 60),
    _ExtremeWirelessIntfSpeedDataTX54_Type()
)
extremeWirelessIntfSpeedDataTX54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedDataTX54.setStatus("current")
_ExtremeWirelessIntfSpeedDataRX1_Type = Unsigned32
_ExtremeWirelessIntfSpeedDataRX1_Object = MibTableColumn
extremeWirelessIntfSpeedDataRX1 = _ExtremeWirelessIntfSpeedDataRX1_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 61),
    _ExtremeWirelessIntfSpeedDataRX1_Type()
)
extremeWirelessIntfSpeedDataRX1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedDataRX1.setStatus("current")
_ExtremeWirelessIntfSpeedDataRX2_Type = Unsigned32
_ExtremeWirelessIntfSpeedDataRX2_Object = MibTableColumn
extremeWirelessIntfSpeedDataRX2 = _ExtremeWirelessIntfSpeedDataRX2_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 62),
    _ExtremeWirelessIntfSpeedDataRX2_Type()
)
extremeWirelessIntfSpeedDataRX2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedDataRX2.setStatus("current")
_ExtremeWirelessIntfSpeedDataRX5p5_Type = Unsigned32
_ExtremeWirelessIntfSpeedDataRX5p5_Object = MibTableColumn
extremeWirelessIntfSpeedDataRX5p5 = _ExtremeWirelessIntfSpeedDataRX5p5_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 63),
    _ExtremeWirelessIntfSpeedDataRX5p5_Type()
)
extremeWirelessIntfSpeedDataRX5p5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedDataRX5p5.setStatus("current")
_ExtremeWirelessIntfSpeedDataRX6_Type = Unsigned32
_ExtremeWirelessIntfSpeedDataRX6_Object = MibTableColumn
extremeWirelessIntfSpeedDataRX6 = _ExtremeWirelessIntfSpeedDataRX6_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 64),
    _ExtremeWirelessIntfSpeedDataRX6_Type()
)
extremeWirelessIntfSpeedDataRX6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedDataRX6.setStatus("current")
_ExtremeWirelessIntfSpeedDataRX9_Type = Unsigned32
_ExtremeWirelessIntfSpeedDataRX9_Object = MibTableColumn
extremeWirelessIntfSpeedDataRX9 = _ExtremeWirelessIntfSpeedDataRX9_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 65),
    _ExtremeWirelessIntfSpeedDataRX9_Type()
)
extremeWirelessIntfSpeedDataRX9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedDataRX9.setStatus("current")
_ExtremeWirelessIntfSpeedDataRX11_Type = Unsigned32
_ExtremeWirelessIntfSpeedDataRX11_Object = MibTableColumn
extremeWirelessIntfSpeedDataRX11 = _ExtremeWirelessIntfSpeedDataRX11_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 66),
    _ExtremeWirelessIntfSpeedDataRX11_Type()
)
extremeWirelessIntfSpeedDataRX11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedDataRX11.setStatus("current")
_ExtremeWirelessIntfSpeedDataRX12_Type = Unsigned32
_ExtremeWirelessIntfSpeedDataRX12_Object = MibTableColumn
extremeWirelessIntfSpeedDataRX12 = _ExtremeWirelessIntfSpeedDataRX12_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 67),
    _ExtremeWirelessIntfSpeedDataRX12_Type()
)
extremeWirelessIntfSpeedDataRX12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedDataRX12.setStatus("current")
_ExtremeWirelessIntfSpeedDataRX18_Type = Unsigned32
_ExtremeWirelessIntfSpeedDataRX18_Object = MibTableColumn
extremeWirelessIntfSpeedDataRX18 = _ExtremeWirelessIntfSpeedDataRX18_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 68),
    _ExtremeWirelessIntfSpeedDataRX18_Type()
)
extremeWirelessIntfSpeedDataRX18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedDataRX18.setStatus("current")
_ExtremeWirelessIntfSpeedDataRX24_Type = Unsigned32
_ExtremeWirelessIntfSpeedDataRX24_Object = MibTableColumn
extremeWirelessIntfSpeedDataRX24 = _ExtremeWirelessIntfSpeedDataRX24_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 69),
    _ExtremeWirelessIntfSpeedDataRX24_Type()
)
extremeWirelessIntfSpeedDataRX24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedDataRX24.setStatus("current")
_ExtremeWirelessIntfSpeedDataRX36_Type = Unsigned32
_ExtremeWirelessIntfSpeedDataRX36_Object = MibTableColumn
extremeWirelessIntfSpeedDataRX36 = _ExtremeWirelessIntfSpeedDataRX36_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 70),
    _ExtremeWirelessIntfSpeedDataRX36_Type()
)
extremeWirelessIntfSpeedDataRX36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedDataRX36.setStatus("current")
_ExtremeWirelessIntfSpeedDataRX48_Type = Unsigned32
_ExtremeWirelessIntfSpeedDataRX48_Object = MibTableColumn
extremeWirelessIntfSpeedDataRX48 = _ExtremeWirelessIntfSpeedDataRX48_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 71),
    _ExtremeWirelessIntfSpeedDataRX48_Type()
)
extremeWirelessIntfSpeedDataRX48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedDataRX48.setStatus("current")
_ExtremeWirelessIntfSpeedDataRX54_Type = Unsigned32
_ExtremeWirelessIntfSpeedDataRX54_Object = MibTableColumn
extremeWirelessIntfSpeedDataRX54 = _ExtremeWirelessIntfSpeedDataRX54_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 41, 1, 72),
    _ExtremeWirelessIntfSpeedDataRX54_Type()
)
extremeWirelessIntfSpeedDataRX54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedDataRX54.setStatus("current")
_ExtremeWirelessIntfFrameSpeedErrorTable_Object = MibTable
extremeWirelessIntfFrameSpeedErrorTable = _ExtremeWirelessIntfFrameSpeedErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42)
)
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSpeedErrorTable.setStatus("current")
_ExtremeWirelessIntfFrameSpeedErrorEntry_Object = MibTableRow
extremeWirelessIntfFrameSpeedErrorEntry = _ExtremeWirelessIntfFrameSpeedErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1)
)
extremeWirelessIntfFrameSpeedErrorEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessIntfFrameSpeedErrorEntry.setStatus("current")
_ExtremeWirelessIntfSpeedReXmit1_Type = Unsigned32
_ExtremeWirelessIntfSpeedReXmit1_Object = MibTableColumn
extremeWirelessIntfSpeedReXmit1 = _ExtremeWirelessIntfSpeedReXmit1_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 1),
    _ExtremeWirelessIntfSpeedReXmit1_Type()
)
extremeWirelessIntfSpeedReXmit1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedReXmit1.setStatus("current")
_ExtremeWirelessIntfSpeedReXmit2_Type = Unsigned32
_ExtremeWirelessIntfSpeedReXmit2_Object = MibTableColumn
extremeWirelessIntfSpeedReXmit2 = _ExtremeWirelessIntfSpeedReXmit2_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 2),
    _ExtremeWirelessIntfSpeedReXmit2_Type()
)
extremeWirelessIntfSpeedReXmit2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedReXmit2.setStatus("current")
_ExtremeWirelessIntfSpeedReXmit5p5_Type = Unsigned32
_ExtremeWirelessIntfSpeedReXmit5p5_Object = MibTableColumn
extremeWirelessIntfSpeedReXmit5p5 = _ExtremeWirelessIntfSpeedReXmit5p5_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 3),
    _ExtremeWirelessIntfSpeedReXmit5p5_Type()
)
extremeWirelessIntfSpeedReXmit5p5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedReXmit5p5.setStatus("current")
_ExtremeWirelessIntfSpeedReXmit6_Type = Unsigned32
_ExtremeWirelessIntfSpeedReXmit6_Object = MibTableColumn
extremeWirelessIntfSpeedReXmit6 = _ExtremeWirelessIntfSpeedReXmit6_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 4),
    _ExtremeWirelessIntfSpeedReXmit6_Type()
)
extremeWirelessIntfSpeedReXmit6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedReXmit6.setStatus("current")
_ExtremeWirelessIntfSpeedReXmit9_Type = Unsigned32
_ExtremeWirelessIntfSpeedReXmit9_Object = MibTableColumn
extremeWirelessIntfSpeedReXmit9 = _ExtremeWirelessIntfSpeedReXmit9_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 5),
    _ExtremeWirelessIntfSpeedReXmit9_Type()
)
extremeWirelessIntfSpeedReXmit9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedReXmit9.setStatus("current")
_ExtremeWirelessIntfSpeedReXmit11_Type = Unsigned32
_ExtremeWirelessIntfSpeedReXmit11_Object = MibTableColumn
extremeWirelessIntfSpeedReXmit11 = _ExtremeWirelessIntfSpeedReXmit11_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 6),
    _ExtremeWirelessIntfSpeedReXmit11_Type()
)
extremeWirelessIntfSpeedReXmit11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedReXmit11.setStatus("current")
_ExtremeWirelessIntfSpeedReXmit12_Type = Unsigned32
_ExtremeWirelessIntfSpeedReXmit12_Object = MibTableColumn
extremeWirelessIntfSpeedReXmit12 = _ExtremeWirelessIntfSpeedReXmit12_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 7),
    _ExtremeWirelessIntfSpeedReXmit12_Type()
)
extremeWirelessIntfSpeedReXmit12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedReXmit12.setStatus("current")
_ExtremeWirelessIntfSpeedReXmit18_Type = Unsigned32
_ExtremeWirelessIntfSpeedReXmit18_Object = MibTableColumn
extremeWirelessIntfSpeedReXmit18 = _ExtremeWirelessIntfSpeedReXmit18_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 8),
    _ExtremeWirelessIntfSpeedReXmit18_Type()
)
extremeWirelessIntfSpeedReXmit18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedReXmit18.setStatus("current")
_ExtremeWirelessIntfSpeedReXmit24_Type = Unsigned32
_ExtremeWirelessIntfSpeedReXmit24_Object = MibTableColumn
extremeWirelessIntfSpeedReXmit24 = _ExtremeWirelessIntfSpeedReXmit24_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 9),
    _ExtremeWirelessIntfSpeedReXmit24_Type()
)
extremeWirelessIntfSpeedReXmit24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedReXmit24.setStatus("current")
_ExtremeWirelessIntfSpeedReXmit36_Type = Unsigned32
_ExtremeWirelessIntfSpeedReXmit36_Object = MibTableColumn
extremeWirelessIntfSpeedReXmit36 = _ExtremeWirelessIntfSpeedReXmit36_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 10),
    _ExtremeWirelessIntfSpeedReXmit36_Type()
)
extremeWirelessIntfSpeedReXmit36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedReXmit36.setStatus("current")
_ExtremeWirelessIntfSpeedReXmit48_Type = Unsigned32
_ExtremeWirelessIntfSpeedReXmit48_Object = MibTableColumn
extremeWirelessIntfSpeedReXmit48 = _ExtremeWirelessIntfSpeedReXmit48_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 11),
    _ExtremeWirelessIntfSpeedReXmit48_Type()
)
extremeWirelessIntfSpeedReXmit48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedReXmit48.setStatus("current")
_ExtremeWirelessIntfSpeedReXmit54_Type = Unsigned32
_ExtremeWirelessIntfSpeedReXmit54_Object = MibTableColumn
extremeWirelessIntfSpeedReXmit54 = _ExtremeWirelessIntfSpeedReXmit54_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 12),
    _ExtremeWirelessIntfSpeedReXmit54_Type()
)
extremeWirelessIntfSpeedReXmit54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedReXmit54.setStatus("current")
_ExtremeWirelessIntfSpeedErrorTX1_Type = Unsigned32
_ExtremeWirelessIntfSpeedErrorTX1_Object = MibTableColumn
extremeWirelessIntfSpeedErrorTX1 = _ExtremeWirelessIntfSpeedErrorTX1_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 13),
    _ExtremeWirelessIntfSpeedErrorTX1_Type()
)
extremeWirelessIntfSpeedErrorTX1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedErrorTX1.setStatus("current")
_ExtremeWirelessIntfSpeedErrorTX2_Type = Unsigned32
_ExtremeWirelessIntfSpeedErrorTX2_Object = MibTableColumn
extremeWirelessIntfSpeedErrorTX2 = _ExtremeWirelessIntfSpeedErrorTX2_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 14),
    _ExtremeWirelessIntfSpeedErrorTX2_Type()
)
extremeWirelessIntfSpeedErrorTX2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedErrorTX2.setStatus("current")
_ExtremeWirelessIntfSpeedErrorTX5p5_Type = Unsigned32
_ExtremeWirelessIntfSpeedErrorTX5p5_Object = MibTableColumn
extremeWirelessIntfSpeedErrorTX5p5 = _ExtremeWirelessIntfSpeedErrorTX5p5_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 15),
    _ExtremeWirelessIntfSpeedErrorTX5p5_Type()
)
extremeWirelessIntfSpeedErrorTX5p5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedErrorTX5p5.setStatus("current")
_ExtremeWirelessIntfSpeedErrorTX6_Type = Unsigned32
_ExtremeWirelessIntfSpeedErrorTX6_Object = MibTableColumn
extremeWirelessIntfSpeedErrorTX6 = _ExtremeWirelessIntfSpeedErrorTX6_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 16),
    _ExtremeWirelessIntfSpeedErrorTX6_Type()
)
extremeWirelessIntfSpeedErrorTX6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedErrorTX6.setStatus("current")
_ExtremeWirelessIntfSpeedErrorTX9_Type = Unsigned32
_ExtremeWirelessIntfSpeedErrorTX9_Object = MibTableColumn
extremeWirelessIntfSpeedErrorTX9 = _ExtremeWirelessIntfSpeedErrorTX9_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 17),
    _ExtremeWirelessIntfSpeedErrorTX9_Type()
)
extremeWirelessIntfSpeedErrorTX9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedErrorTX9.setStatus("current")
_ExtremeWirelessIntfSpeedErrorTX11_Type = Unsigned32
_ExtremeWirelessIntfSpeedErrorTX11_Object = MibTableColumn
extremeWirelessIntfSpeedErrorTX11 = _ExtremeWirelessIntfSpeedErrorTX11_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 18),
    _ExtremeWirelessIntfSpeedErrorTX11_Type()
)
extremeWirelessIntfSpeedErrorTX11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedErrorTX11.setStatus("current")
_ExtremeWirelessIntfSpeedErrorTX12_Type = Unsigned32
_ExtremeWirelessIntfSpeedErrorTX12_Object = MibTableColumn
extremeWirelessIntfSpeedErrorTX12 = _ExtremeWirelessIntfSpeedErrorTX12_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 19),
    _ExtremeWirelessIntfSpeedErrorTX12_Type()
)
extremeWirelessIntfSpeedErrorTX12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedErrorTX12.setStatus("current")
_ExtremeWirelessIntfSpeedErrorTX18_Type = Unsigned32
_ExtremeWirelessIntfSpeedErrorTX18_Object = MibTableColumn
extremeWirelessIntfSpeedErrorTX18 = _ExtremeWirelessIntfSpeedErrorTX18_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 20),
    _ExtremeWirelessIntfSpeedErrorTX18_Type()
)
extremeWirelessIntfSpeedErrorTX18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedErrorTX18.setStatus("current")
_ExtremeWirelessIntfSpeedErrorTX24_Type = Unsigned32
_ExtremeWirelessIntfSpeedErrorTX24_Object = MibTableColumn
extremeWirelessIntfSpeedErrorTX24 = _ExtremeWirelessIntfSpeedErrorTX24_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 21),
    _ExtremeWirelessIntfSpeedErrorTX24_Type()
)
extremeWirelessIntfSpeedErrorTX24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedErrorTX24.setStatus("current")
_ExtremeWirelessIntfSpeedErrorTX36_Type = Unsigned32
_ExtremeWirelessIntfSpeedErrorTX36_Object = MibTableColumn
extremeWirelessIntfSpeedErrorTX36 = _ExtremeWirelessIntfSpeedErrorTX36_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 22),
    _ExtremeWirelessIntfSpeedErrorTX36_Type()
)
extremeWirelessIntfSpeedErrorTX36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedErrorTX36.setStatus("current")
_ExtremeWirelessIntfSpeedErrorTX48_Type = Unsigned32
_ExtremeWirelessIntfSpeedErrorTX48_Object = MibTableColumn
extremeWirelessIntfSpeedErrorTX48 = _ExtremeWirelessIntfSpeedErrorTX48_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 23),
    _ExtremeWirelessIntfSpeedErrorTX48_Type()
)
extremeWirelessIntfSpeedErrorTX48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedErrorTX48.setStatus("current")
_ExtremeWirelessIntfSpeedErrorTX54_Type = Unsigned32
_ExtremeWirelessIntfSpeedErrorTX54_Object = MibTableColumn
extremeWirelessIntfSpeedErrorTX54 = _ExtremeWirelessIntfSpeedErrorTX54_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 24),
    _ExtremeWirelessIntfSpeedErrorTX54_Type()
)
extremeWirelessIntfSpeedErrorTX54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedErrorTX54.setStatus("current")
_ExtremeWirelessIntfSpeedErrorRX1_Type = Unsigned32
_ExtremeWirelessIntfSpeedErrorRX1_Object = MibTableColumn
extremeWirelessIntfSpeedErrorRX1 = _ExtremeWirelessIntfSpeedErrorRX1_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 25),
    _ExtremeWirelessIntfSpeedErrorRX1_Type()
)
extremeWirelessIntfSpeedErrorRX1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedErrorRX1.setStatus("current")
_ExtremeWirelessIntfSpeedErrorRX2_Type = Unsigned32
_ExtremeWirelessIntfSpeedErrorRX2_Object = MibTableColumn
extremeWirelessIntfSpeedErrorRX2 = _ExtremeWirelessIntfSpeedErrorRX2_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 26),
    _ExtremeWirelessIntfSpeedErrorRX2_Type()
)
extremeWirelessIntfSpeedErrorRX2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedErrorRX2.setStatus("current")
_ExtremeWirelessIntfSpeedErrorRX5p5_Type = Unsigned32
_ExtremeWirelessIntfSpeedErrorRX5p5_Object = MibTableColumn
extremeWirelessIntfSpeedErrorRX5p5 = _ExtremeWirelessIntfSpeedErrorRX5p5_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 27),
    _ExtremeWirelessIntfSpeedErrorRX5p5_Type()
)
extremeWirelessIntfSpeedErrorRX5p5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedErrorRX5p5.setStatus("current")
_ExtremeWirelessIntfSpeedErrorRX6_Type = Unsigned32
_ExtremeWirelessIntfSpeedErrorRX6_Object = MibTableColumn
extremeWirelessIntfSpeedErrorRX6 = _ExtremeWirelessIntfSpeedErrorRX6_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 28),
    _ExtremeWirelessIntfSpeedErrorRX6_Type()
)
extremeWirelessIntfSpeedErrorRX6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedErrorRX6.setStatus("current")
_ExtremeWirelessIntfSpeedErrorRX9_Type = Unsigned32
_ExtremeWirelessIntfSpeedErrorRX9_Object = MibTableColumn
extremeWirelessIntfSpeedErrorRX9 = _ExtremeWirelessIntfSpeedErrorRX9_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 29),
    _ExtremeWirelessIntfSpeedErrorRX9_Type()
)
extremeWirelessIntfSpeedErrorRX9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedErrorRX9.setStatus("current")
_ExtremeWirelessIntfSpeedErrorRX11_Type = Unsigned32
_ExtremeWirelessIntfSpeedErrorRX11_Object = MibTableColumn
extremeWirelessIntfSpeedErrorRX11 = _ExtremeWirelessIntfSpeedErrorRX11_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 30),
    _ExtremeWirelessIntfSpeedErrorRX11_Type()
)
extremeWirelessIntfSpeedErrorRX11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedErrorRX11.setStatus("current")
_ExtremeWirelessIntfSpeedErrorRX12_Type = Unsigned32
_ExtremeWirelessIntfSpeedErrorRX12_Object = MibTableColumn
extremeWirelessIntfSpeedErrorRX12 = _ExtremeWirelessIntfSpeedErrorRX12_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 31),
    _ExtremeWirelessIntfSpeedErrorRX12_Type()
)
extremeWirelessIntfSpeedErrorRX12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedErrorRX12.setStatus("current")
_ExtremeWirelessIntfSpeedErrorRX18_Type = Unsigned32
_ExtremeWirelessIntfSpeedErrorRX18_Object = MibTableColumn
extremeWirelessIntfSpeedErrorRX18 = _ExtremeWirelessIntfSpeedErrorRX18_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 32),
    _ExtremeWirelessIntfSpeedErrorRX18_Type()
)
extremeWirelessIntfSpeedErrorRX18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedErrorRX18.setStatus("current")
_ExtremeWirelessIntfSpeedErrorRX24_Type = Unsigned32
_ExtremeWirelessIntfSpeedErrorRX24_Object = MibTableColumn
extremeWirelessIntfSpeedErrorRX24 = _ExtremeWirelessIntfSpeedErrorRX24_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 33),
    _ExtremeWirelessIntfSpeedErrorRX24_Type()
)
extremeWirelessIntfSpeedErrorRX24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedErrorRX24.setStatus("current")
_ExtremeWirelessIntfSpeedErrorRX36_Type = Unsigned32
_ExtremeWirelessIntfSpeedErrorRX36_Object = MibTableColumn
extremeWirelessIntfSpeedErrorRX36 = _ExtremeWirelessIntfSpeedErrorRX36_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 34),
    _ExtremeWirelessIntfSpeedErrorRX36_Type()
)
extremeWirelessIntfSpeedErrorRX36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedErrorRX36.setStatus("current")
_ExtremeWirelessIntfSpeedErrorRX48_Type = Unsigned32
_ExtremeWirelessIntfSpeedErrorRX48_Object = MibTableColumn
extremeWirelessIntfSpeedErrorRX48 = _ExtremeWirelessIntfSpeedErrorRX48_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 35),
    _ExtremeWirelessIntfSpeedErrorRX48_Type()
)
extremeWirelessIntfSpeedErrorRX48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedErrorRX48.setStatus("current")
_ExtremeWirelessIntfSpeedErrorRX54_Type = Unsigned32
_ExtremeWirelessIntfSpeedErrorRX54_Object = MibTableColumn
extremeWirelessIntfSpeedErrorRX54 = _ExtremeWirelessIntfSpeedErrorRX54_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 42, 1, 36),
    _ExtremeWirelessIntfSpeedErrorRX54_Type()
)
extremeWirelessIntfSpeedErrorRX54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfSpeedErrorRX54.setStatus("current")
_ExtremeWirelessIntfUtilizationTable_Object = MibTable
extremeWirelessIntfUtilizationTable = _ExtremeWirelessIntfUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 43)
)
if mibBuilder.loadTexts:
    extremeWirelessIntfUtilizationTable.setStatus("current")
_ExtremeWirelessIntfUtilizationEntry_Object = MibTableRow
extremeWirelessIntfUtilizationEntry = _ExtremeWirelessIntfUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 43, 1)
)
extremeWirelessIntfUtilizationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessIntfUtilizationEntry.setStatus("current")
_ExtremeWirelessIntfUtilizationNav_Type = Unsigned32
_ExtremeWirelessIntfUtilizationNav_Object = MibTableColumn
extremeWirelessIntfUtilizationNav = _ExtremeWirelessIntfUtilizationNav_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 43, 1, 1),
    _ExtremeWirelessIntfUtilizationNav_Type()
)
extremeWirelessIntfUtilizationNav.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfUtilizationNav.setStatus("current")
_ExtremeWirelessIntfUtilizationNoiseFloor_Type = Unsigned32
_ExtremeWirelessIntfUtilizationNoiseFloor_Object = MibTableColumn
extremeWirelessIntfUtilizationNoiseFloor = _ExtremeWirelessIntfUtilizationNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 43, 1, 2),
    _ExtremeWirelessIntfUtilizationNoiseFloor_Type()
)
extremeWirelessIntfUtilizationNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessIntfUtilizationNoiseFloor.setStatus("current")


class _ExtremeWirelessCounterMeasureSource_Type(Integer32):
    """Custom type extremeWirelessCounterMeasureSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clientReport", 1),
          ("micFailure", 2))
    )


_ExtremeWirelessCounterMeasureSource_Type.__name__ = "Integer32"
_ExtremeWirelessCounterMeasureSource_Object = MibScalar
extremeWirelessCounterMeasureSource = _ExtremeWirelessCounterMeasureSource_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 44),
    _ExtremeWirelessCounterMeasureSource_Type()
)
extremeWirelessCounterMeasureSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeWirelessCounterMeasureSource.setStatus("current")
_ExtremeWirelessClientWPAStatsTable_Object = MibTable
extremeWirelessClientWPAStatsTable = _ExtremeWirelessClientWPAStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 47)
)
if mibBuilder.loadTexts:
    extremeWirelessClientWPAStatsTable.setStatus("current")
_ExtremeWirelessClientWPAStatsEntry_Object = MibTableRow
extremeWirelessClientWPAStatsEntry = _ExtremeWirelessClientWPAStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 47, 1)
)
extremeWirelessClientWPAStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessClientDiagMac"),
)
if mibBuilder.loadTexts:
    extremeWirelessClientWPAStatsEntry.setStatus("current")
_ExtremeWirelessClientWPAStatsStarts_Type = Counter32
_ExtremeWirelessClientWPAStatsStarts_Object = MibTableColumn
extremeWirelessClientWPAStatsStarts = _ExtremeWirelessClientWPAStatsStarts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 47, 1, 1),
    _ExtremeWirelessClientWPAStatsStarts_Type()
)
extremeWirelessClientWPAStatsStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientWPAStatsStarts.setStatus("current")
_ExtremeWirelessClientWPAStatsPairwiseKeySuccesses_Type = Counter32
_ExtremeWirelessClientWPAStatsPairwiseKeySuccesses_Object = MibTableColumn
extremeWirelessClientWPAStatsPairwiseKeySuccesses = _ExtremeWirelessClientWPAStatsPairwiseKeySuccesses_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 47, 1, 2),
    _ExtremeWirelessClientWPAStatsPairwiseKeySuccesses_Type()
)
extremeWirelessClientWPAStatsPairwiseKeySuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientWPAStatsPairwiseKeySuccesses.setStatus("current")
_ExtremeWirelessClientWPAStatsPairwiseKeyFailures_Type = Counter32
_ExtremeWirelessClientWPAStatsPairwiseKeyFailures_Object = MibTableColumn
extremeWirelessClientWPAStatsPairwiseKeyFailures = _ExtremeWirelessClientWPAStatsPairwiseKeyFailures_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 47, 1, 3),
    _ExtremeWirelessClientWPAStatsPairwiseKeyFailures_Type()
)
extremeWirelessClientWPAStatsPairwiseKeyFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientWPAStatsPairwiseKeyFailures.setStatus("current")
_ExtremeWirelessClientWPAStatsGroupKeySuccesses_Type = Counter32
_ExtremeWirelessClientWPAStatsGroupKeySuccesses_Object = MibTableColumn
extremeWirelessClientWPAStatsGroupKeySuccesses = _ExtremeWirelessClientWPAStatsGroupKeySuccesses_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 47, 1, 4),
    _ExtremeWirelessClientWPAStatsGroupKeySuccesses_Type()
)
extremeWirelessClientWPAStatsGroupKeySuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientWPAStatsGroupKeySuccesses.setStatus("current")
_ExtremeWirelessClientWPAStatsGroupKeyFailures_Type = Counter32
_ExtremeWirelessClientWPAStatsGroupKeyFailures_Object = MibTableColumn
extremeWirelessClientWPAStatsGroupKeyFailures = _ExtremeWirelessClientWPAStatsGroupKeyFailures_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 47, 1, 5),
    _ExtremeWirelessClientWPAStatsGroupKeyFailures_Type()
)
extremeWirelessClientWPAStatsGroupKeyFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientWPAStatsGroupKeyFailures.setStatus("current")
_ExtremeWirelessClientWPAStatsPairwiseKey1Sends_Type = Counter32
_ExtremeWirelessClientWPAStatsPairwiseKey1Sends_Object = MibTableColumn
extremeWirelessClientWPAStatsPairwiseKey1Sends = _ExtremeWirelessClientWPAStatsPairwiseKey1Sends_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 47, 1, 6),
    _ExtremeWirelessClientWPAStatsPairwiseKey1Sends_Type()
)
extremeWirelessClientWPAStatsPairwiseKey1Sends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientWPAStatsPairwiseKey1Sends.setStatus("current")
_ExtremeWirelessClientWPAStatsPairwiseKey3Sends_Type = Counter32
_ExtremeWirelessClientWPAStatsPairwiseKey3Sends_Object = MibTableColumn
extremeWirelessClientWPAStatsPairwiseKey3Sends = _ExtremeWirelessClientWPAStatsPairwiseKey3Sends_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 47, 1, 7),
    _ExtremeWirelessClientWPAStatsPairwiseKey3Sends_Type()
)
extremeWirelessClientWPAStatsPairwiseKey3Sends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientWPAStatsPairwiseKey3Sends.setStatus("current")
_ExtremeWirelessClientWPAStatsGroupKeySends_Type = Counter32
_ExtremeWirelessClientWPAStatsGroupKeySends_Object = MibTableColumn
extremeWirelessClientWPAStatsGroupKeySends = _ExtremeWirelessClientWPAStatsGroupKeySends_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 47, 1, 8),
    _ExtremeWirelessClientWPAStatsGroupKeySends_Type()
)
extremeWirelessClientWPAStatsGroupKeySends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientWPAStatsGroupKeySends.setStatus("current")
_ExtremeWirelessClientWPAStatsEAPOLKeyReceivedInPairwise1Key_Type = Counter32
_ExtremeWirelessClientWPAStatsEAPOLKeyReceivedInPairwise1Key_Object = MibTableColumn
extremeWirelessClientWPAStatsEAPOLKeyReceivedInPairwise1Key = _ExtremeWirelessClientWPAStatsEAPOLKeyReceivedInPairwise1Key_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 47, 1, 9),
    _ExtremeWirelessClientWPAStatsEAPOLKeyReceivedInPairwise1Key_Type()
)
extremeWirelessClientWPAStatsEAPOLKeyReceivedInPairwise1Key.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientWPAStatsEAPOLKeyReceivedInPairwise1Key.setStatus("current")
_ExtremeWirelessClientWPAStatsEAPOLKeyReceivedInPairwise3Key_Type = Counter32
_ExtremeWirelessClientWPAStatsEAPOLKeyReceivedInPairwise3Key_Object = MibTableColumn
extremeWirelessClientWPAStatsEAPOLKeyReceivedInPairwise3Key = _ExtremeWirelessClientWPAStatsEAPOLKeyReceivedInPairwise3Key_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 47, 1, 10),
    _ExtremeWirelessClientWPAStatsEAPOLKeyReceivedInPairwise3Key_Type()
)
extremeWirelessClientWPAStatsEAPOLKeyReceivedInPairwise3Key.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientWPAStatsEAPOLKeyReceivedInPairwise3Key.setStatus("current")
_ExtremeWirelessClientWPAStatsEAPOLKeyReceivedInGroupKey_Type = Counter32
_ExtremeWirelessClientWPAStatsEAPOLKeyReceivedInGroupKey_Object = MibTableColumn
extremeWirelessClientWPAStatsEAPOLKeyReceivedInGroupKey = _ExtremeWirelessClientWPAStatsEAPOLKeyReceivedInGroupKey_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 47, 1, 11),
    _ExtremeWirelessClientWPAStatsEAPOLKeyReceivedInGroupKey_Type()
)
extremeWirelessClientWPAStatsEAPOLKeyReceivedInGroupKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientWPAStatsEAPOLKeyReceivedInGroupKey.setStatus("current")
_ExtremeWirelessClientWPAStatsDoubleEAPOLKeyReceived_Type = Counter32
_ExtremeWirelessClientWPAStatsDoubleEAPOLKeyReceived_Object = MibTableColumn
extremeWirelessClientWPAStatsDoubleEAPOLKeyReceived = _ExtremeWirelessClientWPAStatsDoubleEAPOLKeyReceived_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 47, 1, 12),
    _ExtremeWirelessClientWPAStatsDoubleEAPOLKeyReceived_Type()
)
extremeWirelessClientWPAStatsDoubleEAPOLKeyReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientWPAStatsDoubleEAPOLKeyReceived.setStatus("current")
_ExtremeWirelessClientWPAStatsEAPOLKeyIgnores_Type = Counter32
_ExtremeWirelessClientWPAStatsEAPOLKeyIgnores_Object = MibTableColumn
extremeWirelessClientWPAStatsEAPOLKeyIgnores = _ExtremeWirelessClientWPAStatsEAPOLKeyIgnores_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 47, 1, 13),
    _ExtremeWirelessClientWPAStatsEAPOLKeyIgnores_Type()
)
extremeWirelessClientWPAStatsEAPOLKeyIgnores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientWPAStatsEAPOLKeyIgnores.setStatus("current")
_ExtremeWirelessClientWPAStatsEAPOLKeyErrors_Type = Counter32
_ExtremeWirelessClientWPAStatsEAPOLKeyErrors_Object = MibTableColumn
extremeWirelessClientWPAStatsEAPOLKeyErrors = _ExtremeWirelessClientWPAStatsEAPOLKeyErrors_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 47, 1, 14),
    _ExtremeWirelessClientWPAStatsEAPOLKeyErrors_Type()
)
extremeWirelessClientWPAStatsEAPOLKeyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientWPAStatsEAPOLKeyErrors.setStatus("current")
_ExtremeWirelessClientWPAStatsEAPOLKeyAborts_Type = Counter32
_ExtremeWirelessClientWPAStatsEAPOLKeyAborts_Object = MibTableColumn
extremeWirelessClientWPAStatsEAPOLKeyAborts = _ExtremeWirelessClientWPAStatsEAPOLKeyAborts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 47, 1, 15),
    _ExtremeWirelessClientWPAStatsEAPOLKeyAborts_Type()
)
extremeWirelessClientWPAStatsEAPOLKeyAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientWPAStatsEAPOLKeyAborts.setStatus("current")
_ExtremeWirelessClientWPAStatsEAPOLKeyVerificationSuccesses_Type = Counter32
_ExtremeWirelessClientWPAStatsEAPOLKeyVerificationSuccesses_Object = MibTableColumn
extremeWirelessClientWPAStatsEAPOLKeyVerificationSuccesses = _ExtremeWirelessClientWPAStatsEAPOLKeyVerificationSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 47, 1, 16),
    _ExtremeWirelessClientWPAStatsEAPOLKeyVerificationSuccesses_Type()
)
extremeWirelessClientWPAStatsEAPOLKeyVerificationSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientWPAStatsEAPOLKeyVerificationSuccesses.setStatus("current")
_ExtremeWirelessOpaqueTable_Object = MibTable
extremeWirelessOpaqueTable = _ExtremeWirelessOpaqueTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 99)
)
if mibBuilder.loadTexts:
    extremeWirelessOpaqueTable.setStatus("current")
_ExtremeWirelessOpaqueEntry_Object = MibTableRow
extremeWirelessOpaqueEntry = _ExtremeWirelessOpaqueEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 99, 1)
)
extremeWirelessOpaqueEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessOpaqueEntry.setStatus("current")
_ExtremeWirelessClientData_Type = OctetString
_ExtremeWirelessClientData_Object = MibTableColumn
extremeWirelessClientData = _ExtremeWirelessClientData_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 99, 1, 1),
    _ExtremeWirelessClientData_Type()
)
extremeWirelessClientData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientData.setStatus("current")
_ExtremeWirelessPAEStatsData_Type = OctetString
_ExtremeWirelessPAEStatsData_Object = MibTableColumn
extremeWirelessPAEStatsData = _ExtremeWirelessPAEStatsData_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 99, 1, 2),
    _ExtremeWirelessPAEStatsData_Type()
)
extremeWirelessPAEStatsData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessPAEStatsData.setStatus("current")
_ExtremeWirelessPAEDiagData_Type = OctetString
_ExtremeWirelessPAEDiagData_Object = MibTableColumn
extremeWirelessPAEDiagData = _ExtremeWirelessPAEDiagData_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 99, 1, 3),
    _ExtremeWirelessPAEDiagData_Type()
)
extremeWirelessPAEDiagData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessPAEDiagData.setStatus("current")
_ExtremeWirelessScanResultsData_Type = OctetString
_ExtremeWirelessScanResultsData_Object = MibTableColumn
extremeWirelessScanResultsData = _ExtremeWirelessScanResultsData_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 99, 1, 4),
    _ExtremeWirelessScanResultsData_Type()
)
extremeWirelessScanResultsData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessScanResultsData.setStatus("current")
_ExtremeWirelessProbeInfoData_Type = OctetString
_ExtremeWirelessProbeInfoData_Object = MibTableColumn
extremeWirelessProbeInfoData = _ExtremeWirelessProbeInfoData_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 99, 1, 5),
    _ExtremeWirelessProbeInfoData_Type()
)
extremeWirelessProbeInfoData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoData.setStatus("current")
_ExtremeWirelessClientDiagData_Type = OctetString
_ExtremeWirelessClientDiagData_Object = MibTableColumn
extremeWirelessClientDiagData = _ExtremeWirelessClientDiagData_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 99, 1, 6),
    _ExtremeWirelessClientDiagData_Type()
)
extremeWirelessClientDiagData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientDiagData.setStatus("current")
_ExtremeWirelessClientAssocData_Type = OctetString
_ExtremeWirelessClientAssocData_Object = MibTableColumn
extremeWirelessClientAssocData = _ExtremeWirelessClientAssocData_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 99, 1, 7),
    _ExtremeWirelessClientAssocData_Type()
)
extremeWirelessClientAssocData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAssocData.setStatus("current")
_ExtremeWirelessClientAuthData_Type = OctetString
_ExtremeWirelessClientAuthData_Object = MibTableColumn
extremeWirelessClientAuthData = _ExtremeWirelessClientAuthData_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 99, 1, 8),
    _ExtremeWirelessClientAuthData_Type()
)
extremeWirelessClientAuthData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientAuthData.setStatus("current")
_ExtremeWirelessClientMACInfoData_Type = OctetString
_ExtremeWirelessClientMACInfoData_Object = MibTableColumn
extremeWirelessClientMACInfoData = _ExtremeWirelessClientMACInfoData_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 99, 1, 9),
    _ExtremeWirelessClientMACInfoData_Type()
)
extremeWirelessClientMACInfoData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessClientMACInfoData.setStatus("current")
_ExtremeWirelessSizeCounterData_Type = OctetString
_ExtremeWirelessSizeCounterData_Object = MibTableColumn
extremeWirelessSizeCounterData = _ExtremeWirelessSizeCounterData_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 99, 1, 10),
    _ExtremeWirelessSizeCounterData_Type()
)
extremeWirelessSizeCounterData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessSizeCounterData.setStatus("current")
_ExtremeWirelessSpeedCounterData_Type = OctetString
_ExtremeWirelessSpeedCounterData_Object = MibTableColumn
extremeWirelessSpeedCounterData = _ExtremeWirelessSpeedCounterData_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 99, 1, 11),
    _ExtremeWirelessSpeedCounterData_Type()
)
extremeWirelessSpeedCounterData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessSpeedCounterData.setStatus("current")
_ExtremeWirelessTraceTable_Object = MibTable
extremeWirelessTraceTable = _ExtremeWirelessTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 100)
)
if mibBuilder.loadTexts:
    extremeWirelessTraceTable.setStatus("current")
_ExtremeWirelessTraceEntry_Object = MibTableRow
extremeWirelessTraceEntry = _ExtremeWirelessTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 100, 1)
)
extremeWirelessTraceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessTraceEntry.setStatus("current")
_ExtremeWirelessTraceMsgsOut_Type = Integer32
_ExtremeWirelessTraceMsgsOut_Object = MibTableColumn
extremeWirelessTraceMsgsOut = _ExtremeWirelessTraceMsgsOut_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 100, 1, 1),
    _ExtremeWirelessTraceMsgsOut_Type()
)
extremeWirelessTraceMsgsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessTraceMsgsOut.setStatus("current")
_ExtremeWirelessTraceBytesOut_Type = Integer32
_ExtremeWirelessTraceBytesOut_Object = MibTableColumn
extremeWirelessTraceBytesOut = _ExtremeWirelessTraceBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 100, 1, 2),
    _ExtremeWirelessTraceBytesOut_Type()
)
extremeWirelessTraceBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessTraceBytesOut.setStatus("current")
_ExtremeWirelessTraceSuppressed_Type = Integer32
_ExtremeWirelessTraceSuppressed_Object = MibTableColumn
extremeWirelessTraceSuppressed = _ExtremeWirelessTraceSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 100, 1, 3),
    _ExtremeWirelessTraceSuppressed_Type()
)
extremeWirelessTraceSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessTraceSuppressed.setStatus("current")
_ExtremeWirelessTraceOtherErr_Type = Integer32
_ExtremeWirelessTraceOtherErr_Object = MibTableColumn
extremeWirelessTraceOtherErr = _ExtremeWirelessTraceOtherErr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 100, 1, 4),
    _ExtremeWirelessTraceOtherErr_Type()
)
extremeWirelessTraceOtherErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessTraceOtherErr.setStatus("current")
_ExtremeWirelessTraceOpaque_Type = OctetString
_ExtremeWirelessTraceOpaque_Object = MibTableColumn
extremeWirelessTraceOpaque = _ExtremeWirelessTraceOpaque_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 100, 1, 5),
    _ExtremeWirelessTraceOpaque_Type()
)
extremeWirelessTraceOpaque.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessTraceOpaque.setStatus("current")
_ExtremeWirelessTraceModuleTable_Object = MibTable
extremeWirelessTraceModuleTable = _ExtremeWirelessTraceModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 101)
)
if mibBuilder.loadTexts:
    extremeWirelessTraceModuleTable.setStatus("current")
_ExtremeWirelessTraceModuleEntry_Object = MibTableRow
extremeWirelessTraceModuleEntry = _ExtremeWirelessTraceModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 101, 1)
)
extremeWirelessTraceModuleEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessTraceModuleId"),
)
if mibBuilder.loadTexts:
    extremeWirelessTraceModuleEntry.setStatus("current")


class _ExtremeWirelessTraceModuleId_Type(Integer32):
    """Custom type extremeWirelessTraceModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeWirelessTraceModuleId_Type.__name__ = "Integer32"
_ExtremeWirelessTraceModuleId_Object = MibTableColumn
extremeWirelessTraceModuleId = _ExtremeWirelessTraceModuleId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 101, 1, 1),
    _ExtremeWirelessTraceModuleId_Type()
)
extremeWirelessTraceModuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeWirelessTraceModuleId.setStatus("current")
_ExtremeWirelessTraceModuleDesc_Type = DisplayString
_ExtremeWirelessTraceModuleDesc_Object = MibTableColumn
extremeWirelessTraceModuleDesc = _ExtremeWirelessTraceModuleDesc_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 101, 1, 2),
    _ExtremeWirelessTraceModuleDesc_Type()
)
extremeWirelessTraceModuleDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessTraceModuleDesc.setStatus("current")
_ExtremeWirelessTraceModuleHeader_Type = DisplayString
_ExtremeWirelessTraceModuleHeader_Object = MibTableColumn
extremeWirelessTraceModuleHeader = _ExtremeWirelessTraceModuleHeader_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 101, 1, 3),
    _ExtremeWirelessTraceModuleHeader_Type()
)
extremeWirelessTraceModuleHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessTraceModuleHeader.setStatus("current")


class _ExtremeWirelessTraceModuleLevel_Type(Integer32):
    """Custom type extremeWirelessTraceModuleLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_ExtremeWirelessTraceModuleLevel_Type.__name__ = "Integer32"
_ExtremeWirelessTraceModuleLevel_Object = MibTableColumn
extremeWirelessTraceModuleLevel = _ExtremeWirelessTraceModuleLevel_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 101, 1, 4),
    _ExtremeWirelessTraceModuleLevel_Type()
)
extremeWirelessTraceModuleLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessTraceModuleLevel.setStatus("current")
_ExtremeWirelessTraceModuleSuppressed_Type = Integer32
_ExtremeWirelessTraceModuleSuppressed_Object = MibTableColumn
extremeWirelessTraceModuleSuppressed = _ExtremeWirelessTraceModuleSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 101, 1, 5),
    _ExtremeWirelessTraceModuleSuppressed_Type()
)
extremeWirelessTraceModuleSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessTraceModuleSuppressed.setStatus("current")
_ExtremeWirelessTraceModuleMsgsOut_Type = Integer32
_ExtremeWirelessTraceModuleMsgsOut_Object = MibTableColumn
extremeWirelessTraceModuleMsgsOut = _ExtremeWirelessTraceModuleMsgsOut_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 101, 1, 6),
    _ExtremeWirelessTraceModuleMsgsOut_Type()
)
extremeWirelessTraceModuleMsgsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessTraceModuleMsgsOut.setStatus("current")
_ExtremeWirelessTraceModuleBytesOut_Type = Integer32
_ExtremeWirelessTraceModuleBytesOut_Object = MibTableColumn
extremeWirelessTraceModuleBytesOut = _ExtremeWirelessTraceModuleBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 101, 1, 7),
    _ExtremeWirelessTraceModuleBytesOut_Type()
)
extremeWirelessTraceModuleBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessTraceModuleBytesOut.setStatus("current")
_ExtremeWirelessLogDiagTable_Object = MibTable
extremeWirelessLogDiagTable = _ExtremeWirelessLogDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 102)
)
if mibBuilder.loadTexts:
    extremeWirelessLogDiagTable.setStatus("current")
_ExtremeWirelessLogDiagEntry_Object = MibTableRow
extremeWirelessLogDiagEntry = _ExtremeWirelessLogDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 102, 1)
)
extremeWirelessLogDiagEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessLogDiagEntry.setStatus("current")
_ExtremeWirelessLogDiagEventLogTotalCount_Type = Unsigned32
_ExtremeWirelessLogDiagEventLogTotalCount_Object = MibTableColumn
extremeWirelessLogDiagEventLogTotalCount = _ExtremeWirelessLogDiagEventLogTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 102, 1, 1),
    _ExtremeWirelessLogDiagEventLogTotalCount_Type()
)
extremeWirelessLogDiagEventLogTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessLogDiagEventLogTotalCount.setStatus("current")
_ExtremeWirelessLogDiagEventLogTotalEmergCount_Type = Unsigned32
_ExtremeWirelessLogDiagEventLogTotalEmergCount_Object = MibTableColumn
extremeWirelessLogDiagEventLogTotalEmergCount = _ExtremeWirelessLogDiagEventLogTotalEmergCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 102, 1, 2),
    _ExtremeWirelessLogDiagEventLogTotalEmergCount_Type()
)
extremeWirelessLogDiagEventLogTotalEmergCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessLogDiagEventLogTotalEmergCount.setStatus("current")
_ExtremeWirelessLogDiagEventLogTotalAlertCount_Type = Unsigned32
_ExtremeWirelessLogDiagEventLogTotalAlertCount_Object = MibTableColumn
extremeWirelessLogDiagEventLogTotalAlertCount = _ExtremeWirelessLogDiagEventLogTotalAlertCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 102, 1, 3),
    _ExtremeWirelessLogDiagEventLogTotalAlertCount_Type()
)
extremeWirelessLogDiagEventLogTotalAlertCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessLogDiagEventLogTotalAlertCount.setStatus("current")
_ExtremeWirelessLogDiagEventLogTotalCritCount_Type = Unsigned32
_ExtremeWirelessLogDiagEventLogTotalCritCount_Object = MibTableColumn
extremeWirelessLogDiagEventLogTotalCritCount = _ExtremeWirelessLogDiagEventLogTotalCritCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 102, 1, 4),
    _ExtremeWirelessLogDiagEventLogTotalCritCount_Type()
)
extremeWirelessLogDiagEventLogTotalCritCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessLogDiagEventLogTotalCritCount.setStatus("current")
_ExtremeWirelessLogDiagEventLogTotalErrorCount_Type = Unsigned32
_ExtremeWirelessLogDiagEventLogTotalErrorCount_Object = MibTableColumn
extremeWirelessLogDiagEventLogTotalErrorCount = _ExtremeWirelessLogDiagEventLogTotalErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 102, 1, 5),
    _ExtremeWirelessLogDiagEventLogTotalErrorCount_Type()
)
extremeWirelessLogDiagEventLogTotalErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessLogDiagEventLogTotalErrorCount.setStatus("current")
_ExtremeWirelessLogDiagEventLogTotalWarnCount_Type = Unsigned32
_ExtremeWirelessLogDiagEventLogTotalWarnCount_Object = MibTableColumn
extremeWirelessLogDiagEventLogTotalWarnCount = _ExtremeWirelessLogDiagEventLogTotalWarnCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 102, 1, 6),
    _ExtremeWirelessLogDiagEventLogTotalWarnCount_Type()
)
extremeWirelessLogDiagEventLogTotalWarnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessLogDiagEventLogTotalWarnCount.setStatus("current")
_ExtremeWirelessLogDiagEventLogTotalNoticeCount_Type = Unsigned32
_ExtremeWirelessLogDiagEventLogTotalNoticeCount_Object = MibTableColumn
extremeWirelessLogDiagEventLogTotalNoticeCount = _ExtremeWirelessLogDiagEventLogTotalNoticeCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 102, 1, 7),
    _ExtremeWirelessLogDiagEventLogTotalNoticeCount_Type()
)
extremeWirelessLogDiagEventLogTotalNoticeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessLogDiagEventLogTotalNoticeCount.setStatus("current")
_ExtremeWirelessLogDiagEventLogTotalInfoCount_Type = Unsigned32
_ExtremeWirelessLogDiagEventLogTotalInfoCount_Object = MibTableColumn
extremeWirelessLogDiagEventLogTotalInfoCount = _ExtremeWirelessLogDiagEventLogTotalInfoCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 102, 1, 8),
    _ExtremeWirelessLogDiagEventLogTotalInfoCount_Type()
)
extremeWirelessLogDiagEventLogTotalInfoCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessLogDiagEventLogTotalInfoCount.setStatus("current")
_ExtremeWirelessLogDiagEventLogTotalDebugCount_Type = Unsigned32
_ExtremeWirelessLogDiagEventLogTotalDebugCount_Object = MibTableColumn
extremeWirelessLogDiagEventLogTotalDebugCount = _ExtremeWirelessLogDiagEventLogTotalDebugCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 102, 1, 9),
    _ExtremeWirelessLogDiagEventLogTotalDebugCount_Type()
)
extremeWirelessLogDiagEventLogTotalDebugCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessLogDiagEventLogTotalDebugCount.setStatus("current")
_ExtremeWirelessLogDiagEventLogTotalSuppressedCount_Type = Unsigned32
_ExtremeWirelessLogDiagEventLogTotalSuppressedCount_Object = MibTableColumn
extremeWirelessLogDiagEventLogTotalSuppressedCount = _ExtremeWirelessLogDiagEventLogTotalSuppressedCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 102, 1, 10),
    _ExtremeWirelessLogDiagEventLogTotalSuppressedCount_Type()
)
extremeWirelessLogDiagEventLogTotalSuppressedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessLogDiagEventLogTotalSuppressedCount.setStatus("current")
_ExtremeWirelessLogDiagEventLogTotalByteCount_Type = Unsigned32
_ExtremeWirelessLogDiagEventLogTotalByteCount_Object = MibTableColumn
extremeWirelessLogDiagEventLogTotalByteCount = _ExtremeWirelessLogDiagEventLogTotalByteCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 102, 1, 11),
    _ExtremeWirelessLogDiagEventLogTotalByteCount_Type()
)
extremeWirelessLogDiagEventLogTotalByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessLogDiagEventLogTotalByteCount.setStatus("current")
_ExtremeWirelessLogDiagSyslogTotalEventCount_Type = Unsigned32
_ExtremeWirelessLogDiagSyslogTotalEventCount_Object = MibTableColumn
extremeWirelessLogDiagSyslogTotalEventCount = _ExtremeWirelessLogDiagSyslogTotalEventCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 102, 1, 12),
    _ExtremeWirelessLogDiagSyslogTotalEventCount_Type()
)
extremeWirelessLogDiagSyslogTotalEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessLogDiagSyslogTotalEventCount.setStatus("current")
_ExtremeWirelessLogDiagSyslogTotalSuppressedCount_Type = Unsigned32
_ExtremeWirelessLogDiagSyslogTotalSuppressedCount_Object = MibTableColumn
extremeWirelessLogDiagSyslogTotalSuppressedCount = _ExtremeWirelessLogDiagSyslogTotalSuppressedCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 102, 1, 13),
    _ExtremeWirelessLogDiagSyslogTotalSuppressedCount_Type()
)
extremeWirelessLogDiagSyslogTotalSuppressedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessLogDiagSyslogTotalSuppressedCount.setStatus("current")
_ExtremeWirelessLogDiagSyslogTotalByteCount_Type = Unsigned32
_ExtremeWirelessLogDiagSyslogTotalByteCount_Object = MibTableColumn
extremeWirelessLogDiagSyslogTotalByteCount = _ExtremeWirelessLogDiagSyslogTotalByteCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 102, 1, 14),
    _ExtremeWirelessLogDiagSyslogTotalByteCount_Type()
)
extremeWirelessLogDiagSyslogTotalByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessLogDiagSyslogTotalByteCount.setStatus("current")
_ExtremeWirelessLogDiagNVRAMTotalEventCount_Type = Unsigned32
_ExtremeWirelessLogDiagNVRAMTotalEventCount_Object = MibTableColumn
extremeWirelessLogDiagNVRAMTotalEventCount = _ExtremeWirelessLogDiagNVRAMTotalEventCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 102, 1, 15),
    _ExtremeWirelessLogDiagNVRAMTotalEventCount_Type()
)
extremeWirelessLogDiagNVRAMTotalEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessLogDiagNVRAMTotalEventCount.setStatus("current")
_ExtremeWirelessLogDiagNVRAMTotalSuppressedCount_Type = Unsigned32
_ExtremeWirelessLogDiagNVRAMTotalSuppressedCount_Object = MibTableColumn
extremeWirelessLogDiagNVRAMTotalSuppressedCount = _ExtremeWirelessLogDiagNVRAMTotalSuppressedCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 102, 1, 16),
    _ExtremeWirelessLogDiagNVRAMTotalSuppressedCount_Type()
)
extremeWirelessLogDiagNVRAMTotalSuppressedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessLogDiagNVRAMTotalSuppressedCount.setStatus("current")
_ExtremeWirelessLogDiagNVRAMTotalDroppedCount_Type = Unsigned32
_ExtremeWirelessLogDiagNVRAMTotalDroppedCount_Object = MibTableColumn
extremeWirelessLogDiagNVRAMTotalDroppedCount = _ExtremeWirelessLogDiagNVRAMTotalDroppedCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 102, 1, 17),
    _ExtremeWirelessLogDiagNVRAMTotalDroppedCount_Type()
)
extremeWirelessLogDiagNVRAMTotalDroppedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessLogDiagNVRAMTotalDroppedCount.setStatus("current")
_ExtremeWirelessLogDiagNVRAMTotalByteCount_Type = Unsigned32
_ExtremeWirelessLogDiagNVRAMTotalByteCount_Object = MibTableColumn
extremeWirelessLogDiagNVRAMTotalByteCount = _ExtremeWirelessLogDiagNVRAMTotalByteCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 102, 1, 18),
    _ExtremeWirelessLogDiagNVRAMTotalByteCount_Type()
)
extremeWirelessLogDiagNVRAMTotalByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessLogDiagNVRAMTotalByteCount.setStatus("current")
_ExtremeWirelessLogDiagClearStats_Type = TruthValue
_ExtremeWirelessLogDiagClearStats_Object = MibTableColumn
extremeWirelessLogDiagClearStats = _ExtremeWirelessLogDiagClearStats_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1, 102, 1, 19),
    _ExtremeWirelessLogDiagClearStats_Type()
)
extremeWirelessLogDiagClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessLogDiagClearStats.setStatus("current")
_ExtremeLACGeneral_ObjectIdentity = ObjectIdentity
extremeLACGeneral = _ExtremeLACGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 1)
)
_ExtremeAPTotalAuthFailures_Type = Integer32
_ExtremeAPTotalAuthFailures_Object = MibScalar
extremeAPTotalAuthFailures = _ExtremeAPTotalAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 1, 1),
    _ExtremeAPTotalAuthFailures_Type()
)
extremeAPTotalAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeAPTotalAuthFailures.setStatus("current")
_ExtremeAPTotalDetectedStations_Type = Integer32
_ExtremeAPTotalDetectedStations_Object = MibScalar
extremeAPTotalDetectedStations = _ExtremeAPTotalDetectedStations_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 1, 2),
    _ExtremeAPTotalDetectedStations_Type()
)
extremeAPTotalDetectedStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeAPTotalDetectedStations.setStatus("current")
_ExtremeAPTotalAssociatedStations_Type = Integer32
_ExtremeAPTotalAssociatedStations_Object = MibScalar
extremeAPTotalAssociatedStations = _ExtremeAPTotalAssociatedStations_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 1, 3),
    _ExtremeAPTotalAssociatedStations_Type()
)
extremeAPTotalAssociatedStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeAPTotalAssociatedStations.setStatus("current")
_ExtremeAPTotalAuthenticatedStations_Type = Integer32
_ExtremeAPTotalAuthenticatedStations_Object = MibScalar
extremeAPTotalAuthenticatedStations = _ExtremeAPTotalAuthenticatedStations_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 1, 4),
    _ExtremeAPTotalAuthenticatedStations_Type()
)
extremeAPTotalAuthenticatedStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeAPTotalAuthenticatedStations.setStatus("current")
_ExtremeWirelessCfgMgmtVLAN_Type = Integer32
_ExtremeWirelessCfgMgmtVLAN_Object = MibScalar
extremeWirelessCfgMgmtVLAN = _ExtremeWirelessCfgMgmtVLAN_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 1, 5),
    _ExtremeWirelessCfgMgmtVLAN_Type()
)
extremeWirelessCfgMgmtVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessCfgMgmtVLAN.setStatus("current")
_ExtremeWirelessCfgNetmask_Type = IpAddress
_ExtremeWirelessCfgNetmask_Object = MibScalar
extremeWirelessCfgNetmask = _ExtremeWirelessCfgNetmask_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 1, 6),
    _ExtremeWirelessCfgNetmask_Type()
)
extremeWirelessCfgNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessCfgNetmask.setStatus("current")
_ExtremeWirelessCfgGateway_Type = IpAddress
_ExtremeWirelessCfgGateway_Object = MibScalar
extremeWirelessCfgGateway = _ExtremeWirelessCfgGateway_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 1, 7),
    _ExtremeWirelessCfgGateway_Type()
)
extremeWirelessCfgGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessCfgGateway.setStatus("current")
_ExtremeWirelessCfgEnableWirelessTraps_Type = TruthValue
_ExtremeWirelessCfgEnableWirelessTraps_Object = MibScalar
extremeWirelessCfgEnableWirelessTraps = _ExtremeWirelessCfgEnableWirelessTraps_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 1, 8),
    _ExtremeWirelessCfgEnableWirelessTraps_Type()
)
extremeWirelessCfgEnableWirelessTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessCfgEnableWirelessTraps.setStatus("current")
_ExtremeWirelessCfgCountryCode_Type = ExtremeWirelessCountryCode
_ExtremeWirelessCfgCountryCode_Object = MibScalar
extremeWirelessCfgCountryCode = _ExtremeWirelessCfgCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 1, 10),
    _ExtremeWirelessCfgCountryCode_Type()
)
extremeWirelessCfgCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessCfgCountryCode.setStatus("current")
_ExtremeProfile_ObjectIdentity = ObjectIdentity
extremeProfile = _ExtremeProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2)
)
_ExtremeRFProfile_ObjectIdentity = ObjectIdentity
extremeRFProfile = _ExtremeRFProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 1)
)
_ExtremeRFProfileTable_Object = MibTable
extremeRFProfileTable = _ExtremeRFProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    extremeRFProfileTable.setStatus("current")
_ExtremeRFProfileEntry_Object = MibTableRow
extremeRFProfileEntry = _ExtremeRFProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 1, 1, 1)
)
extremeRFProfileEntry.setIndexNames(
    (0, "EXTREME-WIRELESS-MIB", "extremeRFProfileIndex"),
)
if mibBuilder.loadTexts:
    extremeRFProfileEntry.setStatus("current")


class _ExtremeRFProfileIndex_Type(Integer32):
    """Custom type extremeRFProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 34),
    )


_ExtremeRFProfileIndex_Type.__name__ = "Integer32"
_ExtremeRFProfileIndex_Object = MibTableColumn
extremeRFProfileIndex = _ExtremeRFProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 1, 1, 1, 1),
    _ExtremeRFProfileIndex_Type()
)
extremeRFProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeRFProfileIndex.setStatus("current")


class _ExtremeRFProfileName_Type(DisplayString):
    """Custom type extremeRFProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExtremeRFProfileName_Type.__name__ = "DisplayString"
_ExtremeRFProfileName_Object = MibTableColumn
extremeRFProfileName = _ExtremeRFProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 1, 1, 1, 2),
    _ExtremeRFProfileName_Type()
)
extremeRFProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeRFProfileName.setStatus("current")
_ExtremeRFProfileType_Type = Dot11Type
_ExtremeRFProfileType_Object = MibTableColumn
extremeRFProfileType = _ExtremeRFProfileType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 1, 1, 1, 3),
    _ExtremeRFProfileType_Type()
)
extremeRFProfileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeRFProfileType.setStatus("current")


class _ExtremeRFProfileBeaconInterval_Type(Integer32):
    """Custom type extremeRFProfileBeaconInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeRFProfileBeaconInterval_Type.__name__ = "Integer32"
_ExtremeRFProfileBeaconInterval_Object = MibTableColumn
extremeRFProfileBeaconInterval = _ExtremeRFProfileBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 1, 1, 1, 5),
    _ExtremeRFProfileBeaconInterval_Type()
)
extremeRFProfileBeaconInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeRFProfileBeaconInterval.setStatus("current")


class _ExtremeRFProfileDTIM_Type(Integer32):
    """Custom type extremeRFProfileDTIM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ExtremeRFProfileDTIM_Type.__name__ = "Integer32"
_ExtremeRFProfileDTIM_Object = MibTableColumn
extremeRFProfileDTIM = _ExtremeRFProfileDTIM_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 1, 1, 1, 6),
    _ExtremeRFProfileDTIM_Type()
)
extremeRFProfileDTIM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeRFProfileDTIM.setStatus("current")


class _ExtremeRFProfileFragLength_Type(Integer32):
    """Custom type extremeRFProfileFragLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2345),
    )


_ExtremeRFProfileFragLength_Type.__name__ = "Integer32"
_ExtremeRFProfileFragLength_Object = MibTableColumn
extremeRFProfileFragLength = _ExtremeRFProfileFragLength_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 1, 1, 1, 7),
    _ExtremeRFProfileFragLength_Type()
)
extremeRFProfileFragLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeRFProfileFragLength.setStatus("current")


class _ExtremeRFProfileRTSThresh_Type(Integer32):
    """Custom type extremeRFProfileRTSThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2347),
    )


_ExtremeRFProfileRTSThresh_Type.__name__ = "Integer32"
_ExtremeRFProfileRTSThresh_Object = MibTableColumn
extremeRFProfileRTSThresh = _ExtremeRFProfileRTSThresh_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 1, 1, 1, 8),
    _ExtremeRFProfileRTSThresh_Type()
)
extremeRFProfileRTSThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeRFProfileRTSThresh.setStatus("current")


class _ExtremeRFProfilePreamble_Type(Integer32):
    """Custom type extremeRFProfilePreamble based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("long", 1),
          ("short", 0))
    )


_ExtremeRFProfilePreamble_Type.__name__ = "Integer32"
_ExtremeRFProfilePreamble_Object = MibTableColumn
extremeRFProfilePreamble = _ExtremeRFProfilePreamble_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 1, 1, 1, 9),
    _ExtremeRFProfilePreamble_Type()
)
extremeRFProfilePreamble.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeRFProfilePreamble.setStatus("current")


class _ExtremeRFProfileShortRetry_Type(Integer32):
    """Custom type extremeRFProfileShortRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ExtremeRFProfileShortRetry_Type.__name__ = "Integer32"
_ExtremeRFProfileShortRetry_Object = MibTableColumn
extremeRFProfileShortRetry = _ExtremeRFProfileShortRetry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 1, 1, 1, 11),
    _ExtremeRFProfileShortRetry_Type()
)
extremeRFProfileShortRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeRFProfileShortRetry.setStatus("current")


class _ExtremeRFProfileLongRetry_Type(Integer32):
    """Custom type extremeRFProfileLongRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ExtremeRFProfileLongRetry_Type.__name__ = "Integer32"
_ExtremeRFProfileLongRetry_Object = MibTableColumn
extremeRFProfileLongRetry = _ExtremeRFProfileLongRetry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 1, 1, 1, 12),
    _ExtremeRFProfileLongRetry_Type()
)
extremeRFProfileLongRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeRFProfileLongRetry.setStatus("current")
_ExtremeRFProfileStatus_Type = RowStatus
_ExtremeRFProfileStatus_Object = MibTableColumn
extremeRFProfileStatus = _ExtremeRFProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 1, 1, 1, 13),
    _ExtremeRFProfileStatus_Type()
)
extremeRFProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeRFProfileStatus.setStatus("current")
_ExtremeSecurityProfile_ObjectIdentity = ObjectIdentity
extremeSecurityProfile = _ExtremeSecurityProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2)
)
_ExtremeSecurityProfileTable_Object = MibTable
extremeSecurityProfileTable = _ExtremeSecurityProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    extremeSecurityProfileTable.setStatus("current")
_ExtremeSecurityProfileEntry_Object = MibTableRow
extremeSecurityProfileEntry = _ExtremeSecurityProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2, 1, 1)
)
extremeSecurityProfileEntry.setIndexNames(
    (0, "EXTREME-WIRELESS-MIB", "extremeSecurityProfileIndex"),
)
if mibBuilder.loadTexts:
    extremeSecurityProfileEntry.setStatus("current")


class _ExtremeSecurityProfileIndex_Type(Integer32):
    """Custom type extremeSecurityProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ExtremeSecurityProfileIndex_Type.__name__ = "Integer32"
_ExtremeSecurityProfileIndex_Object = MibTableColumn
extremeSecurityProfileIndex = _ExtremeSecurityProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2, 1, 1, 1),
    _ExtremeSecurityProfileIndex_Type()
)
extremeSecurityProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeSecurityProfileIndex.setStatus("current")


class _ExtremeSecurityProfileName_Type(DisplayString):
    """Custom type extremeSecurityProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExtremeSecurityProfileName_Type.__name__ = "DisplayString"
_ExtremeSecurityProfileName_Object = MibTableColumn
extremeSecurityProfileName = _ExtremeSecurityProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2, 1, 1, 2),
    _ExtremeSecurityProfileName_Type()
)
extremeSecurityProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeSecurityProfileName.setStatus("current")


class _ExtremeSecurityProfileESSName_Type(OctetString):
    """Custom type extremeSecurityProfileESSName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExtremeSecurityProfileESSName_Type.__name__ = "OctetString"
_ExtremeSecurityProfileESSName_Object = MibTableColumn
extremeSecurityProfileESSName = _ExtremeSecurityProfileESSName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2, 1, 1, 3),
    _ExtremeSecurityProfileESSName_Type()
)
extremeSecurityProfileESSName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeSecurityProfileESSName.setStatus("current")
_ExtremeSecurityProfileSSIDInBeacon_Type = TruthValue
_ExtremeSecurityProfileSSIDInBeacon_Object = MibTableColumn
extremeSecurityProfileSSIDInBeacon = _ExtremeSecurityProfileSSIDInBeacon_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2, 1, 1, 4),
    _ExtremeSecurityProfileSSIDInBeacon_Type()
)
extremeSecurityProfileSSIDInBeacon.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeSecurityProfileSSIDInBeacon.setStatus("current")
_ExtremeSecurityProfileDot11AuthMode_Type = Dot11AuthMode
_ExtremeSecurityProfileDot11AuthMode_Object = MibTableColumn
extremeSecurityProfileDot11AuthMode = _ExtremeSecurityProfileDot11AuthMode_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2, 1, 1, 5),
    _ExtremeSecurityProfileDot11AuthMode_Type()
)
extremeSecurityProfileDot11AuthMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeSecurityProfileDot11AuthMode.setStatus("current")
_ExtremeSecurityProfileNetworkAuthMode_Type = NetworkAuthMode
_ExtremeSecurityProfileNetworkAuthMode_Object = MibTableColumn
extremeSecurityProfileNetworkAuthMode = _ExtremeSecurityProfileNetworkAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2, 1, 1, 6),
    _ExtremeSecurityProfileNetworkAuthMode_Type()
)
extremeSecurityProfileNetworkAuthMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeSecurityProfileNetworkAuthMode.setStatus("current")
_ExtremeSecurityProfileDataVlan_Type = Integer32
_ExtremeSecurityProfileDataVlan_Object = MibTableColumn
extremeSecurityProfileDataVlan = _ExtremeSecurityProfileDataVlan_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2, 1, 1, 7),
    _ExtremeSecurityProfileDataVlan_Type()
)
extremeSecurityProfileDataVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeSecurityProfileDataVlan.setStatus("current")
_ExtremeSecurityProfileIgnoreVSAVlan_Type = TruthValue
_ExtremeSecurityProfileIgnoreVSAVlan_Object = MibTableColumn
extremeSecurityProfileIgnoreVSAVlan = _ExtremeSecurityProfileIgnoreVSAVlan_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2, 1, 1, 8),
    _ExtremeSecurityProfileIgnoreVSAVlan_Type()
)
extremeSecurityProfileIgnoreVSAVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeSecurityProfileIgnoreVSAVlan.setStatus("current")
_ExtremeSecurityWEPDefaultKey_Type = Integer32
_ExtremeSecurityWEPDefaultKey_Object = MibTableColumn
extremeSecurityWEPDefaultKey = _ExtremeSecurityWEPDefaultKey_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2, 1, 1, 9),
    _ExtremeSecurityWEPDefaultKey_Type()
)
extremeSecurityWEPDefaultKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeSecurityWEPDefaultKey.setStatus("current")


class _ExtremeSecurityProfileEncryptionLength_Type(Integer32):
    """Custom type extremeSecurityProfileEncryptionLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("onetwentyeight", 128),
          ("sixtyfour", 64))
    )


_ExtremeSecurityProfileEncryptionLength_Type.__name__ = "Integer32"
_ExtremeSecurityProfileEncryptionLength_Object = MibTableColumn
extremeSecurityProfileEncryptionLength = _ExtremeSecurityProfileEncryptionLength_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2, 1, 1, 10),
    _ExtremeSecurityProfileEncryptionLength_Type()
)
extremeSecurityProfileEncryptionLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeSecurityProfileEncryptionLength.setStatus("current")
_ExtremeSecurityProfileStatus_Type = RowStatus
_ExtremeSecurityProfileStatus_Object = MibTableColumn
extremeSecurityProfileStatus = _ExtremeSecurityProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2, 1, 1, 11),
    _ExtremeSecurityProfileStatus_Type()
)
extremeSecurityProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeSecurityProfileStatus.setStatus("current")
_ExtremeSecurityDot1xConfigTable_Object = MibTable
extremeSecurityDot1xConfigTable = _ExtremeSecurityDot1xConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    extremeSecurityDot1xConfigTable.setStatus("current")
_ExtremeSecurityDot1xConfigEntry_Object = MibTableRow
extremeSecurityDot1xConfigEntry = _ExtremeSecurityDot1xConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2, 2, 1)
)
extremeSecurityDot1xConfigEntry.setIndexNames(
    (0, "EXTREME-WIRELESS-MIB", "extremeSecurityProfileIndex"),
)
if mibBuilder.loadTexts:
    extremeSecurityDot1xConfigEntry.setStatus("current")
_ExtremeSecurityKeyMgmtSuite_Type = WPAKeyMgmtSet
_ExtremeSecurityKeyMgmtSuite_Object = MibTableColumn
extremeSecurityKeyMgmtSuite = _ExtremeSecurityKeyMgmtSuite_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2, 2, 1, 1),
    _ExtremeSecurityKeyMgmtSuite_Type()
)
extremeSecurityKeyMgmtSuite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeSecurityKeyMgmtSuite.setStatus("current")
_ExtremeSecurityMcastCipherSuite_Type = WPACipherSet
_ExtremeSecurityMcastCipherSuite_Object = MibTableColumn
extremeSecurityMcastCipherSuite = _ExtremeSecurityMcastCipherSuite_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2, 2, 1, 2),
    _ExtremeSecurityMcastCipherSuite_Type()
)
extremeSecurityMcastCipherSuite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeSecurityMcastCipherSuite.setStatus("current")


class _ExtremeSecurityDot1xPSKValue_Type(OctetString):
    """Custom type extremeSecurityDot1xPSKValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_ExtremeSecurityDot1xPSKValue_Type.__name__ = "OctetString"
_ExtremeSecurityDot1xPSKValue_Object = MibTableColumn
extremeSecurityDot1xPSKValue = _ExtremeSecurityDot1xPSKValue_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2, 2, 1, 3),
    _ExtremeSecurityDot1xPSKValue_Type()
)
extremeSecurityDot1xPSKValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeSecurityDot1xPSKValue.setStatus("current")
_ExtremeSecurityDot1xPSKPassPhrase_Type = DisplayString
_ExtremeSecurityDot1xPSKPassPhrase_Object = MibTableColumn
extremeSecurityDot1xPSKPassPhrase = _ExtremeSecurityDot1xPSKPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2, 2, 1, 4),
    _ExtremeSecurityDot1xPSKPassPhrase_Type()
)
extremeSecurityDot1xPSKPassPhrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeSecurityDot1xPSKPassPhrase.setStatus("current")
_ExtremeSecurityDot1xReAuthPeriod_Type = Integer32
_ExtremeSecurityDot1xReAuthPeriod_Object = MibTableColumn
extremeSecurityDot1xReAuthPeriod = _ExtremeSecurityDot1xReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2, 2, 1, 5),
    _ExtremeSecurityDot1xReAuthPeriod_Type()
)
extremeSecurityDot1xReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeSecurityDot1xReAuthPeriod.setStatus("current")


class _ExtremeSecurityGroupUpdateTimeOut_Type(Unsigned32):
    """Custom type extremeSecurityGroupUpdateTimeOut based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_ExtremeSecurityGroupUpdateTimeOut_Type.__name__ = "Unsigned32"
_ExtremeSecurityGroupUpdateTimeOut_Object = MibTableColumn
extremeSecurityGroupUpdateTimeOut = _ExtremeSecurityGroupUpdateTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2, 2, 1, 6),
    _ExtremeSecurityGroupUpdateTimeOut_Type()
)
extremeSecurityGroupUpdateTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeSecurityGroupUpdateTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    extremeSecurityGroupUpdateTimeOut.setUnits("minutes")


class _ExtremeSecurityPairwiseUpdateTimeOut_Type(Unsigned32):
    """Custom type extremeSecurityPairwiseUpdateTimeOut based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_ExtremeSecurityPairwiseUpdateTimeOut_Type.__name__ = "Unsigned32"
_ExtremeSecurityPairwiseUpdateTimeOut_Object = MibTableColumn
extremeSecurityPairwiseUpdateTimeOut = _ExtremeSecurityPairwiseUpdateTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2, 2, 1, 7),
    _ExtremeSecurityPairwiseUpdateTimeOut_Type()
)
extremeSecurityPairwiseUpdateTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeSecurityPairwiseUpdateTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    extremeSecurityPairwiseUpdateTimeOut.setUnits("minutes")
_ExtremeSecurityDot11iPreauthEnabled_Type = TruthValue
_ExtremeSecurityDot11iPreauthEnabled_Object = MibTableColumn
extremeSecurityDot11iPreauthEnabled = _ExtremeSecurityDot11iPreauthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2, 2, 1, 8),
    _ExtremeSecurityDot11iPreauthEnabled_Type()
)
extremeSecurityDot11iPreauthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeSecurityDot11iPreauthEnabled.setStatus("current")
_ExtremeWEPKeyTable_Object = MibTable
extremeWEPKeyTable = _ExtremeWEPKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2, 4)
)
if mibBuilder.loadTexts:
    extremeWEPKeyTable.setStatus("current")
_ExtremeWEPKeyEntry_Object = MibTableRow
extremeWEPKeyEntry = _ExtremeWEPKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2, 4, 1)
)
extremeWEPKeyEntry.setIndexNames(
    (0, "EXTREME-WIRELESS-MIB", "extremeSecurityProfileIndex"),
    (0, "EXTREME-WIRELESS-MIB", "extremeWEPKeyIndex"),
)
if mibBuilder.loadTexts:
    extremeWEPKeyEntry.setStatus("current")


class _ExtremeWEPKeyIndex_Type(Integer32):
    """Custom type extremeWEPKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ExtremeWEPKeyIndex_Type.__name__ = "Integer32"
_ExtremeWEPKeyIndex_Object = MibTableColumn
extremeWEPKeyIndex = _ExtremeWEPKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2, 4, 1, 1),
    _ExtremeWEPKeyIndex_Type()
)
extremeWEPKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeWEPKeyIndex.setStatus("current")


class _ExtremeWEPKey_Type(OctetString):
    """Custom type extremeWEPKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_ExtremeWEPKey_Type.__name__ = "OctetString"
_ExtremeWEPKey_Object = MibTableColumn
extremeWEPKey = _ExtremeWEPKey_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2, 4, 1, 2),
    _ExtremeWEPKey_Type()
)
extremeWEPKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeWEPKey.setStatus("current")
_ExtremeWEPKeyStatus_Type = RowStatus
_ExtremeWEPKeyStatus_Object = MibTableColumn
extremeWEPKeyStatus = _ExtremeWEPKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 2, 4, 1, 3),
    _ExtremeWEPKeyStatus_Type()
)
extremeWEPKeyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeWEPKeyStatus.setStatus("current")
_ExtremeWirelessPhysInterfaceConfigTable_Object = MibTable
extremeWirelessPhysInterfaceConfigTable = _ExtremeWirelessPhysInterfaceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 3)
)
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfaceConfigTable.setStatus("current")
_ExtremeWirelessPhysInterfaceConfigEntry_Object = MibTableRow
extremeWirelessPhysInterfaceConfigEntry = _ExtremeWirelessPhysInterfaceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 3, 1)
)
extremeWirelessPhysInterfaceConfigEntry.setIndexNames(
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessPhysInterfaceIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfaceConfigEntry.setStatus("current")
_ExtremeWirelessPhysInterfaceConfigRFProfile_Type = Integer32
_ExtremeWirelessPhysInterfaceConfigRFProfile_Object = MibTableColumn
extremeWirelessPhysInterfaceConfigRFProfile = _ExtremeWirelessPhysInterfaceConfigRFProfile_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 3, 1, 1),
    _ExtremeWirelessPhysInterfaceConfigRFProfile_Type()
)
extremeWirelessPhysInterfaceConfigRFProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfaceConfigRFProfile.setStatus("current")
_ExtremeWirelessPhysInterfaceConfigRFChannel_Type = Integer32
_ExtremeWirelessPhysInterfaceConfigRFChannel_Object = MibTableColumn
extremeWirelessPhysInterfaceConfigRFChannel = _ExtremeWirelessPhysInterfaceConfigRFChannel_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 3, 1, 2),
    _ExtremeWirelessPhysInterfaceConfigRFChannel_Type()
)
extremeWirelessPhysInterfaceConfigRFChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfaceConfigRFChannel.setStatus("current")
_ExtremeWirelessPhysInterfaceConfigSpeed_Type = Dot11Speed
_ExtremeWirelessPhysInterfaceConfigSpeed_Object = MibTableColumn
extremeWirelessPhysInterfaceConfigSpeed = _ExtremeWirelessPhysInterfaceConfigSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 3, 1, 3),
    _ExtremeWirelessPhysInterfaceConfigSpeed_Type()
)
extremeWirelessPhysInterfaceConfigSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfaceConfigSpeed.setStatus("current")
_ExtremeWirelessPhysInterfaceConfigPowerLevel_Type = Integer32
_ExtremeWirelessPhysInterfaceConfigPowerLevel_Object = MibTableColumn
extremeWirelessPhysInterfaceConfigPowerLevel = _ExtremeWirelessPhysInterfaceConfigPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 3, 1, 4),
    _ExtremeWirelessPhysInterfaceConfigPowerLevel_Type()
)
extremeWirelessPhysInterfaceConfigPowerLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeWirelessPhysInterfaceConfigPowerLevel.setStatus("current")
_ExtremeWirelessVirtInterfaceConfigTable_Object = MibTable
extremeWirelessVirtInterfaceConfigTable = _ExtremeWirelessVirtInterfaceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 4)
)
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceConfigTable.setStatus("current")
_ExtremeWirelessVirtInterfaceConfigEntry_Object = MibTableRow
extremeWirelessVirtInterfaceConfigEntry = _ExtremeWirelessVirtInterfaceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 4, 1)
)
extremeWirelessVirtInterfaceConfigEntry.setIndexNames(
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessVirtInterfaceIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceConfigEntry.setStatus("current")
_ExtremeWirelessVirtInterfaceConfigSecurityProfile_Type = Integer32
_ExtremeWirelessVirtInterfaceConfigSecurityProfile_Object = MibTableColumn
extremeWirelessVirtInterfaceConfigSecurityProfile = _ExtremeWirelessVirtInterfaceConfigSecurityProfile_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 4, 1, 1),
    _ExtremeWirelessVirtInterfaceConfigSecurityProfile_Type()
)
extremeWirelessVirtInterfaceConfigSecurityProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceConfigSecurityProfile.setStatus("current")


class _ExtremeWirelessVirtInterfaceConfigMaxClients_Type(Integer32):
    """Custom type extremeWirelessVirtInterfaceConfigMaxClients based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_ExtremeWirelessVirtInterfaceConfigMaxClients_Type.__name__ = "Integer32"
_ExtremeWirelessVirtInterfaceConfigMaxClients_Object = MibTableColumn
extremeWirelessVirtInterfaceConfigMaxClients = _ExtremeWirelessVirtInterfaceConfigMaxClients_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 4, 1, 2),
    _ExtremeWirelessVirtInterfaceConfigMaxClients_Type()
)
extremeWirelessVirtInterfaceConfigMaxClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceConfigMaxClients.setStatus("current")
_ExtremeWirelessVirtInterfaceConfigWirelessBridging_Type = TruthValue
_ExtremeWirelessVirtInterfaceConfigWirelessBridging_Object = MibTableColumn
extremeWirelessVirtInterfaceConfigWirelessBridging = _ExtremeWirelessVirtInterfaceConfigWirelessBridging_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 4, 1, 3),
    _ExtremeWirelessVirtInterfaceConfigWirelessBridging_Type()
)
extremeWirelessVirtInterfaceConfigWirelessBridging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceConfigWirelessBridging.setStatus("current")


class _ExtremeWirelessVirtInterfaceConfigState_Type(Integer32):
    """Custom type extremeWirelessVirtInterfaceConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_ExtremeWirelessVirtInterfaceConfigState_Type.__name__ = "Integer32"
_ExtremeWirelessVirtInterfaceConfigState_Object = MibTableColumn
extremeWirelessVirtInterfaceConfigState = _ExtremeWirelessVirtInterfaceConfigState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 4, 1, 4),
    _ExtremeWirelessVirtInterfaceConfigState_Type()
)
extremeWirelessVirtInterfaceConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessVirtInterfaceConfigState.setStatus("current")
_ExtremeAntennaProfile_ObjectIdentity = ObjectIdentity
extremeAntennaProfile = _ExtremeAntennaProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 5)
)
_ExtremeAntennaProfileTable_Object = MibTable
extremeAntennaProfileTable = _ExtremeAntennaProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    extremeAntennaProfileTable.setStatus("current")
_ExtremeAntennaProfileEntry_Object = MibTableRow
extremeAntennaProfileEntry = _ExtremeAntennaProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 5, 1, 1)
)
extremeAntennaProfileEntry.setIndexNames(
    (0, "EXTREME-WIRELESS-MIB", "extremeAntennaProfileIndex"),
)
if mibBuilder.loadTexts:
    extremeAntennaProfileEntry.setStatus("current")


class _ExtremeAntennaProfileIndex_Type(Integer32):
    """Custom type extremeAntennaProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ExtremeAntennaProfileIndex_Type.__name__ = "Integer32"
_ExtremeAntennaProfileIndex_Object = MibTableColumn
extremeAntennaProfileIndex = _ExtremeAntennaProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 5, 1, 1, 1),
    _ExtremeAntennaProfileIndex_Type()
)
extremeAntennaProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeAntennaProfileIndex.setStatus("current")


class _ExtremeAntennaProfileName_Type(DisplayString):
    """Custom type extremeAntennaProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExtremeAntennaProfileName_Type.__name__ = "DisplayString"
_ExtremeAntennaProfileName_Object = MibTableColumn
extremeAntennaProfileName = _ExtremeAntennaProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 5, 1, 1, 2),
    _ExtremeAntennaProfileName_Type()
)
extremeAntennaProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeAntennaProfileName.setStatus("current")
_ExtremeAntennaProfile2point4GHZGain_Type = Integer32
_ExtremeAntennaProfile2point4GHZGain_Object = MibTableColumn
extremeAntennaProfile2point4GHZGain = _ExtremeAntennaProfile2point4GHZGain_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 5, 1, 1, 3),
    _ExtremeAntennaProfile2point4GHZGain_Type()
)
extremeAntennaProfile2point4GHZGain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeAntennaProfile2point4GHZGain.setStatus("current")
_ExtremeAntennaProfile5GHZGain_Type = Integer32
_ExtremeAntennaProfile5GHZGain_Object = MibTableColumn
extremeAntennaProfile5GHZGain = _ExtremeAntennaProfile5GHZGain_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 5, 1, 1, 4),
    _ExtremeAntennaProfile5GHZGain_Type()
)
extremeAntennaProfile5GHZGain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeAntennaProfile5GHZGain.setStatus("current")
_ExtremeAntennaProfileStatus_Type = RowStatus
_ExtremeAntennaProfileStatus_Object = MibTableColumn
extremeAntennaProfileStatus = _ExtremeAntennaProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 5, 1, 1, 5),
    _ExtremeAntennaProfileStatus_Type()
)
extremeAntennaProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeAntennaProfileStatus.setStatus("current")
_ExtremeWirelessRemoteConnectGlobalCfgGroup_ObjectIdentity = ObjectIdentity
extremeWirelessRemoteConnectGlobalCfgGroup = _ExtremeWirelessRemoteConnectGlobalCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 6)
)
_ExtremeWirelessRemoteConnectGlobalBindingType_Type = WirelessRemoteConnectBindingType
_ExtremeWirelessRemoteConnectGlobalBindingType_Object = MibScalar
extremeWirelessRemoteConnectGlobalBindingType = _ExtremeWirelessRemoteConnectGlobalBindingType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 6, 1),
    _ExtremeWirelessRemoteConnectGlobalBindingType_Type()
)
extremeWirelessRemoteConnectGlobalBindingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectGlobalBindingType.setStatus("current")
_ExtremeWirelessRemoteConnectBindingTable_Object = MibTable
extremeWirelessRemoteConnectBindingTable = _ExtremeWirelessRemoteConnectBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 7)
)
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectBindingTable.setStatus("current")
_ExtremeWirelessRemoteConnectBindingEntry_Object = MibTableRow
extremeWirelessRemoteConnectBindingEntry = _ExtremeWirelessRemoteConnectBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 7, 1)
)
extremeWirelessRemoteConnectBindingEntry.setIndexNames(
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessRemoteConnectBindingPortIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectBindingEntry.setStatus("current")


class _ExtremeWirelessRemoteConnectBindingPortIndex_Type(Integer32):
    """Custom type extremeWirelessRemoteConnectBindingPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ExtremeWirelessRemoteConnectBindingPortIndex_Type.__name__ = "Integer32"
_ExtremeWirelessRemoteConnectBindingPortIndex_Object = MibTableColumn
extremeWirelessRemoteConnectBindingPortIndex = _ExtremeWirelessRemoteConnectBindingPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 7, 1, 1),
    _ExtremeWirelessRemoteConnectBindingPortIndex_Type()
)
extremeWirelessRemoteConnectBindingPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectBindingPortIndex.setStatus("current")
_ExtremeWirelessRemoteConnectBindingIfIndex_Type = Integer32
_ExtremeWirelessRemoteConnectBindingIfIndex_Object = MibTableColumn
extremeWirelessRemoteConnectBindingIfIndex = _ExtremeWirelessRemoteConnectBindingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 7, 1, 2),
    _ExtremeWirelessRemoteConnectBindingIfIndex_Type()
)
extremeWirelessRemoteConnectBindingIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectBindingIfIndex.setStatus("current")
_ExtremeWirelessRemoteConnectBindingType_Type = WirelessRemoteConnectBindingType
_ExtremeWirelessRemoteConnectBindingType_Object = MibTableColumn
extremeWirelessRemoteConnectBindingType = _ExtremeWirelessRemoteConnectBindingType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 7, 1, 3),
    _ExtremeWirelessRemoteConnectBindingType_Type()
)
extremeWirelessRemoteConnectBindingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectBindingType.setStatus("current")
_ExtremeWirelessRemoteConnectBindingMAC_Type = MacAddress
_ExtremeWirelessRemoteConnectBindingMAC_Object = MibTableColumn
extremeWirelessRemoteConnectBindingMAC = _ExtremeWirelessRemoteConnectBindingMAC_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 7, 1, 4),
    _ExtremeWirelessRemoteConnectBindingMAC_Type()
)
extremeWirelessRemoteConnectBindingMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectBindingMAC.setStatus("current")
_ExtremeWirelessRemoteConnectBindingSerial_Type = OctetString
_ExtremeWirelessRemoteConnectBindingSerial_Object = MibTableColumn
extremeWirelessRemoteConnectBindingSerial = _ExtremeWirelessRemoteConnectBindingSerial_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 7, 1, 5),
    _ExtremeWirelessRemoteConnectBindingSerial_Type()
)
extremeWirelessRemoteConnectBindingSerial.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectBindingSerial.setStatus("current")
_ExtremeWirelessRemoteConnectBindingIPAddressType_Type = InetAddressType
_ExtremeWirelessRemoteConnectBindingIPAddressType_Object = MibTableColumn
extremeWirelessRemoteConnectBindingIPAddressType = _ExtremeWirelessRemoteConnectBindingIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 7, 1, 6),
    _ExtremeWirelessRemoteConnectBindingIPAddressType_Type()
)
extremeWirelessRemoteConnectBindingIPAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectBindingIPAddressType.setStatus("current")
_ExtremeWirelessRemoteConnectBindingIPAddress_Type = InetAddress
_ExtremeWirelessRemoteConnectBindingIPAddress_Object = MibTableColumn
extremeWirelessRemoteConnectBindingIPAddress = _ExtremeWirelessRemoteConnectBindingIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 7, 1, 7),
    _ExtremeWirelessRemoteConnectBindingIPAddress_Type()
)
extremeWirelessRemoteConnectBindingIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectBindingIPAddress.setStatus("current")
_ExtremeWirelessRemoteConnectBindingEnabled_Type = TruthValue
_ExtremeWirelessRemoteConnectBindingEnabled_Object = MibTableColumn
extremeWirelessRemoteConnectBindingEnabled = _ExtremeWirelessRemoteConnectBindingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 7, 1, 8),
    _ExtremeWirelessRemoteConnectBindingEnabled_Type()
)
extremeWirelessRemoteConnectBindingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectBindingEnabled.setStatus("current")
_ExtremeWirelessRemoteConnectBindingBound_Type = TruthValue
_ExtremeWirelessRemoteConnectBindingBound_Object = MibTableColumn
extremeWirelessRemoteConnectBindingBound = _ExtremeWirelessRemoteConnectBindingBound_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 7, 1, 9),
    _ExtremeWirelessRemoteConnectBindingBound_Type()
)
extremeWirelessRemoteConnectBindingBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectBindingBound.setStatus("current")
_ExtremeWirelessRemoteConnectBindingRowStatus_Type = RowStatus
_ExtremeWirelessRemoteConnectBindingRowStatus_Object = MibTableColumn
extremeWirelessRemoteConnectBindingRowStatus = _ExtremeWirelessRemoteConnectBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 7, 1, 10),
    _ExtremeWirelessRemoteConnectBindingRowStatus_Type()
)
extremeWirelessRemoteConnectBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectBindingRowStatus.setStatus("current")
_ExtremeWirelessRemoteConnectRedirectBindingTable_Object = MibTable
extremeWirelessRemoteConnectRedirectBindingTable = _ExtremeWirelessRemoteConnectRedirectBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 8)
)
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectRedirectBindingTable.setStatus("current")
_ExtremeWirelessRemoteConnectRedirectBindingEntry_Object = MibTableRow
extremeWirelessRemoteConnectRedirectBindingEntry = _ExtremeWirelessRemoteConnectRedirectBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 8, 1)
)
extremeWirelessRemoteConnectRedirectBindingEntry.setIndexNames(
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessRemoteConnectRedirectBindingIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectRedirectBindingEntry.setStatus("current")


class _ExtremeWirelessRemoteConnectRedirectBindingIndex_Type(Integer32):
    """Custom type extremeWirelessRemoteConnectRedirectBindingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ExtremeWirelessRemoteConnectRedirectBindingIndex_Type.__name__ = "Integer32"
_ExtremeWirelessRemoteConnectRedirectBindingIndex_Object = MibTableColumn
extremeWirelessRemoteConnectRedirectBindingIndex = _ExtremeWirelessRemoteConnectRedirectBindingIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 8, 1, 1),
    _ExtremeWirelessRemoteConnectRedirectBindingIndex_Type()
)
extremeWirelessRemoteConnectRedirectBindingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectRedirectBindingIndex.setStatus("current")
_ExtremeWirelessRemoteConnectRedirectBindingType_Type = WirelessRemoteConnectBindingType
_ExtremeWirelessRemoteConnectRedirectBindingType_Object = MibTableColumn
extremeWirelessRemoteConnectRedirectBindingType = _ExtremeWirelessRemoteConnectRedirectBindingType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 8, 1, 2),
    _ExtremeWirelessRemoteConnectRedirectBindingType_Type()
)
extremeWirelessRemoteConnectRedirectBindingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectRedirectBindingType.setStatus("current")
_ExtremeWirelessRemoteConnectRedirectBindingMAC_Type = MacAddress
_ExtremeWirelessRemoteConnectRedirectBindingMAC_Object = MibTableColumn
extremeWirelessRemoteConnectRedirectBindingMAC = _ExtremeWirelessRemoteConnectRedirectBindingMAC_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 8, 1, 3),
    _ExtremeWirelessRemoteConnectRedirectBindingMAC_Type()
)
extremeWirelessRemoteConnectRedirectBindingMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectRedirectBindingMAC.setStatus("current")
_ExtremeWirelessRemoteConnectRedirectBindingSerial_Type = OctetString
_ExtremeWirelessRemoteConnectRedirectBindingSerial_Object = MibTableColumn
extremeWirelessRemoteConnectRedirectBindingSerial = _ExtremeWirelessRemoteConnectRedirectBindingSerial_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 8, 1, 4),
    _ExtremeWirelessRemoteConnectRedirectBindingSerial_Type()
)
extremeWirelessRemoteConnectRedirectBindingSerial.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectRedirectBindingSerial.setStatus("current")
_ExtremeWirelessRemoteConnectRedirectBindingIPAddressType_Type = InetAddressType
_ExtremeWirelessRemoteConnectRedirectBindingIPAddressType_Object = MibTableColumn
extremeWirelessRemoteConnectRedirectBindingIPAddressType = _ExtremeWirelessRemoteConnectRedirectBindingIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 8, 1, 5),
    _ExtremeWirelessRemoteConnectRedirectBindingIPAddressType_Type()
)
extremeWirelessRemoteConnectRedirectBindingIPAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectRedirectBindingIPAddressType.setStatus("current")
_ExtremeWirelessRemoteConnectRedirectBindingIPAddress_Type = InetAddress
_ExtremeWirelessRemoteConnectRedirectBindingIPAddress_Object = MibTableColumn
extremeWirelessRemoteConnectRedirectBindingIPAddress = _ExtremeWirelessRemoteConnectRedirectBindingIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 8, 1, 6),
    _ExtremeWirelessRemoteConnectRedirectBindingIPAddress_Type()
)
extremeWirelessRemoteConnectRedirectBindingIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectRedirectBindingIPAddress.setStatus("current")
_ExtremeWirelessRemoteConnectRedirectBindAttachSwitchIPAddrType_Type = InetAddressType
_ExtremeWirelessRemoteConnectRedirectBindAttachSwitchIPAddrType_Object = MibTableColumn
extremeWirelessRemoteConnectRedirectBindAttachSwitchIPAddrType = _ExtremeWirelessRemoteConnectRedirectBindAttachSwitchIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 8, 1, 7),
    _ExtremeWirelessRemoteConnectRedirectBindAttachSwitchIPAddrType_Type()
)
extremeWirelessRemoteConnectRedirectBindAttachSwitchIPAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectRedirectBindAttachSwitchIPAddrType.setStatus("current")
_ExtremeWirelessRemoteConnectRedirectBindAttachSwitchIPAddr_Type = InetAddress
_ExtremeWirelessRemoteConnectRedirectBindAttachSwitchIPAddr_Object = MibTableColumn
extremeWirelessRemoteConnectRedirectBindAttachSwitchIPAddr = _ExtremeWirelessRemoteConnectRedirectBindAttachSwitchIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 8, 1, 8),
    _ExtremeWirelessRemoteConnectRedirectBindAttachSwitchIPAddr_Type()
)
extremeWirelessRemoteConnectRedirectBindAttachSwitchIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectRedirectBindAttachSwitchIPAddr.setStatus("current")
_ExtremeWirelessRemoteConnectRedirectBindingEnabled_Type = TruthValue
_ExtremeWirelessRemoteConnectRedirectBindingEnabled_Object = MibTableColumn
extremeWirelessRemoteConnectRedirectBindingEnabled = _ExtremeWirelessRemoteConnectRedirectBindingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 8, 1, 9),
    _ExtremeWirelessRemoteConnectRedirectBindingEnabled_Type()
)
extremeWirelessRemoteConnectRedirectBindingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectRedirectBindingEnabled.setStatus("current")
_ExtremeWirelessRemoteConnectRedirectBindingNumRedirects_Type = Counter32
_ExtremeWirelessRemoteConnectRedirectBindingNumRedirects_Object = MibTableColumn
extremeWirelessRemoteConnectRedirectBindingNumRedirects = _ExtremeWirelessRemoteConnectRedirectBindingNumRedirects_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 8, 1, 10),
    _ExtremeWirelessRemoteConnectRedirectBindingNumRedirects_Type()
)
extremeWirelessRemoteConnectRedirectBindingNumRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectRedirectBindingNumRedirects.setStatus("current")
_ExtremeWirelessRemoteConnectRedirectBindingRowStatus_Type = RowStatus
_ExtremeWirelessRemoteConnectRedirectBindingRowStatus_Object = MibTableColumn
extremeWirelessRemoteConnectRedirectBindingRowStatus = _ExtremeWirelessRemoteConnectRedirectBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 8, 1, 11),
    _ExtremeWirelessRemoteConnectRedirectBindingRowStatus_Type()
)
extremeWirelessRemoteConnectRedirectBindingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectRedirectBindingRowStatus.setStatus("current")
_ExtremeWirelessRemoteConnectDeviceDBGroup_ObjectIdentity = ObjectIdentity
extremeWirelessRemoteConnectDeviceDBGroup = _ExtremeWirelessRemoteConnectDeviceDBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 9)
)


class _ExtremeWirelessRemoteConnectDeviceDBTimeOut_Type(Integer32):
    """Custom type extremeWirelessRemoteConnectDeviceDBTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 3600),
    )


_ExtremeWirelessRemoteConnectDeviceDBTimeOut_Type.__name__ = "Integer32"
_ExtremeWirelessRemoteConnectDeviceDBTimeOut_Object = MibScalar
extremeWirelessRemoteConnectDeviceDBTimeOut = _ExtremeWirelessRemoteConnectDeviceDBTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 9, 1),
    _ExtremeWirelessRemoteConnectDeviceDBTimeOut_Type()
)
extremeWirelessRemoteConnectDeviceDBTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectDeviceDBTimeOut.setStatus("current")
_ExtremeWirelessRemoteConnectUnboundAPsTable_Object = MibTable
extremeWirelessRemoteConnectUnboundAPsTable = _ExtremeWirelessRemoteConnectUnboundAPsTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 10)
)
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectUnboundAPsTable.setStatus("current")
_ExtremeWirelessRemoteConnectUnboundAPsEntry_Object = MibTableRow
extremeWirelessRemoteConnectUnboundAPsEntry = _ExtremeWirelessRemoteConnectUnboundAPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 10, 1)
)
extremeWirelessRemoteConnectUnboundAPsEntry.setIndexNames(
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessRemoteConnectUnboundAPsIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectUnboundAPsEntry.setStatus("current")


class _ExtremeWirelessRemoteConnectUnboundAPsIndex_Type(Integer32):
    """Custom type extremeWirelessRemoteConnectUnboundAPsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeWirelessRemoteConnectUnboundAPsIndex_Type.__name__ = "Integer32"
_ExtremeWirelessRemoteConnectUnboundAPsIndex_Object = MibTableColumn
extremeWirelessRemoteConnectUnboundAPsIndex = _ExtremeWirelessRemoteConnectUnboundAPsIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 10, 1, 1),
    _ExtremeWirelessRemoteConnectUnboundAPsIndex_Type()
)
extremeWirelessRemoteConnectUnboundAPsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectUnboundAPsIndex.setStatus("current")
_ExtremeWirelessRemoteConnectUnboundAPsMAC_Type = MacAddress
_ExtremeWirelessRemoteConnectUnboundAPsMAC_Object = MibTableColumn
extremeWirelessRemoteConnectUnboundAPsMAC = _ExtremeWirelessRemoteConnectUnboundAPsMAC_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 10, 1, 2),
    _ExtremeWirelessRemoteConnectUnboundAPsMAC_Type()
)
extremeWirelessRemoteConnectUnboundAPsMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectUnboundAPsMAC.setStatus("current")
_ExtremeWirelessRemoteConnectUnboundAPsSerial_Type = OctetString
_ExtremeWirelessRemoteConnectUnboundAPsSerial_Object = MibTableColumn
extremeWirelessRemoteConnectUnboundAPsSerial = _ExtremeWirelessRemoteConnectUnboundAPsSerial_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 10, 1, 3),
    _ExtremeWirelessRemoteConnectUnboundAPsSerial_Type()
)
extremeWirelessRemoteConnectUnboundAPsSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectUnboundAPsSerial.setStatus("current")
_ExtremeWirelessRemoteConnectUnboundAPsIPAddressType_Type = InetAddressType
_ExtremeWirelessRemoteConnectUnboundAPsIPAddressType_Object = MibTableColumn
extremeWirelessRemoteConnectUnboundAPsIPAddressType = _ExtremeWirelessRemoteConnectUnboundAPsIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 10, 1, 4),
    _ExtremeWirelessRemoteConnectUnboundAPsIPAddressType_Type()
)
extremeWirelessRemoteConnectUnboundAPsIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectUnboundAPsIPAddressType.setStatus("current")
_ExtremeWirelessRemoteConnectUnboundAPsIPAddress_Type = InetAddress
_ExtremeWirelessRemoteConnectUnboundAPsIPAddress_Object = MibTableColumn
extremeWirelessRemoteConnectUnboundAPsIPAddress = _ExtremeWirelessRemoteConnectUnboundAPsIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 10, 1, 5),
    _ExtremeWirelessRemoteConnectUnboundAPsIPAddress_Type()
)
extremeWirelessRemoteConnectUnboundAPsIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectUnboundAPsIPAddress.setStatus("current")
_ExtremeWirelessRemoteConnectUnboundAPsNumAttempts_Type = Counter32
_ExtremeWirelessRemoteConnectUnboundAPsNumAttempts_Object = MibTableColumn
extremeWirelessRemoteConnectUnboundAPsNumAttempts = _ExtremeWirelessRemoteConnectUnboundAPsNumAttempts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 10, 1, 6),
    _ExtremeWirelessRemoteConnectUnboundAPsNumAttempts_Type()
)
extremeWirelessRemoteConnectUnboundAPsNumAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectUnboundAPsNumAttempts.setStatus("current")
_ExtremeWirelessRemoteConnectUnboundAPsRowStatus_Type = RowStatus
_ExtremeWirelessRemoteConnectUnboundAPsRowStatus_Object = MibTableColumn
extremeWirelessRemoteConnectUnboundAPsRowStatus = _ExtremeWirelessRemoteConnectUnboundAPsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 2, 10, 1, 7),
    _ExtremeWirelessRemoteConnectUnboundAPsRowStatus_Type()
)
extremeWirelessRemoteConnectUnboundAPsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeWirelessRemoteConnectUnboundAPsRowStatus.setStatus("current")
_ExtremeWirelessPortCfgTable_Object = MibTable
extremeWirelessPortCfgTable = _ExtremeWirelessPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 3)
)
if mibBuilder.loadTexts:
    extremeWirelessPortCfgTable.setStatus("current")
_ExtremeWirelessPortCfgEntry_Object = MibTableRow
extremeWirelessPortCfgEntry = _ExtremeWirelessPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 3, 1)
)
extremeWirelessPortCfgEntry.setIndexNames(
    (0, "EXTREME-WIRELESS-MIB", "extremeWirelessPortIfIndex"),
)
if mibBuilder.loadTexts:
    extremeWirelessPortCfgEntry.setStatus("current")
_ExtremeWirelessPortIfIndex_Type = InterfaceIndex
_ExtremeWirelessPortIfIndex_Object = MibTableColumn
extremeWirelessPortIfIndex = _ExtremeWirelessPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 3, 1, 1),
    _ExtremeWirelessPortIfIndex_Type()
)
extremeWirelessPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessPortIfIndex.setStatus("current")
_ExtremeWirelessPortCfgIpAddress_Type = IpAddress
_ExtremeWirelessPortCfgIpAddress_Object = MibTableColumn
extremeWirelessPortCfgIpAddress = _ExtremeWirelessPortCfgIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 3, 1, 2),
    _ExtremeWirelessPortCfgIpAddress_Type()
)
extremeWirelessPortCfgIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortCfgIpAddress.setStatus("current")
_ExtremeWirelessPortCfgLocation_Type = DisplayString
_ExtremeWirelessPortCfgLocation_Object = MibTableColumn
extremeWirelessPortCfgLocation = _ExtremeWirelessPortCfgLocation_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 3, 1, 3),
    _ExtremeWirelessPortCfgLocation_Type()
)
extremeWirelessPortCfgLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortCfgLocation.setStatus("current")
_ExtremeWirelessPortCfgDetectedTimeout_Type = TimeTicks
_ExtremeWirelessPortCfgDetectedTimeout_Object = MibTableColumn
extremeWirelessPortCfgDetectedTimeout = _ExtremeWirelessPortCfgDetectedTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 3, 1, 4),
    _ExtremeWirelessPortCfgDetectedTimeout_Type()
)
extremeWirelessPortCfgDetectedTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortCfgDetectedTimeout.setStatus("current")
_ExtremeWirelessPortCfgClientWatchdog_Type = TruthValue
_ExtremeWirelessPortCfgClientWatchdog_Object = MibTableColumn
extremeWirelessPortCfgClientWatchdog = _ExtremeWirelessPortCfgClientWatchdog_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 3, 1, 5),
    _ExtremeWirelessPortCfgClientWatchdog_Type()
)
extremeWirelessPortCfgClientWatchdog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortCfgClientWatchdog.setStatus("current")
_ExtremeWirelessPortLastChange_Type = TimeTicks
_ExtremeWirelessPortLastChange_Object = MibTableColumn
extremeWirelessPortLastChange = _ExtremeWirelessPortLastChange_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 3, 1, 6),
    _ExtremeWirelessPortLastChange_Type()
)
extremeWirelessPortLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessPortLastChange.setStatus("current")


class _ExtremeWirelessPortState_Type(Integer32):
    """Custom type extremeWirelessPortState based on Integer32"""
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
        *(("addressing", 4),
          ("disabled", 1),
          ("enabled", 2),
          ("error", 8),
          ("online", 7),
          ("register", 5),
          ("reset", 3),
          ("syncing", 6))
    )


_ExtremeWirelessPortState_Type.__name__ = "Integer32"
_ExtremeWirelessPortState_Object = MibTableColumn
extremeWirelessPortState = _ExtremeWirelessPortState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 3, 1, 7),
    _ExtremeWirelessPortState_Type()
)
extremeWirelessPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWirelessPortState.setStatus("current")
_ExtremeWirelessPortAntennaType_Type = ExtremeWirelessAntennaType
_ExtremeWirelessPortAntennaType_Object = MibTableColumn
extremeWirelessPortAntennaType = _ExtremeWirelessPortAntennaType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 3, 1, 8),
    _ExtremeWirelessPortAntennaType_Type()
)
extremeWirelessPortAntennaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortAntennaType.setStatus("current")
_ExtremeWirelessPortAntennaLocation_Type = ExtremeWirelessAntennaLocation
_ExtremeWirelessPortAntennaLocation_Object = MibTableColumn
extremeWirelessPortAntennaLocation = _ExtremeWirelessPortAntennaLocation_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 3, 1, 9),
    _ExtremeWirelessPortAntennaLocation_Type()
)
extremeWirelessPortAntennaLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortAntennaLocation.setStatus("current")
_ExtremeWirelessPortBootstrapServerAddressType_Type = InetAddressType
_ExtremeWirelessPortBootstrapServerAddressType_Object = MibTableColumn
extremeWirelessPortBootstrapServerAddressType = _ExtremeWirelessPortBootstrapServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 3, 1, 10),
    _ExtremeWirelessPortBootstrapServerAddressType_Type()
)
extremeWirelessPortBootstrapServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortBootstrapServerAddressType.setStatus("current")


class _ExtremeWirelessPortBootstrapServerAddress_Type(InetAddress):
    """Custom type extremeWirelessPortBootstrapServerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ExtremeWirelessPortBootstrapServerAddress_Type.__name__ = "InetAddress"
_ExtremeWirelessPortBootstrapServerAddress_Object = MibTableColumn
extremeWirelessPortBootstrapServerAddress = _ExtremeWirelessPortBootstrapServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 3, 1, 11),
    _ExtremeWirelessPortBootstrapServerAddress_Type()
)
extremeWirelessPortBootstrapServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortBootstrapServerAddress.setStatus("current")
_ExtremeWirelessPortBootstrapFilePath_Type = DisplayString
_ExtremeWirelessPortBootstrapFilePath_Object = MibTableColumn
extremeWirelessPortBootstrapFilePath = _ExtremeWirelessPortBootstrapFilePath_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 3, 1, 12),
    _ExtremeWirelessPortBootstrapFilePath_Type()
)
extremeWirelessPortBootstrapFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortBootstrapFilePath.setStatus("current")
_ExtremeWirelessPortBootLoaderServerAddressType_Type = InetAddressType
_ExtremeWirelessPortBootLoaderServerAddressType_Object = MibTableColumn
extremeWirelessPortBootLoaderServerAddressType = _ExtremeWirelessPortBootLoaderServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 3, 1, 13),
    _ExtremeWirelessPortBootLoaderServerAddressType_Type()
)
extremeWirelessPortBootLoaderServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortBootLoaderServerAddressType.setStatus("current")


class _ExtremeWirelessPortBootLoaderServerAddress_Type(InetAddress):
    """Custom type extremeWirelessPortBootLoaderServerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ExtremeWirelessPortBootLoaderServerAddress_Type.__name__ = "InetAddress"
_ExtremeWirelessPortBootLoaderServerAddress_Object = MibTableColumn
extremeWirelessPortBootLoaderServerAddress = _ExtremeWirelessPortBootLoaderServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 3, 1, 14),
    _ExtremeWirelessPortBootLoaderServerAddress_Type()
)
extremeWirelessPortBootLoaderServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortBootLoaderServerAddress.setStatus("current")
_ExtremeWirelessPortBootLoaderFilePath_Type = DisplayString
_ExtremeWirelessPortBootLoaderFilePath_Object = MibTableColumn
extremeWirelessPortBootLoaderFilePath = _ExtremeWirelessPortBootLoaderFilePath_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 3, 1, 15),
    _ExtremeWirelessPortBootLoaderFilePath_Type()
)
extremeWirelessPortBootLoaderFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortBootLoaderFilePath.setStatus("current")
_ExtremeWirelessPortRuntimeServerAddressType_Type = InetAddressType
_ExtremeWirelessPortRuntimeServerAddressType_Object = MibTableColumn
extremeWirelessPortRuntimeServerAddressType = _ExtremeWirelessPortRuntimeServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 3, 1, 16),
    _ExtremeWirelessPortRuntimeServerAddressType_Type()
)
extremeWirelessPortRuntimeServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortRuntimeServerAddressType.setStatus("current")


class _ExtremeWirelessPortRuntimeServerAddress_Type(InetAddress):
    """Custom type extremeWirelessPortRuntimeServerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ExtremeWirelessPortRuntimeServerAddress_Type.__name__ = "InetAddress"
_ExtremeWirelessPortRuntimeServerAddress_Object = MibTableColumn
extremeWirelessPortRuntimeServerAddress = _ExtremeWirelessPortRuntimeServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 3, 1, 17),
    _ExtremeWirelessPortRuntimeServerAddress_Type()
)
extremeWirelessPortRuntimeServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortRuntimeServerAddress.setStatus("current")
_ExtremeWirelessPortRuntimeFilePath_Type = DisplayString
_ExtremeWirelessPortRuntimeFilePath_Object = MibTableColumn
extremeWirelessPortRuntimeFilePath = _ExtremeWirelessPortRuntimeFilePath_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 3, 1, 18),
    _ExtremeWirelessPortRuntimeFilePath_Type()
)
extremeWirelessPortRuntimeFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortRuntimeFilePath.setStatus("current")


class _ExtremeWirelessPortMultiBootMode_Type(Integer32):
    """Custom type extremeWirelessPortMultiBootMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("a-bp", 1),
          ("a300", 0))
    )


_ExtremeWirelessPortMultiBootMode_Type.__name__ = "Integer32"
_ExtremeWirelessPortMultiBootMode_Object = MibTableColumn
extremeWirelessPortMultiBootMode = _ExtremeWirelessPortMultiBootMode_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2, 3, 1, 19),
    _ExtremeWirelessPortMultiBootMode_Type()
)
extremeWirelessPortMultiBootMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeWirelessPortMultiBootMode.setStatus("current")
_ExtremeAPTraps_ObjectIdentity = ObjectIdentity
extremeAPTraps = _ExtremeAPTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 5)
)
_ExtremeAPTrapsPrefix_ObjectIdentity = ObjectIdentity
extremeAPTrapsPrefix = _ExtremeAPTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 5, 0)
)

# Managed Objects groups


# Notification objects

extremeWirelessPortStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 5, 0, 1)
)
extremeWirelessPortStateChange.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessPortState"))
)
if mibBuilder.loadTexts:
    extremeWirelessPortStateChange.setStatus(
        "current"
    )

extremeWirelessPortBootFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 5, 0, 2)
)
extremeWirelessPortBootFailure.setObjects(
    ("EXTREME-WIRELESS-MIB", "extremeWirelessPortIfIndex")
)
if mibBuilder.loadTexts:
    extremeWirelessPortBootFailure.setStatus(
        "current"
    )

extremeWirelessClientStationAgedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 5, 0, 3)
)
extremeWirelessClientStationAgedOut.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessClientID"))
)
if mibBuilder.loadTexts:
    extremeWirelessClientStationAgedOut.setStatus(
        "current"
    )

extremeWirelessNetloginClientAssociated = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 5, 0, 4)
)
extremeWirelessNetloginClientAssociated.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessClientID"))
)
if mibBuilder.loadTexts:
    extremeWirelessNetloginClientAssociated.setStatus(
        "current"
    )

extremeWirelessAPAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 5, 0, 5)
)
extremeWirelessAPAdded.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanResultsStationId"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanResultsFirstSeen"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanResultsLastChange"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanResultsPacketRate"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanResultsChannel"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanResultsAvgRSS"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanResultsSSID"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanResultsRSNEnabled"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanResultsPrivacy"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanResultsNetworkType"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanWPAIEMcastCipher"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanWPAUcastCipherCount"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanWPAUcastCipher"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanWPAKeyMgmtCount"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanWPAKeyMgmtSuite"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanResultsRateSet"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanResultsExtRateSet"))
)
if mibBuilder.loadTexts:
    extremeWirelessAPAdded.setStatus(
        "current"
    )

extremeWirelessAPRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 5, 0, 6)
)
extremeWirelessAPRemoved.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanResultsStationId"))
)
if mibBuilder.loadTexts:
    extremeWirelessAPRemoved.setStatus(
        "current"
    )

extremeWirelessAPUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 5, 0, 7)
)
extremeWirelessAPUpdated.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanResultsStationId"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanResultsFirstSeen"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanResultsLastChange"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanResultsPacketRate"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanResultsChannel"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanResultsAvgRSS"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanResultsSSID"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanResultsRSNEnabled"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanResultsPrivacy"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanResultsNetworkType"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanWPAIEMcastCipher"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanWPAUcastCipherCount"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanWPAUcastCipher"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanWPAKeyMgmtCount"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanWPAKeyMgmtSuite"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanResultsRateSet"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessScanResultsExtRateSet"))
)
if mibBuilder.loadTexts:
    extremeWirelessAPUpdated.setStatus(
        "current"
    )

extremeWirelessProbeInfoAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 5, 0, 8)
)
extremeWirelessProbeInfoAdded.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessProbeInfoSource"))
)
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoAdded.setStatus(
        "current"
    )

extremeWirelessProbeInfoRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 5, 0, 9)
)
extremeWirelessProbeInfoRemoved.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessProbeInfoSource"))
)
if mibBuilder.loadTexts:
    extremeWirelessProbeInfoRemoved.setStatus(
        "current"
    )

extremeWirelessOffChannelScanStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 5, 0, 10)
)
extremeWirelessOffChannelScanStarted.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessOffChannelScanList"))
)
if mibBuilder.loadTexts:
    extremeWirelessOffChannelScanStarted.setStatus(
        "current"
    )

extremeWirelessOffChannelScanFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 5, 0, 11)
)
extremeWirelessOffChannelScanFinished.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessOffChannelScanList"))
)
if mibBuilder.loadTexts:
    extremeWirelessOffChannelScanFinished.setStatus(
        "current"
    )

extremeWirelessCounterMeasureStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 5, 0, 12)
)
extremeWirelessCounterMeasureStarted.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessCounterMeasureSource"))
)
if mibBuilder.loadTexts:
    extremeWirelessCounterMeasureStarted.setStatus(
        "current"
    )

extremeWirelessCounterMeasureStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 5, 0, 13)
)
extremeWirelessCounterMeasureStopped.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    extremeWirelessCounterMeasureStopped.setStatus(
        "current"
    )

extremeWirelessInterfaceChannelRescan = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 5, 0, 14)
)
extremeWirelessInterfaceChannelRescan.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessPhysInterfacePHYChannel"),
        ("EXTREME-WIRELESS-MIB", "extremeWirelessPhysInterfaceChannelAutoSelectStatus"))
)
if mibBuilder.loadTexts:
    extremeWirelessInterfaceChannelRescan.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-WIRELESS-MIB",
    **{"Dot11Type": Dot11Type,
       "Dot11Speed": Dot11Speed,
       "Dot11AChannel": Dot11AChannel,
       "Dot11AuthMode": Dot11AuthMode,
       "NetworkAuthMode": NetworkAuthMode,
       "ExtremeWirelessCountryCode": ExtremeWirelessCountryCode,
       "ExtremeWirelessAntennaType": ExtremeWirelessAntennaType,
       "ExtremeWirelessAntennaLocation": ExtremeWirelessAntennaLocation,
       "ExtremeWirelessPhysInterfaceIndex": ExtremeWirelessPhysInterfaceIndex,
       "ExtremeWirelessVirtInterfaceIndex": ExtremeWirelessVirtInterfaceIndex,
       "ExtremeWirelessChannelAutoSelectStatus": ExtremeWirelessChannelAutoSelectStatus,
       "extremeWireless": extremeWireless,
       "extremeWirelessPortStatusTable": extremeWirelessPortStatusTable,
       "extremeWirelessPortStatusEntry": extremeWirelessPortStatusEntry,
       "extremeWirelessPortIpAddress": extremeWirelessPortIpAddress,
       "extremeWirelessPortNetmask": extremeWirelessPortNetmask,
       "extremeWirelessPortGateway": extremeWirelessPortGateway,
       "extremeWirelessPortManagementIP": extremeWirelessPortManagementIP,
       "extremeWirelessPortEnableWirelessTraps": extremeWirelessPortEnableWirelessTraps,
       "extremeWirelessPortLocation": extremeWirelessPortLocation,
       "extremeWirelessPortDetectedMaxAge": extremeWirelessPortDetectedMaxAge,
       "extremeWirelessPortMgmtVLAN": extremeWirelessPortMgmtVLAN,
       "extremeWirelessPortBootromVersion": extremeWirelessPortBootromVersion,
       "extremeWirelessPortSWVersion": extremeWirelessPortSWVersion,
       "extremeWirelessPortSysDescr": extremeWirelessPortSysDescr,
       "extremeWirelessPortManufacturerName": extremeWirelessPortManufacturerName,
       "extremeWirelessPortProductName": extremeWirelessPortProductName,
       "extremeWirelessPortSerialNumber": extremeWirelessPortSerialNumber,
       "extremeWirelessPortEdpNeighborId": extremeWirelessPortEdpNeighborId,
       "extremeWirelessPortClearCounters": extremeWirelessPortClearCounters,
       "extremeWirelessPortClearLog": extremeWirelessPortClearLog,
       "extremeWirelessPortWatchdogReset": extremeWirelessPortWatchdogReset,
       "extremeWirelessPortNumPhysInterfaces": extremeWirelessPortNumPhysInterfaces,
       "extremeWirelessPortHWVersion": extremeWirelessPortHWVersion,
       "extremeWirelessPortMacAddress": extremeWirelessPortMacAddress,
       "extremeWirelessPortRadiusPortID": extremeWirelessPortRadiusPortID,
       "extremeWirelessPortBootUpTime": extremeWirelessPortBootUpTime,
       "extremeWirelessPortCountryCode": extremeWirelessPortCountryCode,
       "extremeWirelessPortWallclockTime": extremeWirelessPortWallclockTime,
       "extremeWirelessPortPartNumber": extremeWirelessPortPartNumber,
       "extremeWirelessPortPartRevision": extremeWirelessPortPartRevision,
       "extremeWirelessPortUpTime": extremeWirelessPortUpTime,
       "extremeWirelessPortStatusAntennaType": extremeWirelessPortStatusAntennaType,
       "extremeWirelessPortStatusAntennaLocation": extremeWirelessPortStatusAntennaLocation,
       "extremeWirelessPortStatusAntenna2point4GHZGain": extremeWirelessPortStatusAntenna2point4GHZGain,
       "extremeWirelessPortStatusAntenna5GHZGain": extremeWirelessPortStatusAntenna5GHZGain,
       "extremeWirelessPortPrimaryBootloaderVersion": extremeWirelessPortPrimaryBootloaderVersion,
       "extremeWirelessPortSecondaryBootloaderVersion": extremeWirelessPortSecondaryBootloaderVersion,
       "extremeWirelessPortCurrentBootloaderInUse": extremeWirelessPortCurrentBootloaderInUse,
       "extremeWirelessPortLogStatusTable": extremeWirelessPortLogStatusTable,
       "extremeWirelessPortLogStatusEntry": extremeWirelessPortLogStatusEntry,
       "extremeWirelessPortLogStatusIndex": extremeWirelessPortLogStatusIndex,
       "extremeWirelessPortLogStatusDestIp": extremeWirelessPortLogStatusDestIp,
       "extremeWirelessPortLogStatusDestIpType": extremeWirelessPortLogStatusDestIpType,
       "extremeWirelessPortLogStatusPort": extremeWirelessPortLogStatusPort,
       "extremeWirelessPortLogStatusFacility": extremeWirelessPortLogStatusFacility,
       "extremeWirelessPortLogStatusSeverity": extremeWirelessPortLogStatusSeverity,
       "extremeWirelessPortLogStatusStatus": extremeWirelessPortLogStatusStatus,
       "extremeWirelessPortLogTable": extremeWirelessPortLogTable,
       "extremeWirelessPortLogEntry": extremeWirelessPortLogEntry,
       "extremeWirelessPortLogIndex": extremeWirelessPortLogIndex,
       "extremeWirelessPortLogMessage": extremeWirelessPortLogMessage,
       "extremeWirelessPhysInterfaceCtlTable": extremeWirelessPhysInterfaceCtlTable,
       "extremeWirelessPhysInterfaceCtlEntry": extremeWirelessPhysInterfaceCtlEntry,
       "extremeWirelessPhysInterfaceIndex": extremeWirelessPhysInterfaceIndex,
       "extremeWirelessPhysInterfacePHYChannel": extremeWirelessPhysInterfacePHYChannel,
       "extremeWirelessPhysInterfaceSpeed": extremeWirelessPhysInterfaceSpeed,
       "extremeWirelessPhysInterfaceNumVirtInterfaces": extremeWirelessPhysInterfaceNumVirtInterfaces,
       "extremeWirelessPhysInterfaceChannelAutoSelectStatus": extremeWirelessPhysInterfaceChannelAutoSelectStatus,
       "extremeWirelessPhysInterfaceRadarInterfaceChannelList": extremeWirelessPhysInterfaceRadarInterfaceChannelList,
       "extremeWirelessInterfaceStatusTable": extremeWirelessInterfaceStatusTable,
       "extremeWirelessInterfaceStatusEntry": extremeWirelessInterfaceStatusEntry,
       "extremeWirelessIntfTotalDetected": extremeWirelessIntfTotalDetected,
       "extremeWirelessIntfTotalAuthed": extremeWirelessIntfTotalAuthed,
       "extremeWirelessIntfTotalAuthFailed": extremeWirelessIntfTotalAuthFailed,
       "extremeWirelessIntfTotalAssoc": extremeWirelessIntfTotalAssoc,
       "extremeWirelessIntfTotalAssocFailed": extremeWirelessIntfTotalAssocFailed,
       "extremeWirelessIntfRateDetected": extremeWirelessIntfRateDetected,
       "extremeWirelessIntfRateAuthed": extremeWirelessIntfRateAuthed,
       "extremeWirelessIntfRateAuthFailed": extremeWirelessIntfRateAuthFailed,
       "extremeWirelessIntfRateAssoc": extremeWirelessIntfRateAssoc,
       "extremeWirelessIntfRateAssocFailed": extremeWirelessIntfRateAssocFailed,
       "extremeWirelessIntfBlockTime": extremeWirelessIntfBlockTime,
       "extremeWirelessIntfCurrentDetected": extremeWirelessIntfCurrentDetected,
       "extremeWirelessIntfCurrentAuthed": extremeWirelessIntfCurrentAuthed,
       "extremeWirelessIntfCurrentAssoc": extremeWirelessIntfCurrentAssoc,
       "extremeWirelessIntfCurrentForwarding": extremeWirelessIntfCurrentForwarding,
       "extremeWirelessVirtInterfaceCtlTable": extremeWirelessVirtInterfaceCtlTable,
       "extremeWirelessVirtInterfaceCtlEntry": extremeWirelessVirtInterfaceCtlEntry,
       "extremeWirelessVirtInterfaceIndex": extremeWirelessVirtInterfaceIndex,
       "extremeWirelessVirtInterfaceMacAddress": extremeWirelessVirtInterfaceMacAddress,
       "extremeWirelessVirtInterfaceMaxClients": extremeWirelessVirtInterfaceMaxClients,
       "extremeWirelessVirtInterfaceWirelessBridging": extremeWirelessVirtInterfaceWirelessBridging,
       "extremeWirelessVirtInterfaceLastStateChange": extremeWirelessVirtInterfaceLastStateChange,
       "extremeWirelessVirtInterfaceState": extremeWirelessVirtInterfaceState,
       "extremeWirelessVirtInterfaceIappEnabled": extremeWirelessVirtInterfaceIappEnabled,
       "extremeWirelessVirtInterfaceSvpEnabled": extremeWirelessVirtInterfaceSvpEnabled,
       "extremeWirelessVirtInterfaceSecurityCtlTable": extremeWirelessVirtInterfaceSecurityCtlTable,
       "extremeWirelessVirtInterfaceSecurityCtlEntry": extremeWirelessVirtInterfaceSecurityCtlEntry,
       "extremeWirelessVirtInterfaceESSName": extremeWirelessVirtInterfaceESSName,
       "extremeWirelessVirtInterfaceSSIDInBeacon": extremeWirelessVirtInterfaceSSIDInBeacon,
       "extremeWirelessVirtInterfaceDot11AuthMode": extremeWirelessVirtInterfaceDot11AuthMode,
       "extremeWirelessVirtInterfaceNetworkAuthMode": extremeWirelessVirtInterfaceNetworkAuthMode,
       "extremeWirelessVirtInterfaceDataVlan": extremeWirelessVirtInterfaceDataVlan,
       "extremeWirelessVirtInterfaceIgnoreVSAVlan": extremeWirelessVirtInterfaceIgnoreVSAVlan,
       "extremeWirelessVirtInterfaceWEPDefaultKey": extremeWirelessVirtInterfaceWEPDefaultKey,
       "extremeWirelessVirtInterfaceEncryptionLength": extremeWirelessVirtInterfaceEncryptionLength,
       "extremeWirelessVirtInterfaceDot1xCtlTable": extremeWirelessVirtInterfaceDot1xCtlTable,
       "extremeWirelessVirtInterfaceDot1xCtlEntry": extremeWirelessVirtInterfaceDot1xCtlEntry,
       "extremeWirelessVirtInterfaceKeyMgmtSuite": extremeWirelessVirtInterfaceKeyMgmtSuite,
       "extremeWirelessVirtInterfaceMcastCipherSuite": extremeWirelessVirtInterfaceMcastCipherSuite,
       "extremeWirelessVirtInterfaceDot1xPSKValue": extremeWirelessVirtInterfaceDot1xPSKValue,
       "extremeWirelessVirtInterfaceDot1xPSKPassPhrase": extremeWirelessVirtInterfaceDot1xPSKPassPhrase,
       "extremeWirelessVirtInterfaceDot1xReAuthPeriod": extremeWirelessVirtInterfaceDot1xReAuthPeriod,
       "extremeWirelessVirtInterfaceGroupUpdateTimeOut": extremeWirelessVirtInterfaceGroupUpdateTimeOut,
       "extremeWirelessVirtInterfacePairwiseUpdateTimeOut": extremeWirelessVirtInterfacePairwiseUpdateTimeOut,
       "extremeWirelessVirtInterfaceDot11iPreauthEnable": extremeWirelessVirtInterfaceDot11iPreauthEnable,
       "extremeWirelessVirtInterfaceWEPKeyTable": extremeWirelessVirtInterfaceWEPKeyTable,
       "extremeWirelessVirtInterfaceWEPKeyEntry": extremeWirelessVirtInterfaceWEPKeyEntry,
       "extremeWirelessVirtInterfaceWEPKeyIndex": extremeWirelessVirtInterfaceWEPKeyIndex,
       "extremeWirelessVirtInterfaceWEPKey": extremeWirelessVirtInterfaceWEPKey,
       "extremeWirelessVirtInterfaceWEPKeyStatus": extremeWirelessVirtInterfaceWEPKeyStatus,
       "extremeWirelessPhysInterfaceRFCtlTable": extremeWirelessPhysInterfaceRFCtlTable,
       "extremeWirelessPhysInterfaceRFCtlEntry": extremeWirelessPhysInterfaceRFCtlEntry,
       "extremeWirelessPhysInterfaceBeaconPeriod": extremeWirelessPhysInterfaceBeaconPeriod,
       "extremeWirelessPhysInterfaceTxPowerLevel": extremeWirelessPhysInterfaceTxPowerLevel,
       "extremeWirelessPhysInterfaceDTIMPeriod": extremeWirelessPhysInterfaceDTIMPeriod,
       "extremeWirelessPhysInterfaceFragLength": extremeWirelessPhysInterfaceFragLength,
       "extremeWirelessPhysInterfaceLongRetry": extremeWirelessPhysInterfaceLongRetry,
       "extremeWirelessPhysInterfaceShortRetry": extremeWirelessPhysInterfaceShortRetry,
       "extremeWirelessPhysInterfaceRTSThreshold": extremeWirelessPhysInterfaceRTSThreshold,
       "extremeWirelessPhysInterfaceSupportedDataRatesRxValue": extremeWirelessPhysInterfaceSupportedDataRatesRxValue,
       "extremeWirelessPhysInterfaceSupportedDataRatesTxValue": extremeWirelessPhysInterfaceSupportedDataRatesTxValue,
       "extremeWirelessPhysInterfacePHYType": extremeWirelessPhysInterfacePHYType,
       "extremeWirelessPhysInterfacePHYSupportedTypes": extremeWirelessPhysInterfacePHYSupportedTypes,
       "extremeWirelessPhysInterfacePreamble": extremeWirelessPhysInterfacePreamble,
       "extremeWirelessPhysInterfaceAbsTxPowerLevel": extremeWirelessPhysInterfaceAbsTxPowerLevel,
       "extremeWirelessClientTable": extremeWirelessClientTable,
       "extremeWirelessClientEntry": extremeWirelessClientEntry,
       "extremeWirelessClientID": extremeWirelessClientID,
       "extremeWirelessClientState": extremeWirelessClientState,
       "extremeWirelessClientEncryption": extremeWirelessClientEncryption,
       "extremeWirelessClientSignalStrength": extremeWirelessClientSignalStrength,
       "extremeWirelessClientLinkQuality": extremeWirelessClientLinkQuality,
       "extremeWirelessClientVLAN": extremeWirelessClientVLAN,
       "extremeWirelessClientPriority": extremeWirelessClientPriority,
       "extremeWirelessClientAuthType": extremeWirelessClientAuthType,
       "extremeWirelessClientLastStateChangeTime": extremeWirelessClientLastStateChangeTime,
       "extremeWirelessClientTxFrames": extremeWirelessClientTxFrames,
       "extremeWirelessClientRxFrames": extremeWirelessClientRxFrames,
       "extremeWirelessClientTxBytes": extremeWirelessClientTxBytes,
       "extremeWirelessClientRxBytes": extremeWirelessClientRxBytes,
       "extremeWirelessClientLastPacketType": extremeWirelessClientLastPacketType,
       "extremeWirelessClientSSID": extremeWirelessClientSSID,
       "extremeWirelessClientStatus": extremeWirelessClientStatus,
       "extremeWirelessClientIP": extremeWirelessClientIP,
       "extremeWirelessClientUsername": extremeWirelessClientUsername,
       "extremeWirelessClientDecryptionFailures": extremeWirelessClientDecryptionFailures,
       "extremeWirelessClientMICFailures": extremeWirelessClientMICFailures,
       "extremeAPAuthServerTable": extremeAPAuthServerTable,
       "extremeAPAuthServerEntry": extremeAPAuthServerEntry,
       "extremeAPAuthServerIndex": extremeAPAuthServerIndex,
       "extremeAPAuthServerAddressType": extremeAPAuthServerAddressType,
       "extremeAPAuthServerAddress": extremeAPAuthServerAddress,
       "extremeAPAuthServerPort": extremeAPAuthServerPort,
       "extremeAPAuthServerSecret": extremeAPAuthServerSecret,
       "extremeAPAuthServerReTransmit": extremeAPAuthServerReTransmit,
       "extremeAPAuthServerStatus": extremeAPAuthServerStatus,
       "extremeWirelessScanCfgTable": extremeWirelessScanCfgTable,
       "extremeWirelessScanCfgEntry": extremeWirelessScanCfgEntry,
       "extremeWirelessScanEnable": extremeWirelessScanEnable,
       "extremeWirelessScanSendProbe": extremeWirelessScanSendProbe,
       "extremeWirelessScanProbeInterval": extremeWirelessScanProbeInterval,
       "extremeWirelessScanResultTableSize": extremeWirelessScanResultTableSize,
       "extremeWirelessScanResultTimeout": extremeWirelessScanResultTimeout,
       "extremeWirelessScanResetStats": extremeWirelessScanResetStats,
       "extremeWirelessScanClearTable": extremeWirelessScanClearTable,
       "extremeWirelessScanSendAPAddedTrap": extremeWirelessScanSendAPAddedTrap,
       "extremeWirelessScanSendAPRemovedTrap": extremeWirelessScanSendAPRemovedTrap,
       "extremeWirelessScanSendAPUpdatedTrap": extremeWirelessScanSendAPUpdatedTrap,
       "extremeWirelessOffChannelScanCfgTable": extremeWirelessOffChannelScanCfgTable,
       "extremeWirelessOffChannelScanCfgEntry": extremeWirelessOffChannelScanCfgEntry,
       "extremeWirelessOffChannelScanStart": extremeWirelessOffChannelScanStart,
       "extremeWirelessOffChannelScanList": extremeWirelessOffChannelScanList,
       "extremeWirelessOffChannelScanMinWait": extremeWirelessOffChannelScanMinWait,
       "extremeWirelessOffChannelScanMaxWait": extremeWirelessOffChannelScanMaxWait,
       "extremeWirelessOffChannelContinuous": extremeWirelessOffChannelContinuous,
       "extremeWirelessScanStatusTable": extremeWirelessScanStatusTable,
       "extremeWirelessScanStatusEntry": extremeWirelessScanStatusEntry,
       "extremeWirelessScanCurrentTableSize": extremeWirelessScanCurrentTableSize,
       "extremeWirelessScanTableWatermark": extremeWirelessScanTableWatermark,
       "extremeWirelessScanTotalOverflows": extremeWirelessScanTotalOverflows,
       "extremeWirelessScanTotalTimeouts": extremeWirelessScanTotalTimeouts,
       "extremeWirelessScanOffChannelRunning": extremeWirelessScanOffChannelRunning,
       "extremeWirelessScanCurrentChannel": extremeWirelessScanCurrentChannel,
       "extremeWirelessScanLastElement": extremeWirelessScanLastElement,
       "extremeWirelessScanNumProbes": extremeWirelessScanNumProbes,
       "extremeWirelessScanResultsTable": extremeWirelessScanResultsTable,
       "extremeWirelessScanResultsEntry": extremeWirelessScanResultsEntry,
       "extremeWirelessScanResultsStationId": extremeWirelessScanResultsStationId,
       "extremeWirelessScanResultsFirstSeen": extremeWirelessScanResultsFirstSeen,
       "extremeWirelessScanResultsLastChange": extremeWirelessScanResultsLastChange,
       "extremeWirelessScanResultsPacketTime": extremeWirelessScanResultsPacketTime,
       "extremeWirelessScanResultsPacketRate": extremeWirelessScanResultsPacketRate,
       "extremeWirelessScanResultsChannel": extremeWirelessScanResultsChannel,
       "extremeWirelessScanResultsMinRSS": extremeWirelessScanResultsMinRSS,
       "extremeWirelessScanResultsMaxRSS": extremeWirelessScanResultsMaxRSS,
       "extremeWirelessScanResultsAvgRSS": extremeWirelessScanResultsAvgRSS,
       "extremeWirelessScanResultsTotalBeacons": extremeWirelessScanResultsTotalBeacons,
       "extremeWirelessScanResultsTotalProbes": extremeWirelessScanResultsTotalProbes,
       "extremeWirelessScanResultsDiscoveredBy": extremeWirelessScanResultsDiscoveredBy,
       "extremeWirelessScanResultsDSSOFDM": extremeWirelessScanResultsDSSOFDM,
       "extremeWirelessScanResultsRSNEnabled": extremeWirelessScanResultsRSNEnabled,
       "extremeWirelessScanResultsGShortSlot": extremeWirelessScanResultsGShortSlot,
       "extremeWirelessScanResultsChannelAgility": extremeWirelessScanResultsChannelAgility,
       "extremeWirelessScanResultsPBCC": extremeWirelessScanResultsPBCC,
       "extremeWirelessScanResultsPreamble": extremeWirelessScanResultsPreamble,
       "extremeWirelessScanResultsPrivacy": extremeWirelessScanResultsPrivacy,
       "extremeWirelessScanResultsCFPollReq": extremeWirelessScanResultsCFPollReq,
       "extremeWirelessScanResultsCFPollable": extremeWirelessScanResultsCFPollable,
       "extremeWirelessScanResultsNetworkType": extremeWirelessScanResultsNetworkType,
       "extremeWirelessScanResultsSSID": extremeWirelessScanResultsSSID,
       "extremeWirelessScanResultsRateSet": extremeWirelessScanResultsRateSet,
       "extremeWirelessScanResultsExtRateSet": extremeWirelessScanResultsExtRateSet,
       "extremeWirelessScanResultsDSSParameter": extremeWirelessScanResultsDSSParameter,
       "extremeWirelessScanResultsTIMCount": extremeWirelessScanResultsTIMCount,
       "extremeWirelessScanResultsTIMPeriod": extremeWirelessScanResultsTIMPeriod,
       "extremeWirelessScanResultsTIMTrafficInd": extremeWirelessScanResultsTIMTrafficInd,
       "extremeWirelessScanResultsCountryCode": extremeWirelessScanResultsCountryCode,
       "extremeWirelessScanWPAIEPresent": extremeWirelessScanWPAIEPresent,
       "extremeWirelessScanWPAVersion": extremeWirelessScanWPAVersion,
       "extremeWirelessScanWPAIEMcastCipher": extremeWirelessScanWPAIEMcastCipher,
       "extremeWirelessScanWPAUcastCipherCount": extremeWirelessScanWPAUcastCipherCount,
       "extremeWirelessScanWPAUcastCipher": extremeWirelessScanWPAUcastCipher,
       "extremeWirelessScanWPAKeyMgmtCount": extremeWirelessScanWPAKeyMgmtCount,
       "extremeWirelessScanWPAKeyMgmtSuite": extremeWirelessScanWPAKeyMgmtSuite,
       "extremeWirelessScanResultsIEBlob": extremeWirelessScanResultsIEBlob,
       "extremeWirelessProbeInfoCfgTable": extremeWirelessProbeInfoCfgTable,
       "extremeWirelessProbeInfoCfgEntry": extremeWirelessProbeInfoCfgEntry,
       "extremeWirelessProbeInfoEnable": extremeWirelessProbeInfoEnable,
       "extremeWirelessProbeInfoKeepIEs": extremeWirelessProbeInfoKeepIEs,
       "extremeWirelessProbeInfoTableSize": extremeWirelessProbeInfoTableSize,
       "extremeWirelessProbeInfoTimeout": extremeWirelessProbeInfoTimeout,
       "extremeWirelessProbeInfoTableClear": extremeWirelessProbeInfoTableClear,
       "extremeWirelessProbeInfoSourceClear": extremeWirelessProbeInfoSourceClear,
       "extremeWirelessProbeInfoTableStatsClear": extremeWirelessProbeInfoTableStatsClear,
       "extremeWirelessProbeInfoSourceStatsClear": extremeWirelessProbeInfoSourceStatsClear,
       "extremeWirelessProbeInfoSendAddedTrap": extremeWirelessProbeInfoSendAddedTrap,
       "extremeWirelessProbeInfoSendRemovedTrap": extremeWirelessProbeInfoSendRemovedTrap,
       "extremeWirelessProbeInfoStatusTable": extremeWirelessProbeInfoStatusTable,
       "extremeWirelessProbeInfoStatusEntry": extremeWirelessProbeInfoStatusEntry,
       "extremeWirelessProbeInfoStatusCurrentTableSize": extremeWirelessProbeInfoStatusCurrentTableSize,
       "extremeWirelessProbeInfoStatusWatermark": extremeWirelessProbeInfoStatusWatermark,
       "extremeWirelessProbeInfoStatusTotalOverflows": extremeWirelessProbeInfoStatusTotalOverflows,
       "extremeWirelessProbeInfoStatusTotalTimeouts": extremeWirelessProbeInfoStatusTotalTimeouts,
       "extremeWirelessProbeInfoStatusLastElement": extremeWirelessProbeInfoStatusLastElement,
       "extremeWirelessProbeInfoStatusTotalProbes": extremeWirelessProbeInfoStatusTotalProbes,
       "extremeWirelessProbeInfoTable": extremeWirelessProbeInfoTable,
       "extremeWirelessProbeInfoEntry": extremeWirelessProbeInfoEntry,
       "extremeWirelessProbeInfoSource": extremeWirelessProbeInfoSource,
       "extremeWirelessProbeInfoTotalProbes": extremeWirelessProbeInfoTotalProbes,
       "extremeWirelessProbeInfoTotalProbeResp": extremeWirelessProbeInfoTotalProbeResp,
       "extremeWirelessProbeInfoRateIESize": extremeWirelessProbeInfoRateIESize,
       "extremeWirelessProbeInfoRateIE": extremeWirelessProbeInfoRateIE,
       "extremeWirelessProbeInfoFirstSeen": extremeWirelessProbeInfoFirstSeen,
       "extremeWirelessProbeInfoLastChange": extremeWirelessProbeInfoLastChange,
       "extremeWirelessProbeInfoLastRSS": extremeWirelessProbeInfoLastRSS,
       "extremeWirelessProbeInfoLastRate": extremeWirelessProbeInfoLastRate,
       "extremeWirelessProbeInfoLastChannel": extremeWirelessProbeInfoLastChannel,
       "extremeWirelessClientDiagCfgTable": extremeWirelessClientDiagCfgTable,
       "extremeWirelessClientDiagCfgEntry": extremeWirelessClientDiagCfgEntry,
       "extremeWirelessClientDiagCfgEnable": extremeWirelessClientDiagCfgEnable,
       "extremeWirelessClientDiagCfgClearClient": extremeWirelessClientDiagCfgClearClient,
       "extremeWirelessClientDiagCfgTableSize": extremeWirelessClientDiagCfgTableSize,
       "extremeWirelessClientDiagCfgTimeout": extremeWirelessClientDiagCfgTimeout,
       "extremeWirelessClientDiagStatusTable": extremeWirelessClientDiagStatusTable,
       "extremeWirelessClientDiagStatusEntry": extremeWirelessClientDiagStatusEntry,
       "extremeWirelessClientDiagCurrentTableSize": extremeWirelessClientDiagCurrentTableSize,
       "extremeWirelessClientDiagTableWatermark": extremeWirelessClientDiagTableWatermark,
       "extremeWirelessClientDiagTotalOverflows": extremeWirelessClientDiagTotalOverflows,
       "extremeWirelessClientDiagTotalTimeouts": extremeWirelessClientDiagTotalTimeouts,
       "extremeWirelessClientDiagLastElement": extremeWirelessClientDiagLastElement,
       "extremeWirelessClientDiagSupportsSpeedCounters": extremeWirelessClientDiagSupportsSpeedCounters,
       "extremeWirelessClientDiagSupportsSizeCounters": extremeWirelessClientDiagSupportsSizeCounters,
       "extremeWirelessClientDiagSupportsPacketCounters": extremeWirelessClientDiagSupportsPacketCounters,
       "extremeWirelessClientDiagTable": extremeWirelessClientDiagTable,
       "extremeWirelessClientDiagEntry": extremeWirelessClientDiagEntry,
       "extremeWirelessClientDiagMac": extremeWirelessClientDiagMac,
       "extremeWirelessClientDiagStateWatermark": extremeWirelessClientDiagStateWatermark,
       "extremeWirelessClientDiagEntersInDetected": extremeWirelessClientDiagEntersInDetected,
       "extremeWirelessClientDiagErrorsInDetected": extremeWirelessClientDiagErrorsInDetected,
       "extremeWirelessClientDiagAuthReqInDetected": extremeWirelessClientDiagAuthReqInDetected,
       "extremeWirelessClientDiagOtherReqInDetected": extremeWirelessClientDiagOtherReqInDetected,
       "extremeWirelessClientDiagMgmtActionInDetected": extremeWirelessClientDiagMgmtActionInDetected,
       "extremeWirelessClientDiagTimeOutInDetected": extremeWirelessClientDiagTimeOutInDetected,
       "extremeWirelessClientDiagEntersInAuth": extremeWirelessClientDiagEntersInAuth,
       "extremeWirelessClientDiagErrorsInAuth": extremeWirelessClientDiagErrorsInAuth,
       "extremeWirelessClientDiagAssocReqInAuth": extremeWirelessClientDiagAssocReqInAuth,
       "extremeWirelessClientDiagOtherReqInAuth": extremeWirelessClientDiagOtherReqInAuth,
       "extremeWirelessClientDiagMgmtActionInAuth": extremeWirelessClientDiagMgmtActionInAuth,
       "extremeWirelessClientDiagTimeOutInAuth": extremeWirelessClientDiagTimeOutInAuth,
       "extremeWirelessClientDiagEntersInAssoc": extremeWirelessClientDiagEntersInAssoc,
       "extremeWirelessClientDiagErrorsInAssoc": extremeWirelessClientDiagErrorsInAssoc,
       "extremeWirelessClientDiagMgmtActionInAssoc": extremeWirelessClientDiagMgmtActionInAssoc,
       "extremeWirelessClientDiagTimeOutInAssoc": extremeWirelessClientDiagTimeOutInAssoc,
       "extremeWirelessClientDiagEntersInForward": extremeWirelessClientDiagEntersInForward,
       "extremeWirelessClientDiagMgmtActionInForward": extremeWirelessClientDiagMgmtActionInForward,
       "extremeWirelessClientDiagTimeOutInForward": extremeWirelessClientDiagTimeOutInForward,
       "extremeWirelessClientDiagTotal802Auths": extremeWirelessClientDiagTotal802Auths,
       "extremeWirelessClientDiagTotalNetLoginAuths": extremeWirelessClientDiagTotalNetLoginAuths,
       "extremeWirelessClientAssocInfoTable": extremeWirelessClientAssocInfoTable,
       "extremeWirelessClientAssocInfoEntry": extremeWirelessClientAssocInfoEntry,
       "extremeWirelessClientAssocInfoAssociated": extremeWirelessClientAssocInfoAssociated,
       "extremeWirelessClientAssocInfoTotalAssocReq": extremeWirelessClientAssocInfoTotalAssocReq,
       "extremeWirelessClientAssocInfoTotalReAssocReq": extremeWirelessClientAssocInfoTotalReAssocReq,
       "extremeWirelessClientAssocInfoTotalAssocResp": extremeWirelessClientAssocInfoTotalAssocResp,
       "extremeWirelessClientAssocInfoTotalAssocOK": extremeWirelessClientAssocInfoTotalAssocOK,
       "extremeWirelessClientAssocInfoTotalAssocFail": extremeWirelessClientAssocInfoTotalAssocFail,
       "extremeWirelessClientAssocInfoTotalDisassocReq": extremeWirelessClientAssocInfoTotalDisassocReq,
       "extremeWirelessClientAssocInfoTotalDisassocResp": extremeWirelessClientAssocInfoTotalDisassocResp,
       "extremeWirelessClientAssocInfoRateIE": extremeWirelessClientAssocInfoRateIE,
       "extremeWirelessClientAssocInfoLastAssoc": extremeWirelessClientAssocInfoLastAssoc,
       "extremeWirelessClientAssocInfoLastError": extremeWirelessClientAssocInfoLastError,
       "extremeWirelessClientAssocInfoLastErrorType": extremeWirelessClientAssocInfoLastErrorType,
       "extremeWirelessClientAssocInfoErrorRateMismatch": extremeWirelessClientAssocInfoErrorRateMismatch,
       "extremeWirelessClientAssocInfoErrorBadState": extremeWirelessClientAssocInfoErrorBadState,
       "extremeWirelessClientAssocInfoErrorBadCapability": extremeWirelessClientAssocInfoErrorBadCapability,
       "extremeWirelessClientAssocInfoErrorCounterMeasure": extremeWirelessClientAssocInfoErrorCounterMeasure,
       "extremeWirelessClientAssocInfoErrorMcastCipher": extremeWirelessClientAssocInfoErrorMcastCipher,
       "extremeWirelessClientAssocInfoErrorMaxAssoc": extremeWirelessClientAssocInfoErrorMaxAssoc,
       "extremeWirelessClientAssocInfoErrorRSNRequired": extremeWirelessClientAssocInfoErrorRSNRequired,
       "extremeWirelessClientAssocInfoErrorRSNMismatch": extremeWirelessClientAssocInfoErrorRSNMismatch,
       "extremeWirelessClientAssocInfoErrorOther": extremeWirelessClientAssocInfoErrorOther,
       "extremeWirelessClientAssocInfoWPAIEPresent": extremeWirelessClientAssocInfoWPAIEPresent,
       "extremeWirelessClientAssocInfoWPAVersion": extremeWirelessClientAssocInfoWPAVersion,
       "extremeWirelessClientAssocInfoWPAIEMcastCipher": extremeWirelessClientAssocInfoWPAIEMcastCipher,
       "extremeWirelessClientAssocInfoWPAUcastCipherCount": extremeWirelessClientAssocInfoWPAUcastCipherCount,
       "extremeWirelessClientAssocInfoWPAUcastCipher": extremeWirelessClientAssocInfoWPAUcastCipher,
       "extremeWirelessClientAssocInfoWPAKeyMgmtCount": extremeWirelessClientAssocInfoWPAKeyMgmtCount,
       "extremeWirelessClientAssocInfoWPAKeyMgmtSuite": extremeWirelessClientAssocInfoWPAKeyMgmtSuite,
       "extremeWirelessClientAssocIEBlob": extremeWirelessClientAssocIEBlob,
       "extremeWirelessClientAuthInfoTable": extremeWirelessClientAuthInfoTable,
       "extremeWirelessClientAuthInfoEntry": extremeWirelessClientAuthInfoEntry,
       "extremeWirelessClientAuthInfoCurrentAuth": extremeWirelessClientAuthInfoCurrentAuth,
       "extremeWirelessClientAuthInfoTotalAuths": extremeWirelessClientAuthInfoTotalAuths,
       "extremeWirelessClientAuthInfoTotalAuthResp": extremeWirelessClientAuthInfoTotalAuthResp,
       "extremeWirelessClientAuthInfoTotalAuthsOK": extremeWirelessClientAuthInfoTotalAuthsOK,
       "extremeWirelessClientAuthInfoTotalAuthsFailed": extremeWirelessClientAuthInfoTotalAuthsFailed,
       "extremeWirelessClientAuthInfoTotalDeauthReq": extremeWirelessClientAuthInfoTotalDeauthReq,
       "extremeWirelessClientAuthInfoTotalDeauthResp": extremeWirelessClientAuthInfoTotalDeauthResp,
       "extremeWirelessClientAuthInfoTotalOpen": extremeWirelessClientAuthInfoTotalOpen,
       "extremeWirelessClientAuthInfoTotalShared": extremeWirelessClientAuthInfoTotalShared,
       "extremeWirelessClientAuthInfoLastAuth": extremeWirelessClientAuthInfoLastAuth,
       "extremeWirelessClientAuthInfoLastAuthType": extremeWirelessClientAuthInfoLastAuthType,
       "extremeWirelessClientAuthInfoLastError": extremeWirelessClientAuthInfoLastError,
       "extremeWirelessClientAuthInfoLastErrorType": extremeWirelessClientAuthInfoLastErrorType,
       "extremeWirelessClientAuthInfoErrorResourceFailure": extremeWirelessClientAuthInfoErrorResourceFailure,
       "extremeWirelessClientAuthInfoErrorSequenceNum": extremeWirelessClientAuthInfoErrorSequenceNum,
       "extremeWirelessClientAuthInfoErrorChallengeText": extremeWirelessClientAuthInfoErrorChallengeText,
       "extremeWirelessClientAuthInfoErrorTypeMismatch": extremeWirelessClientAuthInfoErrorTypeMismatch,
       "extremeWirelessClientAuthInfoErrorKeyIndex": extremeWirelessClientAuthInfoErrorKeyIndex,
       "extremeWirelessClientAuthInfoErrorOther": extremeWirelessClientAuthInfoErrorOther,
       "extremeWirelessClientMACInfoTable": extremeWirelessClientMACInfoTable,
       "extremeWirelessClientMACInfoEntry": extremeWirelessClientMACInfoEntry,
       "extremeWirelessClientMACInfoMinRSS": extremeWirelessClientMACInfoMinRSS,
       "extremeWirelessClientMACInfoMaxRSS": extremeWirelessClientMACInfoMaxRSS,
       "extremeWirelessClientMACInfoAvgRSS": extremeWirelessClientMACInfoAvgRSS,
       "extremeWirelessClientMACInfoTotalProbeReq": extremeWirelessClientMACInfoTotalProbeReq,
       "extremeWirelessClientMACInfoTotalAuthReq": extremeWirelessClientMACInfoTotalAuthReq,
       "extremeWirelessClientMACInfoTotalAssocReq": extremeWirelessClientMACInfoTotalAssocReq,
       "extremeWirelessClientMACInfoTotalReAssocReq": extremeWirelessClientMACInfoTotalReAssocReq,
       "extremeWirelessClientMACInfoTotalDeAssocReq": extremeWirelessClientMACInfoTotalDeAssocReq,
       "extremeWirelessClientMACInfoTotalDeAuthReq": extremeWirelessClientMACInfoTotalDeAuthReq,
       "extremeWirelessClientMACInfoTotalPsPoll": extremeWirelessClientMACInfoTotalPsPoll,
       "extremeWirelessClientMACInfoTotalData": extremeWirelessClientMACInfoTotalData,
       "extremeWirelessClientMACInfoNavValue": extremeWirelessClientMACInfoNavValue,
       "extremeWirelessClientSizeCounterTable": extremeWirelessClientSizeCounterTable,
       "extremeWirelessClientSizeCounterEntry": extremeWirelessClientSizeCounterEntry,
       "extremeWirelessClientFrameSizeReXmit64": extremeWirelessClientFrameSizeReXmit64,
       "extremeWirelessClientFrameSizeReXmit128": extremeWirelessClientFrameSizeReXmit128,
       "extremeWirelessClientFrameSizeReXmit256": extremeWirelessClientFrameSizeReXmit256,
       "extremeWirelessClientFrameSizeReXmit512": extremeWirelessClientFrameSizeReXmit512,
       "extremeWirelessClientFrameSizeReXmit1024": extremeWirelessClientFrameSizeReXmit1024,
       "extremeWirelessClientFrameSizeReXmit2048": extremeWirelessClientFrameSizeReXmit2048,
       "extremeWirelessClientFrameSizeTX64": extremeWirelessClientFrameSizeTX64,
       "extremeWirelessClientFrameSizeTX128": extremeWirelessClientFrameSizeTX128,
       "extremeWirelessClientFrameSizeTX256": extremeWirelessClientFrameSizeTX256,
       "extremeWirelessClientFrameSizeTX512": extremeWirelessClientFrameSizeTX512,
       "extremeWirelessClientFrameSizeTX1024": extremeWirelessClientFrameSizeTX1024,
       "extremeWirelessClientFrameSizeTX2048": extremeWirelessClientFrameSizeTX2048,
       "extremeWirelessClientFrameSizeRX64": extremeWirelessClientFrameSizeRX64,
       "extremeWirelessClientFrameSizeRX128": extremeWirelessClientFrameSizeRX128,
       "extremeWirelessClientFrameSizeRX256": extremeWirelessClientFrameSizeRX256,
       "extremeWirelessClientFrameSizeRX512": extremeWirelessClientFrameSizeRX512,
       "extremeWirelessClientFrameSizeRX1024": extremeWirelessClientFrameSizeRX1024,
       "extremeWirelessClientFrameSizeRX2048": extremeWirelessClientFrameSizeRX2048,
       "extremeWirelessClientFrameSizeErrorTX64": extremeWirelessClientFrameSizeErrorTX64,
       "extremeWirelessClientFrameSizeErrorTX128": extremeWirelessClientFrameSizeErrorTX128,
       "extremeWirelessClientFrameSizeErrorTX256": extremeWirelessClientFrameSizeErrorTX256,
       "extremeWirelessClientFrameSizeErrorTX512": extremeWirelessClientFrameSizeErrorTX512,
       "extremeWirelessClientFrameSizeErrorTX1024": extremeWirelessClientFrameSizeErrorTX1024,
       "extremeWirelessClientFrameSizeErrorTX2048": extremeWirelessClientFrameSizeErrorTX2048,
       "extremeWirelessClientFrameSizeErrorRX64": extremeWirelessClientFrameSizeErrorRX64,
       "extremeWirelessClientFrameSizeErrorRX128": extremeWirelessClientFrameSizeErrorRX128,
       "extremeWirelessClientFrameSizeErrorRX256": extremeWirelessClientFrameSizeErrorRX256,
       "extremeWirelessClientFrameSizeErrorRX512": extremeWirelessClientFrameSizeErrorRX512,
       "extremeWirelessClientFrameSizeErrorRX1024": extremeWirelessClientFrameSizeErrorRX1024,
       "extremeWirelessClientFrameSizeErrorRX2048": extremeWirelessClientFrameSizeErrorRX2048,
       "extremeWirelessClientPacketSizeTX64": extremeWirelessClientPacketSizeTX64,
       "extremeWirelessClientPacketSizeTX128": extremeWirelessClientPacketSizeTX128,
       "extremeWirelessClientPacketSizeTX256": extremeWirelessClientPacketSizeTX256,
       "extremeWirelessClientPacketSizeTX512": extremeWirelessClientPacketSizeTX512,
       "extremeWirelessClientPacketSizeTX1024": extremeWirelessClientPacketSizeTX1024,
       "extremeWirelessClientPacketSizeTX2048": extremeWirelessClientPacketSizeTX2048,
       "extremeWirelessClientPacketSizeRX64": extremeWirelessClientPacketSizeRX64,
       "extremeWirelessClientPacketSizeRX128": extremeWirelessClientPacketSizeRX128,
       "extremeWirelessClientPacketSizeRX256": extremeWirelessClientPacketSizeRX256,
       "extremeWirelessClientPacketSizeRX512": extremeWirelessClientPacketSizeRX512,
       "extremeWirelessClientPacketSizeRX1024": extremeWirelessClientPacketSizeRX1024,
       "extremeWirelessClientPacketSizeRX2048": extremeWirelessClientPacketSizeRX2048,
       "extremeWirelessClientSpeedCounterTable": extremeWirelessClientSpeedCounterTable,
       "extremeWirelessClientSpeedCounterEntry": extremeWirelessClientSpeedCounterEntry,
       "extremeWirelessClientSpeedReXmit1": extremeWirelessClientSpeedReXmit1,
       "extremeWirelessClientSpeedReXmit2": extremeWirelessClientSpeedReXmit2,
       "extremeWirelessClientSpeedReXmit5p5": extremeWirelessClientSpeedReXmit5p5,
       "extremeWirelessClientSpeedReXmit6": extremeWirelessClientSpeedReXmit6,
       "extremeWirelessClientSpeedReXmit9": extremeWirelessClientSpeedReXmit9,
       "extremeWirelessClientSpeedReXmit12": extremeWirelessClientSpeedReXmit12,
       "extremeWirelessClientSpeedReXmit18": extremeWirelessClientSpeedReXmit18,
       "extremeWirelessClientSpeedReXmit24": extremeWirelessClientSpeedReXmit24,
       "extremeWirelessClientSpeedReXmit36": extremeWirelessClientSpeedReXmit36,
       "extremeWirelessClientSpeedReXmit48": extremeWirelessClientSpeedReXmit48,
       "extremeWirelessClientSpeedReXmit54": extremeWirelessClientSpeedReXmit54,
       "extremeWirelessClientSpeedTX1": extremeWirelessClientSpeedTX1,
       "extremeWirelessClientSpeedTX2": extremeWirelessClientSpeedTX2,
       "extremeWirelessClientSpeedTX5p5": extremeWirelessClientSpeedTX5p5,
       "extremeWirelessClientSpeedTX6": extremeWirelessClientSpeedTX6,
       "extremeWirelessClientSpeedTX9": extremeWirelessClientSpeedTX9,
       "extremeWirelessClientSpeedTX12": extremeWirelessClientSpeedTX12,
       "extremeWirelessClientSpeedTX18": extremeWirelessClientSpeedTX18,
       "extremeWirelessClientSpeedTX24": extremeWirelessClientSpeedTX24,
       "extremeWirelessClientSpeedTX36": extremeWirelessClientSpeedTX36,
       "extremeWirelessClientSpeedTX48": extremeWirelessClientSpeedTX48,
       "extremeWirelessClientSpeedTX54": extremeWirelessClientSpeedTX54,
       "extremeWirelessClientSpeedRX1": extremeWirelessClientSpeedRX1,
       "extremeWirelessClientSpeedRX2": extremeWirelessClientSpeedRX2,
       "extremeWirelessClientSpeedRX5p5": extremeWirelessClientSpeedRX5p5,
       "extremeWirelessClientSpeedRX6": extremeWirelessClientSpeedRX6,
       "extremeWirelessClientSpeedRX9": extremeWirelessClientSpeedRX9,
       "extremeWirelessClientSpeedRX12": extremeWirelessClientSpeedRX12,
       "extremeWirelessClientSpeedRX18": extremeWirelessClientSpeedRX18,
       "extremeWirelessClientSpeedRX24": extremeWirelessClientSpeedRX24,
       "extremeWirelessClientSpeedRX36": extremeWirelessClientSpeedRX36,
       "extremeWirelessClientSpeedRX48": extremeWirelessClientSpeedRX48,
       "extremeWirelessClientSpeedRX54": extremeWirelessClientSpeedRX54,
       "extremeWirelessIntfFrameSizeTable": extremeWirelessIntfFrameSizeTable,
       "extremeWirelessIntfFrameSizeEntry": extremeWirelessIntfFrameSizeEntry,
       "extremeWirelessIntfFrameSizeMgmtTX64": extremeWirelessIntfFrameSizeMgmtTX64,
       "extremeWirelessIntfFrameSizeMgmtTX128": extremeWirelessIntfFrameSizeMgmtTX128,
       "extremeWirelessIntfFrameSizeMgmtTX256": extremeWirelessIntfFrameSizeMgmtTX256,
       "extremeWirelessIntfFrameSizeMgmtTX512": extremeWirelessIntfFrameSizeMgmtTX512,
       "extremeWirelessIntfFrameSizeMgmtTX1024": extremeWirelessIntfFrameSizeMgmtTX1024,
       "extremeWirelessIntfFrameSizeMgmtTX2048": extremeWirelessIntfFrameSizeMgmtTX2048,
       "extremeWirelessIntfFrameSizeMgmtRX64": extremeWirelessIntfFrameSizeMgmtRX64,
       "extremeWirelessIntfFrameSizeMgmtRX128": extremeWirelessIntfFrameSizeMgmtRX128,
       "extremeWirelessIntfFrameSizeMgmtRX256": extremeWirelessIntfFrameSizeMgmtRX256,
       "extremeWirelessIntfFrameSizeMgmtRX512": extremeWirelessIntfFrameSizeMgmtRX512,
       "extremeWirelessIntfFrameSizeMgmtRX1024": extremeWirelessIntfFrameSizeMgmtRX1024,
       "extremeWirelessIntfFrameSizeMgmtRX2048": extremeWirelessIntfFrameSizeMgmtRX2048,
       "extremeWirelessIntfFrameSizeCtlTX64": extremeWirelessIntfFrameSizeCtlTX64,
       "extremeWirelessIntfFrameSizeCtlTX128": extremeWirelessIntfFrameSizeCtlTX128,
       "extremeWirelessIntfFrameSizeCtlTX256": extremeWirelessIntfFrameSizeCtlTX256,
       "extremeWirelessIntfFrameSizeCtlTX512": extremeWirelessIntfFrameSizeCtlTX512,
       "extremeWirelessIntfFrameSizeCtlTX1024": extremeWirelessIntfFrameSizeCtlTX1024,
       "extremeWirelessIntfFrameSizeCtlTX2048": extremeWirelessIntfFrameSizeCtlTX2048,
       "extremeWirelessIntfFrameSizeCtlRX64": extremeWirelessIntfFrameSizeCtlRX64,
       "extremeWirelessIntfFrameSizeCtlRX128": extremeWirelessIntfFrameSizeCtlRX128,
       "extremeWirelessIntfFrameSizeCtlRX256": extremeWirelessIntfFrameSizeCtlRX256,
       "extremeWirelessIntfFrameSizeCtlRX512": extremeWirelessIntfFrameSizeCtlRX512,
       "extremeWirelessIntfFrameSizeCtlRX1024": extremeWirelessIntfFrameSizeCtlRX1024,
       "extremeWirelessIntfFrameSizeCtlRX2048": extremeWirelessIntfFrameSizeCtlRX2048,
       "extremeWirelessIntfFrameSizeDataTX64": extremeWirelessIntfFrameSizeDataTX64,
       "extremeWirelessIntfFrameSizeDataTX128": extremeWirelessIntfFrameSizeDataTX128,
       "extremeWirelessIntfFrameSizeDataTX256": extremeWirelessIntfFrameSizeDataTX256,
       "extremeWirelessIntfFrameSizeDataTX512": extremeWirelessIntfFrameSizeDataTX512,
       "extremeWirelessIntfFrameSizeDataTX1024": extremeWirelessIntfFrameSizeDataTX1024,
       "extremeWirelessIntfFrameSizeDataTX2048": extremeWirelessIntfFrameSizeDataTX2048,
       "extremeWirelessIntfFrameSizeDataRX64": extremeWirelessIntfFrameSizeDataRX64,
       "extremeWirelessIntfFrameSizeDataRX128": extremeWirelessIntfFrameSizeDataRX128,
       "extremeWirelessIntfFrameSizeDataRX256": extremeWirelessIntfFrameSizeDataRX256,
       "extremeWirelessIntfFrameSizeDataRX512": extremeWirelessIntfFrameSizeDataRX512,
       "extremeWirelessIntfFrameSizeDataRX1024": extremeWirelessIntfFrameSizeDataRX1024,
       "extremeWirelessIntfFrameSizeDataRX2048": extremeWirelessIntfFrameSizeDataRX2048,
       "extremeWirelessIntfFrameSizeErrorTable": extremeWirelessIntfFrameSizeErrorTable,
       "extremeWirelessIntfFrameSizeErrorEntry": extremeWirelessIntfFrameSizeErrorEntry,
       "extremeWirelessIntfFrameSizeReXmit64": extremeWirelessIntfFrameSizeReXmit64,
       "extremeWirelessIntfFrameSizeReXmit128": extremeWirelessIntfFrameSizeReXmit128,
       "extremeWirelessIntfFrameSizeReXmit256": extremeWirelessIntfFrameSizeReXmit256,
       "extremeWirelessIntfFrameSizeReXmit512": extremeWirelessIntfFrameSizeReXmit512,
       "extremeWirelessIntfFrameSizeReXmit1024": extremeWirelessIntfFrameSizeReXmit1024,
       "extremeWirelessIntfFrameSizeReXmit2048": extremeWirelessIntfFrameSizeReXmit2048,
       "extremeWirelessIntfFrameSizeErrorTX64": extremeWirelessIntfFrameSizeErrorTX64,
       "extremeWirelessIntfFrameSizeErrorTX128": extremeWirelessIntfFrameSizeErrorTX128,
       "extremeWirelessIntfFrameSizeErrorTX256": extremeWirelessIntfFrameSizeErrorTX256,
       "extremeWirelessIntfFrameSizeErrorTX512": extremeWirelessIntfFrameSizeErrorTX512,
       "extremeWirelessIntfFrameSizeErrorTX1024": extremeWirelessIntfFrameSizeErrorTX1024,
       "extremeWirelessIntfFrameSizeErrorTX2048": extremeWirelessIntfFrameSizeErrorTX2048,
       "extremeWirelessIntfFrameSizeErrorRX64": extremeWirelessIntfFrameSizeErrorRX64,
       "extremeWirelessIntfFrameSizeErrorRX128": extremeWirelessIntfFrameSizeErrorRX128,
       "extremeWirelessIntfFrameSizeErrorRX256": extremeWirelessIntfFrameSizeErrorRX256,
       "extremeWirelessIntfFrameSizeErrorRX512": extremeWirelessIntfFrameSizeErrorRX512,
       "extremeWirelessIntfFrameSizeErrorRX1024": extremeWirelessIntfFrameSizeErrorRX1024,
       "extremeWirelessIntfFrameSizeErrorRX2048": extremeWirelessIntfFrameSizeErrorRX2048,
       "extremeWirelessIntfFrameSpeedTable": extremeWirelessIntfFrameSpeedTable,
       "extremeWirelessIntfFrameSpeedEntry": extremeWirelessIntfFrameSpeedEntry,
       "extremeWirelessIntfSpeedMgmtTX1": extremeWirelessIntfSpeedMgmtTX1,
       "extremeWirelessIntfSpeedMgmtTX2": extremeWirelessIntfSpeedMgmtTX2,
       "extremeWirelessIntfSpeedMgmtTX5p5": extremeWirelessIntfSpeedMgmtTX5p5,
       "extremeWirelessIntfSpeedMgmtTX6": extremeWirelessIntfSpeedMgmtTX6,
       "extremeWirelessIntfSpeedMgmtTX9": extremeWirelessIntfSpeedMgmtTX9,
       "extremeWirelessIntfSpeedMgmtTX11": extremeWirelessIntfSpeedMgmtTX11,
       "extremeWirelessIntfSpeedMgmtTX12": extremeWirelessIntfSpeedMgmtTX12,
       "extremeWirelessIntfSpeedMgmtTX18": extremeWirelessIntfSpeedMgmtTX18,
       "extremeWirelessIntfSpeedMgmtTX24": extremeWirelessIntfSpeedMgmtTX24,
       "extremeWirelessIntfSpeedMgmtTX36": extremeWirelessIntfSpeedMgmtTX36,
       "extremeWirelessIntfSpeedMgmtTX48": extremeWirelessIntfSpeedMgmtTX48,
       "extremeWirelessIntfSpeedMgmtTX54": extremeWirelessIntfSpeedMgmtTX54,
       "extremeWirelessIntfSpeedMgmtRX1": extremeWirelessIntfSpeedMgmtRX1,
       "extremeWirelessIntfSpeedMgmtRX2": extremeWirelessIntfSpeedMgmtRX2,
       "extremeWirelessIntfSpeedMgmtRX5p5": extremeWirelessIntfSpeedMgmtRX5p5,
       "extremeWirelessIntfSpeedMgmtRX6": extremeWirelessIntfSpeedMgmtRX6,
       "extremeWirelessIntfSpeedMgmtRX9": extremeWirelessIntfSpeedMgmtRX9,
       "extremeWirelessIntfSpeedMgmtRX11": extremeWirelessIntfSpeedMgmtRX11,
       "extremeWirelessIntfSpeedMgmtRX12": extremeWirelessIntfSpeedMgmtRX12,
       "extremeWirelessIntfSpeedMgmtRX18": extremeWirelessIntfSpeedMgmtRX18,
       "extremeWirelessIntfSpeedMgmtRX24": extremeWirelessIntfSpeedMgmtRX24,
       "extremeWirelessIntfSpeedMgmtRX36": extremeWirelessIntfSpeedMgmtRX36,
       "extremeWirelessIntfSpeedMgmtRX48": extremeWirelessIntfSpeedMgmtRX48,
       "extremeWirelessIntfSpeedMgmtRX54": extremeWirelessIntfSpeedMgmtRX54,
       "extremeWirelessIntfSpeedCtlTX1": extremeWirelessIntfSpeedCtlTX1,
       "extremeWirelessIntfSpeedCtlTX2": extremeWirelessIntfSpeedCtlTX2,
       "extremeWirelessIntfSpeedCtlTX5p5": extremeWirelessIntfSpeedCtlTX5p5,
       "extremeWirelessIntfSpeedCtlTX6": extremeWirelessIntfSpeedCtlTX6,
       "extremeWirelessIntfSpeedCtlTX9": extremeWirelessIntfSpeedCtlTX9,
       "extremeWirelessIntfSpeedCtlTX11": extremeWirelessIntfSpeedCtlTX11,
       "extremeWirelessIntfSpeedCtlTX12": extremeWirelessIntfSpeedCtlTX12,
       "extremeWirelessIntfSpeedCtlTX18": extremeWirelessIntfSpeedCtlTX18,
       "extremeWirelessIntfSpeedCtlTX24": extremeWirelessIntfSpeedCtlTX24,
       "extremeWirelessIntfSpeedCtlTX36": extremeWirelessIntfSpeedCtlTX36,
       "extremeWirelessIntfSpeedCtlTX48": extremeWirelessIntfSpeedCtlTX48,
       "extremeWirelessIntfSpeedCtlTX54": extremeWirelessIntfSpeedCtlTX54,
       "extremeWirelessIntfSpeedCtlRX1": extremeWirelessIntfSpeedCtlRX1,
       "extremeWirelessIntfSpeedCtlRX2": extremeWirelessIntfSpeedCtlRX2,
       "extremeWirelessIntfSpeedCtlRX5p5": extremeWirelessIntfSpeedCtlRX5p5,
       "extremeWirelessIntfSpeedCtlRX6": extremeWirelessIntfSpeedCtlRX6,
       "extremeWirelessIntfSpeedCtlRX9": extremeWirelessIntfSpeedCtlRX9,
       "extremeWirelessIntfSpeedCtlRX11": extremeWirelessIntfSpeedCtlRX11,
       "extremeWirelessIntfSpeedCtlRX12": extremeWirelessIntfSpeedCtlRX12,
       "extremeWirelessIntfSpeedCtlRX18": extremeWirelessIntfSpeedCtlRX18,
       "extremeWirelessIntfSpeedCtlRX24": extremeWirelessIntfSpeedCtlRX24,
       "extremeWirelessIntfSpeedCtlRX36": extremeWirelessIntfSpeedCtlRX36,
       "extremeWirelessIntfSpeedCtlRX48": extremeWirelessIntfSpeedCtlRX48,
       "extremeWirelessIntfSpeedCtlRX54": extremeWirelessIntfSpeedCtlRX54,
       "extremeWirelessIntfSpeedDataTX1": extremeWirelessIntfSpeedDataTX1,
       "extremeWirelessIntfSpeedDataTX2": extremeWirelessIntfSpeedDataTX2,
       "extremeWirelessIntfSpeedDataTX5p5": extremeWirelessIntfSpeedDataTX5p5,
       "extremeWirelessIntfSpeedDataTX6": extremeWirelessIntfSpeedDataTX6,
       "extremeWirelessIntfSpeedDataTX9": extremeWirelessIntfSpeedDataTX9,
       "extremeWirelessIntfSpeedDataTX11": extremeWirelessIntfSpeedDataTX11,
       "extremeWirelessIntfSpeedDataTX12": extremeWirelessIntfSpeedDataTX12,
       "extremeWirelessIntfSpeedDataTX18": extremeWirelessIntfSpeedDataTX18,
       "extremeWirelessIntfSpeedDataTX24": extremeWirelessIntfSpeedDataTX24,
       "extremeWirelessIntfSpeedDataTX36": extremeWirelessIntfSpeedDataTX36,
       "extremeWirelessIntfSpeedDataTX48": extremeWirelessIntfSpeedDataTX48,
       "extremeWirelessIntfSpeedDataTX54": extremeWirelessIntfSpeedDataTX54,
       "extremeWirelessIntfSpeedDataRX1": extremeWirelessIntfSpeedDataRX1,
       "extremeWirelessIntfSpeedDataRX2": extremeWirelessIntfSpeedDataRX2,
       "extremeWirelessIntfSpeedDataRX5p5": extremeWirelessIntfSpeedDataRX5p5,
       "extremeWirelessIntfSpeedDataRX6": extremeWirelessIntfSpeedDataRX6,
       "extremeWirelessIntfSpeedDataRX9": extremeWirelessIntfSpeedDataRX9,
       "extremeWirelessIntfSpeedDataRX11": extremeWirelessIntfSpeedDataRX11,
       "extremeWirelessIntfSpeedDataRX12": extremeWirelessIntfSpeedDataRX12,
       "extremeWirelessIntfSpeedDataRX18": extremeWirelessIntfSpeedDataRX18,
       "extremeWirelessIntfSpeedDataRX24": extremeWirelessIntfSpeedDataRX24,
       "extremeWirelessIntfSpeedDataRX36": extremeWirelessIntfSpeedDataRX36,
       "extremeWirelessIntfSpeedDataRX48": extremeWirelessIntfSpeedDataRX48,
       "extremeWirelessIntfSpeedDataRX54": extremeWirelessIntfSpeedDataRX54,
       "extremeWirelessIntfFrameSpeedErrorTable": extremeWirelessIntfFrameSpeedErrorTable,
       "extremeWirelessIntfFrameSpeedErrorEntry": extremeWirelessIntfFrameSpeedErrorEntry,
       "extremeWirelessIntfSpeedReXmit1": extremeWirelessIntfSpeedReXmit1,
       "extremeWirelessIntfSpeedReXmit2": extremeWirelessIntfSpeedReXmit2,
       "extremeWirelessIntfSpeedReXmit5p5": extremeWirelessIntfSpeedReXmit5p5,
       "extremeWirelessIntfSpeedReXmit6": extremeWirelessIntfSpeedReXmit6,
       "extremeWirelessIntfSpeedReXmit9": extremeWirelessIntfSpeedReXmit9,
       "extremeWirelessIntfSpeedReXmit11": extremeWirelessIntfSpeedReXmit11,
       "extremeWirelessIntfSpeedReXmit12": extremeWirelessIntfSpeedReXmit12,
       "extremeWirelessIntfSpeedReXmit18": extremeWirelessIntfSpeedReXmit18,
       "extremeWirelessIntfSpeedReXmit24": extremeWirelessIntfSpeedReXmit24,
       "extremeWirelessIntfSpeedReXmit36": extremeWirelessIntfSpeedReXmit36,
       "extremeWirelessIntfSpeedReXmit48": extremeWirelessIntfSpeedReXmit48,
       "extremeWirelessIntfSpeedReXmit54": extremeWirelessIntfSpeedReXmit54,
       "extremeWirelessIntfSpeedErrorTX1": extremeWirelessIntfSpeedErrorTX1,
       "extremeWirelessIntfSpeedErrorTX2": extremeWirelessIntfSpeedErrorTX2,
       "extremeWirelessIntfSpeedErrorTX5p5": extremeWirelessIntfSpeedErrorTX5p5,
       "extremeWirelessIntfSpeedErrorTX6": extremeWirelessIntfSpeedErrorTX6,
       "extremeWirelessIntfSpeedErrorTX9": extremeWirelessIntfSpeedErrorTX9,
       "extremeWirelessIntfSpeedErrorTX11": extremeWirelessIntfSpeedErrorTX11,
       "extremeWirelessIntfSpeedErrorTX12": extremeWirelessIntfSpeedErrorTX12,
       "extremeWirelessIntfSpeedErrorTX18": extremeWirelessIntfSpeedErrorTX18,
       "extremeWirelessIntfSpeedErrorTX24": extremeWirelessIntfSpeedErrorTX24,
       "extremeWirelessIntfSpeedErrorTX36": extremeWirelessIntfSpeedErrorTX36,
       "extremeWirelessIntfSpeedErrorTX48": extremeWirelessIntfSpeedErrorTX48,
       "extremeWirelessIntfSpeedErrorTX54": extremeWirelessIntfSpeedErrorTX54,
       "extremeWirelessIntfSpeedErrorRX1": extremeWirelessIntfSpeedErrorRX1,
       "extremeWirelessIntfSpeedErrorRX2": extremeWirelessIntfSpeedErrorRX2,
       "extremeWirelessIntfSpeedErrorRX5p5": extremeWirelessIntfSpeedErrorRX5p5,
       "extremeWirelessIntfSpeedErrorRX6": extremeWirelessIntfSpeedErrorRX6,
       "extremeWirelessIntfSpeedErrorRX9": extremeWirelessIntfSpeedErrorRX9,
       "extremeWirelessIntfSpeedErrorRX11": extremeWirelessIntfSpeedErrorRX11,
       "extremeWirelessIntfSpeedErrorRX12": extremeWirelessIntfSpeedErrorRX12,
       "extremeWirelessIntfSpeedErrorRX18": extremeWirelessIntfSpeedErrorRX18,
       "extremeWirelessIntfSpeedErrorRX24": extremeWirelessIntfSpeedErrorRX24,
       "extremeWirelessIntfSpeedErrorRX36": extremeWirelessIntfSpeedErrorRX36,
       "extremeWirelessIntfSpeedErrorRX48": extremeWirelessIntfSpeedErrorRX48,
       "extremeWirelessIntfSpeedErrorRX54": extremeWirelessIntfSpeedErrorRX54,
       "extremeWirelessIntfUtilizationTable": extremeWirelessIntfUtilizationTable,
       "extremeWirelessIntfUtilizationEntry": extremeWirelessIntfUtilizationEntry,
       "extremeWirelessIntfUtilizationNav": extremeWirelessIntfUtilizationNav,
       "extremeWirelessIntfUtilizationNoiseFloor": extremeWirelessIntfUtilizationNoiseFloor,
       "extremeWirelessCounterMeasureSource": extremeWirelessCounterMeasureSource,
       "extremeWirelessClientWPAStatsTable": extremeWirelessClientWPAStatsTable,
       "extremeWirelessClientWPAStatsEntry": extremeWirelessClientWPAStatsEntry,
       "extremeWirelessClientWPAStatsStarts": extremeWirelessClientWPAStatsStarts,
       "extremeWirelessClientWPAStatsPairwiseKeySuccesses": extremeWirelessClientWPAStatsPairwiseKeySuccesses,
       "extremeWirelessClientWPAStatsPairwiseKeyFailures": extremeWirelessClientWPAStatsPairwiseKeyFailures,
       "extremeWirelessClientWPAStatsGroupKeySuccesses": extremeWirelessClientWPAStatsGroupKeySuccesses,
       "extremeWirelessClientWPAStatsGroupKeyFailures": extremeWirelessClientWPAStatsGroupKeyFailures,
       "extremeWirelessClientWPAStatsPairwiseKey1Sends": extremeWirelessClientWPAStatsPairwiseKey1Sends,
       "extremeWirelessClientWPAStatsPairwiseKey3Sends": extremeWirelessClientWPAStatsPairwiseKey3Sends,
       "extremeWirelessClientWPAStatsGroupKeySends": extremeWirelessClientWPAStatsGroupKeySends,
       "extremeWirelessClientWPAStatsEAPOLKeyReceivedInPairwise1Key": extremeWirelessClientWPAStatsEAPOLKeyReceivedInPairwise1Key,
       "extremeWirelessClientWPAStatsEAPOLKeyReceivedInPairwise3Key": extremeWirelessClientWPAStatsEAPOLKeyReceivedInPairwise3Key,
       "extremeWirelessClientWPAStatsEAPOLKeyReceivedInGroupKey": extremeWirelessClientWPAStatsEAPOLKeyReceivedInGroupKey,
       "extremeWirelessClientWPAStatsDoubleEAPOLKeyReceived": extremeWirelessClientWPAStatsDoubleEAPOLKeyReceived,
       "extremeWirelessClientWPAStatsEAPOLKeyIgnores": extremeWirelessClientWPAStatsEAPOLKeyIgnores,
       "extremeWirelessClientWPAStatsEAPOLKeyErrors": extremeWirelessClientWPAStatsEAPOLKeyErrors,
       "extremeWirelessClientWPAStatsEAPOLKeyAborts": extremeWirelessClientWPAStatsEAPOLKeyAborts,
       "extremeWirelessClientWPAStatsEAPOLKeyVerificationSuccesses": extremeWirelessClientWPAStatsEAPOLKeyVerificationSuccesses,
       "extremeWirelessOpaqueTable": extremeWirelessOpaqueTable,
       "extremeWirelessOpaqueEntry": extremeWirelessOpaqueEntry,
       "extremeWirelessClientData": extremeWirelessClientData,
       "extremeWirelessPAEStatsData": extremeWirelessPAEStatsData,
       "extremeWirelessPAEDiagData": extremeWirelessPAEDiagData,
       "extremeWirelessScanResultsData": extremeWirelessScanResultsData,
       "extremeWirelessProbeInfoData": extremeWirelessProbeInfoData,
       "extremeWirelessClientDiagData": extremeWirelessClientDiagData,
       "extremeWirelessClientAssocData": extremeWirelessClientAssocData,
       "extremeWirelessClientAuthData": extremeWirelessClientAuthData,
       "extremeWirelessClientMACInfoData": extremeWirelessClientMACInfoData,
       "extremeWirelessSizeCounterData": extremeWirelessSizeCounterData,
       "extremeWirelessSpeedCounterData": extremeWirelessSpeedCounterData,
       "extremeWirelessTraceTable": extremeWirelessTraceTable,
       "extremeWirelessTraceEntry": extremeWirelessTraceEntry,
       "extremeWirelessTraceMsgsOut": extremeWirelessTraceMsgsOut,
       "extremeWirelessTraceBytesOut": extremeWirelessTraceBytesOut,
       "extremeWirelessTraceSuppressed": extremeWirelessTraceSuppressed,
       "extremeWirelessTraceOtherErr": extremeWirelessTraceOtherErr,
       "extremeWirelessTraceOpaque": extremeWirelessTraceOpaque,
       "extremeWirelessTraceModuleTable": extremeWirelessTraceModuleTable,
       "extremeWirelessTraceModuleEntry": extremeWirelessTraceModuleEntry,
       "extremeWirelessTraceModuleId": extremeWirelessTraceModuleId,
       "extremeWirelessTraceModuleDesc": extremeWirelessTraceModuleDesc,
       "extremeWirelessTraceModuleHeader": extremeWirelessTraceModuleHeader,
       "extremeWirelessTraceModuleLevel": extremeWirelessTraceModuleLevel,
       "extremeWirelessTraceModuleSuppressed": extremeWirelessTraceModuleSuppressed,
       "extremeWirelessTraceModuleMsgsOut": extremeWirelessTraceModuleMsgsOut,
       "extremeWirelessTraceModuleBytesOut": extremeWirelessTraceModuleBytesOut,
       "extremeWirelessLogDiagTable": extremeWirelessLogDiagTable,
       "extremeWirelessLogDiagEntry": extremeWirelessLogDiagEntry,
       "extremeWirelessLogDiagEventLogTotalCount": extremeWirelessLogDiagEventLogTotalCount,
       "extremeWirelessLogDiagEventLogTotalEmergCount": extremeWirelessLogDiagEventLogTotalEmergCount,
       "extremeWirelessLogDiagEventLogTotalAlertCount": extremeWirelessLogDiagEventLogTotalAlertCount,
       "extremeWirelessLogDiagEventLogTotalCritCount": extremeWirelessLogDiagEventLogTotalCritCount,
       "extremeWirelessLogDiagEventLogTotalErrorCount": extremeWirelessLogDiagEventLogTotalErrorCount,
       "extremeWirelessLogDiagEventLogTotalWarnCount": extremeWirelessLogDiagEventLogTotalWarnCount,
       "extremeWirelessLogDiagEventLogTotalNoticeCount": extremeWirelessLogDiagEventLogTotalNoticeCount,
       "extremeWirelessLogDiagEventLogTotalInfoCount": extremeWirelessLogDiagEventLogTotalInfoCount,
       "extremeWirelessLogDiagEventLogTotalDebugCount": extremeWirelessLogDiagEventLogTotalDebugCount,
       "extremeWirelessLogDiagEventLogTotalSuppressedCount": extremeWirelessLogDiagEventLogTotalSuppressedCount,
       "extremeWirelessLogDiagEventLogTotalByteCount": extremeWirelessLogDiagEventLogTotalByteCount,
       "extremeWirelessLogDiagSyslogTotalEventCount": extremeWirelessLogDiagSyslogTotalEventCount,
       "extremeWirelessLogDiagSyslogTotalSuppressedCount": extremeWirelessLogDiagSyslogTotalSuppressedCount,
       "extremeWirelessLogDiagSyslogTotalByteCount": extremeWirelessLogDiagSyslogTotalByteCount,
       "extremeWirelessLogDiagNVRAMTotalEventCount": extremeWirelessLogDiagNVRAMTotalEventCount,
       "extremeWirelessLogDiagNVRAMTotalSuppressedCount": extremeWirelessLogDiagNVRAMTotalSuppressedCount,
       "extremeWirelessLogDiagNVRAMTotalDroppedCount": extremeWirelessLogDiagNVRAMTotalDroppedCount,
       "extremeWirelessLogDiagNVRAMTotalByteCount": extremeWirelessLogDiagNVRAMTotalByteCount,
       "extremeWirelessLogDiagClearStats": extremeWirelessLogDiagClearStats,
       "extremeLACGeneral": extremeLACGeneral,
       "extremeAPTotalAuthFailures": extremeAPTotalAuthFailures,
       "extremeAPTotalDetectedStations": extremeAPTotalDetectedStations,
       "extremeAPTotalAssociatedStations": extremeAPTotalAssociatedStations,
       "extremeAPTotalAuthenticatedStations": extremeAPTotalAuthenticatedStations,
       "extremeWirelessCfgMgmtVLAN": extremeWirelessCfgMgmtVLAN,
       "extremeWirelessCfgNetmask": extremeWirelessCfgNetmask,
       "extremeWirelessCfgGateway": extremeWirelessCfgGateway,
       "extremeWirelessCfgEnableWirelessTraps": extremeWirelessCfgEnableWirelessTraps,
       "extremeWirelessCfgCountryCode": extremeWirelessCfgCountryCode,
       "extremeProfile": extremeProfile,
       "extremeRFProfile": extremeRFProfile,
       "extremeRFProfileTable": extremeRFProfileTable,
       "extremeRFProfileEntry": extremeRFProfileEntry,
       "extremeRFProfileIndex": extremeRFProfileIndex,
       "extremeRFProfileName": extremeRFProfileName,
       "extremeRFProfileType": extremeRFProfileType,
       "extremeRFProfileBeaconInterval": extremeRFProfileBeaconInterval,
       "extremeRFProfileDTIM": extremeRFProfileDTIM,
       "extremeRFProfileFragLength": extremeRFProfileFragLength,
       "extremeRFProfileRTSThresh": extremeRFProfileRTSThresh,
       "extremeRFProfilePreamble": extremeRFProfilePreamble,
       "extremeRFProfileShortRetry": extremeRFProfileShortRetry,
       "extremeRFProfileLongRetry": extremeRFProfileLongRetry,
       "extremeRFProfileStatus": extremeRFProfileStatus,
       "extremeSecurityProfile": extremeSecurityProfile,
       "extremeSecurityProfileTable": extremeSecurityProfileTable,
       "extremeSecurityProfileEntry": extremeSecurityProfileEntry,
       "extremeSecurityProfileIndex": extremeSecurityProfileIndex,
       "extremeSecurityProfileName": extremeSecurityProfileName,
       "extremeSecurityProfileESSName": extremeSecurityProfileESSName,
       "extremeSecurityProfileSSIDInBeacon": extremeSecurityProfileSSIDInBeacon,
       "extremeSecurityProfileDot11AuthMode": extremeSecurityProfileDot11AuthMode,
       "extremeSecurityProfileNetworkAuthMode": extremeSecurityProfileNetworkAuthMode,
       "extremeSecurityProfileDataVlan": extremeSecurityProfileDataVlan,
       "extremeSecurityProfileIgnoreVSAVlan": extremeSecurityProfileIgnoreVSAVlan,
       "extremeSecurityWEPDefaultKey": extremeSecurityWEPDefaultKey,
       "extremeSecurityProfileEncryptionLength": extremeSecurityProfileEncryptionLength,
       "extremeSecurityProfileStatus": extremeSecurityProfileStatus,
       "extremeSecurityDot1xConfigTable": extremeSecurityDot1xConfigTable,
       "extremeSecurityDot1xConfigEntry": extremeSecurityDot1xConfigEntry,
       "extremeSecurityKeyMgmtSuite": extremeSecurityKeyMgmtSuite,
       "extremeSecurityMcastCipherSuite": extremeSecurityMcastCipherSuite,
       "extremeSecurityDot1xPSKValue": extremeSecurityDot1xPSKValue,
       "extremeSecurityDot1xPSKPassPhrase": extremeSecurityDot1xPSKPassPhrase,
       "extremeSecurityDot1xReAuthPeriod": extremeSecurityDot1xReAuthPeriod,
       "extremeSecurityGroupUpdateTimeOut": extremeSecurityGroupUpdateTimeOut,
       "extremeSecurityPairwiseUpdateTimeOut": extremeSecurityPairwiseUpdateTimeOut,
       "extremeSecurityDot11iPreauthEnabled": extremeSecurityDot11iPreauthEnabled,
       "extremeWEPKeyTable": extremeWEPKeyTable,
       "extremeWEPKeyEntry": extremeWEPKeyEntry,
       "extremeWEPKeyIndex": extremeWEPKeyIndex,
       "extremeWEPKey": extremeWEPKey,
       "extremeWEPKeyStatus": extremeWEPKeyStatus,
       "extremeWirelessPhysInterfaceConfigTable": extremeWirelessPhysInterfaceConfigTable,
       "extremeWirelessPhysInterfaceConfigEntry": extremeWirelessPhysInterfaceConfigEntry,
       "extremeWirelessPhysInterfaceConfigRFProfile": extremeWirelessPhysInterfaceConfigRFProfile,
       "extremeWirelessPhysInterfaceConfigRFChannel": extremeWirelessPhysInterfaceConfigRFChannel,
       "extremeWirelessPhysInterfaceConfigSpeed": extremeWirelessPhysInterfaceConfigSpeed,
       "extremeWirelessPhysInterfaceConfigPowerLevel": extremeWirelessPhysInterfaceConfigPowerLevel,
       "extremeWirelessVirtInterfaceConfigTable": extremeWirelessVirtInterfaceConfigTable,
       "extremeWirelessVirtInterfaceConfigEntry": extremeWirelessVirtInterfaceConfigEntry,
       "extremeWirelessVirtInterfaceConfigSecurityProfile": extremeWirelessVirtInterfaceConfigSecurityProfile,
       "extremeWirelessVirtInterfaceConfigMaxClients": extremeWirelessVirtInterfaceConfigMaxClients,
       "extremeWirelessVirtInterfaceConfigWirelessBridging": extremeWirelessVirtInterfaceConfigWirelessBridging,
       "extremeWirelessVirtInterfaceConfigState": extremeWirelessVirtInterfaceConfigState,
       "extremeAntennaProfile": extremeAntennaProfile,
       "extremeAntennaProfileTable": extremeAntennaProfileTable,
       "extremeAntennaProfileEntry": extremeAntennaProfileEntry,
       "extremeAntennaProfileIndex": extremeAntennaProfileIndex,
       "extremeAntennaProfileName": extremeAntennaProfileName,
       "extremeAntennaProfile2point4GHZGain": extremeAntennaProfile2point4GHZGain,
       "extremeAntennaProfile5GHZGain": extremeAntennaProfile5GHZGain,
       "extremeAntennaProfileStatus": extremeAntennaProfileStatus,
       "extremeWirelessRemoteConnectGlobalCfgGroup": extremeWirelessRemoteConnectGlobalCfgGroup,
       "extremeWirelessRemoteConnectGlobalBindingType": extremeWirelessRemoteConnectGlobalBindingType,
       "extremeWirelessRemoteConnectBindingTable": extremeWirelessRemoteConnectBindingTable,
       "extremeWirelessRemoteConnectBindingEntry": extremeWirelessRemoteConnectBindingEntry,
       "extremeWirelessRemoteConnectBindingPortIndex": extremeWirelessRemoteConnectBindingPortIndex,
       "extremeWirelessRemoteConnectBindingIfIndex": extremeWirelessRemoteConnectBindingIfIndex,
       "extremeWirelessRemoteConnectBindingType": extremeWirelessRemoteConnectBindingType,
       "extremeWirelessRemoteConnectBindingMAC": extremeWirelessRemoteConnectBindingMAC,
       "extremeWirelessRemoteConnectBindingSerial": extremeWirelessRemoteConnectBindingSerial,
       "extremeWirelessRemoteConnectBindingIPAddressType": extremeWirelessRemoteConnectBindingIPAddressType,
       "extremeWirelessRemoteConnectBindingIPAddress": extremeWirelessRemoteConnectBindingIPAddress,
       "extremeWirelessRemoteConnectBindingEnabled": extremeWirelessRemoteConnectBindingEnabled,
       "extremeWirelessRemoteConnectBindingBound": extremeWirelessRemoteConnectBindingBound,
       "extremeWirelessRemoteConnectBindingRowStatus": extremeWirelessRemoteConnectBindingRowStatus,
       "extremeWirelessRemoteConnectRedirectBindingTable": extremeWirelessRemoteConnectRedirectBindingTable,
       "extremeWirelessRemoteConnectRedirectBindingEntry": extremeWirelessRemoteConnectRedirectBindingEntry,
       "extremeWirelessRemoteConnectRedirectBindingIndex": extremeWirelessRemoteConnectRedirectBindingIndex,
       "extremeWirelessRemoteConnectRedirectBindingType": extremeWirelessRemoteConnectRedirectBindingType,
       "extremeWirelessRemoteConnectRedirectBindingMAC": extremeWirelessRemoteConnectRedirectBindingMAC,
       "extremeWirelessRemoteConnectRedirectBindingSerial": extremeWirelessRemoteConnectRedirectBindingSerial,
       "extremeWirelessRemoteConnectRedirectBindingIPAddressType": extremeWirelessRemoteConnectRedirectBindingIPAddressType,
       "extremeWirelessRemoteConnectRedirectBindingIPAddress": extremeWirelessRemoteConnectRedirectBindingIPAddress,
       "extremeWirelessRemoteConnectRedirectBindAttachSwitchIPAddrType": extremeWirelessRemoteConnectRedirectBindAttachSwitchIPAddrType,
       "extremeWirelessRemoteConnectRedirectBindAttachSwitchIPAddr": extremeWirelessRemoteConnectRedirectBindAttachSwitchIPAddr,
       "extremeWirelessRemoteConnectRedirectBindingEnabled": extremeWirelessRemoteConnectRedirectBindingEnabled,
       "extremeWirelessRemoteConnectRedirectBindingNumRedirects": extremeWirelessRemoteConnectRedirectBindingNumRedirects,
       "extremeWirelessRemoteConnectRedirectBindingRowStatus": extremeWirelessRemoteConnectRedirectBindingRowStatus,
       "extremeWirelessRemoteConnectDeviceDBGroup": extremeWirelessRemoteConnectDeviceDBGroup,
       "extremeWirelessRemoteConnectDeviceDBTimeOut": extremeWirelessRemoteConnectDeviceDBTimeOut,
       "extremeWirelessRemoteConnectUnboundAPsTable": extremeWirelessRemoteConnectUnboundAPsTable,
       "extremeWirelessRemoteConnectUnboundAPsEntry": extremeWirelessRemoteConnectUnboundAPsEntry,
       "extremeWirelessRemoteConnectUnboundAPsIndex": extremeWirelessRemoteConnectUnboundAPsIndex,
       "extremeWirelessRemoteConnectUnboundAPsMAC": extremeWirelessRemoteConnectUnboundAPsMAC,
       "extremeWirelessRemoteConnectUnboundAPsSerial": extremeWirelessRemoteConnectUnboundAPsSerial,
       "extremeWirelessRemoteConnectUnboundAPsIPAddressType": extremeWirelessRemoteConnectUnboundAPsIPAddressType,
       "extremeWirelessRemoteConnectUnboundAPsIPAddress": extremeWirelessRemoteConnectUnboundAPsIPAddress,
       "extremeWirelessRemoteConnectUnboundAPsNumAttempts": extremeWirelessRemoteConnectUnboundAPsNumAttempts,
       "extremeWirelessRemoteConnectUnboundAPsRowStatus": extremeWirelessRemoteConnectUnboundAPsRowStatus,
       "extremeWirelessPortCfgTable": extremeWirelessPortCfgTable,
       "extremeWirelessPortCfgEntry": extremeWirelessPortCfgEntry,
       "extremeWirelessPortIfIndex": extremeWirelessPortIfIndex,
       "extremeWirelessPortCfgIpAddress": extremeWirelessPortCfgIpAddress,
       "extremeWirelessPortCfgLocation": extremeWirelessPortCfgLocation,
       "extremeWirelessPortCfgDetectedTimeout": extremeWirelessPortCfgDetectedTimeout,
       "extremeWirelessPortCfgClientWatchdog": extremeWirelessPortCfgClientWatchdog,
       "extremeWirelessPortLastChange": extremeWirelessPortLastChange,
       "extremeWirelessPortState": extremeWirelessPortState,
       "extremeWirelessPortAntennaType": extremeWirelessPortAntennaType,
       "extremeWirelessPortAntennaLocation": extremeWirelessPortAntennaLocation,
       "extremeWirelessPortBootstrapServerAddressType": extremeWirelessPortBootstrapServerAddressType,
       "extremeWirelessPortBootstrapServerAddress": extremeWirelessPortBootstrapServerAddress,
       "extremeWirelessPortBootstrapFilePath": extremeWirelessPortBootstrapFilePath,
       "extremeWirelessPortBootLoaderServerAddressType": extremeWirelessPortBootLoaderServerAddressType,
       "extremeWirelessPortBootLoaderServerAddress": extremeWirelessPortBootLoaderServerAddress,
       "extremeWirelessPortBootLoaderFilePath": extremeWirelessPortBootLoaderFilePath,
       "extremeWirelessPortRuntimeServerAddressType": extremeWirelessPortRuntimeServerAddressType,
       "extremeWirelessPortRuntimeServerAddress": extremeWirelessPortRuntimeServerAddress,
       "extremeWirelessPortRuntimeFilePath": extremeWirelessPortRuntimeFilePath,
       "extremeWirelessPortMultiBootMode": extremeWirelessPortMultiBootMode,
       "extremeAPTraps": extremeAPTraps,
       "extremeAPTrapsPrefix": extremeAPTrapsPrefix,
       "extremeWirelessPortStateChange": extremeWirelessPortStateChange,
       "extremeWirelessPortBootFailure": extremeWirelessPortBootFailure,
       "extremeWirelessClientStationAgedOut": extremeWirelessClientStationAgedOut,
       "extremeWirelessNetloginClientAssociated": extremeWirelessNetloginClientAssociated,
       "extremeWirelessAPAdded": extremeWirelessAPAdded,
       "extremeWirelessAPRemoved": extremeWirelessAPRemoved,
       "extremeWirelessAPUpdated": extremeWirelessAPUpdated,
       "extremeWirelessProbeInfoAdded": extremeWirelessProbeInfoAdded,
       "extremeWirelessProbeInfoRemoved": extremeWirelessProbeInfoRemoved,
       "extremeWirelessOffChannelScanStarted": extremeWirelessOffChannelScanStarted,
       "extremeWirelessOffChannelScanFinished": extremeWirelessOffChannelScanFinished,
       "extremeWirelessCounterMeasureStarted": extremeWirelessCounterMeasureStarted,
       "extremeWirelessCounterMeasureStopped": extremeWirelessCounterMeasureStopped,
       "extremeWirelessInterfaceChannelRescan": extremeWirelessInterfaceChannelRescan}
)
