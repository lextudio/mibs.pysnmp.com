# SNMP MIB module (HM2-WWAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-WWAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:36 2024
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

(HmActionValue,
 HmEnabledStatus,
 HmLargeDisplayString,
 HmTimeSeconds1970,
 hm2ConfigurationMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmActionValue",
    "HmEnabledStatus",
    "HmLargeDisplayString",
    "HmTimeSeconds1970",
    "hm2ConfigurationMibs")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hm2WwanMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 125)
)
hm2WwanMib.setRevisions(
        ("2015-05-29 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hm2CellularNetworks(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("gsm", 2),
          ("gsmlte", 6),
          ("gsmumts", 5),
          ("lte", 4),
          ("umts", 3),
          ("umtslte", 7))
    )



class Hm2TechnologyLevel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lte", 1),
          ("utms", 2))
    )



class Hm2AuthType(Integer32, TextualConvention):
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
        *(("chap", 3),
          ("none", 1),
          ("pap", 2),
          ("papchap", 4))
    )



class Hm2PdpType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv4v6", 3),
          ("ipv6", 2))
    )



class Hm2ConnectionStatus(Integer32, TextualConvention):
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
        *(("active", 2),
          ("failure", 5),
          ("idle", 3),
          ("inactive", 1),
          ("reconnecting", 4))
    )



class Hm2LimitUnit(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("gb", 3),
          ("kb", 1),
          ("mb", 2))
    )



class Hm2SimCardRole(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("backup", 3),
          ("primary", 2))
    )



class Hm2SimCardStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("simAbsent", 2),
          ("simActive", 6),
          ("simInactive", 5),
          ("simLocked", 3),
          ("simPresent", 1),
          ("simUnlocked", 4))
    )



class Hm2Pin1Status(Integer32, TextualConvention):
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
        *(("blocked", 3),
          ("disabled", 4),
          ("notVerified", 1),
          ("verified", 2),
          ("wrongCode", 5))
    )



class Hm2RegistrationStatus(Integer32, TextualConvention):
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
        *(("failure", 4),
          ("notRegistered", 1),
          ("registered", 3),
          ("registering", 2))
    )



class Hm2RoamingStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("home", 1),
          ("roaming", 2),
          ("roamingDisabled", 3))
    )



class Hm2TrapBits(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Hm2WwanMibNotifications_ObjectIdentity = ObjectIdentity
hm2WwanMibNotifications = _Hm2WwanMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 0)
)
_Hm2WwanMibObjects_ObjectIdentity = ObjectIdentity
hm2WwanMibObjects = _Hm2WwanMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1)
)
_Hm2WwanGeneralGroup_ObjectIdentity = ObjectIdentity
hm2WwanGeneralGroup = _Hm2WwanGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 1)
)


class _Hm2WwanAdminStatus_Type(HmEnabledStatus):
    """Custom type hm2WwanAdminStatus based on HmEnabledStatus"""


_Hm2WwanAdminStatus_Object = MibScalar
hm2WwanAdminStatus = _Hm2WwanAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 1, 1),
    _Hm2WwanAdminStatus_Type()
)
hm2WwanAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanAdminStatus.setStatus("current")


class _Hm2WwanCellularSelection_Type(Hm2CellularNetworks):
    """Custom type hm2WwanCellularSelection based on Hm2CellularNetworks"""


_Hm2WwanCellularSelection_Object = MibScalar
hm2WwanCellularSelection = _Hm2WwanCellularSelection_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 1, 2),
    _Hm2WwanCellularSelection_Type()
)
hm2WwanCellularSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanCellularSelection.setStatus("current")


class _Hm2WwanLtePersistence_Type(HmEnabledStatus):
    """Custom type hm2WwanLtePersistence based on HmEnabledStatus"""


_Hm2WwanLtePersistence_Object = MibScalar
hm2WwanLtePersistence = _Hm2WwanLtePersistence_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 1, 4),
    _Hm2WwanLtePersistence_Type()
)
hm2WwanLtePersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanLtePersistence.setStatus("current")


class _Hm2WwanLtePersistenceInterval_Type(Integer32):
    """Custom type hm2WwanLtePersistenceInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_Hm2WwanLtePersistenceInterval_Type.__name__ = "Integer32"
_Hm2WwanLtePersistenceInterval_Object = MibScalar
hm2WwanLtePersistenceInterval = _Hm2WwanLtePersistenceInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 1, 5),
    _Hm2WwanLtePersistenceInterval_Type()
)
hm2WwanLtePersistenceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanLtePersistenceInterval.setStatus("current")


class _Hm2WwanFailoverTechnologyLevel_Type(Hm2TechnologyLevel):
    """Custom type hm2WwanFailoverTechnologyLevel based on Hm2TechnologyLevel"""


_Hm2WwanFailoverTechnologyLevel_Object = MibScalar
hm2WwanFailoverTechnologyLevel = _Hm2WwanFailoverTechnologyLevel_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 1, 6),
    _Hm2WwanFailoverTechnologyLevel_Type()
)
hm2WwanFailoverTechnologyLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanFailoverTechnologyLevel.setStatus("current")


class _Hm2WwanBackupSimFailoverConnection_Type(HmEnabledStatus):
    """Custom type hm2WwanBackupSimFailoverConnection based on HmEnabledStatus"""


_Hm2WwanBackupSimFailoverConnection_Object = MibScalar
hm2WwanBackupSimFailoverConnection = _Hm2WwanBackupSimFailoverConnection_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 1, 7),
    _Hm2WwanBackupSimFailoverConnection_Type()
)
hm2WwanBackupSimFailoverConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanBackupSimFailoverConnection.setStatus("current")


class _Hm2WwanBackupSimFailoverRegistration_Type(HmEnabledStatus):
    """Custom type hm2WwanBackupSimFailoverRegistration based on HmEnabledStatus"""


_Hm2WwanBackupSimFailoverRegistration_Object = MibScalar
hm2WwanBackupSimFailoverRegistration = _Hm2WwanBackupSimFailoverRegistration_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 1, 8),
    _Hm2WwanBackupSimFailoverRegistration_Type()
)
hm2WwanBackupSimFailoverRegistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanBackupSimFailoverRegistration.setStatus("current")


class _Hm2WwanBackupSimFailoverRoaming_Type(HmEnabledStatus):
    """Custom type hm2WwanBackupSimFailoverRoaming based on HmEnabledStatus"""


_Hm2WwanBackupSimFailoverRoaming_Object = MibScalar
hm2WwanBackupSimFailoverRoaming = _Hm2WwanBackupSimFailoverRoaming_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 1, 9),
    _Hm2WwanBackupSimFailoverRoaming_Type()
)
hm2WwanBackupSimFailoverRoaming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanBackupSimFailoverRoaming.setStatus("current")


class _Hm2WwanBackupSimFailoverDataLimit_Type(HmEnabledStatus):
    """Custom type hm2WwanBackupSimFailoverDataLimit based on HmEnabledStatus"""


_Hm2WwanBackupSimFailoverDataLimit_Object = MibScalar
hm2WwanBackupSimFailoverDataLimit = _Hm2WwanBackupSimFailoverDataLimit_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 1, 10),
    _Hm2WwanBackupSimFailoverDataLimit_Type()
)
hm2WwanBackupSimFailoverDataLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanBackupSimFailoverDataLimit.setStatus("current")


class _Hm2WwanModemResetFailoverRegistration_Type(HmEnabledStatus):
    """Custom type hm2WwanModemResetFailoverRegistration based on HmEnabledStatus"""


_Hm2WwanModemResetFailoverRegistration_Object = MibScalar
hm2WwanModemResetFailoverRegistration = _Hm2WwanModemResetFailoverRegistration_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 1, 11),
    _Hm2WwanModemResetFailoverRegistration_Type()
)
hm2WwanModemResetFailoverRegistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanModemResetFailoverRegistration.setStatus("current")


class _Hm2WwanBackupSimTechnologyLevel_Type(HmEnabledStatus):
    """Custom type hm2WwanBackupSimTechnologyLevel based on HmEnabledStatus"""


_Hm2WwanBackupSimTechnologyLevel_Object = MibScalar
hm2WwanBackupSimTechnologyLevel = _Hm2WwanBackupSimTechnologyLevel_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 1, 12),
    _Hm2WwanBackupSimTechnologyLevel_Type()
)
hm2WwanBackupSimTechnologyLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanBackupSimTechnologyLevel.setStatus("current")


class _Hm2WwanFailoverCycle_Type(HmEnabledStatus):
    """Custom type hm2WwanFailoverCycle based on HmEnabledStatus"""


_Hm2WwanFailoverCycle_Object = MibScalar
hm2WwanFailoverCycle = _Hm2WwanFailoverCycle_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 1, 13),
    _Hm2WwanFailoverCycle_Type()
)
hm2WwanFailoverCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanFailoverCycle.setStatus("current")


class _Hm2WwanSetTrap_Type(Hm2TrapBits):
    """Custom type hm2WwanSetTrap based on Hm2TrapBits"""
    defaultBinValue = "11111111111"


_Hm2WwanSetTrap_Object = MibScalar
hm2WwanSetTrap = _Hm2WwanSetTrap_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 1, 14),
    _Hm2WwanSetTrap_Type()
)
hm2WwanSetTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanSetTrap.setStatus("current")
_Hm2WwanDataGroup_ObjectIdentity = ObjectIdentity
hm2WwanDataGroup = _Hm2WwanDataGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2)
)
_Hm2WwanDataConnectionTable_Object = MibTable
hm2WwanDataConnectionTable = _Hm2WwanDataConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hm2WwanDataConnectionTable.setStatus("current")
_Hm2WwanDataConnectionEntry_Object = MibTableRow
hm2WwanDataConnectionEntry = _Hm2WwanDataConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1)
)
hm2WwanDataConnectionEntry.setIndexNames(
    (0, "HM2-WWAN-MIB", "hm2WwanDataConnectionSimId"),
)
if mibBuilder.loadTexts:
    hm2WwanDataConnectionEntry.setStatus("current")


class _Hm2WwanDataConnectionSimId_Type(Integer32):
    """Custom type hm2WwanDataConnectionSimId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Hm2WwanDataConnectionSimId_Type.__name__ = "Integer32"
