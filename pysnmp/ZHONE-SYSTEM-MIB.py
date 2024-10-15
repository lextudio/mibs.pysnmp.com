# SNMP MIB module (ZHONE-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:09 2024
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
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

(ipIfAddr,
 ipIfLgId,
 ipIfVci,
 ipIfVpi) = mibBuilder.importSymbols(
    "ZHONE-COM-IP-REC-MIB",
    "ipIfAddr",
    "ipIfLgId",
    "ipIfVci",
    "ipIfVpi")

(pportNumber,
 subPortNumber,
 zhoneShelfNumber,
 zhoneSlotNumber) = mibBuilder.importSymbols(
    "ZHONE-INTERFACE-TRANSLATION-MIB",
    "pportNumber",
    "subPortNumber",
    "zhoneShelfNumber",
    "zhoneSlotNumber")

(zhone,
 zhoneModules,
 zhoneShelfIndex,
 zhoneSlotIndex,
 zhoneSystem,
 zhoneTrapModules) = mibBuilder.importSymbols(
    "Zhone",
    "zhone",
    "zhoneModules",
    "zhoneShelfIndex",
    "zhoneSlotIndex",
    "zhoneSystem",
    "zhoneTrapModules")

(ZhoneAdminString,
 ZhoneAlarmSeverity,
 ZhoneAlarmTypeId,
 ZhoneCardLineType,
 ZhoneCardType,
 ZhoneCountryCode,
 ZhoneFileName,
 ZhoneIfType,
 ZhoneRowStatus,
 ZhoneShelfValue,
 ZhoneSlotValue) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneAdminString",
    "ZhoneAlarmSeverity",
    "ZhoneAlarmTypeId",
    "ZhoneCardLineType",
    "ZhoneCardType",
    "ZhoneCountryCode",
    "ZhoneFileName",
    "ZhoneIfType",
    "ZhoneRowStatus",
    "ZhoneShelfValue",
    "ZhoneSlotValue")


# MODULE-IDENTITY

zhoneSystemModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 2)
)
zhoneSystemModule.setRevisions(
        ("2014-06-17 05:22",
         "2014-03-23 21:31",
         "2014-02-03 03:29",
         "2013-11-26 22:45",
         "2013-06-21 15:44",
         "2013-05-16 17:23",
         "2012-12-27 04:29",
         "2012-10-18 13:11",
         "2012-04-10 11:28",
         "2012-03-26 09:32",
         "2012-03-20 16:00",
         "2011-12-20 17:56",
         "2011-12-08 12:00",
         "2011-02-17 13:34",
         "2011-02-08 06:55",
         "2010-05-18 10:00",
         "2009-04-23 14:48",
         "2009-04-20 09:28",
         "2009-04-14 17:07",
         "2008-10-23 22:57",
         "2008-10-07 12:38",
         "2008-09-17 13:20",
         "2008-07-10 20:15",
         "2008-06-08 11:15",
         "2007-12-14 15:20",
         "2007-11-02 11:10",
         "2007-03-26 16:24",
         "2006-11-29 15:11",
         "2006-10-17 14:57",
         "2006-06-16 13:14",
         "2006-05-22 09:52",
         "2006-05-17 16:34",
         "2006-03-15 12:36",
         "2005-05-12 09:13",
         "2005-01-18 14:43",
         "2004-07-02 12:30",
         "2004-02-18 15:00",
         "2003-12-04 14:18",
         "2003-11-08 14:30",
         "2003-04-23 16:26",
         "2003-03-19 10:35",
         "2003-02-20 11:00",
         "2002-11-19 11:15",
         "2002-10-29 15:33",
         "2002-10-24 18:36",
         "2002-10-18 16:03",
         "2002-09-23 15:36",
         "2002-06-11 17:04",
         "2002-06-11 14:01",
         "2002-06-03 08:57",
         "2002-05-24 12:40",
         "2002-05-09 17:42",
         "2002-03-22 15:12",
         "2002-01-10 16:09",
         "2002-01-10 16:04",
         "2001-11-26 15:59",
         "2001-11-16 18:19",
         "2001-11-01 17:14",
         "2001-10-29 12:19",
         "2001-10-25 20:09",
         "2001-10-22 17:10",
         "2001-10-19 11:37",
         "2001-10-18 10:30",
         "2001-10-17 13:51",
         "2001-10-05 12:08",
         "2001-10-02 11:19",
         "2001-09-25 14:50",
         "2001-08-30 17:45",
         "2001-08-22 14:43",
         "2001-08-10 13:37",
         "2001-08-01 16:20",
         "2001-08-01 16:20",
         "2001-07-30 15:32",
         "2001-06-06 17:53",
         "2001-05-25 15:31",
         "2001-05-17 09:59",
         "2001-04-27 11:16",
         "2001-02-18 15:55",
         "2001-02-16 13:12",
         "2001-02-12 19:06",
         "2001-01-22 14:14",
         "2001-01-16 13:44",
         "2000-12-01 12:16",
         "2000-11-11 12:27",
         "2000-11-07 12:09",
         "2000-10-17 19:36",
         "2000-09-15 17:07",
         "2000-09-12 18:02",
         "2000-09-12 18:01")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ZhoneRedundancyWeight(Integer32, TextualConvention):
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
        *(("highPreference", 5),
          ("mediumPreference", 4),
          ("neverActive", 1),
          ("noPreference", 2),
          ("slightPreference", 3))
    )



class ZhoneLocalTimeZone(Integer32, TextualConvention):
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
              34)
        )
    )
    namedValues = NamedValues(
        *(("afghanistan", 20),
          ("atlantic", 9),
          ("australia", 29),
          ("azores", 12),
          ("baghdad", 17),
          ("bangkok", 26),
          ("brasilia", 11),
          ("central", 7),
          ("centralEuropean", 15),
          ("chinaCoast", 27),
          ("dhaka", 24),
          ("eastern", 8),
          ("easternEurope", 16),
          ("gmt", 14),
          ("guam", 30),
          ("hawaii", 3),
          ("india", 22),
          ("internationalDateLineWest", 1),
          ("islamabad", 21),
          ("japan", 28),
          ("kathmandu", 23),
          ("lineIslands", 34),
          ("magadan", 31),
          ("mountain", 6),
          ("newZealand", 32),
          ("newfoundland", 10),
          ("nome", 2),
          ("pacific", 5),
          ("rangoon", 25),
          ("rawakiIslands", 33),
          ("tehran", 18),
          ("uae", 19),
          ("westAfrica", 13),
          ("yukon", 4))
    )



# MIB Managed Objects in the order of their OIDs

_ZhoneZms_ObjectIdentity = ObjectIdentity
zhoneZms = _ZhoneZms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 1)
)
if mibBuilder.loadTexts:
    zhoneZms.setStatus("current")
_ZhoneZmsExists_Type = TruthValue
_ZhoneZmsExists_Object = MibScalar
zhoneZmsExists = _ZhoneZmsExists_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 1, 1),
    _ZhoneZmsExists_Type()
)
zhoneZmsExists.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneZmsExists.setStatus("current")


class _ZhoneZmsConnectionStatus_Type(Integer32):
    """Custom type zhoneZmsConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_ZhoneZmsConnectionStatus_Type.__name__ = "Integer32"
_ZhoneZmsConnectionStatus_Object = MibScalar
zhoneZmsConnectionStatus = _ZhoneZmsConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 1, 2),
    _ZhoneZmsConnectionStatus_Type()
)
zhoneZmsConnectionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneZmsConnectionStatus.setStatus("current")
_ZhoneZmsIpAddress_Type = IpAddress
_ZhoneZmsIpAddress_Object = MibScalar
zhoneZmsIpAddress = _ZhoneZmsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 1, 3),
    _ZhoneZmsIpAddress_Type()
)
zhoneZmsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneZmsIpAddress.setStatus("current")
_ZhoneZmsBlockCli_Type = TruthValue
_ZhoneZmsBlockCli_Object = MibScalar
zhoneZmsBlockCli = _ZhoneZmsBlockCli_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 1, 4),
    _ZhoneZmsBlockCli_Type()
)
zhoneZmsBlockCli.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneZmsBlockCli.setStatus("current")
_ZhoneTraps_ObjectIdentity = ObjectIdentity
zhoneTraps = _ZhoneTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2)
)
if mibBuilder.loadTexts:
    zhoneTraps.setStatus("current")
_ZhoneTrapsTable_Object = MibTable
zhoneTrapsTable = _ZhoneTrapsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    zhoneTrapsTable.setStatus("current")
_ZhoneTrapsEntry_Object = MibTableRow
zhoneTrapsEntry = _ZhoneTrapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 1, 1)
)
zhoneTrapsEntry.setIndexNames(
    (0, "ZHONE-SYSTEM-MIB", "zhoneTrapsDestination"),
)
if mibBuilder.loadTexts:
    zhoneTrapsEntry.setStatus("current")
_ZhoneTrapsDestination_Type = IpAddress
_ZhoneTrapsDestination_Object = MibTableColumn
zhoneTrapsDestination = _ZhoneTrapsDestination_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 1, 1, 1),
    _ZhoneTrapsDestination_Type()
)
zhoneTrapsDestination.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneTrapsDestination.setStatus("current")
_ZhoneTrapsCommunityName_Type = ZhoneAdminString
_ZhoneTrapsCommunityName_Object = MibTableColumn
zhoneTrapsCommunityName = _ZhoneTrapsCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 1, 1, 2),
    _ZhoneTrapsCommunityName_Type()
)
zhoneTrapsCommunityName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTrapsCommunityName.setStatus("current")
_ZhoneTrapsSequenceNumber_Type = Unsigned32
_ZhoneTrapsSequenceNumber_Object = MibTableColumn
zhoneTrapsSequenceNumber = _ZhoneTrapsSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 1, 1, 3),
    _ZhoneTrapsSequenceNumber_Type()
)
zhoneTrapsSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTrapsSequenceNumber.setStatus("current")


class _ZhoneTrapsResendSequenceNumber_Type(Integer32):
    """Custom type zhoneTrapsResendSequenceNumber based on Integer32"""
    defaultValue = 0


_ZhoneTrapsResendSequenceNumber_Object = MibTableColumn
zhoneTrapsResendSequenceNumber = _ZhoneTrapsResendSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 1, 1, 4),
    _ZhoneTrapsResendSequenceNumber_Type()
)
zhoneTrapsResendSequenceNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTrapsResendSequenceNumber.setStatus("current")
_ZhoneTrapsAckedSequenceNumber_Type = Unsigned32
_ZhoneTrapsAckedSequenceNumber_Object = MibTableColumn
zhoneTrapsAckedSequenceNumber = _ZhoneTrapsAckedSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 1, 1, 5),
    _ZhoneTrapsAckedSequenceNumber_Type()
)
zhoneTrapsAckedSequenceNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTrapsAckedSequenceNumber.setStatus("current")


class _ZhoneTrapsSeverity_Type(Integer32):
    """Custom type zhoneTrapsSeverity based on Integer32"""
    defaultValue = 4

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
        *(("critical", 1),
          ("low", 4),
          ("moderate", 3),
          ("severe", 2))
    )


_ZhoneTrapsSeverity_Type.__name__ = "Integer32"
_ZhoneTrapsSeverity_Object = MibTableColumn
zhoneTrapsSeverity = _ZhoneTrapsSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 1, 1, 6),
    _ZhoneTrapsSeverity_Type()
)
zhoneTrapsSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTrapsSeverity.setStatus("current")


class _ZhoneTrapsAllowedCategories_Type(Bits):
    """Custom type zhoneTrapsAllowedCategories based on Bits"""
    namedValues = NamedValues(
        *(("catAdmin", 0),
          ("catIP", 3),
          ("catLine", 1),
          ("catRadio", 5),
          ("catRip", 4),
          ("catVoice", 2))
    )

_ZhoneTrapsAllowedCategories_Type.__name__ = "Bits"
_ZhoneTrapsAllowedCategories_Object = MibTableColumn
zhoneTrapsAllowedCategories = _ZhoneTrapsAllowedCategories_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 1, 1, 7),
    _ZhoneTrapsAllowedCategories_Type()
)
zhoneTrapsAllowedCategories.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTrapsAllowedCategories.setStatus("current")


class _ZhoneTrapsAdminStatus_Type(Integer32):
    """Custom type zhoneTrapsAdminStatus based on Integer32"""
    defaultValue = 1

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


_ZhoneTrapsAdminStatus_Type.__name__ = "Integer32"
_ZhoneTrapsAdminStatus_Object = MibTableColumn
zhoneTrapsAdminStatus = _ZhoneTrapsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 1, 1, 8),
    _ZhoneTrapsAdminStatus_Type()
)
zhoneTrapsAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTrapsAdminStatus.setStatus("current")
_ZhoneTrapsRowStatus_Type = ZhoneRowStatus
_ZhoneTrapsRowStatus_Object = MibTableColumn
zhoneTrapsRowStatus = _ZhoneTrapsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 1, 1, 9),
    _ZhoneTrapsRowStatus_Type()
)
zhoneTrapsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTrapsRowStatus.setStatus("current")


class _ZhoneTrapsGatewayTrapServerAddress_Type(ZhoneAdminString):
    """Custom type zhoneTrapsGatewayTrapServerAddress based on ZhoneAdminString"""
    defaultValue = OctetString("none")


_ZhoneTrapsGatewayTrapServerAddress_Object = MibTableColumn
zhoneTrapsGatewayTrapServerAddress = _ZhoneTrapsGatewayTrapServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 1, 1, 10),
    _ZhoneTrapsGatewayTrapServerAddress_Type()
)
zhoneTrapsGatewayTrapServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTrapsGatewayTrapServerAddress.setStatus("current")


class _ZhoneTrapVersion_Type(Integer32):
    """Custom type zhoneTrapVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("version1", 1)
    )


_ZhoneTrapVersion_Type.__name__ = "Integer32"
_ZhoneTrapVersion_Object = MibScalar
zhoneTrapVersion = _ZhoneTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 2),
    _ZhoneTrapVersion_Type()
)
zhoneTrapVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneTrapVersion.setStatus("current")


class _ZhoneTrapFlags_Type(Bits):
    """Custom type zhoneTrapFlags based on Bits"""
    namedValues = NamedValues(
        *(("trapAcknowledge", 0),
          ("trapOutOfSequence", 1),
          ("trapResetSequenceNumber", 2))
    )

_ZhoneTrapFlags_Type.__name__ = "Bits"
_ZhoneTrapFlags_Object = MibScalar
zhoneTrapFlags = _ZhoneTrapFlags_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 3),
    _ZhoneTrapFlags_Type()
)
zhoneTrapFlags.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneTrapFlags.setStatus("current")
_ZhoneTrapShelf_Type = ZhoneShelfValue
_ZhoneTrapShelf_Object = MibScalar
zhoneTrapShelf = _ZhoneTrapShelf_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 4),
    _ZhoneTrapShelf_Type()
)
zhoneTrapShelf.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneTrapShelf.setStatus("current")
_ZhoneTrapSlot_Type = ZhoneSlotValue
_ZhoneTrapSlot_Object = MibScalar
zhoneTrapSlot = _ZhoneTrapSlot_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 5),
    _ZhoneTrapSlot_Type()
)
zhoneTrapSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneTrapSlot.setStatus("current")


class _ZhoneTrapPort_Type(Integer32):
    """Custom type zhoneTrapPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneTrapPort_Type.__name__ = "Integer32"
_ZhoneTrapPort_Object = MibScalar
zhoneTrapPort = _ZhoneTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 6),
    _ZhoneTrapPort_Type()
)
zhoneTrapPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneTrapPort.setStatus("current")


class _ZhoneTrapSubPort_Type(Integer32):
    """Custom type zhoneTrapSubPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneTrapSubPort_Type.__name__ = "Integer32"
_ZhoneTrapSubPort_Object = MibScalar
zhoneTrapSubPort = _ZhoneTrapSubPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 7),
    _ZhoneTrapSubPort_Type()
)
zhoneTrapSubPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneTrapSubPort.setStatus("current")
_ZhoneTrapProviderId_Type = Integer32
_ZhoneTrapProviderId_Object = MibScalar
zhoneTrapProviderId = _ZhoneTrapProviderId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 8),
    _ZhoneTrapProviderId_Type()
)
zhoneTrapProviderId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneTrapProviderId.setStatus("current")


class _ZhoneTrapText_Type(SnmpAdminString):
    """Custom type zhoneTrapText based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ZhoneTrapText_Type.__name__ = "SnmpAdminString"
_ZhoneTrapText_Object = MibScalar
zhoneTrapText = _ZhoneTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 9),
    _ZhoneTrapText_Type()
)
zhoneTrapText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneTrapText.setStatus("current")
_ZhoneTrapPortType_Type = IANAifType
_ZhoneTrapPortType_Object = MibScalar
zhoneTrapPortType = _ZhoneTrapPortType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 10),
    _ZhoneTrapPortType_Type()
)
zhoneTrapPortType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneTrapPortType.setStatus("current")
_ZhoneTrapPortTypeExtension_Type = ZhoneIfType
_ZhoneTrapPortTypeExtension_Object = MibScalar
zhoneTrapPortTypeExtension = _ZhoneTrapPortTypeExtension_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 11),
    _ZhoneTrapPortTypeExtension_Type()
)
zhoneTrapPortTypeExtension.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneTrapPortTypeExtension.setStatus("current")


class _ZhoneTrapAlarmAction_Type(Integer32):
    """Custom type zhoneTrapAlarmAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("informational", 3),
          ("set", 1))
    )


_ZhoneTrapAlarmAction_Type.__name__ = "Integer32"
_ZhoneTrapAlarmAction_Object = MibScalar
zhoneTrapAlarmAction = _ZhoneTrapAlarmAction_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 12),
    _ZhoneTrapAlarmAction_Type()
)
zhoneTrapAlarmAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneTrapAlarmAction.setStatus("current")
_ZhoneTrapAlarmId_Type = ZhoneAlarmTypeId
_ZhoneTrapAlarmId_Object = MibScalar
zhoneTrapAlarmId = _ZhoneTrapAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 13),
    _ZhoneTrapAlarmId_Type()
)
zhoneTrapAlarmId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneTrapAlarmId.setStatus("current")
_ZhoneTrapAlarmSeverity_Type = ZhoneAlarmSeverity
_ZhoneTrapAlarmSeverity_Object = MibScalar
zhoneTrapAlarmSeverity = _ZhoneTrapAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 14),
    _ZhoneTrapAlarmSeverity_Type()
)
zhoneTrapAlarmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneTrapAlarmSeverity.setStatus("current")
_ZhoneTrapConfigSyncResetInterval_Type = Unsigned32
_ZhoneTrapConfigSyncResetInterval_Object = MibScalar
zhoneTrapConfigSyncResetInterval = _ZhoneTrapConfigSyncResetInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 15),
    _ZhoneTrapConfigSyncResetInterval_Type()
)
zhoneTrapConfigSyncResetInterval.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneTrapConfigSyncResetInterval.setStatus("current")
_ZhoneTrapConfigSyncResetCount_Type = Unsigned32
_ZhoneTrapConfigSyncResetCount_Object = MibScalar
zhoneTrapConfigSyncResetCount = _ZhoneTrapConfigSyncResetCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 16),
    _ZhoneTrapConfigSyncResetCount_Type()
)
zhoneTrapConfigSyncResetCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneTrapConfigSyncResetCount.setStatus("current")
_ZhoneTrapConfigSyncResetLastFtpTime_Type = Unsigned32
_ZhoneTrapConfigSyncResetLastFtpTime_Object = MibScalar
zhoneTrapConfigSyncResetLastFtpTime = _ZhoneTrapConfigSyncResetLastFtpTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 17),
    _ZhoneTrapConfigSyncResetLastFtpTime_Type()
)
zhoneTrapConfigSyncResetLastFtpTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneTrapConfigSyncResetLastFtpTime.setStatus("current")
_ZhoneTrapConfigSyncResetCurrentTime_Type = Unsigned32
_ZhoneTrapConfigSyncResetCurrentTime_Object = MibScalar
zhoneTrapConfigSyncResetCurrentTime = _ZhoneTrapConfigSyncResetCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 18),
    _ZhoneTrapConfigSyncResetCurrentTime_Type()
)
zhoneTrapConfigSyncResetCurrentTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneTrapConfigSyncResetCurrentTime.setStatus("current")
_ZhoneTrapUtcTime_Type = Unsigned32
_ZhoneTrapUtcTime_Object = MibScalar
zhoneTrapUtcTime = _ZhoneTrapUtcTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 2, 19),
    _ZhoneTrapUtcTime_Type()
)
zhoneTrapUtcTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneTrapUtcTime.setStatus("current")
if mibBuilder.loadTexts:
    zhoneTrapUtcTime.setUnits("seconds")
