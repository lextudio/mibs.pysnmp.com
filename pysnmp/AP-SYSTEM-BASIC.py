# SNMP MIB module (AP-SYSTEM-BASIC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AP-SYSTEM-BASIC
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:04 2024
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
 enterprises,
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
    "enterprises",
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

ap_system_basic_mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Pepwave_ObjectIdentity = ObjectIdentity
pepwave = _Pepwave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662)
)
_ProductID_ObjectIdentity = ObjectIdentity
productID = _ProductID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200)
)
_ApMib_ObjectIdentity = ObjectIdentity
apMib = _ApMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1)
)
_ApGeneralMib_ObjectIdentity = ObjectIdentity
apGeneralMib = _ApGeneralMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1)
)
_ApSystemInfo_ObjectIdentity = ObjectIdentity
apSystemInfo = _ApSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 1)
)
_ApSystemBasicInfo_ObjectIdentity = ObjectIdentity
apSystemBasicInfo = _ApSystemBasicInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 1, 1)
)


class _ApSerialNumber_Type(OctetString):
    """Custom type apSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_ApSerialNumber_Type.__name__ = "OctetString"
_ApSerialNumber_Object = MibScalar
apSerialNumber = _ApSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 1, 1, 1),
    _ApSerialNumber_Type()
)
apSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSerialNumber.setStatus("current")


class _ApMacAddress_Type(OctetString):
    """Custom type apMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_ApMacAddress_Type.__name__ = "OctetString"
_ApMacAddress_Object = MibScalar
apMacAddress = _ApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 1, 1, 2),
    _ApMacAddress_Type()
)
apMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMacAddress.setStatus("current")


class _ApSoftwareVerstion_Type(OctetString):
    """Custom type apSoftwareVerstion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ApSoftwareVerstion_Type.__name__ = "OctetString"
_ApSoftwareVerstion_Object = MibScalar
apSoftwareVerstion = _ApSoftwareVerstion_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 1, 1, 3),
    _ApSoftwareVerstion_Type()
)
apSoftwareVerstion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSoftwareVerstion.setStatus("current")


class _ApTime_Type(OctetString):
    """Custom type apTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ApTime_Type.__name__ = "OctetString"
_ApTime_Object = MibScalar
apTime = _ApTime_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 1, 1, 4),
    _ApTime_Type()
)
apTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTime.setStatus("current")
_ApUpTime_Type = TimeTicks
_ApUpTime_Object = MibScalar
apUpTime = _ApUpTime_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 1, 1, 5),
    _ApUpTime_Type()
)
apUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUpTime.setStatus("current")


class _ApStatus_Type(Integer32):
    """Custom type apStatus based on Integer32"""
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
        *(("activating", 3),
          ("bootup", 2),
          ("firmwareUpgrading", 4),
          ("running", 1),
          ("unknown", 0))
    )


_ApStatus_Type.__name__ = "Integer32"
_ApStatus_Object = MibScalar
apStatus = _ApStatus_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 1, 1, 6),
    _ApStatus_Type()
)
apStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStatus.setStatus("current")


class _ApControllerStatus_Type(OctetString):
    """Custom type apControllerStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApControllerStatus_Type.__name__ = "OctetString"
_ApControllerStatus_Object = MibScalar
apControllerStatus = _ApControllerStatus_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 1, 1, 7),
    _ApControllerStatus_Type()
)
apControllerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apControllerStatus.setStatus("current")
_ApCurrentControllerIp_Type = IpAddress
_ApCurrentControllerIp_Object = MibScalar
apCurrentControllerIp = _ApCurrentControllerIp_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 1, 1, 8),
    _ApCurrentControllerIp_Type()
)
apCurrentControllerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCurrentControllerIp.setStatus("current")
_ApSystemConfig_ObjectIdentity = ObjectIdentity
apSystemConfig = _ApSystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 2)
)
_ApSystemBasicConfig_ObjectIdentity = ObjectIdentity
apSystemBasicConfig = _ApSystemBasicConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 2, 1)
)


class _ApName_Type(OctetString):
    """Custom type apName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ApName_Type.__name__ = "OctetString"