_Hm2WwanDataConnectionSimId_Object = MibTableColumn
hm2WwanDataConnectionSimId = _Hm2WwanDataConnectionSimId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 1),
    _Hm2WwanDataConnectionSimId_Type()
)
hm2WwanDataConnectionSimId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionSimId.setStatus("current")


class _Hm2WwanDataConnectionAdminStatus_Type(HmEnabledStatus):
    """Custom type hm2WwanDataConnectionAdminStatus based on HmEnabledStatus"""


_Hm2WwanDataConnectionAdminStatus_Object = MibTableColumn
hm2WwanDataConnectionAdminStatus = _Hm2WwanDataConnectionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 2),
    _Hm2WwanDataConnectionAdminStatus_Type()
)
hm2WwanDataConnectionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionAdminStatus.setStatus("current")


class _Hm2WwanDataConnectionApn_Type(SnmpAdminString):
    """Custom type hm2WwanDataConnectionApn based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hm2WwanDataConnectionApn_Type.__name__ = "SnmpAdminString"
_Hm2WwanDataConnectionApn_Object = MibTableColumn
hm2WwanDataConnectionApn = _Hm2WwanDataConnectionApn_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 3),
    _Hm2WwanDataConnectionApn_Type()
)
hm2WwanDataConnectionApn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionApn.setStatus("current")


class _Hm2WwanDataConnectionApnCurrent_Type(SnmpAdminString):
    """Custom type hm2WwanDataConnectionApnCurrent based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hm2WwanDataConnectionApnCurrent_Type.__name__ = "SnmpAdminString"
_Hm2WwanDataConnectionApnCurrent_Object = MibTableColumn
hm2WwanDataConnectionApnCurrent = _Hm2WwanDataConnectionApnCurrent_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 4),
    _Hm2WwanDataConnectionApnCurrent_Type()
)
hm2WwanDataConnectionApnCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionApnCurrent.setStatus("current")


class _Hm2WwanDataConnectionUser_Type(SnmpAdminString):
    """Custom type hm2WwanDataConnectionUser based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hm2WwanDataConnectionUser_Type.__name__ = "SnmpAdminString"
_Hm2WwanDataConnectionUser_Object = MibTableColumn
hm2WwanDataConnectionUser = _Hm2WwanDataConnectionUser_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 5),
    _Hm2WwanDataConnectionUser_Type()
)
hm2WwanDataConnectionUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionUser.setStatus("current")


class _Hm2WwanDataConnectionPassword_Type(SnmpAdminString):
    """Custom type hm2WwanDataConnectionPassword based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hm2WwanDataConnectionPassword_Type.__name__ = "SnmpAdminString"
_Hm2WwanDataConnectionPassword_Object = MibTableColumn
hm2WwanDataConnectionPassword = _Hm2WwanDataConnectionPassword_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 6),
    _Hm2WwanDataConnectionPassword_Type()
)
hm2WwanDataConnectionPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionPassword.setStatus("current")


class _Hm2WwanDataConnectionAuth_Type(Hm2AuthType):
    """Custom type hm2WwanDataConnectionAuth based on Hm2AuthType"""


_Hm2WwanDataConnectionAuth_Object = MibTableColumn
hm2WwanDataConnectionAuth = _Hm2WwanDataConnectionAuth_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 7),
    _Hm2WwanDataConnectionAuth_Type()
)
hm2WwanDataConnectionAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionAuth.setStatus("current")


class _Hm2WwanDataConnectionPdpType_Type(Hm2PdpType):
    """Custom type hm2WwanDataConnectionPdpType based on Hm2PdpType"""


_Hm2WwanDataConnectionPdpType_Object = MibTableColumn
hm2WwanDataConnectionPdpType = _Hm2WwanDataConnectionPdpType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 8),
    _Hm2WwanDataConnectionPdpType_Type()
)
hm2WwanDataConnectionPdpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionPdpType.setStatus("current")


class _Hm2WwanDataConnectionIpAddressType_Type(InetAddressType):
    """Custom type hm2WwanDataConnectionIpAddressType based on InetAddressType"""


_Hm2WwanDataConnectionIpAddressType_Object = MibTableColumn
hm2WwanDataConnectionIpAddressType = _Hm2WwanDataConnectionIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 9),
    _Hm2WwanDataConnectionIpAddressType_Type()
)
hm2WwanDataConnectionIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionIpAddressType.setStatus("current")


class _Hm2WwanDataConnectionIpAddress_Type(InetAddress):
    """Custom type hm2WwanDataConnectionIpAddress based on InetAddress"""
    defaultHexValue = "00000000"


_Hm2WwanDataConnectionIpAddress_Object = MibTableColumn
hm2WwanDataConnectionIpAddress = _Hm2WwanDataConnectionIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 10),
    _Hm2WwanDataConnectionIpAddress_Type()
)
hm2WwanDataConnectionIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionIpAddress.setStatus("current")


class _Hm2WwanDataConnectionDnsPrimaryType_Type(InetAddressType):
    """Custom type hm2WwanDataConnectionDnsPrimaryType based on InetAddressType"""


_Hm2WwanDataConnectionDnsPrimaryType_Object = MibTableColumn
hm2WwanDataConnectionDnsPrimaryType = _Hm2WwanDataConnectionDnsPrimaryType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 11),
    _Hm2WwanDataConnectionDnsPrimaryType_Type()
)
hm2WwanDataConnectionDnsPrimaryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionDnsPrimaryType.setStatus("current")


class _Hm2WwanDataConnectionDnsPrimary_Type(InetAddress):
    """Custom type hm2WwanDataConnectionDnsPrimary based on InetAddress"""
    defaultHexValue = "00000000"


_Hm2WwanDataConnectionDnsPrimary_Object = MibTableColumn
hm2WwanDataConnectionDnsPrimary = _Hm2WwanDataConnectionDnsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 12),
    _Hm2WwanDataConnectionDnsPrimary_Type()
)
hm2WwanDataConnectionDnsPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionDnsPrimary.setStatus("current")


class _Hm2WwanDataConnectionDnsSecondaryType_Type(InetAddressType):
    """Custom type hm2WwanDataConnectionDnsSecondaryType based on InetAddressType"""


_Hm2WwanDataConnectionDnsSecondaryType_Object = MibTableColumn
hm2WwanDataConnectionDnsSecondaryType = _Hm2WwanDataConnectionDnsSecondaryType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 13),
    _Hm2WwanDataConnectionDnsSecondaryType_Type()
)
hm2WwanDataConnectionDnsSecondaryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionDnsSecondaryType.setStatus("current")


class _Hm2WwanDataConnectionDnsSecondary_Type(InetAddress):
    """Custom type hm2WwanDataConnectionDnsSecondary based on InetAddress"""
    defaultHexValue = "00000000"