_ZhoneConfigSync_ObjectIdentity = ObjectIdentity
zhoneConfigSync = _ZhoneConfigSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 3)
)
if mibBuilder.loadTexts:
    zhoneConfigSync.setStatus("current")
_ZhoneConfigSyncExists_Type = TruthValue
_ZhoneConfigSyncExists_Object = MibScalar
zhoneConfigSyncExists = _ZhoneConfigSyncExists_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 3, 1),
    _ZhoneConfigSyncExists_Type()
)
zhoneConfigSyncExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneConfigSyncExists.setStatus("current")
_ZhoneConfigSyncOverflow_Type = TruthValue
_ZhoneConfigSyncOverflow_Object = MibScalar
zhoneConfigSyncOverflow = _ZhoneConfigSyncOverflow_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 3, 2),
    _ZhoneConfigSyncOverflow_Type()
)
zhoneConfigSyncOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneConfigSyncOverflow.setStatus("current")


class _ZhoneConfigSyncPriority_Type(Integer32):
    """Custom type zhoneConfigSyncPriority based on Integer32"""
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
        *(("high", 4),
          ("low", 2),
          ("medium", 3),
          ("none", 1))
    )


_ZhoneConfigSyncPriority_Type.__name__ = "Integer32"
_ZhoneConfigSyncPriority_Object = MibScalar
zhoneConfigSyncPriority = _ZhoneConfigSyncPriority_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 3, 3),
    _ZhoneConfigSyncPriority_Type()
)
zhoneConfigSyncPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneConfigSyncPriority.setStatus("current")


class _ZhoneConfigSyncAction_Type(Integer32):
    """Custom type zhoneConfigSyncAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createFullList", 3),
          ("createList", 2),
          ("noAction", 1))
    )


_ZhoneConfigSyncAction_Type.__name__ = "Integer32"
_ZhoneConfigSyncAction_Object = MibScalar
zhoneConfigSyncAction = _ZhoneConfigSyncAction_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 3, 4),
    _ZhoneConfigSyncAction_Type()
)
zhoneConfigSyncAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneConfigSyncAction.setStatus("current")
_ZhoneConfigSyncFileName_Type = ZhoneFileName
_ZhoneConfigSyncFileName_Object = MibScalar
zhoneConfigSyncFileName = _ZhoneConfigSyncFileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 3, 5),
    _ZhoneConfigSyncFileName_Type()
)
zhoneConfigSyncFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneConfigSyncFileName.setStatus("current")


class _ZhoneConfigSyncStatus_Type(Integer32):
    """Custom type zhoneConfigSyncStatus based on Integer32"""
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
        *(("syncComplete", 1),
          ("syncError", 3),
          ("syncInitializing", 4),
          ("syncPending", 2))
    )


_ZhoneConfigSyncStatus_Type.__name__ = "Integer32"
_ZhoneConfigSyncStatus_Object = MibScalar
zhoneConfigSyncStatus = _ZhoneConfigSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 3, 6),
    _ZhoneConfigSyncStatus_Type()
)
zhoneConfigSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneConfigSyncStatus.setStatus("current")
_ZhoneConfigSyncUserName_Type = ZhoneAdminString
_ZhoneConfigSyncUserName_Object = MibScalar
zhoneConfigSyncUserName = _ZhoneConfigSyncUserName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 3, 7),
    _ZhoneConfigSyncUserName_Type()
)
zhoneConfigSyncUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneConfigSyncUserName.setStatus("current")
_ZhoneConfigSyncUserPassword_Type = ZhoneAdminString
_ZhoneConfigSyncUserPassword_Object = MibScalar
zhoneConfigSyncUserPassword = _ZhoneConfigSyncUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 3, 8),
    _ZhoneConfigSyncUserPassword_Type()
)
zhoneConfigSyncUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneConfigSyncUserPassword.setStatus("current")
_ZhoneAdmin_ObjectIdentity = ObjectIdentity
zhoneAdmin = _ZhoneAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 4)
)
if mibBuilder.loadTexts:
    zhoneAdmin.setStatus("current")
_ZhoneAdminCommunityTable_Object = MibTable
zhoneAdminCommunityTable = _ZhoneAdminCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    zhoneAdminCommunityTable.setStatus("current")
_ZhoneAdminCommunityEntry_Object = MibTableRow
zhoneAdminCommunityEntry = _ZhoneAdminCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 4, 1, 1)
)
zhoneAdminCommunityEntry.setIndexNames(
    (1, "ZHONE-SYSTEM-MIB", "zhoneAdminCommunityName"),
)
if mibBuilder.loadTexts:
    zhoneAdminCommunityEntry.setStatus("current")


class _ZhoneAdminCommunityName_Type(ZhoneAdminString):
    """Custom type zhoneAdminCommunityName based on ZhoneAdminString"""
    subtypeSpec = ZhoneAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZhoneAdminCommunityName_Type.__name__ = "ZhoneAdminString"
_ZhoneAdminCommunityName_Object = MibTableColumn
zhoneAdminCommunityName = _ZhoneAdminCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 4, 1, 1, 1),
    _ZhoneAdminCommunityName_Type()
)
zhoneAdminCommunityName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneAdminCommunityName.setStatus("current")


class _ZhoneAdminCommunityAccess_Type(Integer32):
    """Custom type zhoneAdminCommunityAccess based on Integer32"""
    defaultValue = 2

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
        *(("admin", 4),
          ("noAccess", 1),
          ("read", 2),
          ("readAndWrite", 3))
    )


_ZhoneAdminCommunityAccess_Type.__name__ = "Integer32"
_ZhoneAdminCommunityAccess_Object = MibTableColumn
zhoneAdminCommunityAccess = _ZhoneAdminCommunityAccess_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 4, 1, 1, 2),
    _ZhoneAdminCommunityAccess_Type()
)
zhoneAdminCommunityAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneAdminCommunityAccess.setStatus("current")


class _ZhoneAdminCommunityAccessListIndex_Type(Integer32):
    """Custom type zhoneAdminCommunityAccessListIndex based on Integer32"""
    defaultBinValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_ZhoneAdminCommunityAccessListIndex_Type.__name__ = "Integer32"
_ZhoneAdminCommunityAccessListIndex_Object = MibTableColumn
zhoneAdminCommunityAccessListIndex = _ZhoneAdminCommunityAccessListIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 4, 1, 1, 3),
    _ZhoneAdminCommunityAccessListIndex_Type()
)
zhoneAdminCommunityAccessListIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneAdminCommunityAccessListIndex.setStatus("current")
_ZhoneAdminCommunityRowStatus_Type = ZhoneRowStatus
_ZhoneAdminCommunityRowStatus_Object = MibTableColumn
zhoneAdminCommunityRowStatus = _ZhoneAdminCommunityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 4, 1, 1, 4),
    _ZhoneAdminCommunityRowStatus_Type()
)
zhoneAdminCommunityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneAdminCommunityRowStatus.setStatus("current")


class _ZhoneNextAdminAccessIndex_Type(Integer32):
    """Custom type zhoneNextAdminAccessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_ZhoneNextAdminAccessIndex_Type.__name__ = "Integer32"
_ZhoneNextAdminAccessIndex_Object = MibScalar
zhoneNextAdminAccessIndex = _ZhoneNextAdminAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 4, 2),
    _ZhoneNextAdminAccessIndex_Type()
)
zhoneNextAdminAccessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneNextAdminAccessIndex.setStatus("current")
_ZhoneAdminAccessListTable_Object = MibTable
zhoneAdminAccessListTable = _ZhoneAdminAccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 4, 3)
)
if mibBuilder.loadTexts:
    zhoneAdminAccessListTable.setStatus("current")
_ZhoneAdminAccessListEntry_Object = MibTableRow
zhoneAdminAccessListEntry = _ZhoneAdminAccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 4, 3, 1)
)
zhoneAdminAccessListEntry.setIndexNames(
    (0, "ZHONE-SYSTEM-MIB", "zhoneAdminAccessListIndex"),
    (0, "ZHONE-SYSTEM-MIB", "zhoneAdminAccessListIpAddress"),
)
if mibBuilder.loadTexts:
    zhoneAdminAccessListEntry.setStatus("current")


class _ZhoneAdminAccessListIndex_Type(Integer32):
    """Custom type zhoneAdminAccessListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_ZhoneAdminAccessListIndex_Type.__name__ = "Integer32"
_ZhoneAdminAccessListIndex_Object = MibTableColumn
zhoneAdminAccessListIndex = _ZhoneAdminAccessListIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 4, 3, 1, 1),
    _ZhoneAdminAccessListIndex_Type()
)
zhoneAdminAccessListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneAdminAccessListIndex.setStatus("current")
_ZhoneAdminAccessListIpAddress_Type = IpAddress
_ZhoneAdminAccessListIpAddress_Object = MibTableColumn
zhoneAdminAccessListIpAddress = _ZhoneAdminAccessListIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 4, 3, 1, 2),
    _ZhoneAdminAccessListIpAddress_Type()
)
zhoneAdminAccessListIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneAdminAccessListIpAddress.setStatus("current")
_ZhoneAdminAccessRowStatus_Type = ZhoneRowStatus
_ZhoneAdminAccessRowStatus_Object = MibTableColumn
zhoneAdminAccessRowStatus = _ZhoneAdminAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 4, 3, 1, 3),
    _ZhoneAdminAccessRowStatus_Type()
)
zhoneAdminAccessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneAdminAccessRowStatus.setStatus("current")
_ZhoneUser_ObjectIdentity = ObjectIdentity
zhoneUser = _ZhoneUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 4, 4)
)
if mibBuilder.loadTexts:
    zhoneUser.setStatus("current")


class _ZhoneUserIdNext_Type(Integer32):
    """Custom type zhoneUserIdNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_ZhoneUserIdNext_Type.__name__ = "Integer32"
_ZhoneUserIdNext_Object = MibScalar
zhoneUserIdNext = _ZhoneUserIdNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 4, 4, 1),
    _ZhoneUserIdNext_Type()
)
zhoneUserIdNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneUserIdNext.setStatus("current")
_ZhoneUserTotalFailedLogins_Type = Counter32
_ZhoneUserTotalFailedLogins_Object = MibScalar
zhoneUserTotalFailedLogins = _ZhoneUserTotalFailedLogins_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 4, 4, 2),
    _ZhoneUserTotalFailedLogins_Type()
)
zhoneUserTotalFailedLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneUserTotalFailedLogins.setStatus("current")
_ZhoneUserTable_Object = MibTable
zhoneUserTable = _ZhoneUserTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 4, 4, 3)
)
if mibBuilder.loadTexts:
    zhoneUserTable.setStatus("current")
_ZhoneUserEntry_Object = MibTableRow
zhoneUserEntry = _ZhoneUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 4, 4, 3, 1)
)
zhoneUserEntry.setIndexNames(
    (0, "ZHONE-SYSTEM-MIB", "zhoneUserId"),
)
if mibBuilder.loadTexts:
    zhoneUserEntry.setStatus("current")


class _ZhoneUserId_Type(Integer32):
    """Custom type zhoneUserId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_ZhoneUserId_Type.__name__ = "Integer32"
_ZhoneUserId_Object = MibTableColumn
zhoneUserId = _ZhoneUserId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 4, 4, 3, 1, 1),
    _ZhoneUserId_Type()
)
zhoneUserId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneUserId.setStatus("current")
_ZhoneUserName_Type = ZhoneAdminString
_ZhoneUserName_Object = MibTableColumn
zhoneUserName = _ZhoneUserName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 4, 4, 3, 1, 2),
    _ZhoneUserName_Type()
)
zhoneUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneUserName.setStatus("current")
_ZhoneUserPassword_Type = ZhoneAdminString
_ZhoneUserPassword_Object = MibTableColumn
zhoneUserPassword = _ZhoneUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 4, 4, 3, 1, 3),
    _ZhoneUserPassword_Type()
)
zhoneUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneUserPassword.setStatus("current")


class _ZhoneUserPrompt_Type(ZhoneAdminString):
    """Custom type zhoneUserPrompt based on ZhoneAdminString"""
    defaultValue = OctetString("zSH> ")


_ZhoneUserPrompt_Object = MibTableColumn
zhoneUserPrompt = _ZhoneUserPrompt_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 4, 4, 3, 1, 4),
    _ZhoneUserPrompt_Type()
)
zhoneUserPrompt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneUserPrompt.setStatus("current")


class _ZhoneUserAccessLevel_Type(Bits):
    """Custom type zhoneUserAccessLevel based on Bits"""
    namedValues = NamedValues(
        *(("userAccessAdmin", 0),
          ("userAccessData", 2),
          ("userAccessDatabase", 4),
          ("userAccessDebug", 7),
          ("userAccessManuf", 3),
          ("userAccessSystems", 5),
          ("userAccessTool", 6),
          ("userAccessVoice", 1))
    )

_ZhoneUserAccessLevel_Type.__name__ = "Bits"
_ZhoneUserAccessLevel_Object = MibTableColumn
zhoneUserAccessLevel = _ZhoneUserAccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 4, 4, 3, 1, 5),
    _ZhoneUserAccessLevel_Type()
)
zhoneUserAccessLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneUserAccessLevel.setStatus("current")


class _ZhoneUserAdmin_Type(Integer32):
    """Custom type zhoneUserAdmin based on Integer32"""
    defaultValue = 1

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


_ZhoneUserAdmin_Type.__name__ = "Integer32"
_ZhoneUserAdmin_Object = MibTableColumn
zhoneUserAdmin = _ZhoneUserAdmin_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 4, 4, 3, 1, 6),
    _ZhoneUserAdmin_Type()
)
zhoneUserAdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneUserAdmin.setStatus("current")
_ZhoneUserLogins_Type = Counter32
_ZhoneUserLogins_Object = MibTableColumn
zhoneUserLogins = _ZhoneUserLogins_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 4, 4, 3, 1, 7),
    _ZhoneUserLogins_Type()
)
zhoneUserLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneUserLogins.setStatus("current")
_ZhoneUserFailedLogins_Type = Counter32
_ZhoneUserFailedLogins_Object = MibTableColumn
zhoneUserFailedLogins = _ZhoneUserFailedLogins_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 4, 4, 3, 1, 8),
    _ZhoneUserFailedLogins_Type()
)
zhoneUserFailedLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneUserFailedLogins.setStatus("current")
_ZhoneUserRowStatus_Type = ZhoneRowStatus
_ZhoneUserRowStatus_Object = MibTableColumn
zhoneUserRowStatus = _ZhoneUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 4, 4, 3, 1, 9),
    _ZhoneUserRowStatus_Type()
)
zhoneUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneUserRowStatus.setStatus("current")
_ZhoneSystemConfiguration_ObjectIdentity = ObjectIdentity
zhoneSystemConfiguration = _ZhoneSystemConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5)
)
if mibBuilder.loadTexts:
    zhoneSystemConfiguration.setStatus("current")
_ZhoneSystemConfigurationNumShelves_Type = Integer32
_ZhoneSystemConfigurationNumShelves_Object = MibScalar
zhoneSystemConfigurationNumShelves = _ZhoneSystemConfigurationNumShelves_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 1),
    _ZhoneSystemConfigurationNumShelves_Type()
)
zhoneSystemConfigurationNumShelves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSystemConfigurationNumShelves.setStatus("current")
if mibBuilder.loadTexts:
    zhoneSystemConfigurationNumShelves.setUnits("shelves")


class _ZhoneSystemConfigurationShelvesArray_Type(OctetString):
    """Custom type zhoneSystemConfigurationShelvesArray based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_ZhoneSystemConfigurationShelvesArray_Type.__name__ = "OctetString"
_ZhoneSystemConfigurationShelvesArray_Object = MibScalar
zhoneSystemConfigurationShelvesArray = _ZhoneSystemConfigurationShelvesArray_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 2),
    _ZhoneSystemConfigurationShelvesArray_Type()
)
zhoneSystemConfigurationShelvesArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSystemConfigurationShelvesArray.setStatus("current")
_ZhoneSystemConfigurationNumCards_Type = Integer32
_ZhoneSystemConfigurationNumCards_Object = MibScalar
zhoneSystemConfigurationNumCards = _ZhoneSystemConfigurationNumCards_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 3),
    _ZhoneSystemConfigurationNumCards_Type()
)
zhoneSystemConfigurationNumCards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSystemConfigurationNumCards.setStatus("current")
_ZhoneSystemConfigurationIpAddress_Type = IpAddress
_ZhoneSystemConfigurationIpAddress_Object = MibScalar
zhoneSystemConfigurationIpAddress = _ZhoneSystemConfigurationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 4),
    _ZhoneSystemConfigurationIpAddress_Type()
)
zhoneSystemConfigurationIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSystemConfigurationIpAddress.setStatus("current")
_ZhoneSystemConfigurationAlternateIpAddress_Type = IpAddress
_ZhoneSystemConfigurationAlternateIpAddress_Object = MibScalar
zhoneSystemConfigurationAlternateIpAddress = _ZhoneSystemConfigurationAlternateIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 5),
    _ZhoneSystemConfigurationAlternateIpAddress_Type()
)
zhoneSystemConfigurationAlternateIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSystemConfigurationAlternateIpAddress.setStatus("current")
_ZhoneSystemConfigurationDateAndTime_Type = DateAndTime
_ZhoneSystemConfigurationDateAndTime_Object = MibScalar
zhoneSystemConfigurationDateAndTime = _ZhoneSystemConfigurationDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 6),
    _ZhoneSystemConfigurationDateAndTime_Type()
)
zhoneSystemConfigurationDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSystemConfigurationDateAndTime.setStatus("current")


class _ZhoneSystemConfigurationCountryRegion_Type(ZhoneCountryCode):
    """Custom type zhoneSystemConfigurationCountryRegion based on ZhoneCountryCode"""