_ApName_Object = MibScalar
apName = _ApName_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 2, 1, 1),
    _ApName_Type()
)
apName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apName.setStatus("current")


class _ApLocation_Type(OctetString):
    """Custom type apLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApLocation_Type.__name__ = "OctetString"
_ApLocation_Object = MibScalar
apLocation = _ApLocation_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 2, 1, 2),
    _ApLocation_Type()
)
apLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLocation.setStatus("current")


class _ApTimeZone_Type(Integer32):
    """Custom type apTimeZone based on Integer32"""
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
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53)
        )
    )
    namedValues = NamedValues(
        *(("africa-cairo", 0),
          ("africa-kampala", 1),
          ("africa-lagos", 2),
          ("asia-china", 3),
          ("asia-hong-kong", 4),
          ("asia-jakarta", 5),
          ("asia-seoul", 6),
          ("asia-taiwan", 7),
          ("asia-tokyo", 8),
          ("europe-athens", 9),
          ("europe-berlin", 10),
          ("europe-dublin", 11),
          ("europe-moscow", 12),
          ("gmt", 25),
          ("gmt-1", 41),
          ("gmt-10", 32),
          ("gmt-11", 31),
          ("gmt-12", 30),
          ("gmt-13", 29),
          ("gmt-14", 28),
          ("gmt-2", 40),
          ("gmt-3", 39),
          ("gmt-4", 38),
          ("gmt-5", 37),
          ("gmt-6", 36),
          ("gmt-7", 35),
          ("gmt-8", 34),
          ("gmt-9", 33),
          ("gmt-plus-1", 42),
          ("gmt-plus-10", 51),
          ("gmt-plus-11", 52),
          ("gmt-plus-12", 53),
          ("gmt-plus-2", 43),
          ("gmt-plus-3", 44),
          ("gmt-plus-4", 45),
          ("gmt-plus-5", 46),
          ("gmt-plus-6", 47),
          ("gmt-plus-7", 48),
          ("gmt-plus-8", 49),
          ("gmt-plus-9", 50),
          ("us-alaska", 13),
          ("us-aleutian", 14),
          ("us-arizona", 15),
          ("us-central", 16),
          ("us-east-indiana", 18),
          ("us-eastern", 17),
          ("us-hawaii", 19),
          ("us-indiana-starke", 20),
          ("us-michigan", 21),
          ("us-mountain", 22),
          ("us-pacific", 23),
          ("us-samoa", 24),
          ("utc", 26),
          ("wet", 27))
    )


_ApTimeZone_Type.__name__ = "Integer32"
_ApTimeZone_Object = MibScalar
apTimeZone = _ApTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 2, 1, 3),
    _ApTimeZone_Type()
)
apTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTimeZone.setStatus("current")


class _ApControllerIp_Type(OctetString):
    """Custom type apControllerIp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApControllerIp_Type.__name__ = "OctetString"
_ApControllerIp_Object = MibScalar
apControllerIp = _ApControllerIp_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 2, 1, 4),
    _ApControllerIp_Type()
)
apControllerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apControllerIp.setStatus("current")


class _ApSystemDomain_Type(OctetString):
    """Custom type apSystemDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApSystemDomain_Type.__name__ = "OctetString"
_ApSystemDomain_Object = MibScalar
apSystemDomain = _ApSystemDomain_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 2, 1, 5),
    _ApSystemDomain_Type()
)
apSystemDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSystemDomain.setStatus("current")


class _ApNtpServer_Type(OctetString):
    """Custom type apNtpServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApNtpServer_Type.__name__ = "OctetString"
_ApNtpServer_Object = MibScalar
apNtpServer = _ApNtpServer_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 2, 1, 6),
    _ApNtpServer_Type()
)
apNtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apNtpServer.setStatus("current")


class _ApMode_Type(Integer32):
    """Custom type apMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 0),
          ("router", 1))
    )


_ApMode_Type.__name__ = "Integer32"
_ApMode_Object = MibScalar
apMode = _ApMode_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 2, 1, 7),
    _ApMode_Type()
)
apMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMode.setStatus("current")


class _ApEthSpeedDuplex_Type(Integer32):
    """Custom type apEthSpeedDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("eth-1000baseTx-FD", 5),
          ("eth-100baseTx-FD", 4),
          ("eth-100baseTx-HD", 3),
          ("eth-10baseTx-FD", 2),
          ("eth-10baseTx-HD", 1))
    )