_Hm2WwanDataConnectionDnsSecondary_Object = MibTableColumn
hm2WwanDataConnectionDnsSecondary = _Hm2WwanDataConnectionDnsSecondary_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 14),
    _Hm2WwanDataConnectionDnsSecondary_Type()
)
hm2WwanDataConnectionDnsSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionDnsSecondary.setStatus("current")
_Hm2WwanDataConnectionIpAddressCurrentType_Type = InetAddressType
_Hm2WwanDataConnectionIpAddressCurrentType_Object = MibTableColumn
hm2WwanDataConnectionIpAddressCurrentType = _Hm2WwanDataConnectionIpAddressCurrentType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 15),
    _Hm2WwanDataConnectionIpAddressCurrentType_Type()
)
hm2WwanDataConnectionIpAddressCurrentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionIpAddressCurrentType.setStatus("current")
_Hm2WwanDataConnectionIpAddressCurrent_Type = InetAddress
_Hm2WwanDataConnectionIpAddressCurrent_Object = MibTableColumn
hm2WwanDataConnectionIpAddressCurrent = _Hm2WwanDataConnectionIpAddressCurrent_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 16),
    _Hm2WwanDataConnectionIpAddressCurrent_Type()
)
hm2WwanDataConnectionIpAddressCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionIpAddressCurrent.setStatus("current")
_Hm2WwanDataConnectionDnsPrimaryCurrentType_Type = InetAddressType
_Hm2WwanDataConnectionDnsPrimaryCurrentType_Object = MibTableColumn
hm2WwanDataConnectionDnsPrimaryCurrentType = _Hm2WwanDataConnectionDnsPrimaryCurrentType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 17),
    _Hm2WwanDataConnectionDnsPrimaryCurrentType_Type()
)
hm2WwanDataConnectionDnsPrimaryCurrentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionDnsPrimaryCurrentType.setStatus("current")
_Hm2WwanDataConnectionDnsPrimaryCurrent_Type = InetAddress
_Hm2WwanDataConnectionDnsPrimaryCurrent_Object = MibTableColumn
hm2WwanDataConnectionDnsPrimaryCurrent = _Hm2WwanDataConnectionDnsPrimaryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 18),
    _Hm2WwanDataConnectionDnsPrimaryCurrent_Type()
)
hm2WwanDataConnectionDnsPrimaryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionDnsPrimaryCurrent.setStatus("current")
_Hm2WwanDataConnectionDnsSecondaryCurrentType_Type = InetAddressType
_Hm2WwanDataConnectionDnsSecondaryCurrentType_Object = MibTableColumn
hm2WwanDataConnectionDnsSecondaryCurrentType = _Hm2WwanDataConnectionDnsSecondaryCurrentType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 19),
    _Hm2WwanDataConnectionDnsSecondaryCurrentType_Type()
)
hm2WwanDataConnectionDnsSecondaryCurrentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionDnsSecondaryCurrentType.setStatus("current")
_Hm2WwanDataConnectionDnsSecondaryCurrent_Type = InetAddress
_Hm2WwanDataConnectionDnsSecondaryCurrent_Object = MibTableColumn
hm2WwanDataConnectionDnsSecondaryCurrent = _Hm2WwanDataConnectionDnsSecondaryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 20),
    _Hm2WwanDataConnectionDnsSecondaryCurrent_Type()
)
hm2WwanDataConnectionDnsSecondaryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionDnsSecondaryCurrent.setStatus("current")


class _Hm2WwanDataConnectionMtu_Type(Integer32):
    """Custom type hm2WwanDataConnectionMtu based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(552, 1500),
    )


_Hm2WwanDataConnectionMtu_Type.__name__ = "Integer32"
_Hm2WwanDataConnectionMtu_Object = MibTableColumn
hm2WwanDataConnectionMtu = _Hm2WwanDataConnectionMtu_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 21),
    _Hm2WwanDataConnectionMtu_Type()
)
hm2WwanDataConnectionMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionMtu.setStatus("current")


class _Hm2WwanDataConnectionFailedRetry_Type(Integer32):
    """Custom type hm2WwanDataConnectionFailedRetry based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32),
    )


_Hm2WwanDataConnectionFailedRetry_Type.__name__ = "Integer32"
_Hm2WwanDataConnectionFailedRetry_Object = MibTableColumn
hm2WwanDataConnectionFailedRetry = _Hm2WwanDataConnectionFailedRetry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 22),
    _Hm2WwanDataConnectionFailedRetry_Type()
)
hm2WwanDataConnectionFailedRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionFailedRetry.setStatus("current")


class _Hm2WwanDataConnectionFailedRetryCurrent_Type(Integer32):
    """Custom type hm2WwanDataConnectionFailedRetryCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Hm2WwanDataConnectionFailedRetryCurrent_Type.__name__ = "Integer32"
_Hm2WwanDataConnectionFailedRetryCurrent_Object = MibTableColumn
hm2WwanDataConnectionFailedRetryCurrent = _Hm2WwanDataConnectionFailedRetryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 23),
    _Hm2WwanDataConnectionFailedRetryCurrent_Type()
)
hm2WwanDataConnectionFailedRetryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionFailedRetryCurrent.setStatus("current")
_Hm2WwanDataConnectionStatus_Type = Hm2ConnectionStatus
_Hm2WwanDataConnectionStatus_Object = MibTableColumn
hm2WwanDataConnectionStatus = _Hm2WwanDataConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 24),
    _Hm2WwanDataConnectionStatus_Type()
)
hm2WwanDataConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionStatus.setStatus("current")
_Hm2WwanDataConnectionStatusErrorReason_Type = HmLargeDisplayString
_Hm2WwanDataConnectionStatusErrorReason_Object = MibTableColumn
hm2WwanDataConnectionStatusErrorReason = _Hm2WwanDataConnectionStatusErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 25),
    _Hm2WwanDataConnectionStatusErrorReason_Type()
)
hm2WwanDataConnectionStatusErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionStatusErrorReason.setStatus("current")
_Hm2WwanDataConnectionActivatedCount_Type = Unsigned32
_Hm2WwanDataConnectionActivatedCount_Object = MibTableColumn
hm2WwanDataConnectionActivatedCount = _Hm2WwanDataConnectionActivatedCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 26),
    _Hm2WwanDataConnectionActivatedCount_Type()
)
hm2WwanDataConnectionActivatedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionActivatedCount.setStatus("current")
_Hm2WwanDataConnectionStartTime_Type = Unsigned32
_Hm2WwanDataConnectionStartTime_Object = MibTableColumn
hm2WwanDataConnectionStartTime = _Hm2WwanDataConnectionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 27),
    _Hm2WwanDataConnectionStartTime_Type()
)
hm2WwanDataConnectionStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionStartTime.setStatus("current")
_Hm2WwanDataConnectionUpTime_Type = Unsigned32
_Hm2WwanDataConnectionUpTime_Object = MibTableColumn
hm2WwanDataConnectionUpTime = _Hm2WwanDataConnectionUpTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 28),
    _Hm2WwanDataConnectionUpTime_Type()
)
hm2WwanDataConnectionUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionUpTime.setStatus("current")
_Hm2WwanDataConnectionTotalUpTime_Type = Unsigned32
_Hm2WwanDataConnectionTotalUpTime_Object = MibTableColumn
hm2WwanDataConnectionTotalUpTime = _Hm2WwanDataConnectionTotalUpTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 1, 1, 29),
    _Hm2WwanDataConnectionTotalUpTime_Type()
)
hm2WwanDataConnectionTotalUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanDataConnectionTotalUpTime.setStatus("current")
_Hm2WwanDataPlanTable_Object = MibTable
hm2WwanDataPlanTable = _Hm2WwanDataPlanTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hm2WwanDataPlanTable.setStatus("current")
_Hm2WwanDataPlanEntry_Object = MibTableRow
hm2WwanDataPlanEntry = _Hm2WwanDataPlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 2, 1)
)
hm2WwanDataPlanEntry.setIndexNames(
    (0, "HM2-WWAN-MIB", "hm2WwanDataPlanSimId"),
)
if mibBuilder.loadTexts:
    hm2WwanDataPlanEntry.setStatus("current")


class _Hm2WwanDataPlanSimId_Type(Integer32):
    """Custom type hm2WwanDataPlanSimId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Hm2WwanDataPlanSimId_Type.__name__ = "Integer32"
_Hm2WwanDataPlanSimId_Object = MibTableColumn
hm2WwanDataPlanSimId = _Hm2WwanDataPlanSimId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 2, 1, 1),
    _Hm2WwanDataPlanSimId_Type()
)
hm2WwanDataPlanSimId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2WwanDataPlanSimId.setStatus("current")


class _Hm2WwanDataPlanMonthlyLimit_Type(Unsigned32):
    """Custom type hm2WwanDataPlanMonthlyLimit based on Unsigned32"""
    defaultValue = 0


_Hm2WwanDataPlanMonthlyLimit_Object = MibTableColumn
hm2WwanDataPlanMonthlyLimit = _Hm2WwanDataPlanMonthlyLimit_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 2, 1, 2),
    _Hm2WwanDataPlanMonthlyLimit_Type()
)
hm2WwanDataPlanMonthlyLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanDataPlanMonthlyLimit.setStatus("current")


class _Hm2WwanDataPlanLimitMeasureUnit_Type(Hm2LimitUnit):
    """Custom type hm2WwanDataPlanLimitMeasureUnit based on Hm2LimitUnit"""


_Hm2WwanDataPlanLimitMeasureUnit_Object = MibTableColumn
hm2WwanDataPlanLimitMeasureUnit = _Hm2WwanDataPlanLimitMeasureUnit_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 2, 1, 3),
    _Hm2WwanDataPlanLimitMeasureUnit_Type()
)
hm2WwanDataPlanLimitMeasureUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanDataPlanLimitMeasureUnit.setStatus("current")


class _Hm2WwanDataPlanWarningThreshold_Type(Integer32):
    """Custom type hm2WwanDataPlanWarningThreshold based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hm2WwanDataPlanWarningThreshold_Type.__name__ = "Integer32"
_Hm2WwanDataPlanWarningThreshold_Object = MibTableColumn
hm2WwanDataPlanWarningThreshold = _Hm2WwanDataPlanWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 2, 1, 4),
    _Hm2WwanDataPlanWarningThreshold_Type()
)
hm2WwanDataPlanWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanDataPlanWarningThreshold.setStatus("current")


class _Hm2WwanDataPlanReset_Type(HmActionValue):
    """Custom type hm2WwanDataPlanReset based on HmActionValue"""


_Hm2WwanDataPlanReset_Object = MibTableColumn
hm2WwanDataPlanReset = _Hm2WwanDataPlanReset_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 2, 1, 5),
    _Hm2WwanDataPlanReset_Type()
)
hm2WwanDataPlanReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanDataPlanReset.setStatus("current")


class _Hm2WwanDataPlanResetDay_Type(Integer32):
    """Custom type hm2WwanDataPlanResetDay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Hm2WwanDataPlanResetDay_Type.__name__ = "Integer32"