_ZhoneSystemConfigurationCountryRegion_Object = MibScalar
zhoneSystemConfigurationCountryRegion = _ZhoneSystemConfigurationCountryRegion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 7),
    _ZhoneSystemConfigurationCountryRegion_Type()
)
zhoneSystemConfigurationCountryRegion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSystemConfigurationCountryRegion.setStatus("current")


class _ZhonePrimaryClockSource_Type(InterfaceIndexOrZero):
    """Custom type zhonePrimaryClockSource based on InterfaceIndexOrZero"""
    defaultValue = 0


_ZhonePrimaryClockSource_Object = MibScalar
zhonePrimaryClockSource = _ZhonePrimaryClockSource_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 8),
    _ZhonePrimaryClockSource_Type()
)
zhonePrimaryClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhonePrimaryClockSource.setStatus("deprecated")


class _ZhoneSystemConfigurationRingSource_Type(Integer32):
    """Custom type zhoneSystemConfigurationRingSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalRingSourceLabel", 2),
          ("internalRingSourceLabel", 1))
    )


_ZhoneSystemConfigurationRingSource_Type.__name__ = "Integer32"
_ZhoneSystemConfigurationRingSource_Object = MibScalar
zhoneSystemConfigurationRingSource = _ZhoneSystemConfigurationRingSource_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 9),
    _ZhoneSystemConfigurationRingSource_Type()
)
zhoneSystemConfigurationRingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSystemConfigurationRingSource.setStatus("current")
_ZhoneSystemCurrentClockSource_Type = InterfaceIndexOrZero
_ZhoneSystemCurrentClockSource_Object = MibScalar
zhoneSystemCurrentClockSource = _ZhoneSystemCurrentClockSource_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 10),
    _ZhoneSystemCurrentClockSource_Type()
)
zhoneSystemCurrentClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSystemCurrentClockSource.setStatus("current")
_ZhoneSystemSecondaryClockSource_Type = InterfaceIndexOrZero
_ZhoneSystemSecondaryClockSource_Object = MibScalar
zhoneSystemSecondaryClockSource = _ZhoneSystemSecondaryClockSource_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 11),
    _ZhoneSystemSecondaryClockSource_Type()
)
zhoneSystemSecondaryClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSystemSecondaryClockSource.setStatus("current")
_ZhoneSystemClockTable_Object = MibTable
zhoneSystemClockTable = _ZhoneSystemClockTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 12)
)
if mibBuilder.loadTexts:
    zhoneSystemClockTable.setStatus("current")
_ZhoneSystemClockEntry_Object = MibTableRow
zhoneSystemClockEntry = _ZhoneSystemClockEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 12, 1)
)
zhoneSystemClockEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zhoneSystemClockEntry.setStatus("current")


class _ZhoneSystemClockEligibility_Type(TruthValue):
    """Custom type zhoneSystemClockEligibility based on TruthValue"""


_ZhoneSystemClockEligibility_Object = MibTableColumn
zhoneSystemClockEligibility = _ZhoneSystemClockEligibility_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 12, 1, 1),
    _ZhoneSystemClockEligibility_Type()
)
zhoneSystemClockEligibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSystemClockEligibility.setStatus("current")


class _ZhoneSystemClockWeight_Type(Integer32):
    """Custom type zhoneSystemClockWeight based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ZhoneSystemClockWeight_Type.__name__ = "Integer32"
_ZhoneSystemClockWeight_Object = MibTableColumn
zhoneSystemClockWeight = _ZhoneSystemClockWeight_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 12, 1, 2),
    _ZhoneSystemClockWeight_Type()
)
zhoneSystemClockWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSystemClockWeight.setStatus("current")


class _ZhoneSystemClockAvailabilityStatus_Type(Integer32):
    """Custom type zhoneSystemClockAvailabilityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_ZhoneSystemClockAvailabilityStatus_Type.__name__ = "Integer32"
_ZhoneSystemClockAvailabilityStatus_Object = MibTableColumn
zhoneSystemClockAvailabilityStatus = _ZhoneSystemClockAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 12, 1, 3),
    _ZhoneSystemClockAvailabilityStatus_Type()
)
zhoneSystemClockAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSystemClockAvailabilityStatus.setStatus("current")


class _ZhoneSystemClockTxClockMode_Type(Integer32):
    """Custom type zhoneSystemClockTxClockMode based on Integer32"""
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
        *(("localTiming", 3),
          ("loopTiming", 4),
          ("other", 1),
          ("provisionedTiming", 2),
          ("throughTiming", 5))
    )


_ZhoneSystemClockTxClockMode_Type.__name__ = "Integer32"
_ZhoneSystemClockTxClockMode_Object = MibTableColumn
zhoneSystemClockTxClockMode = _ZhoneSystemClockTxClockMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 12, 1, 4),
    _ZhoneSystemClockTxClockMode_Type()
)
zhoneSystemClockTxClockMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSystemClockTxClockMode.setStatus("current")


class _ZhoneSystemConsoleLogging_Type(Integer32):
    """Custom type zhoneSystemConsoleLogging based on Integer32"""
    defaultValue = 1

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


_ZhoneSystemConsoleLogging_Type.__name__ = "Integer32"
_ZhoneSystemConsoleLogging_Object = MibScalar
zhoneSystemConsoleLogging = _ZhoneSystemConsoleLogging_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 13),
    _ZhoneSystemConsoleLogging_Type()
)
zhoneSystemConsoleLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSystemConsoleLogging.setStatus("current")


class _ZhoneSystemRevertiveClockSource_Type(TruthValue):
    """Custom type zhoneSystemRevertiveClockSource based on TruthValue"""


_ZhoneSystemRevertiveClockSource_Object = MibScalar
zhoneSystemRevertiveClockSource = _ZhoneSystemRevertiveClockSource_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 14),
    _ZhoneSystemRevertiveClockSource_Type()
)
zhoneSystemRevertiveClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSystemRevertiveClockSource.setStatus("current")


class _ZhoneSystemVoiceBandwidthCheck_Type(TruthValue):
    """Custom type zhoneSystemVoiceBandwidthCheck based on TruthValue"""


_ZhoneSystemVoiceBandwidthCheck_Object = MibScalar
zhoneSystemVoiceBandwidthCheck = _ZhoneSystemVoiceBandwidthCheck_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 15),
    _ZhoneSystemVoiceBandwidthCheck_Type()
)
zhoneSystemVoiceBandwidthCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSystemVoiceBandwidthCheck.setStatus("current")


class _ZhoneAlarmLevelsEnabled_Type(Bits):
    """Custom type zhoneAlarmLevelsEnabled based on Bits"""
    namedValues = NamedValues(
        *(("critical", 0),
          ("major", 1),
          ("minor", 2),
          ("warning", 3))
    )

_ZhoneAlarmLevelsEnabled_Type.__name__ = "Bits"
_ZhoneAlarmLevelsEnabled_Object = MibScalar
zhoneAlarmLevelsEnabled = _ZhoneAlarmLevelsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 16),
    _ZhoneAlarmLevelsEnabled_Type()
)
zhoneAlarmLevelsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAlarmLevelsEnabled.setStatus("current")


class _ZhoneSystemUserAuthMethod_Type(Integer32):
    """Custom type zhoneSystemUserAuthMethod based on Integer32"""
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
        *(("local", 1),
          ("radius", 2),
          ("radiusThenCraft", 4),
          ("radiusThenLocal", 3))
    )


_ZhoneSystemUserAuthMethod_Type.__name__ = "Integer32"
_ZhoneSystemUserAuthMethod_Object = MibScalar
zhoneSystemUserAuthMethod = _ZhoneSystemUserAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 17),
    _ZhoneSystemUserAuthMethod_Type()
)
zhoneSystemUserAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSystemUserAuthMethod.setStatus("current")
_ZhoneSystemRadiusAuthIndex_Type = Integer32
_ZhoneSystemRadiusAuthIndex_Object = MibScalar
zhoneSystemRadiusAuthIndex = _ZhoneSystemRadiusAuthIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 18),
    _ZhoneSystemRadiusAuthIndex_Type()
)
zhoneSystemRadiusAuthIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSystemRadiusAuthIndex.setStatus("current")


class _ZhoneSystemSecureFTP_Type(Integer32):
    """Custom type zhoneSystemSecureFTP based on Integer32"""
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


_ZhoneSystemSecureFTP_Type.__name__ = "Integer32"
_ZhoneSystemSecureFTP_Object = MibScalar
zhoneSystemSecureFTP = _ZhoneSystemSecureFTP_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 19),
    _ZhoneSystemSecureFTP_Type()
)
zhoneSystemSecureFTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSystemSecureFTP.setStatus("current")


class _ZhoneSystemWebInterface_Type(Integer32):
    """Custom type zhoneSystemWebInterface based on Integer32"""
    defaultValue = 1

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


_ZhoneSystemWebInterface_Type.__name__ = "Integer32"
_ZhoneSystemWebInterface_Object = MibScalar
zhoneSystemWebInterface = _ZhoneSystemWebInterface_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 20),
    _ZhoneSystemWebInterface_Type()
)
zhoneSystemWebInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSystemWebInterface.setStatus("current")


class _ZhoneSystemConfigurationOptions_Type(Bits):
    """Custom type zhoneSystemConfigurationOptions based on Bits"""
    namedValues = NamedValues(
        *(("cfmon", 6),
          ("cvlanonly", 0),
          ("disdefpktrules", 3),
          ("enablexcardlinkagg", 4),
          ("fiberlan", 5),
          ("ipg88bits", 2),
          ("nol3bridgetable", 1))
    )

_ZhoneSystemConfigurationOptions_Type.__name__ = "Bits"
_ZhoneSystemConfigurationOptions_Object = MibScalar
zhoneSystemConfigurationOptions = _ZhoneSystemConfigurationOptions_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 21),
    _ZhoneSystemConfigurationOptions_Type()
)
zhoneSystemConfigurationOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSystemConfigurationOptions.setStatus("current")


class _ZhoneSystemConfigurationReservedVlanIdStart_Type(Unsigned32):
    """Custom type zhoneSystemConfigurationReservedVlanIdStart based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4090),
    )


_ZhoneSystemConfigurationReservedVlanIdStart_Type.__name__ = "Unsigned32"
_ZhoneSystemConfigurationReservedVlanIdStart_Object = MibScalar
zhoneSystemConfigurationReservedVlanIdStart = _ZhoneSystemConfigurationReservedVlanIdStart_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 22),
    _ZhoneSystemConfigurationReservedVlanIdStart_Type()
)
zhoneSystemConfigurationReservedVlanIdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSystemConfigurationReservedVlanIdStart.setStatus("current")


class _ZhoneSystemConfigurationReservedVlanIdCount_Type(Unsigned32):
    """Custom type zhoneSystemConfigurationReservedVlanIdCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_ZhoneSystemConfigurationReservedVlanIdCount_Type.__name__ = "Unsigned32"
_ZhoneSystemConfigurationReservedVlanIdCount_Object = MibScalar
zhoneSystemConfigurationReservedVlanIdCount = _ZhoneSystemConfigurationReservedVlanIdCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 23),
    _ZhoneSystemConfigurationReservedVlanIdCount_Type()
)
zhoneSystemConfigurationReservedVlanIdCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSystemConfigurationReservedVlanIdCount.setStatus("current")


class _ZhoneSystemSnmpVersion_Type(Integer32):
    """Custom type zhoneSystemSnmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmpv2", 1),
          ("snmpv3", 2),
          ("snmpv3includingZMS", 3))
    )


_ZhoneSystemSnmpVersion_Type.__name__ = "Integer32"
_ZhoneSystemSnmpVersion_Object = MibScalar
zhoneSystemSnmpVersion = _ZhoneSystemSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 24),
    _ZhoneSystemSnmpVersion_Type()
)
zhoneSystemSnmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSystemSnmpVersion.setStatus("current")


class _ZhoneSystemPersistentLogging_Type(Integer32):
    """Custom type zhoneSystemPersistentLogging based on Integer32"""
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


_ZhoneSystemPersistentLogging_Type.__name__ = "Integer32"
_ZhoneSystemPersistentLogging_Object = MibScalar
zhoneSystemPersistentLogging = _ZhoneSystemPersistentLogging_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 25),
    _ZhoneSystemPersistentLogging_Type()
)
zhoneSystemPersistentLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSystemPersistentLogging.setStatus("current")


class _ZhoneSystemOutletTemperatureHighThreshold_Type(Integer32):
    """Custom type zhoneSystemOutletTemperatureHighThreshold based on Integer32"""
    defaultValue = 65

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(35, 75),
    )


_ZhoneSystemOutletTemperatureHighThreshold_Type.__name__ = "Integer32"
_ZhoneSystemOutletTemperatureHighThreshold_Object = MibScalar
zhoneSystemOutletTemperatureHighThreshold = _ZhoneSystemOutletTemperatureHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 26),
    _ZhoneSystemOutletTemperatureHighThreshold_Type()
)
zhoneSystemOutletTemperatureHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSystemOutletTemperatureHighThreshold.setStatus("current")


class _ZhoneSystemOutletTemperatureLowThreshold_Type(Integer32):
    """Custom type zhoneSystemOutletTemperatureLowThreshold based on Integer32"""
    defaultValue = -12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 0),
    )


_ZhoneSystemOutletTemperatureLowThreshold_Type.__name__ = "Integer32"
_ZhoneSystemOutletTemperatureLowThreshold_Object = MibScalar
zhoneSystemOutletTemperatureLowThreshold = _ZhoneSystemOutletTemperatureLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 5, 27),
    _ZhoneSystemOutletTemperatureLowThreshold_Type()
)
zhoneSystemOutletTemperatureLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSystemOutletTemperatureLowThreshold.setStatus("current")
_ZhoneSoftwareLoadTable_Object = MibTable
zhoneSoftwareLoadTable = _ZhoneSoftwareLoadTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 6)
)
if mibBuilder.loadTexts:
    zhoneSoftwareLoadTable.setStatus("current")
_ZhoneSoftwareLoadEntry_Object = MibTableRow
zhoneSoftwareLoadEntry = _ZhoneSoftwareLoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 6, 1)
)
zhoneSoftwareLoadEntry.setIndexNames(
    (0, "ZHONE-SYSTEM-MIB", "zhoneSwCardType"),
)
if mibBuilder.loadTexts:
    zhoneSoftwareLoadEntry.setStatus("current")
_ZhoneSwCardType_Type = ZhoneCardType
_ZhoneSwCardType_Object = MibTableColumn
zhoneSwCardType = _ZhoneSwCardType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 6, 1, 1),
    _ZhoneSwCardType_Type()
)
zhoneSwCardType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneSwCardType.setStatus("current")
_ZhoneSwCardSwFileName_Type = ZhoneFileName
_ZhoneSwCardSwFileName_Object = MibTableColumn
zhoneSwCardSwFileName = _ZhoneSwCardSwFileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 6, 1, 2),
    _ZhoneSwCardSwFileName_Type()
)
zhoneSwCardSwFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneSwCardSwFileName.setStatus("current")
_ZhoneSwLoadRowStatus_Type = ZhoneRowStatus
_ZhoneSwLoadRowStatus_Object = MibTableColumn
zhoneSwLoadRowStatus = _ZhoneSwLoadRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 6, 1, 3),
    _ZhoneSwLoadRowStatus_Type()
)
zhoneSwLoadRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneSwLoadRowStatus.setStatus("current")
_ZhoneSnmpErrorTable_Object = MibTable
zhoneSnmpErrorTable = _ZhoneSnmpErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 7)
)
if mibBuilder.loadTexts:
    zhoneSnmpErrorTable.setStatus("current")
_ZhoneSnmpErrorEntry_Object = MibTableRow
zhoneSnmpErrorEntry = _ZhoneSnmpErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 7, 1)
)
zhoneSnmpErrorEntry.setIndexNames(
    (0, "ZHONE-SYSTEM-MIB", "zhoneSnmpErrorIpAddress"),
    (0, "ZHONE-SYSTEM-MIB", "zhoneSnmpErrorReqId"),
)
if mibBuilder.loadTexts:
    zhoneSnmpErrorEntry.setStatus("current")
_ZhoneSnmpErrorIpAddress_Type = IpAddress
_ZhoneSnmpErrorIpAddress_Object = MibTableColumn
zhoneSnmpErrorIpAddress = _ZhoneSnmpErrorIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 7, 1, 1),
    _ZhoneSnmpErrorIpAddress_Type()
)
zhoneSnmpErrorIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneSnmpErrorIpAddress.setStatus("current")
_ZhoneSnmpErrorReqId_Type = Unsigned32
_ZhoneSnmpErrorReqId_Object = MibTableColumn
zhoneSnmpErrorReqId = _ZhoneSnmpErrorReqId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 7, 1, 2),
    _ZhoneSnmpErrorReqId_Type()
)
zhoneSnmpErrorReqId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneSnmpErrorReqId.setStatus("current")


class _ZhoneSnmpErrorDisplayString_Type(OctetString):
    """Custom type zhoneSnmpErrorDisplayString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_ZhoneSnmpErrorDisplayString_Type.__name__ = "OctetString"
_ZhoneSnmpErrorDisplayString_Object = MibTableColumn
zhoneSnmpErrorDisplayString = _ZhoneSnmpErrorDisplayString_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 7, 1, 3),
    _ZhoneSnmpErrorDisplayString_Type()
)
zhoneSnmpErrorDisplayString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSnmpErrorDisplayString.setStatus("current")
_ZhoneSnmpErrorTime_Type = TimeTicks
_ZhoneSnmpErrorTime_Object = MibTableColumn
zhoneSnmpErrorTime = _ZhoneSnmpErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 7, 1, 4),
    _ZhoneSnmpErrorTime_Type()
)
zhoneSnmpErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSnmpErrorTime.setStatus("current")
_ZhoneSoftwareDownload_ObjectIdentity = ObjectIdentity
zhoneSoftwareDownload = _ZhoneSoftwareDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 8)
)
if mibBuilder.loadTexts:
    zhoneSoftwareDownload.setStatus("current")
_ZhoneSysSwLogin_Type = ZhoneAdminString
_ZhoneSysSwLogin_Object = MibScalar
zhoneSysSwLogin = _ZhoneSysSwLogin_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 8, 1),
    _ZhoneSysSwLogin_Type()
)
zhoneSysSwLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSysSwLogin.setStatus("current")
_ZhoneSysSwPassword_Type = ZhoneAdminString
_ZhoneSysSwPassword_Object = MibScalar
zhoneSysSwPassword = _ZhoneSysSwPassword_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 8, 2),
    _ZhoneSysSwPassword_Type()
)
zhoneSysSwPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSysSwPassword.setStatus("current")
_ZhoneSysSwPriLoadServer_Type = IpAddress
_ZhoneSysSwPriLoadServer_Object = MibScalar
zhoneSysSwPriLoadServer = _ZhoneSysSwPriLoadServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 8, 3),
    _ZhoneSysSwPriLoadServer_Type()
)
zhoneSysSwPriLoadServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSysSwPriLoadServer.setStatus("current")
_ZhoneSysSwSecLoadServer_Type = IpAddress
_ZhoneSysSwSecLoadServer_Object = MibScalar
zhoneSysSwSecLoadServer = _ZhoneSysSwSecLoadServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 8, 4),
    _ZhoneSysSwSecLoadServer_Type()
)
zhoneSysSwSecLoadServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSysSwSecLoadServer.setStatus("current")


class _ZhoneSysSwRemoteFilePath_Type(OctetString):
    """Custom type zhoneSysSwRemoteFilePath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZhoneSysSwRemoteFilePath_Type.__name__ = "OctetString"