_ApEthSpeedDuplex_Type.__name__ = "Integer32"
_ApEthSpeedDuplex_Object = MibScalar
apEthSpeedDuplex = _ApEthSpeedDuplex_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 2, 1, 8),
    _ApEthSpeedDuplex_Type()
)
apEthSpeedDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apEthSpeedDuplex.setStatus("current")


class _ApVlan_Type(Integer32):
    """Custom type apVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_ApVlan_Type.__name__ = "Integer32"
_ApVlan_Object = MibScalar
apVlan = _ApVlan_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 2, 1, 9),
    _ApVlan_Type()
)
apVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVlan.setStatus("current")


class _ApEthAdvertise_Type(Integer32):
    """Custom type apEthAdvertise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ApEthAdvertise_Type.__name__ = "Integer32"
_ApEthAdvertise_Object = MibScalar
apEthAdvertise = _ApEthAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 2, 1, 10),
    _ApEthAdvertise_Type()
)
apEthAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apEthAdvertise.setStatus("current")
_ApSystemScheduleRebootConfigTable_Object = MibTable
apSystemScheduleRebootConfigTable = _ApSystemScheduleRebootConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    apSystemScheduleRebootConfigTable.setStatus("current")
_ApSystemScheduleRebootConfigEntry_Object = MibTableRow
apSystemScheduleRebootConfigEntry = _ApSystemScheduleRebootConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 2, 2, 1)
)
apSystemScheduleRebootConfigEntry.setIndexNames(
    (0, "AP-SYSTEM-BASIC", "apScheduleRebootIndex"),
)
if mibBuilder.loadTexts:
    apSystemScheduleRebootConfigEntry.setStatus("current")
_ApScheduleRebootIndex_Type = Integer32
_ApScheduleRebootIndex_Object = MibTableColumn
apScheduleRebootIndex = _ApScheduleRebootIndex_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 2, 2, 1, 1),
    _ApScheduleRebootIndex_Type()
)
apScheduleRebootIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apScheduleRebootIndex.setStatus("current")


class _ApScheduleReboot_Type(Integer32):
    """Custom type apScheduleReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApScheduleReboot_Type.__name__ = "Integer32"
_ApScheduleReboot_Object = MibTableColumn
apScheduleReboot = _ApScheduleReboot_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 2, 2, 1, 2),
    _ApScheduleReboot_Type()
)
apScheduleReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apScheduleReboot.setStatus("current")


class _ApScheduleRebootType_Type(Integer32):
    """Custom type apScheduleRebootType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("daily", 2),
          ("monthly", 0),
          ("weekly", 1))
    )


_ApScheduleRebootType_Type.__name__ = "Integer32"
_ApScheduleRebootType_Object = MibTableColumn
apScheduleRebootType = _ApScheduleRebootType_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 2, 2, 1, 3),
    _ApScheduleRebootType_Type()
)
apScheduleRebootType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apScheduleRebootType.setStatus("current")


class _ApScheduleRebootDom_Type(Integer32):
    """Custom type apScheduleRebootDom based on Integer32"""
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
              31)
        )
    )
    namedValues = NamedValues(
        *(("day-1", 1),
          ("day-10", 10),
          ("day-11", 11),
          ("day-12", 12),
          ("day-13", 13),
          ("day-14", 14),
          ("day-15", 15),
          ("day-16", 16),
          ("day-17", 17),
          ("day-18", 18),
          ("day-19", 19),
          ("day-2", 2),
          ("day-20", 20),
          ("day-21", 21),
          ("day-22", 22),
          ("day-23", 23),
          ("day-24", 24),
          ("day-25", 25),
          ("day-26", 26),
          ("day-27", 27),
          ("day-28", 28),
          ("day-29", 29),
          ("day-3", 3),
          ("day-30", 30),
          ("day-31", 31),
          ("day-4", 4),
          ("day-5", 5),
          ("day-6", 6),
          ("day-7", 7),
          ("day-8", 8),
          ("day-9", 9),
          ("na", 0))
    )