_Hm2WwanDataPlanResetDay_Object = MibTableColumn
hm2WwanDataPlanResetDay = _Hm2WwanDataPlanResetDay_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 2, 1, 6),
    _Hm2WwanDataPlanResetDay_Type()
)
hm2WwanDataPlanResetDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanDataPlanResetDay.setStatus("current")
_Hm2WwanDataPlanLastReset_Type = HmTimeSeconds1970
_Hm2WwanDataPlanLastReset_Object = MibTableColumn
hm2WwanDataPlanLastReset = _Hm2WwanDataPlanLastReset_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 2, 1, 7),
    _Hm2WwanDataPlanLastReset_Type()
)
hm2WwanDataPlanLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanDataPlanLastReset.setStatus("current")


class _Hm2WwanDataPlanCutoffThreshold_Type(Integer32):
    """Custom type hm2WwanDataPlanCutoffThreshold based on Integer32"""
    defaultValue = 100


_Hm2WwanDataPlanCutoffThreshold_Object = MibTableColumn
hm2WwanDataPlanCutoffThreshold = _Hm2WwanDataPlanCutoffThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 2, 1, 8),
    _Hm2WwanDataPlanCutoffThreshold_Type()
)
hm2WwanDataPlanCutoffThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanDataPlanCutoffThreshold.setStatus("current")
_Hm2WwanDataPlanMonthlyUsageTx_Type = Counter64
_Hm2WwanDataPlanMonthlyUsageTx_Object = MibTableColumn
hm2WwanDataPlanMonthlyUsageTx = _Hm2WwanDataPlanMonthlyUsageTx_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 2, 1, 9),
    _Hm2WwanDataPlanMonthlyUsageTx_Type()
)
hm2WwanDataPlanMonthlyUsageTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanDataPlanMonthlyUsageTx.setStatus("current")
_Hm2WwanDataPlanMonthlyUsageRx_Type = Counter64
_Hm2WwanDataPlanMonthlyUsageRx_Object = MibTableColumn
hm2WwanDataPlanMonthlyUsageRx = _Hm2WwanDataPlanMonthlyUsageRx_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 2, 1, 10),
    _Hm2WwanDataPlanMonthlyUsageRx_Type()
)
hm2WwanDataPlanMonthlyUsageRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanDataPlanMonthlyUsageRx.setStatus("current")
_Hm2WwanDataPacketStatsTable_Object = MibTable
hm2WwanDataPacketStatsTable = _Hm2WwanDataPacketStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hm2WwanDataPacketStatsTable.setStatus("current")
_Hm2WwanDataPacketStatsEntry_Object = MibTableRow
hm2WwanDataPacketStatsEntry = _Hm2WwanDataPacketStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 3, 1)
)
hm2WwanDataPacketStatsEntry.setIndexNames(
    (0, "HM2-WWAN-MIB", "hm2WwanDataPacketStatsSimId"),
)
if mibBuilder.loadTexts:
    hm2WwanDataPacketStatsEntry.setStatus("current")


class _Hm2WwanDataPacketStatsSimId_Type(Integer32):
    """Custom type hm2WwanDataPacketStatsSimId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Hm2WwanDataPacketStatsSimId_Type.__name__ = "Integer32"
_Hm2WwanDataPacketStatsSimId_Object = MibTableColumn
hm2WwanDataPacketStatsSimId = _Hm2WwanDataPacketStatsSimId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 3, 1, 1),
    _Hm2WwanDataPacketStatsSimId_Type()
)
hm2WwanDataPacketStatsSimId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2WwanDataPacketStatsSimId.setStatus("current")
_Hm2WwanDataPacketStatsTxOk_Type = Counter64
_Hm2WwanDataPacketStatsTxOk_Object = MibTableColumn
hm2WwanDataPacketStatsTxOk = _Hm2WwanDataPacketStatsTxOk_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 3, 1, 2),
    _Hm2WwanDataPacketStatsTxOk_Type()
)
hm2WwanDataPacketStatsTxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanDataPacketStatsTxOk.setStatus("current")
_Hm2WwanDataPacketStatsRxOk_Type = Counter64
_Hm2WwanDataPacketStatsRxOk_Object = MibTableColumn
hm2WwanDataPacketStatsRxOk = _Hm2WwanDataPacketStatsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 3, 1, 3),
    _Hm2WwanDataPacketStatsRxOk_Type()
)
hm2WwanDataPacketStatsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanDataPacketStatsRxOk.setStatus("current")
_Hm2WwanDataPacketStatsTxErrors_Type = Counter64
_Hm2WwanDataPacketStatsTxErrors_Object = MibTableColumn
hm2WwanDataPacketStatsTxErrors = _Hm2WwanDataPacketStatsTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 3, 1, 4),
    _Hm2WwanDataPacketStatsTxErrors_Type()
)
hm2WwanDataPacketStatsTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanDataPacketStatsTxErrors.setStatus("current")
_Hm2WwanDataPacketStatsRxErrors_Type = Counter64
_Hm2WwanDataPacketStatsRxErrors_Object = MibTableColumn
hm2WwanDataPacketStatsRxErrors = _Hm2WwanDataPacketStatsRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 3, 1, 5),
    _Hm2WwanDataPacketStatsRxErrors_Type()
)
hm2WwanDataPacketStatsRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanDataPacketStatsRxErrors.setStatus("current")
_Hm2WwanDataPacketStatsTxOverflows_Type = Counter64
_Hm2WwanDataPacketStatsTxOverflows_Object = MibTableColumn
hm2WwanDataPacketStatsTxOverflows = _Hm2WwanDataPacketStatsTxOverflows_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 3, 1, 6),
    _Hm2WwanDataPacketStatsTxOverflows_Type()
)
hm2WwanDataPacketStatsTxOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanDataPacketStatsTxOverflows.setStatus("current")
_Hm2WwanDataPacketStatsRxOverflows_Type = Counter64
_Hm2WwanDataPacketStatsRxOverflows_Object = MibTableColumn
hm2WwanDataPacketStatsRxOverflows = _Hm2WwanDataPacketStatsRxOverflows_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 3, 1, 7),
    _Hm2WwanDataPacketStatsRxOverflows_Type()
)
hm2WwanDataPacketStatsRxOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanDataPacketStatsRxOverflows.setStatus("current")
_Hm2WwanDataPacketStatsTxBytesOk_Type = Counter64
_Hm2WwanDataPacketStatsTxBytesOk_Object = MibTableColumn
hm2WwanDataPacketStatsTxBytesOk = _Hm2WwanDataPacketStatsTxBytesOk_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 3, 1, 8),
    _Hm2WwanDataPacketStatsTxBytesOk_Type()
)
hm2WwanDataPacketStatsTxBytesOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanDataPacketStatsTxBytesOk.setStatus("current")
_Hm2WwanDataPacketStatsRxBytesOk_Type = Counter64
_Hm2WwanDataPacketStatsRxBytesOk_Object = MibTableColumn
hm2WwanDataPacketStatsRxBytesOk = _Hm2WwanDataPacketStatsRxBytesOk_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 3, 1, 9),
    _Hm2WwanDataPacketStatsRxBytesOk_Type()
)
hm2WwanDataPacketStatsRxBytesOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanDataPacketStatsRxBytesOk.setStatus("current")
_Hm2WwanDataPacketStatsTxDropped_Type = Counter64
_Hm2WwanDataPacketStatsTxDropped_Object = MibTableColumn
hm2WwanDataPacketStatsTxDropped = _Hm2WwanDataPacketStatsTxDropped_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 3, 1, 10),
    _Hm2WwanDataPacketStatsTxDropped_Type()
)
hm2WwanDataPacketStatsTxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanDataPacketStatsTxDropped.setStatus("current")
_Hm2WwanDataPacketStatsRxDropped_Type = Counter64
_Hm2WwanDataPacketStatsRxDropped_Object = MibTableColumn
hm2WwanDataPacketStatsRxDropped = _Hm2WwanDataPacketStatsRxDropped_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 2, 3, 1, 11),
    _Hm2WwanDataPacketStatsRxDropped_Type()
)
hm2WwanDataPacketStatsRxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanDataPacketStatsRxDropped.setStatus("current")
_Hm2WwanSimCardGroup_ObjectIdentity = ObjectIdentity
hm2WwanSimCardGroup = _Hm2WwanSimCardGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 3)
)
_Hm2WwanSimCardTable_Object = MibTable
hm2WwanSimCardTable = _Hm2WwanSimCardTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hm2WwanSimCardTable.setStatus("current")
_Hm2WwanSimCardEntry_Object = MibTableRow
hm2WwanSimCardEntry = _Hm2WwanSimCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 3, 1, 1)
)
hm2WwanSimCardEntry.setIndexNames(
    (0, "HM2-WWAN-MIB", "hm2WwanSimCardSimId"),
)
if mibBuilder.loadTexts:
    hm2WwanSimCardEntry.setStatus("current")


class _Hm2WwanSimCardSimId_Type(Integer32):
    """Custom type hm2WwanSimCardSimId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Hm2WwanSimCardSimId_Type.__name__ = "Integer32"