_ZhoneSysSwRemoteFilePath_Object = MibScalar
zhoneSysSwRemoteFilePath = _ZhoneSysSwRemoteFilePath_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 8, 5),
    _ZhoneSysSwRemoteFilePath_Type()
)
zhoneSysSwRemoteFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSysSwRemoteFilePath.setStatus("current")
_ZhoneSysSwLocalFilePath_Type = ZhoneFileName
_ZhoneSysSwLocalFilePath_Object = MibScalar
zhoneSysSwLocalFilePath = _ZhoneSysSwLocalFilePath_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 8, 6),
    _ZhoneSysSwLocalFilePath_Type()
)
zhoneSysSwLocalFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSysSwLocalFilePath.setStatus("current")


class _ZhoneSysSwAdmin_Type(Integer32):
    """Custom type zhoneSysSwAdmin based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("abortDownLoadSw", 2),
          ("backupDatabase", 13),
          ("configDatabaseActivate", 12),
          ("configScriptActivate", 11),
          ("delete", 3),
          ("downLoadFile", 6),
          ("downLoadSw", 1),
          ("dumpFile", 8),
          ("dumpNetwork", 9),
          ("imageFlashActive", 4),
          ("imageFlashStandby", 5),
          ("restore", 10),
          ("restoreDatabase", 14),
          ("upLoadFile", 7))
    )


_ZhoneSysSwAdmin_Type.__name__ = "Integer32"
_ZhoneSysSwAdmin_Object = MibScalar
zhoneSysSwAdmin = _ZhoneSysSwAdmin_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 8, 7),
    _ZhoneSysSwAdmin_Type()
)
zhoneSysSwAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSysSwAdmin.setStatus("current")


class _ZhoneSysSwStatus_Type(Integer32):
    """Custom type zhoneSysSwStatus based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("deleteFileInUse", 7),
          ("deleteFileNotFound", 6),
          ("deleteSuccessful", 8),
          ("downLoadSwAborted", 3),
          ("downLoadSwFailed", 4),
          ("downLoadSwInProgress", 2),
          ("downLoadSwSuccessful", 5),
          ("downLoadSwUnknown", 1),
          ("operationAborted", 10),
          ("operationFailed", 11),
          ("operationInProgress", 9),
          ("operationSuccessful", 12))
    )


_ZhoneSysSwStatus_Type.__name__ = "Integer32"
_ZhoneSysSwStatus_Object = MibScalar
zhoneSysSwStatus = _ZhoneSysSwStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 8, 8),
    _ZhoneSysSwStatus_Type()
)
zhoneSysSwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSysSwStatus.setStatus("current")
_ZhoneSoftwareReboot_ObjectIdentity = ObjectIdentity
zhoneSoftwareReboot = _ZhoneSoftwareReboot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 9)
)
if mibBuilder.loadTexts:
    zhoneSoftwareReboot.setStatus("current")


class _ZhoneSysRebootAdmin_Type(Integer32):
    """Custom type zhoneSysRebootAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rebootByCardType", 2),
          ("systemReboot", 1))
    )


_ZhoneSysRebootAdmin_Type.__name__ = "Integer32"
_ZhoneSysRebootAdmin_Object = MibScalar
zhoneSysRebootAdmin = _ZhoneSysRebootAdmin_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 9, 1),
    _ZhoneSysRebootAdmin_Type()
)
zhoneSysRebootAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSysRebootAdmin.setStatus("current")
_ZhoneSysRebootCardType_Type = ZhoneCardType
_ZhoneSysRebootCardType_Object = MibScalar
zhoneSysRebootCardType = _ZhoneSysRebootCardType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 9, 2),
    _ZhoneSysRebootCardType_Type()
)
zhoneSysRebootCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSysRebootCardType.setStatus("current")
_ZhoneSysCardSoftwareConfigTable_Object = MibTable
zhoneSysCardSoftwareConfigTable = _ZhoneSysCardSoftwareConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 10)
)
if mibBuilder.loadTexts:
    zhoneSysCardSoftwareConfigTable.setStatus("current")
_ZhoneSysCardSoftwareConfigEntry_Object = MibTableRow
zhoneSysCardSoftwareConfigEntry = _ZhoneSysCardSoftwareConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 10, 1)
)
zhoneSysCardSoftwareConfigEntry.setIndexNames(
    (0, "Zhone", "zhoneShelfIndex"),
    (0, "Zhone", "zhoneSlotIndex"),
)
if mibBuilder.loadTexts:
    zhoneSysCardSoftwareConfigEntry.setStatus("current")


class _ZhoneSysCardSpecificSwFileName_Type(ZhoneFileName):
    """Custom type zhoneSysCardSpecificSwFileName based on ZhoneFileName"""
    defaultValue = OctetString(" ")


_ZhoneSysCardSpecificSwFileName_Object = MibTableColumn
zhoneSysCardSpecificSwFileName = _ZhoneSysCardSpecificSwFileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 10, 1, 1),
    _ZhoneSysCardSpecificSwFileName_Type()
)
zhoneSysCardSpecificSwFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneSysCardSpecificSwFileName.setStatus("current")
_ZhoneSysCardSwSpecificVers_Type = ZhoneAdminString
_ZhoneSysCardSwSpecificVers_Object = MibTableColumn
zhoneSysCardSwSpecificVers = _ZhoneSysCardSwSpecificVers_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 10, 1, 2),
    _ZhoneSysCardSwSpecificVers_Type()
)
zhoneSysCardSwSpecificVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSysCardSwSpecificVers.setStatus("current")


class _ZhoneSysCardUpgradeSwFileName_Type(ZhoneFileName):
    """Custom type zhoneSysCardUpgradeSwFileName based on ZhoneFileName"""
    defaultValue = OctetString("  ")


_ZhoneSysCardUpgradeSwFileName_Object = MibTableColumn
zhoneSysCardUpgradeSwFileName = _ZhoneSysCardUpgradeSwFileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 10, 1, 3),
    _ZhoneSysCardUpgradeSwFileName_Type()
)
zhoneSysCardUpgradeSwFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneSysCardUpgradeSwFileName.setStatus("current")
_ZhoneSysCardSwUpgradeVers_Type = ZhoneAdminString
_ZhoneSysCardSwUpgradeVers_Object = MibTableColumn
zhoneSysCardSwUpgradeVers = _ZhoneSysCardSwUpgradeVers_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 10, 1, 4),
    _ZhoneSysCardSwUpgradeVers_Type()
)
zhoneSysCardSwUpgradeVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSysCardSwUpgradeVers.setStatus("current")
_ZhoneSysCardSwType_Type = ZhoneCardType
_ZhoneSysCardSwType_Object = MibTableColumn
zhoneSysCardSwType = _ZhoneSysCardSwType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 10, 1, 5),
    _ZhoneSysCardSwType_Type()
)
zhoneSysCardSwType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneSysCardSwType.setStatus("current")


class _ZhoneSysCardSwEnable_Type(TruthValue):
    """Custom type zhoneSysCardSwEnable based on TruthValue"""


_ZhoneSysCardSwEnable_Object = MibTableColumn
zhoneSysCardSwEnable = _ZhoneSysCardSwEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 10, 1, 6),
    _ZhoneSysCardSwEnable_Type()
)
zhoneSysCardSwEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneSysCardSwEnable.setStatus("current")


class _ZhoneSysCardSwUpgradeEnable_Type(TruthValue):
    """Custom type zhoneSysCardSwUpgradeEnable based on TruthValue"""


_ZhoneSysCardSwUpgradeEnable_Object = MibTableColumn
zhoneSysCardSwUpgradeEnable = _ZhoneSysCardSwUpgradeEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 10, 1, 7),
    _ZhoneSysCardSwUpgradeEnable_Type()
)
zhoneSysCardSwUpgradeEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneSysCardSwUpgradeEnable.setStatus("current")
_ZhoneSysCardRowStatus_Type = ZhoneRowStatus
_ZhoneSysCardRowStatus_Object = MibTableColumn
zhoneSysCardRowStatus = _ZhoneSysCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 10, 1, 8),
    _ZhoneSysCardRowStatus_Type()
)
zhoneSysCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneSysCardRowStatus.setStatus("current")


class _ZhoneSysCardLineType_Type(ZhoneCardLineType):
    """Custom type zhoneSysCardLineType based on ZhoneCardLineType"""


_ZhoneSysCardLineType_Object = MibTableColumn
zhoneSysCardLineType = _ZhoneSysCardLineType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 10, 1, 9),
    _ZhoneSysCardLineType_Type()
)
zhoneSysCardLineType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneSysCardLineType.setStatus("current")


class _ZhoneSysCardAtmConfiguration_Type(Integer32):
    """Custom type zhoneSysCardAtmConfiguration based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              99)
        )
    )
    namedValues = NamedValues(
        *(("cellRelayAndManagement", 3),
          ("cellRelayOnly", 2),
          ("dataTerm", 4),
          ("hybridDefault", 7),
          ("hybridHighAal5Data", 8),
          ("hybridLowAal5Data", 6),
          ("manual", 99),
          ("notApplicable", 1),
          ("vbnrt20rt75", 14),
          ("vbnrt35rt60", 13),
          ("vbnrt50rt45", 12),
          ("vbnrt5rt95", 15),
          ("vbnrt5rt95cbr", 16),
          ("vbnrt65rt30", 11),
          ("vbnrt80rt15", 10),
          ("vbnrt95rt5", 9),
          ("voiceGateway", 5))
    )


_ZhoneSysCardAtmConfiguration_Type.__name__ = "Integer32"
_ZhoneSysCardAtmConfiguration_Object = MibTableColumn
zhoneSysCardAtmConfiguration = _ZhoneSysCardAtmConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 10, 1, 10),
    _ZhoneSysCardAtmConfiguration_Type()
)
zhoneSysCardAtmConfiguration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneSysCardAtmConfiguration.setStatus("current")


class _ZhoneSysCardLineVoltage_Type(Integer32):
    """Custom type zhoneSysCardLineVoltage based on Integer32"""
    defaultValue = 1

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
        *(("lv-100-volts", 5),
          ("lv-110-volts", 6),
          ("lv-60-volts", 2),
          ("lv-68-volts", 3),
          ("lv-95-volts", 4),
          ("not-used", 1))
    )


_ZhoneSysCardLineVoltage_Type.__name__ = "Integer32"
_ZhoneSysCardLineVoltage_Object = MibTableColumn
zhoneSysCardLineVoltage = _ZhoneSysCardLineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 10, 1, 11),
    _ZhoneSysCardLineVoltage_Type()
)
zhoneSysCardLineVoltage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneSysCardLineVoltage.setStatus("current")


class _ZhoneSysCardVpiVciRange_Type(Integer32):
    """Custom type zhoneSysCardVpiVciRange based on Integer32"""
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
        *(("not-applicable", 1),
          ("vpi-15-vci-127", 4),
          ("vpi-15-vci-63", 2),
          ("vpi-7-vci-127", 3))
    )


_ZhoneSysCardVpiVciRange_Type.__name__ = "Integer32"
_ZhoneSysCardVpiVciRange_Object = MibTableColumn
zhoneSysCardVpiVciRange = _ZhoneSysCardVpiVciRange_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 10, 1, 12),
    _ZhoneSysCardVpiVciRange_Type()
)
zhoneSysCardVpiVciRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneSysCardVpiVciRange.setStatus("current")


class _ZhoneSysCardInitString_Type(OctetString):
    """Custom type zhoneSysCardInitString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ZhoneSysCardInitString_Type.__name__ = "OctetString"
_ZhoneSysCardInitString_Object = MibTableColumn
zhoneSysCardInitString = _ZhoneSysCardInitString_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 10, 1, 13),
    _ZhoneSysCardInitString_Type()
)
zhoneSysCardInitString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneSysCardInitString.setStatus("current")


class _ZhoneSysCardWettingCurrent_Type(Integer32):
    """Custom type zhoneSysCardWettingCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("standard", 2))
    )


_ZhoneSysCardWettingCurrent_Type.__name__ = "Integer32"
_ZhoneSysCardWettingCurrent_Object = MibTableColumn
zhoneSysCardWettingCurrent = _ZhoneSysCardWettingCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 10, 1, 14),
    _ZhoneSysCardWettingCurrent_Type()
)
zhoneSysCardWettingCurrent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneSysCardWettingCurrent.setStatus("current")
_ZhoneCardRedundancy_ObjectIdentity = ObjectIdentity
zhoneCardRedundancy = _ZhoneCardRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 11)
)
_NextCardRedundancyGroupId_Type = Integer32
_NextCardRedundancyGroupId_Object = MibScalar
nextCardRedundancyGroupId = _NextCardRedundancyGroupId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 11, 1),
    _NextCardRedundancyGroupId_Type()
)
nextCardRedundancyGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextCardRedundancyGroupId.setStatus("current")
_ZhoneSysCardRedundancyTable_Object = MibTable
zhoneSysCardRedundancyTable = _ZhoneSysCardRedundancyTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 11, 2)
)
if mibBuilder.loadTexts:
    zhoneSysCardRedundancyTable.setStatus("current")
_ZhoneSysCardRedundancyEntry_Object = MibTableRow
zhoneSysCardRedundancyEntry = _ZhoneSysCardRedundancyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 11, 2, 1)
)
zhoneSysCardRedundancyEntry.setIndexNames(
    (0, "ZHONE-SYSTEM-MIB", "zhoneSysCardRedundancyGroupId"),
    (0, "Zhone", "zhoneShelfIndex"),
    (0, "Zhone", "zhoneSlotIndex"),
)
if mibBuilder.loadTexts:
    zhoneSysCardRedundancyEntry.setStatus("current")


class _ZhoneSysCardRedundancyGroupId_Type(Integer32):
    """Custom type zhoneSysCardRedundancyGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneSysCardRedundancyGroupId_Type.__name__ = "Integer32"
_ZhoneSysCardRedundancyGroupId_Object = MibTableColumn
zhoneSysCardRedundancyGroupId = _ZhoneSysCardRedundancyGroupId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 11, 2, 1, 1),
    _ZhoneSysCardRedundancyGroupId_Type()
)
zhoneSysCardRedundancyGroupId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneSysCardRedundancyGroupId.setStatus("current")


class _ZhoneSysCardRedundancyWeight_Type(ZhoneRedundancyWeight):
    """Custom type zhoneSysCardRedundancyWeight based on ZhoneRedundancyWeight"""


_ZhoneSysCardRedundancyWeight_Object = MibTableColumn
zhoneSysCardRedundancyWeight = _ZhoneSysCardRedundancyWeight_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 11, 2, 1, 2),
    _ZhoneSysCardRedundancyWeight_Type()
)
zhoneSysCardRedundancyWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneSysCardRedundancyWeight.setStatus("current")


class _ZhoneSysCardRedundancyHoldActive_Type(TruthValue):
    """Custom type zhoneSysCardRedundancyHoldActive based on TruthValue"""


_ZhoneSysCardRedundancyHoldActive_Object = MibTableColumn
zhoneSysCardRedundancyHoldActive = _ZhoneSysCardRedundancyHoldActive_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 11, 2, 1, 3),
    _ZhoneSysCardRedundancyHoldActive_Type()
)
zhoneSysCardRedundancyHoldActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneSysCardRedundancyHoldActive.setStatus("current")


class _ZhoneSysCardRedundancyOperStatus_Type(Integer32):
    """Custom type zhoneSysCardRedundancyOperStatus based on Integer32"""
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
        *(("cardIsActive", 2),
          ("cardIsNotRedundant", 4),
          ("cardIsStandby", 3),
          ("cardIsStandbyWithActiveLinks", 5),
          ("noStatus", 1))
    )


_ZhoneSysCardRedundancyOperStatus_Type.__name__ = "Integer32"
_ZhoneSysCardRedundancyOperStatus_Object = MibTableColumn
zhoneSysCardRedundancyOperStatus = _ZhoneSysCardRedundancyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 11, 2, 1, 4),
    _ZhoneSysCardRedundancyOperStatus_Type()
)
zhoneSysCardRedundancyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSysCardRedundancyOperStatus.setStatus("current")
_ZhoneSysCardRedundancyRowStatus_Type = ZhoneRowStatus
_ZhoneSysCardRedundancyRowStatus_Object = MibTableColumn
zhoneSysCardRedundancyRowStatus = _ZhoneSysCardRedundancyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 11, 2, 1, 5),
    _ZhoneSysCardRedundancyRowStatus_Type()
)
zhoneSysCardRedundancyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneSysCardRedundancyRowStatus.setStatus("current")
_ZhoneSntpConfiguration_ObjectIdentity = ObjectIdentity
zhoneSntpConfiguration = _ZhoneSntpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 12)
)
if mibBuilder.loadTexts:
    zhoneSntpConfiguration.setStatus("current")
_ZhoneSntpPrimaryServerIpAddr_Type = IpAddress
_ZhoneSntpPrimaryServerIpAddr_Object = MibScalar
zhoneSntpPrimaryServerIpAddr = _ZhoneSntpPrimaryServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 12, 1),
    _ZhoneSntpPrimaryServerIpAddr_Type()
)
zhoneSntpPrimaryServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSntpPrimaryServerIpAddr.setStatus("current")
_ZhoneSntpSecondaryServerIpAddr_Type = IpAddress
_ZhoneSntpSecondaryServerIpAddr_Object = MibScalar
zhoneSntpSecondaryServerIpAddr = _ZhoneSntpSecondaryServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 12, 2),
    _ZhoneSntpSecondaryServerIpAddr_Type()
)
zhoneSntpSecondaryServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSntpSecondaryServerIpAddr.setStatus("current")


class _ZhoneSntpLocalTimeZone_Type(ZhoneLocalTimeZone):
    """Custom type zhoneSntpLocalTimeZone based on ZhoneLocalTimeZone"""
    defaultValue = 14


_ZhoneSntpLocalTimeZone_Object = MibScalar
zhoneSntpLocalTimeZone = _ZhoneSntpLocalTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 12, 3),
    _ZhoneSntpLocalTimeZone_Type()
)
zhoneSntpLocalTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSntpLocalTimeZone.setStatus("current")


class _ZhoneSntpDaylightSavingTime_Type(TruthValue):
    """Custom type zhoneSntpDaylightSavingTime based on TruthValue"""


_ZhoneSntpDaylightSavingTime_Object = MibScalar
zhoneSntpDaylightSavingTime = _ZhoneSntpDaylightSavingTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 12, 4),
    _ZhoneSntpDaylightSavingTime_Type()
)
zhoneSntpDaylightSavingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSntpDaylightSavingTime.setStatus("current")


class _ZhoneSntpDaylightSavingStart_Type(OctetString):
    """Custom type zhoneSntpDaylightSavingStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_ZhoneSntpDaylightSavingStart_Type.__name__ = "OctetString"
_ZhoneSntpDaylightSavingStart_Object = MibScalar
zhoneSntpDaylightSavingStart = _ZhoneSntpDaylightSavingStart_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 12, 5),
    _ZhoneSntpDaylightSavingStart_Type()
)
zhoneSntpDaylightSavingStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSntpDaylightSavingStart.setStatus("current")
if mibBuilder.loadTexts:
    zhoneSntpDaylightSavingStart.setUnits("characters")