_ApScheduleRebootDom_Type.__name__ = "Integer32"
_ApScheduleRebootDom_Object = MibTableColumn
apScheduleRebootDom = _ApScheduleRebootDom_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 2, 2, 1, 4),
    _ApScheduleRebootDom_Type()
)
apScheduleRebootDom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apScheduleRebootDom.setStatus("current")


class _ApScheduleRebootDow_Type(Integer32):
    """Custom type apScheduleRebootDow based on Integer32"""
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
        *(("friday", 5),
          ("monday", 1),
          ("na", 7),
          ("saturday", 6),
          ("sunday", 0),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )


_ApScheduleRebootDow_Type.__name__ = "Integer32"
_ApScheduleRebootDow_Object = MibTableColumn
apScheduleRebootDow = _ApScheduleRebootDow_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 2, 2, 1, 5),
    _ApScheduleRebootDow_Type()
)
apScheduleRebootDow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apScheduleRebootDow.setStatus("current")


class _ApScheduleRebootHr_Type(Integer32):
    """Custom type apScheduleRebootHr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_ApScheduleRebootHr_Type.__name__ = "Integer32"
_ApScheduleRebootHr_Object = MibTableColumn
apScheduleRebootHr = _ApScheduleRebootHr_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 2, 2, 1, 6),
    _ApScheduleRebootHr_Type()
)
apScheduleRebootHr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apScheduleRebootHr.setStatus("current")


class _ApScheduleRebootMin_Type(Integer32):
    """Custom type apScheduleRebootMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              15,
              30,
              45)
        )
    )
    namedValues = NamedValues(
        *(("mins-0", 0),
          ("mins-15", 15),
          ("mins-30", 30),
          ("mins-45", 45))
    )


_ApScheduleRebootMin_Type.__name__ = "Integer32"
_ApScheduleRebootMin_Object = MibTableColumn
apScheduleRebootMin = _ApScheduleRebootMin_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 2, 2, 1, 7),
    _ApScheduleRebootMin_Type()
)
apScheduleRebootMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apScheduleRebootMin.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AP-SYSTEM-BASIC",
    **{"pepwave": pepwave,
       "productID": productID,
       "apMib": apMib,
       "apGeneralMib": apGeneralMib,
       "ap-system-basic-mib": ap_system_basic_mib,
       "apSystemInfo": apSystemInfo,
       "apSystemBasicInfo": apSystemBasicInfo,
       "apSerialNumber": apSerialNumber,
       "apMacAddress": apMacAddress,
       "apSoftwareVerstion": apSoftwareVerstion,
       "apTime": apTime,
       "apUpTime": apUpTime,
       "apStatus": apStatus,
       "apControllerStatus": apControllerStatus,
       "apCurrentControllerIp": apCurrentControllerIp,
       "apSystemConfig": apSystemConfig,
       "apSystemBasicConfig": apSystemBasicConfig,
       "apName": apName,
       "apLocation": apLocation,
       "apTimeZone": apTimeZone,
       "apControllerIp": apControllerIp,
       "apSystemDomain": apSystemDomain,
       "apNtpServer": apNtpServer,
       "apMode": apMode,
       "apEthSpeedDuplex": apEthSpeedDuplex,
       "apVlan": apVlan,
       "apEthAdvertise": apEthAdvertise,
       "apSystemScheduleRebootConfigTable": apSystemScheduleRebootConfigTable,
       "apSystemScheduleRebootConfigEntry": apSystemScheduleRebootConfigEntry,
       "apScheduleRebootIndex": apScheduleRebootIndex,
       "apScheduleReboot": apScheduleReboot,
       "apScheduleRebootType": apScheduleRebootType,
       "apScheduleRebootDom": apScheduleRebootDom,
       "apScheduleRebootDow": apScheduleRebootDow,
       "apScheduleRebootHr": apScheduleRebootHr,
       "apScheduleRebootMin": apScheduleRebootMin}
)