_Hm2WwanSimCardSimId_Object = MibTableColumn
hm2WwanSimCardSimId = _Hm2WwanSimCardSimId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 3, 1, 1, 1),
    _Hm2WwanSimCardSimId_Type()
)
hm2WwanSimCardSimId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2WwanSimCardSimId.setStatus("current")


class _Hm2WwanSimCardAdminStatus_Type(HmEnabledStatus):
    """Custom type hm2WwanSimCardAdminStatus based on HmEnabledStatus"""


_Hm2WwanSimCardAdminStatus_Object = MibTableColumn
hm2WwanSimCardAdminStatus = _Hm2WwanSimCardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 3, 1, 1, 2),
    _Hm2WwanSimCardAdminStatus_Type()
)
hm2WwanSimCardAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanSimCardAdminStatus.setStatus("current")


class _Hm2WwanSimCardRole_Type(Hm2SimCardRole):
    """Custom type hm2WwanSimCardRole based on Hm2SimCardRole"""


_Hm2WwanSimCardRole_Object = MibTableColumn
hm2WwanSimCardRole = _Hm2WwanSimCardRole_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 3, 1, 1, 3),
    _Hm2WwanSimCardRole_Type()
)
hm2WwanSimCardRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanSimCardRole.setStatus("current")
_Hm2WwanSimCardRoleCurrent_Type = Hm2SimCardRole
_Hm2WwanSimCardRoleCurrent_Object = MibTableColumn
hm2WwanSimCardRoleCurrent = _Hm2WwanSimCardRoleCurrent_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 3, 1, 1, 4),
    _Hm2WwanSimCardRoleCurrent_Type()
)
hm2WwanSimCardRoleCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanSimCardRoleCurrent.setStatus("current")
_Hm2WwanSimCardStatus_Type = Hm2SimCardStatus
_Hm2WwanSimCardStatus_Object = MibTableColumn
hm2WwanSimCardStatus = _Hm2WwanSimCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 3, 1, 1, 5),
    _Hm2WwanSimCardStatus_Type()
)
hm2WwanSimCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanSimCardStatus.setStatus("current")


class _Hm2WwanSimCardSetActive_Type(HmActionValue):
    """Custom type hm2WwanSimCardSetActive based on HmActionValue"""


_Hm2WwanSimCardSetActive_Object = MibTableColumn
hm2WwanSimCardSetActive = _Hm2WwanSimCardSetActive_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 3, 1, 1, 6),
    _Hm2WwanSimCardSetActive_Type()
)
hm2WwanSimCardSetActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanSimCardSetActive.setStatus("current")


class _Hm2WwanSimCardPin1_Type(SnmpAdminString):
    """Custom type hm2WwanSimCardPin1 based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 8),
    )


_Hm2WwanSimCardPin1_Type.__name__ = "SnmpAdminString"
_Hm2WwanSimCardPin1_Object = MibTableColumn
hm2WwanSimCardPin1 = _Hm2WwanSimCardPin1_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 3, 1, 1, 7),
    _Hm2WwanSimCardPin1_Type()
)
hm2WwanSimCardPin1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanSimCardPin1.setStatus("current")
_Hm2WwanSimCardPin1Mode_Type = HmEnabledStatus
_Hm2WwanSimCardPin1Mode_Object = MibTableColumn
hm2WwanSimCardPin1Mode = _Hm2WwanSimCardPin1Mode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 3, 1, 1, 8),
    _Hm2WwanSimCardPin1Mode_Type()
)
hm2WwanSimCardPin1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanSimCardPin1Mode.setStatus("current")
_Hm2WwanSimCardPin1Status_Type = Hm2Pin1Status
_Hm2WwanSimCardPin1Status_Object = MibTableColumn
hm2WwanSimCardPin1Status = _Hm2WwanSimCardPin1Status_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 3, 1, 1, 9),
    _Hm2WwanSimCardPin1Status_Type()
)
hm2WwanSimCardPin1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanSimCardPin1Status.setStatus("current")
_Hm2WwanSimCardPin1VerifyTries_Type = Integer32
_Hm2WwanSimCardPin1VerifyTries_Object = MibTableColumn
hm2WwanSimCardPin1VerifyTries = _Hm2WwanSimCardPin1VerifyTries_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 3, 1, 1, 10),
    _Hm2WwanSimCardPin1VerifyTries_Type()
)
hm2WwanSimCardPin1VerifyTries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanSimCardPin1VerifyTries.setStatus("current")
_Hm2WwanSimCardPin1UnblockTries_Type = Integer32
_Hm2WwanSimCardPin1UnblockTries_Object = MibTableColumn
hm2WwanSimCardPin1UnblockTries = _Hm2WwanSimCardPin1UnblockTries_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 3, 1, 1, 11),
    _Hm2WwanSimCardPin1UnblockTries_Type()
)
hm2WwanSimCardPin1UnblockTries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanSimCardPin1UnblockTries.setStatus("current")


class _Hm2WwanSimCardPuk1_Type(SnmpAdminString):
    """Custom type hm2WwanSimCardPuk1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Hm2WwanSimCardPuk1_Type.__name__ = "SnmpAdminString"
_Hm2WwanSimCardPuk1_Object = MibTableColumn
hm2WwanSimCardPuk1 = _Hm2WwanSimCardPuk1_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 3, 1, 1, 12),
    _Hm2WwanSimCardPuk1_Type()
)
hm2WwanSimCardPuk1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanSimCardPuk1.setStatus("current")


class _Hm2WwanSimCardRoamingMode_Type(HmEnabledStatus):
    """Custom type hm2WwanSimCardRoamingMode based on HmEnabledStatus"""


_Hm2WwanSimCardRoamingMode_Object = MibTableColumn
hm2WwanSimCardRoamingMode = _Hm2WwanSimCardRoamingMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 3, 1, 1, 13),
    _Hm2WwanSimCardRoamingMode_Type()
)
hm2WwanSimCardRoamingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanSimCardRoamingMode.setStatus("current")


class _Hm2WwanSimCardIccid_Type(SnmpAdminString):
    """Custom type hm2WwanSimCardIccid based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(22, 22),
    )


_Hm2WwanSimCardIccid_Type.__name__ = "SnmpAdminString"
_Hm2WwanSimCardIccid_Object = MibTableColumn
hm2WwanSimCardIccid = _Hm2WwanSimCardIccid_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 3, 1, 1, 14),
    _Hm2WwanSimCardIccid_Type()
)
hm2WwanSimCardIccid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WwanSimCardIccid.setStatus("current")


class _Hm2WwanSimCardImsi_Type(SnmpAdminString):
    """Custom type hm2WwanSimCardImsi based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(15, 15),
    )


_Hm2WwanSimCardImsi_Type.__name__ = "SnmpAdminString"
_Hm2WwanSimCardImsi_Object = MibTableColumn
hm2WwanSimCardImsi = _Hm2WwanSimCardImsi_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 3, 1, 1, 15),
    _Hm2WwanSimCardImsi_Type()
)
hm2WwanSimCardImsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanSimCardImsi.setStatus("current")
_Hm2WwanInformationGroup_ObjectIdentity = ObjectIdentity
hm2WwanInformationGroup = _Hm2WwanInformationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4)
)
_Hm2WwanCellularInformationGroup_ObjectIdentity = ObjectIdentity
hm2WwanCellularInformationGroup = _Hm2WwanCellularInformationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4, 1)
)


class _Hm2WwanCellularActiveSimId_Type(Integer32):
    """Custom type hm2WwanCellularActiveSimId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Hm2WwanCellularActiveSimId_Type.__name__ = "Integer32"
_Hm2WwanCellularActiveSimId_Object = MibScalar
hm2WwanCellularActiveSimId = _Hm2WwanCellularActiveSimId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4, 1, 1),
    _Hm2WwanCellularActiveSimId_Type()
)
hm2WwanCellularActiveSimId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanCellularActiveSimId.setStatus("current")
_Hm2WwanCellularRegistration_Type = Hm2RegistrationStatus
_Hm2WwanCellularRegistration_Object = MibScalar
hm2WwanCellularRegistration = _Hm2WwanCellularRegistration_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4, 1, 2),
    _Hm2WwanCellularRegistration_Type()
)
hm2WwanCellularRegistration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanCellularRegistration.setStatus("current")


class _Hm2WwanCellularOperator_Type(SnmpAdminString):
    """Custom type hm2WwanCellularOperator based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2WwanCellularOperator_Type.__name__ = "SnmpAdminString"