class _ZhoneSntpDaylightSavingEnd_Type(OctetString):
    """Custom type zhoneSntpDaylightSavingEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_ZhoneSntpDaylightSavingEnd_Type.__name__ = "OctetString"
_ZhoneSntpDaylightSavingEnd_Object = MibScalar
zhoneSntpDaylightSavingEnd = _ZhoneSntpDaylightSavingEnd_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 12, 6),
    _ZhoneSntpDaylightSavingEnd_Type()
)
zhoneSntpDaylightSavingEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSntpDaylightSavingEnd.setStatus("current")
if mibBuilder.loadTexts:
    zhoneSntpDaylightSavingEnd.setUnits("characters")
_ZhoneAdslPotsBypassRelay_ObjectIdentity = ObjectIdentity
zhoneAdslPotsBypassRelay = _ZhoneAdslPotsBypassRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 13)
)
if mibBuilder.loadTexts:
    zhoneAdslPotsBypassRelay.setStatus("current")


class _ZhoneAdslPotsMaxActiveBypassRelays_Type(Integer32):
    """Custom type zhoneAdslPotsMaxActiveBypassRelays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ZhoneAdslPotsMaxActiveBypassRelays_Type.__name__ = "Integer32"
_ZhoneAdslPotsMaxActiveBypassRelays_Object = MibScalar
zhoneAdslPotsMaxActiveBypassRelays = _ZhoneAdslPotsMaxActiveBypassRelays_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 13, 1),
    _ZhoneAdslPotsMaxActiveBypassRelays_Type()
)
zhoneAdslPotsMaxActiveBypassRelays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAdslPotsMaxActiveBypassRelays.setStatus("current")


class _ZhoneAdslPotsBypassRelayResetAll_Type(Integer32):
    """Custom type zhoneAdslPotsBypassRelayResetAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 2),
          ("unchanged", 1))
    )


_ZhoneAdslPotsBypassRelayResetAll_Type.__name__ = "Integer32"
_ZhoneAdslPotsBypassRelayResetAll_Object = MibScalar
zhoneAdslPotsBypassRelayResetAll = _ZhoneAdslPotsBypassRelayResetAll_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 13, 2),
    _ZhoneAdslPotsBypassRelayResetAll_Type()
)
zhoneAdslPotsBypassRelayResetAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneAdslPotsBypassRelayResetAll.setStatus("current")
_ZhoneBulkStatsSystemConfiguration_ObjectIdentity = ObjectIdentity
zhoneBulkStatsSystemConfiguration = _ZhoneBulkStatsSystemConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 14)
)
if mibBuilder.loadTexts:
    zhoneBulkStatsSystemConfiguration.setStatus("current")


class _ZhoneBulkStatsSystemCollectionEnabled_Type(TruthValue):
    """Custom type zhoneBulkStatsSystemCollectionEnabled based on TruthValue"""


_ZhoneBulkStatsSystemCollectionEnabled_Object = MibScalar
zhoneBulkStatsSystemCollectionEnabled = _ZhoneBulkStatsSystemCollectionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 14, 1),
    _ZhoneBulkStatsSystemCollectionEnabled_Type()
)
zhoneBulkStatsSystemCollectionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneBulkStatsSystemCollectionEnabled.setStatus("current")
_ZhoneBulkStatsSystemFtpAddress_Type = IpAddress
_ZhoneBulkStatsSystemFtpAddress_Object = MibScalar
zhoneBulkStatsSystemFtpAddress = _ZhoneBulkStatsSystemFtpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 14, 2),
    _ZhoneBulkStatsSystemFtpAddress_Type()
)
zhoneBulkStatsSystemFtpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneBulkStatsSystemFtpAddress.setStatus("current")
_ZhoneBulkStatsSystemFtpLogin_Type = ZhoneAdminString
_ZhoneBulkStatsSystemFtpLogin_Object = MibScalar
zhoneBulkStatsSystemFtpLogin = _ZhoneBulkStatsSystemFtpLogin_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 14, 3),
    _ZhoneBulkStatsSystemFtpLogin_Type()
)
zhoneBulkStatsSystemFtpLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneBulkStatsSystemFtpLogin.setStatus("current")
_ZhoneBulkStatsSystemFtpPassword_Type = ZhoneAdminString
_ZhoneBulkStatsSystemFtpPassword_Object = MibScalar
zhoneBulkStatsSystemFtpPassword = _ZhoneBulkStatsSystemFtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 14, 4),
    _ZhoneBulkStatsSystemFtpPassword_Type()
)
zhoneBulkStatsSystemFtpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneBulkStatsSystemFtpPassword.setStatus("current")
_ZhoneBulkStatsSystemFtpDirPath_Type = ZhoneFileName
_ZhoneBulkStatsSystemFtpDirPath_Object = MibScalar
zhoneBulkStatsSystemFtpDirPath = _ZhoneBulkStatsSystemFtpDirPath_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 14, 5),
    _ZhoneBulkStatsSystemFtpDirPath_Type()
)
zhoneBulkStatsSystemFtpDirPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneBulkStatsSystemFtpDirPath.setStatus("current")


class _ZhoneBulkStatsSystemOperStatus_Type(Integer32):
    """Custom type zhoneBulkStatsSystemOperStatus based on Integer32"""
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
        *(("collectionAbortedFileIoFailure", 5),
          ("collectionAbortedNoDiskSpace", 4),
          ("collectionComplete", 2),
          ("collectionCompleteFtpFailure", 6),
          ("collectionInProgress", 1),
          ("collectionPeriodOverrun", 3))
    )


_ZhoneBulkStatsSystemOperStatus_Type.__name__ = "Integer32"
_ZhoneBulkStatsSystemOperStatus_Object = MibScalar
zhoneBulkStatsSystemOperStatus = _ZhoneBulkStatsSystemOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 14, 6),
    _ZhoneBulkStatsSystemOperStatus_Type()
)
zhoneBulkStatsSystemOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneBulkStatsSystemOperStatus.setStatus("current")
_ZhoneBulkStatCollection_ObjectIdentity = ObjectIdentity
zhoneBulkStatCollection = _ZhoneBulkStatCollection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 15)
)
_NextBulkStatCollectionId_Type = Integer32
_NextBulkStatCollectionId_Object = MibScalar
nextBulkStatCollectionId = _NextBulkStatCollectionId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 15, 1),
    _NextBulkStatCollectionId_Type()
)
nextBulkStatCollectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextBulkStatCollectionId.setStatus("current")
_ZhoneBulkStatCollectionTable_Object = MibTable
zhoneBulkStatCollectionTable = _ZhoneBulkStatCollectionTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 15, 2)
)
if mibBuilder.loadTexts:
    zhoneBulkStatCollectionTable.setStatus("current")
_ZhoneBulkStatCollectionEntry_Object = MibTableRow
zhoneBulkStatCollectionEntry = _ZhoneBulkStatCollectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 15, 2, 1)
)
zhoneBulkStatCollectionEntry.setIndexNames(
    (0, "ZHONE-SYSTEM-MIB", "zhoneBulkStatCollectionId"),
)
if mibBuilder.loadTexts:
    zhoneBulkStatCollectionEntry.setStatus("current")


class _ZhoneBulkStatCollectionId_Type(Integer32):
    """Custom type zhoneBulkStatCollectionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_ZhoneBulkStatCollectionId_Type.__name__ = "Integer32"
_ZhoneBulkStatCollectionId_Object = MibTableColumn
zhoneBulkStatCollectionId = _ZhoneBulkStatCollectionId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 15, 2, 1, 1),
    _ZhoneBulkStatCollectionId_Type()
)
zhoneBulkStatCollectionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneBulkStatCollectionId.setStatus("current")


class _ZhoneBulkStatEnabled_Type(TruthValue):
    """Custom type zhoneBulkStatEnabled based on TruthValue"""


_ZhoneBulkStatEnabled_Object = MibTableColumn
zhoneBulkStatEnabled = _ZhoneBulkStatEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 15, 2, 1, 2),
    _ZhoneBulkStatEnabled_Type()
)
zhoneBulkStatEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneBulkStatEnabled.setStatus("current")
_ZhoneBulkStatOID_Type = OctetString
_ZhoneBulkStatOID_Object = MibTableColumn
zhoneBulkStatOID = _ZhoneBulkStatOID_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 15, 2, 1, 3),
    _ZhoneBulkStatOID_Type()
)
zhoneBulkStatOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneBulkStatOID.setStatus("current")
_ZhoneBulkStatInstance_Type = ZhoneAdminString
_ZhoneBulkStatInstance_Object = MibTableColumn
zhoneBulkStatInstance = _ZhoneBulkStatInstance_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 15, 2, 1, 4),
    _ZhoneBulkStatInstance_Type()
)
zhoneBulkStatInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneBulkStatInstance.setStatus("current")


class _ZhoneBulkStatIncludeChildren_Type(TruthValue):
    """Custom type zhoneBulkStatIncludeChildren based on TruthValue"""


_ZhoneBulkStatIncludeChildren_Object = MibTableColumn
zhoneBulkStatIncludeChildren = _ZhoneBulkStatIncludeChildren_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 15, 2, 1, 5),
    _ZhoneBulkStatIncludeChildren_Type()
)
zhoneBulkStatIncludeChildren.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneBulkStatIncludeChildren.setStatus("current")


class _ZhoneBulkStatsCollectionInterval_Type(Integer32):
    """Custom type zhoneBulkStatsCollectionInterval based on Integer32"""
    defaultValue = 15


_ZhoneBulkStatsCollectionInterval_Object = MibTableColumn
zhoneBulkStatsCollectionInterval = _ZhoneBulkStatsCollectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 15, 2, 1, 6),
    _ZhoneBulkStatsCollectionInterval_Type()
)
zhoneBulkStatsCollectionInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneBulkStatsCollectionInterval.setStatus("current")
_ZhoneBulkStatCollectionRowStatus_Type = ZhoneRowStatus
_ZhoneBulkStatCollectionRowStatus_Object = MibTableColumn
zhoneBulkStatCollectionRowStatus = _ZhoneBulkStatCollectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 15, 2, 1, 7),
    _ZhoneBulkStatCollectionRowStatus_Type()
)
zhoneBulkStatCollectionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneBulkStatCollectionRowStatus.setStatus("current")
_ZhoneVideoSystemConfiguration_ObjectIdentity = ObjectIdentity
zhoneVideoSystemConfiguration = _ZhoneVideoSystemConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 16)
)
if mibBuilder.loadTexts:
    zhoneVideoSystemConfiguration.setStatus("current")


class _ZhoneVideoSystemConfigurationIndexNext_Type(Integer32):
    """Custom type zhoneVideoSystemConfigurationIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZhoneVideoSystemConfigurationIndexNext_Type.__name__ = "Integer32"
_ZhoneVideoSystemConfigurationIndexNext_Object = MibScalar
zhoneVideoSystemConfigurationIndexNext = _ZhoneVideoSystemConfigurationIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 16, 1),
    _ZhoneVideoSystemConfigurationIndexNext_Type()
)
zhoneVideoSystemConfigurationIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVideoSystemConfigurationIndexNext.setStatus("current")
_ZhoneVideoSystemConfigurationTable_Object = MibTable
zhoneVideoSystemConfigurationTable = _ZhoneVideoSystemConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 16, 2)
)
if mibBuilder.loadTexts:
    zhoneVideoSystemConfigurationTable.setStatus("current")
_ZhoneVideoSystemConfigurationEntry_Object = MibTableRow
zhoneVideoSystemConfigurationEntry = _ZhoneVideoSystemConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 16, 2, 1)
)
zhoneVideoSystemConfigurationEntry.setIndexNames(
    (0, "ZHONE-SYSTEM-MIB", "zhoneVideoSystemConfigurationIndex"),
)
if mibBuilder.loadTexts:
    zhoneVideoSystemConfigurationEntry.setStatus("current")


class _ZhoneVideoSystemConfigurationIndex_Type(Integer32):
    """Custom type zhoneVideoSystemConfigurationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZhoneVideoSystemConfigurationIndex_Type.__name__ = "Integer32"
_ZhoneVideoSystemConfigurationIndex_Object = MibTableColumn
zhoneVideoSystemConfigurationIndex = _ZhoneVideoSystemConfigurationIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 16, 2, 1, 1),
    _ZhoneVideoSystemConfigurationIndex_Type()
)
zhoneVideoSystemConfigurationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneVideoSystemConfigurationIndex.setStatus("current")
_ZhoneVideoSystemConfigurationNtpServerAddress_Type = IpAddress
_ZhoneVideoSystemConfigurationNtpServerAddress_Object = MibTableColumn
zhoneVideoSystemConfigurationNtpServerAddress = _ZhoneVideoSystemConfigurationNtpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 16, 2, 1, 2),
    _ZhoneVideoSystemConfigurationNtpServerAddress_Type()
)
zhoneVideoSystemConfigurationNtpServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVideoSystemConfigurationNtpServerAddress.setStatus("current")
_ZhoneVideoSystemConfigurationEpgServerAddress_Type = IpAddress
_ZhoneVideoSystemConfigurationEpgServerAddress_Object = MibTableColumn
zhoneVideoSystemConfigurationEpgServerAddress = _ZhoneVideoSystemConfigurationEpgServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 16, 2, 1, 3),
    _ZhoneVideoSystemConfigurationEpgServerAddress_Type()
)
zhoneVideoSystemConfigurationEpgServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVideoSystemConfigurationEpgServerAddress.setStatus("current")
_ZhoneVideoSystemConfigurationSettopBoxHeadEndServerAddress_Type = IpAddress
_ZhoneVideoSystemConfigurationSettopBoxHeadEndServerAddress_Object = MibTableColumn
zhoneVideoSystemConfigurationSettopBoxHeadEndServerAddress = _ZhoneVideoSystemConfigurationSettopBoxHeadEndServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 16, 2, 1, 4),
    _ZhoneVideoSystemConfigurationSettopBoxHeadEndServerAddress_Type()
)
zhoneVideoSystemConfigurationSettopBoxHeadEndServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVideoSystemConfigurationSettopBoxHeadEndServerAddress.setStatus("current")
_ZhoneVideoSystemConfigurationDefaultChannelAddress_Type = IpAddress
_ZhoneVideoSystemConfigurationDefaultChannelAddress_Object = MibTableColumn
zhoneVideoSystemConfigurationDefaultChannelAddress = _ZhoneVideoSystemConfigurationDefaultChannelAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 16, 2, 1, 5),
    _ZhoneVideoSystemConfigurationDefaultChannelAddress_Type()
)
zhoneVideoSystemConfigurationDefaultChannelAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVideoSystemConfigurationDefaultChannelAddress.setStatus("current")
_ZhoneVideoSystemConfigurationNoChannelAvailableAddress_Type = IpAddress
_ZhoneVideoSystemConfigurationNoChannelAvailableAddress_Object = MibTableColumn
zhoneVideoSystemConfigurationNoChannelAvailableAddress = _ZhoneVideoSystemConfigurationNoChannelAvailableAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 16, 2, 1, 6),
    _ZhoneVideoSystemConfigurationNoChannelAvailableAddress_Type()
)
zhoneVideoSystemConfigurationNoChannelAvailableAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVideoSystemConfigurationNoChannelAvailableAddress.setStatus("current")
_ZhoneVideoSystemConfigurationRowStatus_Type = ZhoneRowStatus
_ZhoneVideoSystemConfigurationRowStatus_Object = MibTableColumn
zhoneVideoSystemConfigurationRowStatus = _ZhoneVideoSystemConfigurationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 16, 2, 1, 7),
    _ZhoneVideoSystemConfigurationRowStatus_Type()
)
zhoneVideoSystemConfigurationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVideoSystemConfigurationRowStatus.setStatus("current")


class _ZhoneVideoSystemConfigurationEpgType_Type(Integer32):
    """Custom type zhoneVideoSystemConfigurationEpgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("minerva", 1),
          ("myrio", 2))
    )


_ZhoneVideoSystemConfigurationEpgType_Type.__name__ = "Integer32"
_ZhoneVideoSystemConfigurationEpgType_Object = MibTableColumn
zhoneVideoSystemConfigurationEpgType = _ZhoneVideoSystemConfigurationEpgType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 16, 2, 1, 8),
    _ZhoneVideoSystemConfigurationEpgType_Type()
)
zhoneVideoSystemConfigurationEpgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVideoSystemConfigurationEpgType.setStatus("current")
_ZhoneVideoSystemConfigurationEpgPort_Type = Unsigned32
_ZhoneVideoSystemConfigurationEpgPort_Object = MibTableColumn
zhoneVideoSystemConfigurationEpgPort = _ZhoneVideoSystemConfigurationEpgPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 16, 2, 1, 9),
    _ZhoneVideoSystemConfigurationEpgPort_Type()
)
zhoneVideoSystemConfigurationEpgPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVideoSystemConfigurationEpgPort.setStatus("current")
_ZhoneVideoSystemConfigurationEpgFtpAddress_Type = IpAddress
_ZhoneVideoSystemConfigurationEpgFtpAddress_Object = MibTableColumn
zhoneVideoSystemConfigurationEpgFtpAddress = _ZhoneVideoSystemConfigurationEpgFtpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 16, 2, 1, 10),
    _ZhoneVideoSystemConfigurationEpgFtpAddress_Type()
)
zhoneVideoSystemConfigurationEpgFtpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVideoSystemConfigurationEpgFtpAddress.setStatus("current")
_ZhoneCallDetailRecConfig_ObjectIdentity = ObjectIdentity
zhoneCallDetailRecConfig = _ZhoneCallDetailRecConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 17)
)
if mibBuilder.loadTexts:
    zhoneCallDetailRecConfig.setStatus("current")


class _ZhoneCallDetailRecEnabled_Type(TruthValue):
    """Custom type zhoneCallDetailRecEnabled based on TruthValue"""


_ZhoneCallDetailRecEnabled_Object = MibScalar
zhoneCallDetailRecEnabled = _ZhoneCallDetailRecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 17, 1),
    _ZhoneCallDetailRecEnabled_Type()
)
zhoneCallDetailRecEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCallDetailRecEnabled.setStatus("current")


class _ZhoneCallDetailRecFlushLog_Type(TruthValue):
    """Custom type zhoneCallDetailRecFlushLog based on TruthValue"""


_ZhoneCallDetailRecFlushLog_Object = MibScalar
zhoneCallDetailRecFlushLog = _ZhoneCallDetailRecFlushLog_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 17, 2),
    _ZhoneCallDetailRecFlushLog_Type()
)
zhoneCallDetailRecFlushLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCallDetailRecFlushLog.setStatus("current")


class _ZhoneCallDetailRecCurrFtpServer_Type(Integer32):
    """Custom type zhoneCallDetailRecCurrFtpServer based on Integer32"""
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
        *(("none", 3),
          ("primary", 1),
          ("secondary", 2))
    )


_ZhoneCallDetailRecCurrFtpServer_Type.__name__ = "Integer32"
_ZhoneCallDetailRecCurrFtpServer_Object = MibScalar
zhoneCallDetailRecCurrFtpServer = _ZhoneCallDetailRecCurrFtpServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 17, 3),
    _ZhoneCallDetailRecCurrFtpServer_Type()
)
zhoneCallDetailRecCurrFtpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCallDetailRecCurrFtpServer.setStatus("current")
_ZhoneCallDetailRecPrimFtpIpAddr_Type = IpAddress
_ZhoneCallDetailRecPrimFtpIpAddr_Object = MibScalar
zhoneCallDetailRecPrimFtpIpAddr = _ZhoneCallDetailRecPrimFtpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 17, 4),
    _ZhoneCallDetailRecPrimFtpIpAddr_Type()
)
zhoneCallDetailRecPrimFtpIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCallDetailRecPrimFtpIpAddr.setStatus("current")
_ZhoneCallDetailRecSecFtpIpAddr_Type = IpAddress
_ZhoneCallDetailRecSecFtpIpAddr_Object = MibScalar
zhoneCallDetailRecSecFtpIpAddr = _ZhoneCallDetailRecSecFtpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 17, 5),
    _ZhoneCallDetailRecSecFtpIpAddr_Type()
)
zhoneCallDetailRecSecFtpIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCallDetailRecSecFtpIpAddr.setStatus("current")
_ZhoneCallDetailRecFtpLogin_Type = ZhoneAdminString
_ZhoneCallDetailRecFtpLogin_Object = MibScalar
zhoneCallDetailRecFtpLogin = _ZhoneCallDetailRecFtpLogin_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 17, 6),
    _ZhoneCallDetailRecFtpLogin_Type()
)
zhoneCallDetailRecFtpLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCallDetailRecFtpLogin.setStatus("current")
_ZhoneCallDetailRecFtpPassword_Type = ZhoneAdminString
_ZhoneCallDetailRecFtpPassword_Object = MibScalar
zhoneCallDetailRecFtpPassword = _ZhoneCallDetailRecFtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 17, 7),
    _ZhoneCallDetailRecFtpPassword_Type()
)
zhoneCallDetailRecFtpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCallDetailRecFtpPassword.setStatus("current")
_ZhoneCallDetailRecFtpDirPath_Type = ZhoneFileName
_ZhoneCallDetailRecFtpDirPath_Object = MibScalar
zhoneCallDetailRecFtpDirPath = _ZhoneCallDetailRecFtpDirPath_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 17, 8),
    _ZhoneCallDetailRecFtpDirPath_Type()
)
zhoneCallDetailRecFtpDirPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCallDetailRecFtpDirPath.setStatus("current")


class _ZhoneCallDetailRecRepPeriod_Type(Integer32):
    """Custom type zhoneCallDetailRecRepPeriod based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_ZhoneCallDetailRecRepPeriod_Type.__name__ = "Integer32"