_Hm2WwanCellularOperator_Object = MibScalar
hm2WwanCellularOperator = _Hm2WwanCellularOperator_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4, 1, 3),
    _Hm2WwanCellularOperator_Type()
)
hm2WwanCellularOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanCellularOperator.setStatus("current")
_Hm2WwanCellularNetwork_Type = Hm2CellularNetworks
_Hm2WwanCellularNetwork_Object = MibScalar
hm2WwanCellularNetwork = _Hm2WwanCellularNetwork_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4, 1, 4),
    _Hm2WwanCellularNetwork_Type()
)
hm2WwanCellularNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanCellularNetwork.setStatus("current")
_Hm2WwanCellularMcc_Type = Integer32
_Hm2WwanCellularMcc_Object = MibScalar
hm2WwanCellularMcc = _Hm2WwanCellularMcc_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4, 1, 5),
    _Hm2WwanCellularMcc_Type()
)
hm2WwanCellularMcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanCellularMcc.setStatus("current")
_Hm2WwanCellularMnc_Type = Integer32
_Hm2WwanCellularMnc_Object = MibScalar
hm2WwanCellularMnc = _Hm2WwanCellularMnc_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4, 1, 6),
    _Hm2WwanCellularMnc_Type()
)
hm2WwanCellularMnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanCellularMnc.setStatus("current")
_Hm2WwanCellularLac_Type = Integer32
_Hm2WwanCellularLac_Object = MibScalar
hm2WwanCellularLac = _Hm2WwanCellularLac_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4, 1, 7),
    _Hm2WwanCellularLac_Type()
)
hm2WwanCellularLac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanCellularLac.setStatus("current")
_Hm2WwanCellularBsic_Type = Integer32
_Hm2WwanCellularBsic_Object = MibScalar
hm2WwanCellularBsic = _Hm2WwanCellularBsic_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4, 1, 8),
    _Hm2WwanCellularBsic_Type()
)
hm2WwanCellularBsic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanCellularBsic.setStatus("current")
_Hm2WwanCellularCellId_Type = Integer32
_Hm2WwanCellularCellId_Object = MibScalar
hm2WwanCellularCellId = _Hm2WwanCellularCellId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4, 1, 9),
    _Hm2WwanCellularCellId_Type()
)
hm2WwanCellularCellId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanCellularCellId.setStatus("current")
_Hm2WwanCellularBand_Type = Integer32
_Hm2WwanCellularBand_Object = MibScalar
hm2WwanCellularBand = _Hm2WwanCellularBand_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4, 1, 10),
    _Hm2WwanCellularBand_Type()
)
hm2WwanCellularBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanCellularBand.setStatus("current")
_Hm2WwanCellularChannel_Type = Integer32
_Hm2WwanCellularChannel_Object = MibScalar
hm2WwanCellularChannel = _Hm2WwanCellularChannel_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4, 1, 11),
    _Hm2WwanCellularChannel_Type()
)
hm2WwanCellularChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanCellularChannel.setStatus("current")
_Hm2WwanCellularSignalStrength_Type = Integer32
_Hm2WwanCellularSignalStrength_Object = MibScalar
hm2WwanCellularSignalStrength = _Hm2WwanCellularSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4, 1, 12),
    _Hm2WwanCellularSignalStrength_Type()
)
hm2WwanCellularSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanCellularSignalStrength.setStatus("current")
_Hm2WwanCellularSignalStrengthLte_Type = Integer32
_Hm2WwanCellularSignalStrengthLte_Object = MibScalar
hm2WwanCellularSignalStrengthLte = _Hm2WwanCellularSignalStrengthLte_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4, 1, 13),
    _Hm2WwanCellularSignalStrengthLte_Type()
)
hm2WwanCellularSignalStrengthLte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanCellularSignalStrengthLte.setStatus("current")
_Hm2WwanCellularSignalQuality_Type = Integer32
_Hm2WwanCellularSignalQuality_Object = MibScalar
hm2WwanCellularSignalQuality = _Hm2WwanCellularSignalQuality_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4, 1, 14),
    _Hm2WwanCellularSignalQuality_Type()
)
hm2WwanCellularSignalQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanCellularSignalQuality.setStatus("current")
_Hm2WwanCellularSignalQualityLte_Type = Integer32
_Hm2WwanCellularSignalQualityLte_Object = MibScalar
hm2WwanCellularSignalQualityLte = _Hm2WwanCellularSignalQualityLte_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4, 1, 15),
    _Hm2WwanCellularSignalQualityLte_Type()
)
hm2WwanCellularSignalQualityLte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanCellularSignalQualityLte.setStatus("current")
_Hm2WwanCellularRscp_Type = Integer32
_Hm2WwanCellularRscp_Object = MibScalar
hm2WwanCellularRscp = _Hm2WwanCellularRscp_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4, 1, 16),
    _Hm2WwanCellularRscp_Type()
)
hm2WwanCellularRscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanCellularRscp.setStatus("current")
_Hm2WwanCellularRoamingStatus_Type = Hm2RoamingStatus
_Hm2WwanCellularRoamingStatus_Object = MibScalar
hm2WwanCellularRoamingStatus = _Hm2WwanCellularRoamingStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4, 1, 17),
    _Hm2WwanCellularRoamingStatus_Type()
)
hm2WwanCellularRoamingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanCellularRoamingStatus.setStatus("current")
_Hm2WwanCellularBitErrorRate_Type = Integer32
_Hm2WwanCellularBitErrorRate_Object = MibScalar
hm2WwanCellularBitErrorRate = _Hm2WwanCellularBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4, 1, 18),
    _Hm2WwanCellularBitErrorRate_Type()
)
hm2WwanCellularBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanCellularBitErrorRate.setStatus("current")
_Hm2WwanCellularCurrentTxRate_Type = Unsigned32
_Hm2WwanCellularCurrentTxRate_Object = MibScalar
hm2WwanCellularCurrentTxRate = _Hm2WwanCellularCurrentTxRate_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4, 1, 19),
    _Hm2WwanCellularCurrentTxRate_Type()
)
hm2WwanCellularCurrentTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanCellularCurrentTxRate.setStatus("current")
_Hm2WwanCellularCurrentRxRate_Type = Unsigned32
_Hm2WwanCellularCurrentRxRate_Object = MibScalar
hm2WwanCellularCurrentRxRate = _Hm2WwanCellularCurrentRxRate_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4, 1, 20),
    _Hm2WwanCellularCurrentRxRate_Type()
)
hm2WwanCellularCurrentRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanCellularCurrentRxRate.setStatus("current")
_Hm2WwanCellularMaxTxRate_Type = Unsigned32
_Hm2WwanCellularMaxTxRate_Object = MibScalar
hm2WwanCellularMaxTxRate = _Hm2WwanCellularMaxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4, 1, 21),
    _Hm2WwanCellularMaxTxRate_Type()
)
hm2WwanCellularMaxTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanCellularMaxTxRate.setStatus("current")
_Hm2WwanCellularMaxRxRate_Type = Unsigned32
_Hm2WwanCellularMaxRxRate_Object = MibScalar
hm2WwanCellularMaxRxRate = _Hm2WwanCellularMaxRxRate_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4, 1, 22),
    _Hm2WwanCellularMaxRxRate_Type()
)
hm2WwanCellularMaxRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanCellularMaxRxRate.setStatus("current")
_Hm2WwanModemInformationGroup_ObjectIdentity = ObjectIdentity
hm2WwanModemInformationGroup = _Hm2WwanModemInformationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4, 2)
)


class _Hm2WwanModemManufacturer_Type(SnmpAdminString):
    """Custom type hm2WwanModemManufacturer based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2WwanModemManufacturer_Type.__name__ = "SnmpAdminString"
_Hm2WwanModemManufacturer_Object = MibScalar
hm2WwanModemManufacturer = _Hm2WwanModemManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4, 2, 1),
    _Hm2WwanModemManufacturer_Type()
)
hm2WwanModemManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanModemManufacturer.setStatus("current")


class _Hm2WwanModemModel_Type(SnmpAdminString):
    """Custom type hm2WwanModemModel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hm2WwanModemModel_Type.__name__ = "SnmpAdminString"
_Hm2WwanModemModel_Object = MibScalar
hm2WwanModemModel = _Hm2WwanModemModel_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4, 2, 2),
    _Hm2WwanModemModel_Type()
)
hm2WwanModemModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanModemModel.setStatus("current")


class _Hm2WwanModemRevision_Type(SnmpAdminString):
    """Custom type hm2WwanModemRevision based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2WwanModemRevision_Type.__name__ = "SnmpAdminString"
_Hm2WwanModemRevision_Object = MibScalar
hm2WwanModemRevision = _Hm2WwanModemRevision_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4, 2, 3),
    _Hm2WwanModemRevision_Type()
)
hm2WwanModemRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanModemRevision.setStatus("current")


class _Hm2WwanModemImei_Type(SnmpAdminString):
    """Custom type hm2WwanModemImei based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Hm2WwanModemImei_Type.__name__ = "SnmpAdminString"
_Hm2WwanModemImei_Object = MibScalar
hm2WwanModemImei = _Hm2WwanModemImei_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 1, 4, 2, 4),
    _Hm2WwanModemImei_Type()
)
hm2WwanModemImei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WwanModemImei.setStatus("current")

# Managed Objects groups


# Notification objects

hm2WwanRoamingActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 0, 1)
)
hm2WwanRoamingActiveTrap.setObjects(
      *(("HM2-WWAN-MIB", "hm2WwanCellularRoamingStatus"),
        ("HM2-WWAN-MIB", "hm2WwanCellularOperator"),
        ("HM2-WWAN-MIB", "hm2WwanCellularActiveSimId"))
)
if mibBuilder.loadTexts:
    hm2WwanRoamingActiveTrap.setStatus(
        "current"
    )

hm2WwanLtePersistenceSwitchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 0, 2)
)
hm2WwanLtePersistenceSwitchTrap.setObjects(
      *(("HM2-WWAN-MIB", "hm2WwanLtePersistence"),
        ("HM2-WWAN-MIB", "hm2WwanLtePersistenceInterval"),
        ("HM2-WWAN-MIB", "hm2WwanCellularActiveSimId"))
)
if mibBuilder.loadTexts:
    hm2WwanLtePersistenceSwitchTrap.setStatus(
        "current"
    )

hm2WwanCelluarRegistrationFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 0, 3)
)
hm2WwanCelluarRegistrationFailedTrap.setObjects(
      *(("HM2-WWAN-MIB", "hm2WwanCellularRegistration"),
        ("HM2-WWAN-MIB", "hm2WwanCellularActiveSimId"))
)
if mibBuilder.loadTexts:
    hm2WwanCelluarRegistrationFailedTrap.setStatus(
        "current"
    )

hm2WwanDataConnectionSetupTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 0, 4)
)
hm2WwanDataConnectionSetupTrap.setObjects(
      *(("HM2-WWAN-MIB", "hm2WwanDataConnectionStatus"),
        ("HM2-WWAN-MIB", "hm2WwanCellularActiveSimId"),
        ("HM2-WWAN-MIB", "hm2WwanDataConnectionApnCurrent"))
)
if mibBuilder.loadTexts:
    hm2WwanDataConnectionSetupTrap.setStatus(
        "current"
    )

hm2WwanDataPlanWarningThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 0, 5)
)
hm2WwanDataPlanWarningThresholdTrap.setObjects(
      *(("HM2-WWAN-MIB", "hm2WwanDataPlanWarningThreshold"),
        ("HM2-WWAN-MIB", "hm2WwanCellularActiveSimId"),
        ("HM2-WWAN-MIB", "hm2WwanDataPlanMonthlyLimit"),
        ("HM2-WWAN-MIB", "hm2WwanDataPlanLimitMeasureUnit"),
        ("HM2-WWAN-MIB", "hm2WwanDataPlanMonthlyUsageTx"),
        ("HM2-WWAN-MIB", "hm2WwanDataPlanMonthlyUsageRx"))
)
if mibBuilder.loadTexts:
    hm2WwanDataPlanWarningThresholdTrap.setStatus(
        "current"
    )

hm2WwanSimCardPin1StatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 0, 6)
)
hm2WwanSimCardPin1StatusTrap.setObjects(
      *(("HM2-WWAN-MIB", "hm2WwanSimCardPin1Status"),
        ("HM2-WWAN-MIB", "hm2WwanCellularActiveSimId"),
        ("HM2-WWAN-MIB", "hm2WwanSimCardRoleCurrent"),
        ("HM2-WWAN-MIB", "hm2WwanSimCardStatus"))
)
if mibBuilder.loadTexts:
    hm2WwanSimCardPin1StatusTrap.setStatus(
        "current"
    )

hm2WwanBackupSimFailoverConnectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 0, 7)
)
hm2WwanBackupSimFailoverConnectionTrap.setObjects(
      *(("HM2-WWAN-MIB", "hm2WwanCellularActiveSimId"),
        ("HM2-WWAN-MIB", "hm2WwanSimCardRoleCurrent"))
)
if mibBuilder.loadTexts:
    hm2WwanBackupSimFailoverConnectionTrap.setStatus(
        "current"
    )

hm2WwanBackupSimFailoverRegistrationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 0, 8)
)
hm2WwanBackupSimFailoverRegistrationTrap.setObjects(
      *(("HM2-WWAN-MIB", "hm2WwanCellularActiveSimId"),
        ("HM2-WWAN-MIB", "hm2WwanSimCardRoleCurrent"))
)
if mibBuilder.loadTexts:
    hm2WwanBackupSimFailoverRegistrationTrap.setStatus(
        "current"
    )

hm2WwanBackupSimFailoverRoamingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 0, 9)
)
hm2WwanBackupSimFailoverRoamingTrap.setObjects(
      *(("HM2-WWAN-MIB", "hm2WwanCellularActiveSimId"),
        ("HM2-WWAN-MIB", "hm2WwanSimCardRoleCurrent"))
)
if mibBuilder.loadTexts:
    hm2WwanBackupSimFailoverRoamingTrap.setStatus(
        "current"
    )

hm2WwanBackupSimFailoverDataLimitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 0, 10)
)
hm2WwanBackupSimFailoverDataLimitTrap.setObjects(
      *(("HM2-WWAN-MIB", "hm2WwanCellularActiveSimId"),
        ("HM2-WWAN-MIB", "hm2WwanSimCardRoleCurrent"))
)
if mibBuilder.loadTexts:
    hm2WwanBackupSimFailoverDataLimitTrap.setStatus(
        "current"
    )

hm2WwanModemResetFailoverRegistrationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 125, 0, 11)
)
hm2WwanModemResetFailoverRegistrationTrap.setObjects(
      *(("HM2-WWAN-MIB", "hm2WwanCellularActiveSimId"),
        ("HM2-WWAN-MIB", "hm2WwanSimCardRoleCurrent"))
)
if mibBuilder.loadTexts:
    hm2WwanModemResetFailoverRegistrationTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-WWAN-MIB",
    **{"Hm2CellularNetworks": Hm2CellularNetworks,
       "Hm2TechnologyLevel": Hm2TechnologyLevel,
       "Hm2AuthType": Hm2AuthType,
       "Hm2PdpType": Hm2PdpType,
       "Hm2ConnectionStatus": Hm2ConnectionStatus,
       "Hm2LimitUnit": Hm2LimitUnit,
       "Hm2SimCardRole": Hm2SimCardRole,
       "Hm2SimCardStatus": Hm2SimCardStatus,
       "Hm2Pin1Status": Hm2Pin1Status,
       "Hm2RegistrationStatus": Hm2RegistrationStatus,
       "Hm2RoamingStatus": Hm2RoamingStatus,
       "Hm2TrapBits": Hm2TrapBits,
       "hm2WwanMib": hm2WwanMib,
       "hm2WwanMibNotifications": hm2WwanMibNotifications,
       "hm2WwanRoamingActiveTrap": hm2WwanRoamingActiveTrap,
       "hm2WwanLtePersistenceSwitchTrap": hm2WwanLtePersistenceSwitchTrap,
       "hm2WwanCelluarRegistrationFailedTrap": hm2WwanCelluarRegistrationFailedTrap,
       "hm2WwanDataConnectionSetupTrap": hm2WwanDataConnectionSetupTrap,
       "hm2WwanDataPlanWarningThresholdTrap": hm2WwanDataPlanWarningThresholdTrap,
       "hm2WwanSimCardPin1StatusTrap": hm2WwanSimCardPin1StatusTrap,
       "hm2WwanBackupSimFailoverConnectionTrap": hm2WwanBackupSimFailoverConnectionTrap,
       "hm2WwanBackupSimFailoverRegistrationTrap": hm2WwanBackupSimFailoverRegistrationTrap,
       "hm2WwanBackupSimFailoverRoamingTrap": hm2WwanBackupSimFailoverRoamingTrap,
       "hm2WwanBackupSimFailoverDataLimitTrap": hm2WwanBackupSimFailoverDataLimitTrap,
       "hm2WwanModemResetFailoverRegistrationTrap": hm2WwanModemResetFailoverRegistrationTrap,
       "hm2WwanMibObjects": hm2WwanMibObjects,
       "hm2WwanGeneralGroup": hm2WwanGeneralGroup,
       "hm2WwanAdminStatus": hm2WwanAdminStatus,
       "hm2WwanCellularSelection": hm2WwanCellularSelection,
       "hm2WwanLtePersistence": hm2WwanLtePersistence,
       "hm2WwanLtePersistenceInterval": hm2WwanLtePersistenceInterval,
       "hm2WwanFailoverTechnologyLevel": hm2WwanFailoverTechnologyLevel,
       "hm2WwanBackupSimFailoverConnection": hm2WwanBackupSimFailoverConnection,
       "hm2WwanBackupSimFailoverRegistration": hm2WwanBackupSimFailoverRegistration,
       "hm2WwanBackupSimFailoverRoaming": hm2WwanBackupSimFailoverRoaming,
       "hm2WwanBackupSimFailoverDataLimit": hm2WwanBackupSimFailoverDataLimit,
       "hm2WwanModemResetFailoverRegistration": hm2WwanModemResetFailoverRegistration,
       "hm2WwanBackupSimTechnologyLevel": hm2WwanBackupSimTechnologyLevel,
       "hm2WwanFailoverCycle": hm2WwanFailoverCycle,
       "hm2WwanSetTrap": hm2WwanSetTrap,
       "hm2WwanDataGroup": hm2WwanDataGroup,
       "hm2WwanDataConnectionTable": hm2WwanDataConnectionTable,
       "hm2WwanDataConnectionEntry": hm2WwanDataConnectionEntry,
       "hm2WwanDataConnectionSimId": hm2WwanDataConnectionSimId,
       "hm2WwanDataConnectionAdminStatus": hm2WwanDataConnectionAdminStatus,
       "hm2WwanDataConnectionApn": hm2WwanDataConnectionApn,
       "hm2WwanDataConnectionApnCurrent": hm2WwanDataConnectionApnCurrent,
       "hm2WwanDataConnectionUser": hm2WwanDataConnectionUser,
       "hm2WwanDataConnectionPassword": hm2WwanDataConnectionPassword,
       "hm2WwanDataConnectionAuth": hm2WwanDataConnectionAuth,
       "hm2WwanDataConnectionPdpType": hm2WwanDataConnectionPdpType,
       "hm2WwanDataConnectionIpAddressType": hm2WwanDataConnectionIpAddressType,
       "hm2WwanDataConnectionIpAddress": hm2WwanDataConnectionIpAddress,
       "hm2WwanDataConnectionDnsPrimaryType": hm2WwanDataConnectionDnsPrimaryType,
       "hm2WwanDataConnectionDnsPrimary": hm2WwanDataConnectionDnsPrimary,
       "hm2WwanDataConnectionDnsSecondaryType": hm2WwanDataConnectionDnsSecondaryType,
       "hm2WwanDataConnectionDnsSecondary": hm2WwanDataConnectionDnsSecondary,
       "hm2WwanDataConnectionIpAddressCurrentType": hm2WwanDataConnectionIpAddressCurrentType,
       "hm2WwanDataConnectionIpAddressCurrent": hm2WwanDataConnectionIpAddressCurrent,
       "hm2WwanDataConnectionDnsPrimaryCurrentType": hm2WwanDataConnectionDnsPrimaryCurrentType,
       "hm2WwanDataConnectionDnsPrimaryCurrent": hm2WwanDataConnectionDnsPrimaryCurrent,
       "hm2WwanDataConnectionDnsSecondaryCurrentType": hm2WwanDataConnectionDnsSecondaryCurrentType,
       "hm2WwanDataConnectionDnsSecondaryCurrent": hm2WwanDataConnectionDnsSecondaryCurrent,
       "hm2WwanDataConnectionMtu": hm2WwanDataConnectionMtu,
       "hm2WwanDataConnectionFailedRetry": hm2WwanDataConnectionFailedRetry,
       "hm2WwanDataConnectionFailedRetryCurrent": hm2WwanDataConnectionFailedRetryCurrent,
       "hm2WwanDataConnectionStatus": hm2WwanDataConnectionStatus,
       "hm2WwanDataConnectionStatusErrorReason": hm2WwanDataConnectionStatusErrorReason,
       "hm2WwanDataConnectionActivatedCount": hm2WwanDataConnectionActivatedCount,
       "hm2WwanDataConnectionStartTime": hm2WwanDataConnectionStartTime,
       "hm2WwanDataConnectionUpTime": hm2WwanDataConnectionUpTime,
       "hm2WwanDataConnectionTotalUpTime": hm2WwanDataConnectionTotalUpTime,
       "hm2WwanDataPlanTable": hm2WwanDataPlanTable,
       "hm2WwanDataPlanEntry": hm2WwanDataPlanEntry,
       "hm2WwanDataPlanSimId": hm2WwanDataPlanSimId,
       "hm2WwanDataPlanMonthlyLimit": hm2WwanDataPlanMonthlyLimit,
       "hm2WwanDataPlanLimitMeasureUnit": hm2WwanDataPlanLimitMeasureUnit,
       "hm2WwanDataPlanWarningThreshold": hm2WwanDataPlanWarningThreshold,
       "hm2WwanDataPlanReset": hm2WwanDataPlanReset,
       "hm2WwanDataPlanResetDay": hm2WwanDataPlanResetDay,
       "hm2WwanDataPlanLastReset": hm2WwanDataPlanLastReset,
       "hm2WwanDataPlanCutoffThreshold": hm2WwanDataPlanCutoffThreshold,
       "hm2WwanDataPlanMonthlyUsageTx": hm2WwanDataPlanMonthlyUsageTx,
       "hm2WwanDataPlanMonthlyUsageRx": hm2WwanDataPlanMonthlyUsageRx,
       "hm2WwanDataPacketStatsTable": hm2WwanDataPacketStatsTable,
       "hm2WwanDataPacketStatsEntry": hm2WwanDataPacketStatsEntry,
       "hm2WwanDataPacketStatsSimId": hm2WwanDataPacketStatsSimId,
       "hm2WwanDataPacketStatsTxOk": hm2WwanDataPacketStatsTxOk,
       "hm2WwanDataPacketStatsRxOk": hm2WwanDataPacketStatsRxOk,
       "hm2WwanDataPacketStatsTxErrors": hm2WwanDataPacketStatsTxErrors,
       "hm2WwanDataPacketStatsRxErrors": hm2WwanDataPacketStatsRxErrors,
       "hm2WwanDataPacketStatsTxOverflows": hm2WwanDataPacketStatsTxOverflows,
       "hm2WwanDataPacketStatsRxOverflows": hm2WwanDataPacketStatsRxOverflows,
       "hm2WwanDataPacketStatsTxBytesOk": hm2WwanDataPacketStatsTxBytesOk,
       "hm2WwanDataPacketStatsRxBytesOk": hm2WwanDataPacketStatsRxBytesOk,
       "hm2WwanDataPacketStatsTxDropped": hm2WwanDataPacketStatsTxDropped,
       "hm2WwanDataPacketStatsRxDropped": hm2WwanDataPacketStatsRxDropped,
       "hm2WwanSimCardGroup": hm2WwanSimCardGroup,
       "hm2WwanSimCardTable": hm2WwanSimCardTable,
       "hm2WwanSimCardEntry": hm2WwanSimCardEntry,
       "hm2WwanSimCardSimId": hm2WwanSimCardSimId,
       "hm2WwanSimCardAdminStatus": hm2WwanSimCardAdminStatus,
       "hm2WwanSimCardRole": hm2WwanSimCardRole,
       "hm2WwanSimCardRoleCurrent": hm2WwanSimCardRoleCurrent,
       "hm2WwanSimCardStatus": hm2WwanSimCardStatus,
       "hm2WwanSimCardSetActive": hm2WwanSimCardSetActive,
       "hm2WwanSimCardPin1": hm2WwanSimCardPin1,
       "hm2WwanSimCardPin1Mode": hm2WwanSimCardPin1Mode,
       "hm2WwanSimCardPin1Status": hm2WwanSimCardPin1Status,
       "hm2WwanSimCardPin1VerifyTries": hm2WwanSimCardPin1VerifyTries,
       "hm2WwanSimCardPin1UnblockTries": hm2WwanSimCardPin1UnblockTries,
       "hm2WwanSimCardPuk1": hm2WwanSimCardPuk1,
       "hm2WwanSimCardRoamingMode": hm2WwanSimCardRoamingMode,
       "hm2WwanSimCardIccid": hm2WwanSimCardIccid,
       "hm2WwanSimCardImsi": hm2WwanSimCardImsi,
       "hm2WwanInformationGroup": hm2WwanInformationGroup,
       "hm2WwanCellularInformationGroup": hm2WwanCellularInformationGroup,
       "hm2WwanCellularActiveSimId": hm2WwanCellularActiveSimId,
       "hm2WwanCellularRegistration": hm2WwanCellularRegistration,
       "hm2WwanCellularOperator": hm2WwanCellularOperator,
       "hm2WwanCellularNetwork": hm2WwanCellularNetwork,
       "hm2WwanCellularMcc": hm2WwanCellularMcc,
       "hm2WwanCellularMnc": hm2WwanCellularMnc,
       "hm2WwanCellularLac": hm2WwanCellularLac,
       "hm2WwanCellularBsic": hm2WwanCellularBsic,
       "hm2WwanCellularCellId": hm2WwanCellularCellId,
       "hm2WwanCellularBand": hm2WwanCellularBand,
       "hm2WwanCellularChannel": hm2WwanCellularChannel,
       "hm2WwanCellularSignalStrength": hm2WwanCellularSignalStrength,
       "hm2WwanCellularSignalStrengthLte": hm2WwanCellularSignalStrengthLte,
       "hm2WwanCellularSignalQuality": hm2WwanCellularSignalQuality,
       "hm2WwanCellularSignalQualityLte": hm2WwanCellularSignalQualityLte,
       "hm2WwanCellularRscp": hm2WwanCellularRscp,
       "hm2WwanCellularRoamingStatus": hm2WwanCellularRoamingStatus,
       "hm2WwanCellularBitErrorRate": hm2WwanCellularBitErrorRate,
       "hm2WwanCellularCurrentTxRate": hm2WwanCellularCurrentTxRate,
       "hm2WwanCellularCurrentRxRate": hm2WwanCellularCurrentRxRate,
       "hm2WwanCellularMaxTxRate": hm2WwanCellularMaxTxRate,
       "hm2WwanCellularMaxRxRate": hm2WwanCellularMaxRxRate,
       "hm2WwanModemInformationGroup": hm2WwanModemInformationGroup,
       "hm2WwanModemManufacturer": hm2WwanModemManufacturer,
       "hm2WwanModemModel": hm2WwanModemModel,
       "hm2WwanModemRevision": hm2WwanModemRevision,
       "hm2WwanModemImei": hm2WwanModemImei}
)