_ZhoneCallDetailRecRepPeriod_Object = MibScalar
zhoneCallDetailRecRepPeriod = _ZhoneCallDetailRecRepPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 17, 9),
    _ZhoneCallDetailRecRepPeriod_Type()
)
zhoneCallDetailRecRepPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCallDetailRecRepPeriod.setStatus("current")


class _ZhoneCallDetailRecOperStatus_Type(Integer32):
    """Custom type zhoneCallDetailRecOperStatus based on Integer32"""
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
        *(("active", 1),
          ("ftpFailure", 2),
          ("noConfig", 4),
          ("overrun", 3))
    )


_ZhoneCallDetailRecOperStatus_Type.__name__ = "Integer32"
_ZhoneCallDetailRecOperStatus_Object = MibScalar
zhoneCallDetailRecOperStatus = _ZhoneCallDetailRecOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 17, 10),
    _ZhoneCallDetailRecOperStatus_Type()
)
zhoneCallDetailRecOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCallDetailRecOperStatus.setStatus("current")
_ZhoneSoftwareUpgrade_ObjectIdentity = ObjectIdentity
zhoneSoftwareUpgrade = _ZhoneSoftwareUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 19)
)
if mibBuilder.loadTexts:
    zhoneSoftwareUpgrade.setStatus("current")


class _ZhoneSoftwareUpgradeAction_Type(Integer32):
    """Custom type zhoneSoftwareUpgradeAction based on Integer32"""
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
        *(("sw-upgrade", 1),
          ("sw-upgrade-auto-swact", 2),
          ("swact", 3),
          ("swact-abort", 4))
    )


_ZhoneSoftwareUpgradeAction_Type.__name__ = "Integer32"
_ZhoneSoftwareUpgradeAction_Object = MibScalar
zhoneSoftwareUpgradeAction = _ZhoneSoftwareUpgradeAction_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 19, 1),
    _ZhoneSoftwareUpgradeAction_Type()
)
zhoneSoftwareUpgradeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSoftwareUpgradeAction.setStatus("current")


class _ZhoneSoftwareUpgradeStatus_Type(Integer32):
    """Custom type zhoneSoftwareUpgradeStatus based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("not-started", 1),
          ("standby-upgrade-aborted", 4),
          ("standby-upgrade-completed", 3),
          ("standby-upgrade-started", 2),
          ("swact-aborted", 7),
          ("swact-complete", 6),
          ("swact-started", 5))
    )


_ZhoneSoftwareUpgradeStatus_Type.__name__ = "Integer32"
_ZhoneSoftwareUpgradeStatus_Object = MibScalar
zhoneSoftwareUpgradeStatus = _ZhoneSoftwareUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 19, 2),
    _ZhoneSoftwareUpgradeStatus_Type()
)
zhoneSoftwareUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSoftwareUpgradeStatus.setStatus("current")
_ZhoneSoftwareUpgradeTimeStarted_Type = DateAndTime
_ZhoneSoftwareUpgradeTimeStarted_Object = MibScalar
zhoneSoftwareUpgradeTimeStarted = _ZhoneSoftwareUpgradeTimeStarted_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 19, 3),
    _ZhoneSoftwareUpgradeTimeStarted_Type()
)
zhoneSoftwareUpgradeTimeStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSoftwareUpgradeTimeStarted.setStatus("current")
_ZhoneSoftwareUpgradeTimeCompleted_Type = DateAndTime
_ZhoneSoftwareUpgradeTimeCompleted_Object = MibScalar
zhoneSoftwareUpgradeTimeCompleted = _ZhoneSoftwareUpgradeTimeCompleted_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 19, 4),
    _ZhoneSoftwareUpgradeTimeCompleted_Type()
)
zhoneSoftwareUpgradeTimeCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSoftwareUpgradeTimeCompleted.setStatus("current")
_ZhoneFileSystem_ObjectIdentity = ObjectIdentity
zhoneFileSystem = _ZhoneFileSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 20)
)
if mibBuilder.loadTexts:
    zhoneFileSystem.setStatus("current")


class _ZhoneFileAction_Type(Integer32):
    """Custom type zhoneFileAction based on Integer32"""
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
        *(("cd", 1),
          ("copy", 3),
          ("dir", 2),
          ("mkdir", 5),
          ("mv", 7),
          ("rm", 4),
          ("rmdir", 6))
    )


_ZhoneFileAction_Type.__name__ = "Integer32"
_ZhoneFileAction_Object = MibScalar
zhoneFileAction = _ZhoneFileAction_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 20, 1),
    _ZhoneFileAction_Type()
)
zhoneFileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneFileAction.setStatus("current")
_ZhoneFileName1_Type = ZhoneFileName
_ZhoneFileName1_Object = MibScalar
zhoneFileName1 = _ZhoneFileName1_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 20, 2),
    _ZhoneFileName1_Type()
)
zhoneFileName1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneFileName1.setStatus("current")
_ZhoneFileName2_Type = ZhoneFileName
_ZhoneFileName2_Object = MibScalar
zhoneFileName2 = _ZhoneFileName2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 20, 3),
    _ZhoneFileName2_Type()
)
zhoneFileName2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneFileName2.setStatus("current")
_ZhoneDirectoryPath_Type = ZhoneFileName
_ZhoneDirectoryPath_Object = MibScalar
zhoneDirectoryPath = _ZhoneDirectoryPath_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 20, 4),
    _ZhoneDirectoryPath_Type()
)
zhoneDirectoryPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneDirectoryPath.setStatus("current")
_ZhoneDirectoryBytesAvailable_Type = Unsigned32
_ZhoneDirectoryBytesAvailable_Object = MibScalar
zhoneDirectoryBytesAvailable = _ZhoneDirectoryBytesAvailable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 20, 5),
    _ZhoneDirectoryBytesAvailable_Type()
)
zhoneDirectoryBytesAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDirectoryBytesAvailable.setStatus("current")
_ZhoneBytesReservedForProvisioning_Type = Unsigned32
_ZhoneBytesReservedForProvisioning_Object = MibScalar
zhoneBytesReservedForProvisioning = _ZhoneBytesReservedForProvisioning_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 20, 6),
    _ZhoneBytesReservedForProvisioning_Type()
)
zhoneBytesReservedForProvisioning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneBytesReservedForProvisioning.setStatus("current")
_ZhoneFileTable_Object = MibTable
zhoneFileTable = _ZhoneFileTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 20, 7)
)
if mibBuilder.loadTexts:
    zhoneFileTable.setStatus("current")
_ZhoneFileEntry_Object = MibTableRow
zhoneFileEntry = _ZhoneFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 20, 7, 1)
)
zhoneFileEntry.setIndexNames(
    (0, "ZHONE-SYSTEM-MIB", "zhoneFileIndex"),
)
if mibBuilder.loadTexts:
    zhoneFileEntry.setStatus("current")


class _ZhoneFileIndex_Type(Integer32):
    """Custom type zhoneFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_ZhoneFileIndex_Type.__name__ = "Integer32"
_ZhoneFileIndex_Object = MibTableColumn
zhoneFileIndex = _ZhoneFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 20, 7, 1, 1),
    _ZhoneFileIndex_Type()
)
zhoneFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneFileIndex.setStatus("current")
_ZhoneFileDirectoryPath_Type = ZhoneFileName
_ZhoneFileDirectoryPath_Object = MibTableColumn
zhoneFileDirectoryPath = _ZhoneFileDirectoryPath_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 20, 7, 1, 2),
    _ZhoneFileDirectoryPath_Type()
)
zhoneFileDirectoryPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFileDirectoryPath.setStatus("current")
_ZhoneFileName_Type = ZhoneFileName
_ZhoneFileName_Object = MibTableColumn
zhoneFileName = _ZhoneFileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 20, 7, 1, 3),
    _ZhoneFileName_Type()
)
zhoneFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFileName.setStatus("current")


class _ZhoneFilePrivilege_Type(OctetString):
    """Custom type zhoneFilePrivilege based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_ZhoneFilePrivilege_Type.__name__ = "OctetString"
_ZhoneFilePrivilege_Object = MibTableColumn
zhoneFilePrivilege = _ZhoneFilePrivilege_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 20, 7, 1, 4),
    _ZhoneFilePrivilege_Type()
)
zhoneFilePrivilege.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFilePrivilege.setStatus("current")
_ZhoneFileSize_Type = Unsigned32
_ZhoneFileSize_Object = MibTableColumn
zhoneFileSize = _ZhoneFileSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 20, 7, 1, 5),
    _ZhoneFileSize_Type()
)
zhoneFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFileSize.setStatus("current")
_ZhoneFileLastModified_Type = DateAndTime
_ZhoneFileLastModified_Object = MibTableColumn
zhoneFileLastModified = _ZhoneFileLastModified_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 20, 7, 1, 6),
    _ZhoneFileLastModified_Type()
)
zhoneFileLastModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFileLastModified.setStatus("current")
_CpeMgr_ObjectIdentity = ObjectIdentity
cpeMgr = _CpeMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 21)
)
if mibBuilder.loadTexts:
    cpeMgr.setStatus("current")
_ZhoneEnhancedStatus_ObjectIdentity = ObjectIdentity
zhoneEnhancedStatus = _ZhoneEnhancedStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 22)
)
if mibBuilder.loadTexts:
    zhoneEnhancedStatus.setStatus("current")
_ZhoneEnhancedStatusTable_Object = MibTable
zhoneEnhancedStatusTable = _ZhoneEnhancedStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 22, 1)
)
if mibBuilder.loadTexts:
    zhoneEnhancedStatusTable.setStatus("current")
_ZhoneEnhancedStatusEntry_Object = MibTableRow
zhoneEnhancedStatusEntry = _ZhoneEnhancedStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 22, 1, 1)
)
zhoneEnhancedStatusEntry.setIndexNames(
    (0, "ZHONE-SYSTEM-MIB", "zhoneEnhancedStatusIndex"),
)
if mibBuilder.loadTexts:
    zhoneEnhancedStatusEntry.setStatus("current")


class _ZhoneEnhancedStatusIndex_Type(Integer32):
    """Custom type zhoneEnhancedStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneEnhancedStatusIndex_Type.__name__ = "Integer32"
_ZhoneEnhancedStatusIndex_Object = MibTableColumn
zhoneEnhancedStatusIndex = _ZhoneEnhancedStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 22, 1, 1, 1),
    _ZhoneEnhancedStatusIndex_Type()
)
zhoneEnhancedStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneEnhancedStatusIndex.setStatus("current")


class _ZhoneEnhancedStatusCode_Type(Integer32):
    """Custom type zhoneEnhancedStatusCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 2147483647),
    )


_ZhoneEnhancedStatusCode_Type.__name__ = "Integer32"
_ZhoneEnhancedStatusCode_Object = MibTableColumn
zhoneEnhancedStatusCode = _ZhoneEnhancedStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 22, 1, 1, 2),
    _ZhoneEnhancedStatusCode_Type()
)
zhoneEnhancedStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEnhancedStatusCode.setStatus("current")


class _ZhoneEnhancedStatusText_Type(OctetString):
    """Custom type zhoneEnhancedStatusText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ZhoneEnhancedStatusText_Type.__name__ = "OctetString"
_ZhoneEnhancedStatusText_Object = MibTableColumn
zhoneEnhancedStatusText = _ZhoneEnhancedStatusText_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 22, 1, 1, 3),
    _ZhoneEnhancedStatusText_Type()
)
zhoneEnhancedStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEnhancedStatusText.setStatus("current")
_ZhoneTrapCpePoll_ObjectIdentity = ObjectIdentity
zhoneTrapCpePoll = _ZhoneTrapCpePoll_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 8, 1)
)
if mibBuilder.loadTexts:
    zhoneTrapCpePoll.setStatus("current")
_ZhoneTrapCpePollV2Traps_ObjectIdentity = ObjectIdentity
zhoneTrapCpePollV2Traps = _ZhoneTrapCpePollV2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 8, 1, 0)
)
if mibBuilder.loadTexts:
    zhoneTrapCpePollV2Traps.setStatus("current")
_ZhoneTrapConfigSync_ObjectIdentity = ObjectIdentity
zhoneTrapConfigSync = _ZhoneTrapConfigSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 8, 2)
)
if mibBuilder.loadTexts:
    zhoneTrapConfigSync.setStatus("current")
_ZhoneTrapConfigSyncV2Traps_ObjectIdentity = ObjectIdentity
zhoneTrapConfigSyncV2Traps = _ZhoneTrapConfigSyncV2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 8, 2, 0)
)
if mibBuilder.loadTexts:
    zhoneTrapConfigSyncV2Traps.setStatus("current")
_ZhoneTrapSnmp_ObjectIdentity = ObjectIdentity
zhoneTrapSnmp = _ZhoneTrapSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 8, 4)
)
if mibBuilder.loadTexts:
    zhoneTrapSnmp.setStatus("current")
_ZhoneTrapSnmpV2Traps_ObjectIdentity = ObjectIdentity
zhoneTrapSnmpV2Traps = _ZhoneTrapSnmpV2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 8, 4, 0)
)
if mibBuilder.loadTexts:
    zhoneTrapSnmpV2Traps.setStatus("current")
_ZhoneTrapCardRedundancy_ObjectIdentity = ObjectIdentity
zhoneTrapCardRedundancy = _ZhoneTrapCardRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 8, 5)
)
if mibBuilder.loadTexts:
    zhoneTrapCardRedundancy.setStatus("current")
_ZhoneCardRedundancyV2Traps_ObjectIdentity = ObjectIdentity
zhoneCardRedundancyV2Traps = _ZhoneCardRedundancyV2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 8, 5, 0)
)
if mibBuilder.loadTexts:
    zhoneCardRedundancyV2Traps.setStatus("current")
_ZhoneTrapBulkStatistics_ObjectIdentity = ObjectIdentity
zhoneTrapBulkStatistics = _ZhoneTrapBulkStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 8, 6)
)
if mibBuilder.loadTexts:
    zhoneTrapBulkStatistics.setStatus("current")
_ZhoneBulkStatisticsV2Traps_ObjectIdentity = ObjectIdentity
zhoneBulkStatisticsV2Traps = _ZhoneBulkStatisticsV2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 8, 6, 0)
)
if mibBuilder.loadTexts:
    zhoneBulkStatisticsV2Traps.setStatus("current")
_ZhoneTrapZms_ObjectIdentity = ObjectIdentity
zhoneTrapZms = _ZhoneTrapZms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 8, 7)
)
if mibBuilder.loadTexts:
    zhoneTrapZms.setStatus("current")
_ZhoneTrapZmsV2Traps_ObjectIdentity = ObjectIdentity
zhoneTrapZmsV2Traps = _ZhoneTrapZmsV2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 8, 7, 0)
)
if mibBuilder.loadTexts:
    zhoneTrapZmsV2Traps.setStatus("current")
_ZhoneCompliances_ObjectIdentity = ObjectIdentity
zhoneCompliances = _ZhoneCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 8)
)
_ZhoneGroups_ObjectIdentity = ObjectIdentity
zhoneGroups = _ZhoneGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 8, 1)
)

# Managed Objects groups

zhoneSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 8, 1, 1)
)
zhoneSystemGroup.setObjects(
      *(("ZHONE-SYSTEM-MIB", "zhoneZmsExists"),
        ("ZHONE-SYSTEM-MIB", "zhoneZmsConnectionStatus"),
        ("ZHONE-SYSTEM-MIB", "zhoneZmsIpAddress"),
        ("ZHONE-SYSTEM-MIB", "zhoneZmsBlockCli"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapsCommunityName"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapsSequenceNumber"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapsResendSequenceNumber"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapsAckedSequenceNumber"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapsSeverity"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapsAllowedCategories"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapsAdminStatus"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapsRowStatus"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapsGatewayTrapServerAddress"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapVersion"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapFlags"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapShelf"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapSlot"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapPort"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapSubPort"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapProviderId"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapText"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapPortType"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapPortTypeExtension"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapAlarmAction"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapAlarmId"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapAlarmSeverity"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapConfigSyncResetInterval"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapConfigSyncResetCount"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapConfigSyncResetLastFtpTime"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapConfigSyncResetCurrentTime"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapUtcTime"),
        ("ZHONE-SYSTEM-MIB", "zhoneConfigSyncExists"),
        ("ZHONE-SYSTEM-MIB", "zhoneConfigSyncOverflow"),
        ("ZHONE-SYSTEM-MIB", "zhoneConfigSyncPriority"),
        ("ZHONE-SYSTEM-MIB", "zhoneConfigSyncAction"),
        ("ZHONE-SYSTEM-MIB", "zhoneConfigSyncFileName"),
        ("ZHONE-SYSTEM-MIB", "zhoneConfigSyncStatus"),
        ("ZHONE-SYSTEM-MIB", "zhoneConfigSyncUserName"),
        ("ZHONE-SYSTEM-MIB", "zhoneConfigSyncUserPassword"),
        ("ZHONE-SYSTEM-MIB", "zhoneAdminCommunityAccess"),
        ("ZHONE-SYSTEM-MIB", "zhoneAdminCommunityAccessListIndex"),
        ("ZHONE-SYSTEM-MIB", "zhoneAdminCommunityRowStatus"),
        ("ZHONE-SYSTEM-MIB", "zhoneNextAdminAccessIndex"),
        ("ZHONE-SYSTEM-MIB", "zhoneSwCardSwFileName"),
        ("ZHONE-SYSTEM-MIB", "zhoneSwLoadRowStatus"),
        ("ZHONE-SYSTEM-MIB", "zhoneSnmpErrorDisplayString"),
        ("ZHONE-SYSTEM-MIB", "zhoneSnmpErrorTime"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysSwLogin"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysSwPassword"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysSwPriLoadServer"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysSwSecLoadServer"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysSwRemoteFilePath"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysSwLocalFilePath"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysSwAdmin"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysSwStatus"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysRebootAdmin"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysRebootCardType"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysCardSpecificSwFileName"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysCardSwSpecificVers"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysCardUpgradeSwFileName"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysCardSwUpgradeVers"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysCardSwType"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysCardSwEnable"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysCardSwUpgradeEnable"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysCardRowStatus"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysCardLineType"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysCardAtmConfiguration"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysCardLineVoltage"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysCardVpiVciRange"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysCardInitString"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysCardWettingCurrent"),
        ("ZHONE-SYSTEM-MIB", "nextCardRedundancyGroupId"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysCardRedundancyGroupId"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysCardRedundancyWeight"),
        ("ZHONE-SYSTEM-MIB", "zhoneBulkStatCollectionRowStatus"),
        ("ZHONE-SYSTEM-MIB", "zhoneVideoSystemConfigurationRowStatus"),
        ("ZHONE-SYSTEM-MIB", "zhoneBulkStatInstance"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysCardRedundancyHoldActive"),
        ("ZHONE-SYSTEM-MIB", "zhoneAdminAccessRowStatus"),
        ("ZHONE-SYSTEM-MIB", "zhoneUserIdNext"),
        ("ZHONE-SYSTEM-MIB", "zhoneUserTotalFailedLogins"),
        ("ZHONE-SYSTEM-MIB", "zhoneUserName"),
        ("ZHONE-SYSTEM-MIB", "zhoneUserPassword"),
        ("ZHONE-SYSTEM-MIB", "zhoneUserPrompt"),
        ("ZHONE-SYSTEM-MIB", "zhoneUserAccessLevel"),
        ("ZHONE-SYSTEM-MIB", "zhoneUserAdmin"),
        ("ZHONE-SYSTEM-MIB", "zhoneUserLogins"),
        ("ZHONE-SYSTEM-MIB", "zhoneUserFailedLogins"),
        ("ZHONE-SYSTEM-MIB", "zhoneUserRowStatus"),
        ("ZHONE-SYSTEM-MIB", "zhoneSystemConfigurationNumShelves"),
        ("ZHONE-SYSTEM-MIB", "zhoneSystemConfigurationShelvesArray"),
        ("ZHONE-SYSTEM-MIB", "zhoneSystemConfigurationNumCards"),
        ("ZHONE-SYSTEM-MIB", "zhoneSystemConfigurationIpAddress"),
        ("ZHONE-SYSTEM-MIB", "zhoneSystemConfigurationAlternateIpAddress"),
        ("ZHONE-SYSTEM-MIB", "zhoneSystemConfigurationDateAndTime"),
        ("ZHONE-SYSTEM-MIB", "zhoneSystemConfigurationCountryRegion"),
        ("ZHONE-SYSTEM-MIB", "zhoneSystemConfigurationRingSource"),
        ("ZHONE-SYSTEM-MIB", "zhoneSystemCurrentClockSource"),
        ("ZHONE-SYSTEM-MIB", "zhoneSystemSecondaryClockSource"),
        ("ZHONE-SYSTEM-MIB", "zhoneSystemClockEligibility"),
        ("ZHONE-SYSTEM-MIB", "zhoneSystemClockWeight"),
        ("ZHONE-SYSTEM-MIB", "zhoneSystemClockAvailabilityStatus"),
        ("ZHONE-SYSTEM-MIB", "zhoneSystemClockTxClockMode"),
        ("ZHONE-SYSTEM-MIB", "zhoneSystemConsoleLogging"),
        ("ZHONE-SYSTEM-MIB", "zhoneSystemRevertiveClockSource"),
        ("ZHONE-SYSTEM-MIB", "zhoneSystemVoiceBandwidthCheck"),
        ("ZHONE-SYSTEM-MIB", "zhoneAlarmLevelsEnabled"),
        ("ZHONE-SYSTEM-MIB", "zhoneSystemUserAuthMethod"),
        ("ZHONE-SYSTEM-MIB", "zhoneSystemRadiusAuthIndex"),
        ("ZHONE-SYSTEM-MIB", "zhoneSystemSecureFTP"),
        ("ZHONE-SYSTEM-MIB", "zhoneSystemWebInterface"),
        ("ZHONE-SYSTEM-MIB", "zhoneSystemConfigurationOptions"),
        ("ZHONE-SYSTEM-MIB", "zhoneSystemConfigurationReservedVlanIdStart"),
        ("ZHONE-SYSTEM-MIB", "zhoneSystemConfigurationReservedVlanIdCount"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysCardRedundancyOperStatus"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysCardRedundancyRowStatus"),
        ("ZHONE-SYSTEM-MIB", "zhoneSntpPrimaryServerIpAddr"),
        ("ZHONE-SYSTEM-MIB", "zhoneSntpSecondaryServerIpAddr"),
        ("ZHONE-SYSTEM-MIB", "zhoneSntpLocalTimeZone"),
        ("ZHONE-SYSTEM-MIB", "zhoneSntpDaylightSavingTime"),
        ("ZHONE-SYSTEM-MIB", "zhoneAdslPotsMaxActiveBypassRelays"),
        ("ZHONE-SYSTEM-MIB", "zhoneAdslPotsBypassRelayResetAll"),
        ("ZHONE-SYSTEM-MIB", "zhoneBulkStatsSystemCollectionEnabled"),
        ("ZHONE-SYSTEM-MIB", "zhoneBulkStatsSystemFtpAddress"),
        ("ZHONE-SYSTEM-MIB", "zhoneBulkStatsSystemFtpLogin"),
        ("ZHONE-SYSTEM-MIB", "zhoneBulkStatsSystemFtpPassword"),
        ("ZHONE-SYSTEM-MIB", "zhoneBulkStatsSystemFtpDirPath"),
        ("ZHONE-SYSTEM-MIB", "zhoneBulkStatsSystemOperStatus"),
        ("ZHONE-SYSTEM-MIB", "nextBulkStatCollectionId"),
        ("ZHONE-SYSTEM-MIB", "zhoneBulkStatEnabled"),
        ("ZHONE-SYSTEM-MIB", "zhoneBulkStatOID"),
        ("ZHONE-SYSTEM-MIB", "zhoneBulkStatIncludeChildren"),
        ("ZHONE-SYSTEM-MIB", "zhoneBulkStatsCollectionInterval"),
        ("ZHONE-SYSTEM-MIB", "zhoneVideoSystemConfigurationIndexNext"),
        ("ZHONE-SYSTEM-MIB", "zhoneVideoSystemConfigurationNtpServerAddress"),
        ("ZHONE-SYSTEM-MIB", "zhoneVideoSystemConfigurationEpgServerAddress"),
        ("ZHONE-SYSTEM-MIB", "zhoneVideoSystemConfigurationSettopBoxHeadEndServerAddress"),
        ("ZHONE-SYSTEM-MIB", "zhoneVideoSystemConfigurationDefaultChannelAddress"),
        ("ZHONE-SYSTEM-MIB", "zhoneVideoSystemConfigurationNoChannelAvailableAddress"),
        ("ZHONE-SYSTEM-MIB", "zhoneVideoSystemConfigurationEpgType"),
        ("ZHONE-SYSTEM-MIB", "zhoneVideoSystemConfigurationEpgPort"),
        ("ZHONE-SYSTEM-MIB", "zhoneVideoSystemConfigurationEpgFtpAddress"),
        ("ZHONE-SYSTEM-MIB", "zhoneCallDetailRecEnabled"),
        ("ZHONE-SYSTEM-MIB", "zhoneCallDetailRecFlushLog"),
        ("ZHONE-SYSTEM-MIB", "zhoneCallDetailRecCurrFtpServer"),
        ("ZHONE-SYSTEM-MIB", "zhoneCallDetailRecPrimFtpIpAddr"),
        ("ZHONE-SYSTEM-MIB", "zhoneCallDetailRecSecFtpIpAddr"),
        ("ZHONE-SYSTEM-MIB", "zhoneCallDetailRecFtpLogin"),
        ("ZHONE-SYSTEM-MIB", "zhoneCallDetailRecFtpPassword"),
        ("ZHONE-SYSTEM-MIB", "zhoneCallDetailRecFtpDirPath"),
        ("ZHONE-SYSTEM-MIB", "zhoneCallDetailRecRepPeriod"),
        ("ZHONE-SYSTEM-MIB", "zhoneCallDetailRecOperStatus"),
        ("ZHONE-SYSTEM-MIB", "zhoneSoftwareUpgradeAction"),
        ("ZHONE-SYSTEM-MIB", "zhoneSoftwareUpgradeStatus"),
        ("ZHONE-SYSTEM-MIB", "zhoneSoftwareUpgradeTimeStarted"),
        ("ZHONE-SYSTEM-MIB", "zhoneSoftwareUpgradeTimeCompleted"),
        ("ZHONE-SYSTEM-MIB", "zhoneFileAction"),
        ("ZHONE-SYSTEM-MIB", "zhoneFileName1"),
        ("ZHONE-SYSTEM-MIB", "zhoneFileName2"),
        ("ZHONE-SYSTEM-MIB", "zhoneDirectoryPath"),
        ("ZHONE-SYSTEM-MIB", "zhoneDirectoryBytesAvailable"),
        ("ZHONE-SYSTEM-MIB", "zhoneBytesReservedForProvisioning"),
        ("ZHONE-SYSTEM-MIB", "zhoneFileDirectoryPath"),
        ("ZHONE-SYSTEM-MIB", "zhoneFileName"),
        ("ZHONE-SYSTEM-MIB", "zhoneFilePrivilege"),
        ("ZHONE-SYSTEM-MIB", "zhoneFileSize"),
        ("ZHONE-SYSTEM-MIB", "zhoneFileLastModified"),
        ("ZHONE-SYSTEM-MIB", "zhoneEnhancedStatusCode"),
        ("ZHONE-SYSTEM-MIB", "zhoneEnhancedStatusText"))
)
if mibBuilder.loadTexts:
    zhoneSystemGroup.setStatus("current")

zhoneDeprecatedSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 8, 1, 2)
)
zhoneDeprecatedSystemGroup.setObjects(
    ("ZHONE-SYSTEM-MIB", "zhonePrimaryClockSource")
)
if mibBuilder.loadTexts:
    zhoneDeprecatedSystemGroup.setStatus("deprecated")


# Notification objects

zhoneTrapCpeConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 8, 1, 0, 1)
)
zhoneTrapCpeConnectionDown.setObjects(
      *(("ZHONE-INTERFACE-TRANSLATION-MIB", "zhoneShelfNumber"),
        ("ZHONE-INTERFACE-TRANSLATION-MIB", "zhoneSlotNumber"),
        ("ZHONE-INTERFACE-TRANSLATION-MIB", "pportNumber"),
        ("ZHONE-INTERFACE-TRANSLATION-MIB", "subPortNumber"),
        ("ZHONE-COM-IP-REC-MIB", "ipIfVpi"),
        ("ZHONE-COM-IP-REC-MIB", "ipIfVci"),
        ("ZHONE-COM-IP-REC-MIB", "ipIfLgId"),
        ("ZHONE-COM-IP-REC-MIB", "ipIfAddr"))
)
if mibBuilder.loadTexts:
    zhoneTrapCpeConnectionDown.setStatus(
        "current"
    )

zhoneTrapCpeConnectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 8, 1, 0, 2)
)
zhoneTrapCpeConnectionUp.setObjects(
      *(("ZHONE-INTERFACE-TRANSLATION-MIB", "zhoneShelfNumber"),
        ("ZHONE-INTERFACE-TRANSLATION-MIB", "zhoneSlotNumber"),
        ("ZHONE-INTERFACE-TRANSLATION-MIB", "pportNumber"),
        ("ZHONE-INTERFACE-TRANSLATION-MIB", "subPortNumber"),
        ("ZHONE-COM-IP-REC-MIB", "ipIfVpi"),
        ("ZHONE-COM-IP-REC-MIB", "ipIfVci"),
        ("ZHONE-COM-IP-REC-MIB", "ipIfLgId"),
        ("ZHONE-COM-IP-REC-MIB", "ipIfAddr"))
)
if mibBuilder.loadTexts:
    zhoneTrapCpeConnectionUp.setStatus(
        "current"
    )

zhoneTrapConfigSyncChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 8, 2, 0, 1)
)
zhoneTrapConfigSyncChange.setObjects(
      *(("ZHONE-SYSTEM-MIB", "zhoneConfigSyncAction"),
        ("ZHONE-SYSTEM-MIB", "zhoneConfigSyncPriority"))
)
if mibBuilder.loadTexts:
    zhoneTrapConfigSyncChange.setStatus(
        "current"
    )

zhoneTrapConfigSyncReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 8, 2, 0, 2)
)
zhoneTrapConfigSyncReset.setObjects(
      *(("ZHONE-SYSTEM-MIB", "zhoneTrapConfigSyncResetInterval"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapConfigSyncResetCount"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapConfigSyncResetLastFtpTime"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapConfigSyncResetCurrentTime"))
)
if mibBuilder.loadTexts:
    zhoneTrapConfigSyncReset.setStatus(
        "current"
    )

zhoneTrapSnmpSATimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 8, 4, 0, 1)
)
if mibBuilder.loadTexts:
    zhoneTrapSnmpSATimeout.setStatus(
        "current"
    )

zhoneCardRedundancyStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 8, 5, 0, 1)
)
zhoneCardRedundancyStatusChange.setObjects(
      *(("ZHONE-INTERFACE-TRANSLATION-MIB", "zhoneShelfNumber"),
        ("ZHONE-INTERFACE-TRANSLATION-MIB", "zhoneSlotNumber"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysCardRedundancyGroupId"))
)
if mibBuilder.loadTexts:
    zhoneCardRedundancyStatusChange.setStatus(
        "current"
    )

zhoneCardRedundancyUnsafe = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 8, 5, 0, 2)
)
zhoneCardRedundancyUnsafe.setObjects(
    ("ZHONE-SYSTEM-MIB", "zhoneSysCardRedundancyOperStatus")
)
if mibBuilder.loadTexts:
    zhoneCardRedundancyUnsafe.setStatus(
        "current"
    )

zhoneBulkStatisticsIntervalFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 8, 6, 0, 1)
)
zhoneBulkStatisticsIntervalFailure.setObjects(
    ("ZHONE-SYSTEM-MIB", "zhoneBulkStatsSystemOperStatus")
)
if mibBuilder.loadTexts:
    zhoneBulkStatisticsIntervalFailure.setStatus(
        "current"
    )

zhoneZmsBlockCliChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 8, 7, 0, 1)
)
zhoneZmsBlockCliChange.setObjects(
    ("ZHONE-SYSTEM-MIB", "zhoneZmsBlockCli")
)
if mibBuilder.loadTexts:
    zhoneZmsBlockCliChange.setStatus(
        "deprecated"
    )


# Notifications groups

zhoneTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5504, 8, 1, 3)
)
zhoneTrapGroup.setObjects(
      *(("ZHONE-SYSTEM-MIB", "zhoneTrapCpeConnectionDown"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapCpeConnectionUp"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapConfigSyncChange"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapConfigSyncReset"),
        ("ZHONE-SYSTEM-MIB", "zhoneTrapSnmpSATimeout"),
        ("ZHONE-SYSTEM-MIB", "zhoneCardRedundancyStatusChange"),
        ("ZHONE-SYSTEM-MIB", "zhoneCardRedundancyUnsafe"),
        ("ZHONE-SYSTEM-MIB", "zhoneBulkStatisticsIntervalFailure"))
)
if mibBuilder.loadTexts:
    zhoneTrapGroup.setStatus(
        "current"
    )

zhoneDeprecatedTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5504, 8, 1, 4)
)
zhoneDeprecatedTrapGroup.setObjects(
    ("ZHONE-SYSTEM-MIB", "zhoneZmsBlockCliChange")
)
if mibBuilder.loadTexts:
    zhoneDeprecatedTrapGroup.setStatus(
        "deprecated"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-SYSTEM-MIB",
    **{"ZhoneRedundancyWeight": ZhoneRedundancyWeight,
       "ZhoneLocalTimeZone": ZhoneLocalTimeZone,
       "zhoneZms": zhoneZms,
       "zhoneZmsExists": zhoneZmsExists,
       "zhoneZmsConnectionStatus": zhoneZmsConnectionStatus,
       "zhoneZmsIpAddress": zhoneZmsIpAddress,
       "zhoneZmsBlockCli": zhoneZmsBlockCli,
       "zhoneTraps": zhoneTraps,
       "zhoneTrapsTable": zhoneTrapsTable,
       "zhoneTrapsEntry": zhoneTrapsEntry,
       "zhoneTrapsDestination": zhoneTrapsDestination,
       "zhoneTrapsCommunityName": zhoneTrapsCommunityName,
       "zhoneTrapsSequenceNumber": zhoneTrapsSequenceNumber,
       "zhoneTrapsResendSequenceNumber": zhoneTrapsResendSequenceNumber,
       "zhoneTrapsAckedSequenceNumber": zhoneTrapsAckedSequenceNumber,
       "zhoneTrapsSeverity": zhoneTrapsSeverity,
       "zhoneTrapsAllowedCategories": zhoneTrapsAllowedCategories,
       "zhoneTrapsAdminStatus": zhoneTrapsAdminStatus,
       "zhoneTrapsRowStatus": zhoneTrapsRowStatus,
       "zhoneTrapsGatewayTrapServerAddress": zhoneTrapsGatewayTrapServerAddress,
       "zhoneTrapVersion": zhoneTrapVersion,
       "zhoneTrapFlags": zhoneTrapFlags,
       "zhoneTrapShelf": zhoneTrapShelf,
       "zhoneTrapSlot": zhoneTrapSlot,
       "zhoneTrapPort": zhoneTrapPort,
       "zhoneTrapSubPort": zhoneTrapSubPort,
       "zhoneTrapProviderId": zhoneTrapProviderId,
       "zhoneTrapText": zhoneTrapText,
       "zhoneTrapPortType": zhoneTrapPortType,
       "zhoneTrapPortTypeExtension": zhoneTrapPortTypeExtension,
       "zhoneTrapAlarmAction": zhoneTrapAlarmAction,
       "zhoneTrapAlarmId": zhoneTrapAlarmId,
       "zhoneTrapAlarmSeverity": zhoneTrapAlarmSeverity,
       "zhoneTrapConfigSyncResetInterval": zhoneTrapConfigSyncResetInterval,
       "zhoneTrapConfigSyncResetCount": zhoneTrapConfigSyncResetCount,
       "zhoneTrapConfigSyncResetLastFtpTime": zhoneTrapConfigSyncResetLastFtpTime,
       "zhoneTrapConfigSyncResetCurrentTime": zhoneTrapConfigSyncResetCurrentTime,
       "zhoneTrapUtcTime": zhoneTrapUtcTime,
       "zhoneConfigSync": zhoneConfigSync,
       "zhoneConfigSyncExists": zhoneConfigSyncExists,
       "zhoneConfigSyncOverflow": zhoneConfigSyncOverflow,
       "zhoneConfigSyncPriority": zhoneConfigSyncPriority,
       "zhoneConfigSyncAction": zhoneConfigSyncAction,
       "zhoneConfigSyncFileName": zhoneConfigSyncFileName,
       "zhoneConfigSyncStatus": zhoneConfigSyncStatus,
       "zhoneConfigSyncUserName": zhoneConfigSyncUserName,
       "zhoneConfigSyncUserPassword": zhoneConfigSyncUserPassword,
       "zhoneAdmin": zhoneAdmin,
       "zhoneAdminCommunityTable": zhoneAdminCommunityTable,
       "zhoneAdminCommunityEntry": zhoneAdminCommunityEntry,
       "zhoneAdminCommunityName": zhoneAdminCommunityName,
       "zhoneAdminCommunityAccess": zhoneAdminCommunityAccess,
       "zhoneAdminCommunityAccessListIndex": zhoneAdminCommunityAccessListIndex,
       "zhoneAdminCommunityRowStatus": zhoneAdminCommunityRowStatus,
       "zhoneNextAdminAccessIndex": zhoneNextAdminAccessIndex,
       "zhoneAdminAccessListTable": zhoneAdminAccessListTable,
       "zhoneAdminAccessListEntry": zhoneAdminAccessListEntry,
       "zhoneAdminAccessListIndex": zhoneAdminAccessListIndex,
       "zhoneAdminAccessListIpAddress": zhoneAdminAccessListIpAddress,
       "zhoneAdminAccessRowStatus": zhoneAdminAccessRowStatus,
       "zhoneUser": zhoneUser,
       "zhoneUserIdNext": zhoneUserIdNext,
       "zhoneUserTotalFailedLogins": zhoneUserTotalFailedLogins,
       "zhoneUserTable": zhoneUserTable,
       "zhoneUserEntry": zhoneUserEntry,
       "zhoneUserId": zhoneUserId,
       "zhoneUserName": zhoneUserName,
       "zhoneUserPassword": zhoneUserPassword,
       "zhoneUserPrompt": zhoneUserPrompt,
       "zhoneUserAccessLevel": zhoneUserAccessLevel,
       "zhoneUserAdmin": zhoneUserAdmin,
       "zhoneUserLogins": zhoneUserLogins,
       "zhoneUserFailedLogins": zhoneUserFailedLogins,
       "zhoneUserRowStatus": zhoneUserRowStatus,
       "zhoneSystemConfiguration": zhoneSystemConfiguration,
       "zhoneSystemConfigurationNumShelves": zhoneSystemConfigurationNumShelves,
       "zhoneSystemConfigurationShelvesArray": zhoneSystemConfigurationShelvesArray,
       "zhoneSystemConfigurationNumCards": zhoneSystemConfigurationNumCards,
       "zhoneSystemConfigurationIpAddress": zhoneSystemConfigurationIpAddress,
       "zhoneSystemConfigurationAlternateIpAddress": zhoneSystemConfigurationAlternateIpAddress,
       "zhoneSystemConfigurationDateAndTime": zhoneSystemConfigurationDateAndTime,
       "zhoneSystemConfigurationCountryRegion": zhoneSystemConfigurationCountryRegion,
       "zhonePrimaryClockSource": zhonePrimaryClockSource,
       "zhoneSystemConfigurationRingSource": zhoneSystemConfigurationRingSource,
       "zhoneSystemCurrentClockSource": zhoneSystemCurrentClockSource,
       "zhoneSystemSecondaryClockSource": zhoneSystemSecondaryClockSource,
       "zhoneSystemClockTable": zhoneSystemClockTable,
       "zhoneSystemClockEntry": zhoneSystemClockEntry,
       "zhoneSystemClockEligibility": zhoneSystemClockEligibility,
       "zhoneSystemClockWeight": zhoneSystemClockWeight,
       "zhoneSystemClockAvailabilityStatus": zhoneSystemClockAvailabilityStatus,
       "zhoneSystemClockTxClockMode": zhoneSystemClockTxClockMode,
       "zhoneSystemConsoleLogging": zhoneSystemConsoleLogging,
       "zhoneSystemRevertiveClockSource": zhoneSystemRevertiveClockSource,
       "zhoneSystemVoiceBandwidthCheck": zhoneSystemVoiceBandwidthCheck,
       "zhoneAlarmLevelsEnabled": zhoneAlarmLevelsEnabled,
       "zhoneSystemUserAuthMethod": zhoneSystemUserAuthMethod,
       "zhoneSystemRadiusAuthIndex": zhoneSystemRadiusAuthIndex,
       "zhoneSystemSecureFTP": zhoneSystemSecureFTP,
       "zhoneSystemWebInterface": zhoneSystemWebInterface,
       "zhoneSystemConfigurationOptions": zhoneSystemConfigurationOptions,
       "zhoneSystemConfigurationReservedVlanIdStart": zhoneSystemConfigurationReservedVlanIdStart,
       "zhoneSystemConfigurationReservedVlanIdCount": zhoneSystemConfigurationReservedVlanIdCount,
       "zhoneSystemSnmpVersion": zhoneSystemSnmpVersion,
       "zhoneSystemPersistentLogging": zhoneSystemPersistentLogging,
       "zhoneSystemOutletTemperatureHighThreshold": zhoneSystemOutletTemperatureHighThreshold,
       "zhoneSystemOutletTemperatureLowThreshold": zhoneSystemOutletTemperatureLowThreshold,
       "zhoneSoftwareLoadTable": zhoneSoftwareLoadTable,
       "zhoneSoftwareLoadEntry": zhoneSoftwareLoadEntry,
       "zhoneSwCardType": zhoneSwCardType,
       "zhoneSwCardSwFileName": zhoneSwCardSwFileName,
       "zhoneSwLoadRowStatus": zhoneSwLoadRowStatus,
       "zhoneSnmpErrorTable": zhoneSnmpErrorTable,
       "zhoneSnmpErrorEntry": zhoneSnmpErrorEntry,
       "zhoneSnmpErrorIpAddress": zhoneSnmpErrorIpAddress,
       "zhoneSnmpErrorReqId": zhoneSnmpErrorReqId,
       "zhoneSnmpErrorDisplayString": zhoneSnmpErrorDisplayString,
       "zhoneSnmpErrorTime": zhoneSnmpErrorTime,
       "zhoneSoftwareDownload": zhoneSoftwareDownload,
       "zhoneSysSwLogin": zhoneSysSwLogin,
       "zhoneSysSwPassword": zhoneSysSwPassword,
       "zhoneSysSwPriLoadServer": zhoneSysSwPriLoadServer,
       "zhoneSysSwSecLoadServer": zhoneSysSwSecLoadServer,
       "zhoneSysSwRemoteFilePath": zhoneSysSwRemoteFilePath,
       "zhoneSysSwLocalFilePath": zhoneSysSwLocalFilePath,
       "zhoneSysSwAdmin": zhoneSysSwAdmin,
       "zhoneSysSwStatus": zhoneSysSwStatus,
       "zhoneSoftwareReboot": zhoneSoftwareReboot,
       "zhoneSysRebootAdmin": zhoneSysRebootAdmin,
       "zhoneSysRebootCardType": zhoneSysRebootCardType,
       "zhoneSysCardSoftwareConfigTable": zhoneSysCardSoftwareConfigTable,
       "zhoneSysCardSoftwareConfigEntry": zhoneSysCardSoftwareConfigEntry,
       "zhoneSysCardSpecificSwFileName": zhoneSysCardSpecificSwFileName,
       "zhoneSysCardSwSpecificVers": zhoneSysCardSwSpecificVers,
       "zhoneSysCardUpgradeSwFileName": zhoneSysCardUpgradeSwFileName,
       "zhoneSysCardSwUpgradeVers": zhoneSysCardSwUpgradeVers,
       "zhoneSysCardSwType": zhoneSysCardSwType,
       "zhoneSysCardSwEnable": zhoneSysCardSwEnable,
       "zhoneSysCardSwUpgradeEnable": zhoneSysCardSwUpgradeEnable,
       "zhoneSysCardRowStatus": zhoneSysCardRowStatus,
       "zhoneSysCardLineType": zhoneSysCardLineType,
       "zhoneSysCardAtmConfiguration": zhoneSysCardAtmConfiguration,
       "zhoneSysCardLineVoltage": zhoneSysCardLineVoltage,
       "zhoneSysCardVpiVciRange": zhoneSysCardVpiVciRange,
       "zhoneSysCardInitString": zhoneSysCardInitString,
       "zhoneSysCardWettingCurrent": zhoneSysCardWettingCurrent,
       "zhoneCardRedundancy": zhoneCardRedundancy,
       "nextCardRedundancyGroupId": nextCardRedundancyGroupId,
       "zhoneSysCardRedundancyTable": zhoneSysCardRedundancyTable,
       "zhoneSysCardRedundancyEntry": zhoneSysCardRedundancyEntry,
       "zhoneSysCardRedundancyGroupId": zhoneSysCardRedundancyGroupId,
       "zhoneSysCardRedundancyWeight": zhoneSysCardRedundancyWeight,
       "zhoneSysCardRedundancyHoldActive": zhoneSysCardRedundancyHoldActive,
       "zhoneSysCardRedundancyOperStatus": zhoneSysCardRedundancyOperStatus,
       "zhoneSysCardRedundancyRowStatus": zhoneSysCardRedundancyRowStatus,
       "zhoneSntpConfiguration": zhoneSntpConfiguration,
       "zhoneSntpPrimaryServerIpAddr": zhoneSntpPrimaryServerIpAddr,
       "zhoneSntpSecondaryServerIpAddr": zhoneSntpSecondaryServerIpAddr,
       "zhoneSntpLocalTimeZone": zhoneSntpLocalTimeZone,
       "zhoneSntpDaylightSavingTime": zhoneSntpDaylightSavingTime,
       "zhoneSntpDaylightSavingStart": zhoneSntpDaylightSavingStart,
       "zhoneSntpDaylightSavingEnd": zhoneSntpDaylightSavingEnd,
       "zhoneAdslPotsBypassRelay": zhoneAdslPotsBypassRelay,
       "zhoneAdslPotsMaxActiveBypassRelays": zhoneAdslPotsMaxActiveBypassRelays,
       "zhoneAdslPotsBypassRelayResetAll": zhoneAdslPotsBypassRelayResetAll,
       "zhoneBulkStatsSystemConfiguration": zhoneBulkStatsSystemConfiguration,
       "zhoneBulkStatsSystemCollectionEnabled": zhoneBulkStatsSystemCollectionEnabled,
       "zhoneBulkStatsSystemFtpAddress": zhoneBulkStatsSystemFtpAddress,
       "zhoneBulkStatsSystemFtpLogin": zhoneBulkStatsSystemFtpLogin,
       "zhoneBulkStatsSystemFtpPassword": zhoneBulkStatsSystemFtpPassword,
       "zhoneBulkStatsSystemFtpDirPath": zhoneBulkStatsSystemFtpDirPath,
       "zhoneBulkStatsSystemOperStatus": zhoneBulkStatsSystemOperStatus,
       "zhoneBulkStatCollection": zhoneBulkStatCollection,
       "nextBulkStatCollectionId": nextBulkStatCollectionId,
       "zhoneBulkStatCollectionTable": zhoneBulkStatCollectionTable,
       "zhoneBulkStatCollectionEntry": zhoneBulkStatCollectionEntry,
       "zhoneBulkStatCollectionId": zhoneBulkStatCollectionId,
       "zhoneBulkStatEnabled": zhoneBulkStatEnabled,
       "zhoneBulkStatOID": zhoneBulkStatOID,
       "zhoneBulkStatInstance": zhoneBulkStatInstance,
       "zhoneBulkStatIncludeChildren": zhoneBulkStatIncludeChildren,
       "zhoneBulkStatsCollectionInterval": zhoneBulkStatsCollectionInterval,
       "zhoneBulkStatCollectionRowStatus": zhoneBulkStatCollectionRowStatus,
       "zhoneVideoSystemConfiguration": zhoneVideoSystemConfiguration,
       "zhoneVideoSystemConfigurationIndexNext": zhoneVideoSystemConfigurationIndexNext,
       "zhoneVideoSystemConfigurationTable": zhoneVideoSystemConfigurationTable,
       "zhoneVideoSystemConfigurationEntry": zhoneVideoSystemConfigurationEntry,
       "zhoneVideoSystemConfigurationIndex": zhoneVideoSystemConfigurationIndex,
       "zhoneVideoSystemConfigurationNtpServerAddress": zhoneVideoSystemConfigurationNtpServerAddress,
       "zhoneVideoSystemConfigurationEpgServerAddress": zhoneVideoSystemConfigurationEpgServerAddress,
       "zhoneVideoSystemConfigurationSettopBoxHeadEndServerAddress": zhoneVideoSystemConfigurationSettopBoxHeadEndServerAddress,
       "zhoneVideoSystemConfigurationDefaultChannelAddress": zhoneVideoSystemConfigurationDefaultChannelAddress,
       "zhoneVideoSystemConfigurationNoChannelAvailableAddress": zhoneVideoSystemConfigurationNoChannelAvailableAddress,
       "zhoneVideoSystemConfigurationRowStatus": zhoneVideoSystemConfigurationRowStatus,
       "zhoneVideoSystemConfigurationEpgType": zhoneVideoSystemConfigurationEpgType,
       "zhoneVideoSystemConfigurationEpgPort": zhoneVideoSystemConfigurationEpgPort,
       "zhoneVideoSystemConfigurationEpgFtpAddress": zhoneVideoSystemConfigurationEpgFtpAddress,
       "zhoneCallDetailRecConfig": zhoneCallDetailRecConfig,
       "zhoneCallDetailRecEnabled": zhoneCallDetailRecEnabled,
       "zhoneCallDetailRecFlushLog": zhoneCallDetailRecFlushLog,
       "zhoneCallDetailRecCurrFtpServer": zhoneCallDetailRecCurrFtpServer,
       "zhoneCallDetailRecPrimFtpIpAddr": zhoneCallDetailRecPrimFtpIpAddr,
       "zhoneCallDetailRecSecFtpIpAddr": zhoneCallDetailRecSecFtpIpAddr,
       "zhoneCallDetailRecFtpLogin": zhoneCallDetailRecFtpLogin,
       "zhoneCallDetailRecFtpPassword": zhoneCallDetailRecFtpPassword,
       "zhoneCallDetailRecFtpDirPath": zhoneCallDetailRecFtpDirPath,
       "zhoneCallDetailRecRepPeriod": zhoneCallDetailRecRepPeriod,
       "zhoneCallDetailRecOperStatus": zhoneCallDetailRecOperStatus,
       "zhoneSoftwareUpgrade": zhoneSoftwareUpgrade,
       "zhoneSoftwareUpgradeAction": zhoneSoftwareUpgradeAction,
       "zhoneSoftwareUpgradeStatus": zhoneSoftwareUpgradeStatus,
       "zhoneSoftwareUpgradeTimeStarted": zhoneSoftwareUpgradeTimeStarted,
       "zhoneSoftwareUpgradeTimeCompleted": zhoneSoftwareUpgradeTimeCompleted,
       "zhoneFileSystem": zhoneFileSystem,
       "zhoneFileAction": zhoneFileAction,
       "zhoneFileName1": zhoneFileName1,
       "zhoneFileName2": zhoneFileName2,
       "zhoneDirectoryPath": zhoneDirectoryPath,
       "zhoneDirectoryBytesAvailable": zhoneDirectoryBytesAvailable,
       "zhoneBytesReservedForProvisioning": zhoneBytesReservedForProvisioning,
       "zhoneFileTable": zhoneFileTable,
       "zhoneFileEntry": zhoneFileEntry,
       "zhoneFileIndex": zhoneFileIndex,
       "zhoneFileDirectoryPath": zhoneFileDirectoryPath,
       "zhoneFileName": zhoneFileName,
       "zhoneFilePrivilege": zhoneFilePrivilege,
       "zhoneFileSize": zhoneFileSize,
       "zhoneFileLastModified": zhoneFileLastModified,
       "cpeMgr": cpeMgr,
       "zhoneEnhancedStatus": zhoneEnhancedStatus,
       "zhoneEnhancedStatusTable": zhoneEnhancedStatusTable,
       "zhoneEnhancedStatusEntry": zhoneEnhancedStatusEntry,
       "zhoneEnhancedStatusIndex": zhoneEnhancedStatusIndex,
       "zhoneEnhancedStatusCode": zhoneEnhancedStatusCode,
       "zhoneEnhancedStatusText": zhoneEnhancedStatusText,
       "zhoneTrapCpePoll": zhoneTrapCpePoll,
       "zhoneTrapCpePollV2Traps": zhoneTrapCpePollV2Traps,
       "zhoneTrapCpeConnectionDown": zhoneTrapCpeConnectionDown,
       "zhoneTrapCpeConnectionUp": zhoneTrapCpeConnectionUp,
       "zhoneTrapConfigSync": zhoneTrapConfigSync,
       "zhoneTrapConfigSyncV2Traps": zhoneTrapConfigSyncV2Traps,
       "zhoneTrapConfigSyncChange": zhoneTrapConfigSyncChange,
       "zhoneTrapConfigSyncReset": zhoneTrapConfigSyncReset,
       "zhoneTrapSnmp": zhoneTrapSnmp,
       "zhoneTrapSnmpV2Traps": zhoneTrapSnmpV2Traps,
       "zhoneTrapSnmpSATimeout": zhoneTrapSnmpSATimeout,
       "zhoneTrapCardRedundancy": zhoneTrapCardRedundancy,
       "zhoneCardRedundancyV2Traps": zhoneCardRedundancyV2Traps,
       "zhoneCardRedundancyStatusChange": zhoneCardRedundancyStatusChange,
       "zhoneCardRedundancyUnsafe": zhoneCardRedundancyUnsafe,
       "zhoneTrapBulkStatistics": zhoneTrapBulkStatistics,
       "zhoneBulkStatisticsV2Traps": zhoneBulkStatisticsV2Traps,
       "zhoneBulkStatisticsIntervalFailure": zhoneBulkStatisticsIntervalFailure,
       "zhoneTrapZms": zhoneTrapZms,
       "zhoneTrapZmsV2Traps": zhoneTrapZmsV2Traps,
       "zhoneZmsBlockCliChange": zhoneZmsBlockCliChange,
       "zhoneSystemModule": zhoneSystemModule,
       "zhoneCompliances": zhoneCompliances,
       "zhoneGroups": zhoneGroups,
       "zhoneSystemGroup": zhoneSystemGroup,
       "zhoneDeprecatedSystemGroup": zhoneDeprecatedSystemGroup,
       "zhoneTrapGroup": zhoneTrapGroup,
       "zhoneDeprecatedTrapGroup": zhoneDeprecatedTrapGroup}
)
