# SNMP MIB module (SYMBOL-CC-WS2000-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYMBOL-CC-WS2000-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:36 2024
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
 Bits,
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
 PhysAddress,
 TextualConvention,
 TestAndIncr,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TestAndIncr",
    "TruthValue")


# MODULE-IDENTITY

moduleid = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 1)
)
moduleid.setRevisions(
        ("2010-04-24 09:37",
         "2009-12-30 13:25",
         "2004-12-10 16:49",
         "2004-10-28 16:32",
         "2004-09-08 12:07",
         "2004-02-04 15:32",
         "2004-01-06 00:00",
         "2003-12-11 01:00",
         "2003-12-11 00:00",
         "2003-12-02 00:00",
         "2003-11-26 00:00",
         "2003-11-25 00:00")
)


# Types definitions



class SinglePointer(Integer32):
    """Custom type SinglePointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class MultiPointer63(Bits):
    """Custom type MultiPointer63 based on Bits"""




class MultiPointer255(Bits):
    """Custom type MultiPointer255 based on Bits"""




class DoActionNow(Integer32):
    """Custom type DoActionNow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doActionRightNow", 1),
          ("idleState", 2))
    )





class RadioType(Integer32):
    """Custom type RadioType based on Integer32"""
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
        *(("radio802dot11A", 1),
          ("radio802dot11B", 2),
          ("radio802dot11FH", 4),
          ("radio802dot11G", 3))
    )





class Password(OctetString):
    """Custom type Password based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )





class StaticRowEnable(Integer32):
    """Custom type StaticRowEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )





class PartsPer10k(Unsigned32):
    """Custom type PartsPer10k based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )





class ScaleBy100(Unsigned32):
    """Custom type ScaleBy100 based on Unsigned32"""




class AbbrevRowStatus(Integer32):
    """Custom type AbbrevRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("createAndGo", 4),
          ("destroy", 6))
    )





class DoActionShowProgress(Integer32):
    """Custom type DoActionShowProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doActionRightNow", 1),
          ("idleState", 2))
    )





class HexPassword(OctetString):
    """Custom type HexPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )





class TransmitRate(Bits):
    """Custom type TransmitRate based on Bits"""



# TEXTUAL-CONVENTIONS



class RowStatus(Integer32, TextualConvention):
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )



class DateAndTime(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_Symbol_ObjectIdentity = ObjectIdentity
symbol = _Symbol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388)
)
_Wsd_ObjectIdentity = ObjectIdentity
wsd = _Wsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11)
)
_Sysoids_ObjectIdentity = ObjectIdentity
sysoids = _Sysoids_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 1)
)
_Ws2000_ObjectIdentity = ObjectIdentity
ws2000 = _Ws2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 1, 1)
)
if mibBuilder.loadTexts:
    ws2000.setStatus("current")
_Ws2k_ObjectIdentity = ObjectIdentity
ws2k = _Ws2k_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2)
)
_CcAdmin_ObjectIdentity = ObjectIdentity
ccAdmin = _CcAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2)
)
_CcInfo_ObjectIdentity = ObjectIdentity
ccInfo = _CcInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 1)
)
_CcInfoSerialNumber_Type = DisplayString
_CcInfoSerialNumber_Object = MibScalar
ccInfoSerialNumber = _CcInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 1, 1),
    _CcInfoSerialNumber_Type()
)
ccInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccInfoSerialNumber.setStatus("current")
_CcInfoCountrySelection_Type = DisplayString
_CcInfoCountrySelection_Object = MibScalar
ccInfoCountrySelection = _CcInfoCountrySelection_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 1, 2),
    _CcInfoCountrySelection_Type()
)
ccInfoCountrySelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccInfoCountrySelection.setStatus("current")
_CcIdentfication_ObjectIdentity = ObjectIdentity
ccIdentfication = _CcIdentfication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 1, 3)
)
_CcIdHwVersion_Type = DisplayString
_CcIdHwVersion_Object = MibScalar
ccIdHwVersion = _CcIdHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 1, 3, 1),
    _CcIdHwVersion_Type()
)
ccIdHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccIdHwVersion.setStatus("current")
_CcIdFwVersion_Type = DisplayString
_CcIdFwVersion_Object = MibScalar
ccIdFwVersion = _CcIdFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 1, 3, 2),
    _CcIdFwVersion_Type()
)
ccIdFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccIdFwVersion.setStatus("current")
_CcIdSwVersion_Type = DisplayString
_CcIdSwVersion_Object = MibScalar
ccIdSwVersion = _CcIdSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 1, 3, 3),
    _CcIdSwVersion_Type()
)
ccIdSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccIdSwVersion.setStatus("current")
_CcIdMibVersion_Type = DisplayString
_CcIdMibVersion_Object = MibScalar
ccIdMibVersion = _CcIdMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 1, 3, 4),
    _CcIdMibVersion_Type()
)
ccIdMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccIdMibVersion.setStatus("current")
_CcIdCliVersion_Type = DisplayString
_CcIdCliVersion_Object = MibScalar
ccIdCliVersion = _CcIdCliVersion_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 1, 3, 5),
    _CcIdCliVersion_Type()
)
ccIdCliVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccIdCliVersion.setStatus("current")
_CcIdXmlVersion_Type = DisplayString
_CcIdXmlVersion_Object = MibScalar
ccIdXmlVersion = _CcIdXmlVersion_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 1, 3, 6),
    _CcIdXmlVersion_Type()
)
ccIdXmlVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccIdXmlVersion.setStatus("current")
_CcIdSerialNumber_Type = DisplayString
_CcIdSerialNumber_Object = MibScalar
ccIdSerialNumber = _CcIdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 1, 3, 7),
    _CcIdSerialNumber_Type()
)
ccIdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccIdSerialNumber.setStatus("current")


class _CcSysDNSRelayMode_Type(TruthValue):
    """Custom type ccSysDNSRelayMode based on TruthValue"""


_CcSysDNSRelayMode_Object = MibScalar
ccSysDNSRelayMode = _CcSysDNSRelayMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 1, 4),
    _CcSysDNSRelayMode_Type()
)
ccSysDNSRelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSysDNSRelayMode.setStatus("current")


class _CcApSslv2Mode_Type(TruthValue):
    """Custom type ccApSslv2Mode based on TruthValue"""


_CcApSslv2Mode_Object = MibScalar
ccApSslv2Mode = _CcApSslv2Mode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 1, 5),
    _CcApSslv2Mode_Type()
)
ccApSslv2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccApSslv2Mode.setStatus("current")


class _CcApSshv1Mode_Type(TruthValue):
    """Custom type ccApSshv1Mode based on TruthValue"""


_CcApSshv1Mode_Object = MibScalar
ccApSshv1Mode = _CcApSshv1Mode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 1, 6),
    _CcApSshv1Mode_Type()
)
ccApSshv1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccApSshv1Mode.setStatus("current")


class _CcApSslWeakCipherSupport_Type(TruthValue):
    """Custom type ccApSslWeakCipherSupport based on TruthValue"""


_CcApSslWeakCipherSupport_Object = MibScalar
ccApSslWeakCipherSupport = _CcApSslWeakCipherSupport_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 1, 7),
    _CcApSslWeakCipherSupport_Type()
)
ccApSslWeakCipherSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccApSslWeakCipherSupport.setStatus("current")
_CcReset_ObjectIdentity = ObjectIdentity
ccReset = _CcReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 2)
)
_CcResetFactory_Type = TruthValue
_CcResetFactory_Object = MibScalar
ccResetFactory = _CcResetFactory_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 2, 1),
    _CcResetFactory_Type()
)
ccResetFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccResetFactory.setStatus("current")
_CcResetSwitch_Type = TruthValue
_CcResetSwitch_Object = MibScalar
ccResetSwitch = _CcResetSwitch_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 2, 2),
    _CcResetSwitch_Type()
)
ccResetSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccResetSwitch.setStatus("current")
_CcResetMuCounters_Type = TruthValue
_CcResetMuCounters_Object = MibScalar
ccResetMuCounters = _CcResetMuCounters_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 2, 3),
    _CcResetMuCounters_Type()
)
ccResetMuCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccResetMuCounters.setStatus("obsolete")
_CcResetFactoryExceptIpSnmp_Type = DoActionNow
_CcResetFactoryExceptIpSnmp_Object = MibScalar
ccResetFactoryExceptIpSnmp = _CcResetFactoryExceptIpSnmp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 2, 4),
    _CcResetFactoryExceptIpSnmp_Type()
)
ccResetFactoryExceptIpSnmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccResetFactoryExceptIpSnmp.setStatus("current")
_CcResetStatCounters_Type = TruthValue
_CcResetStatCounters_Object = MibScalar
ccResetStatCounters = _CcResetStatCounters_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 2, 5),
    _CcResetStatCounters_Type()
)
ccResetStatCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccResetStatCounters.setStatus("current")
_CcLoadFw_ObjectIdentity = ObjectIdentity
ccLoadFw = _CcLoadFw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 3)
)


class _CcLoadFwOperation_Type(Integer32):
    """Custom type ccLoadFwOperation based on Integer32"""
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
        *(("cfFirmwareToSwitch", 4),
          ("ftpFirmwareServerToSwitch", 2),
          ("sftpFirmwareServerToSwitch", 5),
          ("tftpFirmwareServerToSwitch", 3),
          ("unspecified", 1))
    )


_CcLoadFwOperation_Type.__name__ = "Integer32"
_CcLoadFwOperation_Object = MibScalar
ccLoadFwOperation = _CcLoadFwOperation_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 3, 1),
    _CcLoadFwOperation_Type()
)
ccLoadFwOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLoadFwOperation.setStatus("current")


class _CcLoadFwInterface_Type(Integer32):
    """Custom type ccLoadFwInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("subnet1", 11),
          ("subnet2", 12),
          ("subnet3", 13),
          ("subnet4", 14),
          ("unspecified", 1),
          ("wan", 2))
    )


_CcLoadFwInterface_Type.__name__ = "Integer32"
_CcLoadFwInterface_Object = MibScalar
ccLoadFwInterface = _CcLoadFwInterface_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 3, 2),
    _CcLoadFwInterface_Type()
)
ccLoadFwInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLoadFwInterface.setStatus("current")


class _CcLoadFwServerPath_Type(DisplayString):
    """Custom type ccLoadFwServerPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_CcLoadFwServerPath_Type.__name__ = "DisplayString"
_CcLoadFwServerPath_Object = MibScalar
ccLoadFwServerPath = _CcLoadFwServerPath_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 3, 3),
    _CcLoadFwServerPath_Type()
)
ccLoadFwServerPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLoadFwServerPath.setStatus("current")


class _CcLoadFwServerFilename_Type(DisplayString):
    """Custom type ccLoadFwServerFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_CcLoadFwServerFilename_Type.__name__ = "DisplayString"
_CcLoadFwServerFilename_Object = MibScalar
ccLoadFwServerFilename = _CcLoadFwServerFilename_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 3, 4),
    _CcLoadFwServerFilename_Type()
)
ccLoadFwServerFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLoadFwServerFilename.setStatus("current")
_CcLoadFwStart_Type = TruthValue
_CcLoadFwStart_Object = MibScalar
ccLoadFwStart = _CcLoadFwStart_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 3, 5),
    _CcLoadFwStart_Type()
)
ccLoadFwStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLoadFwStart.setStatus("current")
_CcLoadFwResult_Type = DisplayString
_CcLoadFwResult_Object = MibScalar
ccLoadFwResult = _CcLoadFwResult_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 3, 6),
    _CcLoadFwResult_Type()
)
ccLoadFwResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccLoadFwResult.setStatus("current")
_CcLoadFwSuccess_Type = TruthValue
_CcLoadFwSuccess_Object = MibScalar
ccLoadFwSuccess = _CcLoadFwSuccess_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 3, 7),
    _CcLoadFwSuccess_Type()
)
ccLoadFwSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccLoadFwSuccess.setStatus("current")
_CcLoadCfg_ObjectIdentity = ObjectIdentity
ccLoadCfg = _CcLoadCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 4)
)


class _CcLoadCfgOperation_Type(Integer32):
    """Custom type ccLoadCfgOperation based on Integer32"""
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
        *(("ftpConfigServerToSwitch", 2),
          ("ftpConfigSwitchToServer", 3),
          ("sftpConfigServerToSwitch", 6),
          ("sftpConfigSwitchToServer", 7),
          ("tftpConfigServerToSwitch", 4),
          ("tftpConfigSwitchToServer", 5),
          ("unspecified", 1))
    )


_CcLoadCfgOperation_Type.__name__ = "Integer32"
_CcLoadCfgOperation_Object = MibScalar
ccLoadCfgOperation = _CcLoadCfgOperation_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 4, 1),
    _CcLoadCfgOperation_Type()
)
ccLoadCfgOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLoadCfgOperation.setStatus("current")


class _CcLoadCfgServerPath_Type(DisplayString):
    """Custom type ccLoadCfgServerPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_CcLoadCfgServerPath_Type.__name__ = "DisplayString"
_CcLoadCfgServerPath_Object = MibScalar
ccLoadCfgServerPath = _CcLoadCfgServerPath_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 4, 2),
    _CcLoadCfgServerPath_Type()
)
ccLoadCfgServerPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLoadCfgServerPath.setStatus("current")


class _CcLoadCfgServerFilename_Type(DisplayString):
    """Custom type ccLoadCfgServerFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_CcLoadCfgServerFilename_Type.__name__ = "DisplayString"
_CcLoadCfgServerFilename_Object = MibScalar
ccLoadCfgServerFilename = _CcLoadCfgServerFilename_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 4, 3),
    _CcLoadCfgServerFilename_Type()
)
ccLoadCfgServerFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLoadCfgServerFilename.setStatus("current")
_CcLoadCfgStart_Type = TruthValue
_CcLoadCfgStart_Object = MibScalar
ccLoadCfgStart = _CcLoadCfgStart_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 4, 4),
    _CcLoadCfgStart_Type()
)
ccLoadCfgStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLoadCfgStart.setStatus("current")
_CcLoadCfgOperationsDone_Type = Counter32
_CcLoadCfgOperationsDone_Object = MibScalar
ccLoadCfgOperationsDone = _CcLoadCfgOperationsDone_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 4, 5),
    _CcLoadCfgOperationsDone_Type()
)
ccLoadCfgOperationsDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccLoadCfgOperationsDone.setStatus("current")
_CcLoadCfgResult_Type = DisplayString
_CcLoadCfgResult_Object = MibScalar
ccLoadCfgResult = _CcLoadCfgResult_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 4, 6),
    _CcLoadCfgResult_Type()
)
ccLoadCfgResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccLoadCfgResult.setStatus("current")
_CcLoadCfgSuccess_Type = TruthValue
_CcLoadCfgSuccess_Object = MibScalar
ccLoadCfgSuccess = _CcLoadCfgSuccess_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 4, 7),
    _CcLoadCfgSuccess_Type()
)
ccLoadCfgSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccLoadCfgSuccess.setStatus("current")
_CcCfgHist_ObjectIdentity = ObjectIdentity
ccCfgHist = _CcCfgHist_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 5)
)
_CcCfgHistChangeCount_Type = Unsigned32
_CcCfgHistChangeCount_Object = MibScalar
ccCfgHistChangeCount = _CcCfgHistChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 5, 1),
    _CcCfgHistChangeCount_Type()
)
ccCfgHistChangeCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCfgHistChangeCount.setStatus("current")
_CcCfgHistChangeTime_Type = TimeTicks
_CcCfgHistChangeTime_Object = MibScalar
ccCfgHistChangeTime = _CcCfgHistChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 5, 2),
    _CcCfgHistChangeTime_Type()
)
ccCfgHistChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCfgHistChangeTime.setStatus("current")
_CcCfgHistSemaphore_Type = TestAndIncr
_CcCfgHistSemaphore_Object = MibScalar
ccCfgHistSemaphore = _CcCfgHistSemaphore_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 5, 3),
    _CcCfgHistSemaphore_Type()
)
ccCfgHistSemaphore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCfgHistSemaphore.setStatus("current")
_CcLoad_ObjectIdentity = ObjectIdentity
ccLoad = _CcLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 6)
)
_CcLoadServerIpAddr_Type = IpAddress
_CcLoadServerIpAddr_Object = MibScalar
ccLoadServerIpAddr = _CcLoadServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 6, 1),
    _CcLoadServerIpAddr_Type()
)
ccLoadServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLoadServerIpAddr.setStatus("current")


class _CcLoadFtpUsername_Type(DisplayString):
    """Custom type ccLoadFtpUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_CcLoadFtpUsername_Type.__name__ = "DisplayString"
_CcLoadFtpUsername_Object = MibScalar
ccLoadFtpUsername = _CcLoadFtpUsername_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 6, 2),
    _CcLoadFtpUsername_Type()
)
ccLoadFtpUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLoadFtpUsername.setStatus("current")


class _CcLoadFtpPassword_Type(DisplayString):
    """Custom type ccLoadFtpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_CcLoadFtpPassword_Type.__name__ = "DisplayString"
_CcLoadFtpPassword_Object = MibScalar
ccLoadFtpPassword = _CcLoadFtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 6, 3),
    _CcLoadFtpPassword_Type()
)
ccLoadFtpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLoadFtpPassword.setStatus("current")
_CcSnmp_ObjectIdentity = ObjectIdentity
ccSnmp = _CcSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7)
)
_CcSnmpAclViolations_Type = Counter32
_CcSnmpAclViolations_Object = MibScalar
ccSnmpAclViolations = _CcSnmpAclViolations_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 1),
    _CcSnmpAclViolations_Type()
)
ccSnmpAclViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccSnmpAclViolations.setStatus("current")
_CcSnmpLastDeniedIpAddr_Type = IpAddress
_CcSnmpLastDeniedIpAddr_Object = MibScalar
ccSnmpLastDeniedIpAddr = _CcSnmpLastDeniedIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 2),
    _CcSnmpLastDeniedIpAddr_Type()
)
ccSnmpLastDeniedIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccSnmpLastDeniedIpAddr.setStatus("current")


class _CcSnmpV3EngineId_Type(DisplayString):
    """Custom type ccSnmpV3EngineId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CcSnmpV3EngineId_Type.__name__ = "DisplayString"
_CcSnmpV3EngineId_Object = MibScalar
ccSnmpV3EngineId = _CcSnmpV3EngineId_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 3),
    _CcSnmpV3EngineId_Type()
)
ccSnmpV3EngineId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccSnmpV3EngineId.setStatus("current")
_CcSnmpAccess_ObjectIdentity = ObjectIdentity
ccSnmpAccess = _CcSnmpAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 4)
)
_CcSnmpAccessV12Table_Object = MibTable
ccSnmpAccessV12Table = _CcSnmpAccessV12Table_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 4, 1)
)
if mibBuilder.loadTexts:
    ccSnmpAccessV12Table.setStatus("current")
_CcSnmpAccessV12Entry_Object = MibTableRow
ccSnmpAccessV12Entry = _CcSnmpAccessV12Entry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 4, 1, 1)
)
ccSnmpAccessV12Entry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccSnmpAccessV12Index"),
)
if mibBuilder.loadTexts:
    ccSnmpAccessV12Entry.setStatus("current")


class _CcSnmpAccessV12Index_Type(Integer32):
    """Custom type ccSnmpAccessV12Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CcSnmpAccessV12Index_Type.__name__ = "Integer32"
_CcSnmpAccessV12Index_Object = MibTableColumn
ccSnmpAccessV12Index = _CcSnmpAccessV12Index_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 4, 1, 1, 1),
    _CcSnmpAccessV12Index_Type()
)
ccSnmpAccessV12Index.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccSnmpAccessV12Index.setStatus("current")
_CcSnmpAccessV12Community_Type = DisplayString
_CcSnmpAccessV12Community_Object = MibTableColumn
ccSnmpAccessV12Community = _CcSnmpAccessV12Community_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 4, 1, 1, 2),
    _CcSnmpAccessV12Community_Type()
)
ccSnmpAccessV12Community.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpAccessV12Community.setStatus("current")
_CcSnmpAccessV12CustomOid_Type = ObjectIdentifier
_CcSnmpAccessV12CustomOid_Object = MibTableColumn
ccSnmpAccessV12CustomOid = _CcSnmpAccessV12CustomOid_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 4, 1, 1, 3),
    _CcSnmpAccessV12CustomOid_Type()
)
ccSnmpAccessV12CustomOid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpAccessV12CustomOid.setStatus("current")


class _CcSnmpAccessV12OidLimit_Type(Integer32):
    """Custom type ccSnmpAccessV12OidLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("custom", 2))
    )


_CcSnmpAccessV12OidLimit_Type.__name__ = "Integer32"
_CcSnmpAccessV12OidLimit_Object = MibTableColumn
ccSnmpAccessV12OidLimit = _CcSnmpAccessV12OidLimit_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 4, 1, 1, 4),
    _CcSnmpAccessV12OidLimit_Type()
)
ccSnmpAccessV12OidLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpAccessV12OidLimit.setStatus("current")


class _CcSnmpAccessV12Access_Type(Integer32):
    """Custom type ccSnmpAccessV12Access based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_CcSnmpAccessV12Access_Type.__name__ = "Integer32"
_CcSnmpAccessV12Access_Object = MibTableColumn
ccSnmpAccessV12Access = _CcSnmpAccessV12Access_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 4, 1, 1, 5),
    _CcSnmpAccessV12Access_Type()
)
ccSnmpAccessV12Access.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpAccessV12Access.setStatus("current")
_CcSnmpAccessV12Enable_Type = AbbrevRowStatus
_CcSnmpAccessV12Enable_Object = MibTableColumn
ccSnmpAccessV12Enable = _CcSnmpAccessV12Enable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 4, 1, 1, 6),
    _CcSnmpAccessV12Enable_Type()
)
ccSnmpAccessV12Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpAccessV12Enable.setStatus("current")
_CcSnmpAccessV3Table_Object = MibTable
ccSnmpAccessV3Table = _CcSnmpAccessV3Table_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 4, 2)
)
if mibBuilder.loadTexts:
    ccSnmpAccessV3Table.setStatus("current")
_CcSnmpAccessV3Entry_Object = MibTableRow
ccSnmpAccessV3Entry = _CcSnmpAccessV3Entry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 4, 2, 1)
)
ccSnmpAccessV3Entry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccSnmpAccessV3Index"),
)
if mibBuilder.loadTexts:
    ccSnmpAccessV3Entry.setStatus("current")


class _CcSnmpAccessV3Index_Type(Integer32):
    """Custom type ccSnmpAccessV3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CcSnmpAccessV3Index_Type.__name__ = "Integer32"
_CcSnmpAccessV3Index_Object = MibTableColumn
ccSnmpAccessV3Index = _CcSnmpAccessV3Index_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 4, 2, 1, 1),
    _CcSnmpAccessV3Index_Type()
)
ccSnmpAccessV3Index.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccSnmpAccessV3Index.setStatus("current")


class _CcSnmpAccessV3User_Type(DisplayString):
    """Custom type ccSnmpAccessV3User based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcSnmpAccessV3User_Type.__name__ = "DisplayString"
_CcSnmpAccessV3User_Object = MibTableColumn
ccSnmpAccessV3User = _CcSnmpAccessV3User_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 4, 2, 1, 2),
    _CcSnmpAccessV3User_Type()
)
ccSnmpAccessV3User.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpAccessV3User.setStatus("current")


class _CcSnmpAccessV3SecurityLevel_Type(Integer32):
    """Custom type ccSnmpAccessV3SecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authNoPriv", 2),
          ("authPriv", 3),
          ("noAuth", 1))
    )


_CcSnmpAccessV3SecurityLevel_Type.__name__ = "Integer32"
_CcSnmpAccessV3SecurityLevel_Object = MibTableColumn
ccSnmpAccessV3SecurityLevel = _CcSnmpAccessV3SecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 4, 2, 1, 3),
    _CcSnmpAccessV3SecurityLevel_Type()
)
ccSnmpAccessV3SecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpAccessV3SecurityLevel.setStatus("current")
_CcSnmpAccessV3CustomOid_Type = ObjectIdentifier
_CcSnmpAccessV3CustomOid_Object = MibTableColumn
ccSnmpAccessV3CustomOid = _CcSnmpAccessV3CustomOid_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 4, 2, 1, 4),
    _CcSnmpAccessV3CustomOid_Type()
)
ccSnmpAccessV3CustomOid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpAccessV3CustomOid.setStatus("current")


class _CcSnmpAccessV3OidLimit_Type(Integer32):
    """Custom type ccSnmpAccessV3OidLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("custom", 2))
    )


_CcSnmpAccessV3OidLimit_Type.__name__ = "Integer32"
_CcSnmpAccessV3OidLimit_Object = MibTableColumn
ccSnmpAccessV3OidLimit = _CcSnmpAccessV3OidLimit_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 4, 2, 1, 5),
    _CcSnmpAccessV3OidLimit_Type()
)
ccSnmpAccessV3OidLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpAccessV3OidLimit.setStatus("current")


class _CcSnmpAccessV3Access_Type(Integer32):
    """Custom type ccSnmpAccessV3Access based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_CcSnmpAccessV3Access_Type.__name__ = "Integer32"
_CcSnmpAccessV3Access_Object = MibTableColumn
ccSnmpAccessV3Access = _CcSnmpAccessV3Access_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 4, 2, 1, 6),
    _CcSnmpAccessV3Access_Type()
)
ccSnmpAccessV3Access.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpAccessV3Access.setStatus("current")


class _CcSnmpAccessV3AuthAlgorithm_Type(Integer32):
    """Custom type ccSnmpAccessV3AuthAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha", 2))
    )


_CcSnmpAccessV3AuthAlgorithm_Type.__name__ = "Integer32"
_CcSnmpAccessV3AuthAlgorithm_Object = MibTableColumn
ccSnmpAccessV3AuthAlgorithm = _CcSnmpAccessV3AuthAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 4, 2, 1, 7),
    _CcSnmpAccessV3AuthAlgorithm_Type()
)
ccSnmpAccessV3AuthAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpAccessV3AuthAlgorithm.setStatus("current")


class _CcSnmpAccessV3AuthPassword_Type(Password):
    """Custom type ccSnmpAccessV3AuthPassword based on Password"""
    subtypeSpec = Password.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 31),
    )


_CcSnmpAccessV3AuthPassword_Type.__name__ = "Password"
_CcSnmpAccessV3AuthPassword_Object = MibTableColumn
ccSnmpAccessV3AuthPassword = _CcSnmpAccessV3AuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 4, 2, 1, 8),
    _CcSnmpAccessV3AuthPassword_Type()
)
ccSnmpAccessV3AuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpAccessV3AuthPassword.setStatus("current")


class _CcSnmpAccessV3PrivacyAlgorithm_Type(Integer32):
    """Custom type ccSnmpAccessV3PrivacyAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aes128", 2),
          ("des", 1))
    )


_CcSnmpAccessV3PrivacyAlgorithm_Type.__name__ = "Integer32"
_CcSnmpAccessV3PrivacyAlgorithm_Object = MibTableColumn
ccSnmpAccessV3PrivacyAlgorithm = _CcSnmpAccessV3PrivacyAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 4, 2, 1, 9),
    _CcSnmpAccessV3PrivacyAlgorithm_Type()
)
ccSnmpAccessV3PrivacyAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpAccessV3PrivacyAlgorithm.setStatus("current")


class _CcSnmpAccessV3PrivacyPassword_Type(Password):
    """Custom type ccSnmpAccessV3PrivacyPassword based on Password"""
    subtypeSpec = Password.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 31),
    )


_CcSnmpAccessV3PrivacyPassword_Type.__name__ = "Password"
_CcSnmpAccessV3PrivacyPassword_Object = MibTableColumn
ccSnmpAccessV3PrivacyPassword = _CcSnmpAccessV3PrivacyPassword_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 4, 2, 1, 10),
    _CcSnmpAccessV3PrivacyPassword_Type()
)
ccSnmpAccessV3PrivacyPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpAccessV3PrivacyPassword.setStatus("current")
_CcSnmpAccessV3Enable_Type = AbbrevRowStatus
_CcSnmpAccessV3Enable_Object = MibTableColumn
ccSnmpAccessV3Enable = _CcSnmpAccessV3Enable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 4, 2, 1, 11),
    _CcSnmpAccessV3Enable_Type()
)
ccSnmpAccessV3Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpAccessV3Enable.setStatus("current")
_CcSnmpAccessControlTable_Object = MibTable
ccSnmpAccessControlTable = _CcSnmpAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 4, 3)
)
if mibBuilder.loadTexts:
    ccSnmpAccessControlTable.setStatus("current")
_CcSnmpAccessControlEntry_Object = MibTableRow
ccSnmpAccessControlEntry = _CcSnmpAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 4, 3, 1)
)
ccSnmpAccessControlEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccSnmpAccessControlIndex"),
)
if mibBuilder.loadTexts:
    ccSnmpAccessControlEntry.setStatus("current")


class _CcSnmpAccessControlIndex_Type(Integer32):
    """Custom type ccSnmpAccessControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CcSnmpAccessControlIndex_Type.__name__ = "Integer32"
_CcSnmpAccessControlIndex_Object = MibTableColumn
ccSnmpAccessControlIndex = _CcSnmpAccessControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 4, 3, 1, 1),
    _CcSnmpAccessControlIndex_Type()
)
ccSnmpAccessControlIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccSnmpAccessControlIndex.setStatus("current")
_CcSnmpAccessControlStartIp_Type = IpAddress
_CcSnmpAccessControlStartIp_Object = MibTableColumn
ccSnmpAccessControlStartIp = _CcSnmpAccessControlStartIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 4, 3, 1, 2),
    _CcSnmpAccessControlStartIp_Type()
)
ccSnmpAccessControlStartIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpAccessControlStartIp.setStatus("current")
_CcSnmpAccessControlEndIp_Type = IpAddress
_CcSnmpAccessControlEndIp_Object = MibTableColumn
ccSnmpAccessControlEndIp = _CcSnmpAccessControlEndIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 4, 3, 1, 3),
    _CcSnmpAccessControlEndIp_Type()
)
ccSnmpAccessControlEndIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpAccessControlEndIp.setStatus("current")
_CcSnmpAccessControlEnable_Type = AbbrevRowStatus
_CcSnmpAccessControlEnable_Object = MibTableColumn
ccSnmpAccessControlEnable = _CcSnmpAccessControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 4, 3, 1, 4),
    _CcSnmpAccessControlEnable_Type()
)
ccSnmpAccessControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpAccessControlEnable.setStatus("current")
_CcSnmpTraps_ObjectIdentity = ObjectIdentity
ccSnmpTraps = _CcSnmpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 5)
)
_CcSnmpTrapSinkV12Table_Object = MibTable
ccSnmpTrapSinkV12Table = _CcSnmpTrapSinkV12Table_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 5, 1)
)
if mibBuilder.loadTexts:
    ccSnmpTrapSinkV12Table.setStatus("current")
_CcSnmpTrapSinkV12Entry_Object = MibTableRow
ccSnmpTrapSinkV12Entry = _CcSnmpTrapSinkV12Entry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 5, 1, 1)
)
ccSnmpTrapSinkV12Entry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccSnmpTrapSinkV12Index"),
)
if mibBuilder.loadTexts:
    ccSnmpTrapSinkV12Entry.setStatus("current")


class _CcSnmpTrapSinkV12Index_Type(Integer32):
    """Custom type ccSnmpTrapSinkV12Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CcSnmpTrapSinkV12Index_Type.__name__ = "Integer32"
_CcSnmpTrapSinkV12Index_Object = MibTableColumn
ccSnmpTrapSinkV12Index = _CcSnmpTrapSinkV12Index_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 5, 1, 1, 1),
    _CcSnmpTrapSinkV12Index_Type()
)
ccSnmpTrapSinkV12Index.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccSnmpTrapSinkV12Index.setStatus("current")
_CcSnmpTrapSinkV12DestinationIp_Type = IpAddress
_CcSnmpTrapSinkV12DestinationIp_Object = MibTableColumn
ccSnmpTrapSinkV12DestinationIp = _CcSnmpTrapSinkV12DestinationIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 5, 1, 1, 2),
    _CcSnmpTrapSinkV12DestinationIp_Type()
)
ccSnmpTrapSinkV12DestinationIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpTrapSinkV12DestinationIp.setStatus("current")
_CcSnmpTrapSinkV12Port_Type = Integer32
_CcSnmpTrapSinkV12Port_Object = MibTableColumn
ccSnmpTrapSinkV12Port = _CcSnmpTrapSinkV12Port_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 5, 1, 1, 3),
    _CcSnmpTrapSinkV12Port_Type()
)
ccSnmpTrapSinkV12Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpTrapSinkV12Port.setStatus("current")
_CcSnmpTrapSinkV12Community_Type = DisplayString
_CcSnmpTrapSinkV12Community_Object = MibTableColumn
ccSnmpTrapSinkV12Community = _CcSnmpTrapSinkV12Community_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 5, 1, 1, 4),
    _CcSnmpTrapSinkV12Community_Type()
)
ccSnmpTrapSinkV12Community.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpTrapSinkV12Community.setStatus("current")


class _CcSnmpTrapSinkV12Version_Type(Integer32):
    """Custom type ccSnmpTrapSinkV12Version based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("snmpV1", 1),
          ("snmpV2", 2))
    )


_CcSnmpTrapSinkV12Version_Type.__name__ = "Integer32"
_CcSnmpTrapSinkV12Version_Object = MibTableColumn
ccSnmpTrapSinkV12Version = _CcSnmpTrapSinkV12Version_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 5, 1, 1, 5),
    _CcSnmpTrapSinkV12Version_Type()
)
ccSnmpTrapSinkV12Version.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpTrapSinkV12Version.setStatus("current")
_CcSnmpTrapSinkV12Enable_Type = AbbrevRowStatus
_CcSnmpTrapSinkV12Enable_Object = MibTableColumn
ccSnmpTrapSinkV12Enable = _CcSnmpTrapSinkV12Enable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 5, 1, 1, 6),
    _CcSnmpTrapSinkV12Enable_Type()
)
ccSnmpTrapSinkV12Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpTrapSinkV12Enable.setStatus("current")
_CcSnmpTrapSinkV3Table_Object = MibTable
ccSnmpTrapSinkV3Table = _CcSnmpTrapSinkV3Table_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 5, 2)
)
if mibBuilder.loadTexts:
    ccSnmpTrapSinkV3Table.setStatus("current")
_CcSnmpTrapSinkV3Entry_Object = MibTableRow
ccSnmpTrapSinkV3Entry = _CcSnmpTrapSinkV3Entry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 5, 2, 1)
)
ccSnmpTrapSinkV3Entry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccSnmpTrapSinkV3Index"),
)
if mibBuilder.loadTexts:
    ccSnmpTrapSinkV3Entry.setStatus("current")


class _CcSnmpTrapSinkV3Index_Type(Integer32):
    """Custom type ccSnmpTrapSinkV3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CcSnmpTrapSinkV3Index_Type.__name__ = "Integer32"
_CcSnmpTrapSinkV3Index_Object = MibTableColumn
ccSnmpTrapSinkV3Index = _CcSnmpTrapSinkV3Index_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 5, 2, 1, 1),
    _CcSnmpTrapSinkV3Index_Type()
)
ccSnmpTrapSinkV3Index.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccSnmpTrapSinkV3Index.setStatus("current")
_CcSnmpTrapSinkV3DestinationIp_Type = IpAddress
_CcSnmpTrapSinkV3DestinationIp_Object = MibTableColumn
ccSnmpTrapSinkV3DestinationIp = _CcSnmpTrapSinkV3DestinationIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 5, 2, 1, 2),
    _CcSnmpTrapSinkV3DestinationIp_Type()
)
ccSnmpTrapSinkV3DestinationIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpTrapSinkV3DestinationIp.setStatus("current")
_CcSnmpTrapSinkV3Port_Type = Integer32
_CcSnmpTrapSinkV3Port_Object = MibTableColumn
ccSnmpTrapSinkV3Port = _CcSnmpTrapSinkV3Port_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 5, 2, 1, 3),
    _CcSnmpTrapSinkV3Port_Type()
)
ccSnmpTrapSinkV3Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpTrapSinkV3Port.setStatus("current")
_CcSnmpTrapSinkV3Username_Type = DisplayString
_CcSnmpTrapSinkV3Username_Object = MibTableColumn
ccSnmpTrapSinkV3Username = _CcSnmpTrapSinkV3Username_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 5, 2, 1, 4),
    _CcSnmpTrapSinkV3Username_Type()
)
ccSnmpTrapSinkV3Username.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpTrapSinkV3Username.setStatus("current")


class _CcSnmpTrapSinkV3SecurityLevel_Type(Integer32):
    """Custom type ccSnmpTrapSinkV3SecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auth", 1),
          ("authNoPriv", 2),
          ("authPriv", 3))
    )


_CcSnmpTrapSinkV3SecurityLevel_Type.__name__ = "Integer32"
_CcSnmpTrapSinkV3SecurityLevel_Object = MibTableColumn
ccSnmpTrapSinkV3SecurityLevel = _CcSnmpTrapSinkV3SecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 5, 2, 1, 5),
    _CcSnmpTrapSinkV3SecurityLevel_Type()
)
ccSnmpTrapSinkV3SecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpTrapSinkV3SecurityLevel.setStatus("current")


class _CcSnmpTrapSinkV3AuthAlgorithm_Type(Integer32):
    """Custom type ccSnmpTrapSinkV3AuthAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha", 2))
    )


_CcSnmpTrapSinkV3AuthAlgorithm_Type.__name__ = "Integer32"
_CcSnmpTrapSinkV3AuthAlgorithm_Object = MibTableColumn
ccSnmpTrapSinkV3AuthAlgorithm = _CcSnmpTrapSinkV3AuthAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 5, 2, 1, 6),
    _CcSnmpTrapSinkV3AuthAlgorithm_Type()
)
ccSnmpTrapSinkV3AuthAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpTrapSinkV3AuthAlgorithm.setStatus("current")


class _CcSnmpTrapSinkV3AuthPassword_Type(Password):
    """Custom type ccSnmpTrapSinkV3AuthPassword based on Password"""
    subtypeSpec = Password.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 31),
    )


_CcSnmpTrapSinkV3AuthPassword_Type.__name__ = "Password"
_CcSnmpTrapSinkV3AuthPassword_Object = MibTableColumn
ccSnmpTrapSinkV3AuthPassword = _CcSnmpTrapSinkV3AuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 5, 2, 1, 7),
    _CcSnmpTrapSinkV3AuthPassword_Type()
)
ccSnmpTrapSinkV3AuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpTrapSinkV3AuthPassword.setStatus("current")


class _CcSnmpTrapSinkV3PrivacyAlgorithm_Type(Integer32):
    """Custom type ccSnmpTrapSinkV3PrivacyAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aes128", 2),
          ("des", 1))
    )


_CcSnmpTrapSinkV3PrivacyAlgorithm_Type.__name__ = "Integer32"
_CcSnmpTrapSinkV3PrivacyAlgorithm_Object = MibTableColumn
ccSnmpTrapSinkV3PrivacyAlgorithm = _CcSnmpTrapSinkV3PrivacyAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 5, 2, 1, 8),
    _CcSnmpTrapSinkV3PrivacyAlgorithm_Type()
)
ccSnmpTrapSinkV3PrivacyAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpTrapSinkV3PrivacyAlgorithm.setStatus("current")


class _CcSnmpTrapSinkV3PrivacyPassword_Type(Password):
    """Custom type ccSnmpTrapSinkV3PrivacyPassword based on Password"""
    subtypeSpec = Password.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 31),
    )


_CcSnmpTrapSinkV3PrivacyPassword_Type.__name__ = "Password"
_CcSnmpTrapSinkV3PrivacyPassword_Object = MibTableColumn
ccSnmpTrapSinkV3PrivacyPassword = _CcSnmpTrapSinkV3PrivacyPassword_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 5, 2, 1, 9),
    _CcSnmpTrapSinkV3PrivacyPassword_Type()
)
ccSnmpTrapSinkV3PrivacyPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpTrapSinkV3PrivacyPassword.setStatus("current")
_CcSnmpTrapSinkV3Enable_Type = AbbrevRowStatus
_CcSnmpTrapSinkV3Enable_Object = MibTableColumn
ccSnmpTrapSinkV3Enable = _CcSnmpTrapSinkV3Enable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 7, 5, 2, 1, 10),
    _CcSnmpTrapSinkV3Enable_Type()
)
ccSnmpTrapSinkV3Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSnmpTrapSinkV3Enable.setStatus("current")
_CcCompactFlash_ObjectIdentity = ObjectIdentity
ccCompactFlash = _CcCompactFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 8)
)
_CcCompactFlashCapacity_Type = Integer32
_CcCompactFlashCapacity_Object = MibScalar
ccCompactFlashCapacity = _CcCompactFlashCapacity_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 8, 1),
    _CcCompactFlashCapacity_Type()
)
ccCompactFlashCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCompactFlashCapacity.setStatus("current")
_CcCompactFlashUsed_Type = Integer32
_CcCompactFlashUsed_Object = MibScalar
ccCompactFlashUsed = _CcCompactFlashUsed_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 8, 2),
    _CcCompactFlashUsed_Type()
)
ccCompactFlashUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCompactFlashUsed.setStatus("current")
_CcSumStats_ObjectIdentity = ObjectIdentity
ccSumStats = _CcSumStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 9)
)
_CcSumStatsShortWindow_Type = Integer32
_CcSumStatsShortWindow_Object = MibScalar
ccSumStatsShortWindow = _CcSumStatsShortWindow_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 9, 1),
    _CcSumStatsShortWindow_Type()
)
ccSumStatsShortWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccSumStatsShortWindow.setStatus("current")
if mibBuilder.loadTexts:
    ccSumStatsShortWindow.setUnits("seconds")
_CcSumStatsShortUpdateInterval_Type = Integer32
_CcSumStatsShortUpdateInterval_Object = MibScalar
ccSumStatsShortUpdateInterval = _CcSumStatsShortUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 9, 2),
    _CcSumStatsShortUpdateInterval_Type()
)
ccSumStatsShortUpdateInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccSumStatsShortUpdateInterval.setStatus("current")
if mibBuilder.loadTexts:
    ccSumStatsShortUpdateInterval.setUnits("seconds")
_CcSumStatsLongWindow_Type = Integer32
_CcSumStatsLongWindow_Object = MibScalar
ccSumStatsLongWindow = _CcSumStatsLongWindow_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 9, 3),
    _CcSumStatsLongWindow_Type()
)
ccSumStatsLongWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccSumStatsLongWindow.setStatus("current")
if mibBuilder.loadTexts:
    ccSumStatsLongWindow.setUnits("minutes")
_CcSumStatsLongUpdateInterval_Type = Integer32
_CcSumStatsLongUpdateInterval_Object = MibScalar
ccSumStatsLongUpdateInterval = _CcSumStatsLongUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 9, 4),
    _CcSumStatsLongUpdateInterval_Type()
)
ccSumStatsLongUpdateInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccSumStatsLongUpdateInterval.setStatus("current")
if mibBuilder.loadTexts:
    ccSumStatsLongUpdateInterval.setUnits("minutes")
_CcMgmtAccess_ObjectIdentity = ObjectIdentity
ccMgmtAccess = _CcMgmtAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 10)
)


class _CcMgmtAccessToAllow_Type(Bits):
    """Custom type ccMgmtAccessToAllow based on Bits"""
    namedValues = NamedValues(
        *(("fromLanAppletHttp", 0),
          ("fromLanAppletHttps", 1),
          ("fromLanCliTelnet", 2),
          ("fromLanSnmp", 4),
          ("fromLanSsh", 3),
          ("fromWanAppletHttp", 5),
          ("fromWanAppletHttps", 6),
          ("fromWanCliTelnet", 7),
          ("fromWanFtp", 10),
          ("fromWanSnmp", 9),
          ("fromWanSsh", 8))
    )

_CcMgmtAccessToAllow_Type.__name__ = "Bits"
_CcMgmtAccessToAllow_Object = MibScalar
ccMgmtAccessToAllow = _CcMgmtAccessToAllow_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 10, 1),
    _CcMgmtAccessToAllow_Type()
)
ccMgmtAccessToAllow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccMgmtAccessToAllow.setStatus("current")
_CcMgmtAccessAirbeam_ObjectIdentity = ObjectIdentity
ccMgmtAccessAirbeam = _CcMgmtAccessAirbeam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 10, 2)
)
_CcMgmtAccessAirbeamAllow_Type = TruthValue
_CcMgmtAccessAirbeamAllow_Object = MibScalar
ccMgmtAccessAirbeamAllow = _CcMgmtAccessAirbeamAllow_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 10, 2, 1),
    _CcMgmtAccessAirbeamAllow_Type()
)
ccMgmtAccessAirbeamAllow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccMgmtAccessAirbeamAllow.setStatus("current")
_CcMgmtAccessAirbeamPassword_Type = Password
_CcMgmtAccessAirbeamPassword_Object = MibScalar
ccMgmtAccessAirbeamPassword = _CcMgmtAccessAirbeamPassword_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 10, 2, 2),
    _CcMgmtAccessAirbeamPassword_Type()
)
ccMgmtAccessAirbeamPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccMgmtAccessAirbeamPassword.setStatus("current")
_CcMgmtAccessAdmin_ObjectIdentity = ObjectIdentity
ccMgmtAccessAdmin = _CcMgmtAccessAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 10, 3)
)


class _CcMgmtAccessAdminAuth_Type(Integer32):
    """Custom type ccMgmtAccessAdminAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("radius", 2))
    )


_CcMgmtAccessAdminAuth_Type.__name__ = "Integer32"
_CcMgmtAccessAdminAuth_Object = MibScalar
ccMgmtAccessAdminAuth = _CcMgmtAccessAdminAuth_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 10, 3, 1),
    _CcMgmtAccessAdminAuth_Type()
)
ccMgmtAccessAdminAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccMgmtAccessAdminAuth.setStatus("current")


class _CcMgmtAccessAdminPassword_Type(Password):
    """Custom type ccMgmtAccessAdminPassword based on Password"""
    subtypeSpec = Password.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 11),
    )


_CcMgmtAccessAdminPassword_Type.__name__ = "Password"
_CcMgmtAccessAdminPassword_Object = MibScalar
ccMgmtAccessAdminPassword = _CcMgmtAccessAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 10, 3, 2),
    _CcMgmtAccessAdminPassword_Type()
)
ccMgmtAccessAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccMgmtAccessAdminPassword.setStatus("current")
_CcMgmtAccessAdminAuthRadiusServerIp_Type = IpAddress
_CcMgmtAccessAdminAuthRadiusServerIp_Object = MibScalar
ccMgmtAccessAdminAuthRadiusServerIp = _CcMgmtAccessAdminAuthRadiusServerIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 10, 3, 4),
    _CcMgmtAccessAdminAuthRadiusServerIp_Type()
)
ccMgmtAccessAdminAuthRadiusServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccMgmtAccessAdminAuthRadiusServerIp.setStatus("current")
_CcMgmtAccessAdminAuthRadiusServerPort_Type = Unsigned32
_CcMgmtAccessAdminAuthRadiusServerPort_Object = MibScalar
ccMgmtAccessAdminAuthRadiusServerPort = _CcMgmtAccessAdminAuthRadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 10, 3, 5),
    _CcMgmtAccessAdminAuthRadiusServerPort_Type()
)
ccMgmtAccessAdminAuthRadiusServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccMgmtAccessAdminAuthRadiusServerPort.setStatus("current")
_CcMgmtAccessAdminAuthRadiusSharedSecret_Type = Password
_CcMgmtAccessAdminAuthRadiusSharedSecret_Object = MibScalar
ccMgmtAccessAdminAuthRadiusSharedSecret = _CcMgmtAccessAdminAuthRadiusSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 10, 3, 6),
    _CcMgmtAccessAdminAuthRadiusSharedSecret_Type()
)
ccMgmtAccessAdminAuthRadiusSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccMgmtAccessAdminAuthRadiusSharedSecret.setStatus("current")
_CcMgmtAccessSsh_ObjectIdentity = ObjectIdentity
ccMgmtAccessSsh = _CcMgmtAccessSsh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 10, 4)
)
_CcMgmtAccessSshAuthTimeout_Type = Unsigned32
_CcMgmtAccessSshAuthTimeout_Object = MibScalar
ccMgmtAccessSshAuthTimeout = _CcMgmtAccessSshAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 10, 4, 1),
    _CcMgmtAccessSshAuthTimeout_Type()
)
ccMgmtAccessSshAuthTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccMgmtAccessSshAuthTimeout.setStatus("current")
_CcMgmtAccessSshInactivityTimeout_Type = Unsigned32
_CcMgmtAccessSshInactivityTimeout_Object = MibScalar
ccMgmtAccessSshInactivityTimeout = _CcMgmtAccessSshInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 10, 4, 2),
    _CcMgmtAccessSshInactivityTimeout_Type()
)
ccMgmtAccessSshInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccMgmtAccessSshInactivityTimeout.setStatus("current")
_CcMgmtAccessHttpsTimeout_Type = Unsigned32
_CcMgmtAccessHttpsTimeout_Object = MibScalar
ccMgmtAccessHttpsTimeout = _CcMgmtAccessHttpsTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 10, 5),
    _CcMgmtAccessHttpsTimeout_Type()
)
ccMgmtAccessHttpsTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccMgmtAccessHttpsTimeout.setStatus("current")
_CcLogging_ObjectIdentity = ObjectIdentity
ccLogging = _CcLogging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 11)
)


class _CcLoggingLevel_Type(Integer32):
    """Custom type ccLoggingLevel based on Integer32"""
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
        *(("level0Emergency", 0),
          ("level1Alert", 1),
          ("level2Critical", 2),
          ("level3Errors", 3),
          ("level4Warnings", 4),
          ("level5Notice", 5),
          ("level6Info", 6),
          ("level7Debug", 7))
    )


_CcLoggingLevel_Type.__name__ = "Integer32"
_CcLoggingLevel_Object = MibScalar
ccLoggingLevel = _CcLoggingLevel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 11, 1),
    _CcLoggingLevel_Type()
)
ccLoggingLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLoggingLevel.setStatus("current")
_CcLoggingToSyslog_Type = TruthValue
_CcLoggingToSyslog_Object = MibScalar
ccLoggingToSyslog = _CcLoggingToSyslog_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 11, 2),
    _CcLoggingToSyslog_Type()
)
ccLoggingToSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLoggingToSyslog.setStatus("current")
_CcLoggingSyslogServer_Type = IpAddress
_CcLoggingSyslogServer_Object = MibScalar
ccLoggingSyslogServer = _CcLoggingSyslogServer_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 11, 3),
    _CcLoggingSyslogServer_Type()
)
ccLoggingSyslogServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLoggingSyslogServer.setStatus("current")
_CcLoggingDeleteCoreFile_Type = DoActionNow
_CcLoggingDeleteCoreFile_Object = MibScalar
ccLoggingDeleteCoreFile = _CcLoggingDeleteCoreFile_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 11, 4),
    _CcLoggingDeleteCoreFile_Type()
)
ccLoggingDeleteCoreFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLoggingDeleteCoreFile.setStatus("current")
_CcLoggingTransferCoreFile_Type = DoActionNow
_CcLoggingTransferCoreFile_Object = MibScalar
ccLoggingTransferCoreFile = _CcLoggingTransferCoreFile_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 11, 5),
    _CcLoggingTransferCoreFile_Type()
)
ccLoggingTransferCoreFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLoggingTransferCoreFile.setStatus("current")
_CcNtp_ObjectIdentity = ObjectIdentity
ccNtp = _CcNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 12)
)
_CcNtpEnable_Type = TruthValue
_CcNtpEnable_Object = MibScalar
ccNtpEnable = _CcNtpEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 12, 1),
    _CcNtpEnable_Type()
)
ccNtpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccNtpEnable.setStatus("current")
_CcNtp0Server_Type = IpAddress
_CcNtp0Server_Object = MibScalar
ccNtp0Server = _CcNtp0Server_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 12, 2),
    _CcNtp0Server_Type()
)
ccNtp0Server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccNtp0Server.setStatus("current")
_CcNtp0Port_Type = Integer32
_CcNtp0Port_Object = MibScalar
ccNtp0Port = _CcNtp0Port_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 12, 3),
    _CcNtp0Port_Type()
)
ccNtp0Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccNtp0Port.setStatus("current")
_CcNtp1Server_Type = IpAddress
_CcNtp1Server_Object = MibScalar
ccNtp1Server = _CcNtp1Server_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 12, 4),
    _CcNtp1Server_Type()
)
ccNtp1Server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccNtp1Server.setStatus("current")
_CcNtp1Port_Type = Integer32
_CcNtp1Port_Object = MibScalar
ccNtp1Port = _CcNtp1Port_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 12, 5),
    _CcNtp1Port_Type()
)
ccNtp1Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccNtp1Port.setStatus("current")
_CcNtp2Server_Type = IpAddress
_CcNtp2Server_Object = MibScalar
ccNtp2Server = _CcNtp2Server_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 12, 6),
    _CcNtp2Server_Type()
)
ccNtp2Server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccNtp2Server.setStatus("current")
_CcNtp2Port_Type = Integer32
_CcNtp2Port_Object = MibScalar
ccNtp2Port = _CcNtp2Port_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 12, 7),
    _CcNtp2Port_Type()
)
ccNtp2Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccNtp2Port.setStatus("current")
_CcNtpGmtHourOffset_Type = Integer32
_CcNtpGmtHourOffset_Object = MibScalar
ccNtpGmtHourOffset = _CcNtpGmtHourOffset_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 12, 8),
    _CcNtpGmtHourOffset_Type()
)
ccNtpGmtHourOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccNtpGmtHourOffset.setStatus("current")
_CcNtpGmtMinuteOffset_Type = Integer32
_CcNtpGmtMinuteOffset_Object = MibScalar
ccNtpGmtMinuteOffset = _CcNtpGmtMinuteOffset_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 12, 9),
    _CcNtpGmtMinuteOffset_Type()
)
ccNtpGmtMinuteOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccNtpGmtMinuteOffset.setStatus("current")
_CcNtpCurrentDateTime_Type = DateAndTime
_CcNtpCurrentDateTime_Object = MibScalar
ccNtpCurrentDateTime = _CcNtpCurrentDateTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 12, 10),
    _CcNtpCurrentDateTime_Type()
)
ccNtpCurrentDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccNtpCurrentDateTime.setStatus("current")
_CcNtpSyncInterval_Type = Integer32
_CcNtpSyncInterval_Object = MibScalar
ccNtpSyncInterval = _CcNtpSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 12, 11),
    _CcNtpSyncInterval_Type()
)
ccNtpSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccNtpSyncInterval.setStatus("current")
_CcDhcpOptions_ObjectIdentity = ObjectIdentity
ccDhcpOptions = _CcDhcpOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 14)
)
_CcDhcpOptionsUpdateFwEna_Type = TruthValue
_CcDhcpOptionsUpdateFwEna_Object = MibScalar
ccDhcpOptionsUpdateFwEna = _CcDhcpOptionsUpdateFwEna_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 14, 1),
    _CcDhcpOptionsUpdateFwEna_Type()
)
ccDhcpOptionsUpdateFwEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcpOptionsUpdateFwEna.setStatus("current")
_CcDhcpOptionsUpdateCfgEna_Type = TruthValue
_CcDhcpOptionsUpdateCfgEna_Object = MibScalar
ccDhcpOptionsUpdateCfgEna = _CcDhcpOptionsUpdateCfgEna_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 14, 2),
    _CcDhcpOptionsUpdateCfgEna_Type()
)
ccDhcpOptionsUpdateCfgEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcpOptionsUpdateCfgEna.setStatus("current")


class _CcDhcpOptionsUpdateInterface_Type(Integer32):
    """Custom type ccDhcpOptionsUpdateInterface based on Integer32"""
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
        *(("subnet1", 2),
          ("subnet2", 3),
          ("subnet3", 4),
          ("subnet4", 5),
          ("wan", 1))
    )


_CcDhcpOptionsUpdateInterface_Type.__name__ = "Integer32"
_CcDhcpOptionsUpdateInterface_Object = MibScalar
ccDhcpOptionsUpdateInterface = _CcDhcpOptionsUpdateInterface_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 14, 3),
    _CcDhcpOptionsUpdateInterface_Type()
)
ccDhcpOptionsUpdateInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccDhcpOptionsUpdateInterface.setStatus("current")
_CcDhcpOptionsUpdateFwFilename_Type = DisplayString
_CcDhcpOptionsUpdateFwFilename_Object = MibScalar
ccDhcpOptionsUpdateFwFilename = _CcDhcpOptionsUpdateFwFilename_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 14, 4),
    _CcDhcpOptionsUpdateFwFilename_Type()
)
ccDhcpOptionsUpdateFwFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcpOptionsUpdateFwFilename.setStatus("current")
_CcDhcpOptionsUpdateCfgFilename_Type = DisplayString
_CcDhcpOptionsUpdateCfgFilename_Object = MibScalar
ccDhcpOptionsUpdateCfgFilename = _CcDhcpOptionsUpdateCfgFilename_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 14, 5),
    _CcDhcpOptionsUpdateCfgFilename_Type()
)
ccDhcpOptionsUpdateCfgFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccDhcpOptionsUpdateCfgFilename.setStatus("current")
_CcRedundancy_ObjectIdentity = ObjectIdentity
ccRedundancy = _CcRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 15)
)


class _CcRedundancyAdminState_Type(Integer32):
    """Custom type ccRedundancyAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("standby", 2))
    )


_CcRedundancyAdminState_Type.__name__ = "Integer32"
_CcRedundancyAdminState_Object = MibScalar
ccRedundancyAdminState = _CcRedundancyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 15, 1),
    _CcRedundancyAdminState_Type()
)
ccRedundancyAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRedundancyAdminState.setStatus("current")


class _CcRedundancyOperState_Type(Integer32):
    """Custom type ccRedundancyOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("redundancy", 1),
          ("standAlone", 3),
          ("upgrade", 2))
    )


_CcRedundancyOperState_Type.__name__ = "Integer32"
_CcRedundancyOperState_Object = MibScalar
ccRedundancyOperState = _CcRedundancyOperState_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 15, 2),
    _CcRedundancyOperState_Type()
)
ccRedundancyOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRedundancyOperState.setStatus("current")


class _CcRedundancyHeartbeatInterface_Type(Integer32):
    """Custom type ccRedundancyHeartbeatInterface based on Integer32"""
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
        *(("port1", 1),
          ("port2", 2),
          ("port3", 3),
          ("port4", 4),
          ("port5", 5),
          ("port6", 6))
    )


_CcRedundancyHeartbeatInterface_Type.__name__ = "Integer32"
_CcRedundancyHeartbeatInterface_Object = MibScalar
ccRedundancyHeartbeatInterface = _CcRedundancyHeartbeatInterface_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 15, 3),
    _CcRedundancyHeartbeatInterface_Type()
)
ccRedundancyHeartbeatInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRedundancyHeartbeatInterface.setStatus("current")
_CcRedundancyHeartbeatInterval_Type = Unsigned32
_CcRedundancyHeartbeatInterval_Object = MibScalar
ccRedundancyHeartbeatInterval = _CcRedundancyHeartbeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 15, 4),
    _CcRedundancyHeartbeatInterval_Type()
)
ccRedundancyHeartbeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRedundancyHeartbeatInterval.setStatus("current")
if mibBuilder.loadTexts:
    ccRedundancyHeartbeatInterval.setUnits("seconds")
_CcRedundancyRevertDelay_Type = Unsigned32
_CcRedundancyRevertDelay_Object = MibScalar
ccRedundancyRevertDelay = _CcRedundancyRevertDelay_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 15, 5),
    _CcRedundancyRevertDelay_Type()
)
ccRedundancyRevertDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRedundancyRevertDelay.setStatus("current")
if mibBuilder.loadTexts:
    ccRedundancyRevertDelay.setUnits("minutes")
_CcRedundancyOperMode_Type = DisplayString
_CcRedundancyOperMode_Object = MibScalar
ccRedundancyOperMode = _CcRedundancyOperMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 15, 6),
    _CcRedundancyOperMode_Type()
)
ccRedundancyOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRedundancyOperMode.setStatus("current")
_CcCertMgnt_ObjectIdentity = ObjectIdentity
ccCertMgnt = _CcCertMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16)
)
_CcCertMgntSelfCerts_ObjectIdentity = ObjectIdentity
ccCertMgntSelfCerts = _CcCertMgntSelfCerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1)
)
_CcCertMgntSelfCertsReqTable_Object = MibTable
ccCertMgntSelfCertsReqTable = _CcCertMgntSelfCertsReqTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 1)
)
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsReqTable.setStatus("current")
_CcCertMgntSelfCertsReqEntry_Object = MibTableRow
ccCertMgntSelfCertsReqEntry = _CcCertMgntSelfCertsReqEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 1, 1)
)
ccCertMgntSelfCertsReqEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsReqIndex"),
)
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsReqEntry.setStatus("current")


class _CcCertMgntSelfCertsReqIndex_Type(Integer32):
    """Custom type ccCertMgntSelfCertsReqIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CcCertMgntSelfCertsReqIndex_Type.__name__ = "Integer32"
_CcCertMgntSelfCertsReqIndex_Object = MibTableColumn
ccCertMgntSelfCertsReqIndex = _CcCertMgntSelfCertsReqIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 1, 1, 1),
    _CcCertMgntSelfCertsReqIndex_Type()
)
ccCertMgntSelfCertsReqIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsReqIndex.setStatus("current")


class _CcCertMgntSelfCertsReqKeyId_Type(DisplayString):
    """Custom type ccCertMgntSelfCertsReqKeyId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 7),
    )


_CcCertMgntSelfCertsReqKeyId_Type.__name__ = "DisplayString"
_CcCertMgntSelfCertsReqKeyId_Object = MibTableColumn
ccCertMgntSelfCertsReqKeyId = _CcCertMgntSelfCertsReqKeyId_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 1, 1, 2),
    _CcCertMgntSelfCertsReqKeyId_Type()
)
ccCertMgntSelfCertsReqKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsReqKeyId.setStatus("current")


class _CcCertMgntSelfCertsReqSubject_Type(DisplayString):
    """Custom type ccCertMgntSelfCertsReqSubject based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 49),
    )


_CcCertMgntSelfCertsReqSubject_Type.__name__ = "DisplayString"
_CcCertMgntSelfCertsReqSubject_Object = MibTableColumn
ccCertMgntSelfCertsReqSubject = _CcCertMgntSelfCertsReqSubject_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 1, 1, 3),
    _CcCertMgntSelfCertsReqSubject_Type()
)
ccCertMgntSelfCertsReqSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsReqSubject.setStatus("current")


class _CcCertMgntSelfCertsReqDept_Type(DisplayString):
    """Custom type ccCertMgntSelfCertsReqDept based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_CcCertMgntSelfCertsReqDept_Type.__name__ = "DisplayString"
_CcCertMgntSelfCertsReqDept_Object = MibTableColumn
ccCertMgntSelfCertsReqDept = _CcCertMgntSelfCertsReqDept_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 1, 1, 4),
    _CcCertMgntSelfCertsReqDept_Type()
)
ccCertMgntSelfCertsReqDept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsReqDept.setStatus("current")


class _CcCertMgntSelfCertsReqOrg_Type(DisplayString):
    """Custom type ccCertMgntSelfCertsReqOrg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_CcCertMgntSelfCertsReqOrg_Type.__name__ = "DisplayString"
_CcCertMgntSelfCertsReqOrg_Object = MibTableColumn
ccCertMgntSelfCertsReqOrg = _CcCertMgntSelfCertsReqOrg_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 1, 1, 5),
    _CcCertMgntSelfCertsReqOrg_Type()
)
ccCertMgntSelfCertsReqOrg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsReqOrg.setStatus("current")


class _CcCertMgntSelfCertsReqCity_Type(DisplayString):
    """Custom type ccCertMgntSelfCertsReqCity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_CcCertMgntSelfCertsReqCity_Type.__name__ = "DisplayString"
_CcCertMgntSelfCertsReqCity_Object = MibTableColumn
ccCertMgntSelfCertsReqCity = _CcCertMgntSelfCertsReqCity_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 1, 1, 6),
    _CcCertMgntSelfCertsReqCity_Type()
)
ccCertMgntSelfCertsReqCity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsReqCity.setStatus("current")


class _CcCertMgntSelfCertsReqState_Type(DisplayString):
    """Custom type ccCertMgntSelfCertsReqState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_CcCertMgntSelfCertsReqState_Type.__name__ = "DisplayString"
_CcCertMgntSelfCertsReqState_Object = MibTableColumn
ccCertMgntSelfCertsReqState = _CcCertMgntSelfCertsReqState_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 1, 1, 7),
    _CcCertMgntSelfCertsReqState_Type()
)
ccCertMgntSelfCertsReqState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsReqState.setStatus("current")


class _CcCertMgntSelfCertsReqPostal_Type(DisplayString):
    """Custom type ccCertMgntSelfCertsReqPostal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_CcCertMgntSelfCertsReqPostal_Type.__name__ = "DisplayString"
_CcCertMgntSelfCertsReqPostal_Object = MibTableColumn
ccCertMgntSelfCertsReqPostal = _CcCertMgntSelfCertsReqPostal_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 1, 1, 8),
    _CcCertMgntSelfCertsReqPostal_Type()
)
ccCertMgntSelfCertsReqPostal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsReqPostal.setStatus("current")


class _CcCertMgntSelfCertsReqCountry_Type(DisplayString):
    """Custom type ccCertMgntSelfCertsReqCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_CcCertMgntSelfCertsReqCountry_Type.__name__ = "DisplayString"
_CcCertMgntSelfCertsReqCountry_Object = MibTableColumn
ccCertMgntSelfCertsReqCountry = _CcCertMgntSelfCertsReqCountry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 1, 1, 9),
    _CcCertMgntSelfCertsReqCountry_Type()
)
ccCertMgntSelfCertsReqCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsReqCountry.setStatus("current")


class _CcCertMgntSelfCertsReqEmail_Type(DisplayString):
    """Custom type ccCertMgntSelfCertsReqEmail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_CcCertMgntSelfCertsReqEmail_Type.__name__ = "DisplayString"
_CcCertMgntSelfCertsReqEmail_Object = MibTableColumn
ccCertMgntSelfCertsReqEmail = _CcCertMgntSelfCertsReqEmail_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 1, 1, 10),
    _CcCertMgntSelfCertsReqEmail_Type()
)
ccCertMgntSelfCertsReqEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsReqEmail.setStatus("current")


class _CcCertMgntSelfCertsReqDomain_Type(DisplayString):
    """Custom type ccCertMgntSelfCertsReqDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_CcCertMgntSelfCertsReqDomain_Type.__name__ = "DisplayString"
_CcCertMgntSelfCertsReqDomain_Object = MibTableColumn
ccCertMgntSelfCertsReqDomain = _CcCertMgntSelfCertsReqDomain_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 1, 1, 11),
    _CcCertMgntSelfCertsReqDomain_Type()
)
ccCertMgntSelfCertsReqDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsReqDomain.setStatus("current")
_CcCertMgntSelfCertsReqIp_Type = IpAddress
_CcCertMgntSelfCertsReqIp_Object = MibTableColumn
ccCertMgntSelfCertsReqIp = _CcCertMgntSelfCertsReqIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 1, 1, 12),
    _CcCertMgntSelfCertsReqIp_Type()
)
ccCertMgntSelfCertsReqIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsReqIp.setStatus("current")


class _CcCertMgntSelfCertsReqSigAlgo_Type(Integer32):
    """Custom type ccCertMgntSelfCertsReqSigAlgo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cryptoMd5Rsa", 1),
          ("cryptoSha1Rsa", 2))
    )


_CcCertMgntSelfCertsReqSigAlgo_Type.__name__ = "Integer32"
_CcCertMgntSelfCertsReqSigAlgo_Object = MibTableColumn
ccCertMgntSelfCertsReqSigAlgo = _CcCertMgntSelfCertsReqSigAlgo_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 1, 1, 13),
    _CcCertMgntSelfCertsReqSigAlgo_Type()
)
ccCertMgntSelfCertsReqSigAlgo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsReqSigAlgo.setStatus("current")


class _CcCertMgntSelfCertsReqKeyLen_Type(Integer32):
    """Custom type ccCertMgntSelfCertsReqKeyLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("keylen1024", 2),
          ("keylen2048", 3),
          ("keylen512", 1))
    )


_CcCertMgntSelfCertsReqKeyLen_Type.__name__ = "Integer32"
_CcCertMgntSelfCertsReqKeyLen_Object = MibTableColumn
ccCertMgntSelfCertsReqKeyLen = _CcCertMgntSelfCertsReqKeyLen_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 1, 1, 14),
    _CcCertMgntSelfCertsReqKeyLen_Type()
)
ccCertMgntSelfCertsReqKeyLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsReqKeyLen.setStatus("current")
_CcCertMgntSelfCertsReqGenReq_Type = DoActionShowProgress
_CcCertMgntSelfCertsReqGenReq_Object = MibTableColumn
ccCertMgntSelfCertsReqGenReq = _CcCertMgntSelfCertsReqGenReq_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 1, 1, 15),
    _CcCertMgntSelfCertsReqGenReq_Type()
)
ccCertMgntSelfCertsReqGenReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsReqGenReq.setStatus("current")
_CcCertMgntSelfCertsReqCertReqStr_Type = DisplayString
_CcCertMgntSelfCertsReqCertReqStr_Object = MibTableColumn
ccCertMgntSelfCertsReqCertReqStr = _CcCertMgntSelfCertsReqCertReqStr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 1, 1, 16),
    _CcCertMgntSelfCertsReqCertReqStr_Type()
)
ccCertMgntSelfCertsReqCertReqStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsReqCertReqStr.setStatus("current")
_CcCertMgntSelfCertsReqRowStatus_Type = AbbrevRowStatus
_CcCertMgntSelfCertsReqRowStatus_Object = MibTableColumn
ccCertMgntSelfCertsReqRowStatus = _CcCertMgntSelfCertsReqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 1, 1, 17),
    _CcCertMgntSelfCertsReqRowStatus_Type()
)
ccCertMgntSelfCertsReqRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsReqRowStatus.setStatus("current")
_CcCertMgntSelfCertsIdName_Type = DisplayString
_CcCertMgntSelfCertsIdName_Object = MibScalar
ccCertMgntSelfCertsIdName = _CcCertMgntSelfCertsIdName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 2),
    _CcCertMgntSelfCertsIdName_Type()
)
ccCertMgntSelfCertsIdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsIdName.setStatus("current")
_CcCertMgntSelfCertsSignedStr_Type = DisplayString
_CcCertMgntSelfCertsSignedStr_Object = MibScalar
ccCertMgntSelfCertsSignedStr = _CcCertMgntSelfCertsSignedStr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 3),
    _CcCertMgntSelfCertsSignedStr_Type()
)
ccCertMgntSelfCertsSignedStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsSignedStr.setStatus("current")
_CcCertMgntSelfCertsSignedImport_Type = DoActionShowProgress
_CcCertMgntSelfCertsSignedImport_Object = MibScalar
ccCertMgntSelfCertsSignedImport = _CcCertMgntSelfCertsSignedImport_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 4),
    _CcCertMgntSelfCertsSignedImport_Type()
)
ccCertMgntSelfCertsSignedImport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsSignedImport.setStatus("current")
_CcCertMgntSelfCertsSignedTable_Object = MibTable
ccCertMgntSelfCertsSignedTable = _CcCertMgntSelfCertsSignedTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 5)
)
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsSignedTable.setStatus("current")
_CcCertMgntSelfCertsSignedEntry_Object = MibTableRow
ccCertMgntSelfCertsSignedEntry = _CcCertMgntSelfCertsSignedEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 5, 1)
)
ccCertMgntSelfCertsSignedEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsSignedIndex"),
)
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsSignedEntry.setStatus("current")


class _CcCertMgntSelfCertsSignedIndex_Type(Integer32):
    """Custom type ccCertMgntSelfCertsSignedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CcCertMgntSelfCertsSignedIndex_Type.__name__ = "Integer32"
_CcCertMgntSelfCertsSignedIndex_Object = MibTableColumn
ccCertMgntSelfCertsSignedIndex = _CcCertMgntSelfCertsSignedIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 5, 1, 1),
    _CcCertMgntSelfCertsSignedIndex_Type()
)
ccCertMgntSelfCertsSignedIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsSignedIndex.setStatus("current")


class _CcCertMgntSelfCertsSignedKeyId_Type(DisplayString):
    """Custom type ccCertMgntSelfCertsSignedKeyId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 7),
    )


_CcCertMgntSelfCertsSignedKeyId_Type.__name__ = "DisplayString"
_CcCertMgntSelfCertsSignedKeyId_Object = MibTableColumn
ccCertMgntSelfCertsSignedKeyId = _CcCertMgntSelfCertsSignedKeyId_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 5, 1, 2),
    _CcCertMgntSelfCertsSignedKeyId_Type()
)
ccCertMgntSelfCertsSignedKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsSignedKeyId.setStatus("current")
_CcCertMgntSelfCertsSignedIssuerName_Type = DisplayString
_CcCertMgntSelfCertsSignedIssuerName_Object = MibTableColumn
ccCertMgntSelfCertsSignedIssuerName = _CcCertMgntSelfCertsSignedIssuerName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 5, 1, 3),
    _CcCertMgntSelfCertsSignedIssuerName_Type()
)
ccCertMgntSelfCertsSignedIssuerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsSignedIssuerName.setStatus("current")
_CcCertMgntSelfCertsSignedSubject_Type = DisplayString
_CcCertMgntSelfCertsSignedSubject_Object = MibTableColumn
ccCertMgntSelfCertsSignedSubject = _CcCertMgntSelfCertsSignedSubject_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 5, 1, 4),
    _CcCertMgntSelfCertsSignedSubject_Type()
)
ccCertMgntSelfCertsSignedSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsSignedSubject.setStatus("current")
_CcCertMgntSelfCertsSignedSerialNumber_Type = DisplayString
_CcCertMgntSelfCertsSignedSerialNumber_Object = MibTableColumn
ccCertMgntSelfCertsSignedSerialNumber = _CcCertMgntSelfCertsSignedSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 5, 1, 5),
    _CcCertMgntSelfCertsSignedSerialNumber_Type()
)
ccCertMgntSelfCertsSignedSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsSignedSerialNumber.setStatus("current")
_CcCertMgntSelfCertsSignedExpiry_Type = DateAndTime
_CcCertMgntSelfCertsSignedExpiry_Object = MibTableColumn
ccCertMgntSelfCertsSignedExpiry = _CcCertMgntSelfCertsSignedExpiry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 5, 1, 6),
    _CcCertMgntSelfCertsSignedExpiry_Type()
)
ccCertMgntSelfCertsSignedExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsSignedExpiry.setStatus("current")
_CcCertMgntSelfCertsSignedDeleteRow_Type = TruthValue
_CcCertMgntSelfCertsSignedDeleteRow_Object = MibTableColumn
ccCertMgntSelfCertsSignedDeleteRow = _CcCertMgntSelfCertsSignedDeleteRow_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 1, 5, 1, 7),
    _CcCertMgntSelfCertsSignedDeleteRow_Type()
)
ccCertMgntSelfCertsSignedDeleteRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCertMgntSelfCertsSignedDeleteRow.setStatus("current")
_CcCACerts_ObjectIdentity = ObjectIdentity
ccCACerts = _CcCACerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 2)
)
_CcCACertsStr_Type = DisplayString
_CcCACertsStr_Object = MibScalar
ccCACertsStr = _CcCACertsStr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 2, 1),
    _CcCACertsStr_Type()
)
ccCACertsStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCACertsStr.setStatus("current")
_CcCACertsImport_Type = DoActionShowProgress
_CcCACertsImport_Object = MibScalar
ccCACertsImport = _CcCACertsImport_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 2, 2),
    _CcCACertsImport_Type()
)
ccCACertsImport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCACertsImport.setStatus("current")
_CcCACertsTable_Object = MibTable
ccCACertsTable = _CcCACertsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 2, 3)
)
if mibBuilder.loadTexts:
    ccCACertsTable.setStatus("current")
_CcCACertsEntry_Object = MibTableRow
ccCACertsEntry = _CcCACertsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 2, 3, 1)
)
ccCACertsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccCACertsIndex"),
)
if mibBuilder.loadTexts:
    ccCACertsEntry.setStatus("current")


class _CcCACertsIndex_Type(Integer32):
    """Custom type ccCACertsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CcCACertsIndex_Type.__name__ = "Integer32"
_CcCACertsIndex_Object = MibTableColumn
ccCACertsIndex = _CcCACertsIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 2, 3, 1, 1),
    _CcCACertsIndex_Type()
)
ccCACertsIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccCACertsIndex.setStatus("current")


class _CcCACertsKeyId_Type(DisplayString):
    """Custom type ccCACertsKeyId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 7),
    )


_CcCACertsKeyId_Type.__name__ = "DisplayString"
_CcCACertsKeyId_Object = MibTableColumn
ccCACertsKeyId = _CcCACertsKeyId_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 2, 3, 1, 2),
    _CcCACertsKeyId_Type()
)
ccCACertsKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCACertsKeyId.setStatus("current")
_CcCACertsIssuerName_Type = DisplayString
_CcCACertsIssuerName_Object = MibTableColumn
ccCACertsIssuerName = _CcCACertsIssuerName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 2, 3, 1, 3),
    _CcCACertsIssuerName_Type()
)
ccCACertsIssuerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCACertsIssuerName.setStatus("current")
_CcCACertsSubject_Type = DisplayString
_CcCACertsSubject_Object = MibTableColumn
ccCACertsSubject = _CcCACertsSubject_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 2, 3, 1, 4),
    _CcCACertsSubject_Type()
)
ccCACertsSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCACertsSubject.setStatus("current")
_CcCACertsSerialNumber_Type = DisplayString
_CcCACertsSerialNumber_Object = MibTableColumn
ccCACertsSerialNumber = _CcCACertsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 2, 3, 1, 5),
    _CcCACertsSerialNumber_Type()
)
ccCACertsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCACertsSerialNumber.setStatus("current")
_CcCACertsExpiry_Type = DateAndTime
_CcCACertsExpiry_Object = MibTableColumn
ccCACertsExpiry = _CcCACertsExpiry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 2, 3, 1, 6),
    _CcCACertsExpiry_Type()
)
ccCACertsExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccCACertsExpiry.setStatus("current")
_CcCACertsDeleteRow_Type = TruthValue
_CcCACertsDeleteRow_Object = MibTableColumn
ccCACertsDeleteRow = _CcCACertsDeleteRow_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 2, 16, 2, 3, 1, 7),
    _CcCACertsDeleteRow_Type()
)
ccCACertsDeleteRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccCACertsDeleteRow.setStatus("current")
_CcNotifications_ObjectIdentity = ObjectIdentity
ccNotifications = _CcNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3)
)
_CcTrapCtrl_ObjectIdentity = ObjectIdentity
ccTrapCtrl = _CcTrapCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000)
)
_CcTrapCtrlEnableTable_Object = MibTable
ccTrapCtrlEnableTable = _CcTrapCtrlEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 1)
)
if mibBuilder.loadTexts:
    ccTrapCtrlEnableTable.setStatus("current")
_CcTrapCtrlEnableEntry_Object = MibTableRow
ccTrapCtrlEnableEntry = _CcTrapCtrlEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 1, 1)
)
ccTrapCtrlEnableEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccTrapCtrlEnableIndex"),
)
if mibBuilder.loadTexts:
    ccTrapCtrlEnableEntry.setStatus("current")


class _CcTrapCtrlEnableIndex_Type(Integer32):
    """Custom type ccTrapCtrlEnableIndex based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("trapCtrlCfAlmostFull", 11),
          ("trapCtrlDenialofService", 13),
          ("trapCtrlMuAssociated", 4),
          ("trapCtrlMuAuthDenied", 14),
          ("trapCtrlMuDeniedAssociation", 6),
          ("trapCtrlMuUnAssociated", 5),
          ("trapCtrlPortStatusChange", 12),
          ("trapCtrlPortalAdopted", 1),
          ("trapCtrlPortalDeniedAdoption", 3),
          ("trapCtrlPortalUnAdopted", 2),
          ("trapCtrlRadarDetected", 15),
          ("trapCtrlRogueApDetected", 16),
          ("trapCtrlSnmpAclViolation", 8),
          ("trapCtrlSnmpAuthFailure", 7),
          ("trapCtrlSnmpColdStart", 9),
          ("trapCtrlSnmpConfigChanged", 10))
    )


_CcTrapCtrlEnableIndex_Type.__name__ = "Integer32"
_CcTrapCtrlEnableIndex_Object = MibTableColumn
ccTrapCtrlEnableIndex = _CcTrapCtrlEnableIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 1, 1, 1),
    _CcTrapCtrlEnableIndex_Type()
)
ccTrapCtrlEnableIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccTrapCtrlEnableIndex.setStatus("current")
_CcTrapCtrlEnableName_Type = DisplayString
_CcTrapCtrlEnableName_Object = MibTableColumn
ccTrapCtrlEnableName = _CcTrapCtrlEnableName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 1, 1, 2),
    _CcTrapCtrlEnableName_Type()
)
ccTrapCtrlEnableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccTrapCtrlEnableName.setStatus("current")
_CcTrapCtrlEnable_Type = TruthValue
_CcTrapCtrlEnable_Object = MibTableColumn
ccTrapCtrlEnable = _CcTrapCtrlEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 1, 1, 3),
    _CcTrapCtrlEnable_Type()
)
ccTrapCtrlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapCtrlEnable.setStatus("current")
_CcTrapCtrlDetails_ObjectIdentity = ObjectIdentity
ccTrapCtrlDetails = _CcTrapCtrlDetails_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2)
)
_CcTrapCtrlPortalAdopted_ObjectIdentity = ObjectIdentity
ccTrapCtrlPortalAdopted = _CcTrapCtrlPortalAdopted_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 1)
)
if mibBuilder.loadTexts:
    ccTrapCtrlPortalAdopted.setStatus("current")
_CcTrapCtrlPortalUnAdopted_ObjectIdentity = ObjectIdentity
ccTrapCtrlPortalUnAdopted = _CcTrapCtrlPortalUnAdopted_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 2)
)
if mibBuilder.loadTexts:
    ccTrapCtrlPortalUnAdopted.setStatus("current")
_CcTrapCtrlPortalDenied_ObjectIdentity = ObjectIdentity
ccTrapCtrlPortalDenied = _CcTrapCtrlPortalDenied_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 3)
)
if mibBuilder.loadTexts:
    ccTrapCtrlPortalDenied.setStatus("current")
_CcTrapCtrlMuAssociated_ObjectIdentity = ObjectIdentity
ccTrapCtrlMuAssociated = _CcTrapCtrlMuAssociated_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 4)
)
if mibBuilder.loadTexts:
    ccTrapCtrlMuAssociated.setStatus("current")
_CcTrapCtrlMuUnAssociated_ObjectIdentity = ObjectIdentity
ccTrapCtrlMuUnAssociated = _CcTrapCtrlMuUnAssociated_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 5)
)
if mibBuilder.loadTexts:
    ccTrapCtrlMuUnAssociated.setStatus("current")
_CcTrapCtrlMuDenied_ObjectIdentity = ObjectIdentity
ccTrapCtrlMuDenied = _CcTrapCtrlMuDenied_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 6)
)
if mibBuilder.loadTexts:
    ccTrapCtrlMuDenied.setStatus("current")
_CcTrapCtrlConfigChange_ObjectIdentity = ObjectIdentity
ccTrapCtrlConfigChange = _CcTrapCtrlConfigChange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 7)
)
if mibBuilder.loadTexts:
    ccTrapCtrlConfigChange.setStatus("current")
_CcTrapCtrlSnmpAclViolation_ObjectIdentity = ObjectIdentity
ccTrapCtrlSnmpAclViolation = _CcTrapCtrlSnmpAclViolation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 8)
)
if mibBuilder.loadTexts:
    ccTrapCtrlSnmpAclViolation.setStatus("current")
_CcTrapCtrlPortStatusChange_ObjectIdentity = ObjectIdentity
ccTrapCtrlPortStatusChange = _CcTrapCtrlPortStatusChange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 9)
)
if mibBuilder.loadTexts:
    ccTrapCtrlPortStatusChange.setStatus("current")
_CcTrapCtrlCfAlmostFull_ObjectIdentity = ObjectIdentity
ccTrapCtrlCfAlmostFull = _CcTrapCtrlCfAlmostFull_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 10)
)
_CcTrapCtrlCfAlmostFullThreshold_Type = Unsigned32
_CcTrapCtrlCfAlmostFullThreshold_Object = MibScalar
ccTrapCtrlCfAlmostFullThreshold = _CcTrapCtrlCfAlmostFullThreshold_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 10, 1),
    _CcTrapCtrlCfAlmostFullThreshold_Type()
)
ccTrapCtrlCfAlmostFullThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapCtrlCfAlmostFullThreshold.setStatus("current")
_CcTrapCtrlFirewallUnderAttack_ObjectIdentity = ObjectIdentity
ccTrapCtrlFirewallUnderAttack = _CcTrapCtrlFirewallUnderAttack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 11)
)


class _CcTrapCtrlFirewallUnderAttackDescription_Type(OctetString):
    """Custom type ccTrapCtrlFirewallUnderAttackDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CcTrapCtrlFirewallUnderAttackDescription_Type.__name__ = "OctetString"
_CcTrapCtrlFirewallUnderAttackDescription_Object = MibScalar
ccTrapCtrlFirewallUnderAttackDescription = _CcTrapCtrlFirewallUnderAttackDescription_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 11, 1),
    _CcTrapCtrlFirewallUnderAttackDescription_Type()
)
ccTrapCtrlFirewallUnderAttackDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccTrapCtrlFirewallUnderAttackDescription.setStatus("current")
_CcTrapCtrlFirewallUnderAttackRateLimit_Type = Unsigned32
_CcTrapCtrlFirewallUnderAttackRateLimit_Object = MibScalar
ccTrapCtrlFirewallUnderAttackRateLimit = _CcTrapCtrlFirewallUnderAttackRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 11, 2),
    _CcTrapCtrlFirewallUnderAttackRateLimit_Type()
)
ccTrapCtrlFirewallUnderAttackRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapCtrlFirewallUnderAttackRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    ccTrapCtrlFirewallUnderAttackRateLimit.setUnits("seconds")
_CcTrapCtrlRadarDetected_ObjectIdentity = ObjectIdentity
ccTrapCtrlRadarDetected = _CcTrapCtrlRadarDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 12)
)
_CcTrapCtrlRadarDetectedPortalMac_Type = PhysAddress
_CcTrapCtrlRadarDetectedPortalMac_Object = MibScalar
ccTrapCtrlRadarDetectedPortalMac = _CcTrapCtrlRadarDetectedPortalMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 12, 1),
    _CcTrapCtrlRadarDetectedPortalMac_Type()
)
ccTrapCtrlRadarDetectedPortalMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccTrapCtrlRadarDetectedPortalMac.setStatus("current")
_CcTrapCtrlRadarDetectedChannel_Type = Unsigned32
_CcTrapCtrlRadarDetectedChannel_Object = MibScalar
ccTrapCtrlRadarDetectedChannel = _CcTrapCtrlRadarDetectedChannel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 12, 2),
    _CcTrapCtrlRadarDetectedChannel_Type()
)
ccTrapCtrlRadarDetectedChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccTrapCtrlRadarDetectedChannel.setStatus("current")
_CcTrapCtrlSumStats_ObjectIdentity = ObjectIdentity
ccTrapCtrlSumStats = _CcTrapCtrlSumStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 13)
)
_CcTrapCtrlSumStatsTable_Object = MibTable
ccTrapCtrlSumStatsTable = _CcTrapCtrlSumStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 13, 1)
)
if mibBuilder.loadTexts:
    ccTrapCtrlSumStatsTable.setStatus("current")
_CcTrapCtrlSumStatsEntry_Object = MibTableRow
ccTrapCtrlSumStatsEntry = _CcTrapCtrlSumStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 13, 1, 1)
)
ccTrapCtrlSumStatsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsIndex"),
)
if mibBuilder.loadTexts:
    ccTrapCtrlSumStatsEntry.setStatus("current")


class _CcTrapCtrlSumStatsIndex_Type(Integer32):
    """Custom type ccTrapCtrlSumStatsIndex based on Integer32"""
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("thresholdsAvgBitSpeed", 9),
          ("thresholdsAvgMuNoise", 11),
          ("thresholdsAvgMuSignal", 10),
          ("thresholdsAvgMuSnr", 12),
          ("thresholdsPctDropped", 20),
          ("thresholdsPctNUcastPkts", 13),
          ("thresholdsPctRfUtil", 19),
          ("thresholdsPktsPerSec", 3),
          ("thresholdsPpmRxUndecrypt", 17),
          ("thresholdsPpmTxDropped", 15),
          ("thresholdsPpmTxWithRetires", 14),
          ("thresholdsThroughput", 6),
          ("thresholdsTotalMus", 18),
          ("thresholdsTxAvgRetries", 16),
          ("unusedNumPkts", 2),
          ("unusedPktsPerSecRx", 5),
          ("unusedPktsPerSecTx", 4),
          ("unusedThroughputRx", 8),
          ("unusedThroughputTx", 7),
          ("unusedTimestamp", 1))
    )


_CcTrapCtrlSumStatsIndex_Type.__name__ = "Integer32"
_CcTrapCtrlSumStatsIndex_Object = MibTableColumn
ccTrapCtrlSumStatsIndex = _CcTrapCtrlSumStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 13, 1, 1, 1),
    _CcTrapCtrlSumStatsIndex_Type()
)
ccTrapCtrlSumStatsIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccTrapCtrlSumStatsIndex.setStatus("current")
_CcTrapCtrlSumStatsDescr_Type = DisplayString
_CcTrapCtrlSumStatsDescr_Object = MibTableColumn
ccTrapCtrlSumStatsDescr = _CcTrapCtrlSumStatsDescr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 13, 1, 1, 2),
    _CcTrapCtrlSumStatsDescr_Type()
)
ccTrapCtrlSumStatsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccTrapCtrlSumStatsDescr.setStatus("current")
_CcTrapCtrlSumStatsUnits_Type = DisplayString
_CcTrapCtrlSumStatsUnits_Object = MibTableColumn
ccTrapCtrlSumStatsUnits = _CcTrapCtrlSumStatsUnits_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 13, 1, 1, 3),
    _CcTrapCtrlSumStatsUnits_Type()
)
ccTrapCtrlSumStatsUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccTrapCtrlSumStatsUnits.setStatus("current")
_CcTrapCtrlSumStatsCanBeSetMu_Type = TruthValue
_CcTrapCtrlSumStatsCanBeSetMu_Object = MibTableColumn
ccTrapCtrlSumStatsCanBeSetMu = _CcTrapCtrlSumStatsCanBeSetMu_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 13, 1, 1, 4),
    _CcTrapCtrlSumStatsCanBeSetMu_Type()
)
ccTrapCtrlSumStatsCanBeSetMu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccTrapCtrlSumStatsCanBeSetMu.setStatus("current")
_CcTrapCtrlSumStatsThresholdMu_Type = Unsigned32
_CcTrapCtrlSumStatsThresholdMu_Object = MibTableColumn
ccTrapCtrlSumStatsThresholdMu = _CcTrapCtrlSumStatsThresholdMu_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 13, 1, 1, 5),
    _CcTrapCtrlSumStatsThresholdMu_Type()
)
ccTrapCtrlSumStatsThresholdMu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapCtrlSumStatsThresholdMu.setStatus("current")
_CcTrapCtrlSumStatsCanBeSetPortal_Type = TruthValue
_CcTrapCtrlSumStatsCanBeSetPortal_Object = MibTableColumn
ccTrapCtrlSumStatsCanBeSetPortal = _CcTrapCtrlSumStatsCanBeSetPortal_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 13, 1, 1, 6),
    _CcTrapCtrlSumStatsCanBeSetPortal_Type()
)
ccTrapCtrlSumStatsCanBeSetPortal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccTrapCtrlSumStatsCanBeSetPortal.setStatus("current")
_CcTrapCtrlSumStatsThresholdPortals_Type = Unsigned32
_CcTrapCtrlSumStatsThresholdPortals_Object = MibTableColumn
ccTrapCtrlSumStatsThresholdPortals = _CcTrapCtrlSumStatsThresholdPortals_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 13, 1, 1, 7),
    _CcTrapCtrlSumStatsThresholdPortals_Type()
)
ccTrapCtrlSumStatsThresholdPortals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapCtrlSumStatsThresholdPortals.setStatus("current")
_CcTrapCtrlSumStatsCanBeSetWlan_Type = TruthValue
_CcTrapCtrlSumStatsCanBeSetWlan_Object = MibTableColumn
ccTrapCtrlSumStatsCanBeSetWlan = _CcTrapCtrlSumStatsCanBeSetWlan_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 13, 1, 1, 8),
    _CcTrapCtrlSumStatsCanBeSetWlan_Type()
)
ccTrapCtrlSumStatsCanBeSetWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccTrapCtrlSumStatsCanBeSetWlan.setStatus("current")
_CcTrapCtrlSumStatsThresholdWlans_Type = Unsigned32
_CcTrapCtrlSumStatsThresholdWlans_Object = MibTableColumn
ccTrapCtrlSumStatsThresholdWlans = _CcTrapCtrlSumStatsThresholdWlans_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 13, 1, 1, 9),
    _CcTrapCtrlSumStatsThresholdWlans_Type()
)
ccTrapCtrlSumStatsThresholdWlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapCtrlSumStatsThresholdWlans.setStatus("current")
_CcTrapCtrlSumStatsCanBeSetSwitch_Type = TruthValue
_CcTrapCtrlSumStatsCanBeSetSwitch_Object = MibTableColumn
ccTrapCtrlSumStatsCanBeSetSwitch = _CcTrapCtrlSumStatsCanBeSetSwitch_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 13, 1, 1, 10),
    _CcTrapCtrlSumStatsCanBeSetSwitch_Type()
)
ccTrapCtrlSumStatsCanBeSetSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccTrapCtrlSumStatsCanBeSetSwitch.setStatus("current")
_CcTrapCtrlSumStatsThresholdSwitch_Type = Unsigned32
_CcTrapCtrlSumStatsThresholdSwitch_Object = MibTableColumn
ccTrapCtrlSumStatsThresholdSwitch = _CcTrapCtrlSumStatsThresholdSwitch_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 13, 1, 1, 11),
    _CcTrapCtrlSumStatsThresholdSwitch_Type()
)
ccTrapCtrlSumStatsThresholdSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapCtrlSumStatsThresholdSwitch.setStatus("current")
_CcTrapCtrlSumStatsMinPktsForTrap_Type = Unsigned32
_CcTrapCtrlSumStatsMinPktsForTrap_Object = MibScalar
ccTrapCtrlSumStatsMinPktsForTrap = _CcTrapCtrlSumStatsMinPktsForTrap_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 13, 2),
    _CcTrapCtrlSumStatsMinPktsForTrap_Type()
)
ccTrapCtrlSumStatsMinPktsForTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrapCtrlSumStatsMinPktsForTrap.setStatus("current")
_CcTrapCtrlSumStatsPortal_ObjectIdentity = ObjectIdentity
ccTrapCtrlSumStatsPortal = _CcTrapCtrlSumStatsPortal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 14)
)
if mibBuilder.loadTexts:
    ccTrapCtrlSumStatsPortal.setStatus("current")
_CcTrapCtrlSumStatsWlan_ObjectIdentity = ObjectIdentity
ccTrapCtrlSumStatsWlan = _CcTrapCtrlSumStatsWlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 15)
)
if mibBuilder.loadTexts:
    ccTrapCtrlSumStatsWlan.setStatus("current")
_CcTrapCtrlSumStatsSwitch_ObjectIdentity = ObjectIdentity
ccTrapCtrlSumStatsSwitch = _CcTrapCtrlSumStatsSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 16)
)
if mibBuilder.loadTexts:
    ccTrapCtrlSumStatsSwitch.setStatus("current")
_CcTrapCtrlLanVlanActivated_ObjectIdentity = ObjectIdentity
ccTrapCtrlLanVlanActivated = _CcTrapCtrlLanVlanActivated_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 17)
)


class _CcTrapCtrlLanVlanActivatedVlanId_Type(Unsigned32):
    """Custom type ccTrapCtrlLanVlanActivatedVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_CcTrapCtrlLanVlanActivatedVlanId_Type.__name__ = "Unsigned32"
_CcTrapCtrlLanVlanActivatedVlanId_Object = MibScalar
ccTrapCtrlLanVlanActivatedVlanId = _CcTrapCtrlLanVlanActivatedVlanId_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 17, 1),
    _CcTrapCtrlLanVlanActivatedVlanId_Type()
)
ccTrapCtrlLanVlanActivatedVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccTrapCtrlLanVlanActivatedVlanId.setStatus("current")
_CcTrapCtrlDhcpOptionsFileTransferStatus_ObjectIdentity = ObjectIdentity
ccTrapCtrlDhcpOptionsFileTransferStatus = _CcTrapCtrlDhcpOptionsFileTransferStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 18)
)


class _CcTrapCtrlDhcpOptionsFileTransferStatusRequested_Type(Bits):
    """Custom type ccTrapCtrlDhcpOptionsFileTransferStatusRequested based on Bits"""
    namedValues = NamedValues(
        *(("dhcpRequestedCfgLoad", 1),
          ("dhcpRequestedFwLoad", 0))
    )

_CcTrapCtrlDhcpOptionsFileTransferStatusRequested_Type.__name__ = "Bits"
_CcTrapCtrlDhcpOptionsFileTransferStatusRequested_Object = MibScalar
ccTrapCtrlDhcpOptionsFileTransferStatusRequested = _CcTrapCtrlDhcpOptionsFileTransferStatusRequested_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 18, 1),
    _CcTrapCtrlDhcpOptionsFileTransferStatusRequested_Type()
)
ccTrapCtrlDhcpOptionsFileTransferStatusRequested.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccTrapCtrlDhcpOptionsFileTransferStatusRequested.setStatus("current")
_CcTrapCtrlRedundancyStateChange_ObjectIdentity = ObjectIdentity
ccTrapCtrlRedundancyStateChange = _CcTrapCtrlRedundancyStateChange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 19)
)


class _CcTrapCtrlRedundancyPreviousOperState_Type(Integer32):
    """Custom type ccTrapCtrlRedundancyPreviousOperState based on Integer32"""
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
        *(("redundantPrimary", 2),
          ("redundantStandby", 3),
          ("redundantUpgrade", 4),
          ("standAlone", 1))
    )


_CcTrapCtrlRedundancyPreviousOperState_Type.__name__ = "Integer32"
_CcTrapCtrlRedundancyPreviousOperState_Object = MibScalar
ccTrapCtrlRedundancyPreviousOperState = _CcTrapCtrlRedundancyPreviousOperState_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1000, 2, 19, 1),
    _CcTrapCtrlRedundancyPreviousOperState_Type()
)
ccTrapCtrlRedundancyPreviousOperState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccTrapCtrlRedundancyPreviousOperState.setStatus("current")
_CcRf_ObjectIdentity = ObjectIdentity
ccRf = _CcRf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4)
)
_CcAp_ObjectIdentity = ObjectIdentity
ccAp = _CcAp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 1)
)
_CcApTable_Object = MibTable
ccApTable = _CcApTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    ccApTable.setStatus("current")
_CcApEntry_Object = MibTableRow
ccApEntry = _CcApEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 1, 1, 1)
)
ccApEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccApIndex"),
)
if mibBuilder.loadTexts:
    ccApEntry.setStatus("current")


class _CcApIndex_Type(Integer32):
    """Custom type ccApIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CcApIndex_Type.__name__ = "Integer32"
_CcApIndex_Object = MibTableColumn
ccApIndex = _CcApIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 1, 1, 1, 1),
    _CcApIndex_Type()
)
ccApIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccApIndex.setStatus("current")
_CcApNicMac_Type = PhysAddress
_CcApNicMac_Object = MibTableColumn
ccApNicMac = _CcApNicMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 1, 1, 1, 2),
    _CcApNicMac_Type()
)
ccApNicMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccApNicMac.setStatus("current")
_CcApModelNumber_Type = DisplayString
_CcApModelNumber_Object = MibTableColumn
ccApModelNumber = _CcApModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 1, 1, 1, 3),
    _CcApModelNumber_Type()
)
ccApModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccApModelNumber.setStatus("current")
_CcApSerialNumber_Type = DisplayString
_CcApSerialNumber_Object = MibTableColumn
ccApSerialNumber = _CcApSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 1, 1, 1, 4),
    _CcApSerialNumber_Type()
)
ccApSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccApSerialNumber.setStatus("current")
_CcApPcbRevision_Type = DisplayString
_CcApPcbRevision_Object = MibTableColumn
ccApPcbRevision = _CcApPcbRevision_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 1, 1, 1, 5),
    _CcApPcbRevision_Type()
)
ccApPcbRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccApPcbRevision.setStatus("current")
_CcApBootLoaderRev_Type = DisplayString
_CcApBootLoaderRev_Object = MibTableColumn
ccApBootLoaderRev = _CcApBootLoaderRev_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 1, 1, 1, 6),
    _CcApBootLoaderRev_Type()
)
ccApBootLoaderRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccApBootLoaderRev.setStatus("current")
_CcApWispVersion_Type = DisplayString
_CcApWispVersion_Object = MibTableColumn
ccApWispVersion = _CcApWispVersion_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 1, 1, 1, 7),
    _CcApWispVersion_Type()
)
ccApWispVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccApWispVersion.setStatus("current")
_CcApRuntimeFwVersion_Type = DisplayString
_CcApRuntimeFwVersion_Object = MibTableColumn
ccApRuntimeFwVersion = _CcApRuntimeFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 1, 1, 1, 8),
    _CcApRuntimeFwVersion_Type()
)
ccApRuntimeFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccApRuntimeFwVersion.setStatus("current")
_CcApNumPortals_Type = Unsigned32
_CcApNumPortals_Object = MibTableColumn
ccApNumPortals = _CcApNumPortals_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 1, 1, 1, 9),
    _CcApNumPortals_Type()
)
ccApNumPortals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccApNumPortals.setStatus("current")
_CcApPointersToPortals_Type = MultiPointer255
_CcApPointersToPortals_Object = MibTableColumn
ccApPointersToPortals = _CcApPointersToPortals_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 1, 1, 1, 10),
    _CcApPointersToPortals_Type()
)
ccApPointersToPortals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccApPointersToPortals.setStatus("current")
_CcPortal_ObjectIdentity = ObjectIdentity
ccPortal = _CcPortal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2)
)
_CcPortalTable_Object = MibTable
ccPortalTable = _CcPortalTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    ccPortalTable.setStatus("current")
_CcPortalEntry_Object = MibTableRow
ccPortalEntry = _CcPortalEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 1, 1)
)
ccPortalEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    ccPortalEntry.setStatus("current")


class _CcPortalIndex_Type(Integer32):
    """Custom type ccPortalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CcPortalIndex_Type.__name__ = "Integer32"
_CcPortalIndex_Object = MibTableColumn
ccPortalIndex = _CcPortalIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 1, 1, 1),
    _CcPortalIndex_Type()
)
ccPortalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccPortalIndex.setStatus("current")
_CcPortalPointerToAp_Type = SinglePointer
_CcPortalPointerToAp_Object = MibTableColumn
ccPortalPointerToAp = _CcPortalPointerToAp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 1, 1, 2),
    _CcPortalPointerToAp_Type()
)
ccPortalPointerToAp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalPointerToAp.setStatus("current")
_CcPortalPointersToWlans_Type = MultiPointer63
_CcPortalPointersToWlans_Object = MibTableColumn
ccPortalPointersToWlans = _CcPortalPointersToWlans_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 1, 1, 3),
    _CcPortalPointersToWlans_Type()
)
ccPortalPointersToWlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalPointersToWlans.setStatus("current")
_CcPortalName_Type = DisplayString
_CcPortalName_Object = MibTableColumn
ccPortalName = _CcPortalName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 1, 1, 4),
    _CcPortalName_Type()
)
ccPortalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalName.setStatus("current")
_CcPortalLocation_Type = DisplayString
_CcPortalLocation_Object = MibTableColumn
ccPortalLocation = _CcPortalLocation_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 1, 1, 5),
    _CcPortalLocation_Type()
)
ccPortalLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalLocation.setStatus("current")


class _CcPortalOptions_Type(Bits):
    """Custom type ccPortalOptions based on Bits"""
    namedValues = NamedValues(
        *(("externalPrimaryAntInstalled", 14),
          ("externalSecondaryAntInstalled", 12),
          ("internalPrimaryAntInstalled", 15),
          ("internalSecondaryAntInstalled", 13),
          ("undefined00", 0),
          ("undefined01", 1),
          ("undefined02", 2),
          ("undefined03", 3),
          ("undefined04", 4),
          ("undefined05", 5),
          ("undefined06", 6),
          ("undefined07", 7),
          ("undefined08", 8),
          ("undefined09", 9),
          ("undefined10", 10),
          ("undefined11", 11))
    )

_CcPortalOptions_Type.__name__ = "Bits"
_CcPortalOptions_Object = MibTableColumn
ccPortalOptions = _CcPortalOptions_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 1, 1, 6),
    _CcPortalOptions_Type()
)
ccPortalOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalOptions.setStatus("current")
_CcPortalMac_Type = PhysAddress
_CcPortalMac_Object = MibTableColumn
ccPortalMac = _CcPortalMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 1, 1, 7),
    _CcPortalMac_Type()
)
ccPortalMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalMac.setStatus("current")
_CcPortalNumberOfEss_Type = Integer32
_CcPortalNumberOfEss_Object = MibTableColumn
ccPortalNumberOfEss = _CcPortalNumberOfEss_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 1, 1, 8),
    _CcPortalNumberOfEss_Type()
)
ccPortalNumberOfEss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalNumberOfEss.setStatus("current")
_CcPortalNumberOfBss_Type = Integer32
_CcPortalNumberOfBss_Object = MibTableColumn
ccPortalNumberOfBss = _CcPortalNumberOfBss_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 1, 1, 9),
    _CcPortalNumberOfBss_Type()
)
ccPortalNumberOfBss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalNumberOfBss.setStatus("current")
_CcPortalAssociatedMus_Type = Integer32
_CcPortalAssociatedMus_Object = MibTableColumn
ccPortalAssociatedMus = _CcPortalAssociatedMus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 1, 1, 10),
    _CcPortalAssociatedMus_Type()
)
ccPortalAssociatedMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalAssociatedMus.setStatus("current")
_CcPortalRadioType_Type = RadioType
_CcPortalRadioType_Object = MibTableColumn
ccPortalRadioType = _CcPortalRadioType_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 1, 1, 11),
    _CcPortalRadioType_Type()
)
ccPortalRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRadioType.setStatus("current")


class _CcPortalChannel_Type(Integer32):
    """Custom type ccPortalChannel based on Integer32"""
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
              36,
              40,
              44,
              48,
              52,
              56,
              60,
              64,
              149,
              153,
              157,
              161)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot11aChannel036", 36),
          ("ieee802dot11aChannel040", 40),
          ("ieee802dot11aChannel044", 44),
          ("ieee802dot11aChannel048", 48),
          ("ieee802dot11aChannel052", 52),
          ("ieee802dot11aChannel056", 56),
          ("ieee802dot11aChannel060", 60),
          ("ieee802dot11aChannel064", 64),
          ("ieee802dot11aChannel149", 149),
          ("ieee802dot11aChannel153", 153),
          ("ieee802dot11aChannel157", 157),
          ("ieee802dot11aChannel161", 161),
          ("ieee802dot11bChannel01", 1),
          ("ieee802dot11bChannel02", 2),
          ("ieee802dot11bChannel03", 3),
          ("ieee802dot11bChannel04", 4),
          ("ieee802dot11bChannel05", 5),
          ("ieee802dot11bChannel06", 6),
          ("ieee802dot11bChannel07", 7),
          ("ieee802dot11bChannel08", 8),
          ("ieee802dot11bChannel09", 9),
          ("ieee802dot11bChannel10", 10),
          ("ieee802dot11bChannel11", 11),
          ("ieee802dot11bChannel12", 12),
          ("ieee802dot11bChannel13", 13),
          ("ieee802dot11bChannel14", 14))
    )


_CcPortalChannel_Type.__name__ = "Integer32"
_CcPortalChannel_Object = MibTableColumn
ccPortalChannel = _CcPortalChannel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 1, 1, 12),
    _CcPortalChannel_Type()
)
ccPortalChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalChannel.setStatus("current")


class _CcPortalTxPowerLevel_Type(Integer32):
    """Custom type ccPortalTxPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CcPortalTxPowerLevel_Type.__name__ = "Integer32"
_CcPortalTxPowerLevel_Object = MibTableColumn
ccPortalTxPowerLevel = _CcPortalTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 1, 1, 13),
    _CcPortalTxPowerLevel_Type()
)
ccPortalTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPowerLevel.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalTxPowerLevel.setUnits("milli-Watts")
_CcPortalLastAdoption_Type = TimeTicks
_CcPortalLastAdoption_Object = MibTableColumn
ccPortalLastAdoption = _CcPortalLastAdoption_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 1, 1, 14),
    _CcPortalLastAdoption_Type()
)
ccPortalLastAdoption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalLastAdoption.setStatus("current")


class _CcPortalState_Type(Integer32):
    """Custom type ccPortalState based on Integer32"""
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
        *(("portalBroken", 5),
          ("portalDeniedAdoptionDueToAcl", 4),
          ("portalReceivingConfig", 2),
          ("portalUpAndAdopted", 3),
          ("portalUpAndWaitingForConfig", 1))
    )


_CcPortalState_Type.__name__ = "Integer32"
_CcPortalState_Object = MibTableColumn
ccPortalState = _CcPortalState_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 1, 1, 15),
    _CcPortalState_Type()
)
ccPortalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalState.setStatus("current")
_CcPortalBackgroundNoiseNumSamples_Type = Counter32
_CcPortalBackgroundNoiseNumSamples_Object = MibTableColumn
ccPortalBackgroundNoiseNumSamples = _CcPortalBackgroundNoiseNumSamples_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 1, 1, 16),
    _CcPortalBackgroundNoiseNumSamples_Type()
)
ccPortalBackgroundNoiseNumSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalBackgroundNoiseNumSamples.setStatus("current")
_CcPortalBackgroundNoiseBest_Type = Integer32
_CcPortalBackgroundNoiseBest_Object = MibTableColumn
ccPortalBackgroundNoiseBest = _CcPortalBackgroundNoiseBest_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 1, 1, 17),
    _CcPortalBackgroundNoiseBest_Type()
)
ccPortalBackgroundNoiseBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalBackgroundNoiseBest.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalBackgroundNoiseBest.setUnits("dBm")
_CcPortalBackgroundNoiseWorst_Type = Integer32
_CcPortalBackgroundNoiseWorst_Object = MibTableColumn
ccPortalBackgroundNoiseWorst = _CcPortalBackgroundNoiseWorst_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 1, 1, 18),
    _CcPortalBackgroundNoiseWorst_Type()
)
ccPortalBackgroundNoiseWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalBackgroundNoiseWorst.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalBackgroundNoiseWorst.setUnits("dBm")
_CcPortalBackgroundNoiseSum_Type = Integer32
_CcPortalBackgroundNoiseSum_Object = MibTableColumn
ccPortalBackgroundNoiseSum = _CcPortalBackgroundNoiseSum_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 1, 1, 19),
    _CcPortalBackgroundNoiseSum_Type()
)
ccPortalBackgroundNoiseSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalBackgroundNoiseSum.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalBackgroundNoiseSum.setUnits("dBm")
_CcPortalBackgroundNoiseSumSquares_Type = Counter64
_CcPortalBackgroundNoiseSumSquares_Object = MibTableColumn
ccPortalBackgroundNoiseSumSquares = _CcPortalBackgroundNoiseSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 1, 1, 20),
    _CcPortalBackgroundNoiseSumSquares_Type()
)
ccPortalBackgroundNoiseSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalBackgroundNoiseSumSquares.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalBackgroundNoiseSumSquares.setUnits("dBm")
_CcPortalLastMac_Type = PhysAddress
_CcPortalLastMac_Object = MibScalar
ccPortalLastMac = _CcPortalLastMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 2),
    _CcPortalLastMac_Type()
)
ccPortalLastMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalLastMac.setStatus("current")


class _CcPortalLastReason_Type(Integer32):
    """Custom type ccPortalLastReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aclViolation", 2),
          ("success", 1),
          ("timeout", 3))
    )


_CcPortalLastReason_Type.__name__ = "Integer32"
_CcPortalLastReason_Object = MibScalar
ccPortalLastReason = _CcPortalLastReason_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 3),
    _CcPortalLastReason_Type()
)
ccPortalLastReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalLastReason.setStatus("current")
_CcPortalAdoptionTable_Object = MibTable
ccPortalAdoptionTable = _CcPortalAdoptionTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 4)
)
if mibBuilder.loadTexts:
    ccPortalAdoptionTable.setStatus("current")
_CcPortalAdoptionEntry_Object = MibTableRow
ccPortalAdoptionEntry = _CcPortalAdoptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 4, 1)
)
ccPortalAdoptionEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccPortalAdoptionIndex"),
)
if mibBuilder.loadTexts:
    ccPortalAdoptionEntry.setStatus("current")


class _CcPortalAdoptionIndex_Type(Integer32):
    """Custom type ccPortalAdoptionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_CcPortalAdoptionIndex_Type.__name__ = "Integer32"
_CcPortalAdoptionIndex_Object = MibTableColumn
ccPortalAdoptionIndex = _CcPortalAdoptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 4, 1, 1),
    _CcPortalAdoptionIndex_Type()
)
ccPortalAdoptionIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccPortalAdoptionIndex.setStatus("current")
_CcPortalAdoptionStartMac_Type = PhysAddress
_CcPortalAdoptionStartMac_Object = MibTableColumn
ccPortalAdoptionStartMac = _CcPortalAdoptionStartMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 4, 1, 2),
    _CcPortalAdoptionStartMac_Type()
)
ccPortalAdoptionStartMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalAdoptionStartMac.setStatus("current")
_CcPortalAdoptionEndMac_Type = PhysAddress
_CcPortalAdoptionEndMac_Object = MibTableColumn
ccPortalAdoptionEndMac = _CcPortalAdoptionEndMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 4, 1, 3),
    _CcPortalAdoptionEndMac_Type()
)
ccPortalAdoptionEndMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalAdoptionEndMac.setStatus("current")
_CcPortalAdoptionWlanPointers_Type = SinglePointer
_CcPortalAdoptionWlanPointers_Object = MibTableColumn
ccPortalAdoptionWlanPointers = _CcPortalAdoptionWlanPointers_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 4, 1, 4),
    _CcPortalAdoptionWlanPointers_Type()
)
ccPortalAdoptionWlanPointers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalAdoptionWlanPointers.setStatus("current")
_CcPortalAdoptionRowStatus_Type = AbbrevRowStatus
_CcPortalAdoptionRowStatus_Object = MibTableColumn
ccPortalAdoptionRowStatus = _CcPortalAdoptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 4, 1, 5),
    _CcPortalAdoptionRowStatus_Type()
)
ccPortalAdoptionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalAdoptionRowStatus.setStatus("current")
_CcPortalSystemStatsTable_Object = MibTable
ccPortalSystemStatsTable = _CcPortalSystemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 5)
)
if mibBuilder.loadTexts:
    ccPortalSystemStatsTable.setStatus("current")
_CcPortalSystemStatsEntry_Object = MibTableRow
ccPortalSystemStatsEntry = _CcPortalSystemStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 5, 1)
)
ccPortalSystemStatsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    ccPortalSystemStatsEntry.setStatus("current")
_CcPortalSystemStatsBeaconsTx_Type = Unsigned32
_CcPortalSystemStatsBeaconsTx_Object = MibTableColumn
ccPortalSystemStatsBeaconsTx = _CcPortalSystemStatsBeaconsTx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 5, 1, 1),
    _CcPortalSystemStatsBeaconsTx_Type()
)
ccPortalSystemStatsBeaconsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSystemStatsBeaconsTx.setStatus("current")
_CcPortalSystemStatsBeaconsTxOctets_Type = Unsigned32
_CcPortalSystemStatsBeaconsTxOctets_Object = MibTableColumn
ccPortalSystemStatsBeaconsTxOctets = _CcPortalSystemStatsBeaconsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 5, 1, 2),
    _CcPortalSystemStatsBeaconsTxOctets_Type()
)
ccPortalSystemStatsBeaconsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSystemStatsBeaconsTxOctets.setStatus("current")
_CcPortalSystemStatsProbeReqRx_Type = Unsigned32
_CcPortalSystemStatsProbeReqRx_Object = MibTableColumn
ccPortalSystemStatsProbeReqRx = _CcPortalSystemStatsProbeReqRx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 5, 1, 3),
    _CcPortalSystemStatsProbeReqRx_Type()
)
ccPortalSystemStatsProbeReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSystemStatsProbeReqRx.setStatus("current")
_CcPortalSystemStatsProbeReqRxOctets_Type = Unsigned32
_CcPortalSystemStatsProbeReqRxOctets_Object = MibTableColumn
ccPortalSystemStatsProbeReqRxOctets = _CcPortalSystemStatsProbeReqRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 5, 1, 4),
    _CcPortalSystemStatsProbeReqRxOctets_Type()
)
ccPortalSystemStatsProbeReqRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSystemStatsProbeReqRxOctets.setStatus("current")
_CcPortalSystemStatsProbeRespRetriesNone_Type = Unsigned32
_CcPortalSystemStatsProbeRespRetriesNone_Object = MibTableColumn
ccPortalSystemStatsProbeRespRetriesNone = _CcPortalSystemStatsProbeRespRetriesNone_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 5, 1, 5),
    _CcPortalSystemStatsProbeRespRetriesNone_Type()
)
ccPortalSystemStatsProbeRespRetriesNone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSystemStatsProbeRespRetriesNone.setStatus("current")
_CcPortalSystemStatsProbeRespRetries1_Type = Unsigned32
_CcPortalSystemStatsProbeRespRetries1_Object = MibTableColumn
ccPortalSystemStatsProbeRespRetries1 = _CcPortalSystemStatsProbeRespRetries1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 5, 1, 6),
    _CcPortalSystemStatsProbeRespRetries1_Type()
)
ccPortalSystemStatsProbeRespRetries1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSystemStatsProbeRespRetries1.setStatus("current")
_CcPortalSystemStatsProbeRespRetries2_Type = Unsigned32
_CcPortalSystemStatsProbeRespRetries2_Object = MibTableColumn
ccPortalSystemStatsProbeRespRetries2 = _CcPortalSystemStatsProbeRespRetries2_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 5, 1, 7),
    _CcPortalSystemStatsProbeRespRetries2_Type()
)
ccPortalSystemStatsProbeRespRetries2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSystemStatsProbeRespRetries2.setStatus("current")
_CcPortalSystemStatsProbeRespRetries3OrMore_Type = Unsigned32
_CcPortalSystemStatsProbeRespRetries3OrMore_Object = MibTableColumn
ccPortalSystemStatsProbeRespRetries3OrMore = _CcPortalSystemStatsProbeRespRetries3OrMore_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 5, 1, 8),
    _CcPortalSystemStatsProbeRespRetries3OrMore_Type()
)
ccPortalSystemStatsProbeRespRetries3OrMore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSystemStatsProbeRespRetries3OrMore.setStatus("current")
_CcPortalSystemStatsProbeRespRetriesFailed_Type = Unsigned32
_CcPortalSystemStatsProbeRespRetriesFailed_Object = MibTableColumn
ccPortalSystemStatsProbeRespRetriesFailed = _CcPortalSystemStatsProbeRespRetriesFailed_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 5, 1, 9),
    _CcPortalSystemStatsProbeRespRetriesFailed_Type()
)
ccPortalSystemStatsProbeRespRetriesFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSystemStatsProbeRespRetriesFailed.setStatus("current")
_CcPortalSystemStatsProbeRespTxOctets_Type = Unsigned32
_CcPortalSystemStatsProbeRespTxOctets_Object = MibTableColumn
ccPortalSystemStatsProbeRespTxOctets = _CcPortalSystemStatsProbeRespTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 5, 1, 10),
    _CcPortalSystemStatsProbeRespTxOctets_Type()
)
ccPortalSystemStatsProbeRespTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSystemStatsProbeRespTxOctets.setStatus("current")
_CcPortalSettingsTable_Object = MibTable
ccPortalSettingsTable = _CcPortalSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 6)
)
if mibBuilder.loadTexts:
    ccPortalSettingsTable.setStatus("current")
_CcPortalSettingsEntry_Object = MibTableRow
ccPortalSettingsEntry = _CcPortalSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 6, 1)
)
ccPortalSettingsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    ccPortalSettingsEntry.setStatus("current")
_CcPortalSettingsName_Type = DisplayString
_CcPortalSettingsName_Object = MibTableColumn
ccPortalSettingsName = _CcPortalSettingsName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 6, 1, 1),
    _CcPortalSettingsName_Type()
)
ccPortalSettingsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalSettingsName.setStatus("current")
_CcPortalSettingsLocation_Type = DisplayString
_CcPortalSettingsLocation_Object = MibTableColumn
ccPortalSettingsLocation = _CcPortalSettingsLocation_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 6, 1, 2),
    _CcPortalSettingsLocation_Type()
)
ccPortalSettingsLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalSettingsLocation.setStatus("current")


class _CcPortalSettingsAntenna_Type(Integer32):
    """Custom type ccPortalSettingsAntenna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullDiversity", 1),
          ("primaryOnly", 2),
          ("secondaryOnly", 3))
    )


_CcPortalSettingsAntenna_Type.__name__ = "Integer32"
_CcPortalSettingsAntenna_Object = MibTableColumn
ccPortalSettingsAntenna = _CcPortalSettingsAntenna_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 6, 1, 3),
    _CcPortalSettingsAntenna_Type()
)
ccPortalSettingsAntenna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalSettingsAntenna.setStatus("current")
_CcPortalSettingsShortPreamble_Type = TruthValue
_CcPortalSettingsShortPreamble_Object = MibTableColumn
ccPortalSettingsShortPreamble = _CcPortalSettingsShortPreamble_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 6, 1, 4),
    _CcPortalSettingsShortPreamble_Type()
)
ccPortalSettingsShortPreamble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalSettingsShortPreamble.setStatus("current")
_CcPortalSettingsUniSpread_Type = TruthValue
_CcPortalSettingsUniSpread_Object = MibTableColumn
ccPortalSettingsUniSpread = _CcPortalSettingsUniSpread_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 6, 1, 5),
    _CcPortalSettingsUniSpread_Type()
)
ccPortalSettingsUniSpread.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalSettingsUniSpread.setStatus("current")
_CcPortalSettingsRtsThresh_Type = Integer32
_CcPortalSettingsRtsThresh_Object = MibTableColumn
ccPortalSettingsRtsThresh = _CcPortalSettingsRtsThresh_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 6, 1, 6),
    _CcPortalSettingsRtsThresh_Type()
)
ccPortalSettingsRtsThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalSettingsRtsThresh.setStatus("current")


class _CcPortalSettingsBeaconInt_Type(Integer32):
    """Custom type ccPortalSettingsBeaconInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 200),
    )


_CcPortalSettingsBeaconInt_Type.__name__ = "Integer32"
_CcPortalSettingsBeaconInt_Object = MibTableColumn
ccPortalSettingsBeaconInt = _CcPortalSettingsBeaconInt_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 6, 1, 7),
    _CcPortalSettingsBeaconInt_Type()
)
ccPortalSettingsBeaconInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalSettingsBeaconInt.setStatus("current")


class _CcPortalSettingsDtimPrd_Type(Integer32):
    """Custom type ccPortalSettingsDtimPrd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_CcPortalSettingsDtimPrd_Type.__name__ = "Integer32"
_CcPortalSettingsDtimPrd_Object = MibTableColumn
ccPortalSettingsDtimPrd = _CcPortalSettingsDtimPrd_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 6, 1, 8),
    _CcPortalSettingsDtimPrd_Type()
)
ccPortalSettingsDtimPrd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalSettingsDtimPrd.setStatus("current")
_CcPortalSettingsSecBeacon_Type = TruthValue
_CcPortalSettingsSecBeacon_Object = MibTableColumn
ccPortalSettingsSecBeacon = _CcPortalSettingsSecBeacon_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 6, 1, 9),
    _CcPortalSettingsSecBeacon_Type()
)
ccPortalSettingsSecBeacon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalSettingsSecBeacon.setStatus("current")
_CcPortalSettingsPriWlan_Type = SinglePointer
_CcPortalSettingsPriWlan_Object = MibTableColumn
ccPortalSettingsPriWlan = _CcPortalSettingsPriWlan_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 6, 1, 10),
    _CcPortalSettingsPriWlan_Type()
)
ccPortalSettingsPriWlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalSettingsPriWlan.setStatus("current")
_CcPortalSettingsBasicRates_Type = TransmitRate
_CcPortalSettingsBasicRates_Object = MibTableColumn
ccPortalSettingsBasicRates = _CcPortalSettingsBasicRates_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 6, 1, 11),
    _CcPortalSettingsBasicRates_Type()
)
ccPortalSettingsBasicRates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalSettingsBasicRates.setStatus("current")
_CcPortalSettingsSupportedRates_Type = TransmitRate
_CcPortalSettingsSupportedRates_Object = MibTableColumn
ccPortalSettingsSupportedRates = _CcPortalSettingsSupportedRates_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 6, 1, 12),
    _CcPortalSettingsSupportedRates_Type()
)
ccPortalSettingsSupportedRates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalSettingsSupportedRates.setStatus("current")


class _CcPortalSettingsBGMode_Type(Integer32):
    """Custom type ccPortalSettingsBGMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("modeB", 3),
          ("modeBandG", 1),
          ("modeG", 2))
    )


_CcPortalSettingsBGMode_Type.__name__ = "Integer32"
_CcPortalSettingsBGMode_Object = MibTableColumn
ccPortalSettingsBGMode = _CcPortalSettingsBGMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 6, 1, 13),
    _CcPortalSettingsBGMode_Type()
)
ccPortalSettingsBGMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalSettingsBGMode.setStatus("current")
_CcPortalSettingsAdoptedWlan_Type = MultiPointer63
_CcPortalSettingsAdoptedWlan_Object = MibTableColumn
ccPortalSettingsAdoptedWlan = _CcPortalSettingsAdoptedWlan_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 6, 1, 14),
    _CcPortalSettingsAdoptedWlan_Type()
)
ccPortalSettingsAdoptedWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSettingsAdoptedWlan.setStatus("current")
_CcPortalSettingsDetector_Type = TruthValue
_CcPortalSettingsDetector_Object = MibTableColumn
ccPortalSettingsDetector = _CcPortalSettingsDetector_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 6, 1, 15),
    _CcPortalSettingsDetector_Type()
)
ccPortalSettingsDetector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalSettingsDetector.setStatus("current")
_CcPortalCfgRadioTable_Object = MibTable
ccPortalCfgRadioTable = _CcPortalCfgRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 7)
)
if mibBuilder.loadTexts:
    ccPortalCfgRadioTable.setStatus("current")
_CcPortalCfgRadioEntry_Object = MibTableRow
ccPortalCfgRadioEntry = _CcPortalCfgRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 7, 1)
)
ccPortalCfgRadioEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    ccPortalCfgRadioEntry.setStatus("current")


class _CcPortalCfgRadioDesPlacement_Type(Integer32):
    """Custom type ccPortalCfgRadioDesPlacement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("indoor", 1),
          ("outdoor", 2))
    )


_CcPortalCfgRadioDesPlacement_Type.__name__ = "Integer32"
_CcPortalCfgRadioDesPlacement_Object = MibTableColumn
ccPortalCfgRadioDesPlacement = _CcPortalCfgRadioDesPlacement_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 7, 1, 1),
    _CcPortalCfgRadioDesPlacement_Type()
)
ccPortalCfgRadioDesPlacement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalCfgRadioDesPlacement.setStatus("current")


class _CcPortalCfgRadioPosChannel_Type(Bits):
    """Custom type ccPortalCfgRadioPosChannel based on Bits"""
    namedValues = NamedValues(
        *(("achannel149", 20),
          ("achannel153", 21),
          ("achannel157", 22),
          ("achannel161", 23),
          ("achannel36", 12),
          ("achannel40", 13),
          ("achannel44", 14),
          ("achannel48", 15),
          ("achannel52", 16),
          ("achannel56", 17),
          ("achannel60", 18),
          ("achannel64", 19),
          ("bchannel01", 1),
          ("bchannel02", 2),
          ("bchannel03", 3),
          ("bchannel04", 4),
          ("bchannel05", 5),
          ("bchannel06", 6),
          ("bchannel07", 7),
          ("bchannel08", 8),
          ("bchannel09", 9),
          ("bchannel10", 10),
          ("bchannel11", 11),
          ("null", 0))
    )

_CcPortalCfgRadioPosChannel_Type.__name__ = "Bits"
_CcPortalCfgRadioPosChannel_Object = MibTableColumn
ccPortalCfgRadioPosChannel = _CcPortalCfgRadioPosChannel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 7, 1, 2),
    _CcPortalCfgRadioPosChannel_Type()
)
ccPortalCfgRadioPosChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalCfgRadioPosChannel.setStatus("current")


class _CcPortalCfgRadioDesChannel_Type(Integer32):
    """Custom type ccPortalCfgRadioDesChannel based on Integer32"""
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
              36,
              40,
              44,
              48,
              52,
              56,
              60,
              64,
              149,
              153,
              157,
              161)
        )
    )
    namedValues = NamedValues(
        *(("achannel149", 149),
          ("achannel153", 153),
          ("achannel157", 157),
          ("achannel161", 161),
          ("achannel36", 36),
          ("achannel40", 40),
          ("achannel44", 44),
          ("achannel48", 48),
          ("achannel52", 52),
          ("achannel56", 56),
          ("achannel60", 60),
          ("achannel64", 64),
          ("bchannel01", 1),
          ("bchannel02", 2),
          ("bchannel03", 3),
          ("bchannel04", 4),
          ("bchannel05", 5),
          ("bchannel06", 6),
          ("bchannel07", 7),
          ("bchannel08", 8),
          ("bchannel09", 9),
          ("bchannel10", 10),
          ("bchannel11", 11),
          ("null", 0))
    )


_CcPortalCfgRadioDesChannel_Type.__name__ = "Integer32"
_CcPortalCfgRadioDesChannel_Object = MibTableColumn
ccPortalCfgRadioDesChannel = _CcPortalCfgRadioDesChannel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 7, 1, 3),
    _CcPortalCfgRadioDesChannel_Type()
)
ccPortalCfgRadioDesChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalCfgRadioDesChannel.setStatus("current")
_CcPortalCfgRadioPosPowerLevel_Type = Integer32
_CcPortalCfgRadioPosPowerLevel_Object = MibTableColumn
ccPortalCfgRadioPosPowerLevel = _CcPortalCfgRadioPosPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 7, 1, 4),
    _CcPortalCfgRadioPosPowerLevel_Type()
)
ccPortalCfgRadioPosPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalCfgRadioPosPowerLevel.setStatus("current")
_CcPortalCfgRadioDesPowerLevel_Type = Integer32
_CcPortalCfgRadioDesPowerLevel_Object = MibTableColumn
ccPortalCfgRadioDesPowerLevel = _CcPortalCfgRadioDesPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 7, 1, 5),
    _CcPortalCfgRadioDesPowerLevel_Type()
)
ccPortalCfgRadioDesPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalCfgRadioDesPowerLevel.setStatus("current")
_CcPortalCfgRadioDesPowerInMW_Type = Integer32
_CcPortalCfgRadioDesPowerInMW_Object = MibTableColumn
ccPortalCfgRadioDesPowerInMW = _CcPortalCfgRadioDesPowerInMW_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 7, 1, 6),
    _CcPortalCfgRadioDesPowerInMW_Type()
)
ccPortalCfgRadioDesPowerInMW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalCfgRadioDesPowerInMW.setStatus("current")
_CcPortalCfgRadioSet_Type = DoActionShowProgress
_CcPortalCfgRadioSet_Object = MibTableColumn
ccPortalCfgRadioSet = _CcPortalCfgRadioSet_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 7, 1, 7),
    _CcPortalCfgRadioSet_Type()
)
ccPortalCfgRadioSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalCfgRadioSet.setStatus("current")
_CcPortalCfgRadioReset_Type = DoActionShowProgress
_CcPortalCfgRadioReset_Object = MibTableColumn
ccPortalCfgRadioReset = _CcPortalCfgRadioReset_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 7, 1, 8),
    _CcPortalCfgRadioReset_Type()
)
ccPortalCfgRadioReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalCfgRadioReset.setStatus("current")


class _CcPortalCfgRadioPlacement_Type(Integer32):
    """Custom type ccPortalCfgRadioPlacement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("indoor", 1),
          ("outdoor", 2))
    )


_CcPortalCfgRadioPlacement_Type.__name__ = "Integer32"
_CcPortalCfgRadioPlacement_Object = MibTableColumn
ccPortalCfgRadioPlacement = _CcPortalCfgRadioPlacement_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 7, 1, 9),
    _CcPortalCfgRadioPlacement_Type()
)
ccPortalCfgRadioPlacement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalCfgRadioPlacement.setStatus("current")


class _CcPortalCfgRadioChannel_Type(Integer32):
    """Custom type ccPortalCfgRadioChannel based on Integer32"""
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
              36,
              40,
              44,
              48,
              52,
              56,
              60,
              64,
              149,
              153,
              157,
              161)
        )
    )
    namedValues = NamedValues(
        *(("achannel149", 149),
          ("achannel153", 153),
          ("achannel157", 157),
          ("achannel161", 161),
          ("achannel36", 36),
          ("achannel40", 40),
          ("achannel44", 44),
          ("achannel48", 48),
          ("achannel52", 52),
          ("achannel56", 56),
          ("achannel60", 60),
          ("achannel64", 64),
          ("bchannel01", 1),
          ("bchannel02", 2),
          ("bchannel03", 3),
          ("bchannel04", 4),
          ("bchannel05", 5),
          ("bchannel06", 6),
          ("bchannel07", 7),
          ("bchannel08", 8),
          ("bchannel09", 9),
          ("bchannel10", 10),
          ("bchannel11", 11),
          ("null", 0))
    )


_CcPortalCfgRadioChannel_Type.__name__ = "Integer32"
_CcPortalCfgRadioChannel_Object = MibTableColumn
ccPortalCfgRadioChannel = _CcPortalCfgRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 7, 1, 10),
    _CcPortalCfgRadioChannel_Type()
)
ccPortalCfgRadioChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalCfgRadioChannel.setStatus("current")
_CcPortalCfgRadioPowerLevel_Type = Unsigned32
_CcPortalCfgRadioPowerLevel_Object = MibTableColumn
ccPortalCfgRadioPowerLevel = _CcPortalCfgRadioPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 7, 1, 11),
    _CcPortalCfgRadioPowerLevel_Type()
)
ccPortalCfgRadioPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalCfgRadioPowerLevel.setStatus("current")
_CcPortalCfgRadioPowerInMW_Type = Unsigned32
_CcPortalCfgRadioPowerInMW_Object = MibTableColumn
ccPortalCfgRadioPowerInMW = _CcPortalCfgRadioPowerInMW_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 7, 1, 12),
    _CcPortalCfgRadioPowerInMW_Type()
)
ccPortalCfgRadioPowerInMW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalCfgRadioPowerInMW.setStatus("current")
_CcPortalSettingsDefaultTable_Object = MibTable
ccPortalSettingsDefaultTable = _CcPortalSettingsDefaultTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 8)
)
if mibBuilder.loadTexts:
    ccPortalSettingsDefaultTable.setStatus("current")
_CcPortalSettingsDefaultEntry_Object = MibTableRow
ccPortalSettingsDefaultEntry = _CcPortalSettingsDefaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 8, 1)
)
ccPortalSettingsDefaultEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccPortalSettingsDefaultIndex"),
)
if mibBuilder.loadTexts:
    ccPortalSettingsDefaultEntry.setStatus("current")


class _CcPortalSettingsDefaultIndex_Type(Integer32):
    """Custom type ccPortalSettingsDefaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("radioA", 1),
          ("radioB", 2),
          ("radioG", 3))
    )


_CcPortalSettingsDefaultIndex_Type.__name__ = "Integer32"
_CcPortalSettingsDefaultIndex_Object = MibTableColumn
ccPortalSettingsDefaultIndex = _CcPortalSettingsDefaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 8, 1, 1),
    _CcPortalSettingsDefaultIndex_Type()
)
ccPortalSettingsDefaultIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccPortalSettingsDefaultIndex.setStatus("current")


class _CcPortalSettingsDefaultAntenna_Type(Integer32):
    """Custom type ccPortalSettingsDefaultAntenna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullDiversity", 1),
          ("primaryOnly", 2),
          ("secondaryOnly", 3))
    )


_CcPortalSettingsDefaultAntenna_Type.__name__ = "Integer32"
_CcPortalSettingsDefaultAntenna_Object = MibTableColumn
ccPortalSettingsDefaultAntenna = _CcPortalSettingsDefaultAntenna_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 8, 1, 2),
    _CcPortalSettingsDefaultAntenna_Type()
)
ccPortalSettingsDefaultAntenna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalSettingsDefaultAntenna.setStatus("current")
_CcPortalSettingsDefaultShortPreamble_Type = TruthValue
_CcPortalSettingsDefaultShortPreamble_Object = MibTableColumn
ccPortalSettingsDefaultShortPreamble = _CcPortalSettingsDefaultShortPreamble_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 8, 1, 3),
    _CcPortalSettingsDefaultShortPreamble_Type()
)
ccPortalSettingsDefaultShortPreamble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalSettingsDefaultShortPreamble.setStatus("current")
_CcPortalSettingsDefaultUniSpread_Type = TruthValue
_CcPortalSettingsDefaultUniSpread_Object = MibTableColumn
ccPortalSettingsDefaultUniSpread = _CcPortalSettingsDefaultUniSpread_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 8, 1, 4),
    _CcPortalSettingsDefaultUniSpread_Type()
)
ccPortalSettingsDefaultUniSpread.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalSettingsDefaultUniSpread.setStatus("current")
_CcPortalSettingsDefaultRtsThresh_Type = Integer32
_CcPortalSettingsDefaultRtsThresh_Object = MibTableColumn
ccPortalSettingsDefaultRtsThresh = _CcPortalSettingsDefaultRtsThresh_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 8, 1, 5),
    _CcPortalSettingsDefaultRtsThresh_Type()
)
ccPortalSettingsDefaultRtsThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalSettingsDefaultRtsThresh.setStatus("current")


class _CcPortalSettingsDefaultBeaconInt_Type(Integer32):
    """Custom type ccPortalSettingsDefaultBeaconInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 200),
    )


_CcPortalSettingsDefaultBeaconInt_Type.__name__ = "Integer32"
_CcPortalSettingsDefaultBeaconInt_Object = MibTableColumn
ccPortalSettingsDefaultBeaconInt = _CcPortalSettingsDefaultBeaconInt_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 8, 1, 6),
    _CcPortalSettingsDefaultBeaconInt_Type()
)
ccPortalSettingsDefaultBeaconInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalSettingsDefaultBeaconInt.setStatus("current")


class _CcPortalSettingsDefaultDtimPrd_Type(Integer32):
    """Custom type ccPortalSettingsDefaultDtimPrd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_CcPortalSettingsDefaultDtimPrd_Type.__name__ = "Integer32"
_CcPortalSettingsDefaultDtimPrd_Object = MibTableColumn
ccPortalSettingsDefaultDtimPrd = _CcPortalSettingsDefaultDtimPrd_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 8, 1, 7),
    _CcPortalSettingsDefaultDtimPrd_Type()
)
ccPortalSettingsDefaultDtimPrd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalSettingsDefaultDtimPrd.setStatus("current")
_CcPortalSettingsDefaultSecBeacon_Type = TruthValue
_CcPortalSettingsDefaultSecBeacon_Object = MibTableColumn
ccPortalSettingsDefaultSecBeacon = _CcPortalSettingsDefaultSecBeacon_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 8, 1, 8),
    _CcPortalSettingsDefaultSecBeacon_Type()
)
ccPortalSettingsDefaultSecBeacon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalSettingsDefaultSecBeacon.setStatus("current")
_CcPortalSettingsDefaultPriWlan_Type = SinglePointer
_CcPortalSettingsDefaultPriWlan_Object = MibTableColumn
ccPortalSettingsDefaultPriWlan = _CcPortalSettingsDefaultPriWlan_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 8, 1, 9),
    _CcPortalSettingsDefaultPriWlan_Type()
)
ccPortalSettingsDefaultPriWlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalSettingsDefaultPriWlan.setStatus("current")
_CcPortalSettingsDefaultBasicRates_Type = TransmitRate
_CcPortalSettingsDefaultBasicRates_Object = MibTableColumn
ccPortalSettingsDefaultBasicRates = _CcPortalSettingsDefaultBasicRates_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 8, 1, 10),
    _CcPortalSettingsDefaultBasicRates_Type()
)
ccPortalSettingsDefaultBasicRates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalSettingsDefaultBasicRates.setStatus("current")
_CcPortalSettingsDefaultSupportedRates_Type = TransmitRate
_CcPortalSettingsDefaultSupportedRates_Object = MibTableColumn
ccPortalSettingsDefaultSupportedRates = _CcPortalSettingsDefaultSupportedRates_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 8, 1, 11),
    _CcPortalSettingsDefaultSupportedRates_Type()
)
ccPortalSettingsDefaultSupportedRates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalSettingsDefaultSupportedRates.setStatus("current")


class _CcPortalSettingsDefaultBGMode_Type(Integer32):
    """Custom type ccPortalSettingsDefaultBGMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("modeB", 3),
          ("modeBandG", 1),
          ("modeG", 2))
    )


_CcPortalSettingsDefaultBGMode_Type.__name__ = "Integer32"
_CcPortalSettingsDefaultBGMode_Object = MibTableColumn
ccPortalSettingsDefaultBGMode = _CcPortalSettingsDefaultBGMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 8, 1, 12),
    _CcPortalSettingsDefaultBGMode_Type()
)
ccPortalSettingsDefaultBGMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalSettingsDefaultBGMode.setStatus("current")
_CcPortalCfgRadioDefaultTable_Object = MibTable
ccPortalCfgRadioDefaultTable = _CcPortalCfgRadioDefaultTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 9)
)
if mibBuilder.loadTexts:
    ccPortalCfgRadioDefaultTable.setStatus("current")
_CcPortalCfgRadioDefaultEntry_Object = MibTableRow
ccPortalCfgRadioDefaultEntry = _CcPortalCfgRadioDefaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 9, 1)
)
ccPortalCfgRadioDefaultEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccPortalSettingsDefaultIndex"),
)
if mibBuilder.loadTexts:
    ccPortalCfgRadioDefaultEntry.setStatus("current")


class _CcPortalCfgRadioDefaultDesPlacement_Type(Integer32):
    """Custom type ccPortalCfgRadioDefaultDesPlacement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("indoor", 1),
          ("outdoor", 2))
    )


_CcPortalCfgRadioDefaultDesPlacement_Type.__name__ = "Integer32"
_CcPortalCfgRadioDefaultDesPlacement_Object = MibTableColumn
ccPortalCfgRadioDefaultDesPlacement = _CcPortalCfgRadioDefaultDesPlacement_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 9, 1, 1),
    _CcPortalCfgRadioDefaultDesPlacement_Type()
)
ccPortalCfgRadioDefaultDesPlacement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalCfgRadioDefaultDesPlacement.setStatus("current")


class _CcPortalCfgRadioDefaultPosChannel_Type(Bits):
    """Custom type ccPortalCfgRadioDefaultPosChannel based on Bits"""
    namedValues = NamedValues(
        *(("achannel149", 20),
          ("achannel153", 21),
          ("achannel157", 22),
          ("achannel161", 23),
          ("achannel36", 12),
          ("achannel40", 13),
          ("achannel44", 14),
          ("achannel48", 15),
          ("achannel52", 16),
          ("achannel56", 17),
          ("achannel60", 18),
          ("achannel64", 19),
          ("bchannel01", 1),
          ("bchannel02", 2),
          ("bchannel03", 3),
          ("bchannel04", 4),
          ("bchannel05", 5),
          ("bchannel06", 6),
          ("bchannel07", 7),
          ("bchannel08", 8),
          ("bchannel09", 9),
          ("bchannel10", 10),
          ("bchannel11", 11),
          ("null", 0))
    )

_CcPortalCfgRadioDefaultPosChannel_Type.__name__ = "Bits"
_CcPortalCfgRadioDefaultPosChannel_Object = MibTableColumn
ccPortalCfgRadioDefaultPosChannel = _CcPortalCfgRadioDefaultPosChannel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 9, 1, 2),
    _CcPortalCfgRadioDefaultPosChannel_Type()
)
ccPortalCfgRadioDefaultPosChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalCfgRadioDefaultPosChannel.setStatus("current")


class _CcPortalCfgRadioDefaultDesChannel_Type(Integer32):
    """Custom type ccPortalCfgRadioDefaultDesChannel based on Integer32"""
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
              36,
              40,
              44,
              48,
              52,
              56,
              60,
              64,
              149,
              153,
              157,
              161)
        )
    )
    namedValues = NamedValues(
        *(("achannel149", 149),
          ("achannel153", 153),
          ("achannel157", 157),
          ("achannel161", 161),
          ("achannel36", 36),
          ("achannel40", 40),
          ("achannel44", 44),
          ("achannel48", 48),
          ("achannel52", 52),
          ("achannel56", 56),
          ("achannel60", 60),
          ("achannel64", 64),
          ("bchannel01", 1),
          ("bchannel02", 2),
          ("bchannel03", 3),
          ("bchannel04", 4),
          ("bchannel05", 5),
          ("bchannel06", 6),
          ("bchannel07", 7),
          ("bchannel08", 8),
          ("bchannel09", 9),
          ("bchannel10", 10),
          ("bchannel11", 11),
          ("null", 0))
    )


_CcPortalCfgRadioDefaultDesChannel_Type.__name__ = "Integer32"
_CcPortalCfgRadioDefaultDesChannel_Object = MibTableColumn
ccPortalCfgRadioDefaultDesChannel = _CcPortalCfgRadioDefaultDesChannel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 9, 1, 3),
    _CcPortalCfgRadioDefaultDesChannel_Type()
)
ccPortalCfgRadioDefaultDesChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalCfgRadioDefaultDesChannel.setStatus("current")
_CcPortalCfgRadioDefaultPosPowerLevel_Type = Integer32
_CcPortalCfgRadioDefaultPosPowerLevel_Object = MibTableColumn
ccPortalCfgRadioDefaultPosPowerLevel = _CcPortalCfgRadioDefaultPosPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 9, 1, 4),
    _CcPortalCfgRadioDefaultPosPowerLevel_Type()
)
ccPortalCfgRadioDefaultPosPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalCfgRadioDefaultPosPowerLevel.setStatus("current")
_CcPortalCfgRadioDefaultDesPowerLevel_Type = Integer32
_CcPortalCfgRadioDefaultDesPowerLevel_Object = MibTableColumn
ccPortalCfgRadioDefaultDesPowerLevel = _CcPortalCfgRadioDefaultDesPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 9, 1, 5),
    _CcPortalCfgRadioDefaultDesPowerLevel_Type()
)
ccPortalCfgRadioDefaultDesPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalCfgRadioDefaultDesPowerLevel.setStatus("current")
_CcPortalCfgRadioDefaultDesPowerInMW_Type = Integer32
_CcPortalCfgRadioDefaultDesPowerInMW_Object = MibTableColumn
ccPortalCfgRadioDefaultDesPowerInMW = _CcPortalCfgRadioDefaultDesPowerInMW_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 9, 1, 6),
    _CcPortalCfgRadioDefaultDesPowerInMW_Type()
)
ccPortalCfgRadioDefaultDesPowerInMW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalCfgRadioDefaultDesPowerInMW.setStatus("current")
_CcPortalCfgRadioDefaultSet_Type = DoActionShowProgress
_CcPortalCfgRadioDefaultSet_Object = MibTableColumn
ccPortalCfgRadioDefaultSet = _CcPortalCfgRadioDefaultSet_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 9, 1, 7),
    _CcPortalCfgRadioDefaultSet_Type()
)
ccPortalCfgRadioDefaultSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalCfgRadioDefaultSet.setStatus("current")
_CcPortalCfgRadioDefaultReset_Type = DoActionShowProgress
_CcPortalCfgRadioDefaultReset_Object = MibTableColumn
ccPortalCfgRadioDefaultReset = _CcPortalCfgRadioDefaultReset_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 9, 1, 8),
    _CcPortalCfgRadioDefaultReset_Type()
)
ccPortalCfgRadioDefaultReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccPortalCfgRadioDefaultReset.setStatus("current")


class _CcPortalCfgRadioDefaultPlacement_Type(Integer32):
    """Custom type ccPortalCfgRadioDefaultPlacement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("indoor", 1),
          ("outdoor", 2))
    )


_CcPortalCfgRadioDefaultPlacement_Type.__name__ = "Integer32"
_CcPortalCfgRadioDefaultPlacement_Object = MibTableColumn
ccPortalCfgRadioDefaultPlacement = _CcPortalCfgRadioDefaultPlacement_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 9, 1, 9),
    _CcPortalCfgRadioDefaultPlacement_Type()
)
ccPortalCfgRadioDefaultPlacement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalCfgRadioDefaultPlacement.setStatus("current")


class _CcPortalCfgRadioDefaultChannel_Type(Integer32):
    """Custom type ccPortalCfgRadioDefaultChannel based on Integer32"""
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
              36,
              40,
              44,
              48,
              52,
              56,
              60,
              64,
              149,
              153,
              157,
              161)
        )
    )
    namedValues = NamedValues(
        *(("achannel149", 149),
          ("achannel153", 153),
          ("achannel157", 157),
          ("achannel161", 161),
          ("achannel36", 36),
          ("achannel40", 40),
          ("achannel44", 44),
          ("achannel48", 48),
          ("achannel52", 52),
          ("achannel56", 56),
          ("achannel60", 60),
          ("achannel64", 64),
          ("bchannel01", 1),
          ("bchannel02", 2),
          ("bchannel03", 3),
          ("bchannel04", 4),
          ("bchannel05", 5),
          ("bchannel06", 6),
          ("bchannel07", 7),
          ("bchannel08", 8),
          ("bchannel09", 9),
          ("bchannel10", 10),
          ("bchannel11", 11),
          ("null", 0))
    )


_CcPortalCfgRadioDefaultChannel_Type.__name__ = "Integer32"
_CcPortalCfgRadioDefaultChannel_Object = MibTableColumn
ccPortalCfgRadioDefaultChannel = _CcPortalCfgRadioDefaultChannel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 9, 1, 10),
    _CcPortalCfgRadioDefaultChannel_Type()
)
ccPortalCfgRadioDefaultChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalCfgRadioDefaultChannel.setStatus("current")
_CcPortalCfgRadioDefaultPowerLevel_Type = Unsigned32
_CcPortalCfgRadioDefaultPowerLevel_Object = MibTableColumn
ccPortalCfgRadioDefaultPowerLevel = _CcPortalCfgRadioDefaultPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 9, 1, 11),
    _CcPortalCfgRadioDefaultPowerLevel_Type()
)
ccPortalCfgRadioDefaultPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalCfgRadioDefaultPowerLevel.setStatus("current")
_CcPortalCfgRadioDefaultPowerInMW_Type = Unsigned32
_CcPortalCfgRadioDefaultPowerInMW_Object = MibTableColumn
ccPortalCfgRadioDefaultPowerInMW = _CcPortalCfgRadioDefaultPowerInMW_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 9, 1, 12),
    _CcPortalCfgRadioDefaultPowerInMW_Type()
)
ccPortalCfgRadioDefaultPowerInMW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalCfgRadioDefaultPowerInMW.setStatus("current")
_Cc802dt1xPortAuth_ObjectIdentity = ObjectIdentity
cc802dt1xPortAuth = _Cc802dt1xPortAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 10)
)


class _Cc802dt1xPortAuthLogin_Type(DisplayString):
    """Custom type cc802dt1xPortAuthLogin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Cc802dt1xPortAuthLogin_Type.__name__ = "DisplayString"
_Cc802dt1xPortAuthLogin_Object = MibScalar
cc802dt1xPortAuthLogin = _Cc802dt1xPortAuthLogin_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 10, 1),
    _Cc802dt1xPortAuthLogin_Type()
)
cc802dt1xPortAuthLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc802dt1xPortAuthLogin.setStatus("current")
_Cc802dt1xPortAuthPass_Type = Password
_Cc802dt1xPortAuthPass_Object = MibScalar
cc802dt1xPortAuthPass = _Cc802dt1xPortAuthPass_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 10, 2),
    _Cc802dt1xPortAuthPass_Type()
)
cc802dt1xPortAuthPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc802dt1xPortAuthPass.setStatus("current")
_Cc802dt1xPortAuthSetAp300_Type = DoActionShowProgress
_Cc802dt1xPortAuthSetAp300_Object = MibScalar
cc802dt1xPortAuthSetAp300 = _Cc802dt1xPortAuthSetAp300_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 10, 3),
    _Cc802dt1xPortAuthSetAp300_Type()
)
cc802dt1xPortAuthSetAp300.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc802dt1xPortAuthSetAp300.setStatus("current")
_CcPortalRfSum_ObjectIdentity = ObjectIdentity
ccPortalRfSum = _CcPortalRfSum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100)
)
_CcPortalStatsTable_Object = MibTable
ccPortalStatsTable = _CcPortalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 1)
)
if mibBuilder.loadTexts:
    ccPortalStatsTable.setStatus("current")
_CcPortalStatsEntry_Object = MibTableRow
ccPortalStatsEntry = _CcPortalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 1, 1)
)
ccPortalStatsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    ccPortalStatsEntry.setStatus("current")
_CcPortalTxPktsUcast_Type = Counter32
_CcPortalTxPktsUcast_Object = MibTableColumn
ccPortalTxPktsUcast = _CcPortalTxPktsUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 1, 1, 1),
    _CcPortalTxPktsUcast_Type()
)
ccPortalTxPktsUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPktsUcast.setStatus("current")
_CcPortalRxPktsUcast_Type = Counter32
_CcPortalRxPktsUcast_Object = MibTableColumn
ccPortalRxPktsUcast = _CcPortalRxPktsUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 1, 1, 2),
    _CcPortalRxPktsUcast_Type()
)
ccPortalRxPktsUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsUcast.setStatus("current")
_CcPortalRxPktsNUcast_Type = Counter32
_CcPortalRxPktsNUcast_Object = MibTableColumn
ccPortalRxPktsNUcast = _CcPortalRxPktsNUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 1, 1, 3),
    _CcPortalRxPktsNUcast_Type()
)
ccPortalRxPktsNUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsNUcast.setStatus("current")
_CcPortalTxOctetsUcast_Type = Counter32
_CcPortalTxOctetsUcast_Object = MibTableColumn
ccPortalTxOctetsUcast = _CcPortalTxOctetsUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 1, 1, 4),
    _CcPortalTxOctetsUcast_Type()
)
ccPortalTxOctetsUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxOctetsUcast.setStatus("current")
_CcPortalRxOctetsUcast_Type = Counter32
_CcPortalRxOctetsUcast_Object = MibTableColumn
ccPortalRxOctetsUcast = _CcPortalRxOctetsUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 1, 1, 5),
    _CcPortalRxOctetsUcast_Type()
)
ccPortalRxOctetsUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsUcast.setStatus("current")
_CcPortalRxOctetsNUcast_Type = Counter32
_CcPortalRxOctetsNUcast_Object = MibTableColumn
ccPortalRxOctetsNUcast = _CcPortalRxOctetsNUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 1, 1, 6),
    _CcPortalRxOctetsNUcast_Type()
)
ccPortalRxOctetsNUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsNUcast.setStatus("current")
_CcPortalRxUndecryptablePkts_Type = Counter32
_CcPortalRxUndecryptablePkts_Object = MibTableColumn
ccPortalRxUndecryptablePkts = _CcPortalRxUndecryptablePkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 1, 1, 7),
    _CcPortalRxUndecryptablePkts_Type()
)
ccPortalRxUndecryptablePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxUndecryptablePkts.setStatus("current")
_CcPortalLastActivity_Type = TimeTicks
_CcPortalLastActivity_Object = MibTableColumn
ccPortalLastActivity = _CcPortalLastActivity_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 1, 1, 8),
    _CcPortalLastActivity_Type()
)
ccPortalLastActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalLastActivity.setStatus("current")
_CcPortalRxPktsTable_Object = MibTable
ccPortalRxPktsTable = _CcPortalRxPktsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 2)
)
if mibBuilder.loadTexts:
    ccPortalRxPktsTable.setStatus("current")
_CcPortalRxPktsEntry_Object = MibTableRow
ccPortalRxPktsEntry = _CcPortalRxPktsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 2, 1)
)
ccPortalRxPktsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    ccPortalRxPktsEntry.setStatus("current")
_CcPortalRxPktsAt1Mb_Type = Counter32
_CcPortalRxPktsAt1Mb_Object = MibTableColumn
ccPortalRxPktsAt1Mb = _CcPortalRxPktsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 2, 1, 1),
    _CcPortalRxPktsAt1Mb_Type()
)
ccPortalRxPktsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsAt1Mb.setStatus("current")
_CcPortalRxPktsAt2Mb_Type = Counter32
_CcPortalRxPktsAt2Mb_Object = MibTableColumn
ccPortalRxPktsAt2Mb = _CcPortalRxPktsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 2, 1, 2),
    _CcPortalRxPktsAt2Mb_Type()
)
ccPortalRxPktsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsAt2Mb.setStatus("current")
_CcPortalRxPktsAt5pt5Mb_Type = Counter32
_CcPortalRxPktsAt5pt5Mb_Object = MibTableColumn
ccPortalRxPktsAt5pt5Mb = _CcPortalRxPktsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 2, 1, 3),
    _CcPortalRxPktsAt5pt5Mb_Type()
)
ccPortalRxPktsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsAt5pt5Mb.setStatus("current")
_CcPortalRxPktsAt6Mb_Type = Counter32
_CcPortalRxPktsAt6Mb_Object = MibTableColumn
ccPortalRxPktsAt6Mb = _CcPortalRxPktsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 2, 1, 4),
    _CcPortalRxPktsAt6Mb_Type()
)
ccPortalRxPktsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsAt6Mb.setStatus("current")
_CcPortalRxPktsAt9Mb_Type = Counter32
_CcPortalRxPktsAt9Mb_Object = MibTableColumn
ccPortalRxPktsAt9Mb = _CcPortalRxPktsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 2, 1, 5),
    _CcPortalRxPktsAt9Mb_Type()
)
ccPortalRxPktsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsAt9Mb.setStatus("current")
_CcPortalRxPktsAt11Mb_Type = Counter32
_CcPortalRxPktsAt11Mb_Object = MibTableColumn
ccPortalRxPktsAt11Mb = _CcPortalRxPktsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 2, 1, 6),
    _CcPortalRxPktsAt11Mb_Type()
)
ccPortalRxPktsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsAt11Mb.setStatus("current")
_CcPortalRxPktsAt12Mb_Type = Counter32
_CcPortalRxPktsAt12Mb_Object = MibTableColumn
ccPortalRxPktsAt12Mb = _CcPortalRxPktsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 2, 1, 7),
    _CcPortalRxPktsAt12Mb_Type()
)
ccPortalRxPktsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsAt12Mb.setStatus("current")
_CcPortalRxPktsAt18Mb_Type = Counter32
_CcPortalRxPktsAt18Mb_Object = MibTableColumn
ccPortalRxPktsAt18Mb = _CcPortalRxPktsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 2, 1, 8),
    _CcPortalRxPktsAt18Mb_Type()
)
ccPortalRxPktsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsAt18Mb.setStatus("current")
_CcPortalRxPktsAt22Mb_Type = Counter32
_CcPortalRxPktsAt22Mb_Object = MibTableColumn
ccPortalRxPktsAt22Mb = _CcPortalRxPktsAt22Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 2, 1, 9),
    _CcPortalRxPktsAt22Mb_Type()
)
ccPortalRxPktsAt22Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsAt22Mb.setStatus("current")
_CcPortalRxPktsAt24Mb_Type = Counter32
_CcPortalRxPktsAt24Mb_Object = MibTableColumn
ccPortalRxPktsAt24Mb = _CcPortalRxPktsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 2, 1, 10),
    _CcPortalRxPktsAt24Mb_Type()
)
ccPortalRxPktsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsAt24Mb.setStatus("current")
_CcPortalRxPktsAt36Mb_Type = Counter32
_CcPortalRxPktsAt36Mb_Object = MibTableColumn
ccPortalRxPktsAt36Mb = _CcPortalRxPktsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 2, 1, 11),
    _CcPortalRxPktsAt36Mb_Type()
)
ccPortalRxPktsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsAt36Mb.setStatus("current")
_CcPortalRxPktsAt48Mb_Type = Counter32
_CcPortalRxPktsAt48Mb_Object = MibTableColumn
ccPortalRxPktsAt48Mb = _CcPortalRxPktsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 2, 1, 12),
    _CcPortalRxPktsAt48Mb_Type()
)
ccPortalRxPktsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsAt48Mb.setStatus("current")
_CcPortalRxPktsAt54Mb_Type = Counter32
_CcPortalRxPktsAt54Mb_Object = MibTableColumn
ccPortalRxPktsAt54Mb = _CcPortalRxPktsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 2, 1, 13),
    _CcPortalRxPktsAt54Mb_Type()
)
ccPortalRxPktsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxPktsAt54Mb.setStatus("current")
_CcPortalTxPktsTable_Object = MibTable
ccPortalTxPktsTable = _CcPortalTxPktsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 3)
)
if mibBuilder.loadTexts:
    ccPortalTxPktsTable.setStatus("current")
_CcPortalTxPktsEntry_Object = MibTableRow
ccPortalTxPktsEntry = _CcPortalTxPktsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 3, 1)
)
ccPortalTxPktsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    ccPortalTxPktsEntry.setStatus("current")
_CcPortalTxPktsAt1Mb_Type = Counter32
_CcPortalTxPktsAt1Mb_Object = MibTableColumn
ccPortalTxPktsAt1Mb = _CcPortalTxPktsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 3, 1, 1),
    _CcPortalTxPktsAt1Mb_Type()
)
ccPortalTxPktsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPktsAt1Mb.setStatus("current")
_CcPortalTxPktsAt2Mb_Type = Counter32
_CcPortalTxPktsAt2Mb_Object = MibTableColumn
ccPortalTxPktsAt2Mb = _CcPortalTxPktsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 3, 1, 2),
    _CcPortalTxPktsAt2Mb_Type()
)
ccPortalTxPktsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPktsAt2Mb.setStatus("current")
_CcPortalTxPktsAt5pt5Mb_Type = Counter32
_CcPortalTxPktsAt5pt5Mb_Object = MibTableColumn
ccPortalTxPktsAt5pt5Mb = _CcPortalTxPktsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 3, 1, 3),
    _CcPortalTxPktsAt5pt5Mb_Type()
)
ccPortalTxPktsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPktsAt5pt5Mb.setStatus("current")
_CcPortalTxPktsAt6Mb_Type = Counter32
_CcPortalTxPktsAt6Mb_Object = MibTableColumn
ccPortalTxPktsAt6Mb = _CcPortalTxPktsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 3, 1, 4),
    _CcPortalTxPktsAt6Mb_Type()
)
ccPortalTxPktsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPktsAt6Mb.setStatus("current")
_CcPortalTxPktsAt9Mb_Type = Counter32
_CcPortalTxPktsAt9Mb_Object = MibTableColumn
ccPortalTxPktsAt9Mb = _CcPortalTxPktsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 3, 1, 5),
    _CcPortalTxPktsAt9Mb_Type()
)
ccPortalTxPktsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPktsAt9Mb.setStatus("current")
_CcPortalTxPktsAt11Mb_Type = Counter32
_CcPortalTxPktsAt11Mb_Object = MibTableColumn
ccPortalTxPktsAt11Mb = _CcPortalTxPktsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 3, 1, 6),
    _CcPortalTxPktsAt11Mb_Type()
)
ccPortalTxPktsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPktsAt11Mb.setStatus("current")
_CcPortalTxPktsAt12Mb_Type = Counter32
_CcPortalTxPktsAt12Mb_Object = MibTableColumn
ccPortalTxPktsAt12Mb = _CcPortalTxPktsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 3, 1, 7),
    _CcPortalTxPktsAt12Mb_Type()
)
ccPortalTxPktsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPktsAt12Mb.setStatus("current")
_CcPortalTxPktsAt18Mb_Type = Counter32
_CcPortalTxPktsAt18Mb_Object = MibTableColumn
ccPortalTxPktsAt18Mb = _CcPortalTxPktsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 3, 1, 8),
    _CcPortalTxPktsAt18Mb_Type()
)
ccPortalTxPktsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPktsAt18Mb.setStatus("current")
_CcPortalTxPktsAt22Mb_Type = Counter32
_CcPortalTxPktsAt22Mb_Object = MibTableColumn
ccPortalTxPktsAt22Mb = _CcPortalTxPktsAt22Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 3, 1, 9),
    _CcPortalTxPktsAt22Mb_Type()
)
ccPortalTxPktsAt22Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPktsAt22Mb.setStatus("current")
_CcPortalTxPktsAt24Mb_Type = Counter32
_CcPortalTxPktsAt24Mb_Object = MibTableColumn
ccPortalTxPktsAt24Mb = _CcPortalTxPktsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 3, 1, 10),
    _CcPortalTxPktsAt24Mb_Type()
)
ccPortalTxPktsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPktsAt24Mb.setStatus("current")
_CcPortalTxPktsAt36Mb_Type = Counter32
_CcPortalTxPktsAt36Mb_Object = MibTableColumn
ccPortalTxPktsAt36Mb = _CcPortalTxPktsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 3, 1, 11),
    _CcPortalTxPktsAt36Mb_Type()
)
ccPortalTxPktsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPktsAt36Mb.setStatus("current")
_CcPortalTxPktsAt48Mb_Type = Counter32
_CcPortalTxPktsAt48Mb_Object = MibTableColumn
ccPortalTxPktsAt48Mb = _CcPortalTxPktsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 3, 1, 12),
    _CcPortalTxPktsAt48Mb_Type()
)
ccPortalTxPktsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPktsAt48Mb.setStatus("current")
_CcPortalTxPktsAt54Mb_Type = Counter32
_CcPortalTxPktsAt54Mb_Object = MibTableColumn
ccPortalTxPktsAt54Mb = _CcPortalTxPktsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 3, 1, 13),
    _CcPortalTxPktsAt54Mb_Type()
)
ccPortalTxPktsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxPktsAt54Mb.setStatus("current")
_CcPortalRxOctetsTable_Object = MibTable
ccPortalRxOctetsTable = _CcPortalRxOctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 4)
)
if mibBuilder.loadTexts:
    ccPortalRxOctetsTable.setStatus("current")
_CcPortalRxOctetsEntry_Object = MibTableRow
ccPortalRxOctetsEntry = _CcPortalRxOctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 4, 1)
)
ccPortalRxOctetsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    ccPortalRxOctetsEntry.setStatus("current")
_CcPortalRxOctetsAt1Mb_Type = Counter32
_CcPortalRxOctetsAt1Mb_Object = MibTableColumn
ccPortalRxOctetsAt1Mb = _CcPortalRxOctetsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 4, 1, 1),
    _CcPortalRxOctetsAt1Mb_Type()
)
ccPortalRxOctetsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsAt1Mb.setStatus("current")
_CcPortalRxOctetsAt2Mb_Type = Counter32
_CcPortalRxOctetsAt2Mb_Object = MibTableColumn
ccPortalRxOctetsAt2Mb = _CcPortalRxOctetsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 4, 1, 2),
    _CcPortalRxOctetsAt2Mb_Type()
)
ccPortalRxOctetsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsAt2Mb.setStatus("current")
_CcPortalRxOctetsAt5pt5Mb_Type = Counter32
_CcPortalRxOctetsAt5pt5Mb_Object = MibTableColumn
ccPortalRxOctetsAt5pt5Mb = _CcPortalRxOctetsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 4, 1, 3),
    _CcPortalRxOctetsAt5pt5Mb_Type()
)
ccPortalRxOctetsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsAt5pt5Mb.setStatus("current")
_CcPortalRxOctetsAt6Mb_Type = Counter32
_CcPortalRxOctetsAt6Mb_Object = MibTableColumn
ccPortalRxOctetsAt6Mb = _CcPortalRxOctetsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 4, 1, 4),
    _CcPortalRxOctetsAt6Mb_Type()
)
ccPortalRxOctetsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsAt6Mb.setStatus("current")
_CcPortalRxOctetsAt9Mb_Type = Counter32
_CcPortalRxOctetsAt9Mb_Object = MibTableColumn
ccPortalRxOctetsAt9Mb = _CcPortalRxOctetsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 4, 1, 5),
    _CcPortalRxOctetsAt9Mb_Type()
)
ccPortalRxOctetsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsAt9Mb.setStatus("current")
_CcPortalRxOctetsAt11Mb_Type = Counter32
_CcPortalRxOctetsAt11Mb_Object = MibTableColumn
ccPortalRxOctetsAt11Mb = _CcPortalRxOctetsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 4, 1, 6),
    _CcPortalRxOctetsAt11Mb_Type()
)
ccPortalRxOctetsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsAt11Mb.setStatus("current")
_CcPortalRxOctetsAt12Mb_Type = Counter32
_CcPortalRxOctetsAt12Mb_Object = MibTableColumn
ccPortalRxOctetsAt12Mb = _CcPortalRxOctetsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 4, 1, 7),
    _CcPortalRxOctetsAt12Mb_Type()
)
ccPortalRxOctetsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsAt12Mb.setStatus("current")
_CcPortalRxOctetsAt18Mb_Type = Counter32
_CcPortalRxOctetsAt18Mb_Object = MibTableColumn
ccPortalRxOctetsAt18Mb = _CcPortalRxOctetsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 4, 1, 8),
    _CcPortalRxOctetsAt18Mb_Type()
)
ccPortalRxOctetsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsAt18Mb.setStatus("current")
_CcPortalRxOctetsAt22Mb_Type = Counter32
_CcPortalRxOctetsAt22Mb_Object = MibTableColumn
ccPortalRxOctetsAt22Mb = _CcPortalRxOctetsAt22Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 4, 1, 9),
    _CcPortalRxOctetsAt22Mb_Type()
)
ccPortalRxOctetsAt22Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsAt22Mb.setStatus("current")
_CcPortalRxOctetsAt24Mb_Type = Counter32
_CcPortalRxOctetsAt24Mb_Object = MibTableColumn
ccPortalRxOctetsAt24Mb = _CcPortalRxOctetsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 4, 1, 10),
    _CcPortalRxOctetsAt24Mb_Type()
)
ccPortalRxOctetsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsAt24Mb.setStatus("current")
_CcPortalRxOctetsAt36Mb_Type = Counter32
_CcPortalRxOctetsAt36Mb_Object = MibTableColumn
ccPortalRxOctetsAt36Mb = _CcPortalRxOctetsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 4, 1, 11),
    _CcPortalRxOctetsAt36Mb_Type()
)
ccPortalRxOctetsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsAt36Mb.setStatus("current")
_CcPortalRxOctetsAt48Mb_Type = Counter32
_CcPortalRxOctetsAt48Mb_Object = MibTableColumn
ccPortalRxOctetsAt48Mb = _CcPortalRxOctetsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 4, 1, 12),
    _CcPortalRxOctetsAt48Mb_Type()
)
ccPortalRxOctetsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsAt48Mb.setStatus("current")
_CcPortalRxOctetsAt54Mb_Type = Counter32
_CcPortalRxOctetsAt54Mb_Object = MibTableColumn
ccPortalRxOctetsAt54Mb = _CcPortalRxOctetsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 4, 1, 13),
    _CcPortalRxOctetsAt54Mb_Type()
)
ccPortalRxOctetsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalRxOctetsAt54Mb.setStatus("current")
_CcPortalTxOctetsTable_Object = MibTable
ccPortalTxOctetsTable = _CcPortalTxOctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 5)
)
if mibBuilder.loadTexts:
    ccPortalTxOctetsTable.setStatus("current")
_CcPortalTxOctetsEntry_Object = MibTableRow
ccPortalTxOctetsEntry = _CcPortalTxOctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 5, 1)
)
ccPortalTxOctetsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    ccPortalTxOctetsEntry.setStatus("current")
_CcPortalTxOctetsAt1Mb_Type = Counter32
_CcPortalTxOctetsAt1Mb_Object = MibTableColumn
ccPortalTxOctetsAt1Mb = _CcPortalTxOctetsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 5, 1, 1),
    _CcPortalTxOctetsAt1Mb_Type()
)
ccPortalTxOctetsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxOctetsAt1Mb.setStatus("current")
_CcPortalTxOctetsAt2Mb_Type = Counter32
_CcPortalTxOctetsAt2Mb_Object = MibTableColumn
ccPortalTxOctetsAt2Mb = _CcPortalTxOctetsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 5, 1, 2),
    _CcPortalTxOctetsAt2Mb_Type()
)
ccPortalTxOctetsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxOctetsAt2Mb.setStatus("current")
_CcPortalTxOctetsAt5pt5Mb_Type = Counter32
_CcPortalTxOctetsAt5pt5Mb_Object = MibTableColumn
ccPortalTxOctetsAt5pt5Mb = _CcPortalTxOctetsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 5, 1, 3),
    _CcPortalTxOctetsAt5pt5Mb_Type()
)
ccPortalTxOctetsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxOctetsAt5pt5Mb.setStatus("current")
_CcPortalTxOctetsAt6Mb_Type = Counter32
_CcPortalTxOctetsAt6Mb_Object = MibTableColumn
ccPortalTxOctetsAt6Mb = _CcPortalTxOctetsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 5, 1, 4),
    _CcPortalTxOctetsAt6Mb_Type()
)
ccPortalTxOctetsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxOctetsAt6Mb.setStatus("current")
_CcPortalTxOctetsAt9Mb_Type = Counter32
_CcPortalTxOctetsAt9Mb_Object = MibTableColumn
ccPortalTxOctetsAt9Mb = _CcPortalTxOctetsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 5, 1, 5),
    _CcPortalTxOctetsAt9Mb_Type()
)
ccPortalTxOctetsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxOctetsAt9Mb.setStatus("current")
_CcPortalTxOctetsAt11Mb_Type = Counter32
_CcPortalTxOctetsAt11Mb_Object = MibTableColumn
ccPortalTxOctetsAt11Mb = _CcPortalTxOctetsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 5, 1, 6),
    _CcPortalTxOctetsAt11Mb_Type()
)
ccPortalTxOctetsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxOctetsAt11Mb.setStatus("current")
_CcPortalTxOctetsAt12Mb_Type = Counter32
_CcPortalTxOctetsAt12Mb_Object = MibTableColumn
ccPortalTxOctetsAt12Mb = _CcPortalTxOctetsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 5, 1, 7),
    _CcPortalTxOctetsAt12Mb_Type()
)
ccPortalTxOctetsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxOctetsAt12Mb.setStatus("current")
_CcPortalTxOctetsAt18Mb_Type = Counter32
_CcPortalTxOctetsAt18Mb_Object = MibTableColumn
ccPortalTxOctetsAt18Mb = _CcPortalTxOctetsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 5, 1, 8),
    _CcPortalTxOctetsAt18Mb_Type()
)
ccPortalTxOctetsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxOctetsAt18Mb.setStatus("current")
_CcPortalTxOctetsAt22Mb_Type = Counter32
_CcPortalTxOctetsAt22Mb_Object = MibTableColumn
ccPortalTxOctetsAt22Mb = _CcPortalTxOctetsAt22Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 5, 1, 9),
    _CcPortalTxOctetsAt22Mb_Type()
)
ccPortalTxOctetsAt22Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxOctetsAt22Mb.setStatus("current")
_CcPortalTxOctetsAt24Mb_Type = Counter32
_CcPortalTxOctetsAt24Mb_Object = MibTableColumn
ccPortalTxOctetsAt24Mb = _CcPortalTxOctetsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 5, 1, 10),
    _CcPortalTxOctetsAt24Mb_Type()
)
ccPortalTxOctetsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxOctetsAt24Mb.setStatus("current")
_CcPortalTxOctetsAt36Mb_Type = Counter32
_CcPortalTxOctetsAt36Mb_Object = MibTableColumn
ccPortalTxOctetsAt36Mb = _CcPortalTxOctetsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 5, 1, 11),
    _CcPortalTxOctetsAt36Mb_Type()
)
ccPortalTxOctetsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxOctetsAt36Mb.setStatus("current")
_CcPortalTxOctetsAt48Mb_Type = Counter32
_CcPortalTxOctetsAt48Mb_Object = MibTableColumn
ccPortalTxOctetsAt48Mb = _CcPortalTxOctetsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 5, 1, 12),
    _CcPortalTxOctetsAt48Mb_Type()
)
ccPortalTxOctetsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxOctetsAt48Mb.setStatus("current")
_CcPortalTxOctetsAt54Mb_Type = Counter32
_CcPortalTxOctetsAt54Mb_Object = MibTableColumn
ccPortalTxOctetsAt54Mb = _CcPortalTxOctetsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 5, 1, 13),
    _CcPortalTxOctetsAt54Mb_Type()
)
ccPortalTxOctetsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxOctetsAt54Mb.setStatus("current")
_CcPortalTxRetriesPktsTable_Object = MibTable
ccPortalTxRetriesPktsTable = _CcPortalTxRetriesPktsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 6)
)
if mibBuilder.loadTexts:
    ccPortalTxRetriesPktsTable.setStatus("current")
_CcPortalTxRetriesPktsEntry_Object = MibTableRow
ccPortalTxRetriesPktsEntry = _CcPortalTxRetriesPktsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 6, 1)
)
ccPortalTxRetriesPktsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    ccPortalTxRetriesPktsEntry.setStatus("current")
_CcPortalTxRetriesPktsNone_Type = Counter32
_CcPortalTxRetriesPktsNone_Object = MibTableColumn
ccPortalTxRetriesPktsNone = _CcPortalTxRetriesPktsNone_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 6, 1, 1),
    _CcPortalTxRetriesPktsNone_Type()
)
ccPortalTxRetriesPktsNone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPktsNone.setStatus("current")
_CcPortalTxRetriesPkts01_Type = Counter32
_CcPortalTxRetriesPkts01_Object = MibTableColumn
ccPortalTxRetriesPkts01 = _CcPortalTxRetriesPkts01_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 6, 1, 2),
    _CcPortalTxRetriesPkts01_Type()
)
ccPortalTxRetriesPkts01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts01.setStatus("current")
_CcPortalTxRetriesPkts02_Type = Counter32
_CcPortalTxRetriesPkts02_Object = MibTableColumn
ccPortalTxRetriesPkts02 = _CcPortalTxRetriesPkts02_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 6, 1, 3),
    _CcPortalTxRetriesPkts02_Type()
)
ccPortalTxRetriesPkts02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts02.setStatus("current")
_CcPortalTxRetriesPkts03_Type = Counter32
_CcPortalTxRetriesPkts03_Object = MibTableColumn
ccPortalTxRetriesPkts03 = _CcPortalTxRetriesPkts03_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 6, 1, 4),
    _CcPortalTxRetriesPkts03_Type()
)
ccPortalTxRetriesPkts03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts03.setStatus("current")
_CcPortalTxRetriesPkts04_Type = Counter32
_CcPortalTxRetriesPkts04_Object = MibTableColumn
ccPortalTxRetriesPkts04 = _CcPortalTxRetriesPkts04_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 6, 1, 5),
    _CcPortalTxRetriesPkts04_Type()
)
ccPortalTxRetriesPkts04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts04.setStatus("current")
_CcPortalTxRetriesPkts05_Type = Counter32
_CcPortalTxRetriesPkts05_Object = MibTableColumn
ccPortalTxRetriesPkts05 = _CcPortalTxRetriesPkts05_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 6, 1, 6),
    _CcPortalTxRetriesPkts05_Type()
)
ccPortalTxRetriesPkts05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts05.setStatus("current")
_CcPortalTxRetriesPkts06_Type = Counter32
_CcPortalTxRetriesPkts06_Object = MibTableColumn
ccPortalTxRetriesPkts06 = _CcPortalTxRetriesPkts06_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 6, 1, 7),
    _CcPortalTxRetriesPkts06_Type()
)
ccPortalTxRetriesPkts06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts06.setStatus("current")
_CcPortalTxRetriesPkts07_Type = Counter32
_CcPortalTxRetriesPkts07_Object = MibTableColumn
ccPortalTxRetriesPkts07 = _CcPortalTxRetriesPkts07_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 6, 1, 8),
    _CcPortalTxRetriesPkts07_Type()
)
ccPortalTxRetriesPkts07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts07.setStatus("current")
_CcPortalTxRetriesPkts08_Type = Counter32
_CcPortalTxRetriesPkts08_Object = MibTableColumn
ccPortalTxRetriesPkts08 = _CcPortalTxRetriesPkts08_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 6, 1, 9),
    _CcPortalTxRetriesPkts08_Type()
)
ccPortalTxRetriesPkts08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts08.setStatus("current")
_CcPortalTxRetriesPkts09_Type = Counter32
_CcPortalTxRetriesPkts09_Object = MibTableColumn
ccPortalTxRetriesPkts09 = _CcPortalTxRetriesPkts09_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 6, 1, 10),
    _CcPortalTxRetriesPkts09_Type()
)
ccPortalTxRetriesPkts09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts09.setStatus("current")
_CcPortalTxRetriesPkts10_Type = Counter32
_CcPortalTxRetriesPkts10_Object = MibTableColumn
ccPortalTxRetriesPkts10 = _CcPortalTxRetriesPkts10_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 6, 1, 11),
    _CcPortalTxRetriesPkts10_Type()
)
ccPortalTxRetriesPkts10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts10.setStatus("current")
_CcPortalTxRetriesPkts11_Type = Counter32
_CcPortalTxRetriesPkts11_Object = MibTableColumn
ccPortalTxRetriesPkts11 = _CcPortalTxRetriesPkts11_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 6, 1, 12),
    _CcPortalTxRetriesPkts11_Type()
)
ccPortalTxRetriesPkts11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts11.setStatus("current")
_CcPortalTxRetriesPkts12_Type = Counter32
_CcPortalTxRetriesPkts12_Object = MibTableColumn
ccPortalTxRetriesPkts12 = _CcPortalTxRetriesPkts12_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 6, 1, 13),
    _CcPortalTxRetriesPkts12_Type()
)
ccPortalTxRetriesPkts12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts12.setStatus("current")
_CcPortalTxRetriesPkts13_Type = Counter32
_CcPortalTxRetriesPkts13_Object = MibTableColumn
ccPortalTxRetriesPkts13 = _CcPortalTxRetriesPkts13_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 6, 1, 14),
    _CcPortalTxRetriesPkts13_Type()
)
ccPortalTxRetriesPkts13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts13.setStatus("current")
_CcPortalTxRetriesPkts14_Type = Counter32
_CcPortalTxRetriesPkts14_Object = MibTableColumn
ccPortalTxRetriesPkts14 = _CcPortalTxRetriesPkts14_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 6, 1, 15),
    _CcPortalTxRetriesPkts14_Type()
)
ccPortalTxRetriesPkts14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts14.setStatus("current")
_CcPortalTxRetriesPkts15_Type = Counter32
_CcPortalTxRetriesPkts15_Object = MibTableColumn
ccPortalTxRetriesPkts15 = _CcPortalTxRetriesPkts15_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 6, 1, 16),
    _CcPortalTxRetriesPkts15_Type()
)
ccPortalTxRetriesPkts15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPkts15.setStatus("current")
_CcPortalTxRetriesPktsFailed_Type = Counter32
_CcPortalTxRetriesPktsFailed_Object = MibTableColumn
ccPortalTxRetriesPktsFailed = _CcPortalTxRetriesPktsFailed_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 6, 1, 17),
    _CcPortalTxRetriesPktsFailed_Type()
)
ccPortalTxRetriesPktsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesPktsFailed.setStatus("current")
_CcPortalTxRetriesOctetsTable_Object = MibTable
ccPortalTxRetriesOctetsTable = _CcPortalTxRetriesOctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 7)
)
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctetsTable.setStatus("current")
_CcPortalTxRetriesOctetsEntry_Object = MibTableRow
ccPortalTxRetriesOctetsEntry = _CcPortalTxRetriesOctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 7, 1)
)
ccPortalTxRetriesOctetsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctetsEntry.setStatus("current")
_CcPortalTxRetriesOctetsNone_Type = Counter32
_CcPortalTxRetriesOctetsNone_Object = MibTableColumn
ccPortalTxRetriesOctetsNone = _CcPortalTxRetriesOctetsNone_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 7, 1, 1),
    _CcPortalTxRetriesOctetsNone_Type()
)
ccPortalTxRetriesOctetsNone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctetsNone.setStatus("current")
_CcPortalTxRetriesOctets01_Type = Counter32
_CcPortalTxRetriesOctets01_Object = MibTableColumn
ccPortalTxRetriesOctets01 = _CcPortalTxRetriesOctets01_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 7, 1, 2),
    _CcPortalTxRetriesOctets01_Type()
)
ccPortalTxRetriesOctets01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets01.setStatus("current")
_CcPortalTxRetriesOctets02_Type = Counter32
_CcPortalTxRetriesOctets02_Object = MibTableColumn
ccPortalTxRetriesOctets02 = _CcPortalTxRetriesOctets02_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 7, 1, 3),
    _CcPortalTxRetriesOctets02_Type()
)
ccPortalTxRetriesOctets02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets02.setStatus("current")
_CcPortalTxRetriesOctets03_Type = Counter32
_CcPortalTxRetriesOctets03_Object = MibTableColumn
ccPortalTxRetriesOctets03 = _CcPortalTxRetriesOctets03_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 7, 1, 4),
    _CcPortalTxRetriesOctets03_Type()
)
ccPortalTxRetriesOctets03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets03.setStatus("current")
_CcPortalTxRetriesOctets04_Type = Counter32
_CcPortalTxRetriesOctets04_Object = MibTableColumn
ccPortalTxRetriesOctets04 = _CcPortalTxRetriesOctets04_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 7, 1, 5),
    _CcPortalTxRetriesOctets04_Type()
)
ccPortalTxRetriesOctets04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets04.setStatus("current")
_CcPortalTxRetriesOctets05_Type = Counter32
_CcPortalTxRetriesOctets05_Object = MibTableColumn
ccPortalTxRetriesOctets05 = _CcPortalTxRetriesOctets05_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 7, 1, 6),
    _CcPortalTxRetriesOctets05_Type()
)
ccPortalTxRetriesOctets05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets05.setStatus("current")
_CcPortalTxRetriesOctets06_Type = Counter32
_CcPortalTxRetriesOctets06_Object = MibTableColumn
ccPortalTxRetriesOctets06 = _CcPortalTxRetriesOctets06_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 7, 1, 7),
    _CcPortalTxRetriesOctets06_Type()
)
ccPortalTxRetriesOctets06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets06.setStatus("current")
_CcPortalTxRetriesOctets07_Type = Counter32
_CcPortalTxRetriesOctets07_Object = MibTableColumn
ccPortalTxRetriesOctets07 = _CcPortalTxRetriesOctets07_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 7, 1, 8),
    _CcPortalTxRetriesOctets07_Type()
)
ccPortalTxRetriesOctets07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets07.setStatus("current")
_CcPortalTxRetriesOctets08_Type = Counter32
_CcPortalTxRetriesOctets08_Object = MibTableColumn
ccPortalTxRetriesOctets08 = _CcPortalTxRetriesOctets08_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 7, 1, 9),
    _CcPortalTxRetriesOctets08_Type()
)
ccPortalTxRetriesOctets08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets08.setStatus("current")
_CcPortalTxRetriesOctets09_Type = Counter32
_CcPortalTxRetriesOctets09_Object = MibTableColumn
ccPortalTxRetriesOctets09 = _CcPortalTxRetriesOctets09_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 7, 1, 10),
    _CcPortalTxRetriesOctets09_Type()
)
ccPortalTxRetriesOctets09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets09.setStatus("current")
_CcPortalTxRetriesOctets10_Type = Counter32
_CcPortalTxRetriesOctets10_Object = MibTableColumn
ccPortalTxRetriesOctets10 = _CcPortalTxRetriesOctets10_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 7, 1, 11),
    _CcPortalTxRetriesOctets10_Type()
)
ccPortalTxRetriesOctets10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets10.setStatus("current")
_CcPortalTxRetriesOctets11_Type = Counter32
_CcPortalTxRetriesOctets11_Object = MibTableColumn
ccPortalTxRetriesOctets11 = _CcPortalTxRetriesOctets11_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 7, 1, 12),
    _CcPortalTxRetriesOctets11_Type()
)
ccPortalTxRetriesOctets11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets11.setStatus("current")
_CcPortalTxRetriesOctets12_Type = Counter32
_CcPortalTxRetriesOctets12_Object = MibTableColumn
ccPortalTxRetriesOctets12 = _CcPortalTxRetriesOctets12_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 7, 1, 13),
    _CcPortalTxRetriesOctets12_Type()
)
ccPortalTxRetriesOctets12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets12.setStatus("current")
_CcPortalTxRetriesOctets13_Type = Counter32
_CcPortalTxRetriesOctets13_Object = MibTableColumn
ccPortalTxRetriesOctets13 = _CcPortalTxRetriesOctets13_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 7, 1, 14),
    _CcPortalTxRetriesOctets13_Type()
)
ccPortalTxRetriesOctets13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets13.setStatus("current")
_CcPortalTxRetriesOctets14_Type = Counter32
_CcPortalTxRetriesOctets14_Object = MibTableColumn
ccPortalTxRetriesOctets14 = _CcPortalTxRetriesOctets14_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 7, 1, 15),
    _CcPortalTxRetriesOctets14_Type()
)
ccPortalTxRetriesOctets14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets14.setStatus("current")
_CcPortalTxRetriesOctets15_Type = Counter32
_CcPortalTxRetriesOctets15_Object = MibTableColumn
ccPortalTxRetriesOctets15 = _CcPortalTxRetriesOctets15_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 7, 1, 16),
    _CcPortalTxRetriesOctets15_Type()
)
ccPortalTxRetriesOctets15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctets15.setStatus("current")
_CcPortalTxRetriesOctetsFailed_Type = Counter32
_CcPortalTxRetriesOctetsFailed_Object = MibTableColumn
ccPortalTxRetriesOctetsFailed = _CcPortalTxRetriesOctetsFailed_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 7, 1, 17),
    _CcPortalTxRetriesOctetsFailed_Type()
)
ccPortalTxRetriesOctetsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalTxRetriesOctetsFailed.setStatus("current")
_CcPortalSigStatsTable_Object = MibTable
ccPortalSigStatsTable = _CcPortalSigStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 8)
)
if mibBuilder.loadTexts:
    ccPortalSigStatsTable.setStatus("current")
_CcPortalSigStatsEntry_Object = MibTableRow
ccPortalSigStatsEntry = _CcPortalSigStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 8, 1)
)
ccPortalSigStatsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    ccPortalSigStatsEntry.setStatus("current")
_CcPortalSigStatsNumPkts_Type = Counter32
_CcPortalSigStatsNumPkts_Object = MibTableColumn
ccPortalSigStatsNumPkts = _CcPortalSigStatsNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 8, 1, 1),
    _CcPortalSigStatsNumPkts_Type()
)
ccPortalSigStatsNumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsNumPkts.setStatus("current")
_CcPortalSigStatsSignalBest_Type = Integer32
_CcPortalSigStatsSignalBest_Object = MibTableColumn
ccPortalSigStatsSignalBest = _CcPortalSigStatsSignalBest_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 8, 1, 2),
    _CcPortalSigStatsSignalBest_Type()
)
ccPortalSigStatsSignalBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsSignalBest.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsSignalBest.setUnits("dBm")
_CcPortalSigStatsSignalWorst_Type = Integer32
_CcPortalSigStatsSignalWorst_Object = MibTableColumn
ccPortalSigStatsSignalWorst = _CcPortalSigStatsSignalWorst_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 8, 1, 3),
    _CcPortalSigStatsSignalWorst_Type()
)
ccPortalSigStatsSignalWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsSignalWorst.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsSignalWorst.setUnits("dBm")
_CcPortalSigStatsSignalSum_Type = Integer32
_CcPortalSigStatsSignalSum_Object = MibTableColumn
ccPortalSigStatsSignalSum = _CcPortalSigStatsSignalSum_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 8, 1, 4),
    _CcPortalSigStatsSignalSum_Type()
)
ccPortalSigStatsSignalSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsSignalSum.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsSignalSum.setUnits("dBm")
_CcPortalSigStatsSignalSumSquares_Type = Counter64
_CcPortalSigStatsSignalSumSquares_Object = MibTableColumn
ccPortalSigStatsSignalSumSquares = _CcPortalSigStatsSignalSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 8, 1, 5),
    _CcPortalSigStatsSignalSumSquares_Type()
)
ccPortalSigStatsSignalSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsSignalSumSquares.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsSignalSumSquares.setUnits("dBm")
_CcPortalSigStatsSignalMostRecent_Type = Integer32
_CcPortalSigStatsSignalMostRecent_Object = MibTableColumn
ccPortalSigStatsSignalMostRecent = _CcPortalSigStatsSignalMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 8, 1, 6),
    _CcPortalSigStatsSignalMostRecent_Type()
)
ccPortalSigStatsSignalMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsSignalMostRecent.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsSignalMostRecent.setUnits("dBm")
_CcPortalSigStatsNoiseBest_Type = Integer32
_CcPortalSigStatsNoiseBest_Object = MibTableColumn
ccPortalSigStatsNoiseBest = _CcPortalSigStatsNoiseBest_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 8, 1, 7),
    _CcPortalSigStatsNoiseBest_Type()
)
ccPortalSigStatsNoiseBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsNoiseBest.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsNoiseBest.setUnits("dBm")
_CcPortalSigStatsNoiseWorst_Type = Integer32
_CcPortalSigStatsNoiseWorst_Object = MibTableColumn
ccPortalSigStatsNoiseWorst = _CcPortalSigStatsNoiseWorst_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 8, 1, 8),
    _CcPortalSigStatsNoiseWorst_Type()
)
ccPortalSigStatsNoiseWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsNoiseWorst.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsNoiseWorst.setUnits("dBm")
_CcPortalSigStatsNoiseSum_Type = Integer32
_CcPortalSigStatsNoiseSum_Object = MibTableColumn
ccPortalSigStatsNoiseSum = _CcPortalSigStatsNoiseSum_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 8, 1, 9),
    _CcPortalSigStatsNoiseSum_Type()
)
ccPortalSigStatsNoiseSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsNoiseSum.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsNoiseSum.setUnits("dBm")
_CcPortalSigStatsNoiseSumSquares_Type = Counter64
_CcPortalSigStatsNoiseSumSquares_Object = MibTableColumn
ccPortalSigStatsNoiseSumSquares = _CcPortalSigStatsNoiseSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 8, 1, 10),
    _CcPortalSigStatsNoiseSumSquares_Type()
)
ccPortalSigStatsNoiseSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsNoiseSumSquares.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsNoiseSumSquares.setUnits("dBm")
_CcPortalSigStatsNoiseMostRecent_Type = Integer32
_CcPortalSigStatsNoiseMostRecent_Object = MibTableColumn
ccPortalSigStatsNoiseMostRecent = _CcPortalSigStatsNoiseMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 8, 1, 11),
    _CcPortalSigStatsNoiseMostRecent_Type()
)
ccPortalSigStatsNoiseMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsNoiseMostRecent.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsNoiseMostRecent.setUnits("dBm")
_CcPortalSigStatsSnrBest_Type = Integer32
_CcPortalSigStatsSnrBest_Object = MibTableColumn
ccPortalSigStatsSnrBest = _CcPortalSigStatsSnrBest_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 8, 1, 12),
    _CcPortalSigStatsSnrBest_Type()
)
ccPortalSigStatsSnrBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsSnrBest.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsSnrBest.setUnits("dB")
_CcPortalSigStatsSnrWorst_Type = Integer32
_CcPortalSigStatsSnrWorst_Object = MibTableColumn
ccPortalSigStatsSnrWorst = _CcPortalSigStatsSnrWorst_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 8, 1, 13),
    _CcPortalSigStatsSnrWorst_Type()
)
ccPortalSigStatsSnrWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsSnrWorst.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsSnrWorst.setUnits("dB")
_CcPortalSigStatsSnrSum_Type = Integer32
_CcPortalSigStatsSnrSum_Object = MibTableColumn
ccPortalSigStatsSnrSum = _CcPortalSigStatsSnrSum_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 8, 1, 14),
    _CcPortalSigStatsSnrSum_Type()
)
ccPortalSigStatsSnrSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsSnrSum.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsSnrSum.setUnits("dB")
_CcPortalSigStatsSnrSumSquares_Type = Counter64
_CcPortalSigStatsSnrSumSquares_Object = MibTableColumn
ccPortalSigStatsSnrSumSquares = _CcPortalSigStatsSnrSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 8, 1, 15),
    _CcPortalSigStatsSnrSumSquares_Type()
)
ccPortalSigStatsSnrSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsSnrSumSquares.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsSnrSumSquares.setUnits("dB")
_CcPortalSigStatsSnrMostRecent_Type = Integer32
_CcPortalSigStatsSnrMostRecent_Object = MibTableColumn
ccPortalSigStatsSnrMostRecent = _CcPortalSigStatsSnrMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 8, 1, 16),
    _CcPortalSigStatsSnrMostRecent_Type()
)
ccPortalSigStatsSnrMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSigStatsSnrMostRecent.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSigStatsSnrMostRecent.setUnits("dB")
_CcPortalSumStatsShortTable_Object = MibTable
ccPortalSumStatsShortTable = _CcPortalSumStatsShortTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 9)
)
if mibBuilder.loadTexts:
    ccPortalSumStatsShortTable.setStatus("current")
_CcPortalSumStatsShortEntry_Object = MibTableRow
ccPortalSumStatsShortEntry = _CcPortalSumStatsShortEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 9, 1)
)
ccPortalSumStatsShortEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    ccPortalSumStatsShortEntry.setStatus("current")
_CcPortalSumStatsShortTimestamp_Type = TimeTicks
_CcPortalSumStatsShortTimestamp_Object = MibTableColumn
ccPortalSumStatsShortTimestamp = _CcPortalSumStatsShortTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 9, 1, 1),
    _CcPortalSumStatsShortTimestamp_Type()
)
ccPortalSumStatsShortTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortTimestamp.setStatus("current")
_CcPortalSumStatsShortNumPkts_Type = Unsigned32
_CcPortalSumStatsShortNumPkts_Object = MibTableColumn
ccPortalSumStatsShortNumPkts = _CcPortalSumStatsShortNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 9, 1, 2),
    _CcPortalSumStatsShortNumPkts_Type()
)
ccPortalSumStatsShortNumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortNumPkts.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortNumPkts.setUnits("packets")
_CcPortalSumStatsShortPktsPerSec100_Type = ScaleBy100
_CcPortalSumStatsShortPktsPerSec100_Object = MibTableColumn
ccPortalSumStatsShortPktsPerSec100 = _CcPortalSumStatsShortPktsPerSec100_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 9, 1, 3),
    _CcPortalSumStatsShortPktsPerSec100_Type()
)
ccPortalSumStatsShortPktsPerSec100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPktsPerSec100.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPktsPerSec100.setUnits("pkts per sec x100")
_CcPortalSumStatsShortPktsPerSecTx100_Type = ScaleBy100
_CcPortalSumStatsShortPktsPerSecTx100_Object = MibTableColumn
ccPortalSumStatsShortPktsPerSecTx100 = _CcPortalSumStatsShortPktsPerSecTx100_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 9, 1, 4),
    _CcPortalSumStatsShortPktsPerSecTx100_Type()
)
ccPortalSumStatsShortPktsPerSecTx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPktsPerSecTx100.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPktsPerSecTx100.setUnits("pkts per sec x100")
_CcPortalSumStatsShortPktsPerSecRx100_Type = ScaleBy100
_CcPortalSumStatsShortPktsPerSecRx100_Object = MibTableColumn
ccPortalSumStatsShortPktsPerSecRx100 = _CcPortalSumStatsShortPktsPerSecRx100_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 9, 1, 5),
    _CcPortalSumStatsShortPktsPerSecRx100_Type()
)
ccPortalSumStatsShortPktsPerSecRx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPktsPerSecRx100.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPktsPerSecRx100.setUnits("pkts per sec x100")
_CcPortalSumStatsShortThroughput_Type = Unsigned32
_CcPortalSumStatsShortThroughput_Object = MibTableColumn
ccPortalSumStatsShortThroughput = _CcPortalSumStatsShortThroughput_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 9, 1, 6),
    _CcPortalSumStatsShortThroughput_Type()
)
ccPortalSumStatsShortThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortThroughput.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortThroughput.setUnits("bits per second")
_CcPortalSumStatsShortThroughputTx_Type = Unsigned32
_CcPortalSumStatsShortThroughputTx_Object = MibTableColumn
ccPortalSumStatsShortThroughputTx = _CcPortalSumStatsShortThroughputTx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 9, 1, 7),
    _CcPortalSumStatsShortThroughputTx_Type()
)
ccPortalSumStatsShortThroughputTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortThroughputTx.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortThroughputTx.setUnits("bits per second")
_CcPortalSumStatsShortThroughputRx_Type = Unsigned32
_CcPortalSumStatsShortThroughputRx_Object = MibTableColumn
ccPortalSumStatsShortThroughputRx = _CcPortalSumStatsShortThroughputRx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 9, 1, 8),
    _CcPortalSumStatsShortThroughputRx_Type()
)
ccPortalSumStatsShortThroughputRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortThroughputRx.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortThroughputRx.setUnits("bits per second")
_CcPortalSumStatsShortAvgBitSpeed_Type = Unsigned32
_CcPortalSumStatsShortAvgBitSpeed_Object = MibTableColumn
ccPortalSumStatsShortAvgBitSpeed = _CcPortalSumStatsShortAvgBitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 9, 1, 9),
    _CcPortalSumStatsShortAvgBitSpeed_Type()
)
ccPortalSumStatsShortAvgBitSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortAvgBitSpeed.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortAvgBitSpeed.setUnits("bits per second")
_CcPortalSumStatsShortAvgMuSignal_Type = Integer32
_CcPortalSumStatsShortAvgMuSignal_Object = MibTableColumn
ccPortalSumStatsShortAvgMuSignal = _CcPortalSumStatsShortAvgMuSignal_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 9, 1, 10),
    _CcPortalSumStatsShortAvgMuSignal_Type()
)
ccPortalSumStatsShortAvgMuSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortAvgMuSignal.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortAvgMuSignal.setUnits("dBm")
_CcPortalSumStatsShortAvgMuNoise_Type = Integer32
_CcPortalSumStatsShortAvgMuNoise_Object = MibTableColumn
ccPortalSumStatsShortAvgMuNoise = _CcPortalSumStatsShortAvgMuNoise_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 9, 1, 11),
    _CcPortalSumStatsShortAvgMuNoise_Type()
)
ccPortalSumStatsShortAvgMuNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortAvgMuNoise.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortAvgMuNoise.setUnits("dBm")
_CcPortalSumStatsShortAvgMuSnr_Type = Integer32
_CcPortalSumStatsShortAvgMuSnr_Object = MibTableColumn
ccPortalSumStatsShortAvgMuSnr = _CcPortalSumStatsShortAvgMuSnr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 9, 1, 12),
    _CcPortalSumStatsShortAvgMuSnr_Type()
)
ccPortalSumStatsShortAvgMuSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortAvgMuSnr.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortAvgMuSnr.setUnits("dB")
_CcPortalSumStatsShortPp10kNUcastPkts_Type = PartsPer10k
_CcPortalSumStatsShortPp10kNUcastPkts_Object = MibTableColumn
ccPortalSumStatsShortPp10kNUcastPkts = _CcPortalSumStatsShortPp10kNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 9, 1, 13),
    _CcPortalSumStatsShortPp10kNUcastPkts_Type()
)
ccPortalSumStatsShortPp10kNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPp10kNUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPp10kNUcastPkts.setUnits("parts-per-10000")
_CcPortalSumStatsShortPp10kTxWithRetries_Type = PartsPer10k
_CcPortalSumStatsShortPp10kTxWithRetries_Object = MibTableColumn
ccPortalSumStatsShortPp10kTxWithRetries = _CcPortalSumStatsShortPp10kTxWithRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 9, 1, 14),
    _CcPortalSumStatsShortPp10kTxWithRetries_Type()
)
ccPortalSumStatsShortPp10kTxWithRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPp10kTxWithRetries.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPp10kTxWithRetries.setUnits("parts-per-10000")
_CcPortalSumStatsShortPp10kTxMaxRetries_Type = PartsPer10k
_CcPortalSumStatsShortPp10kTxMaxRetries_Object = MibTableColumn
ccPortalSumStatsShortPp10kTxMaxRetries = _CcPortalSumStatsShortPp10kTxMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 9, 1, 15),
    _CcPortalSumStatsShortPp10kTxMaxRetries_Type()
)
ccPortalSumStatsShortPp10kTxMaxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPp10kTxMaxRetries.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPp10kTxMaxRetries.setUnits("parts-per-10000")
_CcPortalSumStatsShortTxAvgRetries100_Type = ScaleBy100
_CcPortalSumStatsShortTxAvgRetries100_Object = MibTableColumn
ccPortalSumStatsShortTxAvgRetries100 = _CcPortalSumStatsShortTxAvgRetries100_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 9, 1, 16),
    _CcPortalSumStatsShortTxAvgRetries100_Type()
)
ccPortalSumStatsShortTxAvgRetries100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortTxAvgRetries100.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortTxAvgRetries100.setUnits("average x100")
_CcPortalSumStatsShortPp10kRxUndecrypt_Type = PartsPer10k
_CcPortalSumStatsShortPp10kRxUndecrypt_Object = MibTableColumn
ccPortalSumStatsShortPp10kRxUndecrypt = _CcPortalSumStatsShortPp10kRxUndecrypt_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 9, 1, 17),
    _CcPortalSumStatsShortPp10kRxUndecrypt_Type()
)
ccPortalSumStatsShortPp10kRxUndecrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPp10kRxUndecrypt.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPp10kRxUndecrypt.setUnits("parts-per-10000")


class _CcPortalSumStatsShortTotalMus_Type(Unsigned32):
    """Custom type ccPortalSumStatsShortTotalMus based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CcPortalSumStatsShortTotalMus_Type.__name__ = "Unsigned32"
_CcPortalSumStatsShortTotalMus_Object = MibTableColumn
ccPortalSumStatsShortTotalMus = _CcPortalSumStatsShortTotalMus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 9, 1, 18),
    _CcPortalSumStatsShortTotalMus_Type()
)
ccPortalSumStatsShortTotalMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortTotalMus.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortTotalMus.setUnits("number of MUs")
_CcPortalSumStatsShortPp10kRfUtil_Type = PartsPer10k
_CcPortalSumStatsShortPp10kRfUtil_Object = MibTableColumn
ccPortalSumStatsShortPp10kRfUtil = _CcPortalSumStatsShortPp10kRfUtil_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 9, 1, 19),
    _CcPortalSumStatsShortPp10kRfUtil_Type()
)
ccPortalSumStatsShortPp10kRfUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPp10kRfUtil.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsShortPp10kRfUtil.setUnits("parts-per-10000")
_CcPortalSumStatsLongTable_Object = MibTable
ccPortalSumStatsLongTable = _CcPortalSumStatsLongTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 10)
)
if mibBuilder.loadTexts:
    ccPortalSumStatsLongTable.setStatus("current")
_CcPortalSumStatsLongEntry_Object = MibTableRow
ccPortalSumStatsLongEntry = _CcPortalSumStatsLongEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 10, 1)
)
ccPortalSumStatsLongEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    ccPortalSumStatsLongEntry.setStatus("current")
_CcPortalSumStatsLongTimestamp_Type = TimeTicks
_CcPortalSumStatsLongTimestamp_Object = MibTableColumn
ccPortalSumStatsLongTimestamp = _CcPortalSumStatsLongTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 10, 1, 1),
    _CcPortalSumStatsLongTimestamp_Type()
)
ccPortalSumStatsLongTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongTimestamp.setStatus("current")
_CcPortalSumStatsLongNumPkts_Type = Unsigned32
_CcPortalSumStatsLongNumPkts_Object = MibTableColumn
ccPortalSumStatsLongNumPkts = _CcPortalSumStatsLongNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 10, 1, 2),
    _CcPortalSumStatsLongNumPkts_Type()
)
ccPortalSumStatsLongNumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongNumPkts.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongNumPkts.setUnits("packets")
_CcPortalSumStatsLongPktsPerSec100_Type = ScaleBy100
_CcPortalSumStatsLongPktsPerSec100_Object = MibTableColumn
ccPortalSumStatsLongPktsPerSec100 = _CcPortalSumStatsLongPktsPerSec100_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 10, 1, 3),
    _CcPortalSumStatsLongPktsPerSec100_Type()
)
ccPortalSumStatsLongPktsPerSec100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPktsPerSec100.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPktsPerSec100.setUnits("pkts per sec x100")
_CcPortalSumStatsLongPktsPerSecTx100_Type = ScaleBy100
_CcPortalSumStatsLongPktsPerSecTx100_Object = MibTableColumn
ccPortalSumStatsLongPktsPerSecTx100 = _CcPortalSumStatsLongPktsPerSecTx100_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 10, 1, 4),
    _CcPortalSumStatsLongPktsPerSecTx100_Type()
)
ccPortalSumStatsLongPktsPerSecTx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPktsPerSecTx100.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPktsPerSecTx100.setUnits("pkts per sec x100")
_CcPortalSumStatsLongPktsPerSecRx100_Type = ScaleBy100
_CcPortalSumStatsLongPktsPerSecRx100_Object = MibTableColumn
ccPortalSumStatsLongPktsPerSecRx100 = _CcPortalSumStatsLongPktsPerSecRx100_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 10, 1, 5),
    _CcPortalSumStatsLongPktsPerSecRx100_Type()
)
ccPortalSumStatsLongPktsPerSecRx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPktsPerSecRx100.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPktsPerSecRx100.setUnits("pkts per sec x100")
_CcPortalSumStatsLongThroughput_Type = Unsigned32
_CcPortalSumStatsLongThroughput_Object = MibTableColumn
ccPortalSumStatsLongThroughput = _CcPortalSumStatsLongThroughput_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 10, 1, 6),
    _CcPortalSumStatsLongThroughput_Type()
)
ccPortalSumStatsLongThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongThroughput.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongThroughput.setUnits("bits per second")
_CcPortalSumStatsLongThroughputTx_Type = Unsigned32
_CcPortalSumStatsLongThroughputTx_Object = MibTableColumn
ccPortalSumStatsLongThroughputTx = _CcPortalSumStatsLongThroughputTx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 10, 1, 7),
    _CcPortalSumStatsLongThroughputTx_Type()
)
ccPortalSumStatsLongThroughputTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongThroughputTx.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongThroughputTx.setUnits("bits per second")
_CcPortalSumStatsLongThroughputRx_Type = Unsigned32
_CcPortalSumStatsLongThroughputRx_Object = MibTableColumn
ccPortalSumStatsLongThroughputRx = _CcPortalSumStatsLongThroughputRx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 10, 1, 8),
    _CcPortalSumStatsLongThroughputRx_Type()
)
ccPortalSumStatsLongThroughputRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongThroughputRx.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongThroughputRx.setUnits("bits per second")
_CcPortalSumStatsLongAvgBitSpeed_Type = Unsigned32
_CcPortalSumStatsLongAvgBitSpeed_Object = MibTableColumn
ccPortalSumStatsLongAvgBitSpeed = _CcPortalSumStatsLongAvgBitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 10, 1, 9),
    _CcPortalSumStatsLongAvgBitSpeed_Type()
)
ccPortalSumStatsLongAvgBitSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongAvgBitSpeed.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongAvgBitSpeed.setUnits("bits per second")
_CcPortalSumStatsLongAvgMuSignal_Type = Integer32
_CcPortalSumStatsLongAvgMuSignal_Object = MibTableColumn
ccPortalSumStatsLongAvgMuSignal = _CcPortalSumStatsLongAvgMuSignal_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 10, 1, 10),
    _CcPortalSumStatsLongAvgMuSignal_Type()
)
ccPortalSumStatsLongAvgMuSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongAvgMuSignal.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongAvgMuSignal.setUnits("dBm")
_CcPortalSumStatsLongAvgMuNoise_Type = Integer32
_CcPortalSumStatsLongAvgMuNoise_Object = MibTableColumn
ccPortalSumStatsLongAvgMuNoise = _CcPortalSumStatsLongAvgMuNoise_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 10, 1, 11),
    _CcPortalSumStatsLongAvgMuNoise_Type()
)
ccPortalSumStatsLongAvgMuNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongAvgMuNoise.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongAvgMuNoise.setUnits("dBm")
_CcPortalSumStatsLongAvgMuSnr_Type = Integer32
_CcPortalSumStatsLongAvgMuSnr_Object = MibTableColumn
ccPortalSumStatsLongAvgMuSnr = _CcPortalSumStatsLongAvgMuSnr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 10, 1, 12),
    _CcPortalSumStatsLongAvgMuSnr_Type()
)
ccPortalSumStatsLongAvgMuSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongAvgMuSnr.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongAvgMuSnr.setUnits("dB")
_CcPortalSumStatsLongPp10kNUcastPkts_Type = PartsPer10k
_CcPortalSumStatsLongPp10kNUcastPkts_Object = MibTableColumn
ccPortalSumStatsLongPp10kNUcastPkts = _CcPortalSumStatsLongPp10kNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 10, 1, 13),
    _CcPortalSumStatsLongPp10kNUcastPkts_Type()
)
ccPortalSumStatsLongPp10kNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPp10kNUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPp10kNUcastPkts.setUnits("parts-per-10000")
_CcPortalSumStatsLongPp10kTxWithRetries_Type = PartsPer10k
_CcPortalSumStatsLongPp10kTxWithRetries_Object = MibTableColumn
ccPortalSumStatsLongPp10kTxWithRetries = _CcPortalSumStatsLongPp10kTxWithRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 10, 1, 14),
    _CcPortalSumStatsLongPp10kTxWithRetries_Type()
)
ccPortalSumStatsLongPp10kTxWithRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPp10kTxWithRetries.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPp10kTxWithRetries.setUnits("parts-per-10000")
_CcPortalSumStatsLongPp10kTxMaxRetries_Type = PartsPer10k
_CcPortalSumStatsLongPp10kTxMaxRetries_Object = MibTableColumn
ccPortalSumStatsLongPp10kTxMaxRetries = _CcPortalSumStatsLongPp10kTxMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 10, 1, 15),
    _CcPortalSumStatsLongPp10kTxMaxRetries_Type()
)
ccPortalSumStatsLongPp10kTxMaxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPp10kTxMaxRetries.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPp10kTxMaxRetries.setUnits("parts-per-10000")
_CcPortalSumStatsLongTxAvgRetries100_Type = ScaleBy100
_CcPortalSumStatsLongTxAvgRetries100_Object = MibTableColumn
ccPortalSumStatsLongTxAvgRetries100 = _CcPortalSumStatsLongTxAvgRetries100_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 10, 1, 16),
    _CcPortalSumStatsLongTxAvgRetries100_Type()
)
ccPortalSumStatsLongTxAvgRetries100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongTxAvgRetries100.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongTxAvgRetries100.setUnits("average x100")
_CcPortalSumStatsLongPp10kRxUndecrypt_Type = PartsPer10k
_CcPortalSumStatsLongPp10kRxUndecrypt_Object = MibTableColumn
ccPortalSumStatsLongPp10kRxUndecrypt = _CcPortalSumStatsLongPp10kRxUndecrypt_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 10, 1, 17),
    _CcPortalSumStatsLongPp10kRxUndecrypt_Type()
)
ccPortalSumStatsLongPp10kRxUndecrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPp10kRxUndecrypt.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPp10kRxUndecrypt.setUnits("parts-per-10000")


class _CcPortalSumStatsLongTotalMus_Type(Unsigned32):
    """Custom type ccPortalSumStatsLongTotalMus based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CcPortalSumStatsLongTotalMus_Type.__name__ = "Unsigned32"
_CcPortalSumStatsLongTotalMus_Object = MibTableColumn
ccPortalSumStatsLongTotalMus = _CcPortalSumStatsLongTotalMus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 10, 1, 18),
    _CcPortalSumStatsLongTotalMus_Type()
)
ccPortalSumStatsLongTotalMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongTotalMus.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongTotalMus.setUnits("number of MUs")
_CcPortalSumStatsLongPp10kRfUtil_Type = PartsPer10k
_CcPortalSumStatsLongPp10kRfUtil_Object = MibTableColumn
ccPortalSumStatsLongPp10kRfUtil = _CcPortalSumStatsLongPp10kRfUtil_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 2, 100, 10, 1, 19),
    _CcPortalSumStatsLongPp10kRfUtil_Type()
)
ccPortalSumStatsLongPp10kRfUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPp10kRfUtil.setStatus("current")
if mibBuilder.loadTexts:
    ccPortalSumStatsLongPp10kRfUtil.setUnits("parts-per-10000")
_CcAssociation_ObjectIdentity = ObjectIdentity
ccAssociation = _CcAssociation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 3)
)
_CcAssociationTable_Object = MibTable
ccAssociationTable = _CcAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 3, 1)
)
if mibBuilder.loadTexts:
    ccAssociationTable.setStatus("current")
_CcAssociationEntry_Object = MibTableRow
ccAssociationEntry = _CcAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 3, 1, 1)
)
ccAssociationEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccPortalIndex"),
    (0, "SYMBOL-CC-WS2000-MIB", "ccMuMac"),
)
if mibBuilder.loadTexts:
    ccAssociationEntry.setStatus("current")
_CcAssociationFirstAssociate_Type = TimeTicks
_CcAssociationFirstAssociate_Object = MibTableColumn
ccAssociationFirstAssociate = _CcAssociationFirstAssociate_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 3, 1, 1, 1),
    _CcAssociationFirstAssociate_Type()
)
ccAssociationFirstAssociate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccAssociationFirstAssociate.setStatus("current")
_CcAssociationLastAssociate_Type = TimeTicks
_CcAssociationLastAssociate_Object = MibTableColumn
ccAssociationLastAssociate = _CcAssociationLastAssociate_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 3, 1, 1, 2),
    _CcAssociationLastAssociate_Type()
)
ccAssociationLastAssociate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccAssociationLastAssociate.setStatus("current")
_CcAssociationCountAssociates_Type = Counter32
_CcAssociationCountAssociates_Object = MibTableColumn
ccAssociationCountAssociates = _CcAssociationCountAssociates_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 3, 1, 1, 3),
    _CcAssociationCountAssociates_Type()
)
ccAssociationCountAssociates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccAssociationCountAssociates.setStatus("current")
_CcMus_ObjectIdentity = ObjectIdentity
ccMus = _CcMus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4)
)
_CcMuInfoTable_Object = MibTable
ccMuInfoTable = _CcMuInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 1)
)
if mibBuilder.loadTexts:
    ccMuInfoTable.setStatus("current")
_CcMuInfoEntry_Object = MibTableRow
ccMuInfoEntry = _CcMuInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 1, 1)
)
ccMuInfoEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccMuMac"),
)
if mibBuilder.loadTexts:
    ccMuInfoEntry.setStatus("current")
_CcMuMac_Type = PhysAddress
_CcMuMac_Object = MibTableColumn
ccMuMac = _CcMuMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 1, 1, 1),
    _CcMuMac_Type()
)
ccMuMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuMac.setStatus("current")


class _CcMuWlanIndex_Type(Integer32):
    """Custom type ccMuWlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CcMuWlanIndex_Type.__name__ = "Integer32"
_CcMuWlanIndex_Object = MibTableColumn
ccMuWlanIndex = _CcMuWlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 1, 1, 2),
    _CcMuWlanIndex_Type()
)
ccMuWlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuWlanIndex.setStatus("current")
_CcMuWlanName_Type = DisplayString
_CcMuWlanName_Object = MibTableColumn
ccMuWlanName = _CcMuWlanName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 1, 1, 3),
    _CcMuWlanName_Type()
)
ccMuWlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuWlanName.setStatus("current")
_CcMuIsDataReady_Type = TruthValue
_CcMuIsDataReady_Object = MibTableColumn
ccMuIsDataReady = _CcMuIsDataReady_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 1, 1, 4),
    _CcMuIsDataReady_Type()
)
ccMuIsDataReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuIsDataReady.setStatus("current")


class _CcMuPortalIndex_Type(Integer32):
    """Custom type ccMuPortalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CcMuPortalIndex_Type.__name__ = "Integer32"
_CcMuPortalIndex_Object = MibTableColumn
ccMuPortalIndex = _CcMuPortalIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 1, 1, 5),
    _CcMuPortalIndex_Type()
)
ccMuPortalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuPortalIndex.setStatus("current")
_CcMuPortalMac_Type = PhysAddress
_CcMuPortalMac_Object = MibTableColumn
ccMuPortalMac = _CcMuPortalMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 1, 1, 6),
    _CcMuPortalMac_Type()
)
ccMuPortalMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuPortalMac.setStatus("current")
_CcMuSymbolRogueApEna_Type = TruthValue
_CcMuSymbolRogueApEna_Object = MibTableColumn
ccMuSymbolRogueApEna = _CcMuSymbolRogueApEna_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 1, 1, 7),
    _CcMuSymbolRogueApEna_Type()
)
ccMuSymbolRogueApEna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSymbolRogueApEna.setStatus("current")
_CcMuIpAddr_Type = IpAddress
_CcMuIpAddr_Object = MibTableColumn
ccMuIpAddr = _CcMuIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 1, 1, 8),
    _CcMuIpAddr_Type()
)
ccMuIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuIpAddr.setStatus("current")


class _CcMuType_Type(Integer32):
    """Custom type ccMuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accessPoint", 3),
          ("data", 1),
          ("voice", 2))
    )


_CcMuType_Type.__name__ = "Integer32"
_CcMuType_Object = MibTableColumn
ccMuType = _CcMuType_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 1, 1, 9),
    _CcMuType_Type()
)
ccMuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuType.setStatus("current")
_CcMuRadioType_Type = RadioType
_CcMuRadioType_Object = MibTableColumn
ccMuRadioType = _CcMuRadioType_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 1, 1, 10),
    _CcMuRadioType_Type()
)
ccMuRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRadioType.setStatus("current")


class _CcMuSupportedRates_Type(Bits):
    """Custom type ccMuSupportedRates based on Bits"""
    namedValues = NamedValues(
        *(("supports11Mb", 5),
          ("supports12Mb", 6),
          ("supports18Mb", 7),
          ("supports1Mb", 0),
          ("supports22Mb", 8),
          ("supports24Mb", 9),
          ("supports2Mb", 1),
          ("supports36Mb", 10),
          ("supports48Mb", 11),
          ("supports54Mb", 12),
          ("supports5dot5Mb", 2),
          ("supports6Mb", 3),
          ("supports9Mb", 4))
    )

_CcMuSupportedRates_Type.__name__ = "Bits"
_CcMuSupportedRates_Object = MibTableColumn
ccMuSupportedRates = _CcMuSupportedRates_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 1, 1, 11),
    _CcMuSupportedRates_Type()
)
ccMuSupportedRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSupportedRates.setStatus("current")


class _CcMuPowerMode_Type(Integer32):
    """Custom type ccMuPowerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("continuousAccessMode", 1),
          ("powerSavePolling", 2))
    )


_CcMuPowerMode_Type.__name__ = "Integer32"
_CcMuPowerMode_Object = MibTableColumn
ccMuPowerMode = _CcMuPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 1, 1, 12),
    _CcMuPowerMode_Type()
)
ccMuPowerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuPowerMode.setStatus("current")


class _CcMuAuthenticationMethod_Type(Integer32):
    """Custom type ccMuAuthenticationMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eap802dot1x", 2),
          ("kerberos", 3),
          ("none", 1))
    )


_CcMuAuthenticationMethod_Type.__name__ = "Integer32"
_CcMuAuthenticationMethod_Object = MibTableColumn
ccMuAuthenticationMethod = _CcMuAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 1, 1, 13),
    _CcMuAuthenticationMethod_Type()
)
ccMuAuthenticationMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuAuthenticationMethod.setStatus("current")


class _CcMuEncryptionMethod_Type(Integer32):
    """Custom type ccMuEncryptionMethod based on Integer32"""
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
        *(("keyGuardMCM", 4),
          ("none", 1),
          ("wep128", 3),
          ("wep40", 2),
          ("wpa2AesCcmp", 6),
          ("wpaTKIP", 5))
    )


_CcMuEncryptionMethod_Type.__name__ = "Integer32"
_CcMuEncryptionMethod_Object = MibTableColumn
ccMuEncryptionMethod = _CcMuEncryptionMethod_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 1, 1, 14),
    _CcMuEncryptionMethod_Type()
)
ccMuEncryptionMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuEncryptionMethod.setStatus("current")


class _CcMuVlanId_Type(Unsigned32):
    """Custom type ccMuVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_CcMuVlanId_Type.__name__ = "Unsigned32"
_CcMuVlanId_Object = MibTableColumn
ccMuVlanId = _CcMuVlanId_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 1, 1, 15),
    _CcMuVlanId_Type()
)
ccMuVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuVlanId.setStatus("current")
_CcMuStatsTable_Object = MibTable
ccMuStatsTable = _CcMuStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 2)
)
if mibBuilder.loadTexts:
    ccMuStatsTable.setStatus("current")
_CcMuStatsEntry_Object = MibTableRow
ccMuStatsEntry = _CcMuStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 2, 1)
)
ccMuStatsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccMuMac"),
)
if mibBuilder.loadTexts:
    ccMuStatsEntry.setStatus("current")
_CcMuTxPktsUcast_Type = Counter32
_CcMuTxPktsUcast_Object = MibTableColumn
ccMuTxPktsUcast = _CcMuTxPktsUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 2, 1, 1),
    _CcMuTxPktsUcast_Type()
)
ccMuTxPktsUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxPktsUcast.setStatus("current")
_CcMuRxPktsUcast_Type = Counter32
_CcMuRxPktsUcast_Object = MibTableColumn
ccMuRxPktsUcast = _CcMuRxPktsUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 2, 1, 2),
    _CcMuRxPktsUcast_Type()
)
ccMuRxPktsUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsUcast.setStatus("current")
_CcMuRxPktsNUcast_Type = Counter32
_CcMuRxPktsNUcast_Object = MibTableColumn
ccMuRxPktsNUcast = _CcMuRxPktsNUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 2, 1, 3),
    _CcMuRxPktsNUcast_Type()
)
ccMuRxPktsNUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsNUcast.setStatus("obsolete")
_CcMuTxOctetsUcast_Type = Counter32
_CcMuTxOctetsUcast_Object = MibTableColumn
ccMuTxOctetsUcast = _CcMuTxOctetsUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 2, 1, 4),
    _CcMuTxOctetsUcast_Type()
)
ccMuTxOctetsUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxOctetsUcast.setStatus("current")
_CcMuRxOctetsUcast_Type = Counter32
_CcMuRxOctetsUcast_Object = MibTableColumn
ccMuRxOctetsUcast = _CcMuRxOctetsUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 2, 1, 5),
    _CcMuRxOctetsUcast_Type()
)
ccMuRxOctetsUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsUcast.setStatus("current")
_CcMuRxOctetsNUcast_Type = Counter32
_CcMuRxOctetsNUcast_Object = MibTableColumn
ccMuRxOctetsNUcast = _CcMuRxOctetsNUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 2, 1, 6),
    _CcMuRxOctetsNUcast_Type()
)
ccMuRxOctetsNUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsNUcast.setStatus("obsolete")
_CcMuRxUndecryptablePkts_Type = Counter32
_CcMuRxUndecryptablePkts_Object = MibTableColumn
ccMuRxUndecryptablePkts = _CcMuRxUndecryptablePkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 2, 1, 7),
    _CcMuRxUndecryptablePkts_Type()
)
ccMuRxUndecryptablePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxUndecryptablePkts.setStatus("current")
_CcMuRxRssiNumPkts_Type = Counter32
_CcMuRxRssiNumPkts_Object = MibTableColumn
ccMuRxRssiNumPkts = _CcMuRxRssiNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 2, 1, 8),
    _CcMuRxRssiNumPkts_Type()
)
ccMuRxRssiNumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxRssiNumPkts.setStatus("current")
_CcMuRxRssiSum_Type = Counter32
_CcMuRxRssiSum_Object = MibTableColumn
ccMuRxRssiSum = _CcMuRxRssiSum_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 2, 1, 9),
    _CcMuRxRssiSum_Type()
)
ccMuRxRssiSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxRssiSum.setStatus("current")
_CcMuRxRssiSumSquares_Type = Counter64
_CcMuRxRssiSumSquares_Object = MibTableColumn
ccMuRxRssiSumSquares = _CcMuRxRssiSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 2, 1, 10),
    _CcMuRxRssiSumSquares_Type()
)
ccMuRxRssiSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxRssiSumSquares.setStatus("current")


class _CcMuRxRssiMostRecent_Type(Integer32):
    """Custom type ccMuRxRssiMostRecent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CcMuRxRssiMostRecent_Type.__name__ = "Integer32"
_CcMuRxRssiMostRecent_Object = MibTableColumn
ccMuRxRssiMostRecent = _CcMuRxRssiMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 2, 1, 11),
    _CcMuRxRssiMostRecent_Type()
)
ccMuRxRssiMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxRssiMostRecent.setStatus("current")
_CcMuLastActivity_Type = TimeTicks
_CcMuLastActivity_Object = MibTableColumn
ccMuLastActivity = _CcMuLastActivity_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 2, 1, 12),
    _CcMuLastActivity_Type()
)
ccMuLastActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuLastActivity.setStatus("current")
_CcMuRxPktsTable_Object = MibTable
ccMuRxPktsTable = _CcMuRxPktsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 3)
)
if mibBuilder.loadTexts:
    ccMuRxPktsTable.setStatus("current")
_CcMuRxPktsEntry_Object = MibTableRow
ccMuRxPktsEntry = _CcMuRxPktsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 3, 1)
)
ccMuRxPktsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccMuMac"),
)
if mibBuilder.loadTexts:
    ccMuRxPktsEntry.setStatus("current")
_CcMuRxPktsAt1Mb_Type = Counter32
_CcMuRxPktsAt1Mb_Object = MibTableColumn
ccMuRxPktsAt1Mb = _CcMuRxPktsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 3, 1, 1),
    _CcMuRxPktsAt1Mb_Type()
)
ccMuRxPktsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsAt1Mb.setStatus("current")
_CcMuRxPktsAt2Mb_Type = Counter32
_CcMuRxPktsAt2Mb_Object = MibTableColumn
ccMuRxPktsAt2Mb = _CcMuRxPktsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 3, 1, 2),
    _CcMuRxPktsAt2Mb_Type()
)
ccMuRxPktsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsAt2Mb.setStatus("current")
_CcMuRxPktsAt5pt5Mb_Type = Counter32
_CcMuRxPktsAt5pt5Mb_Object = MibTableColumn
ccMuRxPktsAt5pt5Mb = _CcMuRxPktsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 3, 1, 3),
    _CcMuRxPktsAt5pt5Mb_Type()
)
ccMuRxPktsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsAt5pt5Mb.setStatus("current")
_CcMuRxPktsAt6Mb_Type = Counter32
_CcMuRxPktsAt6Mb_Object = MibTableColumn
ccMuRxPktsAt6Mb = _CcMuRxPktsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 3, 1, 4),
    _CcMuRxPktsAt6Mb_Type()
)
ccMuRxPktsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsAt6Mb.setStatus("current")
_CcMuRxPktsAt9Mb_Type = Counter32
_CcMuRxPktsAt9Mb_Object = MibTableColumn
ccMuRxPktsAt9Mb = _CcMuRxPktsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 3, 1, 5),
    _CcMuRxPktsAt9Mb_Type()
)
ccMuRxPktsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsAt9Mb.setStatus("current")
_CcMuRxPktsAt11Mb_Type = Counter32
_CcMuRxPktsAt11Mb_Object = MibTableColumn
ccMuRxPktsAt11Mb = _CcMuRxPktsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 3, 1, 6),
    _CcMuRxPktsAt11Mb_Type()
)
ccMuRxPktsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsAt11Mb.setStatus("current")
_CcMuRxPktsAt12Mb_Type = Counter32
_CcMuRxPktsAt12Mb_Object = MibTableColumn
ccMuRxPktsAt12Mb = _CcMuRxPktsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 3, 1, 7),
    _CcMuRxPktsAt12Mb_Type()
)
ccMuRxPktsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsAt12Mb.setStatus("current")
_CcMuRxPktsAt18Mb_Type = Counter32
_CcMuRxPktsAt18Mb_Object = MibTableColumn
ccMuRxPktsAt18Mb = _CcMuRxPktsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 3, 1, 8),
    _CcMuRxPktsAt18Mb_Type()
)
ccMuRxPktsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsAt18Mb.setStatus("current")
_CcMuRxPktsAt22Mb_Type = Counter32
_CcMuRxPktsAt22Mb_Object = MibTableColumn
ccMuRxPktsAt22Mb = _CcMuRxPktsAt22Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 3, 1, 9),
    _CcMuRxPktsAt22Mb_Type()
)
ccMuRxPktsAt22Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsAt22Mb.setStatus("current")
_CcMuRxPktsAt24Mb_Type = Counter32
_CcMuRxPktsAt24Mb_Object = MibTableColumn
ccMuRxPktsAt24Mb = _CcMuRxPktsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 3, 1, 10),
    _CcMuRxPktsAt24Mb_Type()
)
ccMuRxPktsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsAt24Mb.setStatus("current")
_CcMuRxPktsAt36Mb_Type = Counter32
_CcMuRxPktsAt36Mb_Object = MibTableColumn
ccMuRxPktsAt36Mb = _CcMuRxPktsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 3, 1, 11),
    _CcMuRxPktsAt36Mb_Type()
)
ccMuRxPktsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsAt36Mb.setStatus("current")
_CcMuRxPktsAt48Mb_Type = Counter32
_CcMuRxPktsAt48Mb_Object = MibTableColumn
ccMuRxPktsAt48Mb = _CcMuRxPktsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 3, 1, 12),
    _CcMuRxPktsAt48Mb_Type()
)
ccMuRxPktsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsAt48Mb.setStatus("current")
_CcMuRxPktsAt54Mb_Type = Counter32
_CcMuRxPktsAt54Mb_Object = MibTableColumn
ccMuRxPktsAt54Mb = _CcMuRxPktsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 3, 1, 13),
    _CcMuRxPktsAt54Mb_Type()
)
ccMuRxPktsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxPktsAt54Mb.setStatus("current")
_CcMuTxPktsTable_Object = MibTable
ccMuTxPktsTable = _CcMuTxPktsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 4)
)
if mibBuilder.loadTexts:
    ccMuTxPktsTable.setStatus("current")
_CcMuTxPktsEntry_Object = MibTableRow
ccMuTxPktsEntry = _CcMuTxPktsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 4, 1)
)
ccMuTxPktsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccMuMac"),
)
if mibBuilder.loadTexts:
    ccMuTxPktsEntry.setStatus("current")
_CcMuTxPktsAt1Mb_Type = Counter32
_CcMuTxPktsAt1Mb_Object = MibTableColumn
ccMuTxPktsAt1Mb = _CcMuTxPktsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 4, 1, 1),
    _CcMuTxPktsAt1Mb_Type()
)
ccMuTxPktsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxPktsAt1Mb.setStatus("current")
_CcMuTxPktsAt2Mb_Type = Counter32
_CcMuTxPktsAt2Mb_Object = MibTableColumn
ccMuTxPktsAt2Mb = _CcMuTxPktsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 4, 1, 2),
    _CcMuTxPktsAt2Mb_Type()
)
ccMuTxPktsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxPktsAt2Mb.setStatus("current")
_CcMuTxPktsAt5pt5Mb_Type = Counter32
_CcMuTxPktsAt5pt5Mb_Object = MibTableColumn
ccMuTxPktsAt5pt5Mb = _CcMuTxPktsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 4, 1, 3),
    _CcMuTxPktsAt5pt5Mb_Type()
)
ccMuTxPktsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxPktsAt5pt5Mb.setStatus("current")
_CcMuTxPktsAt6Mb_Type = Counter32
_CcMuTxPktsAt6Mb_Object = MibTableColumn
ccMuTxPktsAt6Mb = _CcMuTxPktsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 4, 1, 4),
    _CcMuTxPktsAt6Mb_Type()
)
ccMuTxPktsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxPktsAt6Mb.setStatus("current")
_CcMuTxPktsAt9Mb_Type = Counter32
_CcMuTxPktsAt9Mb_Object = MibTableColumn
ccMuTxPktsAt9Mb = _CcMuTxPktsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 4, 1, 5),
    _CcMuTxPktsAt9Mb_Type()
)
ccMuTxPktsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxPktsAt9Mb.setStatus("current")
_CcMuTxPktsAt11Mb_Type = Counter32
_CcMuTxPktsAt11Mb_Object = MibTableColumn
ccMuTxPktsAt11Mb = _CcMuTxPktsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 4, 1, 6),
    _CcMuTxPktsAt11Mb_Type()
)
ccMuTxPktsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxPktsAt11Mb.setStatus("current")
_CcMuTxPktsAt12Mb_Type = Counter32
_CcMuTxPktsAt12Mb_Object = MibTableColumn
ccMuTxPktsAt12Mb = _CcMuTxPktsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 4, 1, 7),
    _CcMuTxPktsAt12Mb_Type()
)
ccMuTxPktsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxPktsAt12Mb.setStatus("current")
_CcMuTxPktsAt18Mb_Type = Counter32
_CcMuTxPktsAt18Mb_Object = MibTableColumn
ccMuTxPktsAt18Mb = _CcMuTxPktsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 4, 1, 8),
    _CcMuTxPktsAt18Mb_Type()
)
ccMuTxPktsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxPktsAt18Mb.setStatus("current")
_CcMuTxPktsAt22Mb_Type = Counter32
_CcMuTxPktsAt22Mb_Object = MibTableColumn
ccMuTxPktsAt22Mb = _CcMuTxPktsAt22Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 4, 1, 9),
    _CcMuTxPktsAt22Mb_Type()
)
ccMuTxPktsAt22Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxPktsAt22Mb.setStatus("current")
_CcMuTxPktsAt24Mb_Type = Counter32
_CcMuTxPktsAt24Mb_Object = MibTableColumn
ccMuTxPktsAt24Mb = _CcMuTxPktsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 4, 1, 10),
    _CcMuTxPktsAt24Mb_Type()
)
ccMuTxPktsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxPktsAt24Mb.setStatus("current")
_CcMuTxPktsAt36Mb_Type = Counter32
_CcMuTxPktsAt36Mb_Object = MibTableColumn
ccMuTxPktsAt36Mb = _CcMuTxPktsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 4, 1, 11),
    _CcMuTxPktsAt36Mb_Type()
)
ccMuTxPktsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxPktsAt36Mb.setStatus("current")
_CcMuTxPktsAt48Mb_Type = Counter32
_CcMuTxPktsAt48Mb_Object = MibTableColumn
ccMuTxPktsAt48Mb = _CcMuTxPktsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 4, 1, 12),
    _CcMuTxPktsAt48Mb_Type()
)
ccMuTxPktsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxPktsAt48Mb.setStatus("current")
_CcMuTxPktsAt54Mb_Type = Counter32
_CcMuTxPktsAt54Mb_Object = MibTableColumn
ccMuTxPktsAt54Mb = _CcMuTxPktsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 4, 1, 13),
    _CcMuTxPktsAt54Mb_Type()
)
ccMuTxPktsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxPktsAt54Mb.setStatus("current")
_CcMuRxOctetsTable_Object = MibTable
ccMuRxOctetsTable = _CcMuRxOctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 5)
)
if mibBuilder.loadTexts:
    ccMuRxOctetsTable.setStatus("current")
_CcMuRxOctetsEntry_Object = MibTableRow
ccMuRxOctetsEntry = _CcMuRxOctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 5, 1)
)
ccMuRxOctetsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccMuMac"),
)
if mibBuilder.loadTexts:
    ccMuRxOctetsEntry.setStatus("current")
_CcMuRxOctetsAt1Mb_Type = Counter32
_CcMuRxOctetsAt1Mb_Object = MibTableColumn
ccMuRxOctetsAt1Mb = _CcMuRxOctetsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 5, 1, 1),
    _CcMuRxOctetsAt1Mb_Type()
)
ccMuRxOctetsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsAt1Mb.setStatus("current")
_CcMuRxOctetsAt2Mb_Type = Counter32
_CcMuRxOctetsAt2Mb_Object = MibTableColumn
ccMuRxOctetsAt2Mb = _CcMuRxOctetsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 5, 1, 2),
    _CcMuRxOctetsAt2Mb_Type()
)
ccMuRxOctetsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsAt2Mb.setStatus("current")
_CcMuRxOctetsAt5pt5Mb_Type = Counter32
_CcMuRxOctetsAt5pt5Mb_Object = MibTableColumn
ccMuRxOctetsAt5pt5Mb = _CcMuRxOctetsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 5, 1, 3),
    _CcMuRxOctetsAt5pt5Mb_Type()
)
ccMuRxOctetsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsAt5pt5Mb.setStatus("current")
_CcMuRxOctetsAt6Mb_Type = Counter32
_CcMuRxOctetsAt6Mb_Object = MibTableColumn
ccMuRxOctetsAt6Mb = _CcMuRxOctetsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 5, 1, 4),
    _CcMuRxOctetsAt6Mb_Type()
)
ccMuRxOctetsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsAt6Mb.setStatus("current")
_CcMuRxOctetsAt9Mb_Type = Counter32
_CcMuRxOctetsAt9Mb_Object = MibTableColumn
ccMuRxOctetsAt9Mb = _CcMuRxOctetsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 5, 1, 5),
    _CcMuRxOctetsAt9Mb_Type()
)
ccMuRxOctetsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsAt9Mb.setStatus("current")
_CcMuRxOctetsAt11Mb_Type = Counter32
_CcMuRxOctetsAt11Mb_Object = MibTableColumn
ccMuRxOctetsAt11Mb = _CcMuRxOctetsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 5, 1, 6),
    _CcMuRxOctetsAt11Mb_Type()
)
ccMuRxOctetsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsAt11Mb.setStatus("current")
_CcMuRxOctetsAt12Mb_Type = Counter32
_CcMuRxOctetsAt12Mb_Object = MibTableColumn
ccMuRxOctetsAt12Mb = _CcMuRxOctetsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 5, 1, 7),
    _CcMuRxOctetsAt12Mb_Type()
)
ccMuRxOctetsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsAt12Mb.setStatus("current")
_CcMuRxOctetsAt18Mb_Type = Counter32
_CcMuRxOctetsAt18Mb_Object = MibTableColumn
ccMuRxOctetsAt18Mb = _CcMuRxOctetsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 5, 1, 8),
    _CcMuRxOctetsAt18Mb_Type()
)
ccMuRxOctetsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsAt18Mb.setStatus("current")
_CcMuRxOctetsAt22Mb_Type = Counter32
_CcMuRxOctetsAt22Mb_Object = MibTableColumn
ccMuRxOctetsAt22Mb = _CcMuRxOctetsAt22Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 5, 1, 9),
    _CcMuRxOctetsAt22Mb_Type()
)
ccMuRxOctetsAt22Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsAt22Mb.setStatus("current")
_CcMuRxOctetsAt24Mb_Type = Counter32
_CcMuRxOctetsAt24Mb_Object = MibTableColumn
ccMuRxOctetsAt24Mb = _CcMuRxOctetsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 5, 1, 10),
    _CcMuRxOctetsAt24Mb_Type()
)
ccMuRxOctetsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsAt24Mb.setStatus("current")
_CcMuRxOctetsAt36Mb_Type = Counter32
_CcMuRxOctetsAt36Mb_Object = MibTableColumn
ccMuRxOctetsAt36Mb = _CcMuRxOctetsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 5, 1, 11),
    _CcMuRxOctetsAt36Mb_Type()
)
ccMuRxOctetsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsAt36Mb.setStatus("current")
_CcMuRxOctetsAt48Mb_Type = Counter32
_CcMuRxOctetsAt48Mb_Object = MibTableColumn
ccMuRxOctetsAt48Mb = _CcMuRxOctetsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 5, 1, 12),
    _CcMuRxOctetsAt48Mb_Type()
)
ccMuRxOctetsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsAt48Mb.setStatus("current")
_CcMuRxOctetsAt54Mb_Type = Counter32
_CcMuRxOctetsAt54Mb_Object = MibTableColumn
ccMuRxOctetsAt54Mb = _CcMuRxOctetsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 5, 1, 13),
    _CcMuRxOctetsAt54Mb_Type()
)
ccMuRxOctetsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuRxOctetsAt54Mb.setStatus("current")
_CcMuTxOctetsTable_Object = MibTable
ccMuTxOctetsTable = _CcMuTxOctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 6)
)
if mibBuilder.loadTexts:
    ccMuTxOctetsTable.setStatus("current")
_CcMuTxOctetsEntry_Object = MibTableRow
ccMuTxOctetsEntry = _CcMuTxOctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 6, 1)
)
ccMuTxOctetsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccMuMac"),
)
if mibBuilder.loadTexts:
    ccMuTxOctetsEntry.setStatus("current")
_CcMuTxOctetsAt1Mb_Type = Counter32
_CcMuTxOctetsAt1Mb_Object = MibTableColumn
ccMuTxOctetsAt1Mb = _CcMuTxOctetsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 6, 1, 1),
    _CcMuTxOctetsAt1Mb_Type()
)
ccMuTxOctetsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxOctetsAt1Mb.setStatus("current")
_CcMuTxOctetsAt2Mb_Type = Counter32
_CcMuTxOctetsAt2Mb_Object = MibTableColumn
ccMuTxOctetsAt2Mb = _CcMuTxOctetsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 6, 1, 2),
    _CcMuTxOctetsAt2Mb_Type()
)
ccMuTxOctetsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxOctetsAt2Mb.setStatus("current")
_CcMuTxOctetsAt5pt5Mb_Type = Counter32
_CcMuTxOctetsAt5pt5Mb_Object = MibTableColumn
ccMuTxOctetsAt5pt5Mb = _CcMuTxOctetsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 6, 1, 3),
    _CcMuTxOctetsAt5pt5Mb_Type()
)
ccMuTxOctetsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxOctetsAt5pt5Mb.setStatus("current")
_CcMuTxOctetsAt6Mb_Type = Counter32
_CcMuTxOctetsAt6Mb_Object = MibTableColumn
ccMuTxOctetsAt6Mb = _CcMuTxOctetsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 6, 1, 4),
    _CcMuTxOctetsAt6Mb_Type()
)
ccMuTxOctetsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxOctetsAt6Mb.setStatus("current")
_CcMuTxOctetsAt9Mb_Type = Counter32
_CcMuTxOctetsAt9Mb_Object = MibTableColumn
ccMuTxOctetsAt9Mb = _CcMuTxOctetsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 6, 1, 5),
    _CcMuTxOctetsAt9Mb_Type()
)
ccMuTxOctetsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxOctetsAt9Mb.setStatus("current")
_CcMuTxOctetsAt11Mb_Type = Counter32
_CcMuTxOctetsAt11Mb_Object = MibTableColumn
ccMuTxOctetsAt11Mb = _CcMuTxOctetsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 6, 1, 6),
    _CcMuTxOctetsAt11Mb_Type()
)
ccMuTxOctetsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxOctetsAt11Mb.setStatus("current")
_CcMuTxOctetsAt12Mb_Type = Counter32
_CcMuTxOctetsAt12Mb_Object = MibTableColumn
ccMuTxOctetsAt12Mb = _CcMuTxOctetsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 6, 1, 7),
    _CcMuTxOctetsAt12Mb_Type()
)
ccMuTxOctetsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxOctetsAt12Mb.setStatus("current")
_CcMuTxOctetsAt18Mb_Type = Counter32
_CcMuTxOctetsAt18Mb_Object = MibTableColumn
ccMuTxOctetsAt18Mb = _CcMuTxOctetsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 6, 1, 8),
    _CcMuTxOctetsAt18Mb_Type()
)
ccMuTxOctetsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxOctetsAt18Mb.setStatus("current")
_CcMuTxOctetsAt22Mb_Type = Counter32
_CcMuTxOctetsAt22Mb_Object = MibTableColumn
ccMuTxOctetsAt22Mb = _CcMuTxOctetsAt22Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 6, 1, 9),
    _CcMuTxOctetsAt22Mb_Type()
)
ccMuTxOctetsAt22Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxOctetsAt22Mb.setStatus("current")
_CcMuTxOctetsAt24Mb_Type = Counter32
_CcMuTxOctetsAt24Mb_Object = MibTableColumn
ccMuTxOctetsAt24Mb = _CcMuTxOctetsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 6, 1, 10),
    _CcMuTxOctetsAt24Mb_Type()
)
ccMuTxOctetsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxOctetsAt24Mb.setStatus("current")
_CcMuTxOctetsAt36Mb_Type = Counter32
_CcMuTxOctetsAt36Mb_Object = MibTableColumn
ccMuTxOctetsAt36Mb = _CcMuTxOctetsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 6, 1, 11),
    _CcMuTxOctetsAt36Mb_Type()
)
ccMuTxOctetsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxOctetsAt36Mb.setStatus("current")
_CcMuTxOctetsAt48Mb_Type = Counter32
_CcMuTxOctetsAt48Mb_Object = MibTableColumn
ccMuTxOctetsAt48Mb = _CcMuTxOctetsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 6, 1, 12),
    _CcMuTxOctetsAt48Mb_Type()
)
ccMuTxOctetsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxOctetsAt48Mb.setStatus("current")
_CcMuTxOctetsAt54Mb_Type = Counter32
_CcMuTxOctetsAt54Mb_Object = MibTableColumn
ccMuTxOctetsAt54Mb = _CcMuTxOctetsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 6, 1, 13),
    _CcMuTxOctetsAt54Mb_Type()
)
ccMuTxOctetsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxOctetsAt54Mb.setStatus("current")
_CcMuTxRetriesTable_Object = MibTable
ccMuTxRetriesTable = _CcMuTxRetriesTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 7)
)
if mibBuilder.loadTexts:
    ccMuTxRetriesTable.setStatus("current")
_CcMuTxRetriesEntry_Object = MibTableRow
ccMuTxRetriesEntry = _CcMuTxRetriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 7, 1)
)
ccMuTxRetriesEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccMuMac"),
)
if mibBuilder.loadTexts:
    ccMuTxRetriesEntry.setStatus("current")
_CcMuTxRetriesNone_Type = Counter32
_CcMuTxRetriesNone_Object = MibTableColumn
ccMuTxRetriesNone = _CcMuTxRetriesNone_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 7, 1, 1),
    _CcMuTxRetriesNone_Type()
)
ccMuTxRetriesNone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesNone.setStatus("current")
_CcMuTxRetries01_Type = Counter32
_CcMuTxRetries01_Object = MibTableColumn
ccMuTxRetries01 = _CcMuTxRetries01_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 7, 1, 2),
    _CcMuTxRetries01_Type()
)
ccMuTxRetries01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries01.setStatus("current")
_CcMuTxRetries02_Type = Counter32
_CcMuTxRetries02_Object = MibTableColumn
ccMuTxRetries02 = _CcMuTxRetries02_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 7, 1, 3),
    _CcMuTxRetries02_Type()
)
ccMuTxRetries02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries02.setStatus("current")
_CcMuTxRetries03_Type = Counter32
_CcMuTxRetries03_Object = MibTableColumn
ccMuTxRetries03 = _CcMuTxRetries03_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 7, 1, 4),
    _CcMuTxRetries03_Type()
)
ccMuTxRetries03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries03.setStatus("current")
_CcMuTxRetries04_Type = Counter32
_CcMuTxRetries04_Object = MibTableColumn
ccMuTxRetries04 = _CcMuTxRetries04_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 7, 1, 5),
    _CcMuTxRetries04_Type()
)
ccMuTxRetries04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries04.setStatus("current")
_CcMuTxRetries05_Type = Counter32
_CcMuTxRetries05_Object = MibTableColumn
ccMuTxRetries05 = _CcMuTxRetries05_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 7, 1, 6),
    _CcMuTxRetries05_Type()
)
ccMuTxRetries05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries05.setStatus("current")
_CcMuTxRetries06_Type = Counter32
_CcMuTxRetries06_Object = MibTableColumn
ccMuTxRetries06 = _CcMuTxRetries06_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 7, 1, 7),
    _CcMuTxRetries06_Type()
)
ccMuTxRetries06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries06.setStatus("current")
_CcMuTxRetries07_Type = Counter32
_CcMuTxRetries07_Object = MibTableColumn
ccMuTxRetries07 = _CcMuTxRetries07_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 7, 1, 8),
    _CcMuTxRetries07_Type()
)
ccMuTxRetries07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries07.setStatus("current")
_CcMuTxRetries08_Type = Counter32
_CcMuTxRetries08_Object = MibTableColumn
ccMuTxRetries08 = _CcMuTxRetries08_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 7, 1, 9),
    _CcMuTxRetries08_Type()
)
ccMuTxRetries08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries08.setStatus("current")
_CcMuTxRetries09_Type = Counter32
_CcMuTxRetries09_Object = MibTableColumn
ccMuTxRetries09 = _CcMuTxRetries09_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 7, 1, 10),
    _CcMuTxRetries09_Type()
)
ccMuTxRetries09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries09.setStatus("current")
_CcMuTxRetries10_Type = Counter32
_CcMuTxRetries10_Object = MibTableColumn
ccMuTxRetries10 = _CcMuTxRetries10_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 7, 1, 11),
    _CcMuTxRetries10_Type()
)
ccMuTxRetries10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries10.setStatus("current")
_CcMuTxRetries11_Type = Counter32
_CcMuTxRetries11_Object = MibTableColumn
ccMuTxRetries11 = _CcMuTxRetries11_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 7, 1, 12),
    _CcMuTxRetries11_Type()
)
ccMuTxRetries11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries11.setStatus("current")
_CcMuTxRetries12_Type = Counter32
_CcMuTxRetries12_Object = MibTableColumn
ccMuTxRetries12 = _CcMuTxRetries12_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 7, 1, 13),
    _CcMuTxRetries12_Type()
)
ccMuTxRetries12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries12.setStatus("current")
_CcMuTxRetries13_Type = Counter32
_CcMuTxRetries13_Object = MibTableColumn
ccMuTxRetries13 = _CcMuTxRetries13_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 7, 1, 14),
    _CcMuTxRetries13_Type()
)
ccMuTxRetries13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries13.setStatus("current")
_CcMuTxRetries14_Type = Counter32
_CcMuTxRetries14_Object = MibTableColumn
ccMuTxRetries14 = _CcMuTxRetries14_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 7, 1, 15),
    _CcMuTxRetries14_Type()
)
ccMuTxRetries14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries14.setStatus("current")
_CcMuTxRetries15_Type = Counter32
_CcMuTxRetries15_Object = MibTableColumn
ccMuTxRetries15 = _CcMuTxRetries15_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 7, 1, 16),
    _CcMuTxRetries15_Type()
)
ccMuTxRetries15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetries15.setStatus("current")
_CcMuTxRetriesFailed_Type = Counter32
_CcMuTxRetriesFailed_Object = MibTableColumn
ccMuTxRetriesFailed = _CcMuTxRetriesFailed_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 7, 1, 17),
    _CcMuTxRetriesFailed_Type()
)
ccMuTxRetriesFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesFailed.setStatus("current")
_CcMuTxRetriesTotal_Type = Counter32
_CcMuTxRetriesTotal_Object = MibTableColumn
ccMuTxRetriesTotal = _CcMuTxRetriesTotal_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 7, 1, 18),
    _CcMuTxRetriesTotal_Type()
)
ccMuTxRetriesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesTotal.setStatus("current")


class _CcMuTxRetriesMostRecent_Type(Integer32):
    """Custom type ccMuTxRetriesMostRecent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CcMuTxRetriesMostRecent_Type.__name__ = "Integer32"
_CcMuTxRetriesMostRecent_Object = MibTableColumn
ccMuTxRetriesMostRecent = _CcMuTxRetriesMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 7, 1, 19),
    _CcMuTxRetriesMostRecent_Type()
)
ccMuTxRetriesMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesMostRecent.setStatus("current")
_CcMuLastMac_Type = PhysAddress
_CcMuLastMac_Object = MibScalar
ccMuLastMac = _CcMuLastMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 8),
    _CcMuLastMac_Type()
)
ccMuLastMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuLastMac.setStatus("current")


class _CcMuLastReason_Type(Integer32):
    """Custom type ccMuLastReason based on Integer32"""
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
        *(("aclViolation", 2),
          ("associationFailed", 4),
          ("authenticationFailedOn802dot1x", 5),
          ("kerberosWrongUsername", 6),
          ("success", 1),
          ("timeout", 3))
    )


_CcMuLastReason_Type.__name__ = "Integer32"
_CcMuLastReason_Object = MibScalar
ccMuLastReason = _CcMuLastReason_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 9),
    _CcMuLastReason_Type()
)
ccMuLastReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuLastReason.setStatus("current")
_CcMuLastPortal_Type = PhysAddress
_CcMuLastPortal_Object = MibScalar
ccMuLastPortal = _CcMuLastPortal_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 10),
    _CcMuLastPortal_Type()
)
ccMuLastPortal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuLastPortal.setStatus("current")
_CcMuRfSum_ObjectIdentity = ObjectIdentity
ccMuRfSum = _CcMuRfSum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100)
)
_CcMuTxRetriesOctetsTable_Object = MibTable
ccMuTxRetriesOctetsTable = _CcMuTxRetriesOctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 1)
)
if mibBuilder.loadTexts:
    ccMuTxRetriesOctetsTable.setStatus("current")
_CcMuTxRetriesOctetsEntry_Object = MibTableRow
ccMuTxRetriesOctetsEntry = _CcMuTxRetriesOctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 1, 1)
)
ccMuTxRetriesOctetsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccMuMac"),
)
if mibBuilder.loadTexts:
    ccMuTxRetriesOctetsEntry.setStatus("current")
_CcMuTxRetriesOctetsNone_Type = Counter32
_CcMuTxRetriesOctetsNone_Object = MibTableColumn
ccMuTxRetriesOctetsNone = _CcMuTxRetriesOctetsNone_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 1, 1, 1),
    _CcMuTxRetriesOctetsNone_Type()
)
ccMuTxRetriesOctetsNone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctetsNone.setStatus("current")
_CcMuTxRetriesOctets01_Type = Counter32
_CcMuTxRetriesOctets01_Object = MibTableColumn
ccMuTxRetriesOctets01 = _CcMuTxRetriesOctets01_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 1, 1, 2),
    _CcMuTxRetriesOctets01_Type()
)
ccMuTxRetriesOctets01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets01.setStatus("current")
_CcMuTxRetriesOctets02_Type = Counter32
_CcMuTxRetriesOctets02_Object = MibTableColumn
ccMuTxRetriesOctets02 = _CcMuTxRetriesOctets02_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 1, 1, 3),
    _CcMuTxRetriesOctets02_Type()
)
ccMuTxRetriesOctets02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets02.setStatus("current")
_CcMuTxRetriesOctets03_Type = Counter32
_CcMuTxRetriesOctets03_Object = MibTableColumn
ccMuTxRetriesOctets03 = _CcMuTxRetriesOctets03_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 1, 1, 4),
    _CcMuTxRetriesOctets03_Type()
)
ccMuTxRetriesOctets03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets03.setStatus("current")
_CcMuTxRetriesOctets04_Type = Counter32
_CcMuTxRetriesOctets04_Object = MibTableColumn
ccMuTxRetriesOctets04 = _CcMuTxRetriesOctets04_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 1, 1, 5),
    _CcMuTxRetriesOctets04_Type()
)
ccMuTxRetriesOctets04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets04.setStatus("current")
_CcMuTxRetriesOctets05_Type = Counter32
_CcMuTxRetriesOctets05_Object = MibTableColumn
ccMuTxRetriesOctets05 = _CcMuTxRetriesOctets05_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 1, 1, 6),
    _CcMuTxRetriesOctets05_Type()
)
ccMuTxRetriesOctets05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets05.setStatus("current")
_CcMuTxRetriesOctets06_Type = Counter32
_CcMuTxRetriesOctets06_Object = MibTableColumn
ccMuTxRetriesOctets06 = _CcMuTxRetriesOctets06_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 1, 1, 7),
    _CcMuTxRetriesOctets06_Type()
)
ccMuTxRetriesOctets06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets06.setStatus("current")
_CcMuTxRetriesOctets07_Type = Counter32
_CcMuTxRetriesOctets07_Object = MibTableColumn
ccMuTxRetriesOctets07 = _CcMuTxRetriesOctets07_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 1, 1, 8),
    _CcMuTxRetriesOctets07_Type()
)
ccMuTxRetriesOctets07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets07.setStatus("current")
_CcMuTxRetriesOctets08_Type = Counter32
_CcMuTxRetriesOctets08_Object = MibTableColumn
ccMuTxRetriesOctets08 = _CcMuTxRetriesOctets08_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 1, 1, 9),
    _CcMuTxRetriesOctets08_Type()
)
ccMuTxRetriesOctets08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets08.setStatus("current")
_CcMuTxRetriesOctets09_Type = Counter32
_CcMuTxRetriesOctets09_Object = MibTableColumn
ccMuTxRetriesOctets09 = _CcMuTxRetriesOctets09_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 1, 1, 10),
    _CcMuTxRetriesOctets09_Type()
)
ccMuTxRetriesOctets09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets09.setStatus("current")
_CcMuTxRetriesOctets10_Type = Counter32
_CcMuTxRetriesOctets10_Object = MibTableColumn
ccMuTxRetriesOctets10 = _CcMuTxRetriesOctets10_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 1, 1, 11),
    _CcMuTxRetriesOctets10_Type()
)
ccMuTxRetriesOctets10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets10.setStatus("current")
_CcMuTxRetriesOctets11_Type = Counter32
_CcMuTxRetriesOctets11_Object = MibTableColumn
ccMuTxRetriesOctets11 = _CcMuTxRetriesOctets11_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 1, 1, 12),
    _CcMuTxRetriesOctets11_Type()
)
ccMuTxRetriesOctets11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets11.setStatus("current")
_CcMuTxRetriesOctets12_Type = Counter32
_CcMuTxRetriesOctets12_Object = MibTableColumn
ccMuTxRetriesOctets12 = _CcMuTxRetriesOctets12_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 1, 1, 13),
    _CcMuTxRetriesOctets12_Type()
)
ccMuTxRetriesOctets12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets12.setStatus("current")
_CcMuTxRetriesOctets13_Type = Counter32
_CcMuTxRetriesOctets13_Object = MibTableColumn
ccMuTxRetriesOctets13 = _CcMuTxRetriesOctets13_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 1, 1, 14),
    _CcMuTxRetriesOctets13_Type()
)
ccMuTxRetriesOctets13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets13.setStatus("current")
_CcMuTxRetriesOctets14_Type = Counter32
_CcMuTxRetriesOctets14_Object = MibTableColumn
ccMuTxRetriesOctets14 = _CcMuTxRetriesOctets14_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 1, 1, 15),
    _CcMuTxRetriesOctets14_Type()
)
ccMuTxRetriesOctets14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets14.setStatus("current")
_CcMuTxRetriesOctets15_Type = Counter32
_CcMuTxRetriesOctets15_Object = MibTableColumn
ccMuTxRetriesOctets15 = _CcMuTxRetriesOctets15_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 1, 1, 16),
    _CcMuTxRetriesOctets15_Type()
)
ccMuTxRetriesOctets15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctets15.setStatus("current")
_CcMuTxRetriesOctetsFailed_Type = Counter32
_CcMuTxRetriesOctetsFailed_Object = MibTableColumn
ccMuTxRetriesOctetsFailed = _CcMuTxRetriesOctetsFailed_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 1, 1, 17),
    _CcMuTxRetriesOctetsFailed_Type()
)
ccMuTxRetriesOctetsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuTxRetriesOctetsFailed.setStatus("current")
_CcMuSigStatsTable_Object = MibTable
ccMuSigStatsTable = _CcMuSigStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 2)
)
if mibBuilder.loadTexts:
    ccMuSigStatsTable.setStatus("current")
_CcMuSigStatsEntry_Object = MibTableRow
ccMuSigStatsEntry = _CcMuSigStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 2, 1)
)
ccMuSigStatsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccMuMac"),
)
if mibBuilder.loadTexts:
    ccMuSigStatsEntry.setStatus("current")
_CcMuSigStatsNumPkts_Type = Counter32
_CcMuSigStatsNumPkts_Object = MibTableColumn
ccMuSigStatsNumPkts = _CcMuSigStatsNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 2, 1, 1),
    _CcMuSigStatsNumPkts_Type()
)
ccMuSigStatsNumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsNumPkts.setStatus("current")
_CcMuSigStatsSignalBest_Type = Integer32
_CcMuSigStatsSignalBest_Object = MibTableColumn
ccMuSigStatsSignalBest = _CcMuSigStatsSignalBest_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 2, 1, 2),
    _CcMuSigStatsSignalBest_Type()
)
ccMuSigStatsSignalBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsSignalBest.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsSignalBest.setUnits("dBm")
_CcMuSigStatsSignalWorst_Type = Integer32
_CcMuSigStatsSignalWorst_Object = MibTableColumn
ccMuSigStatsSignalWorst = _CcMuSigStatsSignalWorst_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 2, 1, 3),
    _CcMuSigStatsSignalWorst_Type()
)
ccMuSigStatsSignalWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsSignalWorst.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsSignalWorst.setUnits("dBm")
_CcMuSigStatsSignalSum_Type = Integer32
_CcMuSigStatsSignalSum_Object = MibTableColumn
ccMuSigStatsSignalSum = _CcMuSigStatsSignalSum_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 2, 1, 4),
    _CcMuSigStatsSignalSum_Type()
)
ccMuSigStatsSignalSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsSignalSum.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsSignalSum.setUnits("dBm")
_CcMuSigStatsSignalSumSquares_Type = Counter64
_CcMuSigStatsSignalSumSquares_Object = MibTableColumn
ccMuSigStatsSignalSumSquares = _CcMuSigStatsSignalSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 2, 1, 5),
    _CcMuSigStatsSignalSumSquares_Type()
)
ccMuSigStatsSignalSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsSignalSumSquares.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsSignalSumSquares.setUnits("dBm")
_CcMuSigStatsSignalMostRecent_Type = Integer32
_CcMuSigStatsSignalMostRecent_Object = MibTableColumn
ccMuSigStatsSignalMostRecent = _CcMuSigStatsSignalMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 2, 1, 6),
    _CcMuSigStatsSignalMostRecent_Type()
)
ccMuSigStatsSignalMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsSignalMostRecent.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsSignalMostRecent.setUnits("dBm")
_CcMuSigStatsNoiseBest_Type = Integer32
_CcMuSigStatsNoiseBest_Object = MibTableColumn
ccMuSigStatsNoiseBest = _CcMuSigStatsNoiseBest_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 2, 1, 7),
    _CcMuSigStatsNoiseBest_Type()
)
ccMuSigStatsNoiseBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsNoiseBest.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsNoiseBest.setUnits("dBm")
_CcMuSigStatsNoiseWorst_Type = Integer32
_CcMuSigStatsNoiseWorst_Object = MibTableColumn
ccMuSigStatsNoiseWorst = _CcMuSigStatsNoiseWorst_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 2, 1, 8),
    _CcMuSigStatsNoiseWorst_Type()
)
ccMuSigStatsNoiseWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsNoiseWorst.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsNoiseWorst.setUnits("dBm")
_CcMuSigStatsNoiseSum_Type = Integer32
_CcMuSigStatsNoiseSum_Object = MibTableColumn
ccMuSigStatsNoiseSum = _CcMuSigStatsNoiseSum_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 2, 1, 9),
    _CcMuSigStatsNoiseSum_Type()
)
ccMuSigStatsNoiseSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsNoiseSum.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsNoiseSum.setUnits("dBm")
_CcMuSigStatsNoiseSumSquares_Type = Counter64
_CcMuSigStatsNoiseSumSquares_Object = MibTableColumn
ccMuSigStatsNoiseSumSquares = _CcMuSigStatsNoiseSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 2, 1, 10),
    _CcMuSigStatsNoiseSumSquares_Type()
)
ccMuSigStatsNoiseSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsNoiseSumSquares.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsNoiseSumSquares.setUnits("dBm")
_CcMuSigStatsNoiseMostRecent_Type = Integer32
_CcMuSigStatsNoiseMostRecent_Object = MibTableColumn
ccMuSigStatsNoiseMostRecent = _CcMuSigStatsNoiseMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 2, 1, 11),
    _CcMuSigStatsNoiseMostRecent_Type()
)
ccMuSigStatsNoiseMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsNoiseMostRecent.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsNoiseMostRecent.setUnits("dBm")
_CcMuSigStatsSnrBest_Type = Integer32
_CcMuSigStatsSnrBest_Object = MibTableColumn
ccMuSigStatsSnrBest = _CcMuSigStatsSnrBest_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 2, 1, 12),
    _CcMuSigStatsSnrBest_Type()
)
ccMuSigStatsSnrBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsSnrBest.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsSnrBest.setUnits("dB")
_CcMuSigStatsSnrWorst_Type = Integer32
_CcMuSigStatsSnrWorst_Object = MibTableColumn
ccMuSigStatsSnrWorst = _CcMuSigStatsSnrWorst_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 2, 1, 13),
    _CcMuSigStatsSnrWorst_Type()
)
ccMuSigStatsSnrWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsSnrWorst.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsSnrWorst.setUnits("dB")
_CcMuSigStatsSnrSum_Type = Integer32
_CcMuSigStatsSnrSum_Object = MibTableColumn
ccMuSigStatsSnrSum = _CcMuSigStatsSnrSum_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 2, 1, 14),
    _CcMuSigStatsSnrSum_Type()
)
ccMuSigStatsSnrSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsSnrSum.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsSnrSum.setUnits("dB")
_CcMuSigStatsSnrSumSquares_Type = Counter64
_CcMuSigStatsSnrSumSquares_Object = MibTableColumn
ccMuSigStatsSnrSumSquares = _CcMuSigStatsSnrSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 2, 1, 15),
    _CcMuSigStatsSnrSumSquares_Type()
)
ccMuSigStatsSnrSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsSnrSumSquares.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsSnrSumSquares.setUnits("dB")
_CcMuSigStatsSnrMostRecent_Type = Integer32
_CcMuSigStatsSnrMostRecent_Object = MibTableColumn
ccMuSigStatsSnrMostRecent = _CcMuSigStatsSnrMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 2, 1, 16),
    _CcMuSigStatsSnrMostRecent_Type()
)
ccMuSigStatsSnrMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSigStatsSnrMostRecent.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSigStatsSnrMostRecent.setUnits("dB")
_CcMuSumStatsShortTable_Object = MibTable
ccMuSumStatsShortTable = _CcMuSumStatsShortTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 3)
)
if mibBuilder.loadTexts:
    ccMuSumStatsShortTable.setStatus("current")
_CcMuSumStatsShortEntry_Object = MibTableRow
ccMuSumStatsShortEntry = _CcMuSumStatsShortEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 3, 1)
)
ccMuSumStatsShortEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccMuMac"),
)
if mibBuilder.loadTexts:
    ccMuSumStatsShortEntry.setStatus("current")
_CcMuSumStatsShortTimestamp_Type = TimeTicks
_CcMuSumStatsShortTimestamp_Object = MibTableColumn
ccMuSumStatsShortTimestamp = _CcMuSumStatsShortTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 3, 1, 1),
    _CcMuSumStatsShortTimestamp_Type()
)
ccMuSumStatsShortTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortTimestamp.setStatus("current")
_CcMuSumStatsShortNumPkts_Type = Unsigned32
_CcMuSumStatsShortNumPkts_Object = MibTableColumn
ccMuSumStatsShortNumPkts = _CcMuSumStatsShortNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 3, 1, 2),
    _CcMuSumStatsShortNumPkts_Type()
)
ccMuSumStatsShortNumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortNumPkts.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortNumPkts.setUnits("packets")
_CcMuSumStatsShortPktsPerSec100_Type = ScaleBy100
_CcMuSumStatsShortPktsPerSec100_Object = MibTableColumn
ccMuSumStatsShortPktsPerSec100 = _CcMuSumStatsShortPktsPerSec100_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 3, 1, 3),
    _CcMuSumStatsShortPktsPerSec100_Type()
)
ccMuSumStatsShortPktsPerSec100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortPktsPerSec100.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortPktsPerSec100.setUnits("pkts per sec x100")
_CcMuSumStatsShortPktsPerSecTx100_Type = ScaleBy100
_CcMuSumStatsShortPktsPerSecTx100_Object = MibTableColumn
ccMuSumStatsShortPktsPerSecTx100 = _CcMuSumStatsShortPktsPerSecTx100_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 3, 1, 4),
    _CcMuSumStatsShortPktsPerSecTx100_Type()
)
ccMuSumStatsShortPktsPerSecTx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortPktsPerSecTx100.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortPktsPerSecTx100.setUnits("pkts per sec x100")
_CcMuSumStatsShortPktsPerSecRx100_Type = ScaleBy100
_CcMuSumStatsShortPktsPerSecRx100_Object = MibTableColumn
ccMuSumStatsShortPktsPerSecRx100 = _CcMuSumStatsShortPktsPerSecRx100_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 3, 1, 5),
    _CcMuSumStatsShortPktsPerSecRx100_Type()
)
ccMuSumStatsShortPktsPerSecRx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortPktsPerSecRx100.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortPktsPerSecRx100.setUnits("pkts per sec x100")
_CcMuSumStatsShortThroughput_Type = Unsigned32
_CcMuSumStatsShortThroughput_Object = MibTableColumn
ccMuSumStatsShortThroughput = _CcMuSumStatsShortThroughput_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 3, 1, 6),
    _CcMuSumStatsShortThroughput_Type()
)
ccMuSumStatsShortThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortThroughput.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortThroughput.setUnits("bits per second")
_CcMuSumStatsShortThroughputTx_Type = Unsigned32
_CcMuSumStatsShortThroughputTx_Object = MibTableColumn
ccMuSumStatsShortThroughputTx = _CcMuSumStatsShortThroughputTx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 3, 1, 7),
    _CcMuSumStatsShortThroughputTx_Type()
)
ccMuSumStatsShortThroughputTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortThroughputTx.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortThroughputTx.setUnits("bits per second")
_CcMuSumStatsShortThroughputRx_Type = Unsigned32
_CcMuSumStatsShortThroughputRx_Object = MibTableColumn
ccMuSumStatsShortThroughputRx = _CcMuSumStatsShortThroughputRx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 3, 1, 8),
    _CcMuSumStatsShortThroughputRx_Type()
)
ccMuSumStatsShortThroughputRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortThroughputRx.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortThroughputRx.setUnits("bits per second")
_CcMuSumStatsShortAvgBitSpeed_Type = Unsigned32
_CcMuSumStatsShortAvgBitSpeed_Object = MibTableColumn
ccMuSumStatsShortAvgBitSpeed = _CcMuSumStatsShortAvgBitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 3, 1, 9),
    _CcMuSumStatsShortAvgBitSpeed_Type()
)
ccMuSumStatsShortAvgBitSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortAvgBitSpeed.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortAvgBitSpeed.setUnits("bits per second")
_CcMuSumStatsShortAvgMuSignal_Type = Integer32
_CcMuSumStatsShortAvgMuSignal_Object = MibTableColumn
ccMuSumStatsShortAvgMuSignal = _CcMuSumStatsShortAvgMuSignal_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 3, 1, 10),
    _CcMuSumStatsShortAvgMuSignal_Type()
)
ccMuSumStatsShortAvgMuSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortAvgMuSignal.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortAvgMuSignal.setUnits("dBm")
_CcMuSumStatsShortAvgMuNoise_Type = Integer32
_CcMuSumStatsShortAvgMuNoise_Object = MibTableColumn
ccMuSumStatsShortAvgMuNoise = _CcMuSumStatsShortAvgMuNoise_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 3, 1, 11),
    _CcMuSumStatsShortAvgMuNoise_Type()
)
ccMuSumStatsShortAvgMuNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortAvgMuNoise.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortAvgMuNoise.setUnits("dBm")
_CcMuSumStatsShortAvgMuSnr_Type = Integer32
_CcMuSumStatsShortAvgMuSnr_Object = MibTableColumn
ccMuSumStatsShortAvgMuSnr = _CcMuSumStatsShortAvgMuSnr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 3, 1, 12),
    _CcMuSumStatsShortAvgMuSnr_Type()
)
ccMuSumStatsShortAvgMuSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortAvgMuSnr.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortAvgMuSnr.setUnits("dB")
_CcMuSumStatsShortPp10kNUcastPkts_Type = PartsPer10k
_CcMuSumStatsShortPp10kNUcastPkts_Object = MibTableColumn
ccMuSumStatsShortPp10kNUcastPkts = _CcMuSumStatsShortPp10kNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 3, 1, 13),
    _CcMuSumStatsShortPp10kNUcastPkts_Type()
)
ccMuSumStatsShortPp10kNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortPp10kNUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortPp10kNUcastPkts.setUnits("parts-per-10000")
_CcMuSumStatsShortPp10kTxWithRetries_Type = PartsPer10k
_CcMuSumStatsShortPp10kTxWithRetries_Object = MibTableColumn
ccMuSumStatsShortPp10kTxWithRetries = _CcMuSumStatsShortPp10kTxWithRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 3, 1, 14),
    _CcMuSumStatsShortPp10kTxWithRetries_Type()
)
ccMuSumStatsShortPp10kTxWithRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortPp10kTxWithRetries.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortPp10kTxWithRetries.setUnits("parts-per-10000")
_CcMuSumStatsShortPp10kDropped_Type = PartsPer10k
_CcMuSumStatsShortPp10kDropped_Object = MibTableColumn
ccMuSumStatsShortPp10kDropped = _CcMuSumStatsShortPp10kDropped_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 3, 1, 15),
    _CcMuSumStatsShortPp10kDropped_Type()
)
ccMuSumStatsShortPp10kDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortPp10kDropped.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortPp10kDropped.setUnits("parts-per-10000")
_CcMuSumStatsShortTxAvgRetries100_Type = ScaleBy100
_CcMuSumStatsShortTxAvgRetries100_Object = MibTableColumn
ccMuSumStatsShortTxAvgRetries100 = _CcMuSumStatsShortTxAvgRetries100_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 3, 1, 16),
    _CcMuSumStatsShortTxAvgRetries100_Type()
)
ccMuSumStatsShortTxAvgRetries100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortTxAvgRetries100.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortTxAvgRetries100.setUnits("average x100")
_CcMuSumStatsShortPp10kRxUndecrypt_Type = PartsPer10k
_CcMuSumStatsShortPp10kRxUndecrypt_Object = MibTableColumn
ccMuSumStatsShortPp10kRxUndecrypt = _CcMuSumStatsShortPp10kRxUndecrypt_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 3, 1, 17),
    _CcMuSumStatsShortPp10kRxUndecrypt_Type()
)
ccMuSumStatsShortPp10kRxUndecrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsShortPp10kRxUndecrypt.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsShortPp10kRxUndecrypt.setUnits("parts-per-10000")
_CcMuSumStatsLongTable_Object = MibTable
ccMuSumStatsLongTable = _CcMuSumStatsLongTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 4)
)
if mibBuilder.loadTexts:
    ccMuSumStatsLongTable.setStatus("current")
_CcMuSumStatsLongEntry_Object = MibTableRow
ccMuSumStatsLongEntry = _CcMuSumStatsLongEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 4, 1)
)
ccMuSumStatsLongEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccMuMac"),
)
if mibBuilder.loadTexts:
    ccMuSumStatsLongEntry.setStatus("current")
_CcMuSumStatsLongTimestamp_Type = TimeTicks
_CcMuSumStatsLongTimestamp_Object = MibTableColumn
ccMuSumStatsLongTimestamp = _CcMuSumStatsLongTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 4, 1, 1),
    _CcMuSumStatsLongTimestamp_Type()
)
ccMuSumStatsLongTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongTimestamp.setStatus("current")
_CcMuSumStatsLongNumPkts_Type = Unsigned32
_CcMuSumStatsLongNumPkts_Object = MibTableColumn
ccMuSumStatsLongNumPkts = _CcMuSumStatsLongNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 4, 1, 2),
    _CcMuSumStatsLongNumPkts_Type()
)
ccMuSumStatsLongNumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongNumPkts.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongNumPkts.setUnits("packets")
_CcMuSumStatsLongPktsPerSec100_Type = ScaleBy100
_CcMuSumStatsLongPktsPerSec100_Object = MibTableColumn
ccMuSumStatsLongPktsPerSec100 = _CcMuSumStatsLongPktsPerSec100_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 4, 1, 3),
    _CcMuSumStatsLongPktsPerSec100_Type()
)
ccMuSumStatsLongPktsPerSec100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongPktsPerSec100.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongPktsPerSec100.setUnits("pkts per sec x100")
_CcMuSumStatsLongPktsPerSecTx100_Type = ScaleBy100
_CcMuSumStatsLongPktsPerSecTx100_Object = MibTableColumn
ccMuSumStatsLongPktsPerSecTx100 = _CcMuSumStatsLongPktsPerSecTx100_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 4, 1, 4),
    _CcMuSumStatsLongPktsPerSecTx100_Type()
)
ccMuSumStatsLongPktsPerSecTx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongPktsPerSecTx100.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongPktsPerSecTx100.setUnits("pkts per sec x100")
_CcMuSumStatsLongPktsPerSecRx100_Type = ScaleBy100
_CcMuSumStatsLongPktsPerSecRx100_Object = MibTableColumn
ccMuSumStatsLongPktsPerSecRx100 = _CcMuSumStatsLongPktsPerSecRx100_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 4, 1, 5),
    _CcMuSumStatsLongPktsPerSecRx100_Type()
)
ccMuSumStatsLongPktsPerSecRx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongPktsPerSecRx100.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongPktsPerSecRx100.setUnits("pkts per sec x100")
_CcMuSumStatsLongThroughput_Type = Unsigned32
_CcMuSumStatsLongThroughput_Object = MibTableColumn
ccMuSumStatsLongThroughput = _CcMuSumStatsLongThroughput_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 4, 1, 6),
    _CcMuSumStatsLongThroughput_Type()
)
ccMuSumStatsLongThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongThroughput.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongThroughput.setUnits("bits per second")
_CcMuSumStatsLongThroughputTx_Type = Unsigned32
_CcMuSumStatsLongThroughputTx_Object = MibTableColumn
ccMuSumStatsLongThroughputTx = _CcMuSumStatsLongThroughputTx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 4, 1, 7),
    _CcMuSumStatsLongThroughputTx_Type()
)
ccMuSumStatsLongThroughputTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongThroughputTx.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongThroughputTx.setUnits("bits per second")
_CcMuSumStatsLongThroughputRx_Type = Unsigned32
_CcMuSumStatsLongThroughputRx_Object = MibTableColumn
ccMuSumStatsLongThroughputRx = _CcMuSumStatsLongThroughputRx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 4, 1, 8),
    _CcMuSumStatsLongThroughputRx_Type()
)
ccMuSumStatsLongThroughputRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongThroughputRx.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongThroughputRx.setUnits("bits per second")
_CcMuSumStatsLongAvgBitSpeed_Type = Unsigned32
_CcMuSumStatsLongAvgBitSpeed_Object = MibTableColumn
ccMuSumStatsLongAvgBitSpeed = _CcMuSumStatsLongAvgBitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 4, 1, 9),
    _CcMuSumStatsLongAvgBitSpeed_Type()
)
ccMuSumStatsLongAvgBitSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongAvgBitSpeed.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongAvgBitSpeed.setUnits("bits per second")
_CcMuSumStatsLongAvgMuSignal_Type = Integer32
_CcMuSumStatsLongAvgMuSignal_Object = MibTableColumn
ccMuSumStatsLongAvgMuSignal = _CcMuSumStatsLongAvgMuSignal_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 4, 1, 10),
    _CcMuSumStatsLongAvgMuSignal_Type()
)
ccMuSumStatsLongAvgMuSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongAvgMuSignal.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongAvgMuSignal.setUnits("dBm")
_CcMuSumStatsLongAvgMuNoise_Type = Integer32
_CcMuSumStatsLongAvgMuNoise_Object = MibTableColumn
ccMuSumStatsLongAvgMuNoise = _CcMuSumStatsLongAvgMuNoise_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 4, 1, 11),
    _CcMuSumStatsLongAvgMuNoise_Type()
)
ccMuSumStatsLongAvgMuNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongAvgMuNoise.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongAvgMuNoise.setUnits("dBm")
_CcMuSumStatsLongAvgMuSnr_Type = Integer32
_CcMuSumStatsLongAvgMuSnr_Object = MibTableColumn
ccMuSumStatsLongAvgMuSnr = _CcMuSumStatsLongAvgMuSnr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 4, 1, 12),
    _CcMuSumStatsLongAvgMuSnr_Type()
)
ccMuSumStatsLongAvgMuSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongAvgMuSnr.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongAvgMuSnr.setUnits("dB")
_CcMuSumStatsLongPp10kNUcastPkts_Type = PartsPer10k
_CcMuSumStatsLongPp10kNUcastPkts_Object = MibTableColumn
ccMuSumStatsLongPp10kNUcastPkts = _CcMuSumStatsLongPp10kNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 4, 1, 13),
    _CcMuSumStatsLongPp10kNUcastPkts_Type()
)
ccMuSumStatsLongPp10kNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongPp10kNUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongPp10kNUcastPkts.setUnits("parts-per-10000")
_CcMuSumStatsLongPp10kTxWithRetries_Type = PartsPer10k
_CcMuSumStatsLongPp10kTxWithRetries_Object = MibTableColumn
ccMuSumStatsLongPp10kTxWithRetries = _CcMuSumStatsLongPp10kTxWithRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 4, 1, 14),
    _CcMuSumStatsLongPp10kTxWithRetries_Type()
)
ccMuSumStatsLongPp10kTxWithRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongPp10kTxWithRetries.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongPp10kTxWithRetries.setUnits("parts-per-10000")
_CcMuSumStatsLongPp10kDropped_Type = PartsPer10k
_CcMuSumStatsLongPp10kDropped_Object = MibTableColumn
ccMuSumStatsLongPp10kDropped = _CcMuSumStatsLongPp10kDropped_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 4, 1, 15),
    _CcMuSumStatsLongPp10kDropped_Type()
)
ccMuSumStatsLongPp10kDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongPp10kDropped.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongPp10kDropped.setUnits("parts-per-10000")
_CcMuSumStatsLongTxAvgRetries100_Type = ScaleBy100
_CcMuSumStatsLongTxAvgRetries100_Object = MibTableColumn
ccMuSumStatsLongTxAvgRetries100 = _CcMuSumStatsLongTxAvgRetries100_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 4, 1, 16),
    _CcMuSumStatsLongTxAvgRetries100_Type()
)
ccMuSumStatsLongTxAvgRetries100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongTxAvgRetries100.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongTxAvgRetries100.setUnits("average x100")
_CcMuSumStatsLongPp10kRxUndecrypt_Type = PartsPer10k
_CcMuSumStatsLongPp10kRxUndecrypt_Object = MibTableColumn
ccMuSumStatsLongPp10kRxUndecrypt = _CcMuSumStatsLongPp10kRxUndecrypt_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 4, 100, 4, 1, 17),
    _CcMuSumStatsLongPp10kRxUndecrypt_Type()
)
ccMuSumStatsLongPp10kRxUndecrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccMuSumStatsLongPp10kRxUndecrypt.setStatus("current")
if mibBuilder.loadTexts:
    ccMuSumStatsLongPp10kRxUndecrypt.setUnits("parts-per-10000")
_CcWlan_ObjectIdentity = ObjectIdentity
ccWlan = _CcWlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5)
)
_CcWlanTable_Object = MibTable
ccWlanTable = _CcWlanTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 1)
)
if mibBuilder.loadTexts:
    ccWlanTable.setStatus("current")
_CcWlanEntry_Object = MibTableRow
ccWlanEntry = _CcWlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 1, 1)
)
ccWlanEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWlanIndex"),
)
if mibBuilder.loadTexts:
    ccWlanEntry.setStatus("current")


class _CcWlanIndex_Type(Integer32):
    """Custom type ccWlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1001),
    )


_CcWlanIndex_Type.__name__ = "Integer32"
_CcWlanIndex_Object = MibTableColumn
ccWlanIndex = _CcWlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 1, 1, 1),
    _CcWlanIndex_Type()
)
ccWlanIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccWlanIndex.setStatus("current")
_CcWlanName_Type = DisplayString
_CcWlanName_Object = MibTableColumn
ccWlanName = _CcWlanName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 1, 1, 2),
    _CcWlanName_Type()
)
ccWlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanName.setStatus("current")
_CcWlanEssid_Type = DisplayString
_CcWlanEssid_Object = MibTableColumn
ccWlanEssid = _CcWlanEssid_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 1, 1, 3),
    _CcWlanEssid_Type()
)
ccWlanEssid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanEssid.setStatus("current")
_CcWlanSubnet_Type = SinglePointer
_CcWlanSubnet_Object = MibTableColumn
ccWlanSubnet = _CcWlanSubnet_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 1, 1, 4),
    _CcWlanSubnet_Type()
)
ccWlanSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanSubnet.setStatus("current")
_CcWlanPortalsAdopted_Type = MultiPointer255
_CcWlanPortalsAdopted_Object = MibTableColumn
ccWlanPortalsAdopted = _CcWlanPortalsAdopted_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 1, 1, 5),
    _CcWlanPortalsAdopted_Type()
)
ccWlanPortalsAdopted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanPortalsAdopted.setStatus("current")
_CcWlanEnable_Type = StaticRowEnable
_CcWlanEnable_Object = MibTableColumn
ccWlanEnable = _CcWlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 1, 1, 6),
    _CcWlanEnable_Type()
)
ccWlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanEnable.setStatus("current")
_CcWlanDisallowMuToMu_Type = TruthValue
_CcWlanDisallowMuToMu_Object = MibTableColumn
ccWlanDisallowMuToMu = _CcWlanDisallowMuToMu_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 1, 1, 7),
    _CcWlanDisallowMuToMu_Type()
)
ccWlanDisallowMuToMu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanDisallowMuToMu.setStatus("current")
_CcWlanVoicePrioritization_Type = TruthValue
_CcWlanVoicePrioritization_Object = MibTableColumn
ccWlanVoicePrioritization = _CcWlanVoicePrioritization_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 1, 1, 8),
    _CcWlanVoicePrioritization_Type()
)
ccWlanVoicePrioritization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanVoicePrioritization.setStatus("current")
_CcWlanAnswerBroadcastEss_Type = TruthValue
_CcWlanAnswerBroadcastEss_Object = MibTableColumn
ccWlanAnswerBroadcastEss = _CcWlanAnswerBroadcastEss_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 1, 1, 9),
    _CcWlanAnswerBroadcastEss_Type()
)
ccWlanAnswerBroadcastEss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAnswerBroadcastEss.setStatus("current")
_CcWlanMulticastAddr1_Type = PhysAddress
_CcWlanMulticastAddr1_Object = MibTableColumn
ccWlanMulticastAddr1 = _CcWlanMulticastAddr1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 1, 1, 10),
    _CcWlanMulticastAddr1_Type()
)
ccWlanMulticastAddr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanMulticastAddr1.setStatus("current")
_CcWlanMulticastAddr2_Type = PhysAddress
_CcWlanMulticastAddr2_Object = MibTableColumn
ccWlanMulticastAddr2 = _CcWlanMulticastAddr2_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 1, 1, 11),
    _CcWlanMulticastAddr2_Type()
)
ccWlanMulticastAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanMulticastAddr2.setStatus("current")


class _CcWlanMuAclDefault_Type(Integer32):
    """Custom type ccWlanMuAclDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowAllMusExceptThoseMatchingAclRules", 1),
          ("denyAllMusExceptThoseMatchingAclRules", 2))
    )


_CcWlanMuAclDefault_Type.__name__ = "Integer32"
_CcWlanMuAclDefault_Object = MibTableColumn
ccWlanMuAclDefault = _CcWlanMuAclDefault_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 1, 1, 12),
    _CcWlanMuAclDefault_Type()
)
ccWlanMuAclDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanMuAclDefault.setStatus("current")


class _CcWlanAuthentication_Type(Integer32):
    """Custom type ccWlanAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auth802dot1xEap", 2),
          ("authKerberos", 3),
          ("authNone", 1))
    )


_CcWlanAuthentication_Type.__name__ = "Integer32"
_CcWlanAuthentication_Object = MibTableColumn
ccWlanAuthentication = _CcWlanAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 1, 1, 13),
    _CcWlanAuthentication_Type()
)
ccWlanAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthentication.setStatus("current")


class _CcWlanEncryption_Type(Integer32):
    """Custom type ccWlanEncryption based on Integer32"""
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
        *(("cryptoKeyguardMcm", 4),
          ("cryptoNone", 1),
          ("cryptoWep104", 3),
          ("cryptoWep40", 2),
          ("cryptoWpa2Ccmp", 6),
          ("cryptoWpaTkip", 5))
    )


_CcWlanEncryption_Type.__name__ = "Integer32"
_CcWlanEncryption_Object = MibTableColumn
ccWlanEncryption = _CcWlanEncryption_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 1, 1, 14),
    _CcWlanEncryption_Type()
)
ccWlanEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanEncryption.setStatus("current")
_CcWlanWeight_Type = Integer32
_CcWlanWeight_Object = MibTableColumn
ccWlanWeight = _CcWlanWeight_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 1, 1, 15),
    _CcWlanWeight_Type()
)
ccWlanWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanWeight.setStatus("current")
_CcWlanAuth_ObjectIdentity = ObjectIdentity
ccWlanAuth = _CcWlanAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2)
)
_CcWlanAuthEapTable_Object = MibTable
ccWlanAuthEapTable = _CcWlanAuthEapTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 1)
)
if mibBuilder.loadTexts:
    ccWlanAuthEapTable.setStatus("current")
_CcWlanAuthEapEntry_Object = MibTableRow
ccWlanAuthEapEntry = _CcWlanAuthEapEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 1, 1)
)
ccWlanAuthEapEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWlanIndex"),
)
if mibBuilder.loadTexts:
    ccWlanAuthEapEntry.setStatus("current")
_CcWlanAuthEapReauthenticationEnable_Type = TruthValue
_CcWlanAuthEapReauthenticationEnable_Object = MibTableColumn
ccWlanAuthEapReauthenticationEnable = _CcWlanAuthEapReauthenticationEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 1, 1, 1),
    _CcWlanAuthEapReauthenticationEnable_Type()
)
ccWlanAuthEapReauthenticationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthEapReauthenticationEnable.setStatus("current")


class _CcWlanAuthEapReauthenticationPeriod_Type(Unsigned32):
    """Custom type ccWlanAuthEapReauthenticationPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 9999),
    )


_CcWlanAuthEapReauthenticationPeriod_Type.__name__ = "Unsigned32"
_CcWlanAuthEapReauthenticationPeriod_Object = MibTableColumn
ccWlanAuthEapReauthenticationPeriod = _CcWlanAuthEapReauthenticationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 1, 1, 2),
    _CcWlanAuthEapReauthenticationPeriod_Type()
)
ccWlanAuthEapReauthenticationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthEapReauthenticationPeriod.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanAuthEapReauthenticationPeriod.setUnits("seconds")


class _CcWlanAuthEapReauthenticationMaxRetries_Type(Unsigned32):
    """Custom type ccWlanAuthEapReauthenticationMaxRetries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CcWlanAuthEapReauthenticationMaxRetries_Type.__name__ = "Unsigned32"
_CcWlanAuthEapReauthenticationMaxRetries_Object = MibTableColumn
ccWlanAuthEapReauthenticationMaxRetries = _CcWlanAuthEapReauthenticationMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 1, 1, 3),
    _CcWlanAuthEapReauthenticationMaxRetries_Type()
)
ccWlanAuthEapReauthenticationMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthEapReauthenticationMaxRetries.setStatus("current")
_CcWlanAuthEapRadius1Server_Type = IpAddress
_CcWlanAuthEapRadius1Server_Object = MibTableColumn
ccWlanAuthEapRadius1Server = _CcWlanAuthEapRadius1Server_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 1, 1, 4),
    _CcWlanAuthEapRadius1Server_Type()
)
ccWlanAuthEapRadius1Server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthEapRadius1Server.setStatus("current")
_CcWlanAuthEapRadius1Port_Type = Unsigned32
_CcWlanAuthEapRadius1Port_Object = MibTableColumn
ccWlanAuthEapRadius1Port = _CcWlanAuthEapRadius1Port_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 1, 1, 5),
    _CcWlanAuthEapRadius1Port_Type()
)
ccWlanAuthEapRadius1Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthEapRadius1Port.setStatus("current")
_CcWlanAuthEapRadius1SharedSecret_Type = Password
_CcWlanAuthEapRadius1SharedSecret_Object = MibTableColumn
ccWlanAuthEapRadius1SharedSecret = _CcWlanAuthEapRadius1SharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 1, 1, 6),
    _CcWlanAuthEapRadius1SharedSecret_Type()
)
ccWlanAuthEapRadius1SharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthEapRadius1SharedSecret.setStatus("current")
_CcWlanAuthEapRadius2Server_Type = IpAddress
_CcWlanAuthEapRadius2Server_Object = MibTableColumn
ccWlanAuthEapRadius2Server = _CcWlanAuthEapRadius2Server_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 1, 1, 7),
    _CcWlanAuthEapRadius2Server_Type()
)
ccWlanAuthEapRadius2Server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthEapRadius2Server.setStatus("current")
_CcWlanAuthEapRadius2Port_Type = Unsigned32
_CcWlanAuthEapRadius2Port_Object = MibTableColumn
ccWlanAuthEapRadius2Port = _CcWlanAuthEapRadius2Port_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 1, 1, 8),
    _CcWlanAuthEapRadius2Port_Type()
)
ccWlanAuthEapRadius2Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthEapRadius2Port.setStatus("current")
_CcWlanAuthEapRadius2SharedSecret_Type = Password
_CcWlanAuthEapRadius2SharedSecret_Object = MibTableColumn
ccWlanAuthEapRadius2SharedSecret = _CcWlanAuthEapRadius2SharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 1, 1, 9),
    _CcWlanAuthEapRadius2SharedSecret_Type()
)
ccWlanAuthEapRadius2SharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthEapRadius2SharedSecret.setStatus("current")


class _CcWlanAuthEapMuQuietPeriod_Type(Unsigned32):
    """Custom type ccWlanAuthEapMuQuietPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcWlanAuthEapMuQuietPeriod_Type.__name__ = "Unsigned32"
_CcWlanAuthEapMuQuietPeriod_Object = MibTableColumn
ccWlanAuthEapMuQuietPeriod = _CcWlanAuthEapMuQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 1, 1, 10),
    _CcWlanAuthEapMuQuietPeriod_Type()
)
ccWlanAuthEapMuQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthEapMuQuietPeriod.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanAuthEapMuQuietPeriod.setUnits("seconds")


class _CcWlanAuthEapMuTimeout_Type(Unsigned32):
    """Custom type ccWlanAuthEapMuTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CcWlanAuthEapMuTimeout_Type.__name__ = "Unsigned32"
_CcWlanAuthEapMuTimeout_Object = MibTableColumn
ccWlanAuthEapMuTimeout = _CcWlanAuthEapMuTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 1, 1, 11),
    _CcWlanAuthEapMuTimeout_Type()
)
ccWlanAuthEapMuTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthEapMuTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanAuthEapMuTimeout.setUnits("seconds")


class _CcWlanAuthEapMuTxPeriod_Type(Unsigned32):
    """Custom type ccWlanAuthEapMuTxPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcWlanAuthEapMuTxPeriod_Type.__name__ = "Unsigned32"
_CcWlanAuthEapMuTxPeriod_Object = MibTableColumn
ccWlanAuthEapMuTxPeriod = _CcWlanAuthEapMuTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 1, 1, 12),
    _CcWlanAuthEapMuTxPeriod_Type()
)
ccWlanAuthEapMuTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthEapMuTxPeriod.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanAuthEapMuTxPeriod.setUnits("seconds")


class _CcWlanAuthEapMuMaxRetries_Type(Unsigned32):
    """Custom type ccWlanAuthEapMuMaxRetries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CcWlanAuthEapMuMaxRetries_Type.__name__ = "Unsigned32"
_CcWlanAuthEapMuMaxRetries_Object = MibTableColumn
ccWlanAuthEapMuMaxRetries = _CcWlanAuthEapMuMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 1, 1, 13),
    _CcWlanAuthEapMuMaxRetries_Type()
)
ccWlanAuthEapMuMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthEapMuMaxRetries.setStatus("current")


class _CcWlanAuthEapServerTimeout_Type(Unsigned32):
    """Custom type ccWlanAuthEapServerTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CcWlanAuthEapServerTimeout_Type.__name__ = "Unsigned32"
_CcWlanAuthEapServerTimeout_Object = MibTableColumn
ccWlanAuthEapServerTimeout = _CcWlanAuthEapServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 1, 1, 14),
    _CcWlanAuthEapServerTimeout_Type()
)
ccWlanAuthEapServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthEapServerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanAuthEapServerTimeout.setUnits("seconds")


class _CcWlanAuthEapServerMaxRetries_Type(Unsigned32):
    """Custom type ccWlanAuthEapServerMaxRetries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CcWlanAuthEapServerMaxRetries_Type.__name__ = "Unsigned32"
_CcWlanAuthEapServerMaxRetries_Object = MibTableColumn
ccWlanAuthEapServerMaxRetries = _CcWlanAuthEapServerMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 1, 1, 15),
    _CcWlanAuthEapServerMaxRetries_Type()
)
ccWlanAuthEapServerMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthEapServerMaxRetries.setStatus("current")
_CcWlanAuthEapRadiusAcctMode_Type = TruthValue
_CcWlanAuthEapRadiusAcctMode_Object = MibTableColumn
ccWlanAuthEapRadiusAcctMode = _CcWlanAuthEapRadiusAcctMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 1, 1, 16),
    _CcWlanAuthEapRadiusAcctMode_Type()
)
ccWlanAuthEapRadiusAcctMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthEapRadiusAcctMode.setStatus("current")


class _CcWlanAuthEapRadiusAcctMuTimeout_Type(Unsigned32):
    """Custom type ccWlanAuthEapRadiusAcctMuTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CcWlanAuthEapRadiusAcctMuTimeout_Type.__name__ = "Unsigned32"
_CcWlanAuthEapRadiusAcctMuTimeout_Object = MibTableColumn
ccWlanAuthEapRadiusAcctMuTimeout = _CcWlanAuthEapRadiusAcctMuTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 1, 1, 17),
    _CcWlanAuthEapRadiusAcctMuTimeout_Type()
)
ccWlanAuthEapRadiusAcctMuTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthEapRadiusAcctMuTimeout.setStatus("current")


class _CcWlanAuthEapRadiusAcctMuRetries_Type(Unsigned32):
    """Custom type ccWlanAuthEapRadiusAcctMuRetries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CcWlanAuthEapRadiusAcctMuRetries_Type.__name__ = "Unsigned32"
_CcWlanAuthEapRadiusAcctMuRetries_Object = MibTableColumn
ccWlanAuthEapRadiusAcctMuRetries = _CcWlanAuthEapRadiusAcctMuRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 1, 1, 18),
    _CcWlanAuthEapRadiusAcctMuRetries_Type()
)
ccWlanAuthEapRadiusAcctMuRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthEapRadiusAcctMuRetries.setStatus("current")
_CcWlanAuthEapSyslogMode_Type = TruthValue
_CcWlanAuthEapSyslogMode_Object = MibTableColumn
ccWlanAuthEapSyslogMode = _CcWlanAuthEapSyslogMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 1, 1, 19),
    _CcWlanAuthEapSyslogMode_Type()
)
ccWlanAuthEapSyslogMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthEapSyslogMode.setStatus("current")
_CcWlanAuthEapSyslogSeverIp_Type = IpAddress
_CcWlanAuthEapSyslogSeverIp_Object = MibTableColumn
ccWlanAuthEapSyslogSeverIp = _CcWlanAuthEapSyslogSeverIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 1, 1, 20),
    _CcWlanAuthEapSyslogSeverIp_Type()
)
ccWlanAuthEapSyslogSeverIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthEapSyslogSeverIp.setStatus("current")
_CcWlanAuthKerberosTable_Object = MibTable
ccWlanAuthKerberosTable = _CcWlanAuthKerberosTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 2)
)
if mibBuilder.loadTexts:
    ccWlanAuthKerberosTable.setStatus("current")
_CcWlanAuthKerberosEntry_Object = MibTableRow
ccWlanAuthKerberosEntry = _CcWlanAuthKerberosEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 2, 1)
)
ccWlanAuthKerberosEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWlanIndex"),
)
if mibBuilder.loadTexts:
    ccWlanAuthKerberosEntry.setStatus("current")
_CcWlanAuthKerberosRealmName_Type = DisplayString
_CcWlanAuthKerberosRealmName_Object = MibTableColumn
ccWlanAuthKerberosRealmName = _CcWlanAuthKerberosRealmName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 2, 1, 1),
    _CcWlanAuthKerberosRealmName_Type()
)
ccWlanAuthKerberosRealmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthKerberosRealmName.setStatus("current")
_CcWlanAuthKerberosUsername_Type = DisplayString
_CcWlanAuthKerberosUsername_Object = MibTableColumn
ccWlanAuthKerberosUsername = _CcWlanAuthKerberosUsername_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 2, 1, 2),
    _CcWlanAuthKerberosUsername_Type()
)
ccWlanAuthKerberosUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthKerberosUsername.setStatus("current")
_CcWlanAuthKerberosPassword_Type = Password
_CcWlanAuthKerberosPassword_Object = MibTableColumn
ccWlanAuthKerberosPassword = _CcWlanAuthKerberosPassword_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 2, 1, 3),
    _CcWlanAuthKerberosPassword_Type()
)
ccWlanAuthKerberosPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthKerberosPassword.setStatus("current")
_CcWlanAuthKerberosKdcServerIp1_Type = IpAddress
_CcWlanAuthKerberosKdcServerIp1_Object = MibTableColumn
ccWlanAuthKerberosKdcServerIp1 = _CcWlanAuthKerberosKdcServerIp1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 2, 1, 4),
    _CcWlanAuthKerberosKdcServerIp1_Type()
)
ccWlanAuthKerberosKdcServerIp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthKerberosKdcServerIp1.setStatus("current")
_CcWlanAuthKerberosKdcPort1_Type = Unsigned32
_CcWlanAuthKerberosKdcPort1_Object = MibTableColumn
ccWlanAuthKerberosKdcPort1 = _CcWlanAuthKerberosKdcPort1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 2, 1, 5),
    _CcWlanAuthKerberosKdcPort1_Type()
)
ccWlanAuthKerberosKdcPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthKerberosKdcPort1.setStatus("current")
_CcWlanAuthKerberosKdcServerIp2_Type = IpAddress
_CcWlanAuthKerberosKdcServerIp2_Object = MibTableColumn
ccWlanAuthKerberosKdcServerIp2 = _CcWlanAuthKerberosKdcServerIp2_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 2, 1, 6),
    _CcWlanAuthKerberosKdcServerIp2_Type()
)
ccWlanAuthKerberosKdcServerIp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthKerberosKdcServerIp2.setStatus("current")
_CcWlanAuthKerberosKdcPort2_Type = Unsigned32
_CcWlanAuthKerberosKdcPort2_Object = MibTableColumn
ccWlanAuthKerberosKdcPort2 = _CcWlanAuthKerberosKdcPort2_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 2, 1, 7),
    _CcWlanAuthKerberosKdcPort2_Type()
)
ccWlanAuthKerberosKdcPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthKerberosKdcPort2.setStatus("current")
_CcWlanAuthKerberosKdcServerIpR_Type = IpAddress
_CcWlanAuthKerberosKdcServerIpR_Object = MibTableColumn
ccWlanAuthKerberosKdcServerIpR = _CcWlanAuthKerberosKdcServerIpR_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 2, 1, 8),
    _CcWlanAuthKerberosKdcServerIpR_Type()
)
ccWlanAuthKerberosKdcServerIpR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthKerberosKdcServerIpR.setStatus("current")
_CcWlanAuthKerberosKdcPortR_Type = Unsigned32
_CcWlanAuthKerberosKdcPortR_Object = MibTableColumn
ccWlanAuthKerberosKdcPortR = _CcWlanAuthKerberosKdcPortR_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 2, 2, 1, 9),
    _CcWlanAuthKerberosKdcPortR_Type()
)
ccWlanAuthKerberosKdcPortR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanAuthKerberosKdcPortR.setStatus("current")
_CcWlanCrypto_ObjectIdentity = ObjectIdentity
ccWlanCrypto = _CcWlanCrypto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3)
)
_CcWlanCryptoWepTable_Object = MibTable
ccWlanCryptoWepTable = _CcWlanCryptoWepTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 1)
)
if mibBuilder.loadTexts:
    ccWlanCryptoWepTable.setStatus("current")
_CcWlanCryptoWepEntry_Object = MibTableRow
ccWlanCryptoWepEntry = _CcWlanCryptoWepEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 1, 1)
)
ccWlanCryptoWepEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWlanIndex"),
)
if mibBuilder.loadTexts:
    ccWlanCryptoWepEntry.setStatus("current")


class _CcWlanCryptoWepPassKey_Type(Password):
    """Custom type ccWlanCryptoWepPassKey based on Password"""
    subtypeSpec = Password.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 32),
    )


_CcWlanCryptoWepPassKey_Type.__name__ = "Password"
_CcWlanCryptoWepPassKey_Object = MibTableColumn
ccWlanCryptoWepPassKey = _CcWlanCryptoWepPassKey_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 1, 1, 1),
    _CcWlanCryptoWepPassKey_Type()
)
ccWlanCryptoWepPassKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanCryptoWepPassKey.setStatus("current")


class _CcWlanCryptoWepKey1_Type(OctetString):
    """Custom type ccWlanCryptoWepKey1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_CcWlanCryptoWepKey1_Type.__name__ = "OctetString"
_CcWlanCryptoWepKey1_Object = MibTableColumn
ccWlanCryptoWepKey1 = _CcWlanCryptoWepKey1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 1, 1, 2),
    _CcWlanCryptoWepKey1_Type()
)
ccWlanCryptoWepKey1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanCryptoWepKey1.setStatus("current")


class _CcWlanCryptoWepKey2_Type(OctetString):
    """Custom type ccWlanCryptoWepKey2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_CcWlanCryptoWepKey2_Type.__name__ = "OctetString"
_CcWlanCryptoWepKey2_Object = MibTableColumn
ccWlanCryptoWepKey2 = _CcWlanCryptoWepKey2_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 1, 1, 3),
    _CcWlanCryptoWepKey2_Type()
)
ccWlanCryptoWepKey2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanCryptoWepKey2.setStatus("current")


class _CcWlanCryptoWepKey3_Type(OctetString):
    """Custom type ccWlanCryptoWepKey3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_CcWlanCryptoWepKey3_Type.__name__ = "OctetString"
_CcWlanCryptoWepKey3_Object = MibTableColumn
ccWlanCryptoWepKey3 = _CcWlanCryptoWepKey3_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 1, 1, 4),
    _CcWlanCryptoWepKey3_Type()
)
ccWlanCryptoWepKey3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanCryptoWepKey3.setStatus("current")


class _CcWlanCryptoWepKey4_Type(OctetString):
    """Custom type ccWlanCryptoWepKey4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_CcWlanCryptoWepKey4_Type.__name__ = "OctetString"
_CcWlanCryptoWepKey4_Object = MibTableColumn
ccWlanCryptoWepKey4 = _CcWlanCryptoWepKey4_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 1, 1, 5),
    _CcWlanCryptoWepKey4_Type()
)
ccWlanCryptoWepKey4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanCryptoWepKey4.setStatus("current")


class _CcWlanCryptoWepKeyToUse_Type(Integer32):
    """Custom type ccWlanCryptoWepKeyToUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CcWlanCryptoWepKeyToUse_Type.__name__ = "Integer32"
_CcWlanCryptoWepKeyToUse_Object = MibTableColumn
ccWlanCryptoWepKeyToUse = _CcWlanCryptoWepKeyToUse_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 1, 1, 6),
    _CcWlanCryptoWepKeyToUse_Type()
)
ccWlanCryptoWepKeyToUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanCryptoWepKeyToUse.setStatus("current")
_CcWlanCryptoWpaTable_Object = MibTable
ccWlanCryptoWpaTable = _CcWlanCryptoWpaTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 2)
)
if mibBuilder.loadTexts:
    ccWlanCryptoWpaTable.setStatus("current")
_CcWlanCryptoWpaEntry_Object = MibTableRow
ccWlanCryptoWpaEntry = _CcWlanCryptoWpaEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 2, 1)
)
ccWlanCryptoWpaEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWlanIndex"),
)
if mibBuilder.loadTexts:
    ccWlanCryptoWpaEntry.setStatus("current")
_CcWlanCryptoWpaBcastKeyRotation_Type = TruthValue
_CcWlanCryptoWpaBcastKeyRotation_Object = MibTableColumn
ccWlanCryptoWpaBcastKeyRotation = _CcWlanCryptoWpaBcastKeyRotation_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 2, 1, 1),
    _CcWlanCryptoWpaBcastKeyRotation_Type()
)
ccWlanCryptoWpaBcastKeyRotation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanCryptoWpaBcastKeyRotation.setStatus("current")


class _CcWlanCryptoWpaKeyRotationInterval_Type(Unsigned32):
    """Custom type ccWlanCryptoWpaKeyRotationInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 604800),
    )


_CcWlanCryptoWpaKeyRotationInterval_Type.__name__ = "Unsigned32"
_CcWlanCryptoWpaKeyRotationInterval_Object = MibTableColumn
ccWlanCryptoWpaKeyRotationInterval = _CcWlanCryptoWpaKeyRotationInterval_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 2, 1, 2),
    _CcWlanCryptoWpaKeyRotationInterval_Type()
)
ccWlanCryptoWpaKeyRotationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanCryptoWpaKeyRotationInterval.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanCryptoWpaKeyRotationInterval.setUnits("seconds")


class _CcWlanCryptoWpaKeyToUse_Type(Integer32):
    """Custom type ccWlanCryptoWpaKeyToUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("use128bitKey", 1),
          ("useAsciiPassPhrase", 2))
    )


_CcWlanCryptoWpaKeyToUse_Type.__name__ = "Integer32"
_CcWlanCryptoWpaKeyToUse_Object = MibTableColumn
ccWlanCryptoWpaKeyToUse = _CcWlanCryptoWpaKeyToUse_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 2, 1, 3),
    _CcWlanCryptoWpaKeyToUse_Type()
)
ccWlanCryptoWpaKeyToUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanCryptoWpaKeyToUse.setStatus("current")


class _CcWlanCryptoWpaPassphrase_Type(OctetString):
    """Custom type ccWlanCryptoWpaPassphrase based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
    )


_CcWlanCryptoWpaPassphrase_Type.__name__ = "OctetString"
_CcWlanCryptoWpaPassphrase_Object = MibTableColumn
ccWlanCryptoWpaPassphrase = _CcWlanCryptoWpaPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 2, 1, 4),
    _CcWlanCryptoWpaPassphrase_Type()
)
ccWlanCryptoWpaPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanCryptoWpaPassphrase.setStatus("current")


class _CcWlanCryptoWpaKey_Type(OctetString):
    """Custom type ccWlanCryptoWpaKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_CcWlanCryptoWpaKey_Type.__name__ = "OctetString"
_CcWlanCryptoWpaKey_Object = MibTableColumn
ccWlanCryptoWpaKey = _CcWlanCryptoWpaKey_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 2, 1, 5),
    _CcWlanCryptoWpaKey_Type()
)
ccWlanCryptoWpaKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanCryptoWpaKey.setStatus("current")
_CcWlanCryptoKeyguardTable_Object = MibTable
ccWlanCryptoKeyguardTable = _CcWlanCryptoKeyguardTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 3)
)
if mibBuilder.loadTexts:
    ccWlanCryptoKeyguardTable.setStatus("current")
_CcWlanCryptoKeyguardEntry_Object = MibTableRow
ccWlanCryptoKeyguardEntry = _CcWlanCryptoKeyguardEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 3, 1)
)
ccWlanCryptoKeyguardEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWlanIndex"),
)
if mibBuilder.loadTexts:
    ccWlanCryptoKeyguardEntry.setStatus("current")


class _CcWlanCryptoKeyguardPasskey_Type(OctetString):
    """Custom type ccWlanCryptoKeyguardPasskey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 32),
    )


_CcWlanCryptoKeyguardPasskey_Type.__name__ = "OctetString"
_CcWlanCryptoKeyguardPasskey_Object = MibTableColumn
ccWlanCryptoKeyguardPasskey = _CcWlanCryptoKeyguardPasskey_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 3, 1, 1),
    _CcWlanCryptoKeyguardPasskey_Type()
)
ccWlanCryptoKeyguardPasskey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanCryptoKeyguardPasskey.setStatus("current")


class _CcWlanCryptoKeyguardKey1_Type(OctetString):
    """Custom type ccWlanCryptoKeyguardKey1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_CcWlanCryptoKeyguardKey1_Type.__name__ = "OctetString"
_CcWlanCryptoKeyguardKey1_Object = MibTableColumn
ccWlanCryptoKeyguardKey1 = _CcWlanCryptoKeyguardKey1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 3, 1, 2),
    _CcWlanCryptoKeyguardKey1_Type()
)
ccWlanCryptoKeyguardKey1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanCryptoKeyguardKey1.setStatus("current")


class _CcWlanCryptoKeyguardKey2_Type(OctetString):
    """Custom type ccWlanCryptoKeyguardKey2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_CcWlanCryptoKeyguardKey2_Type.__name__ = "OctetString"
_CcWlanCryptoKeyguardKey2_Object = MibTableColumn
ccWlanCryptoKeyguardKey2 = _CcWlanCryptoKeyguardKey2_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 3, 1, 3),
    _CcWlanCryptoKeyguardKey2_Type()
)
ccWlanCryptoKeyguardKey2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanCryptoKeyguardKey2.setStatus("current")


class _CcWlanCryptoKeyguardKey3_Type(OctetString):
    """Custom type ccWlanCryptoKeyguardKey3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_CcWlanCryptoKeyguardKey3_Type.__name__ = "OctetString"
_CcWlanCryptoKeyguardKey3_Object = MibTableColumn
ccWlanCryptoKeyguardKey3 = _CcWlanCryptoKeyguardKey3_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 3, 1, 4),
    _CcWlanCryptoKeyguardKey3_Type()
)
ccWlanCryptoKeyguardKey3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanCryptoKeyguardKey3.setStatus("current")


class _CcWlanCryptoKeyguardKey4_Type(OctetString):
    """Custom type ccWlanCryptoKeyguardKey4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_CcWlanCryptoKeyguardKey4_Type.__name__ = "OctetString"
_CcWlanCryptoKeyguardKey4_Object = MibTableColumn
ccWlanCryptoKeyguardKey4 = _CcWlanCryptoKeyguardKey4_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 3, 1, 5),
    _CcWlanCryptoKeyguardKey4_Type()
)
ccWlanCryptoKeyguardKey4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanCryptoKeyguardKey4.setStatus("current")


class _CcWlanCryptoKeyguardKeyToUse_Type(Integer32):
    """Custom type ccWlanCryptoKeyguardKeyToUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CcWlanCryptoKeyguardKeyToUse_Type.__name__ = "Integer32"
_CcWlanCryptoKeyguardKeyToUse_Object = MibTableColumn
ccWlanCryptoKeyguardKeyToUse = _CcWlanCryptoKeyguardKeyToUse_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 3, 1, 6),
    _CcWlanCryptoKeyguardKeyToUse_Type()
)
ccWlanCryptoKeyguardKeyToUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanCryptoKeyguardKeyToUse.setStatus("current")
_CcWlanCryptoWpaTwoTable_Object = MibTable
ccWlanCryptoWpaTwoTable = _CcWlanCryptoWpaTwoTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 4)
)
if mibBuilder.loadTexts:
    ccWlanCryptoWpaTwoTable.setStatus("current")
_CcWlanCryptoWpaTwoEntry_Object = MibTableRow
ccWlanCryptoWpaTwoEntry = _CcWlanCryptoWpaTwoEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 4, 1)
)
ccWlanCryptoWpaTwoEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWlanIndex"),
)
if mibBuilder.loadTexts:
    ccWlanCryptoWpaTwoEntry.setStatus("current")
_CcWlanCryptoWpaTwoBcastKeyRotation_Type = TruthValue
_CcWlanCryptoWpaTwoBcastKeyRotation_Object = MibTableColumn
ccWlanCryptoWpaTwoBcastKeyRotation = _CcWlanCryptoWpaTwoBcastKeyRotation_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 4, 1, 1),
    _CcWlanCryptoWpaTwoBcastKeyRotation_Type()
)
ccWlanCryptoWpaTwoBcastKeyRotation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanCryptoWpaTwoBcastKeyRotation.setStatus("current")


class _CcWlanCryptoWpaTwoKeyRotationInterval_Type(Unsigned32):
    """Custom type ccWlanCryptoWpaTwoKeyRotationInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 604800),
    )


_CcWlanCryptoWpaTwoKeyRotationInterval_Type.__name__ = "Unsigned32"
_CcWlanCryptoWpaTwoKeyRotationInterval_Object = MibTableColumn
ccWlanCryptoWpaTwoKeyRotationInterval = _CcWlanCryptoWpaTwoKeyRotationInterval_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 4, 1, 2),
    _CcWlanCryptoWpaTwoKeyRotationInterval_Type()
)
ccWlanCryptoWpaTwoKeyRotationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanCryptoWpaTwoKeyRotationInterval.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanCryptoWpaTwoKeyRotationInterval.setUnits("seconds")


class _CcWlanCryptoWpaTwoKeyToUse_Type(Integer32):
    """Custom type ccWlanCryptoWpaTwoKeyToUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("use128bitKey", 2),
          ("useAsciiPassphrase", 1))
    )


_CcWlanCryptoWpaTwoKeyToUse_Type.__name__ = "Integer32"
_CcWlanCryptoWpaTwoKeyToUse_Object = MibTableColumn
ccWlanCryptoWpaTwoKeyToUse = _CcWlanCryptoWpaTwoKeyToUse_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 4, 1, 3),
    _CcWlanCryptoWpaTwoKeyToUse_Type()
)
ccWlanCryptoWpaTwoKeyToUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanCryptoWpaTwoKeyToUse.setStatus("current")


class _CcWlanCryptoWpaTwoPassphrase_Type(Password):
    """Custom type ccWlanCryptoWpaTwoPassphrase based on Password"""
    subtypeSpec = Password.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
    )


_CcWlanCryptoWpaTwoPassphrase_Type.__name__ = "Password"
_CcWlanCryptoWpaTwoPassphrase_Object = MibTableColumn
ccWlanCryptoWpaTwoPassphrase = _CcWlanCryptoWpaTwoPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 4, 1, 4),
    _CcWlanCryptoWpaTwoPassphrase_Type()
)
ccWlanCryptoWpaTwoPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanCryptoWpaTwoPassphrase.setStatus("current")


class _CcWlanCryptoWpaTwoKey_Type(OctetString):
    """Custom type ccWlanCryptoWpaTwoKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_CcWlanCryptoWpaTwoKey_Type.__name__ = "OctetString"
_CcWlanCryptoWpaTwoKey_Object = MibTableColumn
ccWlanCryptoWpaTwoKey = _CcWlanCryptoWpaTwoKey_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 4, 1, 5),
    _CcWlanCryptoWpaTwoKey_Type()
)
ccWlanCryptoWpaTwoKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanCryptoWpaTwoKey.setStatus("current")
_CcWlanCryptoWpaTwoAllowTkipClient_Type = TruthValue
_CcWlanCryptoWpaTwoAllowTkipClient_Object = MibTableColumn
ccWlanCryptoWpaTwoAllowTkipClient = _CcWlanCryptoWpaTwoAllowTkipClient_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 4, 1, 6),
    _CcWlanCryptoWpaTwoAllowTkipClient_Type()
)
ccWlanCryptoWpaTwoAllowTkipClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanCryptoWpaTwoAllowTkipClient.setStatus("current")
_CcWlanCryptoWpaTwoFastRoamPreAuth_Type = TruthValue
_CcWlanCryptoWpaTwoFastRoamPreAuth_Object = MibTableColumn
ccWlanCryptoWpaTwoFastRoamPreAuth = _CcWlanCryptoWpaTwoFastRoamPreAuth_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 4, 1, 7),
    _CcWlanCryptoWpaTwoFastRoamPreAuth_Type()
)
ccWlanCryptoWpaTwoFastRoamPreAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanCryptoWpaTwoFastRoamPreAuth.setStatus("current")
_CcWlanCryptoWpaTwoFastRoamKeyCache_Type = TruthValue
_CcWlanCryptoWpaTwoFastRoamKeyCache_Object = MibTableColumn
ccWlanCryptoWpaTwoFastRoamKeyCache = _CcWlanCryptoWpaTwoFastRoamKeyCache_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 3, 4, 1, 8),
    _CcWlanCryptoWpaTwoFastRoamKeyCache_Type()
)
ccWlanCryptoWpaTwoFastRoamKeyCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanCryptoWpaTwoFastRoamKeyCache.setStatus("current")
_CcWlanMuAclTable_Object = MibTable
ccWlanMuAclTable = _CcWlanMuAclTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 4)
)
if mibBuilder.loadTexts:
    ccWlanMuAclTable.setStatus("current")
_CcWlanMuAclEntry_Object = MibTableRow
ccWlanMuAclEntry = _CcWlanMuAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 4, 1)
)
ccWlanMuAclEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWlanIndex"),
    (0, "SYMBOL-CC-WS2000-MIB", "ccWlanMuAclIndex"),
)
if mibBuilder.loadTexts:
    ccWlanMuAclEntry.setStatus("current")


class _CcWlanMuAclIndex_Type(Integer32):
    """Custom type ccWlanMuAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_CcWlanMuAclIndex_Type.__name__ = "Integer32"
_CcWlanMuAclIndex_Object = MibTableColumn
ccWlanMuAclIndex = _CcWlanMuAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 4, 1, 1),
    _CcWlanMuAclIndex_Type()
)
ccWlanMuAclIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccWlanMuAclIndex.setStatus("current")
_CcWlanMuAclStartingMac_Type = PhysAddress
_CcWlanMuAclStartingMac_Object = MibTableColumn
ccWlanMuAclStartingMac = _CcWlanMuAclStartingMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 4, 1, 2),
    _CcWlanMuAclStartingMac_Type()
)
ccWlanMuAclStartingMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanMuAclStartingMac.setStatus("current")
_CcWlanMuAclEndingMac_Type = PhysAddress
_CcWlanMuAclEndingMac_Object = MibTableColumn
ccWlanMuAclEndingMac = _CcWlanMuAclEndingMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 4, 1, 3),
    _CcWlanMuAclEndingMac_Type()
)
ccWlanMuAclEndingMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanMuAclEndingMac.setStatus("current")
_CcWlanMuAclRowStatus_Type = AbbrevRowStatus
_CcWlanMuAclRowStatus_Object = MibTableColumn
ccWlanMuAclRowStatus = _CcWlanMuAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 4, 1, 4),
    _CcWlanMuAclRowStatus_Type()
)
ccWlanMuAclRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanMuAclRowStatus.setStatus("current")


class _CcWlanBwShareMode_Type(Integer32):
    """Custom type ccWlanBwShareMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("roundRobin", 2),
          ("weightedRoundRobin", 3))
    )


_CcWlanBwShareMode_Type.__name__ = "Integer32"
_CcWlanBwShareMode_Object = MibScalar
ccWlanBwShareMode = _CcWlanBwShareMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 5),
    _CcWlanBwShareMode_Type()
)
ccWlanBwShareMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanBwShareMode.setStatus("current")
_CcWlanQosMonitorTable_Object = MibTable
ccWlanQosMonitorTable = _CcWlanQosMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 6)
)
if mibBuilder.loadTexts:
    ccWlanQosMonitorTable.setStatus("current")
_CcWlanQosMonitorEntry_Object = MibTableRow
ccWlanQosMonitorEntry = _CcWlanQosMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 6, 1)
)
ccWlanQosMonitorEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWlanIndex"),
    (0, "SYMBOL-CC-WS2000-MIB", "ccPortalIndex"),
)
if mibBuilder.loadTexts:
    ccWlanQosMonitorEntry.setStatus("current")
_CcWlanQosMonitorSent_Type = Counter32
_CcWlanQosMonitorSent_Object = MibTableColumn
ccWlanQosMonitorSent = _CcWlanQosMonitorSent_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 6, 1, 1),
    _CcWlanQosMonitorSent_Type()
)
ccWlanQosMonitorSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanQosMonitorSent.setStatus("current")
_CcWlanQosMonitorDropped_Type = Counter32
_CcWlanQosMonitorDropped_Object = MibTableColumn
ccWlanQosMonitorDropped = _CcWlanQosMonitorDropped_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 6, 1, 2),
    _CcWlanQosMonitorDropped_Type()
)
ccWlanQosMonitorDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanQosMonitorDropped.setStatus("current")
_CcWlanRfSum_ObjectIdentity = ObjectIdentity
ccWlanRfSum = _CcWlanRfSum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100)
)
_CcWlanStatsTable_Object = MibTable
ccWlanStatsTable = _CcWlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 1)
)
if mibBuilder.loadTexts:
    ccWlanStatsTable.setStatus("current")
_CcWlanStatsEntry_Object = MibTableRow
ccWlanStatsEntry = _CcWlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 1, 1)
)
ccWlanStatsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWlanIndex"),
)
if mibBuilder.loadTexts:
    ccWlanStatsEntry.setStatus("current")
_CcWlanTxPktsUcast_Type = Counter32
_CcWlanTxPktsUcast_Object = MibTableColumn
ccWlanTxPktsUcast = _CcWlanTxPktsUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 1, 1, 1),
    _CcWlanTxPktsUcast_Type()
)
ccWlanTxPktsUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxPktsUcast.setStatus("current")
_CcWlanRxPktsUcast_Type = Counter32
_CcWlanRxPktsUcast_Object = MibTableColumn
ccWlanRxPktsUcast = _CcWlanRxPktsUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 1, 1, 2),
    _CcWlanRxPktsUcast_Type()
)
ccWlanRxPktsUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxPktsUcast.setStatus("current")
_CcWlanRxPktsNUcast_Type = Counter32
_CcWlanRxPktsNUcast_Object = MibTableColumn
ccWlanRxPktsNUcast = _CcWlanRxPktsNUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 1, 1, 3),
    _CcWlanRxPktsNUcast_Type()
)
ccWlanRxPktsNUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxPktsNUcast.setStatus("current")
_CcWlanTxOctetsUcast_Type = Counter32
_CcWlanTxOctetsUcast_Object = MibTableColumn
ccWlanTxOctetsUcast = _CcWlanTxOctetsUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 1, 1, 4),
    _CcWlanTxOctetsUcast_Type()
)
ccWlanTxOctetsUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxOctetsUcast.setStatus("current")
_CcWlanRxOctetsUcast_Type = Counter32
_CcWlanRxOctetsUcast_Object = MibTableColumn
ccWlanRxOctetsUcast = _CcWlanRxOctetsUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 1, 1, 5),
    _CcWlanRxOctetsUcast_Type()
)
ccWlanRxOctetsUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxOctetsUcast.setStatus("current")
_CcWlanRxOctetsNUcast_Type = Counter32
_CcWlanRxOctetsNUcast_Object = MibTableColumn
ccWlanRxOctetsNUcast = _CcWlanRxOctetsNUcast_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 1, 1, 6),
    _CcWlanRxOctetsNUcast_Type()
)
ccWlanRxOctetsNUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxOctetsNUcast.setStatus("current")
_CcWlanRxUndecryptablePkts_Type = Counter32
_CcWlanRxUndecryptablePkts_Object = MibTableColumn
ccWlanRxUndecryptablePkts = _CcWlanRxUndecryptablePkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 1, 1, 7),
    _CcWlanRxUndecryptablePkts_Type()
)
ccWlanRxUndecryptablePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxUndecryptablePkts.setStatus("current")
_CcWlanLastActivity_Type = TimeTicks
_CcWlanLastActivity_Object = MibTableColumn
ccWlanLastActivity = _CcWlanLastActivity_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 1, 1, 8),
    _CcWlanLastActivity_Type()
)
ccWlanLastActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanLastActivity.setStatus("current")
_CcWlanRxPktsTable_Object = MibTable
ccWlanRxPktsTable = _CcWlanRxPktsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 2)
)
if mibBuilder.loadTexts:
    ccWlanRxPktsTable.setStatus("current")
_CcWlanRxPktsEntry_Object = MibTableRow
ccWlanRxPktsEntry = _CcWlanRxPktsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 2, 1)
)
ccWlanRxPktsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWlanIndex"),
)
if mibBuilder.loadTexts:
    ccWlanRxPktsEntry.setStatus("current")
_CcWlanRxPktsAt1Mb_Type = Counter32
_CcWlanRxPktsAt1Mb_Object = MibTableColumn
ccWlanRxPktsAt1Mb = _CcWlanRxPktsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 2, 1, 1),
    _CcWlanRxPktsAt1Mb_Type()
)
ccWlanRxPktsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxPktsAt1Mb.setStatus("current")
_CcWlanRxPktsAt2Mb_Type = Counter32
_CcWlanRxPktsAt2Mb_Object = MibTableColumn
ccWlanRxPktsAt2Mb = _CcWlanRxPktsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 2, 1, 2),
    _CcWlanRxPktsAt2Mb_Type()
)
ccWlanRxPktsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxPktsAt2Mb.setStatus("current")
_CcWlanRxPktsAt5pt5Mb_Type = Counter32
_CcWlanRxPktsAt5pt5Mb_Object = MibTableColumn
ccWlanRxPktsAt5pt5Mb = _CcWlanRxPktsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 2, 1, 3),
    _CcWlanRxPktsAt5pt5Mb_Type()
)
ccWlanRxPktsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxPktsAt5pt5Mb.setStatus("current")
_CcWlanRxPktsAt6Mb_Type = Counter32
_CcWlanRxPktsAt6Mb_Object = MibTableColumn
ccWlanRxPktsAt6Mb = _CcWlanRxPktsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 2, 1, 4),
    _CcWlanRxPktsAt6Mb_Type()
)
ccWlanRxPktsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxPktsAt6Mb.setStatus("current")
_CcWlanRxPktsAt9Mb_Type = Counter32
_CcWlanRxPktsAt9Mb_Object = MibTableColumn
ccWlanRxPktsAt9Mb = _CcWlanRxPktsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 2, 1, 5),
    _CcWlanRxPktsAt9Mb_Type()
)
ccWlanRxPktsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxPktsAt9Mb.setStatus("current")
_CcWlanRxPktsAt11Mb_Type = Counter32
_CcWlanRxPktsAt11Mb_Object = MibTableColumn
ccWlanRxPktsAt11Mb = _CcWlanRxPktsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 2, 1, 6),
    _CcWlanRxPktsAt11Mb_Type()
)
ccWlanRxPktsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxPktsAt11Mb.setStatus("current")
_CcWlanRxPktsAt12Mb_Type = Counter32
_CcWlanRxPktsAt12Mb_Object = MibTableColumn
ccWlanRxPktsAt12Mb = _CcWlanRxPktsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 2, 1, 7),
    _CcWlanRxPktsAt12Mb_Type()
)
ccWlanRxPktsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxPktsAt12Mb.setStatus("current")
_CcWlanRxPktsAt18Mb_Type = Counter32
_CcWlanRxPktsAt18Mb_Object = MibTableColumn
ccWlanRxPktsAt18Mb = _CcWlanRxPktsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 2, 1, 8),
    _CcWlanRxPktsAt18Mb_Type()
)
ccWlanRxPktsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxPktsAt18Mb.setStatus("current")
_CcWlanRxPktsAt22Mb_Type = Counter32
_CcWlanRxPktsAt22Mb_Object = MibTableColumn
ccWlanRxPktsAt22Mb = _CcWlanRxPktsAt22Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 2, 1, 9),
    _CcWlanRxPktsAt22Mb_Type()
)
ccWlanRxPktsAt22Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxPktsAt22Mb.setStatus("current")
_CcWlanRxPktsAt24Mb_Type = Counter32
_CcWlanRxPktsAt24Mb_Object = MibTableColumn
ccWlanRxPktsAt24Mb = _CcWlanRxPktsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 2, 1, 10),
    _CcWlanRxPktsAt24Mb_Type()
)
ccWlanRxPktsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxPktsAt24Mb.setStatus("current")
_CcWlanRxPktsAt36Mb_Type = Counter32
_CcWlanRxPktsAt36Mb_Object = MibTableColumn
ccWlanRxPktsAt36Mb = _CcWlanRxPktsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 2, 1, 11),
    _CcWlanRxPktsAt36Mb_Type()
)
ccWlanRxPktsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxPktsAt36Mb.setStatus("current")
_CcWlanRxPktsAt48Mb_Type = Counter32
_CcWlanRxPktsAt48Mb_Object = MibTableColumn
ccWlanRxPktsAt48Mb = _CcWlanRxPktsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 2, 1, 12),
    _CcWlanRxPktsAt48Mb_Type()
)
ccWlanRxPktsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxPktsAt48Mb.setStatus("current")
_CcWlanRxPktsAt54Mb_Type = Counter32
_CcWlanRxPktsAt54Mb_Object = MibTableColumn
ccWlanRxPktsAt54Mb = _CcWlanRxPktsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 2, 1, 13),
    _CcWlanRxPktsAt54Mb_Type()
)
ccWlanRxPktsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxPktsAt54Mb.setStatus("current")
_CcWlanTxPktsTable_Object = MibTable
ccWlanTxPktsTable = _CcWlanTxPktsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 3)
)
if mibBuilder.loadTexts:
    ccWlanTxPktsTable.setStatus("current")
_CcWlanTxPktsEntry_Object = MibTableRow
ccWlanTxPktsEntry = _CcWlanTxPktsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 3, 1)
)
ccWlanTxPktsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWlanIndex"),
)
if mibBuilder.loadTexts:
    ccWlanTxPktsEntry.setStatus("current")
_CcWlanTxPktsAt1Mb_Type = Counter32
_CcWlanTxPktsAt1Mb_Object = MibTableColumn
ccWlanTxPktsAt1Mb = _CcWlanTxPktsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 3, 1, 1),
    _CcWlanTxPktsAt1Mb_Type()
)
ccWlanTxPktsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxPktsAt1Mb.setStatus("current")
_CcWlanTxPktsAt2Mb_Type = Counter32
_CcWlanTxPktsAt2Mb_Object = MibTableColumn
ccWlanTxPktsAt2Mb = _CcWlanTxPktsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 3, 1, 2),
    _CcWlanTxPktsAt2Mb_Type()
)
ccWlanTxPktsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxPktsAt2Mb.setStatus("current")
_CcWlanTxPktsAt5pt5Mb_Type = Counter32
_CcWlanTxPktsAt5pt5Mb_Object = MibTableColumn
ccWlanTxPktsAt5pt5Mb = _CcWlanTxPktsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 3, 1, 3),
    _CcWlanTxPktsAt5pt5Mb_Type()
)
ccWlanTxPktsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxPktsAt5pt5Mb.setStatus("current")
_CcWlanTxPktsAt6Mb_Type = Counter32
_CcWlanTxPktsAt6Mb_Object = MibTableColumn
ccWlanTxPktsAt6Mb = _CcWlanTxPktsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 3, 1, 4),
    _CcWlanTxPktsAt6Mb_Type()
)
ccWlanTxPktsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxPktsAt6Mb.setStatus("current")
_CcWlanTxPktsAt9Mb_Type = Counter32
_CcWlanTxPktsAt9Mb_Object = MibTableColumn
ccWlanTxPktsAt9Mb = _CcWlanTxPktsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 3, 1, 5),
    _CcWlanTxPktsAt9Mb_Type()
)
ccWlanTxPktsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxPktsAt9Mb.setStatus("current")
_CcWlanTxPktsAt11Mb_Type = Counter32
_CcWlanTxPktsAt11Mb_Object = MibTableColumn
ccWlanTxPktsAt11Mb = _CcWlanTxPktsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 3, 1, 6),
    _CcWlanTxPktsAt11Mb_Type()
)
ccWlanTxPktsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxPktsAt11Mb.setStatus("current")
_CcWlanTxPktsAt12Mb_Type = Counter32
_CcWlanTxPktsAt12Mb_Object = MibTableColumn
ccWlanTxPktsAt12Mb = _CcWlanTxPktsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 3, 1, 7),
    _CcWlanTxPktsAt12Mb_Type()
)
ccWlanTxPktsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxPktsAt12Mb.setStatus("current")
_CcWlanTxPktsAt18Mb_Type = Counter32
_CcWlanTxPktsAt18Mb_Object = MibTableColumn
ccWlanTxPktsAt18Mb = _CcWlanTxPktsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 3, 1, 8),
    _CcWlanTxPktsAt18Mb_Type()
)
ccWlanTxPktsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxPktsAt18Mb.setStatus("current")
_CcWlanTxPktsAt22Mb_Type = Counter32
_CcWlanTxPktsAt22Mb_Object = MibTableColumn
ccWlanTxPktsAt22Mb = _CcWlanTxPktsAt22Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 3, 1, 9),
    _CcWlanTxPktsAt22Mb_Type()
)
ccWlanTxPktsAt22Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxPktsAt22Mb.setStatus("current")
_CcWlanTxPktsAt24Mb_Type = Counter32
_CcWlanTxPktsAt24Mb_Object = MibTableColumn
ccWlanTxPktsAt24Mb = _CcWlanTxPktsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 3, 1, 10),
    _CcWlanTxPktsAt24Mb_Type()
)
ccWlanTxPktsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxPktsAt24Mb.setStatus("current")
_CcWlanTxPktsAt36Mb_Type = Counter32
_CcWlanTxPktsAt36Mb_Object = MibTableColumn
ccWlanTxPktsAt36Mb = _CcWlanTxPktsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 3, 1, 11),
    _CcWlanTxPktsAt36Mb_Type()
)
ccWlanTxPktsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxPktsAt36Mb.setStatus("current")
_CcWlanTxPktsAt48Mb_Type = Counter32
_CcWlanTxPktsAt48Mb_Object = MibTableColumn
ccWlanTxPktsAt48Mb = _CcWlanTxPktsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 3, 1, 12),
    _CcWlanTxPktsAt48Mb_Type()
)
ccWlanTxPktsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxPktsAt48Mb.setStatus("current")
_CcWlanTxPktsAt54Mb_Type = Counter32
_CcWlanTxPktsAt54Mb_Object = MibTableColumn
ccWlanTxPktsAt54Mb = _CcWlanTxPktsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 3, 1, 13),
    _CcWlanTxPktsAt54Mb_Type()
)
ccWlanTxPktsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxPktsAt54Mb.setStatus("current")
_CcWlanRxOctetsTable_Object = MibTable
ccWlanRxOctetsTable = _CcWlanRxOctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 4)
)
if mibBuilder.loadTexts:
    ccWlanRxOctetsTable.setStatus("current")
_CcWlanRxOctetsEntry_Object = MibTableRow
ccWlanRxOctetsEntry = _CcWlanRxOctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 4, 1)
)
ccWlanRxOctetsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWlanIndex"),
)
if mibBuilder.loadTexts:
    ccWlanRxOctetsEntry.setStatus("current")
_CcWlanRxOctetsAt1Mb_Type = Counter32
_CcWlanRxOctetsAt1Mb_Object = MibTableColumn
ccWlanRxOctetsAt1Mb = _CcWlanRxOctetsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 4, 1, 1),
    _CcWlanRxOctetsAt1Mb_Type()
)
ccWlanRxOctetsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxOctetsAt1Mb.setStatus("current")
_CcWlanRxOctetsAt2Mb_Type = Counter32
_CcWlanRxOctetsAt2Mb_Object = MibTableColumn
ccWlanRxOctetsAt2Mb = _CcWlanRxOctetsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 4, 1, 2),
    _CcWlanRxOctetsAt2Mb_Type()
)
ccWlanRxOctetsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxOctetsAt2Mb.setStatus("current")
_CcWlanRxOctetsAt5pt5Mb_Type = Counter32
_CcWlanRxOctetsAt5pt5Mb_Object = MibTableColumn
ccWlanRxOctetsAt5pt5Mb = _CcWlanRxOctetsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 4, 1, 3),
    _CcWlanRxOctetsAt5pt5Mb_Type()
)
ccWlanRxOctetsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxOctetsAt5pt5Mb.setStatus("current")
_CcWlanRxOctetsAt6Mb_Type = Counter32
_CcWlanRxOctetsAt6Mb_Object = MibTableColumn
ccWlanRxOctetsAt6Mb = _CcWlanRxOctetsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 4, 1, 4),
    _CcWlanRxOctetsAt6Mb_Type()
)
ccWlanRxOctetsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxOctetsAt6Mb.setStatus("current")
_CcWlanRxOctetsAt9Mb_Type = Counter32
_CcWlanRxOctetsAt9Mb_Object = MibTableColumn
ccWlanRxOctetsAt9Mb = _CcWlanRxOctetsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 4, 1, 5),
    _CcWlanRxOctetsAt9Mb_Type()
)
ccWlanRxOctetsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxOctetsAt9Mb.setStatus("current")
_CcWlanRxOctetsAt11Mb_Type = Counter32
_CcWlanRxOctetsAt11Mb_Object = MibTableColumn
ccWlanRxOctetsAt11Mb = _CcWlanRxOctetsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 4, 1, 6),
    _CcWlanRxOctetsAt11Mb_Type()
)
ccWlanRxOctetsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxOctetsAt11Mb.setStatus("current")
_CcWlanRxOctetsAt12Mb_Type = Counter32
_CcWlanRxOctetsAt12Mb_Object = MibTableColumn
ccWlanRxOctetsAt12Mb = _CcWlanRxOctetsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 4, 1, 7),
    _CcWlanRxOctetsAt12Mb_Type()
)
ccWlanRxOctetsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxOctetsAt12Mb.setStatus("current")
_CcWlanRxOctetsAt18Mb_Type = Counter32
_CcWlanRxOctetsAt18Mb_Object = MibTableColumn
ccWlanRxOctetsAt18Mb = _CcWlanRxOctetsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 4, 1, 8),
    _CcWlanRxOctetsAt18Mb_Type()
)
ccWlanRxOctetsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxOctetsAt18Mb.setStatus("current")
_CcWlanRxOctetsAt22Mb_Type = Counter32
_CcWlanRxOctetsAt22Mb_Object = MibTableColumn
ccWlanRxOctetsAt22Mb = _CcWlanRxOctetsAt22Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 4, 1, 9),
    _CcWlanRxOctetsAt22Mb_Type()
)
ccWlanRxOctetsAt22Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxOctetsAt22Mb.setStatus("current")
_CcWlanRxOctetsAt24Mb_Type = Counter32
_CcWlanRxOctetsAt24Mb_Object = MibTableColumn
ccWlanRxOctetsAt24Mb = _CcWlanRxOctetsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 4, 1, 10),
    _CcWlanRxOctetsAt24Mb_Type()
)
ccWlanRxOctetsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxOctetsAt24Mb.setStatus("current")
_CcWlanRxOctetsAt36Mb_Type = Counter32
_CcWlanRxOctetsAt36Mb_Object = MibTableColumn
ccWlanRxOctetsAt36Mb = _CcWlanRxOctetsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 4, 1, 11),
    _CcWlanRxOctetsAt36Mb_Type()
)
ccWlanRxOctetsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxOctetsAt36Mb.setStatus("current")
_CcWlanRxOctetsAt48Mb_Type = Counter32
_CcWlanRxOctetsAt48Mb_Object = MibTableColumn
ccWlanRxOctetsAt48Mb = _CcWlanRxOctetsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 4, 1, 12),
    _CcWlanRxOctetsAt48Mb_Type()
)
ccWlanRxOctetsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxOctetsAt48Mb.setStatus("current")
_CcWlanRxOctetsAt54Mb_Type = Counter32
_CcWlanRxOctetsAt54Mb_Object = MibTableColumn
ccWlanRxOctetsAt54Mb = _CcWlanRxOctetsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 4, 1, 13),
    _CcWlanRxOctetsAt54Mb_Type()
)
ccWlanRxOctetsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanRxOctetsAt54Mb.setStatus("current")
_CcWlanTxOctetsTable_Object = MibTable
ccWlanTxOctetsTable = _CcWlanTxOctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 5)
)
if mibBuilder.loadTexts:
    ccWlanTxOctetsTable.setStatus("current")
_CcWlanTxOctetsEntry_Object = MibTableRow
ccWlanTxOctetsEntry = _CcWlanTxOctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 5, 1)
)
ccWlanTxOctetsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWlanIndex"),
)
if mibBuilder.loadTexts:
    ccWlanTxOctetsEntry.setStatus("current")
_CcWlanTxOctetsAt1Mb_Type = Counter32
_CcWlanTxOctetsAt1Mb_Object = MibTableColumn
ccWlanTxOctetsAt1Mb = _CcWlanTxOctetsAt1Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 5, 1, 1),
    _CcWlanTxOctetsAt1Mb_Type()
)
ccWlanTxOctetsAt1Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxOctetsAt1Mb.setStatus("current")
_CcWlanTxOctetsAt2Mb_Type = Counter32
_CcWlanTxOctetsAt2Mb_Object = MibTableColumn
ccWlanTxOctetsAt2Mb = _CcWlanTxOctetsAt2Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 5, 1, 2),
    _CcWlanTxOctetsAt2Mb_Type()
)
ccWlanTxOctetsAt2Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxOctetsAt2Mb.setStatus("current")
_CcWlanTxOctetsAt5pt5Mb_Type = Counter32
_CcWlanTxOctetsAt5pt5Mb_Object = MibTableColumn
ccWlanTxOctetsAt5pt5Mb = _CcWlanTxOctetsAt5pt5Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 5, 1, 3),
    _CcWlanTxOctetsAt5pt5Mb_Type()
)
ccWlanTxOctetsAt5pt5Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxOctetsAt5pt5Mb.setStatus("current")
_CcWlanTxOctetsAt6Mb_Type = Counter32
_CcWlanTxOctetsAt6Mb_Object = MibTableColumn
ccWlanTxOctetsAt6Mb = _CcWlanTxOctetsAt6Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 5, 1, 4),
    _CcWlanTxOctetsAt6Mb_Type()
)
ccWlanTxOctetsAt6Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxOctetsAt6Mb.setStatus("current")
_CcWlanTxOctetsAt9Mb_Type = Counter32
_CcWlanTxOctetsAt9Mb_Object = MibTableColumn
ccWlanTxOctetsAt9Mb = _CcWlanTxOctetsAt9Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 5, 1, 5),
    _CcWlanTxOctetsAt9Mb_Type()
)
ccWlanTxOctetsAt9Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxOctetsAt9Mb.setStatus("current")
_CcWlanTxOctetsAt11Mb_Type = Counter32
_CcWlanTxOctetsAt11Mb_Object = MibTableColumn
ccWlanTxOctetsAt11Mb = _CcWlanTxOctetsAt11Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 5, 1, 6),
    _CcWlanTxOctetsAt11Mb_Type()
)
ccWlanTxOctetsAt11Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxOctetsAt11Mb.setStatus("current")
_CcWlanTxOctetsAt12Mb_Type = Counter32
_CcWlanTxOctetsAt12Mb_Object = MibTableColumn
ccWlanTxOctetsAt12Mb = _CcWlanTxOctetsAt12Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 5, 1, 7),
    _CcWlanTxOctetsAt12Mb_Type()
)
ccWlanTxOctetsAt12Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxOctetsAt12Mb.setStatus("current")
_CcWlanTxOctetsAt18Mb_Type = Counter32
_CcWlanTxOctetsAt18Mb_Object = MibTableColumn
ccWlanTxOctetsAt18Mb = _CcWlanTxOctetsAt18Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 5, 1, 8),
    _CcWlanTxOctetsAt18Mb_Type()
)
ccWlanTxOctetsAt18Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxOctetsAt18Mb.setStatus("current")
_CcWlanTxOctetsAt22Mb_Type = Counter32
_CcWlanTxOctetsAt22Mb_Object = MibTableColumn
ccWlanTxOctetsAt22Mb = _CcWlanTxOctetsAt22Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 5, 1, 9),
    _CcWlanTxOctetsAt22Mb_Type()
)
ccWlanTxOctetsAt22Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxOctetsAt22Mb.setStatus("current")
_CcWlanTxOctetsAt24Mb_Type = Counter32
_CcWlanTxOctetsAt24Mb_Object = MibTableColumn
ccWlanTxOctetsAt24Mb = _CcWlanTxOctetsAt24Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 5, 1, 10),
    _CcWlanTxOctetsAt24Mb_Type()
)
ccWlanTxOctetsAt24Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxOctetsAt24Mb.setStatus("current")
_CcWlanTxOctetsAt36Mb_Type = Counter32
_CcWlanTxOctetsAt36Mb_Object = MibTableColumn
ccWlanTxOctetsAt36Mb = _CcWlanTxOctetsAt36Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 5, 1, 11),
    _CcWlanTxOctetsAt36Mb_Type()
)
ccWlanTxOctetsAt36Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxOctetsAt36Mb.setStatus("current")
_CcWlanTxOctetsAt48Mb_Type = Counter32
_CcWlanTxOctetsAt48Mb_Object = MibTableColumn
ccWlanTxOctetsAt48Mb = _CcWlanTxOctetsAt48Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 5, 1, 12),
    _CcWlanTxOctetsAt48Mb_Type()
)
ccWlanTxOctetsAt48Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxOctetsAt48Mb.setStatus("current")
_CcWlanTxOctetsAt54Mb_Type = Counter32
_CcWlanTxOctetsAt54Mb_Object = MibTableColumn
ccWlanTxOctetsAt54Mb = _CcWlanTxOctetsAt54Mb_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 5, 1, 13),
    _CcWlanTxOctetsAt54Mb_Type()
)
ccWlanTxOctetsAt54Mb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxOctetsAt54Mb.setStatus("current")
_CcWlanTxRetriesPktsTable_Object = MibTable
ccWlanTxRetriesPktsTable = _CcWlanTxRetriesPktsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 6)
)
if mibBuilder.loadTexts:
    ccWlanTxRetriesPktsTable.setStatus("current")
_CcWlanTxRetriesPktsEntry_Object = MibTableRow
ccWlanTxRetriesPktsEntry = _CcWlanTxRetriesPktsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 6, 1)
)
ccWlanTxRetriesPktsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWlanIndex"),
)
if mibBuilder.loadTexts:
    ccWlanTxRetriesPktsEntry.setStatus("current")
_CcWlanTxRetriesPktsNone_Type = Counter32
_CcWlanTxRetriesPktsNone_Object = MibTableColumn
ccWlanTxRetriesPktsNone = _CcWlanTxRetriesPktsNone_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 6, 1, 1),
    _CcWlanTxRetriesPktsNone_Type()
)
ccWlanTxRetriesPktsNone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesPktsNone.setStatus("current")
_CcWlanTxRetriesPkts01_Type = Counter32
_CcWlanTxRetriesPkts01_Object = MibTableColumn
ccWlanTxRetriesPkts01 = _CcWlanTxRetriesPkts01_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 6, 1, 2),
    _CcWlanTxRetriesPkts01_Type()
)
ccWlanTxRetriesPkts01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesPkts01.setStatus("current")
_CcWlanTxRetriesPkts02_Type = Counter32
_CcWlanTxRetriesPkts02_Object = MibTableColumn
ccWlanTxRetriesPkts02 = _CcWlanTxRetriesPkts02_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 6, 1, 3),
    _CcWlanTxRetriesPkts02_Type()
)
ccWlanTxRetriesPkts02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesPkts02.setStatus("current")
_CcWlanTxRetriesPkts03_Type = Counter32
_CcWlanTxRetriesPkts03_Object = MibTableColumn
ccWlanTxRetriesPkts03 = _CcWlanTxRetriesPkts03_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 6, 1, 4),
    _CcWlanTxRetriesPkts03_Type()
)
ccWlanTxRetriesPkts03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesPkts03.setStatus("current")
_CcWlanTxRetriesPkts04_Type = Counter32
_CcWlanTxRetriesPkts04_Object = MibTableColumn
ccWlanTxRetriesPkts04 = _CcWlanTxRetriesPkts04_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 6, 1, 5),
    _CcWlanTxRetriesPkts04_Type()
)
ccWlanTxRetriesPkts04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesPkts04.setStatus("current")
_CcWlanTxRetriesPkts05_Type = Counter32
_CcWlanTxRetriesPkts05_Object = MibTableColumn
ccWlanTxRetriesPkts05 = _CcWlanTxRetriesPkts05_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 6, 1, 6),
    _CcWlanTxRetriesPkts05_Type()
)
ccWlanTxRetriesPkts05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesPkts05.setStatus("current")
_CcWlanTxRetriesPkts06_Type = Counter32
_CcWlanTxRetriesPkts06_Object = MibTableColumn
ccWlanTxRetriesPkts06 = _CcWlanTxRetriesPkts06_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 6, 1, 7),
    _CcWlanTxRetriesPkts06_Type()
)
ccWlanTxRetriesPkts06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesPkts06.setStatus("current")
_CcWlanTxRetriesPkts07_Type = Counter32
_CcWlanTxRetriesPkts07_Object = MibTableColumn
ccWlanTxRetriesPkts07 = _CcWlanTxRetriesPkts07_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 6, 1, 8),
    _CcWlanTxRetriesPkts07_Type()
)
ccWlanTxRetriesPkts07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesPkts07.setStatus("current")
_CcWlanTxRetriesPkts08_Type = Counter32
_CcWlanTxRetriesPkts08_Object = MibTableColumn
ccWlanTxRetriesPkts08 = _CcWlanTxRetriesPkts08_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 6, 1, 9),
    _CcWlanTxRetriesPkts08_Type()
)
ccWlanTxRetriesPkts08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesPkts08.setStatus("current")
_CcWlanTxRetriesPkts09_Type = Counter32
_CcWlanTxRetriesPkts09_Object = MibTableColumn
ccWlanTxRetriesPkts09 = _CcWlanTxRetriesPkts09_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 6, 1, 10),
    _CcWlanTxRetriesPkts09_Type()
)
ccWlanTxRetriesPkts09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesPkts09.setStatus("current")
_CcWlanTxRetriesPkts10_Type = Counter32
_CcWlanTxRetriesPkts10_Object = MibTableColumn
ccWlanTxRetriesPkts10 = _CcWlanTxRetriesPkts10_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 6, 1, 11),
    _CcWlanTxRetriesPkts10_Type()
)
ccWlanTxRetriesPkts10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesPkts10.setStatus("current")
_CcWlanTxRetriesPkts11_Type = Counter32
_CcWlanTxRetriesPkts11_Object = MibTableColumn
ccWlanTxRetriesPkts11 = _CcWlanTxRetriesPkts11_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 6, 1, 12),
    _CcWlanTxRetriesPkts11_Type()
)
ccWlanTxRetriesPkts11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesPkts11.setStatus("current")
_CcWlanTxRetriesPkts12_Type = Counter32
_CcWlanTxRetriesPkts12_Object = MibTableColumn
ccWlanTxRetriesPkts12 = _CcWlanTxRetriesPkts12_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 6, 1, 13),
    _CcWlanTxRetriesPkts12_Type()
)
ccWlanTxRetriesPkts12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesPkts12.setStatus("current")
_CcWlanTxRetriesPkts13_Type = Counter32
_CcWlanTxRetriesPkts13_Object = MibTableColumn
ccWlanTxRetriesPkts13 = _CcWlanTxRetriesPkts13_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 6, 1, 14),
    _CcWlanTxRetriesPkts13_Type()
)
ccWlanTxRetriesPkts13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesPkts13.setStatus("current")
_CcWlanTxRetriesPkts14_Type = Counter32
_CcWlanTxRetriesPkts14_Object = MibTableColumn
ccWlanTxRetriesPkts14 = _CcWlanTxRetriesPkts14_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 6, 1, 15),
    _CcWlanTxRetriesPkts14_Type()
)
ccWlanTxRetriesPkts14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesPkts14.setStatus("current")
_CcWlanTxRetriesPkts15_Type = Counter32
_CcWlanTxRetriesPkts15_Object = MibTableColumn
ccWlanTxRetriesPkts15 = _CcWlanTxRetriesPkts15_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 6, 1, 16),
    _CcWlanTxRetriesPkts15_Type()
)
ccWlanTxRetriesPkts15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesPkts15.setStatus("current")
_CcWlanTxRetriesPktsFailed_Type = Counter32
_CcWlanTxRetriesPktsFailed_Object = MibTableColumn
ccWlanTxRetriesPktsFailed = _CcWlanTxRetriesPktsFailed_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 6, 1, 17),
    _CcWlanTxRetriesPktsFailed_Type()
)
ccWlanTxRetriesPktsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesPktsFailed.setStatus("current")
_CcWlanTxRetriesOctetsTable_Object = MibTable
ccWlanTxRetriesOctetsTable = _CcWlanTxRetriesOctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 7)
)
if mibBuilder.loadTexts:
    ccWlanTxRetriesOctetsTable.setStatus("current")
_CcWlanTxRetriesOctetsEntry_Object = MibTableRow
ccWlanTxRetriesOctetsEntry = _CcWlanTxRetriesOctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 7, 1)
)
ccWlanTxRetriesOctetsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWlanIndex"),
)
if mibBuilder.loadTexts:
    ccWlanTxRetriesOctetsEntry.setStatus("current")
_CcWlanTxRetriesOctetsNone_Type = Counter32
_CcWlanTxRetriesOctetsNone_Object = MibTableColumn
ccWlanTxRetriesOctetsNone = _CcWlanTxRetriesOctetsNone_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 7, 1, 1),
    _CcWlanTxRetriesOctetsNone_Type()
)
ccWlanTxRetriesOctetsNone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesOctetsNone.setStatus("current")
_CcWlanTxRetriesOctets01_Type = Counter32
_CcWlanTxRetriesOctets01_Object = MibTableColumn
ccWlanTxRetriesOctets01 = _CcWlanTxRetriesOctets01_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 7, 1, 2),
    _CcWlanTxRetriesOctets01_Type()
)
ccWlanTxRetriesOctets01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesOctets01.setStatus("current")
_CcWlanTxRetriesOctets02_Type = Counter32
_CcWlanTxRetriesOctets02_Object = MibTableColumn
ccWlanTxRetriesOctets02 = _CcWlanTxRetriesOctets02_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 7, 1, 3),
    _CcWlanTxRetriesOctets02_Type()
)
ccWlanTxRetriesOctets02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesOctets02.setStatus("current")
_CcWlanTxRetriesOctets03_Type = Counter32
_CcWlanTxRetriesOctets03_Object = MibTableColumn
ccWlanTxRetriesOctets03 = _CcWlanTxRetriesOctets03_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 7, 1, 4),
    _CcWlanTxRetriesOctets03_Type()
)
ccWlanTxRetriesOctets03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesOctets03.setStatus("current")
_CcWlanTxRetriesOctets04_Type = Counter32
_CcWlanTxRetriesOctets04_Object = MibTableColumn
ccWlanTxRetriesOctets04 = _CcWlanTxRetriesOctets04_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 7, 1, 5),
    _CcWlanTxRetriesOctets04_Type()
)
ccWlanTxRetriesOctets04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesOctets04.setStatus("current")
_CcWlanTxRetriesOctets05_Type = Counter32
_CcWlanTxRetriesOctets05_Object = MibTableColumn
ccWlanTxRetriesOctets05 = _CcWlanTxRetriesOctets05_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 7, 1, 6),
    _CcWlanTxRetriesOctets05_Type()
)
ccWlanTxRetriesOctets05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesOctets05.setStatus("current")
_CcWlanTxRetriesOctets06_Type = Counter32
_CcWlanTxRetriesOctets06_Object = MibTableColumn
ccWlanTxRetriesOctets06 = _CcWlanTxRetriesOctets06_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 7, 1, 7),
    _CcWlanTxRetriesOctets06_Type()
)
ccWlanTxRetriesOctets06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesOctets06.setStatus("current")
_CcWlanTxRetriesOctets07_Type = Counter32
_CcWlanTxRetriesOctets07_Object = MibTableColumn
ccWlanTxRetriesOctets07 = _CcWlanTxRetriesOctets07_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 7, 1, 8),
    _CcWlanTxRetriesOctets07_Type()
)
ccWlanTxRetriesOctets07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesOctets07.setStatus("current")
_CcWlanTxRetriesOctets08_Type = Counter32
_CcWlanTxRetriesOctets08_Object = MibTableColumn
ccWlanTxRetriesOctets08 = _CcWlanTxRetriesOctets08_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 7, 1, 9),
    _CcWlanTxRetriesOctets08_Type()
)
ccWlanTxRetriesOctets08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesOctets08.setStatus("current")
_CcWlanTxRetriesOctets09_Type = Counter32
_CcWlanTxRetriesOctets09_Object = MibTableColumn
ccWlanTxRetriesOctets09 = _CcWlanTxRetriesOctets09_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 7, 1, 10),
    _CcWlanTxRetriesOctets09_Type()
)
ccWlanTxRetriesOctets09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesOctets09.setStatus("current")
_CcWlanTxRetriesOctets10_Type = Counter32
_CcWlanTxRetriesOctets10_Object = MibTableColumn
ccWlanTxRetriesOctets10 = _CcWlanTxRetriesOctets10_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 7, 1, 11),
    _CcWlanTxRetriesOctets10_Type()
)
ccWlanTxRetriesOctets10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesOctets10.setStatus("current")
_CcWlanTxRetriesOctets11_Type = Counter32
_CcWlanTxRetriesOctets11_Object = MibTableColumn
ccWlanTxRetriesOctets11 = _CcWlanTxRetriesOctets11_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 7, 1, 12),
    _CcWlanTxRetriesOctets11_Type()
)
ccWlanTxRetriesOctets11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesOctets11.setStatus("current")
_CcWlanTxRetriesOctets12_Type = Counter32
_CcWlanTxRetriesOctets12_Object = MibTableColumn
ccWlanTxRetriesOctets12 = _CcWlanTxRetriesOctets12_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 7, 1, 13),
    _CcWlanTxRetriesOctets12_Type()
)
ccWlanTxRetriesOctets12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesOctets12.setStatus("current")
_CcWlanTxRetriesOctets13_Type = Counter32
_CcWlanTxRetriesOctets13_Object = MibTableColumn
ccWlanTxRetriesOctets13 = _CcWlanTxRetriesOctets13_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 7, 1, 14),
    _CcWlanTxRetriesOctets13_Type()
)
ccWlanTxRetriesOctets13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesOctets13.setStatus("current")
_CcWlanTxRetriesOctets14_Type = Counter32
_CcWlanTxRetriesOctets14_Object = MibTableColumn
ccWlanTxRetriesOctets14 = _CcWlanTxRetriesOctets14_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 7, 1, 15),
    _CcWlanTxRetriesOctets14_Type()
)
ccWlanTxRetriesOctets14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesOctets14.setStatus("current")
_CcWlanTxRetriesOctets15_Type = Counter32
_CcWlanTxRetriesOctets15_Object = MibTableColumn
ccWlanTxRetriesOctets15 = _CcWlanTxRetriesOctets15_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 7, 1, 16),
    _CcWlanTxRetriesOctets15_Type()
)
ccWlanTxRetriesOctets15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesOctets15.setStatus("current")
_CcWlanTxRetriesOctetsFailed_Type = Counter32
_CcWlanTxRetriesOctetsFailed_Object = MibTableColumn
ccWlanTxRetriesOctetsFailed = _CcWlanTxRetriesOctetsFailed_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 7, 1, 17),
    _CcWlanTxRetriesOctetsFailed_Type()
)
ccWlanTxRetriesOctetsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanTxRetriesOctetsFailed.setStatus("current")
_CcWlanSigStatsTable_Object = MibTable
ccWlanSigStatsTable = _CcWlanSigStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 8)
)
if mibBuilder.loadTexts:
    ccWlanSigStatsTable.setStatus("current")
_CcWlanSigStatsEntry_Object = MibTableRow
ccWlanSigStatsEntry = _CcWlanSigStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 8, 1)
)
ccWlanSigStatsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWlanIndex"),
)
if mibBuilder.loadTexts:
    ccWlanSigStatsEntry.setStatus("current")
_CcWlanSigStatsNumPkts_Type = Counter32
_CcWlanSigStatsNumPkts_Object = MibTableColumn
ccWlanSigStatsNumPkts = _CcWlanSigStatsNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 8, 1, 1),
    _CcWlanSigStatsNumPkts_Type()
)
ccWlanSigStatsNumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSigStatsNumPkts.setStatus("current")
_CcWlanSigStatsSignalBest_Type = Integer32
_CcWlanSigStatsSignalBest_Object = MibTableColumn
ccWlanSigStatsSignalBest = _CcWlanSigStatsSignalBest_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 8, 1, 2),
    _CcWlanSigStatsSignalBest_Type()
)
ccWlanSigStatsSignalBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSigStatsSignalBest.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSigStatsSignalBest.setUnits("dBm")
_CcWlanSigStatsSignalWorst_Type = Integer32
_CcWlanSigStatsSignalWorst_Object = MibTableColumn
ccWlanSigStatsSignalWorst = _CcWlanSigStatsSignalWorst_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 8, 1, 3),
    _CcWlanSigStatsSignalWorst_Type()
)
ccWlanSigStatsSignalWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSigStatsSignalWorst.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSigStatsSignalWorst.setUnits("dBm")
_CcWlanSigStatsSignalSum_Type = Integer32
_CcWlanSigStatsSignalSum_Object = MibTableColumn
ccWlanSigStatsSignalSum = _CcWlanSigStatsSignalSum_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 8, 1, 4),
    _CcWlanSigStatsSignalSum_Type()
)
ccWlanSigStatsSignalSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSigStatsSignalSum.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSigStatsSignalSum.setUnits("dBm")
_CcWlanSigStatsSignalSumSquares_Type = Counter64
_CcWlanSigStatsSignalSumSquares_Object = MibTableColumn
ccWlanSigStatsSignalSumSquares = _CcWlanSigStatsSignalSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 8, 1, 5),
    _CcWlanSigStatsSignalSumSquares_Type()
)
ccWlanSigStatsSignalSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSigStatsSignalSumSquares.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSigStatsSignalSumSquares.setUnits("dBm")
_CcWlanSigStatsNoiseBest_Type = Integer32
_CcWlanSigStatsNoiseBest_Object = MibTableColumn
ccWlanSigStatsNoiseBest = _CcWlanSigStatsNoiseBest_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 8, 1, 6),
    _CcWlanSigStatsNoiseBest_Type()
)
ccWlanSigStatsNoiseBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSigStatsNoiseBest.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSigStatsNoiseBest.setUnits("dBm")
_CcWlanSigStatsNoiseWorst_Type = Integer32
_CcWlanSigStatsNoiseWorst_Object = MibTableColumn
ccWlanSigStatsNoiseWorst = _CcWlanSigStatsNoiseWorst_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 8, 1, 7),
    _CcWlanSigStatsNoiseWorst_Type()
)
ccWlanSigStatsNoiseWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSigStatsNoiseWorst.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSigStatsNoiseWorst.setUnits("dBm")
_CcWlanSigStatsNoiseSum_Type = Integer32
_CcWlanSigStatsNoiseSum_Object = MibTableColumn
ccWlanSigStatsNoiseSum = _CcWlanSigStatsNoiseSum_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 8, 1, 8),
    _CcWlanSigStatsNoiseSum_Type()
)
ccWlanSigStatsNoiseSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSigStatsNoiseSum.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSigStatsNoiseSum.setUnits("dBm")
_CcWlanSigStatsNoiseSumSquares_Type = Counter64
_CcWlanSigStatsNoiseSumSquares_Object = MibTableColumn
ccWlanSigStatsNoiseSumSquares = _CcWlanSigStatsNoiseSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 8, 1, 9),
    _CcWlanSigStatsNoiseSumSquares_Type()
)
ccWlanSigStatsNoiseSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSigStatsNoiseSumSquares.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSigStatsNoiseSumSquares.setUnits("dBm")
_CcWlanSigStatsSnrBest_Type = Integer32
_CcWlanSigStatsSnrBest_Object = MibTableColumn
ccWlanSigStatsSnrBest = _CcWlanSigStatsSnrBest_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 8, 1, 10),
    _CcWlanSigStatsSnrBest_Type()
)
ccWlanSigStatsSnrBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSigStatsSnrBest.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSigStatsSnrBest.setUnits("dB")
_CcWlanSigStatsSnrWorst_Type = Integer32
_CcWlanSigStatsSnrWorst_Object = MibTableColumn
ccWlanSigStatsSnrWorst = _CcWlanSigStatsSnrWorst_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 8, 1, 11),
    _CcWlanSigStatsSnrWorst_Type()
)
ccWlanSigStatsSnrWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSigStatsSnrWorst.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSigStatsSnrWorst.setUnits("dB")
_CcWlanSigStatsSnrSum_Type = Integer32
_CcWlanSigStatsSnrSum_Object = MibTableColumn
ccWlanSigStatsSnrSum = _CcWlanSigStatsSnrSum_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 8, 1, 12),
    _CcWlanSigStatsSnrSum_Type()
)
ccWlanSigStatsSnrSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSigStatsSnrSum.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSigStatsSnrSum.setUnits("dB")
_CcWlanSigStatsSnrSumSquares_Type = Counter64
_CcWlanSigStatsSnrSumSquares_Object = MibTableColumn
ccWlanSigStatsSnrSumSquares = _CcWlanSigStatsSnrSumSquares_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 8, 1, 13),
    _CcWlanSigStatsSnrSumSquares_Type()
)
ccWlanSigStatsSnrSumSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSigStatsSnrSumSquares.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSigStatsSnrSumSquares.setUnits("dB")
_CcWlanSumStatsShortTable_Object = MibTable
ccWlanSumStatsShortTable = _CcWlanSumStatsShortTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 9)
)
if mibBuilder.loadTexts:
    ccWlanSumStatsShortTable.setStatus("current")
_CcWlanSumStatsShortEntry_Object = MibTableRow
ccWlanSumStatsShortEntry = _CcWlanSumStatsShortEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 9, 1)
)
ccWlanSumStatsShortEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWlanIndex"),
)
if mibBuilder.loadTexts:
    ccWlanSumStatsShortEntry.setStatus("current")
_CcWlanSumStatsShortTimestamp_Type = TimeTicks
_CcWlanSumStatsShortTimestamp_Object = MibTableColumn
ccWlanSumStatsShortTimestamp = _CcWlanSumStatsShortTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 9, 1, 1),
    _CcWlanSumStatsShortTimestamp_Type()
)
ccWlanSumStatsShortTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortTimestamp.setStatus("current")
_CcWlanSumStatsShortNumPkts_Type = Unsigned32
_CcWlanSumStatsShortNumPkts_Object = MibTableColumn
ccWlanSumStatsShortNumPkts = _CcWlanSumStatsShortNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 9, 1, 2),
    _CcWlanSumStatsShortNumPkts_Type()
)
ccWlanSumStatsShortNumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortNumPkts.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortNumPkts.setUnits("packets")
_CcWlanSumStatsShortPktsPerSec100_Type = ScaleBy100
_CcWlanSumStatsShortPktsPerSec100_Object = MibTableColumn
ccWlanSumStatsShortPktsPerSec100 = _CcWlanSumStatsShortPktsPerSec100_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 9, 1, 3),
    _CcWlanSumStatsShortPktsPerSec100_Type()
)
ccWlanSumStatsShortPktsPerSec100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortPktsPerSec100.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortPktsPerSec100.setUnits("pkts per sec x100")
_CcWlanSumStatsShortPktsPerSecTx100_Type = ScaleBy100
_CcWlanSumStatsShortPktsPerSecTx100_Object = MibTableColumn
ccWlanSumStatsShortPktsPerSecTx100 = _CcWlanSumStatsShortPktsPerSecTx100_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 9, 1, 4),
    _CcWlanSumStatsShortPktsPerSecTx100_Type()
)
ccWlanSumStatsShortPktsPerSecTx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortPktsPerSecTx100.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortPktsPerSecTx100.setUnits("pkts per sec x100")
_CcWlanSumStatsShortPktsPerSecRx100_Type = ScaleBy100
_CcWlanSumStatsShortPktsPerSecRx100_Object = MibTableColumn
ccWlanSumStatsShortPktsPerSecRx100 = _CcWlanSumStatsShortPktsPerSecRx100_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 9, 1, 5),
    _CcWlanSumStatsShortPktsPerSecRx100_Type()
)
ccWlanSumStatsShortPktsPerSecRx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortPktsPerSecRx100.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortPktsPerSecRx100.setUnits("pkts per sec x100")
_CcWlanSumStatsShortThroughput_Type = Unsigned32
_CcWlanSumStatsShortThroughput_Object = MibTableColumn
ccWlanSumStatsShortThroughput = _CcWlanSumStatsShortThroughput_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 9, 1, 6),
    _CcWlanSumStatsShortThroughput_Type()
)
ccWlanSumStatsShortThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortThroughput.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortThroughput.setUnits("bits per second")
_CcWlanSumStatsShortThroughputTx_Type = Unsigned32
_CcWlanSumStatsShortThroughputTx_Object = MibTableColumn
ccWlanSumStatsShortThroughputTx = _CcWlanSumStatsShortThroughputTx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 9, 1, 7),
    _CcWlanSumStatsShortThroughputTx_Type()
)
ccWlanSumStatsShortThroughputTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortThroughputTx.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortThroughputTx.setUnits("bits per second")
_CcWlanSumStatsShortThroughputRx_Type = Unsigned32
_CcWlanSumStatsShortThroughputRx_Object = MibTableColumn
ccWlanSumStatsShortThroughputRx = _CcWlanSumStatsShortThroughputRx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 9, 1, 8),
    _CcWlanSumStatsShortThroughputRx_Type()
)
ccWlanSumStatsShortThroughputRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortThroughputRx.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortThroughputRx.setUnits("bits per second")
_CcWlanSumStatsShortAvgBitSpeed_Type = Unsigned32
_CcWlanSumStatsShortAvgBitSpeed_Object = MibTableColumn
ccWlanSumStatsShortAvgBitSpeed = _CcWlanSumStatsShortAvgBitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 9, 1, 9),
    _CcWlanSumStatsShortAvgBitSpeed_Type()
)
ccWlanSumStatsShortAvgBitSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortAvgBitSpeed.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortAvgBitSpeed.setUnits("bits per second")
_CcWlanSumStatsShortAvgMuSignal_Type = Integer32
_CcWlanSumStatsShortAvgMuSignal_Object = MibTableColumn
ccWlanSumStatsShortAvgMuSignal = _CcWlanSumStatsShortAvgMuSignal_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 9, 1, 10),
    _CcWlanSumStatsShortAvgMuSignal_Type()
)
ccWlanSumStatsShortAvgMuSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortAvgMuSignal.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortAvgMuSignal.setUnits("dBm")
_CcWlanSumStatsShortAvgMuNoise_Type = Integer32
_CcWlanSumStatsShortAvgMuNoise_Object = MibTableColumn
ccWlanSumStatsShortAvgMuNoise = _CcWlanSumStatsShortAvgMuNoise_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 9, 1, 11),
    _CcWlanSumStatsShortAvgMuNoise_Type()
)
ccWlanSumStatsShortAvgMuNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortAvgMuNoise.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortAvgMuNoise.setUnits("dBm")
_CcWlanSumStatsShortAvgMuSnr_Type = Integer32
_CcWlanSumStatsShortAvgMuSnr_Object = MibTableColumn
ccWlanSumStatsShortAvgMuSnr = _CcWlanSumStatsShortAvgMuSnr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 9, 1, 12),
    _CcWlanSumStatsShortAvgMuSnr_Type()
)
ccWlanSumStatsShortAvgMuSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortAvgMuSnr.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortAvgMuSnr.setUnits("dB")
_CcWlanSumStatsShortPp10kNUcastPkts_Type = PartsPer10k
_CcWlanSumStatsShortPp10kNUcastPkts_Object = MibTableColumn
ccWlanSumStatsShortPp10kNUcastPkts = _CcWlanSumStatsShortPp10kNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 9, 1, 13),
    _CcWlanSumStatsShortPp10kNUcastPkts_Type()
)
ccWlanSumStatsShortPp10kNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortPp10kNUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortPp10kNUcastPkts.setUnits("parts-per-10000")
_CcWlanSumStatsShortPp10kTxWithRetries_Type = PartsPer10k
_CcWlanSumStatsShortPp10kTxWithRetries_Object = MibTableColumn
ccWlanSumStatsShortPp10kTxWithRetries = _CcWlanSumStatsShortPp10kTxWithRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 9, 1, 14),
    _CcWlanSumStatsShortPp10kTxWithRetries_Type()
)
ccWlanSumStatsShortPp10kTxWithRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortPp10kTxWithRetries.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortPp10kTxWithRetries.setUnits("parts-per-10000")
_CcWlanSumStatsShortPp10kDropped_Type = PartsPer10k
_CcWlanSumStatsShortPp10kDropped_Object = MibTableColumn
ccWlanSumStatsShortPp10kDropped = _CcWlanSumStatsShortPp10kDropped_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 9, 1, 15),
    _CcWlanSumStatsShortPp10kDropped_Type()
)
ccWlanSumStatsShortPp10kDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortPp10kDropped.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortPp10kDropped.setUnits("parts-per-10000")
_CcWlanSumStatsShortTxAvgRetries100_Type = ScaleBy100
_CcWlanSumStatsShortTxAvgRetries100_Object = MibTableColumn
ccWlanSumStatsShortTxAvgRetries100 = _CcWlanSumStatsShortTxAvgRetries100_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 9, 1, 16),
    _CcWlanSumStatsShortTxAvgRetries100_Type()
)
ccWlanSumStatsShortTxAvgRetries100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortTxAvgRetries100.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortTxAvgRetries100.setUnits("average x100")
_CcWlanSumStatsShortPp10kRxUndecrypt_Type = PartsPer10k
_CcWlanSumStatsShortPp10kRxUndecrypt_Object = MibTableColumn
ccWlanSumStatsShortPp10kRxUndecrypt = _CcWlanSumStatsShortPp10kRxUndecrypt_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 9, 1, 17),
    _CcWlanSumStatsShortPp10kRxUndecrypt_Type()
)
ccWlanSumStatsShortPp10kRxUndecrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortPp10kRxUndecrypt.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortPp10kRxUndecrypt.setUnits("parts-per-10000")


class _CcWlanSumStatsShortTotalMus_Type(Unsigned32):
    """Custom type ccWlanSumStatsShortTotalMus based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CcWlanSumStatsShortTotalMus_Type.__name__ = "Unsigned32"
_CcWlanSumStatsShortTotalMus_Object = MibTableColumn
ccWlanSumStatsShortTotalMus = _CcWlanSumStatsShortTotalMus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 9, 1, 18),
    _CcWlanSumStatsShortTotalMus_Type()
)
ccWlanSumStatsShortTotalMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortTotalMus.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortTotalMus.setUnits("number of MUs")
_CcWlanSumStatsShortSkip1_Type = Integer32
_CcWlanSumStatsShortSkip1_Object = MibTableColumn
ccWlanSumStatsShortSkip1 = _CcWlanSumStatsShortSkip1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 9, 1, 19),
    _CcWlanSumStatsShortSkip1_Type()
)
ccWlanSumStatsShortSkip1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanSumStatsShortSkip1.setStatus("obsolete")
_CcWlanSumStatsLongTable_Object = MibTable
ccWlanSumStatsLongTable = _CcWlanSumStatsLongTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 10)
)
if mibBuilder.loadTexts:
    ccWlanSumStatsLongTable.setStatus("current")
_CcWlanSumStatsLongEntry_Object = MibTableRow
ccWlanSumStatsLongEntry = _CcWlanSumStatsLongEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 10, 1)
)
ccWlanSumStatsLongEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWlanIndex"),
)
if mibBuilder.loadTexts:
    ccWlanSumStatsLongEntry.setStatus("current")
_CcWlanSumStatsLongTimestamp_Type = TimeTicks
_CcWlanSumStatsLongTimestamp_Object = MibTableColumn
ccWlanSumStatsLongTimestamp = _CcWlanSumStatsLongTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 10, 1, 1),
    _CcWlanSumStatsLongTimestamp_Type()
)
ccWlanSumStatsLongTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongTimestamp.setStatus("current")
_CcWlanSumStatsLongNumPkts_Type = Unsigned32
_CcWlanSumStatsLongNumPkts_Object = MibTableColumn
ccWlanSumStatsLongNumPkts = _CcWlanSumStatsLongNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 10, 1, 2),
    _CcWlanSumStatsLongNumPkts_Type()
)
ccWlanSumStatsLongNumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongNumPkts.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongNumPkts.setUnits("packets")
_CcWlanSumStatsLongPktsPerSec100_Type = ScaleBy100
_CcWlanSumStatsLongPktsPerSec100_Object = MibTableColumn
ccWlanSumStatsLongPktsPerSec100 = _CcWlanSumStatsLongPktsPerSec100_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 10, 1, 3),
    _CcWlanSumStatsLongPktsPerSec100_Type()
)
ccWlanSumStatsLongPktsPerSec100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongPktsPerSec100.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongPktsPerSec100.setUnits("pkts per sec x100")
_CcWlanSumStatsLongPktsPerSecTx100_Type = ScaleBy100
_CcWlanSumStatsLongPktsPerSecTx100_Object = MibTableColumn
ccWlanSumStatsLongPktsPerSecTx100 = _CcWlanSumStatsLongPktsPerSecTx100_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 10, 1, 4),
    _CcWlanSumStatsLongPktsPerSecTx100_Type()
)
ccWlanSumStatsLongPktsPerSecTx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongPktsPerSecTx100.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongPktsPerSecTx100.setUnits("pkts per sec x100")
_CcWlanSumStatsLongPktsPerSecRx100_Type = ScaleBy100
_CcWlanSumStatsLongPktsPerSecRx100_Object = MibTableColumn
ccWlanSumStatsLongPktsPerSecRx100 = _CcWlanSumStatsLongPktsPerSecRx100_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 10, 1, 5),
    _CcWlanSumStatsLongPktsPerSecRx100_Type()
)
ccWlanSumStatsLongPktsPerSecRx100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongPktsPerSecRx100.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongPktsPerSecRx100.setUnits("pkts per sec x100")
_CcWlanSumStatsLongThroughput_Type = Unsigned32
_CcWlanSumStatsLongThroughput_Object = MibTableColumn
ccWlanSumStatsLongThroughput = _CcWlanSumStatsLongThroughput_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 10, 1, 6),
    _CcWlanSumStatsLongThroughput_Type()
)
ccWlanSumStatsLongThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongThroughput.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongThroughput.setUnits("bits per second")
_CcWlanSumStatsLongThroughputTx_Type = Unsigned32
_CcWlanSumStatsLongThroughputTx_Object = MibTableColumn
ccWlanSumStatsLongThroughputTx = _CcWlanSumStatsLongThroughputTx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 10, 1, 7),
    _CcWlanSumStatsLongThroughputTx_Type()
)
ccWlanSumStatsLongThroughputTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongThroughputTx.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongThroughputTx.setUnits("bits per second")
_CcWlanSumStatsLongThroughputRx_Type = Unsigned32
_CcWlanSumStatsLongThroughputRx_Object = MibTableColumn
ccWlanSumStatsLongThroughputRx = _CcWlanSumStatsLongThroughputRx_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 10, 1, 8),
    _CcWlanSumStatsLongThroughputRx_Type()
)
ccWlanSumStatsLongThroughputRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongThroughputRx.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongThroughputRx.setUnits("bits per second")
_CcWlanSumStatsLongAvgBitSpeed_Type = Unsigned32
_CcWlanSumStatsLongAvgBitSpeed_Object = MibTableColumn
ccWlanSumStatsLongAvgBitSpeed = _CcWlanSumStatsLongAvgBitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 10, 1, 9),
    _CcWlanSumStatsLongAvgBitSpeed_Type()
)
ccWlanSumStatsLongAvgBitSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongAvgBitSpeed.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongAvgBitSpeed.setUnits("bits per second")
_CcWlanSumStatsLongAvgMuSignal_Type = Integer32
_CcWlanSumStatsLongAvgMuSignal_Object = MibTableColumn
ccWlanSumStatsLongAvgMuSignal = _CcWlanSumStatsLongAvgMuSignal_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 10, 1, 10),
    _CcWlanSumStatsLongAvgMuSignal_Type()
)
ccWlanSumStatsLongAvgMuSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongAvgMuSignal.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongAvgMuSignal.setUnits("dBm")
_CcWlanSumStatsLongAvgMuNoise_Type = Integer32
_CcWlanSumStatsLongAvgMuNoise_Object = MibTableColumn
ccWlanSumStatsLongAvgMuNoise = _CcWlanSumStatsLongAvgMuNoise_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 10, 1, 11),
    _CcWlanSumStatsLongAvgMuNoise_Type()
)
ccWlanSumStatsLongAvgMuNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongAvgMuNoise.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongAvgMuNoise.setUnits("dBm")
_CcWlanSumStatsLongAvgMuSnr_Type = Integer32
_CcWlanSumStatsLongAvgMuSnr_Object = MibTableColumn
ccWlanSumStatsLongAvgMuSnr = _CcWlanSumStatsLongAvgMuSnr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 10, 1, 12),
    _CcWlanSumStatsLongAvgMuSnr_Type()
)
ccWlanSumStatsLongAvgMuSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongAvgMuSnr.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongAvgMuSnr.setUnits("dB")
_CcWlanSumStatsLongPp10kNUcastPkts_Type = PartsPer10k
_CcWlanSumStatsLongPp10kNUcastPkts_Object = MibTableColumn
ccWlanSumStatsLongPp10kNUcastPkts = _CcWlanSumStatsLongPp10kNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 10, 1, 13),
    _CcWlanSumStatsLongPp10kNUcastPkts_Type()
)
ccWlanSumStatsLongPp10kNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongPp10kNUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongPp10kNUcastPkts.setUnits("parts-per-10000")
_CcWlanSumStatsLongPp10kTxWithRetries_Type = PartsPer10k
_CcWlanSumStatsLongPp10kTxWithRetries_Object = MibTableColumn
ccWlanSumStatsLongPp10kTxWithRetries = _CcWlanSumStatsLongPp10kTxWithRetries_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 10, 1, 14),
    _CcWlanSumStatsLongPp10kTxWithRetries_Type()
)
ccWlanSumStatsLongPp10kTxWithRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongPp10kTxWithRetries.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongPp10kTxWithRetries.setUnits("parts-per-10000")
_CcWlanSumStatsLongPp10kDropped_Type = PartsPer10k
_CcWlanSumStatsLongPp10kDropped_Object = MibTableColumn
ccWlanSumStatsLongPp10kDropped = _CcWlanSumStatsLongPp10kDropped_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 10, 1, 15),
    _CcWlanSumStatsLongPp10kDropped_Type()
)
ccWlanSumStatsLongPp10kDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongPp10kDropped.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongPp10kDropped.setUnits("parts-per-10000")
_CcWlanSumStatsLongTxAvgRetries100_Type = ScaleBy100
_CcWlanSumStatsLongTxAvgRetries100_Object = MibTableColumn
ccWlanSumStatsLongTxAvgRetries100 = _CcWlanSumStatsLongTxAvgRetries100_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 10, 1, 16),
    _CcWlanSumStatsLongTxAvgRetries100_Type()
)
ccWlanSumStatsLongTxAvgRetries100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongTxAvgRetries100.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongTxAvgRetries100.setUnits("average x100")
_CcWlanSumStatsLongPp10kRxUndecrypt_Type = PartsPer10k
_CcWlanSumStatsLongPp10kRxUndecrypt_Object = MibTableColumn
ccWlanSumStatsLongPp10kRxUndecrypt = _CcWlanSumStatsLongPp10kRxUndecrypt_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 10, 1, 17),
    _CcWlanSumStatsLongPp10kRxUndecrypt_Type()
)
ccWlanSumStatsLongPp10kRxUndecrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongPp10kRxUndecrypt.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongPp10kRxUndecrypt.setUnits("parts-per-10000")


class _CcWlanSumStatsLongTotalMus_Type(Unsigned32):
    """Custom type ccWlanSumStatsLongTotalMus based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CcWlanSumStatsLongTotalMus_Type.__name__ = "Unsigned32"
_CcWlanSumStatsLongTotalMus_Object = MibTableColumn
ccWlanSumStatsLongTotalMus = _CcWlanSumStatsLongTotalMus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 10, 1, 18),
    _CcWlanSumStatsLongTotalMus_Type()
)
ccWlanSumStatsLongTotalMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongTotalMus.setStatus("current")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongTotalMus.setUnits("number of MUs")
_CcWlanSumStatsLongSkip1_Type = Integer32
_CcWlanSumStatsLongSkip1_Object = MibTableColumn
ccWlanSumStatsLongSkip1 = _CcWlanSumStatsLongSkip1_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 4, 5, 100, 10, 1, 19),
    _CcWlanSumStatsLongSkip1_Type()
)
ccWlanSumStatsLongSkip1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWlanSumStatsLongSkip1.setStatus("obsolete")
_CcSwitch_ObjectIdentity = ObjectIdentity
ccSwitch = _CcSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5)
)
_CcWan_ObjectIdentity = ObjectIdentity
ccWan = _CcWan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1)
)
_CcWanTable_Object = MibTable
ccWanTable = _CcWanTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    ccWanTable.setStatus("current")
_CcWanEntry_Object = MibTableRow
ccWanEntry = _CcWanEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 1, 1)
)
ccWanEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWanIndex"),
)
if mibBuilder.loadTexts:
    ccWanEntry.setStatus("current")


class _CcWanIndex_Type(Integer32):
    """Custom type ccWanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_CcWanIndex_Type.__name__ = "Integer32"
_CcWanIndex_Object = MibTableColumn
ccWanIndex = _CcWanIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 1, 1, 1),
    _CcWanIndex_Type()
)
ccWanIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccWanIndex.setStatus("current")
_CcWanDhcpEnable_Type = TruthValue
_CcWanDhcpEnable_Object = MibTableColumn
ccWanDhcpEnable = _CcWanDhcpEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 1, 1, 2),
    _CcWanDhcpEnable_Type()
)
ccWanDhcpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanDhcpEnable.setStatus("current")
_CcWanDhcpIpAddr_Type = IpAddress
_CcWanDhcpIpAddr_Object = MibTableColumn
ccWanDhcpIpAddr = _CcWanDhcpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 1, 1, 3),
    _CcWanDhcpIpAddr_Type()
)
ccWanDhcpIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWanDhcpIpAddr.setStatus("current")
_CcWanDhcpSubnetMask_Type = IpAddress
_CcWanDhcpSubnetMask_Object = MibTableColumn
ccWanDhcpSubnetMask = _CcWanDhcpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 1, 1, 4),
    _CcWanDhcpSubnetMask_Type()
)
ccWanDhcpSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWanDhcpSubnetMask.setStatus("current")
_CcWanDhcpDefaultGateway_Type = IpAddress
_CcWanDhcpDefaultGateway_Object = MibTableColumn
ccWanDhcpDefaultGateway = _CcWanDhcpDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 1, 1, 5),
    _CcWanDhcpDefaultGateway_Type()
)
ccWanDhcpDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWanDhcpDefaultGateway.setStatus("current")
_CcWanDhcpPrimaryDnsServer_Type = IpAddress
_CcWanDhcpPrimaryDnsServer_Object = MibTableColumn
ccWanDhcpPrimaryDnsServer = _CcWanDhcpPrimaryDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 1, 1, 6),
    _CcWanDhcpPrimaryDnsServer_Type()
)
ccWanDhcpPrimaryDnsServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWanDhcpPrimaryDnsServer.setStatus("current")
_CcWanDhcpSecondaryDnsServer_Type = IpAddress
_CcWanDhcpSecondaryDnsServer_Object = MibTableColumn
ccWanDhcpSecondaryDnsServer = _CcWanDhcpSecondaryDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 1, 1, 7),
    _CcWanDhcpSecondaryDnsServer_Type()
)
ccWanDhcpSecondaryDnsServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWanDhcpSecondaryDnsServer.setStatus("current")
_CcWanSubnetMask_Type = IpAddress
_CcWanSubnetMask_Object = MibTableColumn
ccWanSubnetMask = _CcWanSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 1, 1, 8),
    _CcWanSubnetMask_Type()
)
ccWanSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanSubnetMask.setStatus("current")
_CcWanDefaultGateway_Type = IpAddress
_CcWanDefaultGateway_Object = MibTableColumn
ccWanDefaultGateway = _CcWanDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 1, 1, 9),
    _CcWanDefaultGateway_Type()
)
ccWanDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanDefaultGateway.setStatus("current")
_CcWanPrimaryDnsServer_Type = IpAddress
_CcWanPrimaryDnsServer_Object = MibTableColumn
ccWanPrimaryDnsServer = _CcWanPrimaryDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 1, 1, 10),
    _CcWanPrimaryDnsServer_Type()
)
ccWanPrimaryDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanPrimaryDnsServer.setStatus("current")
_CcWanSecondaryDnsServer_Type = IpAddress
_CcWanSecondaryDnsServer_Object = MibTableColumn
ccWanSecondaryDnsServer = _CcWanSecondaryDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 1, 1, 11),
    _CcWanSecondaryDnsServer_Type()
)
ccWanSecondaryDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanSecondaryDnsServer.setStatus("current")
_CcWanPppoeTable_Object = MibTable
ccWanPppoeTable = _CcWanPppoeTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 2)
)
if mibBuilder.loadTexts:
    ccWanPppoeTable.setStatus("current")
_CcWanPppoeEntry_Object = MibTableRow
ccWanPppoeEntry = _CcWanPppoeEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 2, 1)
)
ccWanPppoeEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWanIndex"),
)
if mibBuilder.loadTexts:
    ccWanPppoeEntry.setStatus("current")
_CcWanPppoeEnable_Type = StaticRowEnable
_CcWanPppoeEnable_Object = MibTableColumn
ccWanPppoeEnable = _CcWanPppoeEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 2, 1, 1),
    _CcWanPppoeEnable_Type()
)
ccWanPppoeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanPppoeEnable.setStatus("current")
_CcWanPppoeUsername_Type = DisplayString
_CcWanPppoeUsername_Object = MibTableColumn
ccWanPppoeUsername = _CcWanPppoeUsername_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 2, 1, 2),
    _CcWanPppoeUsername_Type()
)
ccWanPppoeUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanPppoeUsername.setStatus("current")
_CcWanPppoePassword_Type = DisplayString
_CcWanPppoePassword_Object = MibTableColumn
ccWanPppoePassword = _CcWanPppoePassword_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 2, 1, 3),
    _CcWanPppoePassword_Type()
)
ccWanPppoePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanPppoePassword.setStatus("current")
_CcWanPppoeKeepAlive_Type = TruthValue
_CcWanPppoeKeepAlive_Object = MibTableColumn
ccWanPppoeKeepAlive = _CcWanPppoeKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 2, 1, 4),
    _CcWanPppoeKeepAlive_Type()
)
ccWanPppoeKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanPppoeKeepAlive.setStatus("current")
_CcWanPppoeIdleTime_Type = Unsigned32
_CcWanPppoeIdleTime_Object = MibTableColumn
ccWanPppoeIdleTime = _CcWanPppoeIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 2, 1, 5),
    _CcWanPppoeIdleTime_Type()
)
ccWanPppoeIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanPppoeIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    ccWanPppoeIdleTime.setUnits("seconds")


class _CcWanPppoeAuthType_Type(Integer32):
    """Custom type ccWanPppoeAuthType based on Integer32"""
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
        *(("chap", 4),
          ("none", 1),
          ("pap", 3),
          ("papOrChap", 2))
    )


_CcWanPppoeAuthType_Type.__name__ = "Integer32"
_CcWanPppoeAuthType_Object = MibTableColumn
ccWanPppoeAuthType = _CcWanPppoeAuthType_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 2, 1, 6),
    _CcWanPppoeAuthType_Type()
)
ccWanPppoeAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanPppoeAuthType.setStatus("current")
_CcWanIpAddrTable_Object = MibTable
ccWanIpAddrTable = _CcWanIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 3)
)
if mibBuilder.loadTexts:
    ccWanIpAddrTable.setStatus("current")
_CcWanIpAddrEntry_Object = MibTableRow
ccWanIpAddrEntry = _CcWanIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 3, 1)
)
ccWanIpAddrEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWanIndex"),
    (0, "SYMBOL-CC-WS2000-MIB", "ccWanIpAddrIndex"),
)
if mibBuilder.loadTexts:
    ccWanIpAddrEntry.setStatus("current")


class _CcWanIpAddrIndex_Type(Integer32):
    """Custom type ccWanIpAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_CcWanIpAddrIndex_Type.__name__ = "Integer32"
_CcWanIpAddrIndex_Object = MibTableColumn
ccWanIpAddrIndex = _CcWanIpAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 3, 1, 1),
    _CcWanIpAddrIndex_Type()
)
ccWanIpAddrIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccWanIpAddrIndex.setStatus("current")
_CcWanIpAddrEnable_Type = StaticRowEnable
_CcWanIpAddrEnable_Object = MibTableColumn
ccWanIpAddrEnable = _CcWanIpAddrEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 3, 1, 2),
    _CcWanIpAddrEnable_Type()
)
ccWanIpAddrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanIpAddrEnable.setStatus("current")
_CcWanIpAddr_Type = IpAddress
_CcWanIpAddr_Object = MibTableColumn
ccWanIpAddr = _CcWanIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 3, 1, 3),
    _CcWanIpAddr_Type()
)
ccWanIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanIpAddr.setStatus("current")
_CcWanFirewall_ObjectIdentity = ObjectIdentity
ccWanFirewall = _CcWanFirewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 4)
)
_CcWanFirewallGlobalEnable_Type = TruthValue
_CcWanFirewallGlobalEnable_Object = MibScalar
ccWanFirewallGlobalEnable = _CcWanFirewallGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 4, 1),
    _CcWanFirewallGlobalEnable_Type()
)
ccWanFirewallGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanFirewallGlobalEnable.setStatus("current")
_CcWanFirewallTable_Object = MibTable
ccWanFirewallTable = _CcWanFirewallTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 4, 2)
)
if mibBuilder.loadTexts:
    ccWanFirewallTable.setStatus("current")
_CcWanFirewallEntry_Object = MibTableRow
ccWanFirewallEntry = _CcWanFirewallEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 4, 2, 1)
)
ccWanFirewallEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWanIndex"),
)
if mibBuilder.loadTexts:
    ccWanFirewallEntry.setStatus("current")


class _CcWanFirewallIndex_Type(Integer32):
    """Custom type ccWanFirewallIndex based on Integer32"""
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
        *(("fwFtpBounceAttack", 8),
          ("fwIpSequenceNumberPrediction", 10),
          ("fwIpSpoofing", 1),
          ("fwIpUnalignedTimestamp", 9),
          ("fwLandAttack", 3),
          ("fwMimeFloodAttack", 11),
          ("fwPingOfDeath", 2),
          ("fwReassemblyAttack", 4),
          ("fwSourceRouting", 6),
          ("fwSynFloodAttack", 5),
          ("fwWinnukeAttack", 7))
    )


_CcWanFirewallIndex_Type.__name__ = "Integer32"
_CcWanFirewallIndex_Object = MibTableColumn
ccWanFirewallIndex = _CcWanFirewallIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 4, 2, 1, 1),
    _CcWanFirewallIndex_Type()
)
ccWanFirewallIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccWanFirewallIndex.setStatus("current")
_CcWanFirewallDescription_Type = DisplayString
_CcWanFirewallDescription_Object = MibTableColumn
ccWanFirewallDescription = _CcWanFirewallDescription_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 4, 2, 1, 2),
    _CcWanFirewallDescription_Type()
)
ccWanFirewallDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWanFirewallDescription.setStatus("current")
_CcWanFirewallAlwaysEnabled_Type = TruthValue
_CcWanFirewallAlwaysEnabled_Object = MibTableColumn
ccWanFirewallAlwaysEnabled = _CcWanFirewallAlwaysEnabled_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 4, 2, 1, 3),
    _CcWanFirewallAlwaysEnabled_Type()
)
ccWanFirewallAlwaysEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWanFirewallAlwaysEnabled.setStatus("current")
_CcWanFirewallEnable_Type = TruthValue
_CcWanFirewallEnable_Object = MibTableColumn
ccWanFirewallEnable = _CcWanFirewallEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 4, 2, 1, 4),
    _CcWanFirewallEnable_Type()
)
ccWanFirewallEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanFirewallEnable.setStatus("current")
_CcWanFirewallMimeFloodMaxHeaderLength_Type = Unsigned32
_CcWanFirewallMimeFloodMaxHeaderLength_Object = MibScalar
ccWanFirewallMimeFloodMaxHeaderLength = _CcWanFirewallMimeFloodMaxHeaderLength_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 4, 3),
    _CcWanFirewallMimeFloodMaxHeaderLength_Type()
)
ccWanFirewallMimeFloodMaxHeaderLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanFirewallMimeFloodMaxHeaderLength.setStatus("current")
if mibBuilder.loadTexts:
    ccWanFirewallMimeFloodMaxHeaderLength.setUnits("bytes")
_CcWanFirewallMimeFloodMaxHeaders_Type = Unsigned32
_CcWanFirewallMimeFloodMaxHeaders_Object = MibScalar
ccWanFirewallMimeFloodMaxHeaders = _CcWanFirewallMimeFloodMaxHeaders_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 4, 4),
    _CcWanFirewallMimeFloodMaxHeaders_Type()
)
ccWanFirewallMimeFloodMaxHeaders.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanFirewallMimeFloodMaxHeaders.setStatus("current")
_CcWanNatTimeout_Type = Unsigned32
_CcWanNatTimeout_Object = MibScalar
ccWanNatTimeout = _CcWanNatTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 4, 5),
    _CcWanNatTimeout_Type()
)
ccWanNatTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanNatTimeout.setStatus("current")
_CcWanNat_ObjectIdentity = ObjectIdentity
ccWanNat = _CcWanNat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 5)
)
_CcWanNatLowestUnusedSlot_Type = Unsigned32
_CcWanNatLowestUnusedSlot_Object = MibScalar
ccWanNatLowestUnusedSlot = _CcWanNatLowestUnusedSlot_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 5, 1),
    _CcWanNatLowestUnusedSlot_Type()
)
ccWanNatLowestUnusedSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWanNatLowestUnusedSlot.setStatus("current")
_CcWanNatTable_Object = MibTable
ccWanNatTable = _CcWanNatTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 5, 2)
)
if mibBuilder.loadTexts:
    ccWanNatTable.setStatus("current")
_CcWanNatEntry_Object = MibTableRow
ccWanNatEntry = _CcWanNatEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 5, 2, 1)
)
ccWanNatEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWanNatIndex"),
    (0, "SYMBOL-CC-WS2000-MIB", "ccWanNatWanIpAddress"),
)
if mibBuilder.loadTexts:
    ccWanNatEntry.setStatus("current")


class _CcWanNatIndex_Type(Integer32):
    """Custom type ccWanNatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_CcWanNatIndex_Type.__name__ = "Integer32"
_CcWanNatIndex_Object = MibTableColumn
ccWanNatIndex = _CcWanNatIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 5, 2, 1, 1),
    _CcWanNatIndex_Type()
)
ccWanNatIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccWanNatIndex.setStatus("current")
_CcWanNatWanIpAddress_Type = IpAddress
_CcWanNatWanIpAddress_Object = MibTableColumn
ccWanNatWanIpAddress = _CcWanNatWanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 5, 2, 1, 2),
    _CcWanNatWanIpAddress_Type()
)
ccWanNatWanIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccWanNatWanIpAddress.setStatus("current")


class _CcWanNatType_Type(Integer32):
    """Custom type ccWanNatType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nat1to1", 2),
          ("nat1toMany", 3),
          ("natNone", 1))
    )


_CcWanNatType_Type.__name__ = "Integer32"
_CcWanNatType_Object = MibTableColumn
ccWanNatType = _CcWanNatType_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 5, 2, 1, 3),
    _CcWanNatType_Type()
)
ccWanNatType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanNatType.setStatus("current")
_CcWanNat1to1IpAddr_Type = IpAddress
_CcWanNat1to1IpAddr_Object = MibTableColumn
ccWanNat1to1IpAddr = _CcWanNat1to1IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 5, 2, 1, 4),
    _CcWanNat1to1IpAddr_Type()
)
ccWanNat1to1IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanNat1to1IpAddr.setStatus("current")
_CcWanNatInboundDefaultEna_Type = TruthValue
_CcWanNatInboundDefaultEna_Object = MibTableColumn
ccWanNatInboundDefaultEna = _CcWanNatInboundDefaultEna_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 5, 2, 1, 5),
    _CcWanNatInboundDefaultEna_Type()
)
ccWanNatInboundDefaultEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanNatInboundDefaultEna.setStatus("current")
_CcWanNatInboundDefaultIp_Type = IpAddress
_CcWanNatInboundDefaultIp_Object = MibTableColumn
ccWanNatInboundDefaultIp = _CcWanNatInboundDefaultIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 5, 2, 1, 6),
    _CcWanNatInboundDefaultIp_Type()
)
ccWanNatInboundDefaultIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanNatInboundDefaultIp.setStatus("current")
_CcWanNatInboundTable_Object = MibTable
ccWanNatInboundTable = _CcWanNatInboundTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 5, 3)
)
if mibBuilder.loadTexts:
    ccWanNatInboundTable.setStatus("current")
_CcWanNatInboundEntry_Object = MibTableRow
ccWanNatInboundEntry = _CcWanNatInboundEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 5, 3, 1)
)
ccWanNatInboundEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWanNatIndex"),
    (0, "SYMBOL-CC-WS2000-MIB", "ccWanNatWanIpAddress"),
    (0, "SYMBOL-CC-WS2000-MIB", "ccWanNatInboundIndex"),
)
if mibBuilder.loadTexts:
    ccWanNatInboundEntry.setStatus("current")


class _CcWanNatInboundIndex_Type(Integer32):
    """Custom type ccWanNatInboundIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CcWanNatInboundIndex_Type.__name__ = "Integer32"
_CcWanNatInboundIndex_Object = MibTableColumn
ccWanNatInboundIndex = _CcWanNatInboundIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 5, 3, 1, 1),
    _CcWanNatInboundIndex_Type()
)
ccWanNatInboundIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccWanNatInboundIndex.setStatus("current")
_CcWanNatInboundName_Type = DisplayString
_CcWanNatInboundName_Object = MibTableColumn
ccWanNatInboundName = _CcWanNatInboundName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 5, 3, 1, 2),
    _CcWanNatInboundName_Type()
)
ccWanNatInboundName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanNatInboundName.setStatus("current")


class _CcWanNatInboundTransport_Type(Integer32):
    """Custom type ccWanNatInboundTransport based on Integer32"""
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
        *(("ah", 5),
          ("all", 1),
          ("esp", 6),
          ("gre", 7),
          ("icmp", 4),
          ("tcp", 2),
          ("udp", 3))
    )


_CcWanNatInboundTransport_Type.__name__ = "Integer32"
_CcWanNatInboundTransport_Object = MibTableColumn
ccWanNatInboundTransport = _CcWanNatInboundTransport_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 5, 3, 1, 3),
    _CcWanNatInboundTransport_Type()
)
ccWanNatInboundTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanNatInboundTransport.setStatus("current")
_CcWanNatInboundStartPort_Type = Integer32
_CcWanNatInboundStartPort_Object = MibTableColumn
ccWanNatInboundStartPort = _CcWanNatInboundStartPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 5, 3, 1, 4),
    _CcWanNatInboundStartPort_Type()
)
ccWanNatInboundStartPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanNatInboundStartPort.setStatus("current")
_CcWanNatInboundEndPort_Type = Integer32
_CcWanNatInboundEndPort_Object = MibTableColumn
ccWanNatInboundEndPort = _CcWanNatInboundEndPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 5, 3, 1, 5),
    _CcWanNatInboundEndPort_Type()
)
ccWanNatInboundEndPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanNatInboundEndPort.setStatus("current")
_CcWanNatInboundIpAddr_Type = IpAddress
_CcWanNatInboundIpAddr_Object = MibTableColumn
ccWanNatInboundIpAddr = _CcWanNatInboundIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 5, 3, 1, 6),
    _CcWanNatInboundIpAddr_Type()
)
ccWanNatInboundIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanNatInboundIpAddr.setStatus("current")
_CcWanNatInboundTranslationPort_Type = Integer32
_CcWanNatInboundTranslationPort_Object = MibTableColumn
ccWanNatInboundTranslationPort = _CcWanNatInboundTranslationPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 5, 3, 1, 7),
    _CcWanNatInboundTranslationPort_Type()
)
ccWanNatInboundTranslationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanNatInboundTranslationPort.setStatus("current")
_CcWanNatInboundRowStatus_Type = AbbrevRowStatus
_CcWanNatInboundRowStatus_Object = MibTableColumn
ccWanNatInboundRowStatus = _CcWanNatInboundRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 5, 3, 1, 8),
    _CcWanNatInboundRowStatus_Type()
)
ccWanNatInboundRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanNatInboundRowStatus.setStatus("current")
_CcWanNatOutboundTable_Object = MibTable
ccWanNatOutboundTable = _CcWanNatOutboundTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 5, 4)
)
if mibBuilder.loadTexts:
    ccWanNatOutboundTable.setStatus("current")
_CcWanNatOutboundEntry_Object = MibTableRow
ccWanNatOutboundEntry = _CcWanNatOutboundEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 5, 4, 1)
)
ccWanNatOutboundEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWanNatIndex"),
    (0, "SYMBOL-CC-WS2000-MIB", "ccWanNatWanIpAddress"),
    (0, "SYMBOL-CC-WS2000-MIB", "ccWanNatOutboundSubnetIndex"),
)
if mibBuilder.loadTexts:
    ccWanNatOutboundEntry.setStatus("current")


class _CcWanNatOutboundSubnetIndex_Type(Integer32):
    """Custom type ccWanNatOutboundSubnetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CcWanNatOutboundSubnetIndex_Type.__name__ = "Integer32"
_CcWanNatOutboundSubnetIndex_Object = MibTableColumn
ccWanNatOutboundSubnetIndex = _CcWanNatOutboundSubnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 5, 4, 1, 1),
    _CcWanNatOutboundSubnetIndex_Type()
)
ccWanNatOutboundSubnetIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccWanNatOutboundSubnetIndex.setStatus("current")


class _CcWanNatOutboundEnable_Type(Integer32):
    """Custom type ccWanNatOutboundEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CcWanNatOutboundEnable_Type.__name__ = "Integer32"
_CcWanNatOutboundEnable_Object = MibTableColumn
ccWanNatOutboundEnable = _CcWanNatOutboundEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 5, 4, 1, 2),
    _CcWanNatOutboundEnable_Type()
)
ccWanNatOutboundEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanNatOutboundEnable.setStatus("current")
_CcWanNatOutboundPossibleIpAddr_Type = MultiPointer63
_CcWanNatOutboundPossibleIpAddr_Object = MibTableColumn
ccWanNatOutboundPossibleIpAddr = _CcWanNatOutboundPossibleIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 5, 4, 1, 3),
    _CcWanNatOutboundPossibleIpAddr_Type()
)
ccWanNatOutboundPossibleIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWanNatOutboundPossibleIpAddr.setStatus("current")
_CcWanNatOutboundIpAddr_Type = SinglePointer
_CcWanNatOutboundIpAddr_Object = MibTableColumn
ccWanNatOutboundIpAddr = _CcWanNatOutboundIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 5, 4, 1, 4),
    _CcWanNatOutboundIpAddr_Type()
)
ccWanNatOutboundIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanNatOutboundIpAddr.setStatus("current")
_CcWanVpn_ObjectIdentity = ObjectIdentity
ccWanVpn = _CcWanVpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6)
)
_CcWanVpnTunnelConfig_ObjectIdentity = ObjectIdentity
ccWanVpnTunnelConfig = _CcWanVpnTunnelConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4)
)
_CcWanVpnTable_Object = MibTable
ccWanVpnTable = _CcWanVpnTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 1)
)
if mibBuilder.loadTexts:
    ccWanVpnTable.setStatus("current")
_CcWanVpnEntry_Object = MibTableRow
ccWanVpnEntry = _CcWanVpnEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 1, 1)
)
ccWanVpnEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWanVpnIndex"),
)
if mibBuilder.loadTexts:
    ccWanVpnEntry.setStatus("current")


class _CcWanVpnIndex_Type(Integer32):
    """Custom type ccWanVpnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_CcWanVpnIndex_Type.__name__ = "Integer32"
_CcWanVpnIndex_Object = MibTableColumn
ccWanVpnIndex = _CcWanVpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 1, 1, 1),
    _CcWanVpnIndex_Type()
)
ccWanVpnIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccWanVpnIndex.setStatus("current")


class _CcWanVpnName_Type(DisplayString):
    """Custom type ccWanVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 13),
    )


_CcWanVpnName_Type.__name__ = "DisplayString"
_CcWanVpnName_Object = MibTableColumn
ccWanVpnName = _CcWanVpnName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 1, 1, 2),
    _CcWanVpnName_Type()
)
ccWanVpnName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnName.setStatus("current")
_CcWanVpnLocalSubnet_Type = SinglePointer
_CcWanVpnLocalSubnet_Object = MibTableColumn
ccWanVpnLocalSubnet = _CcWanVpnLocalSubnet_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 1, 1, 3),
    _CcWanVpnLocalSubnet_Type()
)
ccWanVpnLocalSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnLocalSubnet.setStatus("current")
_CcWanVpnLocalWanIp_Type = SinglePointer
_CcWanVpnLocalWanIp_Object = MibTableColumn
ccWanVpnLocalWanIp = _CcWanVpnLocalWanIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 1, 1, 4),
    _CcWanVpnLocalWanIp_Type()
)
ccWanVpnLocalWanIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnLocalWanIp.setStatus("current")


class _CcWanVpnRemoteSubnet_Type(IpAddress):
    """Custom type ccWanVpnRemoteSubnet based on IpAddress"""
    defaultHexValue = "00000000"


_CcWanVpnRemoteSubnet_Object = MibTableColumn
ccWanVpnRemoteSubnet = _CcWanVpnRemoteSubnet_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 1, 1, 5),
    _CcWanVpnRemoteSubnet_Type()
)
ccWanVpnRemoteSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnRemoteSubnet.setStatus("current")


class _CcWanVpnRemoteSubnetMask_Type(IpAddress):
    """Custom type ccWanVpnRemoteSubnetMask based on IpAddress"""
    defaultHexValue = "00000000"


_CcWanVpnRemoteSubnetMask_Object = MibTableColumn
ccWanVpnRemoteSubnetMask = _CcWanVpnRemoteSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 1, 1, 6),
    _CcWanVpnRemoteSubnetMask_Type()
)
ccWanVpnRemoteSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnRemoteSubnetMask.setStatus("current")


class _CcWanVpnRemoteGateway_Type(IpAddress):
    """Custom type ccWanVpnRemoteGateway based on IpAddress"""
    defaultHexValue = "00000000"


_CcWanVpnRemoteGateway_Object = MibTableColumn
ccWanVpnRemoteGateway = _CcWanVpnRemoteGateway_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 1, 1, 7),
    _CcWanVpnRemoteGateway_Type()
)
ccWanVpnRemoteGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnRemoteGateway.setStatus("current")


class _CcWanVpnKeyExchange_Type(Integer32):
    """Custom type ccWanVpnKeyExchange based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 2),
          ("manual", 1))
    )


_CcWanVpnKeyExchange_Type.__name__ = "Integer32"
_CcWanVpnKeyExchange_Object = MibTableColumn
ccWanVpnKeyExchange = _CcWanVpnKeyExchange_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 1, 1, 8),
    _CcWanVpnKeyExchange_Type()
)
ccWanVpnKeyExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyExchange.setStatus("current")
_CcWanVpnRowStatus_Type = RowStatus
_CcWanVpnRowStatus_Object = MibTableColumn
ccWanVpnRowStatus = _CcWanVpnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 1, 1, 9),
    _CcWanVpnRowStatus_Type()
)
ccWanVpnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnRowStatus.setStatus("current")
_CcWanVpnKeyManualTable_Object = MibTable
ccWanVpnKeyManualTable = _CcWanVpnKeyManualTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 2)
)
if mibBuilder.loadTexts:
    ccWanVpnKeyManualTable.setStatus("current")
_CcWanVpnKeyManualEntry_Object = MibTableRow
ccWanVpnKeyManualEntry = _CcWanVpnKeyManualEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 2, 1)
)
if mibBuilder.loadTexts:
    ccWanVpnKeyManualEntry.setStatus("current")


class _CcWanVpnKeyManualAhAuth_Type(Integer32):
    """Custom type ccWanVpnKeyManualAhAuth based on Integer32"""
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
        *(("md5", 2),
          ("none", 1),
          ("sha1", 3))
    )


_CcWanVpnKeyManualAhAuth_Type.__name__ = "Integer32"
_CcWanVpnKeyManualAhAuth_Object = MibTableColumn
ccWanVpnKeyManualAhAuth = _CcWanVpnKeyManualAhAuth_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 2, 1, 1),
    _CcWanVpnKeyManualAhAuth_Type()
)
ccWanVpnKeyManualAhAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyManualAhAuth.setStatus("current")


class _CcWanVpnKeyManualInAhAuthKey_Type(HexPassword):
    """Custom type ccWanVpnKeyManualInAhAuthKey based on HexPassword"""
    subtypeSpec = HexPassword.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CcWanVpnKeyManualInAhAuthKey_Type.__name__ = "HexPassword"
_CcWanVpnKeyManualInAhAuthKey_Object = MibTableColumn
ccWanVpnKeyManualInAhAuthKey = _CcWanVpnKeyManualInAhAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 2, 1, 2),
    _CcWanVpnKeyManualInAhAuthKey_Type()
)
ccWanVpnKeyManualInAhAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyManualInAhAuthKey.setStatus("current")


class _CcWanVpnKeyManualOutAhAuthKey_Type(HexPassword):
    """Custom type ccWanVpnKeyManualOutAhAuthKey based on HexPassword"""
    subtypeSpec = HexPassword.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CcWanVpnKeyManualOutAhAuthKey_Type.__name__ = "HexPassword"
_CcWanVpnKeyManualOutAhAuthKey_Object = MibTableColumn
ccWanVpnKeyManualOutAhAuthKey = _CcWanVpnKeyManualOutAhAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 2, 1, 3),
    _CcWanVpnKeyManualOutAhAuthKey_Type()
)
ccWanVpnKeyManualOutAhAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyManualOutAhAuthKey.setStatus("current")


class _CcWanVpnKeyManualInAhSpi_Type(Unsigned32):
    """Custom type ccWanVpnKeyManualInAhSpi based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 4294967295),
    )


_CcWanVpnKeyManualInAhSpi_Type.__name__ = "Unsigned32"
_CcWanVpnKeyManualInAhSpi_Object = MibTableColumn
ccWanVpnKeyManualInAhSpi = _CcWanVpnKeyManualInAhSpi_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 2, 1, 4),
    _CcWanVpnKeyManualInAhSpi_Type()
)
ccWanVpnKeyManualInAhSpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyManualInAhSpi.setStatus("current")


class _CcWanVpnKeyManualOutAhSpi_Type(Unsigned32):
    """Custom type ccWanVpnKeyManualOutAhSpi based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 4294967295),
    )


_CcWanVpnKeyManualOutAhSpi_Type.__name__ = "Unsigned32"
_CcWanVpnKeyManualOutAhSpi_Object = MibTableColumn
ccWanVpnKeyManualOutAhSpi = _CcWanVpnKeyManualOutAhSpi_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 2, 1, 5),
    _CcWanVpnKeyManualOutAhSpi_Type()
)
ccWanVpnKeyManualOutAhSpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyManualOutAhSpi.setStatus("current")


class _CcWanVpnKeyManualEspType_Type(Integer32):
    """Custom type ccWanVpnKeyManualEspType based on Integer32"""
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
        *(("esp", 2),
          ("espWithAuthentication", 3),
          ("none", 1))
    )


_CcWanVpnKeyManualEspType_Type.__name__ = "Integer32"
_CcWanVpnKeyManualEspType_Object = MibTableColumn
ccWanVpnKeyManualEspType = _CcWanVpnKeyManualEspType_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 2, 1, 6),
    _CcWanVpnKeyManualEspType_Type()
)
ccWanVpnKeyManualEspType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyManualEspType.setStatus("current")


class _CcWanVpnKeyManualEspEncrypAlg_Type(Integer32):
    """Custom type ccWanVpnKeyManualEspEncrypAlg based on Integer32"""
    defaultValue = 1

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
        *(("aes128bit", 3),
          ("aes192bit", 4),
          ("aes256bit", 5),
          ("des", 1),
          ("des3", 2))
    )


_CcWanVpnKeyManualEspEncrypAlg_Type.__name__ = "Integer32"
_CcWanVpnKeyManualEspEncrypAlg_Object = MibTableColumn
ccWanVpnKeyManualEspEncrypAlg = _CcWanVpnKeyManualEspEncrypAlg_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 2, 1, 7),
    _CcWanVpnKeyManualEspEncrypAlg_Type()
)
ccWanVpnKeyManualEspEncrypAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyManualEspEncrypAlg.setStatus("current")


class _CcWanVpnKeyManualInEspEncrypKey_Type(HexPassword):
    """Custom type ccWanVpnKeyManualInEspEncrypKey based on HexPassword"""
    subtypeSpec = HexPassword.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CcWanVpnKeyManualInEspEncrypKey_Type.__name__ = "HexPassword"
_CcWanVpnKeyManualInEspEncrypKey_Object = MibTableColumn
ccWanVpnKeyManualInEspEncrypKey = _CcWanVpnKeyManualInEspEncrypKey_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 2, 1, 8),
    _CcWanVpnKeyManualInEspEncrypKey_Type()
)
ccWanVpnKeyManualInEspEncrypKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyManualInEspEncrypKey.setStatus("current")


class _CcWanVpnKeyManualOutEspEncrypKey_Type(HexPassword):
    """Custom type ccWanVpnKeyManualOutEspEncrypKey based on HexPassword"""
    subtypeSpec = HexPassword.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CcWanVpnKeyManualOutEspEncrypKey_Type.__name__ = "HexPassword"
_CcWanVpnKeyManualOutEspEncrypKey_Object = MibTableColumn
ccWanVpnKeyManualOutEspEncrypKey = _CcWanVpnKeyManualOutEspEncrypKey_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 2, 1, 9),
    _CcWanVpnKeyManualOutEspEncrypKey_Type()
)
ccWanVpnKeyManualOutEspEncrypKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyManualOutEspEncrypKey.setStatus("current")


class _CcWanVpnKeyManualEspAuthAlg_Type(Integer32):
    """Custom type ccWanVpnKeyManualEspAuthAlg based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha1", 2))
    )


_CcWanVpnKeyManualEspAuthAlg_Type.__name__ = "Integer32"
_CcWanVpnKeyManualEspAuthAlg_Object = MibTableColumn
ccWanVpnKeyManualEspAuthAlg = _CcWanVpnKeyManualEspAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 2, 1, 10),
    _CcWanVpnKeyManualEspAuthAlg_Type()
)
ccWanVpnKeyManualEspAuthAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyManualEspAuthAlg.setStatus("current")


class _CcWanVpnKeyManualInEspAuthKey_Type(HexPassword):
    """Custom type ccWanVpnKeyManualInEspAuthKey based on HexPassword"""
    subtypeSpec = HexPassword.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CcWanVpnKeyManualInEspAuthKey_Type.__name__ = "HexPassword"
_CcWanVpnKeyManualInEspAuthKey_Object = MibTableColumn
ccWanVpnKeyManualInEspAuthKey = _CcWanVpnKeyManualInEspAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 2, 1, 11),
    _CcWanVpnKeyManualInEspAuthKey_Type()
)
ccWanVpnKeyManualInEspAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyManualInEspAuthKey.setStatus("current")


class _CcWanVpnKeyManualOutEspAuthKey_Type(HexPassword):
    """Custom type ccWanVpnKeyManualOutEspAuthKey based on HexPassword"""
    subtypeSpec = HexPassword.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CcWanVpnKeyManualOutEspAuthKey_Type.__name__ = "HexPassword"
_CcWanVpnKeyManualOutEspAuthKey_Object = MibTableColumn
ccWanVpnKeyManualOutEspAuthKey = _CcWanVpnKeyManualOutEspAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 2, 1, 12),
    _CcWanVpnKeyManualOutEspAuthKey_Type()
)
ccWanVpnKeyManualOutEspAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyManualOutEspAuthKey.setStatus("current")


class _CcWanVpnKeyManualInEspSpi_Type(Unsigned32):
    """Custom type ccWanVpnKeyManualInEspSpi based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 4294967295),
    )


_CcWanVpnKeyManualInEspSpi_Type.__name__ = "Unsigned32"
_CcWanVpnKeyManualInEspSpi_Object = MibTableColumn
ccWanVpnKeyManualInEspSpi = _CcWanVpnKeyManualInEspSpi_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 2, 1, 13),
    _CcWanVpnKeyManualInEspSpi_Type()
)
ccWanVpnKeyManualInEspSpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyManualInEspSpi.setStatus("current")


class _CcWanVpnKeyManualOutEspSpi_Type(Unsigned32):
    """Custom type ccWanVpnKeyManualOutEspSpi based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 4294967295),
    )


_CcWanVpnKeyManualOutEspSpi_Type.__name__ = "Unsigned32"
_CcWanVpnKeyManualOutEspSpi_Object = MibTableColumn
ccWanVpnKeyManualOutEspSpi = _CcWanVpnKeyManualOutEspSpi_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 2, 1, 14),
    _CcWanVpnKeyManualOutEspSpi_Type()
)
ccWanVpnKeyManualOutEspSpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyManualOutEspSpi.setStatus("current")
_CcWanVpnKeyAutoTable_Object = MibTable
ccWanVpnKeyAutoTable = _CcWanVpnKeyAutoTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 3)
)
if mibBuilder.loadTexts:
    ccWanVpnKeyAutoTable.setStatus("current")
_CcWanVpnKeyAutoEntry_Object = MibTableRow
ccWanVpnKeyAutoEntry = _CcWanVpnKeyAutoEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 3, 1)
)
if mibBuilder.loadTexts:
    ccWanVpnKeyAutoEntry.setStatus("current")


class _CcWanVpnKeyAutoUsePerfectSecrecy_Type(TruthValue):
    """Custom type ccWanVpnKeyAutoUsePerfectSecrecy based on TruthValue"""


_CcWanVpnKeyAutoUsePerfectSecrecy_Object = MibTableColumn
ccWanVpnKeyAutoUsePerfectSecrecy = _CcWanVpnKeyAutoUsePerfectSecrecy_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 3, 1, 1),
    _CcWanVpnKeyAutoUsePerfectSecrecy_Type()
)
ccWanVpnKeyAutoUsePerfectSecrecy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyAutoUsePerfectSecrecy.setStatus("current")


class _CcWanVpnKeyAutoAhAuth_Type(Integer32):
    """Custom type ccWanVpnKeyAutoAhAuth based on Integer32"""
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
        *(("md5", 2),
          ("none", 1),
          ("sha1", 3))
    )


_CcWanVpnKeyAutoAhAuth_Type.__name__ = "Integer32"
_CcWanVpnKeyAutoAhAuth_Object = MibTableColumn
ccWanVpnKeyAutoAhAuth = _CcWanVpnKeyAutoAhAuth_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 3, 1, 2),
    _CcWanVpnKeyAutoAhAuth_Type()
)
ccWanVpnKeyAutoAhAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyAutoAhAuth.setStatus("current")


class _CcWanVpnKeyAutoEspType_Type(Integer32):
    """Custom type ccWanVpnKeyAutoEspType based on Integer32"""
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
        *(("esp", 2),
          ("espWithAuthentication", 3),
          ("none", 1))
    )


_CcWanVpnKeyAutoEspType_Type.__name__ = "Integer32"
_CcWanVpnKeyAutoEspType_Object = MibTableColumn
ccWanVpnKeyAutoEspType = _CcWanVpnKeyAutoEspType_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 3, 1, 3),
    _CcWanVpnKeyAutoEspType_Type()
)
ccWanVpnKeyAutoEspType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyAutoEspType.setStatus("current")


class _CcWanVpnKeyAutoEspEncrypAlg_Type(Integer32):
    """Custom type ccWanVpnKeyAutoEspEncrypAlg based on Integer32"""
    defaultValue = 1

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
        *(("aes128bit", 3),
          ("aes196bit", 4),
          ("aes256bit", 5),
          ("des", 1),
          ("des3", 2))
    )


_CcWanVpnKeyAutoEspEncrypAlg_Type.__name__ = "Integer32"
_CcWanVpnKeyAutoEspEncrypAlg_Object = MibTableColumn
ccWanVpnKeyAutoEspEncrypAlg = _CcWanVpnKeyAutoEspEncrypAlg_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 3, 1, 4),
    _CcWanVpnKeyAutoEspEncrypAlg_Type()
)
ccWanVpnKeyAutoEspEncrypAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyAutoEspEncrypAlg.setStatus("current")


class _CcWanVpnKeyAutoEspAuthAlg_Type(Integer32):
    """Custom type ccWanVpnKeyAutoEspAuthAlg based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha1", 2))
    )


_CcWanVpnKeyAutoEspAuthAlg_Type.__name__ = "Integer32"
_CcWanVpnKeyAutoEspAuthAlg_Object = MibTableColumn
ccWanVpnKeyAutoEspAuthAlg = _CcWanVpnKeyAutoEspAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 3, 1, 5),
    _CcWanVpnKeyAutoEspAuthAlg_Type()
)
ccWanVpnKeyAutoEspAuthAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyAutoEspAuthAlg.setStatus("current")


class _CcWanVpnKeyAutoIkeOperationMode_Type(Integer32):
    """Custom type ccWanVpnKeyAutoIkeOperationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggressive", 2),
          ("main", 1))
    )


_CcWanVpnKeyAutoIkeOperationMode_Type.__name__ = "Integer32"
_CcWanVpnKeyAutoIkeOperationMode_Object = MibTableColumn
ccWanVpnKeyAutoIkeOperationMode = _CcWanVpnKeyAutoIkeOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 3, 1, 6),
    _CcWanVpnKeyAutoIkeOperationMode_Type()
)
ccWanVpnKeyAutoIkeOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyAutoIkeOperationMode.setStatus("current")


class _CcWanVpnKeyAutoIkeLocalIdType_Type(Integer32):
    """Custom type ccWanVpnKeyAutoIkeLocalIdType based on Integer32"""
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
        *(("fqdn", 2),
          ("ip", 1),
          ("ufqdn", 3))
    )


_CcWanVpnKeyAutoIkeLocalIdType_Type.__name__ = "Integer32"
_CcWanVpnKeyAutoIkeLocalIdType_Object = MibTableColumn
ccWanVpnKeyAutoIkeLocalIdType = _CcWanVpnKeyAutoIkeLocalIdType_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 3, 1, 7),
    _CcWanVpnKeyAutoIkeLocalIdType_Type()
)
ccWanVpnKeyAutoIkeLocalIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyAutoIkeLocalIdType.setStatus("current")


class _CcWanVpnKeyAutoIkeLocalIdData_Type(DisplayString):
    """Custom type ccWanVpnKeyAutoIkeLocalIdData based on DisplayString"""
    defaultValue = OctetString("?")


_CcWanVpnKeyAutoIkeLocalIdData_Object = MibTableColumn
ccWanVpnKeyAutoIkeLocalIdData = _CcWanVpnKeyAutoIkeLocalIdData_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 3, 1, 8),
    _CcWanVpnKeyAutoIkeLocalIdData_Type()
)
ccWanVpnKeyAutoIkeLocalIdData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyAutoIkeLocalIdData.setStatus("current")


class _CcWanVpnKeyAutoIkeRemoteIdType_Type(Integer32):
    """Custom type ccWanVpnKeyAutoIkeRemoteIdType based on Integer32"""
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
        *(("fqdn", 2),
          ("ip", 1),
          ("ufqdn", 3))
    )


_CcWanVpnKeyAutoIkeRemoteIdType_Type.__name__ = "Integer32"
_CcWanVpnKeyAutoIkeRemoteIdType_Object = MibTableColumn
ccWanVpnKeyAutoIkeRemoteIdType = _CcWanVpnKeyAutoIkeRemoteIdType_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 3, 1, 9),
    _CcWanVpnKeyAutoIkeRemoteIdType_Type()
)
ccWanVpnKeyAutoIkeRemoteIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyAutoIkeRemoteIdType.setStatus("current")


class _CcWanVpnKeyAutoIkeRemoteIdData_Type(DisplayString):
    """Custom type ccWanVpnKeyAutoIkeRemoteIdData based on DisplayString"""
    defaultValue = OctetString("?")


_CcWanVpnKeyAutoIkeRemoteIdData_Object = MibTableColumn
ccWanVpnKeyAutoIkeRemoteIdData = _CcWanVpnKeyAutoIkeRemoteIdData_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 3, 1, 10),
    _CcWanVpnKeyAutoIkeRemoteIdData_Type()
)
ccWanVpnKeyAutoIkeRemoteIdData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyAutoIkeRemoteIdData.setStatus("current")


class _CcWanVpnKeyAutoIkeAuthType_Type(Integer32):
    """Custom type ccWanVpnKeyAutoIkeAuthType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("psk", 1),
          ("rsa", 2))
    )


_CcWanVpnKeyAutoIkeAuthType_Type.__name__ = "Integer32"
_CcWanVpnKeyAutoIkeAuthType_Object = MibTableColumn
ccWanVpnKeyAutoIkeAuthType = _CcWanVpnKeyAutoIkeAuthType_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 3, 1, 11),
    _CcWanVpnKeyAutoIkeAuthType_Type()
)
ccWanVpnKeyAutoIkeAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyAutoIkeAuthType.setStatus("current")


class _CcWanVpnKeyAutoIkeAuthAlg_Type(Integer32):
    """Custom type ccWanVpnKeyAutoIkeAuthAlg based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha1", 2))
    )


_CcWanVpnKeyAutoIkeAuthAlg_Type.__name__ = "Integer32"
_CcWanVpnKeyAutoIkeAuthAlg_Object = MibTableColumn
ccWanVpnKeyAutoIkeAuthAlg = _CcWanVpnKeyAutoIkeAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 3, 1, 12),
    _CcWanVpnKeyAutoIkeAuthAlg_Type()
)
ccWanVpnKeyAutoIkeAuthAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyAutoIkeAuthAlg.setStatus("current")


class _CcWanVpnKeyAutoIkeAuthPassphrase_Type(Password):
    """Custom type ccWanVpnKeyAutoIkeAuthPassphrase based on Password"""
    defaultValue = OctetString("?")


_CcWanVpnKeyAutoIkeAuthPassphrase_Object = MibTableColumn
ccWanVpnKeyAutoIkeAuthPassphrase = _CcWanVpnKeyAutoIkeAuthPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 3, 1, 13),
    _CcWanVpnKeyAutoIkeAuthPassphrase_Type()
)
ccWanVpnKeyAutoIkeAuthPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyAutoIkeAuthPassphrase.setStatus("current")


class _CcWanVpnKeyAutoIkeEncrypAlg_Type(Integer32):
    """Custom type ccWanVpnKeyAutoIkeEncrypAlg based on Integer32"""
    defaultValue = 1

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
        *(("aes128bit", 3),
          ("aes196bit", 4),
          ("aes256bit", 5),
          ("des", 1),
          ("des3", 2))
    )


_CcWanVpnKeyAutoIkeEncrypAlg_Type.__name__ = "Integer32"
_CcWanVpnKeyAutoIkeEncrypAlg_Object = MibTableColumn
ccWanVpnKeyAutoIkeEncrypAlg = _CcWanVpnKeyAutoIkeEncrypAlg_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 3, 1, 14),
    _CcWanVpnKeyAutoIkeEncrypAlg_Type()
)
ccWanVpnKeyAutoIkeEncrypAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyAutoIkeEncrypAlg.setStatus("current")


class _CcWanVpnKeyAutoIkeXauthMode_Type(Integer32):
    """Custom type ccWanVpnKeyAutoIkeXauthMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("generic", 2),
          ("none", 1))
    )


_CcWanVpnKeyAutoIkeXauthMode_Type.__name__ = "Integer32"
_CcWanVpnKeyAutoIkeXauthMode_Object = MibTableColumn
ccWanVpnKeyAutoIkeXauthMode = _CcWanVpnKeyAutoIkeXauthMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 3, 1, 15),
    _CcWanVpnKeyAutoIkeXauthMode_Type()
)
ccWanVpnKeyAutoIkeXauthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyAutoIkeXauthMode.setStatus("current")


class _CcWanVpnKeyAutoIkeXauthUsername_Type(DisplayString):
    """Custom type ccWanVpnKeyAutoIkeXauthUsername based on DisplayString"""
    defaultValue = OctetString("?")


_CcWanVpnKeyAutoIkeXauthUsername_Object = MibTableColumn
ccWanVpnKeyAutoIkeXauthUsername = _CcWanVpnKeyAutoIkeXauthUsername_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 3, 1, 16),
    _CcWanVpnKeyAutoIkeXauthUsername_Type()
)
ccWanVpnKeyAutoIkeXauthUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyAutoIkeXauthUsername.setStatus("current")


class _CcWanVpnKeyAutoIkeXauthPassword_Type(Password):
    """Custom type ccWanVpnKeyAutoIkeXauthPassword based on Password"""
    defaultValue = OctetString("?")


_CcWanVpnKeyAutoIkeXauthPassword_Object = MibTableColumn
ccWanVpnKeyAutoIkeXauthPassword = _CcWanVpnKeyAutoIkeXauthPassword_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 3, 1, 17),
    _CcWanVpnKeyAutoIkeXauthPassword_Type()
)
ccWanVpnKeyAutoIkeXauthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyAutoIkeXauthPassword.setStatus("current")


class _CcWanVpnKeyAutoIkeKeyLifetime_Type(Unsigned32):
    """Custom type ccWanVpnKeyAutoIkeKeyLifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 4294967295),
    )


_CcWanVpnKeyAutoIkeKeyLifetime_Type.__name__ = "Unsigned32"
_CcWanVpnKeyAutoIkeKeyLifetime_Object = MibTableColumn
ccWanVpnKeyAutoIkeKeyLifetime = _CcWanVpnKeyAutoIkeKeyLifetime_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 3, 1, 18),
    _CcWanVpnKeyAutoIkeKeyLifetime_Type()
)
ccWanVpnKeyAutoIkeKeyLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyAutoIkeKeyLifetime.setStatus("current")
if mibBuilder.loadTexts:
    ccWanVpnKeyAutoIkeKeyLifetime.setUnits("seconds")


class _CcWanVpnKeyAutoIkeDiffieHelmanGroup_Type(Integer32):
    """Custom type ccWanVpnKeyAutoIkeDiffieHelmanGroup based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("group1length768bit", 1),
          ("group2length1024bit", 2))
    )


_CcWanVpnKeyAutoIkeDiffieHelmanGroup_Type.__name__ = "Integer32"
_CcWanVpnKeyAutoIkeDiffieHelmanGroup_Object = MibTableColumn
ccWanVpnKeyAutoIkeDiffieHelmanGroup = _CcWanVpnKeyAutoIkeDiffieHelmanGroup_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 4, 3, 1, 19),
    _CcWanVpnKeyAutoIkeDiffieHelmanGroup_Type()
)
ccWanVpnKeyAutoIkeDiffieHelmanGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanVpnKeyAutoIkeDiffieHelmanGroup.setStatus("current")
_CcWanVpnTunnelStatus_ObjectIdentity = ObjectIdentity
ccWanVpnTunnelStatus = _CcWanVpnTunnelStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 5)
)
_CcWanVpnSaTable_Object = MibTable
ccWanVpnSaTable = _CcWanVpnSaTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 5, 1)
)
if mibBuilder.loadTexts:
    ccWanVpnSaTable.setStatus("current")
_CcWanVpnSaEntry_Object = MibTableRow
ccWanVpnSaEntry = _CcWanVpnSaEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 5, 1, 1)
)
ccWanVpnSaEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWanVpnSaTunnelName"),
)
if mibBuilder.loadTexts:
    ccWanVpnSaEntry.setStatus("current")


class _CcWanVpnSaTunnelName_Type(DisplayString):
    """Custom type ccWanVpnSaTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 13),
    )


_CcWanVpnSaTunnelName_Type.__name__ = "DisplayString"
_CcWanVpnSaTunnelName_Object = MibTableColumn
ccWanVpnSaTunnelName = _CcWanVpnSaTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 5, 1, 1, 1),
    _CcWanVpnSaTunnelName_Type()
)
ccWanVpnSaTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWanVpnSaTunnelName.setStatus("current")


class _CcWanVpnSaStatus_Type(Integer32):
    """Custom type ccWanVpnSaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("nonActive", 2))
    )


_CcWanVpnSaStatus_Type.__name__ = "Integer32"
_CcWanVpnSaStatus_Object = MibTableColumn
ccWanVpnSaStatus = _CcWanVpnSaStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 5, 1, 1, 2),
    _CcWanVpnSaStatus_Type()
)
ccWanVpnSaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWanVpnSaStatus.setStatus("current")


class _CcWanVpnSaInSpi_Type(Unsigned32):
    """Custom type ccWanVpnSaInSpi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 4294967295),
    )


_CcWanVpnSaInSpi_Type.__name__ = "Unsigned32"
_CcWanVpnSaInSpi_Object = MibTableColumn
ccWanVpnSaInSpi = _CcWanVpnSaInSpi_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 5, 1, 1, 3),
    _CcWanVpnSaInSpi_Type()
)
ccWanVpnSaInSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWanVpnSaInSpi.setStatus("current")


class _CcWanVpnSaOutSpi_Type(Unsigned32):
    """Custom type ccWanVpnSaOutSpi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 4294967295),
    )


_CcWanVpnSaOutSpi_Type.__name__ = "Unsigned32"
_CcWanVpnSaOutSpi_Object = MibTableColumn
ccWanVpnSaOutSpi = _CcWanVpnSaOutSpi_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 5, 1, 1, 4),
    _CcWanVpnSaOutSpi_Type()
)
ccWanVpnSaOutSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWanVpnSaOutSpi.setStatus("current")
_CcWanVpnSaLifetime_Type = Unsigned32
_CcWanVpnSaLifetime_Object = MibTableColumn
ccWanVpnSaLifetime = _CcWanVpnSaLifetime_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 5, 1, 1, 5),
    _CcWanVpnSaLifetime_Type()
)
ccWanVpnSaLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWanVpnSaLifetime.setStatus("current")
if mibBuilder.loadTexts:
    ccWanVpnSaLifetime.setUnits("seconds")
_CcWanVpnSaTxBytes_Type = Unsigned32
_CcWanVpnSaTxBytes_Object = MibTableColumn
ccWanVpnSaTxBytes = _CcWanVpnSaTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 5, 1, 1, 6),
    _CcWanVpnSaTxBytes_Type()
)
ccWanVpnSaTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWanVpnSaTxBytes.setStatus("current")
_CcWanVpnSaRxBytes_Type = Unsigned32
_CcWanVpnSaRxBytes_Object = MibTableColumn
ccWanVpnSaRxBytes = _CcWanVpnSaRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 5, 1, 1, 7),
    _CcWanVpnSaRxBytes_Type()
)
ccWanVpnSaRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWanVpnSaRxBytes.setStatus("current")
_CcWanVpnIkeTable_Object = MibTable
ccWanVpnIkeTable = _CcWanVpnIkeTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 5, 2)
)
if mibBuilder.loadTexts:
    ccWanVpnIkeTable.setStatus("current")
_CcWanVpnIkeEntry_Object = MibTableRow
ccWanVpnIkeEntry = _CcWanVpnIkeEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 5, 2, 1)
)
ccWanVpnIkeEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWanVpnIkeTunnelName"),
)
if mibBuilder.loadTexts:
    ccWanVpnIkeEntry.setStatus("current")


class _CcWanVpnIkeTunnelName_Type(DisplayString):
    """Custom type ccWanVpnIkeTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CcWanVpnIkeTunnelName_Type.__name__ = "DisplayString"
_CcWanVpnIkeTunnelName_Object = MibTableColumn
ccWanVpnIkeTunnelName = _CcWanVpnIkeTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 5, 2, 1, 1),
    _CcWanVpnIkeTunnelName_Type()
)
ccWanVpnIkeTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWanVpnIkeTunnelName.setStatus("current")
_CcWanVpnIkeState_Type = DisplayString
_CcWanVpnIkeState_Object = MibTableColumn
ccWanVpnIkeState = _CcWanVpnIkeState_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 5, 2, 1, 2),
    _CcWanVpnIkeState_Type()
)
ccWanVpnIkeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWanVpnIkeState.setStatus("current")
_CcWanVpnIkeRemainingLife_Type = Unsigned32
_CcWanVpnIkeRemainingLife_Object = MibTableColumn
ccWanVpnIkeRemainingLife = _CcWanVpnIkeRemainingLife_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 6, 5, 2, 1, 3),
    _CcWanVpnIkeRemainingLife_Type()
)
ccWanVpnIkeRemainingLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWanVpnIkeRemainingLife.setStatus("current")
if mibBuilder.loadTexts:
    ccWanVpnIkeRemainingLife.setUnits("seconds")
_CcWanContentBlock_ObjectIdentity = ObjectIdentity
ccWanContentBlock = _CcWanContentBlock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 7)
)


class _CcWanContentBlockSmtp_Type(Bits):
    """Custom type ccWanContentBlockSmtp based on Bits"""
    namedValues = NamedValues(
        *(("blockSmtpData", 3),
          ("blockSmtpExpn", 9),
          ("blockSmtpHelo", 0),
          ("blockSmtpMail", 1),
          ("blockSmtpQuit", 4),
          ("blockSmtpRcpt", 2),
          ("blockSmtpReset", 7),
          ("blockSmtpSaml", 6),
          ("blockSmtpSend", 5),
          ("blockSmtpVrfy", 8))
    )

_CcWanContentBlockSmtp_Type.__name__ = "Bits"
_CcWanContentBlockSmtp_Object = MibScalar
ccWanContentBlockSmtp = _CcWanContentBlockSmtp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 7, 1),
    _CcWanContentBlockSmtp_Type()
)
ccWanContentBlockSmtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanContentBlockSmtp.setStatus("current")


class _CcWanContentBlockFtp_Type(Bits):
    """Custom type ccWanContentBlockFtp based on Bits"""
    namedValues = NamedValues(
        *(("blockFtpChangeDirectory", 4),
          ("blockFtpCreateDirectory", 3),
          ("blockFtpDirectoryList", 2),
          ("blockFtpPassiveOperation", 5),
          ("blockFtpRetrievingFiles", 1),
          ("blockFtpStoringFiles", 0))
    )

_CcWanContentBlockFtp_Type.__name__ = "Bits"
_CcWanContentBlockFtp_Object = MibScalar
ccWanContentBlockFtp = _CcWanContentBlockFtp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 7, 2),
    _CcWanContentBlockFtp_Type()
)
ccWanContentBlockFtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanContentBlockFtp.setStatus("current")


class _CcWanContentBlockHttp_Type(Bits):
    """Custom type ccWanContentBlockHttp based on Bits"""
    namedValues = NamedValues(
        *(("blockHttpActiveX", 1),
          ("blockHttpWebProxy", 0))
    )

_CcWanContentBlockHttp_Type.__name__ = "Bits"
_CcWanContentBlockHttp_Object = MibScalar
ccWanContentBlockHttp = _CcWanContentBlockHttp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 7, 3),
    _CcWanContentBlockHttp_Type()
)
ccWanContentBlockHttp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanContentBlockHttp.setStatus("current")
_CcWanContentBlockOutUrlTable_Object = MibTable
ccWanContentBlockOutUrlTable = _CcWanContentBlockOutUrlTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 7, 4)
)
if mibBuilder.loadTexts:
    ccWanContentBlockOutUrlTable.setStatus("current")
_CcWanContentBlockOutUrlEntry_Object = MibTableRow
ccWanContentBlockOutUrlEntry = _CcWanContentBlockOutUrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 7, 4, 1)
)
ccWanContentBlockOutUrlEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccWanContentBlockOutUrlIndex"),
)
if mibBuilder.loadTexts:
    ccWanContentBlockOutUrlEntry.setStatus("current")


class _CcWanContentBlockOutUrlIndex_Type(Unsigned32):
    """Custom type ccWanContentBlockOutUrlIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcWanContentBlockOutUrlIndex_Type.__name__ = "Unsigned32"
_CcWanContentBlockOutUrlIndex_Object = MibTableColumn
ccWanContentBlockOutUrlIndex = _CcWanContentBlockOutUrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 7, 4, 1, 1),
    _CcWanContentBlockOutUrlIndex_Type()
)
ccWanContentBlockOutUrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccWanContentBlockOutUrlIndex.setStatus("current")
_CcWanContentBlockOutUrlExtension_Type = DisplayString
_CcWanContentBlockOutUrlExtension_Object = MibTableColumn
ccWanContentBlockOutUrlExtension = _CcWanContentBlockOutUrlExtension_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 7, 4, 1, 2),
    _CcWanContentBlockOutUrlExtension_Type()
)
ccWanContentBlockOutUrlExtension.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanContentBlockOutUrlExtension.setStatus("current")
_CcWanContentBlockOutUrlRowStatus_Type = StaticRowEnable
_CcWanContentBlockOutUrlRowStatus_Object = MibTableColumn
ccWanContentBlockOutUrlRowStatus = _CcWanContentBlockOutUrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 1, 7, 4, 1, 3),
    _CcWanContentBlockOutUrlRowStatus_Type()
)
ccWanContentBlockOutUrlRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccWanContentBlockOutUrlRowStatus.setStatus("current")
_CcPort_ObjectIdentity = ObjectIdentity
ccPort = _CcPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 2)
)
_CcPortTable_Object = MibTable
ccPortTable = _CcPortTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    ccPortTable.setStatus("current")
_CcPortEntry_Object = MibTableRow
ccPortEntry = _CcPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 2, 1, 1)
)
ccPortEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccPortIndex"),
)
if mibBuilder.loadTexts:
    ccPortEntry.setStatus("current")


class _CcPortIndex_Type(Integer32):
    """Custom type ccPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_CcPortIndex_Type.__name__ = "Integer32"
_CcPortIndex_Object = MibTableColumn
ccPortIndex = _CcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 2, 1, 1, 1),
    _CcPortIndex_Type()
)
ccPortIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccPortIndex.setStatus("current")


class _CcPortType_Type(Integer32):
    """Custom type ccPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lanPort", 2),
          ("wanPort", 1))
    )


_CcPortType_Type.__name__ = "Integer32"
_CcPortType_Object = MibTableColumn
ccPortType = _CcPortType_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 2, 1, 1, 2),
    _CcPortType_Type()
)
ccPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortType.setStatus("current")
_CcPortPoeEquipped_Type = TruthValue
_CcPortPoeEquipped_Object = MibTableColumn
ccPortPoeEquipped = _CcPortPoeEquipped_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 2, 1, 1, 3),
    _CcPortPoeEquipped_Type()
)
ccPortPoeEquipped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortPoeEquipped.setStatus("current")


class _CcPortStatus_Type(Integer32):
    """Custom type ccPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_CcPortStatus_Type.__name__ = "Integer32"
_CcPortStatus_Object = MibTableColumn
ccPortStatus = _CcPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 2, 1, 1, 4),
    _CcPortStatus_Type()
)
ccPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortStatus.setStatus("current")


class _CcPortDuplex_Type(Integer32):
    """Custom type ccPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 2),
          ("halfDuplex", 1))
    )


_CcPortDuplex_Type.__name__ = "Integer32"
_CcPortDuplex_Object = MibTableColumn
ccPortDuplex = _CcPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 2, 1, 1, 5),
    _CcPortDuplex_Type()
)
ccPortDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortDuplex.setStatus("current")
_CcPortSpeed_Type = Unsigned32
_CcPortSpeed_Object = MibTableColumn
ccPortSpeed = _CcPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 2, 1, 1, 6),
    _CcPortSpeed_Type()
)
ccPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccPortSpeed.setStatus("current")
_CcLan_ObjectIdentity = ObjectIdentity
ccLan = _CcLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4)
)
_CcSubnet_ObjectIdentity = ObjectIdentity
ccSubnet = _CcSubnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2)
)
_CcSubnetTable_Object = MibTable
ccSubnetTable = _CcSubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 1)
)
if mibBuilder.loadTexts:
    ccSubnetTable.setStatus("current")
_CcSubnetEntry_Object = MibTableRow
ccSubnetEntry = _CcSubnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 1, 1)
)
ccSubnetEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccSubnetIndex"),
)
if mibBuilder.loadTexts:
    ccSubnetEntry.setStatus("current")


class _CcSubnetIndex_Type(Integer32):
    """Custom type ccSubnetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_CcSubnetIndex_Type.__name__ = "Integer32"
_CcSubnetIndex_Object = MibTableColumn
ccSubnetIndex = _CcSubnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 1, 1, 1),
    _CcSubnetIndex_Type()
)
ccSubnetIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccSubnetIndex.setStatus("current")
_CcSubnetEnable_Type = StaticRowEnable
_CcSubnetEnable_Object = MibTableColumn
ccSubnetEnable = _CcSubnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 1, 1, 2),
    _CcSubnetEnable_Type()
)
ccSubnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetEnable.setStatus("current")
_CcSubnetName_Type = DisplayString
_CcSubnetName_Object = MibTableColumn
ccSubnetName = _CcSubnetName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 1, 1, 3),
    _CcSubnetName_Type()
)
ccSubnetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetName.setStatus("current")
_CcSubnetIpAddress_Type = IpAddress
_CcSubnetIpAddress_Object = MibTableColumn
ccSubnetIpAddress = _CcSubnetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 1, 1, 4),
    _CcSubnetIpAddress_Type()
)
ccSubnetIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetIpAddress.setStatus("current")
_CcSubnetIpSubnetMask_Type = IpAddress
_CcSubnetIpSubnetMask_Object = MibTableColumn
ccSubnetIpSubnetMask = _CcSubnetIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 1, 1, 5),
    _CcSubnetIpSubnetMask_Type()
)
ccSubnetIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetIpSubnetMask.setStatus("current")


class _CcSubnetPortMembers_Type(Bits):
    """Custom type ccSubnetPortMembers based on Bits"""
    namedValues = NamedValues(
        *(("null", 0),
          ("port1", 1),
          ("port2", 2),
          ("port3", 3),
          ("port4", 4),
          ("port5", 5),
          ("port6", 6))
    )

_CcSubnetPortMembers_Type.__name__ = "Bits"
_CcSubnetPortMembers_Object = MibTableColumn
ccSubnetPortMembers = _CcSubnetPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 1, 1, 6),
    _CcSubnetPortMembers_Type()
)
ccSubnetPortMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetPortMembers.setStatus("current")


class _CcSubnetWlanMembers_Type(Bits):
    """Custom type ccSubnetWlanMembers based on Bits"""
    namedValues = NamedValues(
        *(("null", 0),
          ("wlan1", 1),
          ("wlan2", 2),
          ("wlan3", 3),
          ("wlan4", 4))
    )

_CcSubnetWlanMembers_Type.__name__ = "Bits"
_CcSubnetWlanMembers_Object = MibTableColumn
ccSubnetWlanMembers = _CcSubnetWlanMembers_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 1, 1, 7),
    _CcSubnetWlanMembers_Type()
)
ccSubnetWlanMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetWlanMembers.setStatus("current")


class _CcSubnetDhcpState_Type(Integer32):
    """Custom type ccSubnetDhcpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dhcpClient", 1),
          ("dhcpNone", 3),
          ("dhcpServer", 2))
    )


_CcSubnetDhcpState_Type.__name__ = "Integer32"
_CcSubnetDhcpState_Object = MibTableColumn
ccSubnetDhcpState = _CcSubnetDhcpState_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 1, 1, 8),
    _CcSubnetDhcpState_Type()
)
ccSubnetDhcpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetDhcpState.setStatus("current")
_CcSubnetDhcpIpAddress_Type = IpAddress
_CcSubnetDhcpIpAddress_Object = MibTableColumn
ccSubnetDhcpIpAddress = _CcSubnetDhcpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 1, 1, 9),
    _CcSubnetDhcpIpAddress_Type()
)
ccSubnetDhcpIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccSubnetDhcpIpAddress.setStatus("current")
_CcSubnetDhcpSubnetMask_Type = IpAddress
_CcSubnetDhcpSubnetMask_Object = MibTableColumn
ccSubnetDhcpSubnetMask = _CcSubnetDhcpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 1, 1, 10),
    _CcSubnetDhcpSubnetMask_Type()
)
ccSubnetDhcpSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccSubnetDhcpSubnetMask.setStatus("current")
_CcSubnetDhcpServerTable_Object = MibTable
ccSubnetDhcpServerTable = _CcSubnetDhcpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 2)
)
if mibBuilder.loadTexts:
    ccSubnetDhcpServerTable.setStatus("current")
_CcSubnetDhcpServerEntry_Object = MibTableRow
ccSubnetDhcpServerEntry = _CcSubnetDhcpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 2, 1)
)
ccSubnetDhcpServerEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccSubnetIndex"),
)
if mibBuilder.loadTexts:
    ccSubnetDhcpServerEntry.setStatus("current")
_CcSubnetDhcpServerEnable_Type = StaticRowEnable
_CcSubnetDhcpServerEnable_Object = MibTableColumn
ccSubnetDhcpServerEnable = _CcSubnetDhcpServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 2, 1, 1),
    _CcSubnetDhcpServerEnable_Type()
)
ccSubnetDhcpServerEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccSubnetDhcpServerEnable.setStatus("current")
_CcSubnetDhcpServerPoolStart_Type = IpAddress
_CcSubnetDhcpServerPoolStart_Object = MibTableColumn
ccSubnetDhcpServerPoolStart = _CcSubnetDhcpServerPoolStart_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 2, 1, 2),
    _CcSubnetDhcpServerPoolStart_Type()
)
ccSubnetDhcpServerPoolStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetDhcpServerPoolStart.setStatus("current")
_CcSubnetDhcpServerPoolEnd_Type = IpAddress
_CcSubnetDhcpServerPoolEnd_Object = MibTableColumn
ccSubnetDhcpServerPoolEnd = _CcSubnetDhcpServerPoolEnd_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 2, 1, 3),
    _CcSubnetDhcpServerPoolEnd_Type()
)
ccSubnetDhcpServerPoolEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetDhcpServerPoolEnd.setStatus("current")
_CcSubnetDhcpServerPrimaryDns_Type = IpAddress
_CcSubnetDhcpServerPrimaryDns_Object = MibTableColumn
ccSubnetDhcpServerPrimaryDns = _CcSubnetDhcpServerPrimaryDns_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 2, 1, 4),
    _CcSubnetDhcpServerPrimaryDns_Type()
)
ccSubnetDhcpServerPrimaryDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetDhcpServerPrimaryDns.setStatus("current")
_CcSubnetDhcpServerSecondaryDns_Type = IpAddress
_CcSubnetDhcpServerSecondaryDns_Object = MibTableColumn
ccSubnetDhcpServerSecondaryDns = _CcSubnetDhcpServerSecondaryDns_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 2, 1, 5),
    _CcSubnetDhcpServerSecondaryDns_Type()
)
ccSubnetDhcpServerSecondaryDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetDhcpServerSecondaryDns.setStatus("current")
_CcSubnetDhcpServerDefaultGateway_Type = IpAddress
_CcSubnetDhcpServerDefaultGateway_Object = MibTableColumn
ccSubnetDhcpServerDefaultGateway = _CcSubnetDhcpServerDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 2, 1, 6),
    _CcSubnetDhcpServerDefaultGateway_Type()
)
ccSubnetDhcpServerDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetDhcpServerDefaultGateway.setStatus("current")
_CcSubnetDhcpServerLeaseTime_Type = Integer32
_CcSubnetDhcpServerLeaseTime_Object = MibTableColumn
ccSubnetDhcpServerLeaseTime = _CcSubnetDhcpServerLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 2, 1, 7),
    _CcSubnetDhcpServerLeaseTime_Type()
)
ccSubnetDhcpServerLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetDhcpServerLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    ccSubnetDhcpServerLeaseTime.setUnits("seconds")
_CcSubnetDhcpServerWinsServer_Type = IpAddress
_CcSubnetDhcpServerWinsServer_Object = MibTableColumn
ccSubnetDhcpServerWinsServer = _CcSubnetDhcpServerWinsServer_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 2, 1, 8),
    _CcSubnetDhcpServerWinsServer_Type()
)
ccSubnetDhcpServerWinsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetDhcpServerWinsServer.setStatus("current")
_CcSubnetDhcpServerDomainName_Type = DisplayString
_CcSubnetDhcpServerDomainName_Object = MibTableColumn
ccSubnetDhcpServerDomainName = _CcSubnetDhcpServerDomainName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 2, 1, 9),
    _CcSubnetDhcpServerDomainName_Type()
)
ccSubnetDhcpServerDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetDhcpServerDomainName.setStatus("current")
_CcSubnetDhcpServerStaticMapTable_Object = MibTable
ccSubnetDhcpServerStaticMapTable = _CcSubnetDhcpServerStaticMapTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 3)
)
if mibBuilder.loadTexts:
    ccSubnetDhcpServerStaticMapTable.setStatus("current")
_CcSubnetDhcpServerStaticMapEntry_Object = MibTableRow
ccSubnetDhcpServerStaticMapEntry = _CcSubnetDhcpServerStaticMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 3, 1)
)
ccSubnetDhcpServerStaticMapEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccSubnetIndex"),
    (0, "SYMBOL-CC-WS2000-MIB", "ccSubnetDhcpServerStaticMapMac"),
)
if mibBuilder.loadTexts:
    ccSubnetDhcpServerStaticMapEntry.setStatus("current")
_CcSubnetDhcpServerStaticMapMac_Type = PhysAddress
_CcSubnetDhcpServerStaticMapMac_Object = MibTableColumn
ccSubnetDhcpServerStaticMapMac = _CcSubnetDhcpServerStaticMapMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 3, 1, 1),
    _CcSubnetDhcpServerStaticMapMac_Type()
)
ccSubnetDhcpServerStaticMapMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccSubnetDhcpServerStaticMapMac.setStatus("current")
_CcSubnetDhcpServerStaticMapIpAddr_Type = IpAddress
_CcSubnetDhcpServerStaticMapIpAddr_Object = MibTableColumn
ccSubnetDhcpServerStaticMapIpAddr = _CcSubnetDhcpServerStaticMapIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 3, 1, 2),
    _CcSubnetDhcpServerStaticMapIpAddr_Type()
)
ccSubnetDhcpServerStaticMapIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccSubnetDhcpServerStaticMapIpAddr.setStatus("current")
_CcSubnetDhcpServerStaticMapEnable_Type = AbbrevRowStatus
_CcSubnetDhcpServerStaticMapEnable_Object = MibTableColumn
ccSubnetDhcpServerStaticMapEnable = _CcSubnetDhcpServerStaticMapEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 3, 1, 3),
    _CcSubnetDhcpServerStaticMapEnable_Type()
)
ccSubnetDhcpServerStaticMapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccSubnetDhcpServerStaticMapEnable.setStatus("current")
_CcSubnetAccess_ObjectIdentity = ObjectIdentity
ccSubnetAccess = _CcSubnetAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4)
)
_CcSubnetAccessTable_Object = MibTable
ccSubnetAccessTable = _CcSubnetAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 1)
)
if mibBuilder.loadTexts:
    ccSubnetAccessTable.setStatus("current")
_CcSubnetAccessEntry_Object = MibTableRow
ccSubnetAccessEntry = _CcSubnetAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 1, 1)
)
ccSubnetAccessEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccSubnetIndex"),
    (0, "SYMBOL-CC-WS2000-MIB", "ccSubnetAccessDestIndex"),
)
if mibBuilder.loadTexts:
    ccSubnetAccessEntry.setStatus("current")


class _CcSubnetAccessDestIndex_Type(Unsigned32):
    """Custom type ccSubnetAccessDestIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CcSubnetAccessDestIndex_Type.__name__ = "Unsigned32"
_CcSubnetAccessDestIndex_Object = MibTableColumn
ccSubnetAccessDestIndex = _CcSubnetAccessDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 1, 1, 1),
    _CcSubnetAccessDestIndex_Type()
)
ccSubnetAccessDestIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccSubnetAccessDestIndex.setStatus("current")


class _CcSubnetAccessDestType_Type(Integer32):
    """Custom type ccSubnetAccessDestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destSubnet", 1),
          ("destWan", 2))
    )


_CcSubnetAccessDestType_Type.__name__ = "Integer32"
_CcSubnetAccessDestType_Object = MibTableColumn
ccSubnetAccessDestType = _CcSubnetAccessDestType_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 1, 1, 2),
    _CcSubnetAccessDestType_Type()
)
ccSubnetAccessDestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccSubnetAccessDestType.setStatus("current")
_CcSubnetAccessDestPtrToDest_Type = SinglePointer
_CcSubnetAccessDestPtrToDest_Object = MibTableColumn
ccSubnetAccessDestPtrToDest = _CcSubnetAccessDestPtrToDest_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 1, 1, 3),
    _CcSubnetAccessDestPtrToDest_Type()
)
ccSubnetAccessDestPtrToDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccSubnetAccessDestPtrToDest.setStatus("current")


class _CcSubnetAccessRuleType_Type(Integer32):
    """Custom type ccSubnetAccessRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_CcSubnetAccessRuleType_Type.__name__ = "Integer32"
_CcSubnetAccessRuleType_Object = MibTableColumn
ccSubnetAccessRuleType = _CcSubnetAccessRuleType_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 1, 1, 4),
    _CcSubnetAccessRuleType_Type()
)
ccSubnetAccessRuleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessRuleType.setStatus("current")
_CcSubnetAccessPtrToRules_Type = MultiPointer255
_CcSubnetAccessPtrToRules_Object = MibTableColumn
ccSubnetAccessPtrToRules = _CcSubnetAccessPtrToRules_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 1, 1, 5),
    _CcSubnetAccessPtrToRules_Type()
)
ccSubnetAccessPtrToRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccSubnetAccessPtrToRules.setStatus("current")
_CcSubnetAccessRuleTable_Object = MibTable
ccSubnetAccessRuleTable = _CcSubnetAccessRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 2)
)
if mibBuilder.loadTexts:
    ccSubnetAccessRuleTable.setStatus("current")
_CcSubnetAccessRuleEntry_Object = MibTableRow
ccSubnetAccessRuleEntry = _CcSubnetAccessRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 2, 1)
)
ccSubnetAccessRuleEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccSubnetAccessRuleIndex"),
)
if mibBuilder.loadTexts:
    ccSubnetAccessRuleEntry.setStatus("current")


class _CcSubnetAccessRuleIndex_Type(Unsigned32):
    """Custom type ccSubnetAccessRuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CcSubnetAccessRuleIndex_Type.__name__ = "Unsigned32"
_CcSubnetAccessRuleIndex_Object = MibTableColumn
ccSubnetAccessRuleIndex = _CcSubnetAccessRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 2, 1, 1),
    _CcSubnetAccessRuleIndex_Type()
)
ccSubnetAccessRuleIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccSubnetAccessRuleIndex.setStatus("current")
_CcSubnetAccessRuleSrcPtr_Type = SinglePointer
_CcSubnetAccessRuleSrcPtr_Object = MibTableColumn
ccSubnetAccessRuleSrcPtr = _CcSubnetAccessRuleSrcPtr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 2, 1, 2),
    _CcSubnetAccessRuleSrcPtr_Type()
)
ccSubnetAccessRuleSrcPtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessRuleSrcPtr.setStatus("current")
_CcSubnetAccessRuleDestPtr_Type = SinglePointer
_CcSubnetAccessRuleDestPtr_Object = MibTableColumn
ccSubnetAccessRuleDestPtr = _CcSubnetAccessRuleDestPtr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 2, 1, 3),
    _CcSubnetAccessRuleDestPtr_Type()
)
ccSubnetAccessRuleDestPtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessRuleDestPtr.setStatus("current")
_CcSubnetAccessRuleName_Type = DisplayString
_CcSubnetAccessRuleName_Object = MibTableColumn
ccSubnetAccessRuleName = _CcSubnetAccessRuleName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 2, 1, 4),
    _CcSubnetAccessRuleName_Type()
)
ccSubnetAccessRuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessRuleName.setStatus("current")


class _CcSubnetAccessRuleTransport_Type(Integer32):
    """Custom type ccSubnetAccessRuleTransport based on Integer32"""
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
        *(("ah", 5),
          ("all", 1),
          ("esp", 6),
          ("gre", 7),
          ("icmp", 4),
          ("tcp", 2),
          ("udp", 3))
    )


_CcSubnetAccessRuleTransport_Type.__name__ = "Integer32"
_CcSubnetAccessRuleTransport_Object = MibTableColumn
ccSubnetAccessRuleTransport = _CcSubnetAccessRuleTransport_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 2, 1, 5),
    _CcSubnetAccessRuleTransport_Type()
)
ccSubnetAccessRuleTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessRuleTransport.setStatus("current")
_CcSubnetAccessRuleStartPort_Type = Integer32
_CcSubnetAccessRuleStartPort_Object = MibTableColumn
ccSubnetAccessRuleStartPort = _CcSubnetAccessRuleStartPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 2, 1, 6),
    _CcSubnetAccessRuleStartPort_Type()
)
ccSubnetAccessRuleStartPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessRuleStartPort.setStatus("current")
_CcSubnetAccessRuleEndPort_Type = Integer32
_CcSubnetAccessRuleEndPort_Object = MibTableColumn
ccSubnetAccessRuleEndPort = _CcSubnetAccessRuleEndPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 2, 1, 7),
    _CcSubnetAccessRuleEndPort_Type()
)
ccSubnetAccessRuleEndPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessRuleEndPort.setStatus("current")
_CcSubnetAccessRuleRowStatus_Type = AbbrevRowStatus
_CcSubnetAccessRuleRowStatus_Object = MibTableColumn
ccSubnetAccessRuleRowStatus = _CcSubnetAccessRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 2, 1, 8),
    _CcSubnetAccessRuleRowStatus_Type()
)
ccSubnetAccessRuleRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessRuleRowStatus.setStatus("current")
_CcSubnetAccessAdvInTable_Object = MibTable
ccSubnetAccessAdvInTable = _CcSubnetAccessAdvInTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 3)
)
if mibBuilder.loadTexts:
    ccSubnetAccessAdvInTable.setStatus("current")
_CcSubnetAccessAdvInEntry_Object = MibTableRow
ccSubnetAccessAdvInEntry = _CcSubnetAccessAdvInEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 3, 1)
)
ccSubnetAccessAdvInEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvInIndex"),
)
if mibBuilder.loadTexts:
    ccSubnetAccessAdvInEntry.setStatus("current")


class _CcSubnetAccessAdvInIndex_Type(Unsigned32):
    """Custom type ccSubnetAccessAdvInIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CcSubnetAccessAdvInIndex_Type.__name__ = "Unsigned32"
_CcSubnetAccessAdvInIndex_Object = MibTableColumn
ccSubnetAccessAdvInIndex = _CcSubnetAccessAdvInIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 3, 1, 1),
    _CcSubnetAccessAdvInIndex_Type()
)
ccSubnetAccessAdvInIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvInIndex.setStatus("current")
_CcSubnetAccessAdvInSrcIp_Type = IpAddress
_CcSubnetAccessAdvInSrcIp_Object = MibTableColumn
ccSubnetAccessAdvInSrcIp = _CcSubnetAccessAdvInSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 3, 1, 2),
    _CcSubnetAccessAdvInSrcIp_Type()
)
ccSubnetAccessAdvInSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvInSrcIp.setStatus("current")


class _CcSubnetAccessAdvInSrcIpLength_Type(Integer32):
    """Custom type ccSubnetAccessAdvInSrcIpLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CcSubnetAccessAdvInSrcIpLength_Type.__name__ = "Integer32"
_CcSubnetAccessAdvInSrcIpLength_Object = MibTableColumn
ccSubnetAccessAdvInSrcIpLength = _CcSubnetAccessAdvInSrcIpLength_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 3, 1, 3),
    _CcSubnetAccessAdvInSrcIpLength_Type()
)
ccSubnetAccessAdvInSrcIpLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvInSrcIpLength.setStatus("current")
_CcSubnetAccessAdvInDestIp_Type = IpAddress
_CcSubnetAccessAdvInDestIp_Object = MibTableColumn
ccSubnetAccessAdvInDestIp = _CcSubnetAccessAdvInDestIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 3, 1, 4),
    _CcSubnetAccessAdvInDestIp_Type()
)
ccSubnetAccessAdvInDestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvInDestIp.setStatus("current")


class _CcSubnetAccessAdvInDestIpLength_Type(Integer32):
    """Custom type ccSubnetAccessAdvInDestIpLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CcSubnetAccessAdvInDestIpLength_Type.__name__ = "Integer32"
_CcSubnetAccessAdvInDestIpLength_Object = MibTableColumn
ccSubnetAccessAdvInDestIpLength = _CcSubnetAccessAdvInDestIpLength_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 3, 1, 5),
    _CcSubnetAccessAdvInDestIpLength_Type()
)
ccSubnetAccessAdvInDestIpLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvInDestIpLength.setStatus("current")


class _CcSubnetAccessAdvInTransport_Type(Integer32):
    """Custom type ccSubnetAccessAdvInTransport based on Integer32"""
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
        *(("ah", 5),
          ("all", 1),
          ("esp", 6),
          ("gre", 7),
          ("icmp", 4),
          ("tcp", 2),
          ("udp", 3))
    )


_CcSubnetAccessAdvInTransport_Type.__name__ = "Integer32"
_CcSubnetAccessAdvInTransport_Object = MibTableColumn
ccSubnetAccessAdvInTransport = _CcSubnetAccessAdvInTransport_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 3, 1, 6),
    _CcSubnetAccessAdvInTransport_Type()
)
ccSubnetAccessAdvInTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvInTransport.setStatus("current")
_CcSubnetAccessAdvInSrcPortStart_Type = Integer32
_CcSubnetAccessAdvInSrcPortStart_Object = MibTableColumn
ccSubnetAccessAdvInSrcPortStart = _CcSubnetAccessAdvInSrcPortStart_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 3, 1, 7),
    _CcSubnetAccessAdvInSrcPortStart_Type()
)
ccSubnetAccessAdvInSrcPortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvInSrcPortStart.setStatus("current")
_CcSubnetAccessAdvInSrcPortEnd_Type = Integer32
_CcSubnetAccessAdvInSrcPortEnd_Object = MibTableColumn
ccSubnetAccessAdvInSrcPortEnd = _CcSubnetAccessAdvInSrcPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 3, 1, 8),
    _CcSubnetAccessAdvInSrcPortEnd_Type()
)
ccSubnetAccessAdvInSrcPortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvInSrcPortEnd.setStatus("current")
_CcSubnetAccessAdvInDestPortStart_Type = Integer32
_CcSubnetAccessAdvInDestPortStart_Object = MibTableColumn
ccSubnetAccessAdvInDestPortStart = _CcSubnetAccessAdvInDestPortStart_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 3, 1, 9),
    _CcSubnetAccessAdvInDestPortStart_Type()
)
ccSubnetAccessAdvInDestPortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvInDestPortStart.setStatus("current")
_CcSubnetAccessAdvInDestPortEnd_Type = Integer32
_CcSubnetAccessAdvInDestPortEnd_Object = MibTableColumn
ccSubnetAccessAdvInDestPortEnd = _CcSubnetAccessAdvInDestPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 3, 1, 10),
    _CcSubnetAccessAdvInDestPortEnd_Type()
)
ccSubnetAccessAdvInDestPortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvInDestPortEnd.setStatus("current")
_CcSubnetAccessAdvInReverseNatIp_Type = IpAddress
_CcSubnetAccessAdvInReverseNatIp_Object = MibTableColumn
ccSubnetAccessAdvInReverseNatIp = _CcSubnetAccessAdvInReverseNatIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 3, 1, 12),
    _CcSubnetAccessAdvInReverseNatIp_Type()
)
ccSubnetAccessAdvInReverseNatIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvInReverseNatIp.setStatus("current")
_CcSubnetAccessAdvInReverseNatPort_Type = Integer32
_CcSubnetAccessAdvInReverseNatPort_Object = MibTableColumn
ccSubnetAccessAdvInReverseNatPort = _CcSubnetAccessAdvInReverseNatPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 3, 1, 13),
    _CcSubnetAccessAdvInReverseNatPort_Type()
)
ccSubnetAccessAdvInReverseNatPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvInReverseNatPort.setStatus("current")


class _CcSubnetAccessAdvInAction_Type(Integer32):
    """Custom type ccSubnetAccessAdvInAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_CcSubnetAccessAdvInAction_Type.__name__ = "Integer32"
_CcSubnetAccessAdvInAction_Object = MibTableColumn
ccSubnetAccessAdvInAction = _CcSubnetAccessAdvInAction_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 3, 1, 14),
    _CcSubnetAccessAdvInAction_Type()
)
ccSubnetAccessAdvInAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvInAction.setStatus("current")
_CcSubnetAccessAdvInRowStatus_Type = AbbrevRowStatus
_CcSubnetAccessAdvInRowStatus_Object = MibTableColumn
ccSubnetAccessAdvInRowStatus = _CcSubnetAccessAdvInRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 3, 1, 15),
    _CcSubnetAccessAdvInRowStatus_Type()
)
ccSubnetAccessAdvInRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvInRowStatus.setStatus("current")
_CcSubnetAccessAdvOutTable_Object = MibTable
ccSubnetAccessAdvOutTable = _CcSubnetAccessAdvOutTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 4)
)
if mibBuilder.loadTexts:
    ccSubnetAccessAdvOutTable.setStatus("current")
_CcSubnetAccessAdvOutEntry_Object = MibTableRow
ccSubnetAccessAdvOutEntry = _CcSubnetAccessAdvOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 4, 1)
)
ccSubnetAccessAdvOutEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvOutIndex"),
)
if mibBuilder.loadTexts:
    ccSubnetAccessAdvOutEntry.setStatus("current")


class _CcSubnetAccessAdvOutIndex_Type(Unsigned32):
    """Custom type ccSubnetAccessAdvOutIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CcSubnetAccessAdvOutIndex_Type.__name__ = "Unsigned32"
_CcSubnetAccessAdvOutIndex_Object = MibTableColumn
ccSubnetAccessAdvOutIndex = _CcSubnetAccessAdvOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 4, 1, 1),
    _CcSubnetAccessAdvOutIndex_Type()
)
ccSubnetAccessAdvOutIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvOutIndex.setStatus("current")
_CcSubnetAccessAdvOutSrcIp_Type = IpAddress
_CcSubnetAccessAdvOutSrcIp_Object = MibTableColumn
ccSubnetAccessAdvOutSrcIp = _CcSubnetAccessAdvOutSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 4, 1, 2),
    _CcSubnetAccessAdvOutSrcIp_Type()
)
ccSubnetAccessAdvOutSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvOutSrcIp.setStatus("current")


class _CcSubnetAccessAdvOutSrcIpLength_Type(Integer32):
    """Custom type ccSubnetAccessAdvOutSrcIpLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CcSubnetAccessAdvOutSrcIpLength_Type.__name__ = "Integer32"
_CcSubnetAccessAdvOutSrcIpLength_Object = MibTableColumn
ccSubnetAccessAdvOutSrcIpLength = _CcSubnetAccessAdvOutSrcIpLength_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 4, 1, 3),
    _CcSubnetAccessAdvOutSrcIpLength_Type()
)
ccSubnetAccessAdvOutSrcIpLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvOutSrcIpLength.setStatus("current")
_CcSubnetAccessAdvOutDestIp_Type = IpAddress
_CcSubnetAccessAdvOutDestIp_Object = MibTableColumn
ccSubnetAccessAdvOutDestIp = _CcSubnetAccessAdvOutDestIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 4, 1, 4),
    _CcSubnetAccessAdvOutDestIp_Type()
)
ccSubnetAccessAdvOutDestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvOutDestIp.setStatus("current")


class _CcSubnetAccessAdvOutDestIpLength_Type(Integer32):
    """Custom type ccSubnetAccessAdvOutDestIpLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CcSubnetAccessAdvOutDestIpLength_Type.__name__ = "Integer32"
_CcSubnetAccessAdvOutDestIpLength_Object = MibTableColumn
ccSubnetAccessAdvOutDestIpLength = _CcSubnetAccessAdvOutDestIpLength_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 4, 1, 5),
    _CcSubnetAccessAdvOutDestIpLength_Type()
)
ccSubnetAccessAdvOutDestIpLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvOutDestIpLength.setStatus("current")


class _CcSubnetAccessAdvOutTransport_Type(Integer32):
    """Custom type ccSubnetAccessAdvOutTransport based on Integer32"""
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
        *(("ah", 5),
          ("all", 1),
          ("esp", 6),
          ("gre", 7),
          ("icmp", 4),
          ("tcp", 2),
          ("udp", 3))
    )


_CcSubnetAccessAdvOutTransport_Type.__name__ = "Integer32"
_CcSubnetAccessAdvOutTransport_Object = MibTableColumn
ccSubnetAccessAdvOutTransport = _CcSubnetAccessAdvOutTransport_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 4, 1, 6),
    _CcSubnetAccessAdvOutTransport_Type()
)
ccSubnetAccessAdvOutTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvOutTransport.setStatus("current")
_CcSubnetAccessAdvOutSrcPortStart_Type = Integer32
_CcSubnetAccessAdvOutSrcPortStart_Object = MibTableColumn
ccSubnetAccessAdvOutSrcPortStart = _CcSubnetAccessAdvOutSrcPortStart_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 4, 1, 7),
    _CcSubnetAccessAdvOutSrcPortStart_Type()
)
ccSubnetAccessAdvOutSrcPortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvOutSrcPortStart.setStatus("current")
_CcSubnetAccessAdvOutSrcPortEnd_Type = Integer32
_CcSubnetAccessAdvOutSrcPortEnd_Object = MibTableColumn
ccSubnetAccessAdvOutSrcPortEnd = _CcSubnetAccessAdvOutSrcPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 4, 1, 8),
    _CcSubnetAccessAdvOutSrcPortEnd_Type()
)
ccSubnetAccessAdvOutSrcPortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvOutSrcPortEnd.setStatus("current")
_CcSubnetAccessAdvOutDestPortStart_Type = Integer32
_CcSubnetAccessAdvOutDestPortStart_Object = MibTableColumn
ccSubnetAccessAdvOutDestPortStart = _CcSubnetAccessAdvOutDestPortStart_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 4, 1, 9),
    _CcSubnetAccessAdvOutDestPortStart_Type()
)
ccSubnetAccessAdvOutDestPortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvOutDestPortStart.setStatus("current")
_CcSubnetAccessAdvOutDestPortEnd_Type = Integer32
_CcSubnetAccessAdvOutDestPortEnd_Object = MibTableColumn
ccSubnetAccessAdvOutDestPortEnd = _CcSubnetAccessAdvOutDestPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 4, 1, 10),
    _CcSubnetAccessAdvOutDestPortEnd_Type()
)
ccSubnetAccessAdvOutDestPortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvOutDestPortEnd.setStatus("current")
_CcSubnetAccessAdvOutReverseNat_Type = SinglePointer
_CcSubnetAccessAdvOutReverseNat_Object = MibTableColumn
ccSubnetAccessAdvOutReverseNat = _CcSubnetAccessAdvOutReverseNat_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 4, 1, 11),
    _CcSubnetAccessAdvOutReverseNat_Type()
)
ccSubnetAccessAdvOutReverseNat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvOutReverseNat.setStatus("current")


class _CcSubnetAccessAdvOutAction_Type(Integer32):
    """Custom type ccSubnetAccessAdvOutAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_CcSubnetAccessAdvOutAction_Type.__name__ = "Integer32"
_CcSubnetAccessAdvOutAction_Object = MibTableColumn
ccSubnetAccessAdvOutAction = _CcSubnetAccessAdvOutAction_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 4, 1, 12),
    _CcSubnetAccessAdvOutAction_Type()
)
ccSubnetAccessAdvOutAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvOutAction.setStatus("current")
_CcSubnetAccessAdvOutRowStatus_Type = AbbrevRowStatus
_CcSubnetAccessAdvOutRowStatus_Object = MibTableColumn
ccSubnetAccessAdvOutRowStatus = _CcSubnetAccessAdvOutRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 4, 1, 13),
    _CcSubnetAccessAdvOutRowStatus_Type()
)
ccSubnetAccessAdvOutRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvOutRowStatus.setStatus("current")
_CcSubnetAccessAdvOverrideMode_Type = TruthValue
_CcSubnetAccessAdvOverrideMode_Object = MibScalar
ccSubnetAccessAdvOverrideMode = _CcSubnetAccessAdvOverrideMode_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 5),
    _CcSubnetAccessAdvOverrideMode_Type()
)
ccSubnetAccessAdvOverrideMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvOverrideMode.setStatus("current")
_CcSubnetAccessAdvImportRules_Type = DoActionNow
_CcSubnetAccessAdvImportRules_Object = MibScalar
ccSubnetAccessAdvImportRules = _CcSubnetAccessAdvImportRules_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 2, 4, 6),
    _CcSubnetAccessAdvImportRules_Type()
)
ccSubnetAccessAdvImportRules.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccSubnetAccessAdvImportRules.setStatus("current")
_CcLanVlan_ObjectIdentity = ObjectIdentity
ccLanVlan = _CcLanVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 3)
)


class _CcLanVlanType_Type(Integer32):
    """Custom type ccLanVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portBased", 1),
          ("userBased", 2))
    )


_CcLanVlanType_Type.__name__ = "Integer32"
_CcLanVlanType_Object = MibScalar
ccLanVlanType = _CcLanVlanType_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 3, 1),
    _CcLanVlanType_Type()
)
ccLanVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLanVlanType.setStatus("current")
_CcLanVlanTrunkPort_Type = Unsigned32
_CcLanVlanTrunkPort_Object = MibScalar
ccLanVlanTrunkPort = _CcLanVlanTrunkPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 3, 2),
    _CcLanVlanTrunkPort_Type()
)
ccLanVlanTrunkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLanVlanTrunkPort.setStatus("current")


class _CcLanVlanDefaultTag_Type(Unsigned32):
    """Custom type ccLanVlanDefaultTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_CcLanVlanDefaultTag_Type.__name__ = "Unsigned32"
_CcLanVlanDefaultTag_Object = MibScalar
ccLanVlanDefaultTag = _CcLanVlanDefaultTag_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 3, 3),
    _CcLanVlanDefaultTag_Type()
)
ccLanVlanDefaultTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLanVlanDefaultTag.setStatus("current")


class _CcLanVlanTrunked_Type(Bits):
    """Custom type ccLanVlanTrunked based on Bits"""
    namedValues = NamedValues(
        *(("noVlansAreTrunked", 0),
          ("trunkVlan01", 1),
          ("trunkVlan02", 2),
          ("trunkVlan03", 3),
          ("trunkVlan04", 4),
          ("trunkVlan05", 5),
          ("trunkVlan06", 6),
          ("trunkVlan07", 7),
          ("trunkVlan08", 8),
          ("trunkVlan09", 9),
          ("trunkVlan10", 10),
          ("trunkVlan11", 11),
          ("trunkVlan12", 12),
          ("trunkVlan13", 13),
          ("trunkVlan14", 14),
          ("trunkVlan15", 15),
          ("trunkVlan16", 16),
          ("trunkVlan17", 17),
          ("trunkVlan18", 18),
          ("trunkVlan19", 19),
          ("trunkVlan20", 20),
          ("trunkVlan21", 21),
          ("trunkVlan22", 22),
          ("trunkVlan23", 23),
          ("trunkVlan24", 24),
          ("trunkVlan25", 25),
          ("trunkVlan26", 26),
          ("trunkVlan27", 27),
          ("trunkVlan28", 28),
          ("trunkVlan29", 29),
          ("trunkVlan30", 30),
          ("trunkVlan31", 31))
    )

_CcLanVlanTrunked_Type.__name__ = "Bits"
_CcLanVlanTrunked_Object = MibScalar
ccLanVlanTrunked = _CcLanVlanTrunked_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 3, 4),
    _CcLanVlanTrunked_Type()
)
ccLanVlanTrunked.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLanVlanTrunked.setStatus("current")
_CcLanVlanTable_Object = MibTable
ccLanVlanTable = _CcLanVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 3, 5)
)
if mibBuilder.loadTexts:
    ccLanVlanTable.setStatus("current")
_CcLanVlanEntry_Object = MibTableRow
ccLanVlanEntry = _CcLanVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 3, 5, 1)
)
ccLanVlanEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccSubnetIndex"),
)
if mibBuilder.loadTexts:
    ccLanVlanEntry.setStatus("current")


class _CcLanVlanId_Type(Unsigned32):
    """Custom type ccLanVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_CcLanVlanId_Type.__name__ = "Unsigned32"
_CcLanVlanId_Object = MibTableColumn
ccLanVlanId = _CcLanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 5, 4, 3, 5, 1, 1),
    _CcLanVlanId_Type()
)
ccLanVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLanVlanId.setStatus("current")
_CcRouter_ObjectIdentity = ObjectIdentity
ccRouter = _CcRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 6)
)
_CcRouterRip_ObjectIdentity = ObjectIdentity
ccRouterRip = _CcRouterRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 6, 1)
)


class _CcRouterRipType_Type(Integer32):
    """Custom type ccRouterRipType based on Integer32"""
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
        *(("noRip", 1),
          ("ripV1", 2),
          ("ripV2", 4),
          ("ripV2withV1compatibility", 3))
    )


_CcRouterRipType_Type.__name__ = "Integer32"
_CcRouterRipType_Object = MibScalar
ccRouterRipType = _CcRouterRipType_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 6, 1, 1),
    _CcRouterRipType_Type()
)
ccRouterRipType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRouterRipType.setStatus("current")


class _CcRouterRipDirection_Type(Integer32):
    """Custom type ccRouterRipDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 1),
          ("rxOnly", 2),
          ("txOnly", 3))
    )


_CcRouterRipDirection_Type.__name__ = "Integer32"
_CcRouterRipDirection_Object = MibScalar
ccRouterRipDirection = _CcRouterRipDirection_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 6, 1, 2),
    _CcRouterRipDirection_Type()
)
ccRouterRipDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRouterRipDirection.setStatus("current")
_CcRouterRip2_ObjectIdentity = ObjectIdentity
ccRouterRip2 = _CcRouterRip2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 6, 1, 3)
)


class _CcRouterRip2AuthType_Type(Integer32):
    """Custom type ccRouterRip2AuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 3),
          ("none", 1),
          ("simple", 2))
    )


_CcRouterRip2AuthType_Type.__name__ = "Integer32"
_CcRouterRip2AuthType_Object = MibScalar
ccRouterRip2AuthType = _CcRouterRip2AuthType_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 6, 1, 3, 1),
    _CcRouterRip2AuthType_Type()
)
ccRouterRip2AuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRouterRip2AuthType.setStatus("current")
_CcRouterRip2SimplePassword_Type = Password
_CcRouterRip2SimplePassword_Object = MibScalar
ccRouterRip2SimplePassword = _CcRouterRip2SimplePassword_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 6, 1, 3, 2),
    _CcRouterRip2SimplePassword_Type()
)
ccRouterRip2SimplePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRouterRip2SimplePassword.setStatus("current")


class _CcRouterRip2Md5Key1Id_Type(Integer32):
    """Custom type ccRouterRip2Md5Key1Id based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CcRouterRip2Md5Key1Id_Type.__name__ = "Integer32"
_CcRouterRip2Md5Key1Id_Object = MibScalar
ccRouterRip2Md5Key1Id = _CcRouterRip2Md5Key1Id_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 6, 1, 3, 3),
    _CcRouterRip2Md5Key1Id_Type()
)
ccRouterRip2Md5Key1Id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRouterRip2Md5Key1Id.setStatus("current")


class _CcRouterRip2Md5Key1AuthKey_Type(Password):
    """Custom type ccRouterRip2Md5Key1AuthKey based on Password"""
    subtypeSpec = Password.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CcRouterRip2Md5Key1AuthKey_Type.__name__ = "Password"
_CcRouterRip2Md5Key1AuthKey_Object = MibScalar
ccRouterRip2Md5Key1AuthKey = _CcRouterRip2Md5Key1AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 6, 1, 3, 4),
    _CcRouterRip2Md5Key1AuthKey_Type()
)
ccRouterRip2Md5Key1AuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRouterRip2Md5Key1AuthKey.setStatus("current")


class _CcRouterRip2Md5Key2Id_Type(Integer32):
    """Custom type ccRouterRip2Md5Key2Id based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CcRouterRip2Md5Key2Id_Type.__name__ = "Integer32"
_CcRouterRip2Md5Key2Id_Object = MibScalar
ccRouterRip2Md5Key2Id = _CcRouterRip2Md5Key2Id_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 6, 1, 3, 5),
    _CcRouterRip2Md5Key2Id_Type()
)
ccRouterRip2Md5Key2Id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRouterRip2Md5Key2Id.setStatus("current")


class _CcRouterRip2Md5Key2AuthKey_Type(Password):
    """Custom type ccRouterRip2Md5Key2AuthKey based on Password"""
    subtypeSpec = Password.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CcRouterRip2Md5Key2AuthKey_Type.__name__ = "Password"
_CcRouterRip2Md5Key2AuthKey_Object = MibScalar
ccRouterRip2Md5Key2AuthKey = _CcRouterRip2Md5Key2AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 6, 1, 3, 6),
    _CcRouterRip2Md5Key2AuthKey_Type()
)
ccRouterRip2Md5Key2AuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRouterRip2Md5Key2AuthKey.setStatus("current")
_CcRouterRoutesTable_Object = MibTable
ccRouterRoutesTable = _CcRouterRoutesTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 6, 2)
)
if mibBuilder.loadTexts:
    ccRouterRoutesTable.setStatus("current")
_CcRouterRoutesEntry_Object = MibTableRow
ccRouterRoutesEntry = _CcRouterRoutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 6, 2, 1)
)
ccRouterRoutesEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccRouterRoutesIndex"),
)
if mibBuilder.loadTexts:
    ccRouterRoutesEntry.setStatus("current")


class _CcRouterRoutesIndex_Type(Unsigned32):
    """Custom type ccRouterRoutesIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CcRouterRoutesIndex_Type.__name__ = "Unsigned32"
_CcRouterRoutesIndex_Object = MibTableColumn
ccRouterRoutesIndex = _CcRouterRoutesIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 6, 2, 1, 1),
    _CcRouterRoutesIndex_Type()
)
ccRouterRoutesIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccRouterRoutesIndex.setStatus("current")
_CcRouterRoutesDest_Type = IpAddress
_CcRouterRoutesDest_Object = MibTableColumn
ccRouterRoutesDest = _CcRouterRoutesDest_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 6, 2, 1, 2),
    _CcRouterRoutesDest_Type()
)
ccRouterRoutesDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRouterRoutesDest.setStatus("current")
_CcRouterRoutesDestMask_Type = IpAddress
_CcRouterRoutesDestMask_Object = MibTableColumn
ccRouterRoutesDestMask = _CcRouterRoutesDestMask_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 6, 2, 1, 3),
    _CcRouterRoutesDestMask_Type()
)
ccRouterRoutesDestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRouterRoutesDestMask.setStatus("current")
_CcRouterRoutesGateway_Type = IpAddress
_CcRouterRoutesGateway_Object = MibTableColumn
ccRouterRoutesGateway = _CcRouterRoutesGateway_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 6, 2, 1, 4),
    _CcRouterRoutesGateway_Type()
)
ccRouterRoutesGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRouterRoutesGateway.setStatus("current")
_CcRouterRoutesInterface_Type = SinglePointer
_CcRouterRoutesInterface_Object = MibTableColumn
ccRouterRoutesInterface = _CcRouterRoutesInterface_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 6, 2, 1, 5),
    _CcRouterRoutesInterface_Type()
)
ccRouterRoutesInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRouterRoutesInterface.setStatus("current")
_CcRouterRoutesMetric_Type = Integer32
_CcRouterRoutesMetric_Object = MibTableColumn
ccRouterRoutesMetric = _CcRouterRoutesMetric_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 6, 2, 1, 6),
    _CcRouterRoutesMetric_Type()
)
ccRouterRoutesMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRouterRoutesMetric.setStatus("current")
_CcRouterUserRoutesTable_Object = MibTable
ccRouterUserRoutesTable = _CcRouterUserRoutesTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 6, 3)
)
if mibBuilder.loadTexts:
    ccRouterUserRoutesTable.setStatus("current")
_CcRouterUserRoutesEntry_Object = MibTableRow
ccRouterUserRoutesEntry = _CcRouterUserRoutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 6, 3, 1)
)
ccRouterUserRoutesEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccRouterUserRoutesIndex"),
)
if mibBuilder.loadTexts:
    ccRouterUserRoutesEntry.setStatus("current")


class _CcRouterUserRoutesIndex_Type(Integer32):
    """Custom type ccRouterUserRoutesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CcRouterUserRoutesIndex_Type.__name__ = "Integer32"
_CcRouterUserRoutesIndex_Object = MibTableColumn
ccRouterUserRoutesIndex = _CcRouterUserRoutesIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 6, 3, 1, 1),
    _CcRouterUserRoutesIndex_Type()
)
ccRouterUserRoutesIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccRouterUserRoutesIndex.setStatus("current")
_CcRouterUserRoutesDest_Type = IpAddress
_CcRouterUserRoutesDest_Object = MibTableColumn
ccRouterUserRoutesDest = _CcRouterUserRoutesDest_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 6, 3, 1, 2),
    _CcRouterUserRoutesDest_Type()
)
ccRouterUserRoutesDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRouterUserRoutesDest.setStatus("current")
_CcRouterUserRoutesDestMask_Type = IpAddress
_CcRouterUserRoutesDestMask_Object = MibTableColumn
ccRouterUserRoutesDestMask = _CcRouterUserRoutesDestMask_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 6, 3, 1, 3),
    _CcRouterUserRoutesDestMask_Type()
)
ccRouterUserRoutesDestMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRouterUserRoutesDestMask.setStatus("current")
_CcRouterUserRoutesGateway_Type = IpAddress
_CcRouterUserRoutesGateway_Object = MibTableColumn
ccRouterUserRoutesGateway = _CcRouterUserRoutesGateway_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 6, 3, 1, 4),
    _CcRouterUserRoutesGateway_Type()
)
ccRouterUserRoutesGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRouterUserRoutesGateway.setStatus("current")


class _CcRouterUserRoutesInterface_Type(Integer32):
    """Custom type ccRouterUserRoutesInterface based on Integer32"""
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
        *(("subnet1", 2),
          ("subnet2", 3),
          ("subnet3", 4),
          ("subnet4", 5),
          ("wan", 1))
    )


_CcRouterUserRoutesInterface_Type.__name__ = "Integer32"
_CcRouterUserRoutesInterface_Object = MibTableColumn
ccRouterUserRoutesInterface = _CcRouterUserRoutesInterface_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 6, 3, 1, 5),
    _CcRouterUserRoutesInterface_Type()
)
ccRouterUserRoutesInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRouterUserRoutesInterface.setStatus("current")
_CcRouterUserRoutesMetric_Type = Integer32
_CcRouterUserRoutesMetric_Object = MibTableColumn
ccRouterUserRoutesMetric = _CcRouterUserRoutesMetric_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 6, 3, 1, 6),
    _CcRouterUserRoutesMetric_Type()
)
ccRouterUserRoutesMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRouterUserRoutesMetric.setStatus("current")
_CcRouterUserRoutesRowStatus_Type = AbbrevRowStatus
_CcRouterUserRoutesRowStatus_Object = MibTableColumn
ccRouterUserRoutesRowStatus = _CcRouterUserRoutesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 6, 3, 1, 7),
    _CcRouterUserRoutesRowStatus_Type()
)
ccRouterUserRoutesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRouterUserRoutesRowStatus.setStatus("current")
_CcRap_ObjectIdentity = ObjectIdentity
ccRap = _CcRap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7)
)
_CcRapControl_ObjectIdentity = ObjectIdentity
ccRapControl = _CcRapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 1)
)
_CcRapControlPollSymbolMus_ObjectIdentity = ObjectIdentity
ccRapControlPollSymbolMus = _CcRapControlPollSymbolMus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 1, 3)
)
_CcRapPollSymbolMusEnable_Type = TruthValue
_CcRapPollSymbolMusEnable_Object = MibScalar
ccRapPollSymbolMusEnable = _CcRapPollSymbolMusEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 1, 3, 1),
    _CcRapPollSymbolMusEnable_Type()
)
ccRapPollSymbolMusEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapPollSymbolMusEnable.setStatus("current")
_CcRapPollSymbolMusInterval_Type = Integer32
_CcRapPollSymbolMusInterval_Object = MibScalar
ccRapPollSymbolMusInterval = _CcRapPollSymbolMusInterval_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 1, 3, 2),
    _CcRapPollSymbolMusInterval_Type()
)
ccRapPollSymbolMusInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapPollSymbolMusInterval.setStatus("current")
if mibBuilder.loadTexts:
    ccRapPollSymbolMusInterval.setUnits("minutes")
_CcRapControlOnChannel_ObjectIdentity = ObjectIdentity
ccRapControlOnChannel = _CcRapControlOnChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 1, 4)
)
_CcRapOnChannelEnable_Type = TruthValue
_CcRapOnChannelEnable_Object = MibScalar
ccRapOnChannelEnable = _CcRapOnChannelEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 1, 4, 1),
    _CcRapOnChannelEnable_Type()
)
ccRapOnChannelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapOnChannelEnable.setStatus("current")
_CcRapOnChannelInterval_Type = Integer32
_CcRapOnChannelInterval_Object = MibScalar
ccRapOnChannelInterval = _CcRapOnChannelInterval_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 1, 4, 2),
    _CcRapOnChannelInterval_Type()
)
ccRapOnChannelInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapOnChannelInterval.setStatus("current")
if mibBuilder.loadTexts:
    ccRapOnChannelInterval.setUnits("minutes")
_CcRapControlDetectors_ObjectIdentity = ObjectIdentity
ccRapControlDetectors = _CcRapControlDetectors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 1, 5)
)
_CcRapDetectorsEnable_Type = TruthValue
_CcRapDetectorsEnable_Object = MibScalar
ccRapDetectorsEnable = _CcRapDetectorsEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 1, 5, 1),
    _CcRapDetectorsEnable_Type()
)
ccRapDetectorsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapDetectorsEnable.setStatus("current")
_CcRapDetectorsInterval_Type = Integer32
_CcRapDetectorsInterval_Object = MibScalar
ccRapDetectorsInterval = _CcRapDetectorsInterval_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 1, 5, 2),
    _CcRapDetectorsInterval_Type()
)
ccRapDetectorsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapDetectorsInterval.setStatus("current")
if mibBuilder.loadTexts:
    ccRapDetectorsInterval.setUnits("minutes")
_CcRapAuth_ObjectIdentity = ObjectIdentity
ccRapAuth = _CcRapAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 2)
)
_CcRapAuthList_ObjectIdentity = ObjectIdentity
ccRapAuthList = _CcRapAuthList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 2, 2)
)
_CcRapAuthAllSymbolMac_Type = TruthValue
_CcRapAuthAllSymbolMac_Object = MibScalar
ccRapAuthAllSymbolMac = _CcRapAuthAllSymbolMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 2, 2, 1),
    _CcRapAuthAllSymbolMac_Type()
)
ccRapAuthAllSymbolMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapAuthAllSymbolMac.setStatus("current")
_CcRapAuthTable_Object = MibTable
ccRapAuthTable = _CcRapAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ccRapAuthTable.setStatus("current")
_CcRapAuthEntry_Object = MibTableRow
ccRapAuthEntry = _CcRapAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 2, 2, 2, 1)
)
ccRapAuthEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccRapAuthIndex"),
)
if mibBuilder.loadTexts:
    ccRapAuthEntry.setStatus("current")


class _CcRapAuthIndex_Type(Unsigned32):
    """Custom type ccRapAuthIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_CcRapAuthIndex_Type.__name__ = "Unsigned32"
_CcRapAuthIndex_Object = MibTableColumn
ccRapAuthIndex = _CcRapAuthIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 2, 2, 2, 1, 1),
    _CcRapAuthIndex_Type()
)
ccRapAuthIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccRapAuthIndex.setStatus("current")
_CcRapAuthMacFilter_Type = PhysAddress
_CcRapAuthMacFilter_Object = MibTableColumn
ccRapAuthMacFilter = _CcRapAuthMacFilter_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 2, 2, 2, 1, 2),
    _CcRapAuthMacFilter_Type()
)
ccRapAuthMacFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapAuthMacFilter.setStatus("current")
_CcRapAuthEssidFilter_Type = DisplayString
_CcRapAuthEssidFilter_Object = MibTableColumn
ccRapAuthEssidFilter = _CcRapAuthEssidFilter_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 2, 2, 2, 1, 3),
    _CcRapAuthEssidFilter_Type()
)
ccRapAuthEssidFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapAuthEssidFilter.setStatus("current")
_CcRapAuthRowExists_Type = TruthValue
_CcRapAuthRowExists_Object = MibTableColumn
ccRapAuthRowExists = _CcRapAuthRowExists_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 2, 2, 2, 1, 4),
    _CcRapAuthRowExists_Type()
)
ccRapAuthRowExists.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapAuthRowExists.setStatus("current")
_CcRapAuthErase_Type = DoActionNow
_CcRapAuthErase_Object = MibScalar
ccRapAuthErase = _CcRapAuthErase_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 2, 2, 3),
    _CcRapAuthErase_Type()
)
ccRapAuthErase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapAuthErase.setStatus("current")
_CcRapAuthCopyAllApproved_Type = DoActionNow
_CcRapAuthCopyAllApproved_Object = MibScalar
ccRapAuthCopyAllApproved = _CcRapAuthCopyAllApproved_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 2, 2, 4),
    _CcRapAuthCopyAllApproved_Type()
)
ccRapAuthCopyAllApproved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapAuthCopyAllApproved.setStatus("current")
_CcRapAuthCopyAllRogue_Type = DoActionNow
_CcRapAuthCopyAllRogue_Object = MibScalar
ccRapAuthCopyAllRogue = _CcRapAuthCopyAllRogue_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 2, 2, 5),
    _CcRapAuthCopyAllRogue_Type()
)
ccRapAuthCopyAllRogue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapAuthCopyAllRogue.setStatus("current")
_CcRapResults_ObjectIdentity = ObjectIdentity
ccRapResults = _CcRapResults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3)
)
_CcRapResultsApproved_ObjectIdentity = ObjectIdentity
ccRapResultsApproved = _CcRapResultsApproved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 1)
)
_CcRapResultsApprovedAgeOut_Type = Integer32
_CcRapResultsApprovedAgeOut_Object = MibScalar
ccRapResultsApprovedAgeOut = _CcRapResultsApprovedAgeOut_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 1, 1),
    _CcRapResultsApprovedAgeOut_Type()
)
ccRapResultsApprovedAgeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapResultsApprovedAgeOut.setStatus("current")
if mibBuilder.loadTexts:
    ccRapResultsApprovedAgeOut.setUnits("minutes")
_CcRapResultsApprovedTable_Object = MibTable
ccRapResultsApprovedTable = _CcRapResultsApprovedTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ccRapResultsApprovedTable.setStatus("current")
_CcRapResultsApprovedEntry_Object = MibTableRow
ccRapResultsApprovedEntry = _CcRapResultsApprovedEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 1, 2, 1)
)
ccRapResultsApprovedEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccRapResultsApprovedIndex"),
)
if mibBuilder.loadTexts:
    ccRapResultsApprovedEntry.setStatus("current")


class _CcRapResultsApprovedIndex_Type(Unsigned32):
    """Custom type ccRapResultsApprovedIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_CcRapResultsApprovedIndex_Type.__name__ = "Unsigned32"
_CcRapResultsApprovedIndex_Object = MibTableColumn
ccRapResultsApprovedIndex = _CcRapResultsApprovedIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 1, 2, 1, 1),
    _CcRapResultsApprovedIndex_Type()
)
ccRapResultsApprovedIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccRapResultsApprovedIndex.setStatus("current")
_CcRapResultsApprovedApMac_Type = PhysAddress
_CcRapResultsApprovedApMac_Object = MibTableColumn
ccRapResultsApprovedApMac = _CcRapResultsApprovedApMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 1, 2, 1, 2),
    _CcRapResultsApprovedApMac_Type()
)
ccRapResultsApprovedApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsApprovedApMac.setStatus("current")
_CcRapResultsApprovedEssid_Type = DisplayString
_CcRapResultsApprovedEssid_Object = MibTableColumn
ccRapResultsApprovedEssid = _CcRapResultsApprovedEssid_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 1, 2, 1, 3),
    _CcRapResultsApprovedEssid_Type()
)
ccRapResultsApprovedEssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsApprovedEssid.setStatus("current")
_CcRapResultsApprovedCopyToAuthTable_Type = DoActionNow
_CcRapResultsApprovedCopyToAuthTable_Object = MibTableColumn
ccRapResultsApprovedCopyToAuthTable = _CcRapResultsApprovedCopyToAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 1, 2, 1, 4),
    _CcRapResultsApprovedCopyToAuthTable_Type()
)
ccRapResultsApprovedCopyToAuthTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapResultsApprovedCopyToAuthTable.setStatus("current")
_CcRapResultsApprovedFirstHeard_Type = TimeTicks
_CcRapResultsApprovedFirstHeard_Object = MibTableColumn
ccRapResultsApprovedFirstHeard = _CcRapResultsApprovedFirstHeard_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 1, 2, 1, 5),
    _CcRapResultsApprovedFirstHeard_Type()
)
ccRapResultsApprovedFirstHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsApprovedFirstHeard.setStatus("current")
_CcRapResultsApprovedLastHeard_Type = TimeTicks
_CcRapResultsApprovedLastHeard_Object = MibTableColumn
ccRapResultsApprovedLastHeard = _CcRapResultsApprovedLastHeard_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 1, 2, 1, 6),
    _CcRapResultsApprovedLastHeard_Type()
)
ccRapResultsApprovedLastHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsApprovedLastHeard.setStatus("current")
_CcRapResultsApprovedPortalPtr_Type = MultiPointer255
_CcRapResultsApprovedPortalPtr_Object = MibTableColumn
ccRapResultsApprovedPortalPtr = _CcRapResultsApprovedPortalPtr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 1, 2, 1, 7),
    _CcRapResultsApprovedPortalPtr_Type()
)
ccRapResultsApprovedPortalPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsApprovedPortalPtr.setStatus("current")


class _CcRapResultsApprovedHowFound_Type(Integer32):
    """Custom type ccRapResultsApprovedHowFound based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("viaDetector", 3),
          ("viaOnChannelDetection", 2),
          ("viaSymbolMuPolling", 1))
    )


_CcRapResultsApprovedHowFound_Type.__name__ = "Integer32"
_CcRapResultsApprovedHowFound_Object = MibTableColumn
ccRapResultsApprovedHowFound = _CcRapResultsApprovedHowFound_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 1, 2, 1, 8),
    _CcRapResultsApprovedHowFound_Type()
)
ccRapResultsApprovedHowFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsApprovedHowFound.setStatus("current")


class _CcRapResultsApprovedHowAuth_Type(Integer32):
    """Custom type ccRapResultsApprovedHowAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onAuthList", 1),
          ("viaRadius", 2))
    )


_CcRapResultsApprovedHowAuth_Type.__name__ = "Integer32"
_CcRapResultsApprovedHowAuth_Object = MibTableColumn
ccRapResultsApprovedHowAuth = _CcRapResultsApprovedHowAuth_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 1, 2, 1, 9),
    _CcRapResultsApprovedHowAuth_Type()
)
ccRapResultsApprovedHowAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsApprovedHowAuth.setStatus("current")
_CcRapResultsApprovedChannel_Type = Integer32
_CcRapResultsApprovedChannel_Object = MibTableColumn
ccRapResultsApprovedChannel = _CcRapResultsApprovedChannel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 1, 2, 1, 10),
    _CcRapResultsApprovedChannel_Type()
)
ccRapResultsApprovedChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsApprovedChannel.setStatus("current")
_CcRapResultsApprovedErase_Type = DoActionNow
_CcRapResultsApprovedErase_Object = MibScalar
ccRapResultsApprovedErase = _CcRapResultsApprovedErase_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 1, 3),
    _CcRapResultsApprovedErase_Type()
)
ccRapResultsApprovedErase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapResultsApprovedErase.setStatus("current")
_CcRapResultsRogue_ObjectIdentity = ObjectIdentity
ccRapResultsRogue = _CcRapResultsRogue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 2)
)
_CcRapResultsRogueAgeOut_Type = Integer32
_CcRapResultsRogueAgeOut_Object = MibScalar
ccRapResultsRogueAgeOut = _CcRapResultsRogueAgeOut_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 2, 1),
    _CcRapResultsRogueAgeOut_Type()
)
ccRapResultsRogueAgeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapResultsRogueAgeOut.setStatus("current")
if mibBuilder.loadTexts:
    ccRapResultsRogueAgeOut.setUnits("minutes")
_CcRapResultsRogueTable_Object = MibTable
ccRapResultsRogueTable = _CcRapResultsRogueTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 2, 2)
)
if mibBuilder.loadTexts:
    ccRapResultsRogueTable.setStatus("current")
_CcRapResultsRogueEntry_Object = MibTableRow
ccRapResultsRogueEntry = _CcRapResultsRogueEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 2, 2, 1)
)
ccRapResultsRogueEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccRapResultsRogueIndex"),
)
if mibBuilder.loadTexts:
    ccRapResultsRogueEntry.setStatus("current")


class _CcRapResultsRogueIndex_Type(Unsigned32):
    """Custom type ccRapResultsRogueIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_CcRapResultsRogueIndex_Type.__name__ = "Unsigned32"
_CcRapResultsRogueIndex_Object = MibTableColumn
ccRapResultsRogueIndex = _CcRapResultsRogueIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 2, 2, 1, 1),
    _CcRapResultsRogueIndex_Type()
)
ccRapResultsRogueIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccRapResultsRogueIndex.setStatus("current")
_CcRapResultsRogueApMac_Type = PhysAddress
_CcRapResultsRogueApMac_Object = MibTableColumn
ccRapResultsRogueApMac = _CcRapResultsRogueApMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 2, 2, 1, 2),
    _CcRapResultsRogueApMac_Type()
)
ccRapResultsRogueApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsRogueApMac.setStatus("current")
_CcRapResultsRogueEssid_Type = DisplayString
_CcRapResultsRogueEssid_Object = MibTableColumn
ccRapResultsRogueEssid = _CcRapResultsRogueEssid_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 2, 2, 1, 3),
    _CcRapResultsRogueEssid_Type()
)
ccRapResultsRogueEssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsRogueEssid.setStatus("current")
_CcRapResultsRogueCopyToAuthTable_Type = DoActionNow
_CcRapResultsRogueCopyToAuthTable_Object = MibTableColumn
ccRapResultsRogueCopyToAuthTable = _CcRapResultsRogueCopyToAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 2, 2, 1, 4),
    _CcRapResultsRogueCopyToAuthTable_Type()
)
ccRapResultsRogueCopyToAuthTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapResultsRogueCopyToAuthTable.setStatus("current")
_CcRapResultsRogueFirstHeard_Type = TimeTicks
_CcRapResultsRogueFirstHeard_Object = MibTableColumn
ccRapResultsRogueFirstHeard = _CcRapResultsRogueFirstHeard_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 2, 2, 1, 5),
    _CcRapResultsRogueFirstHeard_Type()
)
ccRapResultsRogueFirstHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsRogueFirstHeard.setStatus("current")
_CcRapResultsRogueLastHeard_Type = TimeTicks
_CcRapResultsRogueLastHeard_Object = MibTableColumn
ccRapResultsRogueLastHeard = _CcRapResultsRogueLastHeard_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 2, 2, 1, 6),
    _CcRapResultsRogueLastHeard_Type()
)
ccRapResultsRogueLastHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsRogueLastHeard.setStatus("current")
_CcRapResultsRoguePortalPtr_Type = MultiPointer255
_CcRapResultsRoguePortalPtr_Object = MibTableColumn
ccRapResultsRoguePortalPtr = _CcRapResultsRoguePortalPtr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 2, 2, 1, 7),
    _CcRapResultsRoguePortalPtr_Type()
)
ccRapResultsRoguePortalPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsRoguePortalPtr.setStatus("current")


class _CcRapResultsRogueHowFound_Type(Integer32):
    """Custom type ccRapResultsRogueHowFound based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("viaDetector", 3),
          ("viaOnChannelDetection", 2),
          ("viaSymbolMuPolling", 1))
    )


_CcRapResultsRogueHowFound_Type.__name__ = "Integer32"
_CcRapResultsRogueHowFound_Object = MibTableColumn
ccRapResultsRogueHowFound = _CcRapResultsRogueHowFound_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 2, 2, 1, 8),
    _CcRapResultsRogueHowFound_Type()
)
ccRapResultsRogueHowFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsRogueHowFound.setStatus("current")
_CcRapResultsRogueClosestPortalPtr_Type = SinglePointer
_CcRapResultsRogueClosestPortalPtr_Object = MibTableColumn
ccRapResultsRogueClosestPortalPtr = _CcRapResultsRogueClosestPortalPtr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 2, 2, 1, 9),
    _CcRapResultsRogueClosestPortalPtr_Type()
)
ccRapResultsRogueClosestPortalPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsRogueClosestPortalPtr.setStatus("current")
_CcRapResultsRogueClosestPortalRssi_Type = Integer32
_CcRapResultsRogueClosestPortalRssi_Object = MibTableColumn
ccRapResultsRogueClosestPortalRssi = _CcRapResultsRogueClosestPortalRssi_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 2, 2, 1, 10),
    _CcRapResultsRogueClosestPortalRssi_Type()
)
ccRapResultsRogueClosestPortalRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsRogueClosestPortalRssi.setStatus("current")
_CcRapResultsRogueChannel_Type = Integer32
_CcRapResultsRogueChannel_Object = MibTableColumn
ccRapResultsRogueChannel = _CcRapResultsRogueChannel_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 2, 2, 1, 11),
    _CcRapResultsRogueChannel_Type()
)
ccRapResultsRogueChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapResultsRogueChannel.setStatus("current")
_CcRapResultsRogueErase_Type = DoActionNow
_CcRapResultsRogueErase_Object = MibScalar
ccRapResultsRogueErase = _CcRapResultsRogueErase_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 2, 3),
    _CcRapResultsRogueErase_Type()
)
ccRapResultsRogueErase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapResultsRogueErase.setStatus("current")
_CcRapLocate_ObjectIdentity = ObjectIdentity
ccRapLocate = _CcRapLocate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 4)
)
_CcRapPortalResults_ObjectIdentity = ObjectIdentity
ccRapPortalResults = _CcRapPortalResults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 4, 1)
)
_CcRapPortalResultsApMac_Type = PhysAddress
_CcRapPortalResultsApMac_Object = MibScalar
ccRapPortalResultsApMac = _CcRapPortalResultsApMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 4, 1, 1),
    _CcRapPortalResultsApMac_Type()
)
ccRapPortalResultsApMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapPortalResultsApMac.setStatus("current")
_CcRapPortalResultsApEssid_Type = DisplayString
_CcRapPortalResultsApEssid_Object = MibScalar
ccRapPortalResultsApEssid = _CcRapPortalResultsApEssid_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 4, 1, 2),
    _CcRapPortalResultsApEssid_Type()
)
ccRapPortalResultsApEssid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapPortalResultsApEssid.setStatus("current")
_CcRapPortalResultsInProcess_Type = DoActionShowProgress
_CcRapPortalResultsInProcess_Object = MibScalar
ccRapPortalResultsInProcess = _CcRapPortalResultsInProcess_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 4, 1, 3),
    _CcRapPortalResultsInProcess_Type()
)
ccRapPortalResultsInProcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapPortalResultsInProcess.setStatus("current")
_CcRapPortalResultsTable_Object = MibTable
ccRapPortalResultsTable = _CcRapPortalResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 4, 1, 4)
)
if mibBuilder.loadTexts:
    ccRapPortalResultsTable.setStatus("current")
_CcRapPortalResultsEntry_Object = MibTableRow
ccRapPortalResultsEntry = _CcRapPortalResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 4, 1, 4, 1)
)
ccRapPortalResultsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccRapPortalResultsIndex"),
)
if mibBuilder.loadTexts:
    ccRapPortalResultsEntry.setStatus("current")


class _CcRapPortalResultsIndex_Type(Unsigned32):
    """Custom type ccRapPortalResultsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000000),
    )


_CcRapPortalResultsIndex_Type.__name__ = "Unsigned32"
_CcRapPortalResultsIndex_Object = MibTableColumn
ccRapPortalResultsIndex = _CcRapPortalResultsIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 4, 1, 4, 1, 1),
    _CcRapPortalResultsIndex_Type()
)
ccRapPortalResultsIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccRapPortalResultsIndex.setStatus("current")
_CcRapPortalResultsPortalMac_Type = PhysAddress
_CcRapPortalResultsPortalMac_Object = MibTableColumn
ccRapPortalResultsPortalMac = _CcRapPortalResultsPortalMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 4, 1, 4, 1, 2),
    _CcRapPortalResultsPortalMac_Type()
)
ccRapPortalResultsPortalMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapPortalResultsPortalMac.setStatus("current")
_CcRapPortalResultsRssi_Type = Integer32
_CcRapPortalResultsRssi_Object = MibTableColumn
ccRapPortalResultsRssi = _CcRapPortalResultsRssi_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 4, 1, 4, 1, 3),
    _CcRapPortalResultsRssi_Type()
)
ccRapPortalResultsRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapPortalResultsRssi.setStatus("current")
_CcRapPollOneMu_ObjectIdentity = ObjectIdentity
ccRapPollOneMu = _CcRapPollOneMu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 4, 2)
)
_CcRapPollOneMuMac_Type = PhysAddress
_CcRapPollOneMuMac_Object = MibScalar
ccRapPollOneMuMac = _CcRapPollOneMuMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 4, 2, 1),
    _CcRapPollOneMuMac_Type()
)
ccRapPollOneMuMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapPollOneMuMac.setStatus("current")
_CcRapPollOneMuInProcess_Type = DoActionShowProgress
_CcRapPollOneMuInProcess_Object = MibScalar
ccRapPollOneMuInProcess = _CcRapPollOneMuInProcess_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 4, 2, 2),
    _CcRapPollOneMuInProcess_Type()
)
ccRapPollOneMuInProcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRapPollOneMuInProcess.setStatus("current")


class _CcRapPollOneMuStatus_Type(Integer32):
    """Custom type ccRapPollOneMuStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAssociated", 3),
          ("notSymbolRogueEnabled", 1),
          ("symbolRogueEnabled", 2))
    )


_CcRapPollOneMuStatus_Type.__name__ = "Integer32"
_CcRapPollOneMuStatus_Object = MibScalar
ccRapPollOneMuStatus = _CcRapPollOneMuStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 4, 2, 3),
    _CcRapPollOneMuStatus_Type()
)
ccRapPollOneMuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapPollOneMuStatus.setStatus("current")
_CcRapPollOneMuResultsTable_Object = MibTable
ccRapPollOneMuResultsTable = _CcRapPollOneMuResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 4, 2, 4)
)
if mibBuilder.loadTexts:
    ccRapPollOneMuResultsTable.setStatus("current")
_CcRapPollOneMuResultsEntry_Object = MibTableRow
ccRapPollOneMuResultsEntry = _CcRapPollOneMuResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 4, 2, 4, 1)
)
ccRapPollOneMuResultsEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccRapPollOneMuResultsIndex"),
)
if mibBuilder.loadTexts:
    ccRapPollOneMuResultsEntry.setStatus("current")


class _CcRapPollOneMuResultsIndex_Type(Unsigned32):
    """Custom type ccRapPollOneMuResultsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000000),
    )


_CcRapPollOneMuResultsIndex_Type.__name__ = "Unsigned32"
_CcRapPollOneMuResultsIndex_Object = MibTableColumn
ccRapPollOneMuResultsIndex = _CcRapPollOneMuResultsIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 4, 2, 4, 1, 1),
    _CcRapPollOneMuResultsIndex_Type()
)
ccRapPollOneMuResultsIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccRapPollOneMuResultsIndex.setStatus("current")
_CcRapPollOneMuResultsRssi_Type = Integer32
_CcRapPollOneMuResultsRssi_Object = MibTableColumn
ccRapPollOneMuResultsRssi = _CcRapPollOneMuResultsRssi_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 4, 2, 4, 1, 2),
    _CcRapPollOneMuResultsRssi_Type()
)
ccRapPollOneMuResultsRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapPollOneMuResultsRssi.setStatus("current")
_CcRapPollOneMuResultsEssid_Type = DisplayString
_CcRapPollOneMuResultsEssid_Object = MibTableColumn
ccRapPollOneMuResultsEssid = _CcRapPollOneMuResultsEssid_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 4, 2, 4, 1, 3),
    _CcRapPollOneMuResultsEssid_Type()
)
ccRapPollOneMuResultsEssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapPollOneMuResultsEssid.setStatus("current")
_CcRapPollOneMuResultsApMac_Type = PhysAddress
_CcRapPollOneMuResultsApMac_Object = MibTableColumn
ccRapPollOneMuResultsApMac = _CcRapPollOneMuResultsApMac_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 4, 2, 4, 1, 4),
    _CcRapPollOneMuResultsApMac_Type()
)
ccRapPollOneMuResultsApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRapPollOneMuResultsApMac.setStatus("current")
_CcRadiusServer_ObjectIdentity = ObjectIdentity
ccRadiusServer = _CcRadiusServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8)
)
_CcRadius_ObjectIdentity = ObjectIdentity
ccRadius = _CcRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 1)
)


class _CcRadiusDataSource_Type(Integer32):
    """Custom type ccRadiusDataSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ldap", 2),
          ("local", 1))
    )


_CcRadiusDataSource_Type.__name__ = "Integer32"
_CcRadiusDataSource_Object = MibScalar
ccRadiusDataSource = _CcRadiusDataSource_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 1, 1),
    _CcRadiusDataSource_Type()
)
ccRadiusDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusDataSource.setStatus("current")


class _CcRadiusDefaultEapType_Type(Integer32):
    """Custom type ccRadiusDefaultEapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("peap", 2),
          ("ttls", 1))
    )


_CcRadiusDefaultEapType_Type.__name__ = "Integer32"
_CcRadiusDefaultEapType_Object = MibScalar
ccRadiusDefaultEapType = _CcRadiusDefaultEapType_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 1, 2),
    _CcRadiusDefaultEapType_Type()
)
ccRadiusDefaultEapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusDefaultEapType.setStatus("current")


class _CcRadiusAuthTypePeap_Type(Integer32):
    """Custom type ccRadiusAuthTypePeap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gtc", 1),
          ("msChap2", 2))
    )


_CcRadiusAuthTypePeap_Type.__name__ = "Integer32"
_CcRadiusAuthTypePeap_Object = MibScalar
ccRadiusAuthTypePeap = _CcRadiusAuthTypePeap_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 1, 4),
    _CcRadiusAuthTypePeap_Type()
)
ccRadiusAuthTypePeap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusAuthTypePeap.setStatus("current")


class _CcRadiusAuthTypeTtls_Type(Integer32):
    """Custom type ccRadiusAuthTypeTtls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("msChap2", 3),
          ("pap", 2))
    )


_CcRadiusAuthTypeTtls_Type.__name__ = "Integer32"
_CcRadiusAuthTypeTtls_Object = MibScalar
ccRadiusAuthTypeTtls = _CcRadiusAuthTypeTtls_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 1, 5),
    _CcRadiusAuthTypeTtls_Type()
)
ccRadiusAuthTypeTtls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusAuthTypeTtls.setStatus("current")


class _CcRadiusServerCertificate_Type(DisplayString):
    """Custom type ccRadiusServerCertificate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CcRadiusServerCertificate_Type.__name__ = "DisplayString"
_CcRadiusServerCertificate_Object = MibScalar
ccRadiusServerCertificate = _CcRadiusServerCertificate_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 1, 6),
    _CcRadiusServerCertificate_Type()
)
ccRadiusServerCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusServerCertificate.setStatus("current")


class _CcRadiusCACertificate_Type(DisplayString):
    """Custom type ccRadiusCACertificate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CcRadiusCACertificate_Type.__name__ = "DisplayString"
_CcRadiusCACertificate_Object = MibScalar
ccRadiusCACertificate = _CcRadiusCACertificate_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 1, 7),
    _CcRadiusCACertificate_Type()
)
ccRadiusCACertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusCACertificate.setStatus("current")
_CcRadiusClientAuthTable_Object = MibTable
ccRadiusClientAuthTable = _CcRadiusClientAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 1, 8)
)
if mibBuilder.loadTexts:
    ccRadiusClientAuthTable.setStatus("current")
_CcRadiusClientAuthEntry_Object = MibTableRow
ccRadiusClientAuthEntry = _CcRadiusClientAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 1, 8, 1)
)
ccRadiusClientAuthEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccRadiusClientAuthIndex"),
)
if mibBuilder.loadTexts:
    ccRadiusClientAuthEntry.setStatus("current")


class _CcRadiusClientAuthIndex_Type(Unsigned32):
    """Custom type ccRadiusClientAuthIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcRadiusClientAuthIndex_Type.__name__ = "Unsigned32"
_CcRadiusClientAuthIndex_Object = MibTableColumn
ccRadiusClientAuthIndex = _CcRadiusClientAuthIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 1, 8, 1, 1),
    _CcRadiusClientAuthIndex_Type()
)
ccRadiusClientAuthIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccRadiusClientAuthIndex.setStatus("current")
_CcRadiusClientAuthIpAddr_Type = IpAddress
_CcRadiusClientAuthIpAddr_Object = MibTableColumn
ccRadiusClientAuthIpAddr = _CcRadiusClientAuthIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 1, 8, 1, 2),
    _CcRadiusClientAuthIpAddr_Type()
)
ccRadiusClientAuthIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusClientAuthIpAddr.setStatus("current")
_CcRadiusClientAuthMask_Type = IpAddress
_CcRadiusClientAuthMask_Object = MibTableColumn
ccRadiusClientAuthMask = _CcRadiusClientAuthMask_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 1, 8, 1, 3),
    _CcRadiusClientAuthMask_Type()
)
ccRadiusClientAuthMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusClientAuthMask.setStatus("current")
_CcRadiusClientAuthSharedSecret_Type = Password
_CcRadiusClientAuthSharedSecret_Object = MibTableColumn
ccRadiusClientAuthSharedSecret = _CcRadiusClientAuthSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 1, 8, 1, 4),
    _CcRadiusClientAuthSharedSecret_Type()
)
ccRadiusClientAuthSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusClientAuthSharedSecret.setStatus("current")
_CcRadiusClientAuthRowStatus_Type = AbbrevRowStatus
_CcRadiusClientAuthRowStatus_Object = MibTableColumn
ccRadiusClientAuthRowStatus = _CcRadiusClientAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 1, 8, 1, 5),
    _CcRadiusClientAuthRowStatus_Type()
)
ccRadiusClientAuthRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusClientAuthRowStatus.setStatus("current")
_CcRadiusProxy_ObjectIdentity = ObjectIdentity
ccRadiusProxy = _CcRadiusProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 2)
)


class _CcRadiusProxyRetryCount_Type(Integer32):
    """Custom type ccRadiusProxyRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 6),
    )


_CcRadiusProxyRetryCount_Type.__name__ = "Integer32"
_CcRadiusProxyRetryCount_Object = MibScalar
ccRadiusProxyRetryCount = _CcRadiusProxyRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 2, 1),
    _CcRadiusProxyRetryCount_Type()
)
ccRadiusProxyRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusProxyRetryCount.setStatus("current")


class _CcRadiusProxyTimeout_Type(Integer32):
    """Custom type ccRadiusProxyTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10),
    )


_CcRadiusProxyTimeout_Type.__name__ = "Integer32"
_CcRadiusProxyTimeout_Object = MibScalar
ccRadiusProxyTimeout = _CcRadiusProxyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 2, 2),
    _CcRadiusProxyTimeout_Type()
)
ccRadiusProxyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusProxyTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ccRadiusProxyTimeout.setUnits("seconds")
_CcRadiusProxyServerTable_Object = MibTable
ccRadiusProxyServerTable = _CcRadiusProxyServerTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 2, 3)
)
if mibBuilder.loadTexts:
    ccRadiusProxyServerTable.setStatus("current")
_CcRadiusProxyServerEntry_Object = MibTableRow
ccRadiusProxyServerEntry = _CcRadiusProxyServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 2, 3, 1)
)
ccRadiusProxyServerEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccRadiusProxyServerIndex"),
)
if mibBuilder.loadTexts:
    ccRadiusProxyServerEntry.setStatus("current")


class _CcRadiusProxyServerIndex_Type(Unsigned32):
    """Custom type ccRadiusProxyServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_CcRadiusProxyServerIndex_Type.__name__ = "Unsigned32"
_CcRadiusProxyServerIndex_Object = MibTableColumn
ccRadiusProxyServerIndex = _CcRadiusProxyServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 2, 3, 1, 1),
    _CcRadiusProxyServerIndex_Type()
)
ccRadiusProxyServerIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccRadiusProxyServerIndex.setStatus("current")


class _CcRadiusProxyServerPrefixOrSuffix_Type(DisplayString):
    """Custom type ccRadiusProxyServerPrefixOrSuffix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_CcRadiusProxyServerPrefixOrSuffix_Type.__name__ = "DisplayString"
_CcRadiusProxyServerPrefixOrSuffix_Object = MibTableColumn
ccRadiusProxyServerPrefixOrSuffix = _CcRadiusProxyServerPrefixOrSuffix_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 2, 3, 1, 2),
    _CcRadiusProxyServerPrefixOrSuffix_Type()
)
ccRadiusProxyServerPrefixOrSuffix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusProxyServerPrefixOrSuffix.setStatus("current")
_CcRadiusProxyServerIp_Type = IpAddress
_CcRadiusProxyServerIp_Object = MibTableColumn
ccRadiusProxyServerIp = _CcRadiusProxyServerIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 2, 3, 1, 3),
    _CcRadiusProxyServerIp_Type()
)
ccRadiusProxyServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusProxyServerIp.setStatus("current")
_CcRadiusProxyServerPort_Type = Integer32
_CcRadiusProxyServerPort_Object = MibTableColumn
ccRadiusProxyServerPort = _CcRadiusProxyServerPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 2, 3, 1, 4),
    _CcRadiusProxyServerPort_Type()
)
ccRadiusProxyServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusProxyServerPort.setStatus("current")
_CcRadiusProxyServerSharedSecret_Type = Password
_CcRadiusProxyServerSharedSecret_Object = MibTableColumn
ccRadiusProxyServerSharedSecret = _CcRadiusProxyServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 2, 3, 1, 5),
    _CcRadiusProxyServerSharedSecret_Type()
)
ccRadiusProxyServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusProxyServerSharedSecret.setStatus("current")
_CcRadiusProxyServerRowStatus_Type = AbbrevRowStatus
_CcRadiusProxyServerRowStatus_Object = MibTableColumn
ccRadiusProxyServerRowStatus = _CcRadiusProxyServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 2, 3, 1, 6),
    _CcRadiusProxyServerRowStatus_Type()
)
ccRadiusProxyServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusProxyServerRowStatus.setStatus("current")
_CcRadiusLdap_ObjectIdentity = ObjectIdentity
ccRadiusLdap = _CcRadiusLdap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 3)
)
_CcRadiusLdapServerIp_Type = IpAddress
_CcRadiusLdapServerIp_Object = MibScalar
ccRadiusLdapServerIp = _CcRadiusLdapServerIp_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 3, 1),
    _CcRadiusLdapServerIp_Type()
)
ccRadiusLdapServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdapServerIp.setStatus("current")


class _CcRadiusLdapServerPort_Type(Integer32):
    """Custom type ccRadiusLdapServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_CcRadiusLdapServerPort_Type.__name__ = "Integer32"
_CcRadiusLdapServerPort_Object = MibScalar
ccRadiusLdapServerPort = _CcRadiusLdapServerPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 3, 2),
    _CcRadiusLdapServerPort_Type()
)
ccRadiusLdapServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdapServerPort.setStatus("current")


class _CcRadiusLdapLoginAttribute_Type(DisplayString):
    """Custom type ccRadiusLdapLoginAttribute based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CcRadiusLdapLoginAttribute_Type.__name__ = "DisplayString"
_CcRadiusLdapLoginAttribute_Object = MibScalar
ccRadiusLdapLoginAttribute = _CcRadiusLdapLoginAttribute_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 3, 3),
    _CcRadiusLdapLoginAttribute_Type()
)
ccRadiusLdapLoginAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdapLoginAttribute.setStatus("current")
_CcRadiusLdapPasswordAttribute_Type = DisplayString
_CcRadiusLdapPasswordAttribute_Object = MibScalar
ccRadiusLdapPasswordAttribute = _CcRadiusLdapPasswordAttribute_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 3, 4),
    _CcRadiusLdapPasswordAttribute_Type()
)
ccRadiusLdapPasswordAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdapPasswordAttribute.setStatus("current")


class _CcRadiusLdapBindDistinguishedName_Type(DisplayString):
    """Custom type ccRadiusLdapBindDistinguishedName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcRadiusLdapBindDistinguishedName_Type.__name__ = "DisplayString"
_CcRadiusLdapBindDistinguishedName_Object = MibScalar
ccRadiusLdapBindDistinguishedName = _CcRadiusLdapBindDistinguishedName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 3, 5),
    _CcRadiusLdapBindDistinguishedName_Type()
)
ccRadiusLdapBindDistinguishedName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdapBindDistinguishedName.setStatus("current")
_CcRadiusLdapBindDistinguishedPassword_Type = Password
_CcRadiusLdapBindDistinguishedPassword_Object = MibScalar
ccRadiusLdapBindDistinguishedPassword = _CcRadiusLdapBindDistinguishedPassword_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 3, 6),
    _CcRadiusLdapBindDistinguishedPassword_Type()
)
ccRadiusLdapBindDistinguishedPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdapBindDistinguishedPassword.setStatus("current")


class _CcRadiusLdapBaseDistinguishedName_Type(DisplayString):
    """Custom type ccRadiusLdapBaseDistinguishedName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcRadiusLdapBaseDistinguishedName_Type.__name__ = "DisplayString"
_CcRadiusLdapBaseDistinguishedName_Object = MibScalar
ccRadiusLdapBaseDistinguishedName = _CcRadiusLdapBaseDistinguishedName_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 3, 7),
    _CcRadiusLdapBaseDistinguishedName_Type()
)
ccRadiusLdapBaseDistinguishedName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdapBaseDistinguishedName.setStatus("current")


class _CcRadiusLdapGroupAttribute_Type(DisplayString):
    """Custom type ccRadiusLdapGroupAttribute based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CcRadiusLdapGroupAttribute_Type.__name__ = "DisplayString"
_CcRadiusLdapGroupAttribute_Object = MibScalar
ccRadiusLdapGroupAttribute = _CcRadiusLdapGroupAttribute_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 3, 8),
    _CcRadiusLdapGroupAttribute_Type()
)
ccRadiusLdapGroupAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdapGroupAttribute.setStatus("current")


class _CcRadiusLdapGroupFilter_Type(DisplayString):
    """Custom type ccRadiusLdapGroupFilter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcRadiusLdapGroupFilter_Type.__name__ = "DisplayString"
_CcRadiusLdapGroupFilter_Object = MibScalar
ccRadiusLdapGroupFilter = _CcRadiusLdapGroupFilter_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 3, 9),
    _CcRadiusLdapGroupFilter_Type()
)
ccRadiusLdapGroupFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdapGroupFilter.setStatus("current")


class _CcRadiusLdapGroupMembershipAttribute_Type(DisplayString):
    """Custom type ccRadiusLdapGroupMembershipAttribute based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CcRadiusLdapGroupMembershipAttribute_Type.__name__ = "DisplayString"
_CcRadiusLdapGroupMembershipAttribute_Object = MibScalar
ccRadiusLdapGroupMembershipAttribute = _CcRadiusLdapGroupMembershipAttribute_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 3, 10),
    _CcRadiusLdapGroupMembershipAttribute_Type()
)
ccRadiusLdapGroupMembershipAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusLdapGroupMembershipAttribute.setStatus("current")
_CcRadiusUsers_ObjectIdentity = ObjectIdentity
ccRadiusUsers = _CcRadiusUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 4)
)
_CcRadiusUsersGroupTable_Object = MibTable
ccRadiusUsersGroupTable = _CcRadiusUsersGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 4, 1)
)
if mibBuilder.loadTexts:
    ccRadiusUsersGroupTable.setStatus("obsolete")
_CcRadiusUsersGroupEntry_Object = MibTableRow
ccRadiusUsersGroupEntry = _CcRadiusUsersGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 4, 1, 1)
)
ccRadiusUsersGroupEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccRadiusUsersGroup"),
)
if mibBuilder.loadTexts:
    ccRadiusUsersGroupEntry.setStatus("obsolete")


class _CcRadiusUsersGroup_Type(DisplayString):
    """Custom type ccRadiusUsersGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_CcRadiusUsersGroup_Type.__name__ = "DisplayString"
_CcRadiusUsersGroup_Object = MibTableColumn
ccRadiusUsersGroup = _CcRadiusUsersGroup_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 4, 1, 1, 1),
    _CcRadiusUsersGroup_Type()
)
ccRadiusUsersGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccRadiusUsersGroup.setStatus("obsolete")
_CcRadiusUsersGroupRowStatus_Type = AbbrevRowStatus
_CcRadiusUsersGroupRowStatus_Object = MibTableColumn
ccRadiusUsersGroupRowStatus = _CcRadiusUsersGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 4, 1, 1, 2),
    _CcRadiusUsersGroupRowStatus_Type()
)
ccRadiusUsersGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccRadiusUsersGroupRowStatus.setStatus("obsolete")
_CcRadiusUsersGroupId_Type = Integer32
_CcRadiusUsersGroupId_Object = MibTableColumn
ccRadiusUsersGroupId = _CcRadiusUsersGroupId_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 4, 1, 1, 3),
    _CcRadiusUsersGroupId_Type()
)
ccRadiusUsersGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccRadiusUsersGroupId.setStatus("obsolete")
_CcRadiusUsersTable_Object = MibTable
ccRadiusUsersTable = _CcRadiusUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 4, 2)
)
if mibBuilder.loadTexts:
    ccRadiusUsersTable.setStatus("current")
_CcRadiusUsersEntry_Object = MibTableRow
ccRadiusUsersEntry = _CcRadiusUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 4, 2, 1)
)
ccRadiusUsersEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccRadiusUsersId"),
)
if mibBuilder.loadTexts:
    ccRadiusUsersEntry.setStatus("current")


class _CcRadiusUsersId_Type(DisplayString):
    """Custom type ccRadiusUsersId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_CcRadiusUsersId_Type.__name__ = "DisplayString"
_CcRadiusUsersId_Object = MibTableColumn
ccRadiusUsersId = _CcRadiusUsersId_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 4, 2, 1, 1),
    _CcRadiusUsersId_Type()
)
ccRadiusUsersId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccRadiusUsersId.setStatus("current")


class _CcRadiusUsersPassword_Type(Password):
    """Custom type ccRadiusUsersPassword based on Password"""
    subtypeSpec = Password.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_CcRadiusUsersPassword_Type.__name__ = "Password"
_CcRadiusUsersPassword_Object = MibTableColumn
ccRadiusUsersPassword = _CcRadiusUsersPassword_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 4, 2, 1, 2),
    _CcRadiusUsersPassword_Type()
)
ccRadiusUsersPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccRadiusUsersPassword.setStatus("current")


class _CcRadiusUsersGroups_Type(Bits):
    """Custom type ccRadiusUsersGroups based on Bits"""
    namedValues = NamedValues(
        *(("group1", 1),
          ("group10", 10),
          ("group2", 2),
          ("group3", 3),
          ("group4", 4),
          ("group5", 5),
          ("group6", 6),
          ("group7", 7),
          ("group8", 8),
          ("group9", 9),
          ("null", 0))
    )

_CcRadiusUsersGroups_Type.__name__ = "Bits"
_CcRadiusUsersGroups_Object = MibTableColumn
ccRadiusUsersGroups = _CcRadiusUsersGroups_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 4, 2, 1, 3),
    _CcRadiusUsersGroups_Type()
)
ccRadiusUsersGroups.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccRadiusUsersGroups.setStatus("current")
_CcRadiusUsersRowStatus_Type = AbbrevRowStatus
_CcRadiusUsersRowStatus_Object = MibTableColumn
ccRadiusUsersRowStatus = _CcRadiusUsersRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 4, 2, 1, 4),
    _CcRadiusUsersRowStatus_Type()
)
ccRadiusUsersRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccRadiusUsersRowStatus.setStatus("current")
_CcRadiusAccess_ObjectIdentity = ObjectIdentity
ccRadiusAccess = _CcRadiusAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 5)
)
_CcRadiusAccessTable_Object = MibTable
ccRadiusAccessTable = _CcRadiusAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 5, 1)
)
if mibBuilder.loadTexts:
    ccRadiusAccessTable.setStatus("obsolete")
_CcRadiusAccessEntry_Object = MibTableRow
ccRadiusAccessEntry = _CcRadiusAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 5, 1, 1)
)
ccRadiusAccessEntry.setIndexNames(
    (0, "SYMBOL-CC-WS2000-MIB", "ccRadiusUsersGroup"),
)
if mibBuilder.loadTexts:
    ccRadiusAccessEntry.setStatus("obsolete")


class _CcRadiusAccessWlanPtrs_Type(Bits):
    """Custom type ccRadiusAccessWlanPtrs based on Bits"""
    namedValues = NamedValues(
        *(("null", 0),
          ("wlan1", 1),
          ("wlan2", 2),
          ("wlan3", 3),
          ("wlan4", 4))
    )

_CcRadiusAccessWlanPtrs_Type.__name__ = "Bits"
_CcRadiusAccessWlanPtrs_Object = MibTableColumn
ccRadiusAccessWlanPtrs = _CcRadiusAccessWlanPtrs_Object(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 8, 5, 1, 1, 2),
    _CcRadiusAccessWlanPtrs_Type()
)
ccRadiusAccessWlanPtrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccRadiusAccessWlanPtrs.setStatus("obsolete")
_CcGroups_ObjectIdentity = ObjectIdentity
ccGroups = _CcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 1000)
)
_CcGroupsV1dot0_ObjectIdentity = ObjectIdentity
ccGroupsV1dot0 = _CcGroupsV1dot0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 1000, 1)
)
_CcGroupsV1dot5_ObjectIdentity = ObjectIdentity
ccGroupsV1dot5 = _CcGroupsV1dot5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 1000, 2)
)
_CcGroupsV2dot0_ObjectIdentity = ObjectIdentity
ccGroupsV2dot0 = _CcGroupsV2dot0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 1000, 3)
)
ccWanVpnEntry.registerAugmentions(
    ("SYMBOL-CC-WS2000-MIB",
     "ccWanVpnKeyManualEntry")
)
ccWanVpnKeyManualEntry.setIndexNames(*ccWanVpnEntry.getIndexNames())
ccWanVpnEntry.registerAugmentions(
    ("SYMBOL-CC-WS2000-MIB",
     "ccWanVpnKeyAutoEntry")
)
ccWanVpnKeyAutoEntry.setIndexNames(*ccWanVpnEntry.getIndexNames())

# Managed Objects groups

ccAdminGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 1000, 1, 1)
)
ccAdminGroup.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccInfoSerialNumber"),
        ("SYMBOL-CC-WS2000-MIB", "ccResetFactory"),
        ("SYMBOL-CC-WS2000-MIB", "ccResetSwitch"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFwOperation"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFwInterface"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFwServerPath"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFwServerFilename"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFwStart"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFwResult"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFwSuccess"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadCfgOperation"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadCfgServerPath"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadCfgServerFilename"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadCfgStart"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadCfgOperationsDone"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadCfgResult"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadCfgSuccess"),
        ("SYMBOL-CC-WS2000-MIB", "ccCfgHistChangeCount"),
        ("SYMBOL-CC-WS2000-MIB", "ccCfgHistChangeTime"),
        ("SYMBOL-CC-WS2000-MIB", "ccCfgHistSemaphore"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpLastDeniedIpAddr"),
        ("SYMBOL-CC-WS2000-MIB", "ccSysDNSRelayMode"),
        ("SYMBOL-CC-WS2000-MIB", "ccApSslv2Mode"),
        ("SYMBOL-CC-WS2000-MIB", "ccApSshv1Mode"),
        ("SYMBOL-CC-WS2000-MIB", "ccApSslWeakCipherSupport"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpAclViolations"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadServerIpAddr"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFtpUsername"))
)
if mibBuilder.loadTexts:
    ccAdminGroup.setStatus("current")

ccApGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 1000, 1, 3)
)
ccApGroup.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccApIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccApNicMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccApModelNumber"),
        ("SYMBOL-CC-WS2000-MIB", "ccApSerialNumber"),
        ("SYMBOL-CC-WS2000-MIB", "ccApPcbRevision"),
        ("SYMBOL-CC-WS2000-MIB", "ccApBootLoaderRev"),
        ("SYMBOL-CC-WS2000-MIB", "ccApWispVersion"),
        ("SYMBOL-CC-WS2000-MIB", "ccApRuntimeFwVersion"),
        ("SYMBOL-CC-WS2000-MIB", "ccApNumPortals"),
        ("SYMBOL-CC-WS2000-MIB", "ccApPointersToPortals"))
)
if mibBuilder.loadTexts:
    ccApGroup.setStatus("current")

ccPortalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 1000, 1, 4)
)
ccPortalGroup.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccPortalIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalPointerToAp"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalPointersToWlans"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalOptions"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalNumberOfEss"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalNumberOfBss"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalAssociatedMus"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalChannel"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPowerLevel"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalLastMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalLastReason"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalName"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalLocation"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalLastAdoption"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRadioType"))
)
if mibBuilder.loadTexts:
    ccPortalGroup.setStatus("current")

ccAssociationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 1000, 1, 5)
)
ccAssociationGroup.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccAssociationFirstAssociate"),
        ("SYMBOL-CC-WS2000-MIB", "ccAssociationLastAssociate"),
        ("SYMBOL-CC-WS2000-MIB", "ccAssociationCountAssociates"))
)
if mibBuilder.loadTexts:
    ccAssociationGroup.setStatus("current")

ccMuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 1000, 1, 6)
)
ccMuGroup.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccMuMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuWlanIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuWlanName"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuPortalIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuPortalMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSymbolRogueApEna"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuIpAddr"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuType"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRadioType"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSupportedRates"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuPowerMode"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuAuthenticationMethod"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuEncryptionMethod"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxUndecryptablePkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxRssiNumPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxRssiSum"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxRssiSumSquares"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxRssiMostRecent"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuLastActivity"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt1Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt2Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt5pt5Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt6Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt9Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt11Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt12Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt18Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt22Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt24Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt36Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt48Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt54Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt1Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt2Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt5pt5Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt6Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt9Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt11Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt12Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt18Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt22Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt24Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt36Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt48Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt54Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt1Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt2Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt5pt5Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt6Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt9Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt11Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt12Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt18Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt22Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt24Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt36Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt48Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt54Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt1Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt2Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt5pt5Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt6Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt9Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt11Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt12Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt18Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt22Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt24Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt36Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt48Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt54Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries01"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries02"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries03"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries04"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries05"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries06"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries07"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries08"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries09"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries10"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries11"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries12"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries13"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries14"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries15"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesNone"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesFailed"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesTotal"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuLastPortal"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesMostRecent"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuLastMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuLastReason"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuIsDataReady"))
)
if mibBuilder.loadTexts:
    ccMuGroup.setStatus("current")

ccGroupsV1dot5variables = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 1000, 2, 1)
)
ccGroupsV1dot5variables.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccInfoSerialNumber"),
        ("SYMBOL-CC-WS2000-MIB", "ccInfoCountrySelection"),
        ("SYMBOL-CC-WS2000-MIB", "ccIdHwVersion"),
        ("SYMBOL-CC-WS2000-MIB", "ccIdFwVersion"),
        ("SYMBOL-CC-WS2000-MIB", "ccIdSwVersion"),
        ("SYMBOL-CC-WS2000-MIB", "ccIdMibVersion"),
        ("SYMBOL-CC-WS2000-MIB", "ccIdCliVersion"),
        ("SYMBOL-CC-WS2000-MIB", "ccIdXmlVersion"),
        ("SYMBOL-CC-WS2000-MIB", "ccIdSerialNumber"),
        ("SYMBOL-CC-WS2000-MIB", "ccResetFactory"),
        ("SYMBOL-CC-WS2000-MIB", "ccResetSwitch"),
        ("SYMBOL-CC-WS2000-MIB", "ccResetFactoryExceptIpSnmp"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFwOperation"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFwInterface"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFwServerPath"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFwServerFilename"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFwStart"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFwResult"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFwSuccess"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadCfgOperation"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadCfgServerPath"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadCfgServerFilename"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadCfgStart"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadCfgOperationsDone"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadCfgResult"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadCfgSuccess"),
        ("SYMBOL-CC-WS2000-MIB", "ccCfgHistChangeCount"),
        ("SYMBOL-CC-WS2000-MIB", "ccCfgHistChangeTime"),
        ("SYMBOL-CC-WS2000-MIB", "ccCfgHistSemaphore"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadServerIpAddr"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFtpUsername"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFtpPassword"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpAclViolations"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpLastDeniedIpAddr"),
        ("SYMBOL-CC-WS2000-MIB", "ccCompactFlashCapacity"),
        ("SYMBOL-CC-WS2000-MIB", "ccCompactFlashUsed"),
        ("SYMBOL-CC-WS2000-MIB", "ccSumStatsShortWindow"),
        ("SYMBOL-CC-WS2000-MIB", "ccSumStatsShortUpdateInterval"),
        ("SYMBOL-CC-WS2000-MIB", "ccSumStatsLongWindow"),
        ("SYMBOL-CC-WS2000-MIB", "ccSumStatsLongUpdateInterval"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlCfAlmostFullThreshold"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlFirewallUnderAttackDescription"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlFirewallUnderAttackRateLimit"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlRadarDetectedPortalMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlRadarDetectedChannel"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsDescr"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsUnits"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsCanBeSetMu"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsThresholdMu"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsCanBeSetPortal"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsThresholdPortals"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsCanBeSetWlan"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsThresholdWlans"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsCanBeSetSwitch"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsThresholdSwitch"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsMinPktsForTrap"),
        ("SYMBOL-CC-WS2000-MIB", "ccApIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccApNicMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccApModelNumber"),
        ("SYMBOL-CC-WS2000-MIB", "ccApSerialNumber"),
        ("SYMBOL-CC-WS2000-MIB", "ccApPcbRevision"),
        ("SYMBOL-CC-WS2000-MIB", "ccApBootLoaderRev"),
        ("SYMBOL-CC-WS2000-MIB", "ccApWispVersion"),
        ("SYMBOL-CC-WS2000-MIB", "ccApRuntimeFwVersion"),
        ("SYMBOL-CC-WS2000-MIB", "ccApNumPortals"),
        ("SYMBOL-CC-WS2000-MIB", "ccApPointersToPortals"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalPointerToAp"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalPointersToWlans"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalName"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalLocation"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalOptions"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalNumberOfEss"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalNumberOfBss"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalAssociatedMus"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRadioType"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalChannel"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPowerLevel"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalLastAdoption"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalState"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalLastMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalLastReason"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSystemStatsBeaconsTx"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSystemStatsBeaconsTxOctets"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSystemStatsProbeReqRx"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSystemStatsProbeReqRxOctets"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSystemStatsProbeRespRetriesNone"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSystemStatsProbeRespRetries1"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSystemStatsProbeRespRetries2"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSystemStatsProbeRespRetriesFailed"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSystemStatsProbeRespTxOctets"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPktsUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsNUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxOctetsUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsNUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxUndecryptablePkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalLastActivity"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsAt1Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsAt2Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsAt5pt5Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsAt6Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsAt9Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsAt11Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsAt12Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsAt18Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsAt22Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsAt24Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsAt36Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsAt48Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsAt54Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPktsAt1Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPktsAt2Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPktsAt5pt5Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPktsAt6Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPktsAt9Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPktsAt11Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPktsAt12Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPktsAt18Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPktsAt22Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPktsAt24Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPktsAt36Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPktsAt48Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPktsAt54Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsAt1Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsAt2Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsAt5pt5Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsAt6Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsAt9Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsAt11Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsAt12Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsAt18Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsAt22Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsAt24Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsAt36Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsAt48Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsAt54Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxOctetsAt1Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxOctetsAt2Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxOctetsAt5pt5Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxOctetsAt6Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxOctetsAt9Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxOctetsAt11Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxOctetsAt12Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxOctetsAt18Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxOctetsAt22Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxOctetsAt24Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxOctetsAt36Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxOctetsAt48Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxOctetsAt54Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPktsNone"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts01"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts02"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts03"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts04"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts05"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts06"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts07"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts08"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts09"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts10"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts11"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts12"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts13"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts14"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts15"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPktsFailed"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctetsNone"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets01"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets02"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets03"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets04"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets05"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets06"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets07"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets08"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets09"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets10"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets11"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets12"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets13"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets14"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets15"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctetsFailed"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsNumPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsSignalBest"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsSignalWorst"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsSignalSum"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsSignalSumSquares"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsSignalMostRecent"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsNoiseBest"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsNoiseWorst"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsNoiseSum"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsNoiseSumSquares"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsNoiseMostRecent"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsSnrBest"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsSnrWorst"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsSnrSum"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsSnrSumSquares"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsSnrMostRecent"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortTimestamp"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortNumPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortPktsPerSec100"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortPktsPerSecTx100"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortPktsPerSecRx100"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortThroughput"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortThroughputTx"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortThroughputRx"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortAvgBitSpeed"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortAvgMuSignal"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortAvgMuNoise"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortAvgMuSnr"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortPp10kNUcastPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortPp10kTxWithRetries"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortTxAvgRetries100"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortPp10kRxUndecrypt"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortTotalMus"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortPp10kRfUtil"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongTimestamp"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongNumPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongPktsPerSec100"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongPktsPerSecTx100"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongPktsPerSecRx100"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongThroughput"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongThroughputTx"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongThroughputRx"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongAvgBitSpeed"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongAvgMuSignal"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongAvgMuNoise"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongAvgMuSnr"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongPp10kNUcastPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongPp10kTxWithRetries"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongTxAvgRetries100"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongPp10kRxUndecrypt"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongTotalMus"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongPp10kRfUtil"),
        ("SYMBOL-CC-WS2000-MIB", "ccAssociationFirstAssociate"),
        ("SYMBOL-CC-WS2000-MIB", "ccAssociationLastAssociate"),
        ("SYMBOL-CC-WS2000-MIB", "ccAssociationCountAssociates"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuWlanIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuWlanName"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuIsDataReady"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuPortalIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuPortalMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSymbolRogueApEna"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuIpAddr"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuType"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRadioType"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSupportedRates"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuPowerMode"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuAuthenticationMethod"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuEncryptionMethod"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxUndecryptablePkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxRssiNumPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxRssiSum"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxRssiSumSquares"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxRssiMostRecent"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuLastActivity"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt1Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt2Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt5pt5Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt6Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt9Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt11Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt12Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt18Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt22Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt24Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt36Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt48Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt54Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt1Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt2Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt5pt5Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt6Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt9Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt11Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt12Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt18Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt22Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt24Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt36Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt48Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt54Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt1Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt2Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt5pt5Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt6Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt9Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt11Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt12Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt18Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt22Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt24Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt36Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt48Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt54Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt1Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt2Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt5pt5Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt6Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt9Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt11Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt12Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt18Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt22Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt24Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt36Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt48Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt54Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesNone"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries01"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries02"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries03"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries04"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries05"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries06"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries07"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries08"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries09"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries10"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries11"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries12"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries13"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries14"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries15"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesFailed"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesTotal"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesMostRecent"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuLastMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuLastReason"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuLastPortal"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctetsNone"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets01"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets02"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets03"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets04"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets05"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets06"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets07"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets08"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets09"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets10"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets11"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets12"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets13"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets14"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets15"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctetsFailed"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsNumPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsSignalBest"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsSignalWorst"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsSignalSum"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsSignalSumSquares"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsSignalMostRecent"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsNoiseBest"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsNoiseWorst"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsNoiseSum"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsNoiseSumSquares"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsNoiseMostRecent"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsSnrBest"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsSnrWorst"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsSnrSum"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsSnrSumSquares"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsSnrMostRecent"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortTimestamp"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortNumPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortPktsPerSec100"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortPktsPerSecTx100"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortPktsPerSecRx100"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortThroughput"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortThroughputTx"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortThroughputRx"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortAvgBitSpeed"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortAvgMuSignal"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortAvgMuNoise"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortAvgMuSnr"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortPp10kNUcastPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortPp10kTxWithRetries"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortTxAvgRetries100"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortPp10kRxUndecrypt"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongTimestamp"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongNumPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongPktsPerSec100"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongPktsPerSecTx100"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongPktsPerSecRx100"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongThroughput"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongThroughputTx"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongThroughputRx"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongAvgBitSpeed"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongAvgMuSignal"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongAvgMuNoise"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongAvgMuSnr"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongPp10kNUcastPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongPp10kTxWithRetries"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongTxAvgRetries100"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongPp10kRxUndecrypt"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanName"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanEssid"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSubnet"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanPortalsAdopted"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanEnable"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanDisallowMuToMu"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanVoicePrioritization"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAnswerBroadcastEss"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanMulticastAddr1"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanMulticastAddr2"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanMuAclDefault"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthentication"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanEncryption"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapReauthenticationEnable"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapReauthenticationPeriod"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapReauthenticationMaxRetries"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapRadius1Server"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapRadius1Port"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapRadius1SharedSecret"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapRadius2Server"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapRadius2Port"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapRadius2SharedSecret"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapMuQuietPeriod"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapMuTimeout"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapMuTxPeriod"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapMuMaxRetries"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapServerTimeout"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapServerMaxRetries"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthKerberosRealmName"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthKerberosUsername"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthKerberosPassword"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthKerberosKdcServerIp1"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthKerberosKdcPort1"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthKerberosKdcServerIp2"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthKerberosKdcPort2"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthKerberosKdcServerIpR"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthKerberosKdcPortR"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWepPassKey"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWepKey1"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWepKey2"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWepKey3"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWepKey4"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWepKeyToUse"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWpaBcastKeyRotation"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWpaKeyRotationInterval"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWpaKeyToUse"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWpaPassphrase"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWpaKey"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoKeyguardPasskey"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoKeyguardKey1"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoKeyguardKey2"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoKeyguardKey3"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoKeyguardKey4"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoKeyguardKeyToUse"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxPktsUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsNUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxOctetsUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsNUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxUndecryptablePkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanLastActivity"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsAt1Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsAt2Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsAt5pt5Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsAt6Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsAt9Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsAt11Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsAt12Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsAt18Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsAt22Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsAt24Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsAt36Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsAt48Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsAt54Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxPktsAt1Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxPktsAt2Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxPktsAt5pt5Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxPktsAt6Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxPktsAt9Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxPktsAt11Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxPktsAt12Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxPktsAt18Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxPktsAt22Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxPktsAt24Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxPktsAt36Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxPktsAt48Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxPktsAt54Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsAt1Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsAt2Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsAt5pt5Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsAt6Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsAt9Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsAt11Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsAt12Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsAt18Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsAt22Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsAt24Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsAt36Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsAt48Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsAt54Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxOctetsAt1Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxOctetsAt2Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxOctetsAt5pt5Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxOctetsAt6Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxOctetsAt9Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxOctetsAt11Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxOctetsAt12Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxOctetsAt18Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxOctetsAt22Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxOctetsAt24Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxOctetsAt36Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxOctetsAt48Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxOctetsAt54Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPktsNone"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts01"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts02"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts03"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts04"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts05"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts06"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts07"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts08"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts09"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts10"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts11"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts12"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts13"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts14"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts15"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPktsFailed"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctetsNone"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets01"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets02"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets03"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets04"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets05"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets06"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets07"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets08"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets09"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets10"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets11"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets12"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets13"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets14"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets15"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctetsFailed"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSigStatsNumPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSigStatsSignalBest"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSigStatsSignalWorst"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSigStatsSignalSum"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSigStatsSignalSumSquares"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSigStatsNoiseBest"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSigStatsNoiseWorst"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSigStatsNoiseSum"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSigStatsNoiseSumSquares"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSigStatsSnrBest"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSigStatsSnrWorst"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSigStatsSnrSum"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSigStatsSnrSumSquares"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortTimestamp"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortNumPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortPktsPerSec100"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortPktsPerSecTx100"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortPktsPerSecRx100"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortThroughput"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortThroughputTx"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortThroughputRx"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortAvgBitSpeed"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortAvgMuSignal"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortAvgMuNoise"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortAvgMuSnr"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortPp10kNUcastPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortPp10kTxWithRetries"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortTxAvgRetries100"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortPp10kRxUndecrypt"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortTotalMus"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongTimestamp"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongNumPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongPktsPerSec100"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongPktsPerSecTx100"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongPktsPerSecRx100"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongThroughput"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongThroughputTx"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongThroughputRx"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongAvgBitSpeed"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongAvgMuSignal"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongAvgMuNoise"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongAvgMuSnr"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongPp10kNUcastPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongPp10kTxWithRetries"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongTxAvgRetries100"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongPp10kRxUndecrypt"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongTotalMus"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanDhcpEnable"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanDhcpIpAddr"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanDhcpSubnetMask"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanDhcpDefaultGateway"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanDhcpPrimaryDnsServer"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanDhcpSecondaryDnsServer"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanSubnetMask"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanDefaultGateway"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanPrimaryDnsServer"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanSecondaryDnsServer"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanPppoeEnable"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanPppoeUsername"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanPppoePassword"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanPppoeKeepAlive"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanPppoeIdleTime"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanPppoeAuthType"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanIpAddrIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanIpAddrEnable"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanIpAddr"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanFirewallGlobalEnable"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanFirewallIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanFirewallDescription"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanFirewallAlwaysEnabled"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanFirewallEnable"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanFirewallMimeFloodMaxHeaderLength"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanFirewallMimeFloodMaxHeaders"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortType"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortPoeEquipped"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortStatus"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortDuplex"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalBackgroundNoiseNumSamples"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalBackgroundNoiseBest"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalBackgroundNoiseWorst"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalBackgroundNoiseSum"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalBackgroundNoiseSumSquares"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongPp10kDropped"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortPp10kDropped"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSystemStatsProbeRespRetries3OrMore"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortPp10kTxMaxRetries"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortSpeed"),
        ("SYMBOL-CC-WS2000-MIB", "ccResetStatCounters"))
)
if mibBuilder.loadTexts:
    ccGroupsV1dot5variables.setStatus("current")

ccGroupsV1dot5obsoleted = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 1000, 2, 2)
)
ccGroupsV1dot5obsoleted.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccLoadFtpPassword"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsNUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsNUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccResetMuCounters"))
)
if mibBuilder.loadTexts:
    ccGroupsV1dot5obsoleted.setStatus("obsolete")

ccGroupsV2dot0variables = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 1000, 3, 1)
)
ccGroupsV2dot0variables.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccInfoSerialNumber"),
        ("SYMBOL-CC-WS2000-MIB", "ccInfoCountrySelection"),
        ("SYMBOL-CC-WS2000-MIB", "ccIdHwVersion"),
        ("SYMBOL-CC-WS2000-MIB", "ccIdFwVersion"),
        ("SYMBOL-CC-WS2000-MIB", "ccIdSwVersion"),
        ("SYMBOL-CC-WS2000-MIB", "ccIdMibVersion"),
        ("SYMBOL-CC-WS2000-MIB", "ccIdCliVersion"),
        ("SYMBOL-CC-WS2000-MIB", "ccIdXmlVersion"),
        ("SYMBOL-CC-WS2000-MIB", "ccIdSerialNumber"),
        ("SYMBOL-CC-WS2000-MIB", "ccResetFactory"),
        ("SYMBOL-CC-WS2000-MIB", "ccResetSwitch"),
        ("SYMBOL-CC-WS2000-MIB", "ccResetFactoryExceptIpSnmp"),
        ("SYMBOL-CC-WS2000-MIB", "ccResetStatCounters"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFwOperation"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFwInterface"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFwServerPath"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFwServerFilename"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFwStart"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFwResult"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFwSuccess"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadCfgOperation"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadCfgServerPath"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadCfgServerFilename"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadCfgStart"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadCfgOperationsDone"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadCfgResult"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadCfgSuccess"),
        ("SYMBOL-CC-WS2000-MIB", "ccCfgHistChangeCount"),
        ("SYMBOL-CC-WS2000-MIB", "ccCfgHistChangeTime"),
        ("SYMBOL-CC-WS2000-MIB", "ccCfgHistSemaphore"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadServerIpAddr"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFtpUsername"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFtpPassword"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpAclViolations"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpLastDeniedIpAddr"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpAccessV12Index"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpAccessV12Community"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpAccessV12CustomOid"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpAccessV12OidLimit"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpAccessV12Access"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpAccessV12Enable"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpAccessV3Index"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpAccessV3SecurityLevel"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpAccessV3CustomOid"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpAccessV3OidLimit"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpAccessV3Access"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpAccessV3AuthAlgorithm"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpAccessV3AuthPassword"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpAccessV3PrivacyAlgorithm"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpAccessV3PrivacyPassword"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpAccessV3Enable"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpAccessControlIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpAccessControlStartIp"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpAccessControlEndIp"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpAccessControlEnable"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpTrapSinkV12Index"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpTrapSinkV12DestinationIp"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpTrapSinkV12Port"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpTrapSinkV12Community"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpTrapSinkV12Version"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpTrapSinkV12Enable"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpTrapSinkV3Index"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpTrapSinkV3DestinationIp"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpTrapSinkV3Port"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpTrapSinkV3Username"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpTrapSinkV3SecurityLevel"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpTrapSinkV3AuthAlgorithm"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpTrapSinkV3AuthPassword"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpTrapSinkV3PrivacyAlgorithm"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpTrapSinkV3PrivacyPassword"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpTrapSinkV3Enable"),
        ("SYMBOL-CC-WS2000-MIB", "ccCompactFlashCapacity"),
        ("SYMBOL-CC-WS2000-MIB", "ccCompactFlashUsed"),
        ("SYMBOL-CC-WS2000-MIB", "ccSumStatsShortWindow"),
        ("SYMBOL-CC-WS2000-MIB", "ccSumStatsShortUpdateInterval"),
        ("SYMBOL-CC-WS2000-MIB", "ccSumStatsLongWindow"),
        ("SYMBOL-CC-WS2000-MIB", "ccSumStatsLongUpdateInterval"),
        ("SYMBOL-CC-WS2000-MIB", "ccMgmtAccessToAllow"),
        ("SYMBOL-CC-WS2000-MIB", "ccMgmtAccessAirbeamAllow"),
        ("SYMBOL-CC-WS2000-MIB", "ccMgmtAccessAirbeamPassword"),
        ("SYMBOL-CC-WS2000-MIB", "ccMgmtAccessAdminAuth"),
        ("SYMBOL-CC-WS2000-MIB", "ccMgmtAccessAdminPassword"),
        ("SYMBOL-CC-WS2000-MIB", "ccMgmtAccessAdminAuthRadiusServerIp"),
        ("SYMBOL-CC-WS2000-MIB", "ccMgmtAccessAdminAuthRadiusServerPort"),
        ("SYMBOL-CC-WS2000-MIB", "ccMgmtAccessAdminAuthRadiusSharedSecret"),
        ("SYMBOL-CC-WS2000-MIB", "ccMgmtAccessSshAuthTimeout"),
        ("SYMBOL-CC-WS2000-MIB", "ccMgmtAccessSshInactivityTimeout"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoggingLevel"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoggingToSyslog"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoggingSyslogServer"),
        ("SYMBOL-CC-WS2000-MIB", "ccNtpEnable"),
        ("SYMBOL-CC-WS2000-MIB", "ccNtp0Server"),
        ("SYMBOL-CC-WS2000-MIB", "ccNtp0Port"),
        ("SYMBOL-CC-WS2000-MIB", "ccNtp1Server"),
        ("SYMBOL-CC-WS2000-MIB", "ccNtp1Port"),
        ("SYMBOL-CC-WS2000-MIB", "ccNtp2Server"),
        ("SYMBOL-CC-WS2000-MIB", "ccNtp2Port"),
        ("SYMBOL-CC-WS2000-MIB", "ccNtpGmtHourOffset"),
        ("SYMBOL-CC-WS2000-MIB", "ccNtpGmtMinuteOffset"),
        ("SYMBOL-CC-WS2000-MIB", "ccDhcpOptionsUpdateFwEna"),
        ("SYMBOL-CC-WS2000-MIB", "ccDhcpOptionsUpdateCfgEna"),
        ("SYMBOL-CC-WS2000-MIB", "ccDhcpOptionsUpdateInterface"),
        ("SYMBOL-CC-WS2000-MIB", "ccDhcpOptionsUpdateFwFilename"),
        ("SYMBOL-CC-WS2000-MIB", "ccDhcpOptionsUpdateCfgFilename"),
        ("SYMBOL-CC-WS2000-MIB", "ccRedundancyAdminState"),
        ("SYMBOL-CC-WS2000-MIB", "ccRedundancyOperState"),
        ("SYMBOL-CC-WS2000-MIB", "ccRedundancyHeartbeatInterval"),
        ("SYMBOL-CC-WS2000-MIB", "ccRedundancyRevertDelay"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlCfAlmostFullThreshold"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlFirewallUnderAttackDescription"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlFirewallUnderAttackRateLimit"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlRadarDetectedPortalMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlRadarDetectedChannel"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsDescr"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsUnits"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsCanBeSetMu"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsThresholdMu"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsCanBeSetPortal"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsThresholdPortals"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsCanBeSetWlan"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsThresholdWlans"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsCanBeSetSwitch"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsThresholdSwitch"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsMinPktsForTrap"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlLanVlanActivatedVlanId"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlDhcpOptionsFileTransferStatusRequested"),
        ("SYMBOL-CC-WS2000-MIB", "ccApIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccApNicMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccApModelNumber"),
        ("SYMBOL-CC-WS2000-MIB", "ccApSerialNumber"),
        ("SYMBOL-CC-WS2000-MIB", "ccApPcbRevision"),
        ("SYMBOL-CC-WS2000-MIB", "ccApBootLoaderRev"),
        ("SYMBOL-CC-WS2000-MIB", "ccApWispVersion"),
        ("SYMBOL-CC-WS2000-MIB", "ccApRuntimeFwVersion"),
        ("SYMBOL-CC-WS2000-MIB", "ccApNumPortals"),
        ("SYMBOL-CC-WS2000-MIB", "ccApPointersToPortals"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalPointerToAp"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalPointersToWlans"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalName"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalLocation"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalOptions"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalNumberOfEss"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalNumberOfBss"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalAssociatedMus"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRadioType"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalChannel"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPowerLevel"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalLastAdoption"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalState"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalBackgroundNoiseNumSamples"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalBackgroundNoiseBest"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalBackgroundNoiseWorst"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalBackgroundNoiseSum"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalBackgroundNoiseSumSquares"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalLastMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalLastReason"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalAdoptionIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalAdoptionStartMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalAdoptionEndMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalAdoptionWlanPointers"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalAdoptionRowStatus"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSystemStatsBeaconsTx"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSystemStatsBeaconsTxOctets"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSystemStatsProbeReqRx"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSystemStatsProbeReqRxOctets"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSystemStatsProbeRespRetriesNone"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSystemStatsProbeRespRetries1"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSystemStatsProbeRespRetries2"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSystemStatsProbeRespRetriesFailed"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSystemStatsProbeRespTxOctets"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPktsUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsNUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxOctetsUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsNUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxUndecryptablePkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalLastActivity"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsAt1Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsAt2Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsAt5pt5Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsAt6Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsAt9Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsAt11Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsAt12Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsAt18Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsAt22Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsAt24Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsAt36Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsAt48Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxPktsAt54Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPktsAt1Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPktsAt2Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPktsAt5pt5Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPktsAt6Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPktsAt9Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPktsAt11Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPktsAt12Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPktsAt18Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPktsAt22Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPktsAt24Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPktsAt36Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPktsAt48Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxPktsAt54Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsAt1Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsAt2Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsAt5pt5Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsAt6Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsAt9Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsAt11Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsAt12Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsAt18Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsAt22Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsAt24Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsAt36Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsAt48Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalRxOctetsAt54Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxOctetsAt1Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxOctetsAt2Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxOctetsAt5pt5Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxOctetsAt6Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxOctetsAt9Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxOctetsAt11Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxOctetsAt12Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxOctetsAt18Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxOctetsAt22Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxOctetsAt24Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxOctetsAt36Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxOctetsAt48Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxOctetsAt54Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPktsNone"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts01"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts02"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts03"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts04"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts05"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts06"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts07"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts08"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts09"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts10"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts11"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts12"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts13"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts14"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPkts15"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesPktsFailed"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctetsNone"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets01"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets02"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets03"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets04"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets05"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets06"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets07"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets08"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets09"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets10"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets11"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets12"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets13"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets14"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctets15"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalTxRetriesOctetsFailed"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsNumPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsSignalBest"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsSignalWorst"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsSignalSum"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsSignalSumSquares"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsSignalMostRecent"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsNoiseBest"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsNoiseWorst"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsNoiseSum"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsNoiseSumSquares"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsNoiseMostRecent"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsSnrBest"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsSnrWorst"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsSnrSum"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsSnrSumSquares"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSigStatsSnrMostRecent"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortTimestamp"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortNumPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortPktsPerSec100"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortPktsPerSecTx100"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortPktsPerSecRx100"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortThroughput"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortThroughputTx"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortThroughputRx"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortAvgBitSpeed"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortAvgMuSignal"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortAvgMuNoise"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortAvgMuSnr"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortPp10kNUcastPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortPp10kTxWithRetries"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortTxAvgRetries100"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortPp10kRxUndecrypt"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortTotalMus"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsShortPp10kRfUtil"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongTimestamp"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongNumPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongPktsPerSec100"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongPktsPerSecTx100"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongPktsPerSecRx100"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongThroughput"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongThroughputTx"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongThroughputRx"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongAvgBitSpeed"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongAvgMuSignal"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongAvgMuNoise"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongAvgMuSnr"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongPp10kNUcastPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongPp10kTxWithRetries"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongTxAvgRetries100"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongPp10kRxUndecrypt"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongTotalMus"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongPp10kRfUtil"),
        ("SYMBOL-CC-WS2000-MIB", "ccAssociationFirstAssociate"),
        ("SYMBOL-CC-WS2000-MIB", "ccAssociationLastAssociate"),
        ("SYMBOL-CC-WS2000-MIB", "ccAssociationCountAssociates"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuWlanIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuWlanName"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuIsDataReady"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuPortalIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuPortalMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSymbolRogueApEna"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuIpAddr"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuType"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRadioType"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSupportedRates"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuPowerMode"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuAuthenticationMethod"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuEncryptionMethod"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuVlanId"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxUndecryptablePkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxRssiNumPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxRssiSum"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxRssiSumSquares"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxRssiMostRecent"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuLastActivity"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt1Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt2Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt5pt5Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt6Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt9Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt11Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt12Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt18Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt22Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt24Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt36Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt48Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxPktsAt54Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt1Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt2Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt5pt5Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt6Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt9Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt11Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt12Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt18Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt22Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt24Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt36Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt48Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxPktsAt54Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt1Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt2Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt5pt5Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt6Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt9Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt11Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt12Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt18Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt22Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt24Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt36Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt48Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuRxOctetsAt54Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt1Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt2Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt5pt5Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt6Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt9Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt11Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt12Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt18Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt22Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt24Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt36Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt48Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxOctetsAt54Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesNone"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries01"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries02"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries03"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries04"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries05"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries06"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries07"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries08"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries09"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries10"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries11"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries12"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries13"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries14"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetries15"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesFailed"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesTotal"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesMostRecent"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuLastMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuLastReason"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuLastPortal"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctetsNone"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets01"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets02"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets03"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets04"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets05"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets06"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets07"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets08"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets09"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets10"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets11"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets12"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets13"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets14"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctets15"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuTxRetriesOctetsFailed"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsNumPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsSignalBest"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsSignalWorst"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsSignalSum"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsSignalSumSquares"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsSignalMostRecent"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsNoiseBest"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsNoiseWorst"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsNoiseSum"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsNoiseSumSquares"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsNoiseMostRecent"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsSnrBest"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsSnrWorst"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsSnrSum"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsSnrSumSquares"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSigStatsSnrMostRecent"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortTimestamp"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortNumPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortPktsPerSec100"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortPktsPerSecTx100"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortPktsPerSecRx100"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortThroughput"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortThroughputTx"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortThroughputRx"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortAvgBitSpeed"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortAvgMuSignal"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortAvgMuNoise"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortAvgMuSnr"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortPp10kNUcastPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortPp10kTxWithRetries"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortTxAvgRetries100"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsShortPp10kRxUndecrypt"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongTimestamp"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongNumPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongPktsPerSec100"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongPktsPerSecTx100"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongPktsPerSecRx100"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongThroughput"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongThroughputTx"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongThroughputRx"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongAvgBitSpeed"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongAvgMuSignal"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongAvgMuNoise"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongAvgMuSnr"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongPp10kNUcastPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongPp10kTxWithRetries"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongTxAvgRetries100"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuSumStatsLongPp10kRxUndecrypt"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanName"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanEssid"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSubnet"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanPortalsAdopted"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanEnable"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanDisallowMuToMu"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanVoicePrioritization"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAnswerBroadcastEss"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanMulticastAddr1"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanMulticastAddr2"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanMuAclDefault"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthentication"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanEncryption"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanWeight"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapReauthenticationEnable"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapReauthenticationPeriod"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapReauthenticationMaxRetries"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapRadius1Server"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapRadius1Port"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapRadius1SharedSecret"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapRadius2Server"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapRadius2Port"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapRadius2SharedSecret"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapMuQuietPeriod"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapMuTimeout"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapMuTxPeriod"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapMuMaxRetries"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapServerTimeout"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapServerMaxRetries"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthKerberosRealmName"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthKerberosUsername"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthKerberosPassword"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthKerberosKdcServerIp1"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthKerberosKdcPort1"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthKerberosKdcServerIp2"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthKerberosKdcPort2"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthKerberosKdcServerIpR"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthKerberosKdcPortR"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWepPassKey"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWepKey1"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWepKey2"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWepKey3"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWepKey4"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWepKeyToUse"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWpaBcastKeyRotation"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWpaKeyRotationInterval"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWpaKeyToUse"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWpaPassphrase"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWpaKey"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoKeyguardPasskey"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoKeyguardKey1"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoKeyguardKey2"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoKeyguardKey3"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoKeyguardKey4"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoKeyguardKeyToUse"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanMuAclIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanMuAclStartingMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanMuAclEndingMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanMuAclRowStatus"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanBwShareMode"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxPktsUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsNUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxOctetsUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsNUcast"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxUndecryptablePkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanLastActivity"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsAt1Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsAt2Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsAt5pt5Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsAt6Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsAt9Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsAt11Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsAt12Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsAt18Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsAt22Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsAt24Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsAt36Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsAt48Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxPktsAt54Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxPktsAt1Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxPktsAt2Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxPktsAt5pt5Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxPktsAt6Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxPktsAt9Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxPktsAt11Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxPktsAt12Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxPktsAt18Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxPktsAt22Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxPktsAt24Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxPktsAt36Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxPktsAt48Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxPktsAt54Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsAt1Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsAt2Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsAt5pt5Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsAt6Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsAt9Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsAt11Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsAt12Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsAt18Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsAt22Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsAt24Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsAt36Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsAt48Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanRxOctetsAt54Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxOctetsAt1Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxOctetsAt2Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxOctetsAt5pt5Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxOctetsAt6Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxOctetsAt9Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxOctetsAt11Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxOctetsAt12Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxOctetsAt18Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxOctetsAt22Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxOctetsAt24Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxOctetsAt36Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxOctetsAt48Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxOctetsAt54Mb"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPktsNone"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts01"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts02"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts03"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts04"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts05"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts06"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts07"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts08"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts09"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts10"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts11"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts12"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts13"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts14"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPkts15"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesPktsFailed"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctetsNone"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets01"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets02"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets03"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets04"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets05"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets06"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets07"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets08"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets09"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets10"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets11"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets12"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets13"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets14"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctets15"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanTxRetriesOctetsFailed"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSigStatsNumPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSigStatsSignalBest"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSigStatsSignalWorst"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSigStatsSignalSum"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSigStatsSignalSumSquares"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSigStatsNoiseBest"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSigStatsNoiseWorst"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSigStatsNoiseSum"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSigStatsNoiseSumSquares"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSigStatsSnrBest"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSigStatsSnrWorst"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSigStatsSnrSum"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSigStatsSnrSumSquares"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortTimestamp"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortNumPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortPktsPerSec100"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortPktsPerSecTx100"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortPktsPerSecRx100"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortThroughput"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortThroughputTx"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortThroughputRx"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortAvgBitSpeed"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortAvgMuSignal"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortAvgMuNoise"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortAvgMuSnr"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortPp10kNUcastPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortPp10kTxWithRetries"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortTxAvgRetries100"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortPp10kRxUndecrypt"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortTotalMus"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongTimestamp"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongNumPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongPktsPerSec100"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongPktsPerSecTx100"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongPktsPerSecRx100"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongThroughput"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongThroughputTx"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongThroughputRx"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongAvgBitSpeed"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongAvgMuSignal"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongAvgMuNoise"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongAvgMuSnr"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongPp10kNUcastPkts"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongPp10kTxWithRetries"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongTxAvgRetries100"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongPp10kRxUndecrypt"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongTotalMus"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanDhcpEnable"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanDhcpIpAddr"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanDhcpSubnetMask"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanDhcpDefaultGateway"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanDhcpPrimaryDnsServer"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanDhcpSecondaryDnsServer"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanSubnetMask"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanDefaultGateway"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanPrimaryDnsServer"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanSecondaryDnsServer"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanPppoeEnable"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanPppoeUsername"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanPppoePassword"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanPppoeKeepAlive"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanPppoeIdleTime"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanPppoeAuthType"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanIpAddrIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanIpAddrEnable"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanIpAddr"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanFirewallGlobalEnable"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanFirewallIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanFirewallDescription"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanFirewallAlwaysEnabled"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanFirewallEnable"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanFirewallMimeFloodMaxHeaderLength"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanFirewallMimeFloodMaxHeaders"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanNatIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanNatWanIpAddress"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanNatType"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanNat1to1IpAddr"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanNatInboundDefaultEna"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanNatInboundDefaultIp"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanNatInboundIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanNatInboundName"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanNatInboundTransport"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanNatInboundStartPort"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanNatInboundEndPort"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanNatInboundIpAddr"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanNatInboundRowStatus"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanNatOutboundSubnetIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanNatOutboundPossibleIpAddr"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanNatOutboundIpAddr"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnName"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnLocalSubnet"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnLocalWanIp"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnRemoteSubnet"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnRemoteSubnetMask"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnRemoteGateway"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyExchange"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnRowStatus"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyManualAhAuth"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyManualInAhAuthKey"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyManualOutAhAuthKey"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyManualInAhSpi"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyManualOutAhSpi"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyManualEspType"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyManualEspEncrypAlg"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyManualInEspEncrypKey"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyManualOutEspEncrypKey"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyManualEspAuthAlg"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyManualInEspAuthKey"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyManualOutEspAuthKey"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyManualInEspSpi"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyManualOutEspSpi"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyAutoUsePerfectSecrecy"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyAutoAhAuth"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyAutoEspType"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyAutoEspEncrypAlg"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyAutoEspAuthAlg"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyAutoIkeOperationMode"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyAutoIkeLocalIdType"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyAutoIkeLocalIdData"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyAutoIkeRemoteIdType"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyAutoIkeRemoteIdData"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyAutoIkeAuthAlg"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyAutoIkeAuthPassphrase"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyAutoIkeEncrypAlg"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyAutoIkeXauthMode"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyAutoIkeXauthUsername"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyAutoIkeXauthPassword"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyAutoIkeKeyLifetime"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyAutoIkeDiffieHelmanGroup"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnSaTunnelName"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnSaStatus"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnSaInSpi"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnSaOutSpi"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnSaLifetime"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnSaTxBytes"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnSaRxBytes"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnIkeTunnelName"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnIkeState"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnIkeRemainingLife"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanContentBlockSmtp"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanContentBlockFtp"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanContentBlockHttp"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanContentBlockOutUrlIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanContentBlockOutUrlExtension"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanContentBlockOutUrlRowStatus"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortType"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortPoeEquipped"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortStatus"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortDuplex"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortSpeed"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetEnable"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetName"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetIpAddress"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetIpSubnetMask"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetPortMembers"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetWlanMembers"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetDhcpState"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetDhcpIpAddress"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetDhcpSubnetMask"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetDhcpServerEnable"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetDhcpServerPoolStart"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetDhcpServerPoolEnd"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetDhcpServerPrimaryDns"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetDhcpServerSecondaryDns"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetDhcpServerDefaultGateway"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetDhcpServerLeaseTime"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetDhcpServerStaticMapMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetDhcpServerStaticMapIpAddr"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetDhcpServerStaticMapEnable"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessDestIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessRuleIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessDestType"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessDestPtrToDest"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessRuleName"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessRuleType"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvInIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccLanVlanType"),
        ("SYMBOL-CC-WS2000-MIB", "ccLanVlanTrunkPort"),
        ("SYMBOL-CC-WS2000-MIB", "ccLanVlanDefaultTag"),
        ("SYMBOL-CC-WS2000-MIB", "ccLanVlanTrunked"),
        ("SYMBOL-CC-WS2000-MIB", "ccLanVlanId"),
        ("SYMBOL-CC-WS2000-MIB", "ccRouterRipType"),
        ("SYMBOL-CC-WS2000-MIB", "ccRouterRipDirection"),
        ("SYMBOL-CC-WS2000-MIB", "ccRouterRip2AuthType"),
        ("SYMBOL-CC-WS2000-MIB", "ccRouterRip2SimplePassword"),
        ("SYMBOL-CC-WS2000-MIB", "ccRouterRip2Md5Key1Id"),
        ("SYMBOL-CC-WS2000-MIB", "ccRouterRip2Md5Key1AuthKey"),
        ("SYMBOL-CC-WS2000-MIB", "ccRouterRip2Md5Key2Id"),
        ("SYMBOL-CC-WS2000-MIB", "ccRouterRip2Md5Key2AuthKey"),
        ("SYMBOL-CC-WS2000-MIB", "ccRouterRoutesIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccRouterRoutesDest"),
        ("SYMBOL-CC-WS2000-MIB", "ccRouterRoutesDestMask"),
        ("SYMBOL-CC-WS2000-MIB", "ccRouterRoutesGateway"),
        ("SYMBOL-CC-WS2000-MIB", "ccRouterRoutesInterface"),
        ("SYMBOL-CC-WS2000-MIB", "ccRouterRoutesMetric"),
        ("SYMBOL-CC-WS2000-MIB", "ccRouterUserRoutesIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccRouterUserRoutesDest"),
        ("SYMBOL-CC-WS2000-MIB", "ccRouterUserRoutesDestMask"),
        ("SYMBOL-CC-WS2000-MIB", "ccRouterUserRoutesGateway"),
        ("SYMBOL-CC-WS2000-MIB", "ccRouterUserRoutesInterface"),
        ("SYMBOL-CC-WS2000-MIB", "ccRouterUserRoutesMetric"),
        ("SYMBOL-CC-WS2000-MIB", "ccRouterUserRoutesRowStatus"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapPollSymbolMusEnable"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapPollSymbolMusInterval"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapOnChannelEnable"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapOnChannelInterval"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapDetectorsEnable"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapDetectorsInterval"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapAuthAllSymbolMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapAuthIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapAuthMacFilter"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapAuthEssidFilter"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapAuthRowExists"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapAuthErase"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapAuthCopyAllApproved"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapResultsApprovedAgeOut"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapResultsApprovedApMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapResultsApprovedEssid"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapResultsApprovedCopyToAuthTable"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapResultsApprovedFirstHeard"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapResultsApprovedLastHeard"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapResultsApprovedPortalPtr"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapResultsApprovedHowFound"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapResultsApprovedHowAuth"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapResultsApprovedErase"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapResultsRogueAgeOut"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapResultsRogueApMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapResultsRogueEssid"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapResultsRogueCopyToAuthTable"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapResultsRogueFirstHeard"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapResultsRogueLastHeard"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapResultsRoguePortalPtr"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapResultsRogueHowFound"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapResultsRogueClosestPortalPtr"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapResultsRogueClosestPortalRssi"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapResultsRogueErase"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapPortalResultsApMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapPortalResultsApEssid"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapPortalResultsInProcess"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapPortalResultsPortalMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapPortalResultsRssi"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapPollOneMuMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapPollOneMuInProcess"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapPollOneMuStatus"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapPollOneMuResultsIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapPollOneMuResultsRssi"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapPollOneMuResultsEssid"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapPollOneMuResultsApMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusDataSource"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusDefaultEapType"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusClientAuthIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusClientAuthIpAddr"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusClientAuthMask"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusClientAuthSharedSecret"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusProxyRetryCount"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusProxyTimeout"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusProxyServerIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusProxyServerIp"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusProxyServerPort"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusProxyServerSharedSecret"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusLdapServerIp"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusLdapServerPort"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusLdapLoginAttribute"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusLdapPasswordAttribute"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusLdapBindDistinguishedName"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusLdapBindDistinguishedPassword"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusLdapBaseDistinguishedName"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusLdapGroupAttribute"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusLdapGroupFilter"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusLdapGroupMembershipAttribute"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusUsersId"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusUsersPassword"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusUsersGroups"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusUsersRowStatus"),
        ("SYMBOL-CC-WS2000-MIB", "ccNtpCurrentDateTime"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusAuthTypePeap"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusAuthTypeTtls"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusClientAuthRowStatus"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusProxyServerPrefixOrSuffix"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvInSrcIp"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvInSrcIpLength"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvInDestIp"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvInDestIpLength"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvInTransport"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvInSrcPortStart"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvInSrcPortEnd"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvInDestPortStart"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvInDestPortEnd"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvInAction"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvInRowStatus"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvOutIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvOutSrcIp"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvOutSrcIpLength"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvOutDestIp"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvOutDestIpLength"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvOutTransport"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvOutSrcPortStart"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvOutSrcPortEnd"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvOutDestPortStart"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvOutDestPortEnd"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvOutReverseNat"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvOutAction"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlRedundancyPreviousOperState"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvOutRowStatus"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanNatLowestUnusedSlot"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessPtrToRules"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessRuleSrcPtr"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessRuleDestPtr"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessRuleTransport"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessRuleStartPort"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessRuleEndPort"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessRuleRowStatus"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlEnableIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlEnableName"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlEnable"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanQosMonitorSent"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanQosMonitorDropped"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortPp10kDropped"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusProxyServerRowStatus"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanNatOutboundEnable"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapResultsApprovedIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapResultsRogueIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongPp10kDropped"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpAccessV3User"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpV3EngineId"),
        ("SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsReqIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsReqKeyId"),
        ("SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsReqSubject"),
        ("SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsReqDept"),
        ("SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsReqOrg"),
        ("SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsReqCity"),
        ("SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsReqState"),
        ("SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsReqPostal"),
        ("SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsReqCountry"),
        ("SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsReqEmail"),
        ("SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsReqDomain"),
        ("SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsReqIp"),
        ("SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsReqSigAlgo"),
        ("SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsReqKeyLen"),
        ("SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsReqGenReq"),
        ("SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsReqCertReqStr"),
        ("SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsReqRowStatus"),
        ("SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsSignedStr"),
        ("SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsSignedImport"),
        ("SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsSignedIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsSignedKeyId"),
        ("SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsSignedIssuerName"),
        ("SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsSignedSubject"),
        ("SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsSignedSerialNumber"),
        ("SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsSignedExpiry"),
        ("SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsSignedDeleteRow"),
        ("SYMBOL-CC-WS2000-MIB", "ccCACertsStr"),
        ("SYMBOL-CC-WS2000-MIB", "ccCACertsImport"),
        ("SYMBOL-CC-WS2000-MIB", "ccCACertsIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccCACertsKeyId"),
        ("SYMBOL-CC-WS2000-MIB", "ccCACertsIssuerName"),
        ("SYMBOL-CC-WS2000-MIB", "ccCACertsSubject"),
        ("SYMBOL-CC-WS2000-MIB", "ccCACertsSerialNumber"),
        ("SYMBOL-CC-WS2000-MIB", "ccCACertsExpiry"),
        ("SYMBOL-CC-WS2000-MIB", "ccCACertsDeleteRow"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSettingsName"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSettingsLocation"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSettingsAntenna"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSettingsShortPreamble"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSettingsUniSpread"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSettingsRtsThresh"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSettingsBeaconInt"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSettingsDtimPrd"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSettingsSecBeacon"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSettingsPriWlan"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSettingsBasicRates"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSettingsSupportedRates"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSettingsBGMode"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSettingsAdoptedWlan"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalCfgRadioDesPlacement"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalCfgRadioPosChannel"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalCfgRadioDesChannel"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalCfgRadioPosPowerLevel"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalCfgRadioDesPowerLevel"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalCfgRadioPowerInMW"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalCfgRadioSet"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalCfgRadioReset"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalCfgRadioPlacement"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalCfgRadioChannel"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalCfgRadioPowerLevel"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSettingsDefaultAntenna"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSettingsDefaultShortPreamble"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSettingsDefaultUniSpread"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSettingsDefaultRtsThresh"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSettingsDefaultBeaconInt"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSettingsDefaultDtimPrd"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSettingsDefaultSecBeacon"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSettingsDefaultPriWlan"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSettingsDefaultBasicRates"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSettingsDefaultSupportedRates"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSettingsDefaultBGMode"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalCfgRadioDefaultDesPlacement"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalCfgRadioDefaultPosChannel"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalCfgRadioDefaultDesChannel"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalCfgRadioDefaultPosPowerLevel"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalCfgRadioDefaultDesPowerLevel"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalCfgRadioDefaultSet"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalCfgRadioDefaultReset"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalCfgRadioDefaultPlacement"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalCfgRadioDefaultChannel"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalCfgRadioDefaultPowerLevel"),
        ("SYMBOL-CC-WS2000-MIB", "cc802dt1xPortAuthLogin"),
        ("SYMBOL-CC-WS2000-MIB", "cc802dt1xPortAuthPass"),
        ("SYMBOL-CC-WS2000-MIB", "cc802dt1xPortAuthSetAp300"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSettingsDefaultIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapPortalResultsIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapAuthCopyAllRogue"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSettingsDetector"),
        ("SYMBOL-CC-WS2000-MIB", "ccRedundancyHeartbeatInterface"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusCACertificate"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusServerCertificate"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetDhcpServerDomainName"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetDhcpServerWinsServer"),
        ("SYMBOL-CC-WS2000-MIB", "ccCertMgntSelfCertsIdName"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSystemStatsProbeRespRetries3OrMore"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalSumStatsLongPp10kTxMaxRetries"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWpaTwoFastRoamKeyCache"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWpaTwoFastRoamPreAuth"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWpaTwoAllowTkipClient"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWpaTwoKey"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWpaTwoPassphrase"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWpaTwoKeyToUse"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWpaTwoKeyRotationInterval"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanCryptoWpaTwoBcastKeyRotation"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvOverrideMode"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvImportRules"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapSyslogMode"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapSyslogSeverIp"),
        ("SYMBOL-CC-WS2000-MIB", "ccMgmtAccessHttpsTimeout"),
        ("SYMBOL-CC-WS2000-MIB", "ccNtpSyncInterval"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanNatTimeout"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoggingDeleteCoreFile"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoggingTransferCoreFile"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapRadiusAcctMuRetries"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanVpnKeyAutoIkeAuthType"),
        ("SYMBOL-CC-WS2000-MIB", "ccWanNatInboundTranslationPort"),
        ("SYMBOL-CC-WS2000-MIB", "ccRedundancyOperMode"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapResultsApprovedChannel"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapResultsRogueChannel"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalCfgRadioDefaultDesPowerInMW"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalCfgRadioDesPowerInMW"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalCfgRadioDefaultPowerInMW"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapRadiusAcctMode"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanAuthEapRadiusAcctMuTimeout"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvInReverseNatIp"),
        ("SYMBOL-CC-WS2000-MIB", "ccSubnetAccessAdvInReverseNatPort"))
)
if mibBuilder.loadTexts:
    ccGroupsV2dot0variables.setStatus("current")

ccGroupsV2dot0obsoleted = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 1000, 3, 2)
)
ccGroupsV2dot0obsoleted.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsShortSkip1"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanSumStatsLongSkip1"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusAccessWlanPtrs"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusUsersGroup"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusUsersGroupRowStatus"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadiusUsersGroupId"))
)
if mibBuilder.loadTexts:
    ccGroupsV2dot0obsoleted.setStatus("obsolete")


# Notification objects

ccPortalAdopted = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 1)
)
ccPortalAdopted.setObjects(
    ("SYMBOL-CC-WS2000-MIB", "ccPortalLastMac")
)
if mibBuilder.loadTexts:
    ccPortalAdopted.setStatus(
        "current"
    )

ccPortalUnAdopted = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 2)
)
ccPortalUnAdopted.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccPortalLastMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalLastReason"))
)
if mibBuilder.loadTexts:
    ccPortalUnAdopted.setStatus(
        "current"
    )

ccPortalDenied = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 3)
)
ccPortalDenied.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccPortalLastMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalLastReason"))
)
if mibBuilder.loadTexts:
    ccPortalDenied.setStatus(
        "current"
    )

ccMuAssociated = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 4)
)
ccMuAssociated.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccMuLastMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuLastPortal"))
)
if mibBuilder.loadTexts:
    ccMuAssociated.setStatus(
        "current"
    )

ccMuUnAssociated = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 5)
)
ccMuUnAssociated.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccMuLastMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuLastPortal"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuLastReason"))
)
if mibBuilder.loadTexts:
    ccMuUnAssociated.setStatus(
        "current"
    )

ccMuDenied = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 6)
)
ccMuDenied.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccMuLastMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuLastPortal"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuLastReason"))
)
if mibBuilder.loadTexts:
    ccMuDenied.setStatus(
        "current"
    )

ccConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 7)
)
ccConfigChange.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccCfgHistChangeTime"),
        ("SYMBOL-CC-WS2000-MIB", "ccCfgHistChangeCount"))
)
if mibBuilder.loadTexts:
    ccConfigChange.setStatus(
        "current"
    )

ccSnmpAclViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 8)
)
ccSnmpAclViolation.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccSnmpLastDeniedIpAddr"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpAclViolations"))
)
if mibBuilder.loadTexts:
    ccSnmpAclViolation.setStatus(
        "current"
    )

ccPortStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 9)
)
ccPortStatusChange.setObjects(
    ("SYMBOL-CC-WS2000-MIB", "ccPortStatus")
)
if mibBuilder.loadTexts:
    ccPortStatusChange.setStatus(
        "current"
    )

ccCfAlmostFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 10)
)
ccCfAlmostFull.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccCompactFlashCapacity"),
        ("SYMBOL-CC-WS2000-MIB", "ccCompactFlashUsed"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlCfAlmostFullThreshold"))
)
if mibBuilder.loadTexts:
    ccCfAlmostFull.setStatus(
        "current"
    )

ccFirewallUnderAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 11)
)
ccFirewallUnderAttack.setObjects(
    ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlFirewallUnderAttackDescription")
)
if mibBuilder.loadTexts:
    ccFirewallUnderAttack.setStatus(
        "current"
    )

ccRadarDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 12)
)
ccRadarDetected.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlRadarDetectedPortalMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlRadarDetectedChannel"))
)
if mibBuilder.loadTexts:
    ccRadarDetected.setStatus(
        "current"
    )

ccSumStatsMu = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 13)
)
ccSumStatsMu.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsDescr"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsThresholdMu"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsUnits"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuIpAddr"))
)
if mibBuilder.loadTexts:
    ccSumStatsMu.setStatus(
        "current"
    )

ccSumStatsPortal = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 14)
)
ccSumStatsPortal.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsThresholdPortals"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsUnits"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalMac"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalName"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalLocation"))
)
if mibBuilder.loadTexts:
    ccSumStatsPortal.setStatus(
        "current"
    )

ccSumStatsWlan = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 15)
)
ccSumStatsWlan.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsDescr"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsThresholdWlans"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsUnits"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanIndex"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanName"),
        ("SYMBOL-CC-WS2000-MIB", "ccWlanEssid"))
)
if mibBuilder.loadTexts:
    ccSumStatsWlan.setStatus(
        "current"
    )

ccSumStatsSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 16)
)
ccSumStatsSwitch.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsDescr"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsThresholdSwitch"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlSumStatsUnits"))
)
if mibBuilder.loadTexts:
    ccSumStatsSwitch.setStatus(
        "current"
    )

ccLanVlanActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 17)
)
ccLanVlanActivated.setObjects(
    ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlLanVlanActivatedVlanId")
)
if mibBuilder.loadTexts:
    ccLanVlanActivated.setStatus(
        "current"
    )

ccDhcpOptionsFileTransferStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 18)
)
ccDhcpOptionsFileTransferStatus.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlDhcpOptionsFileTransferStatusRequested"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFwServerFilename"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFwSuccess"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadFwResult"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadCfgServerFilename"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadCfgSuccess"),
        ("SYMBOL-CC-WS2000-MIB", "ccLoadCfgResult"))
)
if mibBuilder.loadTexts:
    ccDhcpOptionsFileTransferStatus.setStatus(
        "current"
    )

ccRedundancyStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 3, 19)
)
ccRedundancyStateChange.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccRedundancyOperState"),
        ("SYMBOL-CC-WS2000-MIB", "ccTrapCtrlRedundancyPreviousOperState"))
)
if mibBuilder.loadTexts:
    ccRedundancyStateChange.setStatus(
        "current"
    )

ccRapNewApprovedAp = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 1, 4)
)
ccRapNewApprovedAp.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccRapResultsApprovedPortalPtr"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapResultsApprovedHowFound"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapResultsApprovedHowAuth"))
)
if mibBuilder.loadTexts:
    ccRapNewApprovedAp.setStatus(
        "current"
    )

ccRapNewRogueAp = NotificationType(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 7, 3, 2, 4)
)
ccRapNewRogueAp.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccRapResultsRoguePortalPtr"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapResultsRogueHowFound"))
)
if mibBuilder.loadTexts:
    ccRapNewRogueAp.setStatus(
        "current"
    )


# Notifications groups

ccNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 1000, 1, 2)
)
ccNotificationsGroup.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccPortalAdopted"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalUnAdopted"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalDenied"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuAssociated"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuUnAssociated"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuDenied"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpAclViolation"),
        ("SYMBOL-CC-WS2000-MIB", "ccConfigChange"))
)
if mibBuilder.loadTexts:
    ccNotificationsGroup.setStatus(
        "current"
    )

ccGroupsV1dot5notifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 1000, 2, 3)
)
ccGroupsV1dot5notifications.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccPortStatusChange"),
        ("SYMBOL-CC-WS2000-MIB", "ccCfAlmostFull"),
        ("SYMBOL-CC-WS2000-MIB", "ccFirewallUnderAttack"),
        ("SYMBOL-CC-WS2000-MIB", "ccSumStatsMu"),
        ("SYMBOL-CC-WS2000-MIB", "ccSumStatsPortal"),
        ("SYMBOL-CC-WS2000-MIB", "ccSumStatsWlan"),
        ("SYMBOL-CC-WS2000-MIB", "ccSumStatsSwitch"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadarDetected"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalAdopted"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalUnAdopted"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalDenied"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuAssociated"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuUnAssociated"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuDenied"),
        ("SYMBOL-CC-WS2000-MIB", "ccConfigChange"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpAclViolation"))
)
if mibBuilder.loadTexts:
    ccGroupsV1dot5notifications.setStatus(
        "current"
    )

ccGroupsV2dot0notifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 388, 11, 2, 1000, 3, 3)
)
ccGroupsV2dot0notifications.setObjects(
      *(("SYMBOL-CC-WS2000-MIB", "ccPortalAdopted"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalUnAdopted"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortalDenied"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuAssociated"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuUnAssociated"),
        ("SYMBOL-CC-WS2000-MIB", "ccMuDenied"),
        ("SYMBOL-CC-WS2000-MIB", "ccConfigChange"),
        ("SYMBOL-CC-WS2000-MIB", "ccSnmpAclViolation"),
        ("SYMBOL-CC-WS2000-MIB", "ccPortStatusChange"),
        ("SYMBOL-CC-WS2000-MIB", "ccCfAlmostFull"),
        ("SYMBOL-CC-WS2000-MIB", "ccFirewallUnderAttack"),
        ("SYMBOL-CC-WS2000-MIB", "ccRadarDetected"),
        ("SYMBOL-CC-WS2000-MIB", "ccSumStatsMu"),
        ("SYMBOL-CC-WS2000-MIB", "ccSumStatsPortal"),
        ("SYMBOL-CC-WS2000-MIB", "ccSumStatsWlan"),
        ("SYMBOL-CC-WS2000-MIB", "ccSumStatsSwitch"),
        ("SYMBOL-CC-WS2000-MIB", "ccLanVlanActivated"),
        ("SYMBOL-CC-WS2000-MIB", "ccDhcpOptionsFileTransferStatus"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapNewApprovedAp"),
        ("SYMBOL-CC-WS2000-MIB", "ccRapNewRogueAp"),
        ("SYMBOL-CC-WS2000-MIB", "ccRedundancyStateChange"))
)
if mibBuilder.loadTexts:
    ccGroupsV2dot0notifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYMBOL-CC-WS2000-MIB",
    **{"SinglePointer": SinglePointer,
       "MultiPointer63": MultiPointer63,
       "MultiPointer255": MultiPointer255,
       "DoActionNow": DoActionNow,
       "RadioType": RadioType,
       "Password": Password,
       "StaticRowEnable": StaticRowEnable,
       "PartsPer10k": PartsPer10k,
       "ScaleBy100": ScaleBy100,
       "AbbrevRowStatus": AbbrevRowStatus,
       "DoActionShowProgress": DoActionShowProgress,
       "HexPassword": HexPassword,
       "TransmitRate": TransmitRate,
       "RowStatus": RowStatus,
       "DateAndTime": DateAndTime,
       "symbol": symbol,
       "wsd": wsd,
       "sysoids": sysoids,
       "ws2000": ws2000,
       "ws2k": ws2k,
       "moduleid": moduleid,
       "ccAdmin": ccAdmin,
       "ccInfo": ccInfo,
       "ccInfoSerialNumber": ccInfoSerialNumber,
       "ccInfoCountrySelection": ccInfoCountrySelection,
       "ccIdentfication": ccIdentfication,
       "ccIdHwVersion": ccIdHwVersion,
       "ccIdFwVersion": ccIdFwVersion,
       "ccIdSwVersion": ccIdSwVersion,
       "ccIdMibVersion": ccIdMibVersion,
       "ccIdCliVersion": ccIdCliVersion,
       "ccIdXmlVersion": ccIdXmlVersion,
       "ccIdSerialNumber": ccIdSerialNumber,
       "ccSysDNSRelayMode": ccSysDNSRelayMode,
       "ccApSslv2Mode": ccApSslv2Mode,
       "ccApSshv1Mode": ccApSshv1Mode,
       "ccApSslWeakCipherSupport": ccApSslWeakCipherSupport,
       "ccReset": ccReset,
       "ccResetFactory": ccResetFactory,
       "ccResetSwitch": ccResetSwitch,
       "ccResetMuCounters": ccResetMuCounters,
       "ccResetFactoryExceptIpSnmp": ccResetFactoryExceptIpSnmp,
       "ccResetStatCounters": ccResetStatCounters,
       "ccLoadFw": ccLoadFw,
       "ccLoadFwOperation": ccLoadFwOperation,
       "ccLoadFwInterface": ccLoadFwInterface,
       "ccLoadFwServerPath": ccLoadFwServerPath,
       "ccLoadFwServerFilename": ccLoadFwServerFilename,
       "ccLoadFwStart": ccLoadFwStart,
       "ccLoadFwResult": ccLoadFwResult,
       "ccLoadFwSuccess": ccLoadFwSuccess,
       "ccLoadCfg": ccLoadCfg,
       "ccLoadCfgOperation": ccLoadCfgOperation,
       "ccLoadCfgServerPath": ccLoadCfgServerPath,
       "ccLoadCfgServerFilename": ccLoadCfgServerFilename,
       "ccLoadCfgStart": ccLoadCfgStart,
       "ccLoadCfgOperationsDone": ccLoadCfgOperationsDone,
       "ccLoadCfgResult": ccLoadCfgResult,
       "ccLoadCfgSuccess": ccLoadCfgSuccess,
       "ccCfgHist": ccCfgHist,
       "ccCfgHistChangeCount": ccCfgHistChangeCount,
       "ccCfgHistChangeTime": ccCfgHistChangeTime,
       "ccCfgHistSemaphore": ccCfgHistSemaphore,
       "ccLoad": ccLoad,
       "ccLoadServerIpAddr": ccLoadServerIpAddr,
       "ccLoadFtpUsername": ccLoadFtpUsername,
       "ccLoadFtpPassword": ccLoadFtpPassword,
       "ccSnmp": ccSnmp,
       "ccSnmpAclViolations": ccSnmpAclViolations,
       "ccSnmpLastDeniedIpAddr": ccSnmpLastDeniedIpAddr,
       "ccSnmpV3EngineId": ccSnmpV3EngineId,
       "ccSnmpAccess": ccSnmpAccess,
       "ccSnmpAccessV12Table": ccSnmpAccessV12Table,
       "ccSnmpAccessV12Entry": ccSnmpAccessV12Entry,
       "ccSnmpAccessV12Index": ccSnmpAccessV12Index,
       "ccSnmpAccessV12Community": ccSnmpAccessV12Community,
       "ccSnmpAccessV12CustomOid": ccSnmpAccessV12CustomOid,
       "ccSnmpAccessV12OidLimit": ccSnmpAccessV12OidLimit,
       "ccSnmpAccessV12Access": ccSnmpAccessV12Access,
       "ccSnmpAccessV12Enable": ccSnmpAccessV12Enable,
       "ccSnmpAccessV3Table": ccSnmpAccessV3Table,
       "ccSnmpAccessV3Entry": ccSnmpAccessV3Entry,
       "ccSnmpAccessV3Index": ccSnmpAccessV3Index,
       "ccSnmpAccessV3User": ccSnmpAccessV3User,
       "ccSnmpAccessV3SecurityLevel": ccSnmpAccessV3SecurityLevel,
       "ccSnmpAccessV3CustomOid": ccSnmpAccessV3CustomOid,
       "ccSnmpAccessV3OidLimit": ccSnmpAccessV3OidLimit,
       "ccSnmpAccessV3Access": ccSnmpAccessV3Access,
       "ccSnmpAccessV3AuthAlgorithm": ccSnmpAccessV3AuthAlgorithm,
       "ccSnmpAccessV3AuthPassword": ccSnmpAccessV3AuthPassword,
       "ccSnmpAccessV3PrivacyAlgorithm": ccSnmpAccessV3PrivacyAlgorithm,
       "ccSnmpAccessV3PrivacyPassword": ccSnmpAccessV3PrivacyPassword,
       "ccSnmpAccessV3Enable": ccSnmpAccessV3Enable,
       "ccSnmpAccessControlTable": ccSnmpAccessControlTable,
       "ccSnmpAccessControlEntry": ccSnmpAccessControlEntry,
       "ccSnmpAccessControlIndex": ccSnmpAccessControlIndex,
       "ccSnmpAccessControlStartIp": ccSnmpAccessControlStartIp,
       "ccSnmpAccessControlEndIp": ccSnmpAccessControlEndIp,
       "ccSnmpAccessControlEnable": ccSnmpAccessControlEnable,
       "ccSnmpTraps": ccSnmpTraps,
       "ccSnmpTrapSinkV12Table": ccSnmpTrapSinkV12Table,
       "ccSnmpTrapSinkV12Entry": ccSnmpTrapSinkV12Entry,
       "ccSnmpTrapSinkV12Index": ccSnmpTrapSinkV12Index,
       "ccSnmpTrapSinkV12DestinationIp": ccSnmpTrapSinkV12DestinationIp,
       "ccSnmpTrapSinkV12Port": ccSnmpTrapSinkV12Port,
       "ccSnmpTrapSinkV12Community": ccSnmpTrapSinkV12Community,
       "ccSnmpTrapSinkV12Version": ccSnmpTrapSinkV12Version,
       "ccSnmpTrapSinkV12Enable": ccSnmpTrapSinkV12Enable,
       "ccSnmpTrapSinkV3Table": ccSnmpTrapSinkV3Table,
       "ccSnmpTrapSinkV3Entry": ccSnmpTrapSinkV3Entry,
       "ccSnmpTrapSinkV3Index": ccSnmpTrapSinkV3Index,
       "ccSnmpTrapSinkV3DestinationIp": ccSnmpTrapSinkV3DestinationIp,
       "ccSnmpTrapSinkV3Port": ccSnmpTrapSinkV3Port,
       "ccSnmpTrapSinkV3Username": ccSnmpTrapSinkV3Username,
       "ccSnmpTrapSinkV3SecurityLevel": ccSnmpTrapSinkV3SecurityLevel,
       "ccSnmpTrapSinkV3AuthAlgorithm": ccSnmpTrapSinkV3AuthAlgorithm,
       "ccSnmpTrapSinkV3AuthPassword": ccSnmpTrapSinkV3AuthPassword,
       "ccSnmpTrapSinkV3PrivacyAlgorithm": ccSnmpTrapSinkV3PrivacyAlgorithm,
       "ccSnmpTrapSinkV3PrivacyPassword": ccSnmpTrapSinkV3PrivacyPassword,
       "ccSnmpTrapSinkV3Enable": ccSnmpTrapSinkV3Enable,
       "ccCompactFlash": ccCompactFlash,
       "ccCompactFlashCapacity": ccCompactFlashCapacity,
       "ccCompactFlashUsed": ccCompactFlashUsed,
       "ccSumStats": ccSumStats,
       "ccSumStatsShortWindow": ccSumStatsShortWindow,
       "ccSumStatsShortUpdateInterval": ccSumStatsShortUpdateInterval,
       "ccSumStatsLongWindow": ccSumStatsLongWindow,
       "ccSumStatsLongUpdateInterval": ccSumStatsLongUpdateInterval,
       "ccMgmtAccess": ccMgmtAccess,
       "ccMgmtAccessToAllow": ccMgmtAccessToAllow,
       "ccMgmtAccessAirbeam": ccMgmtAccessAirbeam,
       "ccMgmtAccessAirbeamAllow": ccMgmtAccessAirbeamAllow,
       "ccMgmtAccessAirbeamPassword": ccMgmtAccessAirbeamPassword,
       "ccMgmtAccessAdmin": ccMgmtAccessAdmin,
       "ccMgmtAccessAdminAuth": ccMgmtAccessAdminAuth,
       "ccMgmtAccessAdminPassword": ccMgmtAccessAdminPassword,
       "ccMgmtAccessAdminAuthRadiusServerIp": ccMgmtAccessAdminAuthRadiusServerIp,
       "ccMgmtAccessAdminAuthRadiusServerPort": ccMgmtAccessAdminAuthRadiusServerPort,
       "ccMgmtAccessAdminAuthRadiusSharedSecret": ccMgmtAccessAdminAuthRadiusSharedSecret,
       "ccMgmtAccessSsh": ccMgmtAccessSsh,
       "ccMgmtAccessSshAuthTimeout": ccMgmtAccessSshAuthTimeout,
       "ccMgmtAccessSshInactivityTimeout": ccMgmtAccessSshInactivityTimeout,
       "ccMgmtAccessHttpsTimeout": ccMgmtAccessHttpsTimeout,
       "ccLogging": ccLogging,
       "ccLoggingLevel": ccLoggingLevel,
       "ccLoggingToSyslog": ccLoggingToSyslog,
       "ccLoggingSyslogServer": ccLoggingSyslogServer,
       "ccLoggingDeleteCoreFile": ccLoggingDeleteCoreFile,
       "ccLoggingTransferCoreFile": ccLoggingTransferCoreFile,
       "ccNtp": ccNtp,
       "ccNtpEnable": ccNtpEnable,
       "ccNtp0Server": ccNtp0Server,
       "ccNtp0Port": ccNtp0Port,
       "ccNtp1Server": ccNtp1Server,
       "ccNtp1Port": ccNtp1Port,
       "ccNtp2Server": ccNtp2Server,
       "ccNtp2Port": ccNtp2Port,
       "ccNtpGmtHourOffset": ccNtpGmtHourOffset,
       "ccNtpGmtMinuteOffset": ccNtpGmtMinuteOffset,
       "ccNtpCurrentDateTime": ccNtpCurrentDateTime,
       "ccNtpSyncInterval": ccNtpSyncInterval,
       "ccDhcpOptions": ccDhcpOptions,
       "ccDhcpOptionsUpdateFwEna": ccDhcpOptionsUpdateFwEna,
       "ccDhcpOptionsUpdateCfgEna": ccDhcpOptionsUpdateCfgEna,
       "ccDhcpOptionsUpdateInterface": ccDhcpOptionsUpdateInterface,
       "ccDhcpOptionsUpdateFwFilename": ccDhcpOptionsUpdateFwFilename,
       "ccDhcpOptionsUpdateCfgFilename": ccDhcpOptionsUpdateCfgFilename,
       "ccRedundancy": ccRedundancy,
       "ccRedundancyAdminState": ccRedundancyAdminState,
       "ccRedundancyOperState": ccRedundancyOperState,
       "ccRedundancyHeartbeatInterface": ccRedundancyHeartbeatInterface,
       "ccRedundancyHeartbeatInterval": ccRedundancyHeartbeatInterval,
       "ccRedundancyRevertDelay": ccRedundancyRevertDelay,
       "ccRedundancyOperMode": ccRedundancyOperMode,
       "ccCertMgnt": ccCertMgnt,
       "ccCertMgntSelfCerts": ccCertMgntSelfCerts,
       "ccCertMgntSelfCertsReqTable": ccCertMgntSelfCertsReqTable,
       "ccCertMgntSelfCertsReqEntry": ccCertMgntSelfCertsReqEntry,
       "ccCertMgntSelfCertsReqIndex": ccCertMgntSelfCertsReqIndex,
       "ccCertMgntSelfCertsReqKeyId": ccCertMgntSelfCertsReqKeyId,
       "ccCertMgntSelfCertsReqSubject": ccCertMgntSelfCertsReqSubject,
       "ccCertMgntSelfCertsReqDept": ccCertMgntSelfCertsReqDept,
       "ccCertMgntSelfCertsReqOrg": ccCertMgntSelfCertsReqOrg,
       "ccCertMgntSelfCertsReqCity": ccCertMgntSelfCertsReqCity,
       "ccCertMgntSelfCertsReqState": ccCertMgntSelfCertsReqState,
       "ccCertMgntSelfCertsReqPostal": ccCertMgntSelfCertsReqPostal,
       "ccCertMgntSelfCertsReqCountry": ccCertMgntSelfCertsReqCountry,
       "ccCertMgntSelfCertsReqEmail": ccCertMgntSelfCertsReqEmail,
       "ccCertMgntSelfCertsReqDomain": ccCertMgntSelfCertsReqDomain,
       "ccCertMgntSelfCertsReqIp": ccCertMgntSelfCertsReqIp,
       "ccCertMgntSelfCertsReqSigAlgo": ccCertMgntSelfCertsReqSigAlgo,
       "ccCertMgntSelfCertsReqKeyLen": ccCertMgntSelfCertsReqKeyLen,
       "ccCertMgntSelfCertsReqGenReq": ccCertMgntSelfCertsReqGenReq,
       "ccCertMgntSelfCertsReqCertReqStr": ccCertMgntSelfCertsReqCertReqStr,
       "ccCertMgntSelfCertsReqRowStatus": ccCertMgntSelfCertsReqRowStatus,
       "ccCertMgntSelfCertsIdName": ccCertMgntSelfCertsIdName,
       "ccCertMgntSelfCertsSignedStr": ccCertMgntSelfCertsSignedStr,
       "ccCertMgntSelfCertsSignedImport": ccCertMgntSelfCertsSignedImport,
       "ccCertMgntSelfCertsSignedTable": ccCertMgntSelfCertsSignedTable,
       "ccCertMgntSelfCertsSignedEntry": ccCertMgntSelfCertsSignedEntry,
       "ccCertMgntSelfCertsSignedIndex": ccCertMgntSelfCertsSignedIndex,
       "ccCertMgntSelfCertsSignedKeyId": ccCertMgntSelfCertsSignedKeyId,
       "ccCertMgntSelfCertsSignedIssuerName": ccCertMgntSelfCertsSignedIssuerName,
       "ccCertMgntSelfCertsSignedSubject": ccCertMgntSelfCertsSignedSubject,
       "ccCertMgntSelfCertsSignedSerialNumber": ccCertMgntSelfCertsSignedSerialNumber,
       "ccCertMgntSelfCertsSignedExpiry": ccCertMgntSelfCertsSignedExpiry,
       "ccCertMgntSelfCertsSignedDeleteRow": ccCertMgntSelfCertsSignedDeleteRow,
       "ccCACerts": ccCACerts,
       "ccCACertsStr": ccCACertsStr,
       "ccCACertsImport": ccCACertsImport,
       "ccCACertsTable": ccCACertsTable,
       "ccCACertsEntry": ccCACertsEntry,
       "ccCACertsIndex": ccCACertsIndex,
       "ccCACertsKeyId": ccCACertsKeyId,
       "ccCACertsIssuerName": ccCACertsIssuerName,
       "ccCACertsSubject": ccCACertsSubject,
       "ccCACertsSerialNumber": ccCACertsSerialNumber,
       "ccCACertsExpiry": ccCACertsExpiry,
       "ccCACertsDeleteRow": ccCACertsDeleteRow,
       "ccNotifications": ccNotifications,
       "ccPortalAdopted": ccPortalAdopted,
       "ccPortalUnAdopted": ccPortalUnAdopted,
       "ccPortalDenied": ccPortalDenied,
       "ccMuAssociated": ccMuAssociated,
       "ccMuUnAssociated": ccMuUnAssociated,
       "ccMuDenied": ccMuDenied,
       "ccConfigChange": ccConfigChange,
       "ccSnmpAclViolation": ccSnmpAclViolation,
       "ccPortStatusChange": ccPortStatusChange,
       "ccCfAlmostFull": ccCfAlmostFull,
       "ccFirewallUnderAttack": ccFirewallUnderAttack,
       "ccRadarDetected": ccRadarDetected,
       "ccSumStatsMu": ccSumStatsMu,
       "ccSumStatsPortal": ccSumStatsPortal,
       "ccSumStatsWlan": ccSumStatsWlan,
       "ccSumStatsSwitch": ccSumStatsSwitch,
       "ccLanVlanActivated": ccLanVlanActivated,
       "ccDhcpOptionsFileTransferStatus": ccDhcpOptionsFileTransferStatus,
       "ccRedundancyStateChange": ccRedundancyStateChange,
       "ccTrapCtrl": ccTrapCtrl,
       "ccTrapCtrlEnableTable": ccTrapCtrlEnableTable,
       "ccTrapCtrlEnableEntry": ccTrapCtrlEnableEntry,
       "ccTrapCtrlEnableIndex": ccTrapCtrlEnableIndex,
       "ccTrapCtrlEnableName": ccTrapCtrlEnableName,
       "ccTrapCtrlEnable": ccTrapCtrlEnable,
       "ccTrapCtrlDetails": ccTrapCtrlDetails,
       "ccTrapCtrlPortalAdopted": ccTrapCtrlPortalAdopted,
       "ccTrapCtrlPortalUnAdopted": ccTrapCtrlPortalUnAdopted,
       "ccTrapCtrlPortalDenied": ccTrapCtrlPortalDenied,
       "ccTrapCtrlMuAssociated": ccTrapCtrlMuAssociated,
       "ccTrapCtrlMuUnAssociated": ccTrapCtrlMuUnAssociated,
       "ccTrapCtrlMuDenied": ccTrapCtrlMuDenied,
       "ccTrapCtrlConfigChange": ccTrapCtrlConfigChange,
       "ccTrapCtrlSnmpAclViolation": ccTrapCtrlSnmpAclViolation,
       "ccTrapCtrlPortStatusChange": ccTrapCtrlPortStatusChange,
       "ccTrapCtrlCfAlmostFull": ccTrapCtrlCfAlmostFull,
       "ccTrapCtrlCfAlmostFullThreshold": ccTrapCtrlCfAlmostFullThreshold,
       "ccTrapCtrlFirewallUnderAttack": ccTrapCtrlFirewallUnderAttack,
       "ccTrapCtrlFirewallUnderAttackDescription": ccTrapCtrlFirewallUnderAttackDescription,
       "ccTrapCtrlFirewallUnderAttackRateLimit": ccTrapCtrlFirewallUnderAttackRateLimit,
       "ccTrapCtrlRadarDetected": ccTrapCtrlRadarDetected,
       "ccTrapCtrlRadarDetectedPortalMac": ccTrapCtrlRadarDetectedPortalMac,
       "ccTrapCtrlRadarDetectedChannel": ccTrapCtrlRadarDetectedChannel,
       "ccTrapCtrlSumStats": ccTrapCtrlSumStats,
       "ccTrapCtrlSumStatsTable": ccTrapCtrlSumStatsTable,
       "ccTrapCtrlSumStatsEntry": ccTrapCtrlSumStatsEntry,
       "ccTrapCtrlSumStatsIndex": ccTrapCtrlSumStatsIndex,
       "ccTrapCtrlSumStatsDescr": ccTrapCtrlSumStatsDescr,
       "ccTrapCtrlSumStatsUnits": ccTrapCtrlSumStatsUnits,
       "ccTrapCtrlSumStatsCanBeSetMu": ccTrapCtrlSumStatsCanBeSetMu,
       "ccTrapCtrlSumStatsThresholdMu": ccTrapCtrlSumStatsThresholdMu,
       "ccTrapCtrlSumStatsCanBeSetPortal": ccTrapCtrlSumStatsCanBeSetPortal,
       "ccTrapCtrlSumStatsThresholdPortals": ccTrapCtrlSumStatsThresholdPortals,
       "ccTrapCtrlSumStatsCanBeSetWlan": ccTrapCtrlSumStatsCanBeSetWlan,
       "ccTrapCtrlSumStatsThresholdWlans": ccTrapCtrlSumStatsThresholdWlans,
       "ccTrapCtrlSumStatsCanBeSetSwitch": ccTrapCtrlSumStatsCanBeSetSwitch,
       "ccTrapCtrlSumStatsThresholdSwitch": ccTrapCtrlSumStatsThresholdSwitch,
       "ccTrapCtrlSumStatsMinPktsForTrap": ccTrapCtrlSumStatsMinPktsForTrap,
       "ccTrapCtrlSumStatsPortal": ccTrapCtrlSumStatsPortal,
       "ccTrapCtrlSumStatsWlan": ccTrapCtrlSumStatsWlan,
       "ccTrapCtrlSumStatsSwitch": ccTrapCtrlSumStatsSwitch,
       "ccTrapCtrlLanVlanActivated": ccTrapCtrlLanVlanActivated,
       "ccTrapCtrlLanVlanActivatedVlanId": ccTrapCtrlLanVlanActivatedVlanId,
       "ccTrapCtrlDhcpOptionsFileTransferStatus": ccTrapCtrlDhcpOptionsFileTransferStatus,
       "ccTrapCtrlDhcpOptionsFileTransferStatusRequested": ccTrapCtrlDhcpOptionsFileTransferStatusRequested,
       "ccTrapCtrlRedundancyStateChange": ccTrapCtrlRedundancyStateChange,
       "ccTrapCtrlRedundancyPreviousOperState": ccTrapCtrlRedundancyPreviousOperState,
       "ccRf": ccRf,
       "ccAp": ccAp,
       "ccApTable": ccApTable,
       "ccApEntry": ccApEntry,
       "ccApIndex": ccApIndex,
       "ccApNicMac": ccApNicMac,
       "ccApModelNumber": ccApModelNumber,
       "ccApSerialNumber": ccApSerialNumber,
       "ccApPcbRevision": ccApPcbRevision,
       "ccApBootLoaderRev": ccApBootLoaderRev,
       "ccApWispVersion": ccApWispVersion,
       "ccApRuntimeFwVersion": ccApRuntimeFwVersion,
       "ccApNumPortals": ccApNumPortals,
       "ccApPointersToPortals": ccApPointersToPortals,
       "ccPortal": ccPortal,
       "ccPortalTable": ccPortalTable,
       "ccPortalEntry": ccPortalEntry,
       "ccPortalIndex": ccPortalIndex,
       "ccPortalPointerToAp": ccPortalPointerToAp,
       "ccPortalPointersToWlans": ccPortalPointersToWlans,
       "ccPortalName": ccPortalName,
       "ccPortalLocation": ccPortalLocation,
       "ccPortalOptions": ccPortalOptions,
       "ccPortalMac": ccPortalMac,
       "ccPortalNumberOfEss": ccPortalNumberOfEss,
       "ccPortalNumberOfBss": ccPortalNumberOfBss,
       "ccPortalAssociatedMus": ccPortalAssociatedMus,
       "ccPortalRadioType": ccPortalRadioType,
       "ccPortalChannel": ccPortalChannel,
       "ccPortalTxPowerLevel": ccPortalTxPowerLevel,
       "ccPortalLastAdoption": ccPortalLastAdoption,
       "ccPortalState": ccPortalState,
       "ccPortalBackgroundNoiseNumSamples": ccPortalBackgroundNoiseNumSamples,
       "ccPortalBackgroundNoiseBest": ccPortalBackgroundNoiseBest,
       "ccPortalBackgroundNoiseWorst": ccPortalBackgroundNoiseWorst,
       "ccPortalBackgroundNoiseSum": ccPortalBackgroundNoiseSum,
       "ccPortalBackgroundNoiseSumSquares": ccPortalBackgroundNoiseSumSquares,
       "ccPortalLastMac": ccPortalLastMac,
       "ccPortalLastReason": ccPortalLastReason,
       "ccPortalAdoptionTable": ccPortalAdoptionTable,
       "ccPortalAdoptionEntry": ccPortalAdoptionEntry,
       "ccPortalAdoptionIndex": ccPortalAdoptionIndex,
       "ccPortalAdoptionStartMac": ccPortalAdoptionStartMac,
       "ccPortalAdoptionEndMac": ccPortalAdoptionEndMac,
       "ccPortalAdoptionWlanPointers": ccPortalAdoptionWlanPointers,
       "ccPortalAdoptionRowStatus": ccPortalAdoptionRowStatus,
       "ccPortalSystemStatsTable": ccPortalSystemStatsTable,
       "ccPortalSystemStatsEntry": ccPortalSystemStatsEntry,
       "ccPortalSystemStatsBeaconsTx": ccPortalSystemStatsBeaconsTx,
       "ccPortalSystemStatsBeaconsTxOctets": ccPortalSystemStatsBeaconsTxOctets,
       "ccPortalSystemStatsProbeReqRx": ccPortalSystemStatsProbeReqRx,
       "ccPortalSystemStatsProbeReqRxOctets": ccPortalSystemStatsProbeReqRxOctets,
       "ccPortalSystemStatsProbeRespRetriesNone": ccPortalSystemStatsProbeRespRetriesNone,
       "ccPortalSystemStatsProbeRespRetries1": ccPortalSystemStatsProbeRespRetries1,
       "ccPortalSystemStatsProbeRespRetries2": ccPortalSystemStatsProbeRespRetries2,
       "ccPortalSystemStatsProbeRespRetries3OrMore": ccPortalSystemStatsProbeRespRetries3OrMore,
       "ccPortalSystemStatsProbeRespRetriesFailed": ccPortalSystemStatsProbeRespRetriesFailed,
       "ccPortalSystemStatsProbeRespTxOctets": ccPortalSystemStatsProbeRespTxOctets,
       "ccPortalSettingsTable": ccPortalSettingsTable,
       "ccPortalSettingsEntry": ccPortalSettingsEntry,
       "ccPortalSettingsName": ccPortalSettingsName,
       "ccPortalSettingsLocation": ccPortalSettingsLocation,
       "ccPortalSettingsAntenna": ccPortalSettingsAntenna,
       "ccPortalSettingsShortPreamble": ccPortalSettingsShortPreamble,
       "ccPortalSettingsUniSpread": ccPortalSettingsUniSpread,
       "ccPortalSettingsRtsThresh": ccPortalSettingsRtsThresh,
       "ccPortalSettingsBeaconInt": ccPortalSettingsBeaconInt,
       "ccPortalSettingsDtimPrd": ccPortalSettingsDtimPrd,
       "ccPortalSettingsSecBeacon": ccPortalSettingsSecBeacon,
       "ccPortalSettingsPriWlan": ccPortalSettingsPriWlan,
       "ccPortalSettingsBasicRates": ccPortalSettingsBasicRates,
       "ccPortalSettingsSupportedRates": ccPortalSettingsSupportedRates,
       "ccPortalSettingsBGMode": ccPortalSettingsBGMode,
       "ccPortalSettingsAdoptedWlan": ccPortalSettingsAdoptedWlan,
       "ccPortalSettingsDetector": ccPortalSettingsDetector,
       "ccPortalCfgRadioTable": ccPortalCfgRadioTable,
       "ccPortalCfgRadioEntry": ccPortalCfgRadioEntry,
       "ccPortalCfgRadioDesPlacement": ccPortalCfgRadioDesPlacement,
       "ccPortalCfgRadioPosChannel": ccPortalCfgRadioPosChannel,
       "ccPortalCfgRadioDesChannel": ccPortalCfgRadioDesChannel,
       "ccPortalCfgRadioPosPowerLevel": ccPortalCfgRadioPosPowerLevel,
       "ccPortalCfgRadioDesPowerLevel": ccPortalCfgRadioDesPowerLevel,
       "ccPortalCfgRadioDesPowerInMW": ccPortalCfgRadioDesPowerInMW,
       "ccPortalCfgRadioSet": ccPortalCfgRadioSet,
       "ccPortalCfgRadioReset": ccPortalCfgRadioReset,
       "ccPortalCfgRadioPlacement": ccPortalCfgRadioPlacement,
       "ccPortalCfgRadioChannel": ccPortalCfgRadioChannel,
       "ccPortalCfgRadioPowerLevel": ccPortalCfgRadioPowerLevel,
       "ccPortalCfgRadioPowerInMW": ccPortalCfgRadioPowerInMW,
       "ccPortalSettingsDefaultTable": ccPortalSettingsDefaultTable,
       "ccPortalSettingsDefaultEntry": ccPortalSettingsDefaultEntry,
       "ccPortalSettingsDefaultIndex": ccPortalSettingsDefaultIndex,
       "ccPortalSettingsDefaultAntenna": ccPortalSettingsDefaultAntenna,
       "ccPortalSettingsDefaultShortPreamble": ccPortalSettingsDefaultShortPreamble,
       "ccPortalSettingsDefaultUniSpread": ccPortalSettingsDefaultUniSpread,
       "ccPortalSettingsDefaultRtsThresh": ccPortalSettingsDefaultRtsThresh,
       "ccPortalSettingsDefaultBeaconInt": ccPortalSettingsDefaultBeaconInt,
       "ccPortalSettingsDefaultDtimPrd": ccPortalSettingsDefaultDtimPrd,
       "ccPortalSettingsDefaultSecBeacon": ccPortalSettingsDefaultSecBeacon,
       "ccPortalSettingsDefaultPriWlan": ccPortalSettingsDefaultPriWlan,
       "ccPortalSettingsDefaultBasicRates": ccPortalSettingsDefaultBasicRates,
       "ccPortalSettingsDefaultSupportedRates": ccPortalSettingsDefaultSupportedRates,
       "ccPortalSettingsDefaultBGMode": ccPortalSettingsDefaultBGMode,
       "ccPortalCfgRadioDefaultTable": ccPortalCfgRadioDefaultTable,
       "ccPortalCfgRadioDefaultEntry": ccPortalCfgRadioDefaultEntry,
       "ccPortalCfgRadioDefaultDesPlacement": ccPortalCfgRadioDefaultDesPlacement,
       "ccPortalCfgRadioDefaultPosChannel": ccPortalCfgRadioDefaultPosChannel,
       "ccPortalCfgRadioDefaultDesChannel": ccPortalCfgRadioDefaultDesChannel,
       "ccPortalCfgRadioDefaultPosPowerLevel": ccPortalCfgRadioDefaultPosPowerLevel,
       "ccPortalCfgRadioDefaultDesPowerLevel": ccPortalCfgRadioDefaultDesPowerLevel,
       "ccPortalCfgRadioDefaultDesPowerInMW": ccPortalCfgRadioDefaultDesPowerInMW,
       "ccPortalCfgRadioDefaultSet": ccPortalCfgRadioDefaultSet,
       "ccPortalCfgRadioDefaultReset": ccPortalCfgRadioDefaultReset,
       "ccPortalCfgRadioDefaultPlacement": ccPortalCfgRadioDefaultPlacement,
       "ccPortalCfgRadioDefaultChannel": ccPortalCfgRadioDefaultChannel,
       "ccPortalCfgRadioDefaultPowerLevel": ccPortalCfgRadioDefaultPowerLevel,
       "ccPortalCfgRadioDefaultPowerInMW": ccPortalCfgRadioDefaultPowerInMW,
       "cc802dt1xPortAuth": cc802dt1xPortAuth,
       "cc802dt1xPortAuthLogin": cc802dt1xPortAuthLogin,
       "cc802dt1xPortAuthPass": cc802dt1xPortAuthPass,
       "cc802dt1xPortAuthSetAp300": cc802dt1xPortAuthSetAp300,
       "ccPortalRfSum": ccPortalRfSum,
       "ccPortalStatsTable": ccPortalStatsTable,
       "ccPortalStatsEntry": ccPortalStatsEntry,
       "ccPortalTxPktsUcast": ccPortalTxPktsUcast,
       "ccPortalRxPktsUcast": ccPortalRxPktsUcast,
       "ccPortalRxPktsNUcast": ccPortalRxPktsNUcast,
       "ccPortalTxOctetsUcast": ccPortalTxOctetsUcast,
       "ccPortalRxOctetsUcast": ccPortalRxOctetsUcast,
       "ccPortalRxOctetsNUcast": ccPortalRxOctetsNUcast,
       "ccPortalRxUndecryptablePkts": ccPortalRxUndecryptablePkts,
       "ccPortalLastActivity": ccPortalLastActivity,
       "ccPortalRxPktsTable": ccPortalRxPktsTable,
       "ccPortalRxPktsEntry": ccPortalRxPktsEntry,
       "ccPortalRxPktsAt1Mb": ccPortalRxPktsAt1Mb,
       "ccPortalRxPktsAt2Mb": ccPortalRxPktsAt2Mb,
       "ccPortalRxPktsAt5pt5Mb": ccPortalRxPktsAt5pt5Mb,
       "ccPortalRxPktsAt6Mb": ccPortalRxPktsAt6Mb,
       "ccPortalRxPktsAt9Mb": ccPortalRxPktsAt9Mb,
       "ccPortalRxPktsAt11Mb": ccPortalRxPktsAt11Mb,
       "ccPortalRxPktsAt12Mb": ccPortalRxPktsAt12Mb,
       "ccPortalRxPktsAt18Mb": ccPortalRxPktsAt18Mb,
       "ccPortalRxPktsAt22Mb": ccPortalRxPktsAt22Mb,
       "ccPortalRxPktsAt24Mb": ccPortalRxPktsAt24Mb,
       "ccPortalRxPktsAt36Mb": ccPortalRxPktsAt36Mb,
       "ccPortalRxPktsAt48Mb": ccPortalRxPktsAt48Mb,
       "ccPortalRxPktsAt54Mb": ccPortalRxPktsAt54Mb,
       "ccPortalTxPktsTable": ccPortalTxPktsTable,
       "ccPortalTxPktsEntry": ccPortalTxPktsEntry,
       "ccPortalTxPktsAt1Mb": ccPortalTxPktsAt1Mb,
       "ccPortalTxPktsAt2Mb": ccPortalTxPktsAt2Mb,
       "ccPortalTxPktsAt5pt5Mb": ccPortalTxPktsAt5pt5Mb,
       "ccPortalTxPktsAt6Mb": ccPortalTxPktsAt6Mb,
       "ccPortalTxPktsAt9Mb": ccPortalTxPktsAt9Mb,
       "ccPortalTxPktsAt11Mb": ccPortalTxPktsAt11Mb,
       "ccPortalTxPktsAt12Mb": ccPortalTxPktsAt12Mb,
       "ccPortalTxPktsAt18Mb": ccPortalTxPktsAt18Mb,
       "ccPortalTxPktsAt22Mb": ccPortalTxPktsAt22Mb,
       "ccPortalTxPktsAt24Mb": ccPortalTxPktsAt24Mb,
       "ccPortalTxPktsAt36Mb": ccPortalTxPktsAt36Mb,
       "ccPortalTxPktsAt48Mb": ccPortalTxPktsAt48Mb,
       "ccPortalTxPktsAt54Mb": ccPortalTxPktsAt54Mb,
       "ccPortalRxOctetsTable": ccPortalRxOctetsTable,
       "ccPortalRxOctetsEntry": ccPortalRxOctetsEntry,
       "ccPortalRxOctetsAt1Mb": ccPortalRxOctetsAt1Mb,
       "ccPortalRxOctetsAt2Mb": ccPortalRxOctetsAt2Mb,
       "ccPortalRxOctetsAt5pt5Mb": ccPortalRxOctetsAt5pt5Mb,
       "ccPortalRxOctetsAt6Mb": ccPortalRxOctetsAt6Mb,
       "ccPortalRxOctetsAt9Mb": ccPortalRxOctetsAt9Mb,
       "ccPortalRxOctetsAt11Mb": ccPortalRxOctetsAt11Mb,
       "ccPortalRxOctetsAt12Mb": ccPortalRxOctetsAt12Mb,
       "ccPortalRxOctetsAt18Mb": ccPortalRxOctetsAt18Mb,
       "ccPortalRxOctetsAt22Mb": ccPortalRxOctetsAt22Mb,
       "ccPortalRxOctetsAt24Mb": ccPortalRxOctetsAt24Mb,
       "ccPortalRxOctetsAt36Mb": ccPortalRxOctetsAt36Mb,
       "ccPortalRxOctetsAt48Mb": ccPortalRxOctetsAt48Mb,
       "ccPortalRxOctetsAt54Mb": ccPortalRxOctetsAt54Mb,
       "ccPortalTxOctetsTable": ccPortalTxOctetsTable,
       "ccPortalTxOctetsEntry": ccPortalTxOctetsEntry,
       "ccPortalTxOctetsAt1Mb": ccPortalTxOctetsAt1Mb,
       "ccPortalTxOctetsAt2Mb": ccPortalTxOctetsAt2Mb,
       "ccPortalTxOctetsAt5pt5Mb": ccPortalTxOctetsAt5pt5Mb,
       "ccPortalTxOctetsAt6Mb": ccPortalTxOctetsAt6Mb,
       "ccPortalTxOctetsAt9Mb": ccPortalTxOctetsAt9Mb,
       "ccPortalTxOctetsAt11Mb": ccPortalTxOctetsAt11Mb,
       "ccPortalTxOctetsAt12Mb": ccPortalTxOctetsAt12Mb,
       "ccPortalTxOctetsAt18Mb": ccPortalTxOctetsAt18Mb,
       "ccPortalTxOctetsAt22Mb": ccPortalTxOctetsAt22Mb,
       "ccPortalTxOctetsAt24Mb": ccPortalTxOctetsAt24Mb,
       "ccPortalTxOctetsAt36Mb": ccPortalTxOctetsAt36Mb,
       "ccPortalTxOctetsAt48Mb": ccPortalTxOctetsAt48Mb,
       "ccPortalTxOctetsAt54Mb": ccPortalTxOctetsAt54Mb,
       "ccPortalTxRetriesPktsTable": ccPortalTxRetriesPktsTable,
       "ccPortalTxRetriesPktsEntry": ccPortalTxRetriesPktsEntry,
       "ccPortalTxRetriesPktsNone": ccPortalTxRetriesPktsNone,
       "ccPortalTxRetriesPkts01": ccPortalTxRetriesPkts01,
       "ccPortalTxRetriesPkts02": ccPortalTxRetriesPkts02,
       "ccPortalTxRetriesPkts03": ccPortalTxRetriesPkts03,
       "ccPortalTxRetriesPkts04": ccPortalTxRetriesPkts04,
       "ccPortalTxRetriesPkts05": ccPortalTxRetriesPkts05,
       "ccPortalTxRetriesPkts06": ccPortalTxRetriesPkts06,
       "ccPortalTxRetriesPkts07": ccPortalTxRetriesPkts07,
       "ccPortalTxRetriesPkts08": ccPortalTxRetriesPkts08,
       "ccPortalTxRetriesPkts09": ccPortalTxRetriesPkts09,
       "ccPortalTxRetriesPkts10": ccPortalTxRetriesPkts10,
       "ccPortalTxRetriesPkts11": ccPortalTxRetriesPkts11,
       "ccPortalTxRetriesPkts12": ccPortalTxRetriesPkts12,
       "ccPortalTxRetriesPkts13": ccPortalTxRetriesPkts13,
       "ccPortalTxRetriesPkts14": ccPortalTxRetriesPkts14,
       "ccPortalTxRetriesPkts15": ccPortalTxRetriesPkts15,
       "ccPortalTxRetriesPktsFailed": ccPortalTxRetriesPktsFailed,
       "ccPortalTxRetriesOctetsTable": ccPortalTxRetriesOctetsTable,
       "ccPortalTxRetriesOctetsEntry": ccPortalTxRetriesOctetsEntry,
       "ccPortalTxRetriesOctetsNone": ccPortalTxRetriesOctetsNone,
       "ccPortalTxRetriesOctets01": ccPortalTxRetriesOctets01,
       "ccPortalTxRetriesOctets02": ccPortalTxRetriesOctets02,
       "ccPortalTxRetriesOctets03": ccPortalTxRetriesOctets03,
       "ccPortalTxRetriesOctets04": ccPortalTxRetriesOctets04,
       "ccPortalTxRetriesOctets05": ccPortalTxRetriesOctets05,
       "ccPortalTxRetriesOctets06": ccPortalTxRetriesOctets06,
       "ccPortalTxRetriesOctets07": ccPortalTxRetriesOctets07,
       "ccPortalTxRetriesOctets08": ccPortalTxRetriesOctets08,
       "ccPortalTxRetriesOctets09": ccPortalTxRetriesOctets09,
       "ccPortalTxRetriesOctets10": ccPortalTxRetriesOctets10,
       "ccPortalTxRetriesOctets11": ccPortalTxRetriesOctets11,
       "ccPortalTxRetriesOctets12": ccPortalTxRetriesOctets12,
       "ccPortalTxRetriesOctets13": ccPortalTxRetriesOctets13,
       "ccPortalTxRetriesOctets14": ccPortalTxRetriesOctets14,
       "ccPortalTxRetriesOctets15": ccPortalTxRetriesOctets15,
       "ccPortalTxRetriesOctetsFailed": ccPortalTxRetriesOctetsFailed,
       "ccPortalSigStatsTable": ccPortalSigStatsTable,
       "ccPortalSigStatsEntry": ccPortalSigStatsEntry,
       "ccPortalSigStatsNumPkts": ccPortalSigStatsNumPkts,
       "ccPortalSigStatsSignalBest": ccPortalSigStatsSignalBest,
       "ccPortalSigStatsSignalWorst": ccPortalSigStatsSignalWorst,
       "ccPortalSigStatsSignalSum": ccPortalSigStatsSignalSum,
       "ccPortalSigStatsSignalSumSquares": ccPortalSigStatsSignalSumSquares,
       "ccPortalSigStatsSignalMostRecent": ccPortalSigStatsSignalMostRecent,
       "ccPortalSigStatsNoiseBest": ccPortalSigStatsNoiseBest,
       "ccPortalSigStatsNoiseWorst": ccPortalSigStatsNoiseWorst,
       "ccPortalSigStatsNoiseSum": ccPortalSigStatsNoiseSum,
       "ccPortalSigStatsNoiseSumSquares": ccPortalSigStatsNoiseSumSquares,
       "ccPortalSigStatsNoiseMostRecent": ccPortalSigStatsNoiseMostRecent,
       "ccPortalSigStatsSnrBest": ccPortalSigStatsSnrBest,
       "ccPortalSigStatsSnrWorst": ccPortalSigStatsSnrWorst,
       "ccPortalSigStatsSnrSum": ccPortalSigStatsSnrSum,
       "ccPortalSigStatsSnrSumSquares": ccPortalSigStatsSnrSumSquares,
       "ccPortalSigStatsSnrMostRecent": ccPortalSigStatsSnrMostRecent,
       "ccPortalSumStatsShortTable": ccPortalSumStatsShortTable,
       "ccPortalSumStatsShortEntry": ccPortalSumStatsShortEntry,
       "ccPortalSumStatsShortTimestamp": ccPortalSumStatsShortTimestamp,
       "ccPortalSumStatsShortNumPkts": ccPortalSumStatsShortNumPkts,
       "ccPortalSumStatsShortPktsPerSec100": ccPortalSumStatsShortPktsPerSec100,
       "ccPortalSumStatsShortPktsPerSecTx100": ccPortalSumStatsShortPktsPerSecTx100,
       "ccPortalSumStatsShortPktsPerSecRx100": ccPortalSumStatsShortPktsPerSecRx100,
       "ccPortalSumStatsShortThroughput": ccPortalSumStatsShortThroughput,
       "ccPortalSumStatsShortThroughputTx": ccPortalSumStatsShortThroughputTx,
       "ccPortalSumStatsShortThroughputRx": ccPortalSumStatsShortThroughputRx,
       "ccPortalSumStatsShortAvgBitSpeed": ccPortalSumStatsShortAvgBitSpeed,
       "ccPortalSumStatsShortAvgMuSignal": ccPortalSumStatsShortAvgMuSignal,
       "ccPortalSumStatsShortAvgMuNoise": ccPortalSumStatsShortAvgMuNoise,
       "ccPortalSumStatsShortAvgMuSnr": ccPortalSumStatsShortAvgMuSnr,
       "ccPortalSumStatsShortPp10kNUcastPkts": ccPortalSumStatsShortPp10kNUcastPkts,
       "ccPortalSumStatsShortPp10kTxWithRetries": ccPortalSumStatsShortPp10kTxWithRetries,
       "ccPortalSumStatsShortPp10kTxMaxRetries": ccPortalSumStatsShortPp10kTxMaxRetries,
       "ccPortalSumStatsShortTxAvgRetries100": ccPortalSumStatsShortTxAvgRetries100,
       "ccPortalSumStatsShortPp10kRxUndecrypt": ccPortalSumStatsShortPp10kRxUndecrypt,
       "ccPortalSumStatsShortTotalMus": ccPortalSumStatsShortTotalMus,
       "ccPortalSumStatsShortPp10kRfUtil": ccPortalSumStatsShortPp10kRfUtil,
       "ccPortalSumStatsLongTable": ccPortalSumStatsLongTable,
       "ccPortalSumStatsLongEntry": ccPortalSumStatsLongEntry,
       "ccPortalSumStatsLongTimestamp": ccPortalSumStatsLongTimestamp,
       "ccPortalSumStatsLongNumPkts": ccPortalSumStatsLongNumPkts,
       "ccPortalSumStatsLongPktsPerSec100": ccPortalSumStatsLongPktsPerSec100,
       "ccPortalSumStatsLongPktsPerSecTx100": ccPortalSumStatsLongPktsPerSecTx100,
       "ccPortalSumStatsLongPktsPerSecRx100": ccPortalSumStatsLongPktsPerSecRx100,
       "ccPortalSumStatsLongThroughput": ccPortalSumStatsLongThroughput,
       "ccPortalSumStatsLongThroughputTx": ccPortalSumStatsLongThroughputTx,
       "ccPortalSumStatsLongThroughputRx": ccPortalSumStatsLongThroughputRx,
       "ccPortalSumStatsLongAvgBitSpeed": ccPortalSumStatsLongAvgBitSpeed,
       "ccPortalSumStatsLongAvgMuSignal": ccPortalSumStatsLongAvgMuSignal,
       "ccPortalSumStatsLongAvgMuNoise": ccPortalSumStatsLongAvgMuNoise,
       "ccPortalSumStatsLongAvgMuSnr": ccPortalSumStatsLongAvgMuSnr,
       "ccPortalSumStatsLongPp10kNUcastPkts": ccPortalSumStatsLongPp10kNUcastPkts,
       "ccPortalSumStatsLongPp10kTxWithRetries": ccPortalSumStatsLongPp10kTxWithRetries,
       "ccPortalSumStatsLongPp10kTxMaxRetries": ccPortalSumStatsLongPp10kTxMaxRetries,
       "ccPortalSumStatsLongTxAvgRetries100": ccPortalSumStatsLongTxAvgRetries100,
       "ccPortalSumStatsLongPp10kRxUndecrypt": ccPortalSumStatsLongPp10kRxUndecrypt,
       "ccPortalSumStatsLongTotalMus": ccPortalSumStatsLongTotalMus,
       "ccPortalSumStatsLongPp10kRfUtil": ccPortalSumStatsLongPp10kRfUtil,
       "ccAssociation": ccAssociation,
       "ccAssociationTable": ccAssociationTable,
       "ccAssociationEntry": ccAssociationEntry,
       "ccAssociationFirstAssociate": ccAssociationFirstAssociate,
       "ccAssociationLastAssociate": ccAssociationLastAssociate,
       "ccAssociationCountAssociates": ccAssociationCountAssociates,
       "ccMus": ccMus,
       "ccMuInfoTable": ccMuInfoTable,
       "ccMuInfoEntry": ccMuInfoEntry,
       "ccMuMac": ccMuMac,
       "ccMuWlanIndex": ccMuWlanIndex,
       "ccMuWlanName": ccMuWlanName,
       "ccMuIsDataReady": ccMuIsDataReady,
       "ccMuPortalIndex": ccMuPortalIndex,
       "ccMuPortalMac": ccMuPortalMac,
       "ccMuSymbolRogueApEna": ccMuSymbolRogueApEna,
       "ccMuIpAddr": ccMuIpAddr,
       "ccMuType": ccMuType,
       "ccMuRadioType": ccMuRadioType,
       "ccMuSupportedRates": ccMuSupportedRates,
       "ccMuPowerMode": ccMuPowerMode,
       "ccMuAuthenticationMethod": ccMuAuthenticationMethod,
       "ccMuEncryptionMethod": ccMuEncryptionMethod,
       "ccMuVlanId": ccMuVlanId,
       "ccMuStatsTable": ccMuStatsTable,
       "ccMuStatsEntry": ccMuStatsEntry,
       "ccMuTxPktsUcast": ccMuTxPktsUcast,
       "ccMuRxPktsUcast": ccMuRxPktsUcast,
       "ccMuRxPktsNUcast": ccMuRxPktsNUcast,
       "ccMuTxOctetsUcast": ccMuTxOctetsUcast,
       "ccMuRxOctetsUcast": ccMuRxOctetsUcast,
       "ccMuRxOctetsNUcast": ccMuRxOctetsNUcast,
       "ccMuRxUndecryptablePkts": ccMuRxUndecryptablePkts,
       "ccMuRxRssiNumPkts": ccMuRxRssiNumPkts,
       "ccMuRxRssiSum": ccMuRxRssiSum,
       "ccMuRxRssiSumSquares": ccMuRxRssiSumSquares,
       "ccMuRxRssiMostRecent": ccMuRxRssiMostRecent,
       "ccMuLastActivity": ccMuLastActivity,
       "ccMuRxPktsTable": ccMuRxPktsTable,
       "ccMuRxPktsEntry": ccMuRxPktsEntry,
       "ccMuRxPktsAt1Mb": ccMuRxPktsAt1Mb,
       "ccMuRxPktsAt2Mb": ccMuRxPktsAt2Mb,
       "ccMuRxPktsAt5pt5Mb": ccMuRxPktsAt5pt5Mb,
       "ccMuRxPktsAt6Mb": ccMuRxPktsAt6Mb,
       "ccMuRxPktsAt9Mb": ccMuRxPktsAt9Mb,
       "ccMuRxPktsAt11Mb": ccMuRxPktsAt11Mb,
       "ccMuRxPktsAt12Mb": ccMuRxPktsAt12Mb,
       "ccMuRxPktsAt18Mb": ccMuRxPktsAt18Mb,
       "ccMuRxPktsAt22Mb": ccMuRxPktsAt22Mb,
       "ccMuRxPktsAt24Mb": ccMuRxPktsAt24Mb,
       "ccMuRxPktsAt36Mb": ccMuRxPktsAt36Mb,
       "ccMuRxPktsAt48Mb": ccMuRxPktsAt48Mb,
       "ccMuRxPktsAt54Mb": ccMuRxPktsAt54Mb,
       "ccMuTxPktsTable": ccMuTxPktsTable,
       "ccMuTxPktsEntry": ccMuTxPktsEntry,
       "ccMuTxPktsAt1Mb": ccMuTxPktsAt1Mb,
       "ccMuTxPktsAt2Mb": ccMuTxPktsAt2Mb,
       "ccMuTxPktsAt5pt5Mb": ccMuTxPktsAt5pt5Mb,
       "ccMuTxPktsAt6Mb": ccMuTxPktsAt6Mb,
       "ccMuTxPktsAt9Mb": ccMuTxPktsAt9Mb,
       "ccMuTxPktsAt11Mb": ccMuTxPktsAt11Mb,
       "ccMuTxPktsAt12Mb": ccMuTxPktsAt12Mb,
       "ccMuTxPktsAt18Mb": ccMuTxPktsAt18Mb,
       "ccMuTxPktsAt22Mb": ccMuTxPktsAt22Mb,
       "ccMuTxPktsAt24Mb": ccMuTxPktsAt24Mb,
       "ccMuTxPktsAt36Mb": ccMuTxPktsAt36Mb,
       "ccMuTxPktsAt48Mb": ccMuTxPktsAt48Mb,
       "ccMuTxPktsAt54Mb": ccMuTxPktsAt54Mb,
       "ccMuRxOctetsTable": ccMuRxOctetsTable,
       "ccMuRxOctetsEntry": ccMuRxOctetsEntry,
       "ccMuRxOctetsAt1Mb": ccMuRxOctetsAt1Mb,
       "ccMuRxOctetsAt2Mb": ccMuRxOctetsAt2Mb,
       "ccMuRxOctetsAt5pt5Mb": ccMuRxOctetsAt5pt5Mb,
       "ccMuRxOctetsAt6Mb": ccMuRxOctetsAt6Mb,
       "ccMuRxOctetsAt9Mb": ccMuRxOctetsAt9Mb,
       "ccMuRxOctetsAt11Mb": ccMuRxOctetsAt11Mb,
       "ccMuRxOctetsAt12Mb": ccMuRxOctetsAt12Mb,
       "ccMuRxOctetsAt18Mb": ccMuRxOctetsAt18Mb,
       "ccMuRxOctetsAt22Mb": ccMuRxOctetsAt22Mb,
       "ccMuRxOctetsAt24Mb": ccMuRxOctetsAt24Mb,
       "ccMuRxOctetsAt36Mb": ccMuRxOctetsAt36Mb,
       "ccMuRxOctetsAt48Mb": ccMuRxOctetsAt48Mb,
       "ccMuRxOctetsAt54Mb": ccMuRxOctetsAt54Mb,
       "ccMuTxOctetsTable": ccMuTxOctetsTable,
       "ccMuTxOctetsEntry": ccMuTxOctetsEntry,
       "ccMuTxOctetsAt1Mb": ccMuTxOctetsAt1Mb,
       "ccMuTxOctetsAt2Mb": ccMuTxOctetsAt2Mb,
       "ccMuTxOctetsAt5pt5Mb": ccMuTxOctetsAt5pt5Mb,
       "ccMuTxOctetsAt6Mb": ccMuTxOctetsAt6Mb,
       "ccMuTxOctetsAt9Mb": ccMuTxOctetsAt9Mb,
       "ccMuTxOctetsAt11Mb": ccMuTxOctetsAt11Mb,
       "ccMuTxOctetsAt12Mb": ccMuTxOctetsAt12Mb,
       "ccMuTxOctetsAt18Mb": ccMuTxOctetsAt18Mb,
       "ccMuTxOctetsAt22Mb": ccMuTxOctetsAt22Mb,
       "ccMuTxOctetsAt24Mb": ccMuTxOctetsAt24Mb,
       "ccMuTxOctetsAt36Mb": ccMuTxOctetsAt36Mb,
       "ccMuTxOctetsAt48Mb": ccMuTxOctetsAt48Mb,
       "ccMuTxOctetsAt54Mb": ccMuTxOctetsAt54Mb,
       "ccMuTxRetriesTable": ccMuTxRetriesTable,
       "ccMuTxRetriesEntry": ccMuTxRetriesEntry,
       "ccMuTxRetriesNone": ccMuTxRetriesNone,
       "ccMuTxRetries01": ccMuTxRetries01,
       "ccMuTxRetries02": ccMuTxRetries02,
       "ccMuTxRetries03": ccMuTxRetries03,
       "ccMuTxRetries04": ccMuTxRetries04,
       "ccMuTxRetries05": ccMuTxRetries05,
       "ccMuTxRetries06": ccMuTxRetries06,
       "ccMuTxRetries07": ccMuTxRetries07,
       "ccMuTxRetries08": ccMuTxRetries08,
       "ccMuTxRetries09": ccMuTxRetries09,
       "ccMuTxRetries10": ccMuTxRetries10,
       "ccMuTxRetries11": ccMuTxRetries11,
       "ccMuTxRetries12": ccMuTxRetries12,
       "ccMuTxRetries13": ccMuTxRetries13,
       "ccMuTxRetries14": ccMuTxRetries14,
       "ccMuTxRetries15": ccMuTxRetries15,
       "ccMuTxRetriesFailed": ccMuTxRetriesFailed,
       "ccMuTxRetriesTotal": ccMuTxRetriesTotal,
       "ccMuTxRetriesMostRecent": ccMuTxRetriesMostRecent,
       "ccMuLastMac": ccMuLastMac,
       "ccMuLastReason": ccMuLastReason,
       "ccMuLastPortal": ccMuLastPortal,
       "ccMuRfSum": ccMuRfSum,
       "ccMuTxRetriesOctetsTable": ccMuTxRetriesOctetsTable,
       "ccMuTxRetriesOctetsEntry": ccMuTxRetriesOctetsEntry,
       "ccMuTxRetriesOctetsNone": ccMuTxRetriesOctetsNone,
       "ccMuTxRetriesOctets01": ccMuTxRetriesOctets01,
       "ccMuTxRetriesOctets02": ccMuTxRetriesOctets02,
       "ccMuTxRetriesOctets03": ccMuTxRetriesOctets03,
       "ccMuTxRetriesOctets04": ccMuTxRetriesOctets04,
       "ccMuTxRetriesOctets05": ccMuTxRetriesOctets05,
       "ccMuTxRetriesOctets06": ccMuTxRetriesOctets06,
       "ccMuTxRetriesOctets07": ccMuTxRetriesOctets07,
       "ccMuTxRetriesOctets08": ccMuTxRetriesOctets08,
       "ccMuTxRetriesOctets09": ccMuTxRetriesOctets09,
       "ccMuTxRetriesOctets10": ccMuTxRetriesOctets10,
       "ccMuTxRetriesOctets11": ccMuTxRetriesOctets11,
       "ccMuTxRetriesOctets12": ccMuTxRetriesOctets12,
       "ccMuTxRetriesOctets13": ccMuTxRetriesOctets13,
       "ccMuTxRetriesOctets14": ccMuTxRetriesOctets14,
       "ccMuTxRetriesOctets15": ccMuTxRetriesOctets15,
       "ccMuTxRetriesOctetsFailed": ccMuTxRetriesOctetsFailed,
       "ccMuSigStatsTable": ccMuSigStatsTable,
       "ccMuSigStatsEntry": ccMuSigStatsEntry,
       "ccMuSigStatsNumPkts": ccMuSigStatsNumPkts,
       "ccMuSigStatsSignalBest": ccMuSigStatsSignalBest,
       "ccMuSigStatsSignalWorst": ccMuSigStatsSignalWorst,
       "ccMuSigStatsSignalSum": ccMuSigStatsSignalSum,
       "ccMuSigStatsSignalSumSquares": ccMuSigStatsSignalSumSquares,
       "ccMuSigStatsSignalMostRecent": ccMuSigStatsSignalMostRecent,
       "ccMuSigStatsNoiseBest": ccMuSigStatsNoiseBest,
       "ccMuSigStatsNoiseWorst": ccMuSigStatsNoiseWorst,
       "ccMuSigStatsNoiseSum": ccMuSigStatsNoiseSum,
       "ccMuSigStatsNoiseSumSquares": ccMuSigStatsNoiseSumSquares,
       "ccMuSigStatsNoiseMostRecent": ccMuSigStatsNoiseMostRecent,
       "ccMuSigStatsSnrBest": ccMuSigStatsSnrBest,
       "ccMuSigStatsSnrWorst": ccMuSigStatsSnrWorst,
       "ccMuSigStatsSnrSum": ccMuSigStatsSnrSum,
       "ccMuSigStatsSnrSumSquares": ccMuSigStatsSnrSumSquares,
       "ccMuSigStatsSnrMostRecent": ccMuSigStatsSnrMostRecent,
       "ccMuSumStatsShortTable": ccMuSumStatsShortTable,
       "ccMuSumStatsShortEntry": ccMuSumStatsShortEntry,
       "ccMuSumStatsShortTimestamp": ccMuSumStatsShortTimestamp,
       "ccMuSumStatsShortNumPkts": ccMuSumStatsShortNumPkts,
       "ccMuSumStatsShortPktsPerSec100": ccMuSumStatsShortPktsPerSec100,
       "ccMuSumStatsShortPktsPerSecTx100": ccMuSumStatsShortPktsPerSecTx100,
       "ccMuSumStatsShortPktsPerSecRx100": ccMuSumStatsShortPktsPerSecRx100,
       "ccMuSumStatsShortThroughput": ccMuSumStatsShortThroughput,
       "ccMuSumStatsShortThroughputTx": ccMuSumStatsShortThroughputTx,
       "ccMuSumStatsShortThroughputRx": ccMuSumStatsShortThroughputRx,
       "ccMuSumStatsShortAvgBitSpeed": ccMuSumStatsShortAvgBitSpeed,
       "ccMuSumStatsShortAvgMuSignal": ccMuSumStatsShortAvgMuSignal,
       "ccMuSumStatsShortAvgMuNoise": ccMuSumStatsShortAvgMuNoise,
       "ccMuSumStatsShortAvgMuSnr": ccMuSumStatsShortAvgMuSnr,
       "ccMuSumStatsShortPp10kNUcastPkts": ccMuSumStatsShortPp10kNUcastPkts,
       "ccMuSumStatsShortPp10kTxWithRetries": ccMuSumStatsShortPp10kTxWithRetries,
       "ccMuSumStatsShortPp10kDropped": ccMuSumStatsShortPp10kDropped,
       "ccMuSumStatsShortTxAvgRetries100": ccMuSumStatsShortTxAvgRetries100,
       "ccMuSumStatsShortPp10kRxUndecrypt": ccMuSumStatsShortPp10kRxUndecrypt,
       "ccMuSumStatsLongTable": ccMuSumStatsLongTable,
       "ccMuSumStatsLongEntry": ccMuSumStatsLongEntry,
       "ccMuSumStatsLongTimestamp": ccMuSumStatsLongTimestamp,
       "ccMuSumStatsLongNumPkts": ccMuSumStatsLongNumPkts,
       "ccMuSumStatsLongPktsPerSec100": ccMuSumStatsLongPktsPerSec100,
       "ccMuSumStatsLongPktsPerSecTx100": ccMuSumStatsLongPktsPerSecTx100,
       "ccMuSumStatsLongPktsPerSecRx100": ccMuSumStatsLongPktsPerSecRx100,
       "ccMuSumStatsLongThroughput": ccMuSumStatsLongThroughput,
       "ccMuSumStatsLongThroughputTx": ccMuSumStatsLongThroughputTx,
       "ccMuSumStatsLongThroughputRx": ccMuSumStatsLongThroughputRx,
       "ccMuSumStatsLongAvgBitSpeed": ccMuSumStatsLongAvgBitSpeed,
       "ccMuSumStatsLongAvgMuSignal": ccMuSumStatsLongAvgMuSignal,
       "ccMuSumStatsLongAvgMuNoise": ccMuSumStatsLongAvgMuNoise,
       "ccMuSumStatsLongAvgMuSnr": ccMuSumStatsLongAvgMuSnr,
       "ccMuSumStatsLongPp10kNUcastPkts": ccMuSumStatsLongPp10kNUcastPkts,
       "ccMuSumStatsLongPp10kTxWithRetries": ccMuSumStatsLongPp10kTxWithRetries,
       "ccMuSumStatsLongPp10kDropped": ccMuSumStatsLongPp10kDropped,
       "ccMuSumStatsLongTxAvgRetries100": ccMuSumStatsLongTxAvgRetries100,
       "ccMuSumStatsLongPp10kRxUndecrypt": ccMuSumStatsLongPp10kRxUndecrypt,
       "ccWlan": ccWlan,
       "ccWlanTable": ccWlanTable,
       "ccWlanEntry": ccWlanEntry,
       "ccWlanIndex": ccWlanIndex,
       "ccWlanName": ccWlanName,
       "ccWlanEssid": ccWlanEssid,
       "ccWlanSubnet": ccWlanSubnet,
       "ccWlanPortalsAdopted": ccWlanPortalsAdopted,
       "ccWlanEnable": ccWlanEnable,
       "ccWlanDisallowMuToMu": ccWlanDisallowMuToMu,
       "ccWlanVoicePrioritization": ccWlanVoicePrioritization,
       "ccWlanAnswerBroadcastEss": ccWlanAnswerBroadcastEss,
       "ccWlanMulticastAddr1": ccWlanMulticastAddr1,
       "ccWlanMulticastAddr2": ccWlanMulticastAddr2,
       "ccWlanMuAclDefault": ccWlanMuAclDefault,
       "ccWlanAuthentication": ccWlanAuthentication,
       "ccWlanEncryption": ccWlanEncryption,
       "ccWlanWeight": ccWlanWeight,
       "ccWlanAuth": ccWlanAuth,
       "ccWlanAuthEapTable": ccWlanAuthEapTable,
       "ccWlanAuthEapEntry": ccWlanAuthEapEntry,
       "ccWlanAuthEapReauthenticationEnable": ccWlanAuthEapReauthenticationEnable,
       "ccWlanAuthEapReauthenticationPeriod": ccWlanAuthEapReauthenticationPeriod,
       "ccWlanAuthEapReauthenticationMaxRetries": ccWlanAuthEapReauthenticationMaxRetries,
       "ccWlanAuthEapRadius1Server": ccWlanAuthEapRadius1Server,
       "ccWlanAuthEapRadius1Port": ccWlanAuthEapRadius1Port,
       "ccWlanAuthEapRadius1SharedSecret": ccWlanAuthEapRadius1SharedSecret,
       "ccWlanAuthEapRadius2Server": ccWlanAuthEapRadius2Server,
       "ccWlanAuthEapRadius2Port": ccWlanAuthEapRadius2Port,
       "ccWlanAuthEapRadius2SharedSecret": ccWlanAuthEapRadius2SharedSecret,
       "ccWlanAuthEapMuQuietPeriod": ccWlanAuthEapMuQuietPeriod,
       "ccWlanAuthEapMuTimeout": ccWlanAuthEapMuTimeout,
       "ccWlanAuthEapMuTxPeriod": ccWlanAuthEapMuTxPeriod,
       "ccWlanAuthEapMuMaxRetries": ccWlanAuthEapMuMaxRetries,
       "ccWlanAuthEapServerTimeout": ccWlanAuthEapServerTimeout,
       "ccWlanAuthEapServerMaxRetries": ccWlanAuthEapServerMaxRetries,
       "ccWlanAuthEapRadiusAcctMode": ccWlanAuthEapRadiusAcctMode,
       "ccWlanAuthEapRadiusAcctMuTimeout": ccWlanAuthEapRadiusAcctMuTimeout,
       "ccWlanAuthEapRadiusAcctMuRetries": ccWlanAuthEapRadiusAcctMuRetries,
       "ccWlanAuthEapSyslogMode": ccWlanAuthEapSyslogMode,
       "ccWlanAuthEapSyslogSeverIp": ccWlanAuthEapSyslogSeverIp,
       "ccWlanAuthKerberosTable": ccWlanAuthKerberosTable,
       "ccWlanAuthKerberosEntry": ccWlanAuthKerberosEntry,
       "ccWlanAuthKerberosRealmName": ccWlanAuthKerberosRealmName,
       "ccWlanAuthKerberosUsername": ccWlanAuthKerberosUsername,
       "ccWlanAuthKerberosPassword": ccWlanAuthKerberosPassword,
       "ccWlanAuthKerberosKdcServerIp1": ccWlanAuthKerberosKdcServerIp1,
       "ccWlanAuthKerberosKdcPort1": ccWlanAuthKerberosKdcPort1,
       "ccWlanAuthKerberosKdcServerIp2": ccWlanAuthKerberosKdcServerIp2,
       "ccWlanAuthKerberosKdcPort2": ccWlanAuthKerberosKdcPort2,
       "ccWlanAuthKerberosKdcServerIpR": ccWlanAuthKerberosKdcServerIpR,
       "ccWlanAuthKerberosKdcPortR": ccWlanAuthKerberosKdcPortR,
       "ccWlanCrypto": ccWlanCrypto,
       "ccWlanCryptoWepTable": ccWlanCryptoWepTable,
       "ccWlanCryptoWepEntry": ccWlanCryptoWepEntry,
       "ccWlanCryptoWepPassKey": ccWlanCryptoWepPassKey,
       "ccWlanCryptoWepKey1": ccWlanCryptoWepKey1,
       "ccWlanCryptoWepKey2": ccWlanCryptoWepKey2,
       "ccWlanCryptoWepKey3": ccWlanCryptoWepKey3,
       "ccWlanCryptoWepKey4": ccWlanCryptoWepKey4,
       "ccWlanCryptoWepKeyToUse": ccWlanCryptoWepKeyToUse,
       "ccWlanCryptoWpaTable": ccWlanCryptoWpaTable,
       "ccWlanCryptoWpaEntry": ccWlanCryptoWpaEntry,
       "ccWlanCryptoWpaBcastKeyRotation": ccWlanCryptoWpaBcastKeyRotation,
       "ccWlanCryptoWpaKeyRotationInterval": ccWlanCryptoWpaKeyRotationInterval,
       "ccWlanCryptoWpaKeyToUse": ccWlanCryptoWpaKeyToUse,
       "ccWlanCryptoWpaPassphrase": ccWlanCryptoWpaPassphrase,
       "ccWlanCryptoWpaKey": ccWlanCryptoWpaKey,
       "ccWlanCryptoKeyguardTable": ccWlanCryptoKeyguardTable,
       "ccWlanCryptoKeyguardEntry": ccWlanCryptoKeyguardEntry,
       "ccWlanCryptoKeyguardPasskey": ccWlanCryptoKeyguardPasskey,
       "ccWlanCryptoKeyguardKey1": ccWlanCryptoKeyguardKey1,
       "ccWlanCryptoKeyguardKey2": ccWlanCryptoKeyguardKey2,
       "ccWlanCryptoKeyguardKey3": ccWlanCryptoKeyguardKey3,
       "ccWlanCryptoKeyguardKey4": ccWlanCryptoKeyguardKey4,
       "ccWlanCryptoKeyguardKeyToUse": ccWlanCryptoKeyguardKeyToUse,
       "ccWlanCryptoWpaTwoTable": ccWlanCryptoWpaTwoTable,
       "ccWlanCryptoWpaTwoEntry": ccWlanCryptoWpaTwoEntry,
       "ccWlanCryptoWpaTwoBcastKeyRotation": ccWlanCryptoWpaTwoBcastKeyRotation,
       "ccWlanCryptoWpaTwoKeyRotationInterval": ccWlanCryptoWpaTwoKeyRotationInterval,
       "ccWlanCryptoWpaTwoKeyToUse": ccWlanCryptoWpaTwoKeyToUse,
       "ccWlanCryptoWpaTwoPassphrase": ccWlanCryptoWpaTwoPassphrase,
       "ccWlanCryptoWpaTwoKey": ccWlanCryptoWpaTwoKey,
       "ccWlanCryptoWpaTwoAllowTkipClient": ccWlanCryptoWpaTwoAllowTkipClient,
       "ccWlanCryptoWpaTwoFastRoamPreAuth": ccWlanCryptoWpaTwoFastRoamPreAuth,
       "ccWlanCryptoWpaTwoFastRoamKeyCache": ccWlanCryptoWpaTwoFastRoamKeyCache,
       "ccWlanMuAclTable": ccWlanMuAclTable,
       "ccWlanMuAclEntry": ccWlanMuAclEntry,
       "ccWlanMuAclIndex": ccWlanMuAclIndex,
       "ccWlanMuAclStartingMac": ccWlanMuAclStartingMac,
       "ccWlanMuAclEndingMac": ccWlanMuAclEndingMac,
       "ccWlanMuAclRowStatus": ccWlanMuAclRowStatus,
       "ccWlanBwShareMode": ccWlanBwShareMode,
       "ccWlanQosMonitorTable": ccWlanQosMonitorTable,
       "ccWlanQosMonitorEntry": ccWlanQosMonitorEntry,
       "ccWlanQosMonitorSent": ccWlanQosMonitorSent,
       "ccWlanQosMonitorDropped": ccWlanQosMonitorDropped,
       "ccWlanRfSum": ccWlanRfSum,
       "ccWlanStatsTable": ccWlanStatsTable,
       "ccWlanStatsEntry": ccWlanStatsEntry,
       "ccWlanTxPktsUcast": ccWlanTxPktsUcast,
       "ccWlanRxPktsUcast": ccWlanRxPktsUcast,
       "ccWlanRxPktsNUcast": ccWlanRxPktsNUcast,
       "ccWlanTxOctetsUcast": ccWlanTxOctetsUcast,
       "ccWlanRxOctetsUcast": ccWlanRxOctetsUcast,
       "ccWlanRxOctetsNUcast": ccWlanRxOctetsNUcast,
       "ccWlanRxUndecryptablePkts": ccWlanRxUndecryptablePkts,
       "ccWlanLastActivity": ccWlanLastActivity,
       "ccWlanRxPktsTable": ccWlanRxPktsTable,
       "ccWlanRxPktsEntry": ccWlanRxPktsEntry,
       "ccWlanRxPktsAt1Mb": ccWlanRxPktsAt1Mb,
       "ccWlanRxPktsAt2Mb": ccWlanRxPktsAt2Mb,
       "ccWlanRxPktsAt5pt5Mb": ccWlanRxPktsAt5pt5Mb,
       "ccWlanRxPktsAt6Mb": ccWlanRxPktsAt6Mb,
       "ccWlanRxPktsAt9Mb": ccWlanRxPktsAt9Mb,
       "ccWlanRxPktsAt11Mb": ccWlanRxPktsAt11Mb,
       "ccWlanRxPktsAt12Mb": ccWlanRxPktsAt12Mb,
       "ccWlanRxPktsAt18Mb": ccWlanRxPktsAt18Mb,
       "ccWlanRxPktsAt22Mb": ccWlanRxPktsAt22Mb,
       "ccWlanRxPktsAt24Mb": ccWlanRxPktsAt24Mb,
       "ccWlanRxPktsAt36Mb": ccWlanRxPktsAt36Mb,
       "ccWlanRxPktsAt48Mb": ccWlanRxPktsAt48Mb,
       "ccWlanRxPktsAt54Mb": ccWlanRxPktsAt54Mb,
       "ccWlanTxPktsTable": ccWlanTxPktsTable,
       "ccWlanTxPktsEntry": ccWlanTxPktsEntry,
       "ccWlanTxPktsAt1Mb": ccWlanTxPktsAt1Mb,
       "ccWlanTxPktsAt2Mb": ccWlanTxPktsAt2Mb,
       "ccWlanTxPktsAt5pt5Mb": ccWlanTxPktsAt5pt5Mb,
       "ccWlanTxPktsAt6Mb": ccWlanTxPktsAt6Mb,
       "ccWlanTxPktsAt9Mb": ccWlanTxPktsAt9Mb,
       "ccWlanTxPktsAt11Mb": ccWlanTxPktsAt11Mb,
       "ccWlanTxPktsAt12Mb": ccWlanTxPktsAt12Mb,
       "ccWlanTxPktsAt18Mb": ccWlanTxPktsAt18Mb,
       "ccWlanTxPktsAt22Mb": ccWlanTxPktsAt22Mb,
       "ccWlanTxPktsAt24Mb": ccWlanTxPktsAt24Mb,
       "ccWlanTxPktsAt36Mb": ccWlanTxPktsAt36Mb,
       "ccWlanTxPktsAt48Mb": ccWlanTxPktsAt48Mb,
       "ccWlanTxPktsAt54Mb": ccWlanTxPktsAt54Mb,
       "ccWlanRxOctetsTable": ccWlanRxOctetsTable,
       "ccWlanRxOctetsEntry": ccWlanRxOctetsEntry,
       "ccWlanRxOctetsAt1Mb": ccWlanRxOctetsAt1Mb,
       "ccWlanRxOctetsAt2Mb": ccWlanRxOctetsAt2Mb,
       "ccWlanRxOctetsAt5pt5Mb": ccWlanRxOctetsAt5pt5Mb,
       "ccWlanRxOctetsAt6Mb": ccWlanRxOctetsAt6Mb,
       "ccWlanRxOctetsAt9Mb": ccWlanRxOctetsAt9Mb,
       "ccWlanRxOctetsAt11Mb": ccWlanRxOctetsAt11Mb,
       "ccWlanRxOctetsAt12Mb": ccWlanRxOctetsAt12Mb,
       "ccWlanRxOctetsAt18Mb": ccWlanRxOctetsAt18Mb,
       "ccWlanRxOctetsAt22Mb": ccWlanRxOctetsAt22Mb,
       "ccWlanRxOctetsAt24Mb": ccWlanRxOctetsAt24Mb,
       "ccWlanRxOctetsAt36Mb": ccWlanRxOctetsAt36Mb,
       "ccWlanRxOctetsAt48Mb": ccWlanRxOctetsAt48Mb,
       "ccWlanRxOctetsAt54Mb": ccWlanRxOctetsAt54Mb,
       "ccWlanTxOctetsTable": ccWlanTxOctetsTable,
       "ccWlanTxOctetsEntry": ccWlanTxOctetsEntry,
       "ccWlanTxOctetsAt1Mb": ccWlanTxOctetsAt1Mb,
       "ccWlanTxOctetsAt2Mb": ccWlanTxOctetsAt2Mb,
       "ccWlanTxOctetsAt5pt5Mb": ccWlanTxOctetsAt5pt5Mb,
       "ccWlanTxOctetsAt6Mb": ccWlanTxOctetsAt6Mb,
       "ccWlanTxOctetsAt9Mb": ccWlanTxOctetsAt9Mb,
       "ccWlanTxOctetsAt11Mb": ccWlanTxOctetsAt11Mb,
       "ccWlanTxOctetsAt12Mb": ccWlanTxOctetsAt12Mb,
       "ccWlanTxOctetsAt18Mb": ccWlanTxOctetsAt18Mb,
       "ccWlanTxOctetsAt22Mb": ccWlanTxOctetsAt22Mb,
       "ccWlanTxOctetsAt24Mb": ccWlanTxOctetsAt24Mb,
       "ccWlanTxOctetsAt36Mb": ccWlanTxOctetsAt36Mb,
       "ccWlanTxOctetsAt48Mb": ccWlanTxOctetsAt48Mb,
       "ccWlanTxOctetsAt54Mb": ccWlanTxOctetsAt54Mb,
       "ccWlanTxRetriesPktsTable": ccWlanTxRetriesPktsTable,
       "ccWlanTxRetriesPktsEntry": ccWlanTxRetriesPktsEntry,
       "ccWlanTxRetriesPktsNone": ccWlanTxRetriesPktsNone,
       "ccWlanTxRetriesPkts01": ccWlanTxRetriesPkts01,
       "ccWlanTxRetriesPkts02": ccWlanTxRetriesPkts02,
       "ccWlanTxRetriesPkts03": ccWlanTxRetriesPkts03,
       "ccWlanTxRetriesPkts04": ccWlanTxRetriesPkts04,
       "ccWlanTxRetriesPkts05": ccWlanTxRetriesPkts05,
       "ccWlanTxRetriesPkts06": ccWlanTxRetriesPkts06,
       "ccWlanTxRetriesPkts07": ccWlanTxRetriesPkts07,
       "ccWlanTxRetriesPkts08": ccWlanTxRetriesPkts08,
       "ccWlanTxRetriesPkts09": ccWlanTxRetriesPkts09,
       "ccWlanTxRetriesPkts10": ccWlanTxRetriesPkts10,
       "ccWlanTxRetriesPkts11": ccWlanTxRetriesPkts11,
       "ccWlanTxRetriesPkts12": ccWlanTxRetriesPkts12,
       "ccWlanTxRetriesPkts13": ccWlanTxRetriesPkts13,
       "ccWlanTxRetriesPkts14": ccWlanTxRetriesPkts14,
       "ccWlanTxRetriesPkts15": ccWlanTxRetriesPkts15,
       "ccWlanTxRetriesPktsFailed": ccWlanTxRetriesPktsFailed,
       "ccWlanTxRetriesOctetsTable": ccWlanTxRetriesOctetsTable,
       "ccWlanTxRetriesOctetsEntry": ccWlanTxRetriesOctetsEntry,
       "ccWlanTxRetriesOctetsNone": ccWlanTxRetriesOctetsNone,
       "ccWlanTxRetriesOctets01": ccWlanTxRetriesOctets01,
       "ccWlanTxRetriesOctets02": ccWlanTxRetriesOctets02,
       "ccWlanTxRetriesOctets03": ccWlanTxRetriesOctets03,
       "ccWlanTxRetriesOctets04": ccWlanTxRetriesOctets04,
       "ccWlanTxRetriesOctets05": ccWlanTxRetriesOctets05,
       "ccWlanTxRetriesOctets06": ccWlanTxRetriesOctets06,
       "ccWlanTxRetriesOctets07": ccWlanTxRetriesOctets07,
       "ccWlanTxRetriesOctets08": ccWlanTxRetriesOctets08,
       "ccWlanTxRetriesOctets09": ccWlanTxRetriesOctets09,
       "ccWlanTxRetriesOctets10": ccWlanTxRetriesOctets10,
       "ccWlanTxRetriesOctets11": ccWlanTxRetriesOctets11,
       "ccWlanTxRetriesOctets12": ccWlanTxRetriesOctets12,
       "ccWlanTxRetriesOctets13": ccWlanTxRetriesOctets13,
       "ccWlanTxRetriesOctets14": ccWlanTxRetriesOctets14,
       "ccWlanTxRetriesOctets15": ccWlanTxRetriesOctets15,
       "ccWlanTxRetriesOctetsFailed": ccWlanTxRetriesOctetsFailed,
       "ccWlanSigStatsTable": ccWlanSigStatsTable,
       "ccWlanSigStatsEntry": ccWlanSigStatsEntry,
       "ccWlanSigStatsNumPkts": ccWlanSigStatsNumPkts,
       "ccWlanSigStatsSignalBest": ccWlanSigStatsSignalBest,
       "ccWlanSigStatsSignalWorst": ccWlanSigStatsSignalWorst,
       "ccWlanSigStatsSignalSum": ccWlanSigStatsSignalSum,
       "ccWlanSigStatsSignalSumSquares": ccWlanSigStatsSignalSumSquares,
       "ccWlanSigStatsNoiseBest": ccWlanSigStatsNoiseBest,
       "ccWlanSigStatsNoiseWorst": ccWlanSigStatsNoiseWorst,
       "ccWlanSigStatsNoiseSum": ccWlanSigStatsNoiseSum,
       "ccWlanSigStatsNoiseSumSquares": ccWlanSigStatsNoiseSumSquares,
       "ccWlanSigStatsSnrBest": ccWlanSigStatsSnrBest,
       "ccWlanSigStatsSnrWorst": ccWlanSigStatsSnrWorst,
       "ccWlanSigStatsSnrSum": ccWlanSigStatsSnrSum,
       "ccWlanSigStatsSnrSumSquares": ccWlanSigStatsSnrSumSquares,
       "ccWlanSumStatsShortTable": ccWlanSumStatsShortTable,
       "ccWlanSumStatsShortEntry": ccWlanSumStatsShortEntry,
       "ccWlanSumStatsShortTimestamp": ccWlanSumStatsShortTimestamp,
       "ccWlanSumStatsShortNumPkts": ccWlanSumStatsShortNumPkts,
       "ccWlanSumStatsShortPktsPerSec100": ccWlanSumStatsShortPktsPerSec100,
       "ccWlanSumStatsShortPktsPerSecTx100": ccWlanSumStatsShortPktsPerSecTx100,
       "ccWlanSumStatsShortPktsPerSecRx100": ccWlanSumStatsShortPktsPerSecRx100,
       "ccWlanSumStatsShortThroughput": ccWlanSumStatsShortThroughput,
       "ccWlanSumStatsShortThroughputTx": ccWlanSumStatsShortThroughputTx,
       "ccWlanSumStatsShortThroughputRx": ccWlanSumStatsShortThroughputRx,
       "ccWlanSumStatsShortAvgBitSpeed": ccWlanSumStatsShortAvgBitSpeed,
       "ccWlanSumStatsShortAvgMuSignal": ccWlanSumStatsShortAvgMuSignal,
       "ccWlanSumStatsShortAvgMuNoise": ccWlanSumStatsShortAvgMuNoise,
       "ccWlanSumStatsShortAvgMuSnr": ccWlanSumStatsShortAvgMuSnr,
       "ccWlanSumStatsShortPp10kNUcastPkts": ccWlanSumStatsShortPp10kNUcastPkts,
       "ccWlanSumStatsShortPp10kTxWithRetries": ccWlanSumStatsShortPp10kTxWithRetries,
       "ccWlanSumStatsShortPp10kDropped": ccWlanSumStatsShortPp10kDropped,
       "ccWlanSumStatsShortTxAvgRetries100": ccWlanSumStatsShortTxAvgRetries100,
       "ccWlanSumStatsShortPp10kRxUndecrypt": ccWlanSumStatsShortPp10kRxUndecrypt,
       "ccWlanSumStatsShortTotalMus": ccWlanSumStatsShortTotalMus,
       "ccWlanSumStatsShortSkip1": ccWlanSumStatsShortSkip1,
       "ccWlanSumStatsLongTable": ccWlanSumStatsLongTable,
       "ccWlanSumStatsLongEntry": ccWlanSumStatsLongEntry,
       "ccWlanSumStatsLongTimestamp": ccWlanSumStatsLongTimestamp,
       "ccWlanSumStatsLongNumPkts": ccWlanSumStatsLongNumPkts,
       "ccWlanSumStatsLongPktsPerSec100": ccWlanSumStatsLongPktsPerSec100,
       "ccWlanSumStatsLongPktsPerSecTx100": ccWlanSumStatsLongPktsPerSecTx100,
       "ccWlanSumStatsLongPktsPerSecRx100": ccWlanSumStatsLongPktsPerSecRx100,
       "ccWlanSumStatsLongThroughput": ccWlanSumStatsLongThroughput,
       "ccWlanSumStatsLongThroughputTx": ccWlanSumStatsLongThroughputTx,
       "ccWlanSumStatsLongThroughputRx": ccWlanSumStatsLongThroughputRx,
       "ccWlanSumStatsLongAvgBitSpeed": ccWlanSumStatsLongAvgBitSpeed,
       "ccWlanSumStatsLongAvgMuSignal": ccWlanSumStatsLongAvgMuSignal,
       "ccWlanSumStatsLongAvgMuNoise": ccWlanSumStatsLongAvgMuNoise,
       "ccWlanSumStatsLongAvgMuSnr": ccWlanSumStatsLongAvgMuSnr,
       "ccWlanSumStatsLongPp10kNUcastPkts": ccWlanSumStatsLongPp10kNUcastPkts,
       "ccWlanSumStatsLongPp10kTxWithRetries": ccWlanSumStatsLongPp10kTxWithRetries,
       "ccWlanSumStatsLongPp10kDropped": ccWlanSumStatsLongPp10kDropped,
       "ccWlanSumStatsLongTxAvgRetries100": ccWlanSumStatsLongTxAvgRetries100,
       "ccWlanSumStatsLongPp10kRxUndecrypt": ccWlanSumStatsLongPp10kRxUndecrypt,
       "ccWlanSumStatsLongTotalMus": ccWlanSumStatsLongTotalMus,
       "ccWlanSumStatsLongSkip1": ccWlanSumStatsLongSkip1,
       "ccSwitch": ccSwitch,
       "ccWan": ccWan,
       "ccWanTable": ccWanTable,
       "ccWanEntry": ccWanEntry,
       "ccWanIndex": ccWanIndex,
       "ccWanDhcpEnable": ccWanDhcpEnable,
       "ccWanDhcpIpAddr": ccWanDhcpIpAddr,
       "ccWanDhcpSubnetMask": ccWanDhcpSubnetMask,
       "ccWanDhcpDefaultGateway": ccWanDhcpDefaultGateway,
       "ccWanDhcpPrimaryDnsServer": ccWanDhcpPrimaryDnsServer,
       "ccWanDhcpSecondaryDnsServer": ccWanDhcpSecondaryDnsServer,
       "ccWanSubnetMask": ccWanSubnetMask,
       "ccWanDefaultGateway": ccWanDefaultGateway,
       "ccWanPrimaryDnsServer": ccWanPrimaryDnsServer,
       "ccWanSecondaryDnsServer": ccWanSecondaryDnsServer,
       "ccWanPppoeTable": ccWanPppoeTable,
       "ccWanPppoeEntry": ccWanPppoeEntry,
       "ccWanPppoeEnable": ccWanPppoeEnable,
       "ccWanPppoeUsername": ccWanPppoeUsername,
       "ccWanPppoePassword": ccWanPppoePassword,
       "ccWanPppoeKeepAlive": ccWanPppoeKeepAlive,
       "ccWanPppoeIdleTime": ccWanPppoeIdleTime,
       "ccWanPppoeAuthType": ccWanPppoeAuthType,
       "ccWanIpAddrTable": ccWanIpAddrTable,
       "ccWanIpAddrEntry": ccWanIpAddrEntry,
       "ccWanIpAddrIndex": ccWanIpAddrIndex,
       "ccWanIpAddrEnable": ccWanIpAddrEnable,
       "ccWanIpAddr": ccWanIpAddr,
       "ccWanFirewall": ccWanFirewall,
       "ccWanFirewallGlobalEnable": ccWanFirewallGlobalEnable,
       "ccWanFirewallTable": ccWanFirewallTable,
       "ccWanFirewallEntry": ccWanFirewallEntry,
       "ccWanFirewallIndex": ccWanFirewallIndex,
       "ccWanFirewallDescription": ccWanFirewallDescription,
       "ccWanFirewallAlwaysEnabled": ccWanFirewallAlwaysEnabled,
       "ccWanFirewallEnable": ccWanFirewallEnable,
       "ccWanFirewallMimeFloodMaxHeaderLength": ccWanFirewallMimeFloodMaxHeaderLength,
       "ccWanFirewallMimeFloodMaxHeaders": ccWanFirewallMimeFloodMaxHeaders,
       "ccWanNatTimeout": ccWanNatTimeout,
       "ccWanNat": ccWanNat,
       "ccWanNatLowestUnusedSlot": ccWanNatLowestUnusedSlot,
       "ccWanNatTable": ccWanNatTable,
       "ccWanNatEntry": ccWanNatEntry,
       "ccWanNatIndex": ccWanNatIndex,
       "ccWanNatWanIpAddress": ccWanNatWanIpAddress,
       "ccWanNatType": ccWanNatType,
       "ccWanNat1to1IpAddr": ccWanNat1to1IpAddr,
       "ccWanNatInboundDefaultEna": ccWanNatInboundDefaultEna,
       "ccWanNatInboundDefaultIp": ccWanNatInboundDefaultIp,
       "ccWanNatInboundTable": ccWanNatInboundTable,
       "ccWanNatInboundEntry": ccWanNatInboundEntry,
       "ccWanNatInboundIndex": ccWanNatInboundIndex,
       "ccWanNatInboundName": ccWanNatInboundName,
       "ccWanNatInboundTransport": ccWanNatInboundTransport,
       "ccWanNatInboundStartPort": ccWanNatInboundStartPort,
       "ccWanNatInboundEndPort": ccWanNatInboundEndPort,
       "ccWanNatInboundIpAddr": ccWanNatInboundIpAddr,
       "ccWanNatInboundTranslationPort": ccWanNatInboundTranslationPort,
       "ccWanNatInboundRowStatus": ccWanNatInboundRowStatus,
       "ccWanNatOutboundTable": ccWanNatOutboundTable,
       "ccWanNatOutboundEntry": ccWanNatOutboundEntry,
       "ccWanNatOutboundSubnetIndex": ccWanNatOutboundSubnetIndex,
       "ccWanNatOutboundEnable": ccWanNatOutboundEnable,
       "ccWanNatOutboundPossibleIpAddr": ccWanNatOutboundPossibleIpAddr,
       "ccWanNatOutboundIpAddr": ccWanNatOutboundIpAddr,
       "ccWanVpn": ccWanVpn,
       "ccWanVpnTunnelConfig": ccWanVpnTunnelConfig,
       "ccWanVpnTable": ccWanVpnTable,
       "ccWanVpnEntry": ccWanVpnEntry,
       "ccWanVpnIndex": ccWanVpnIndex,
       "ccWanVpnName": ccWanVpnName,
       "ccWanVpnLocalSubnet": ccWanVpnLocalSubnet,
       "ccWanVpnLocalWanIp": ccWanVpnLocalWanIp,
       "ccWanVpnRemoteSubnet": ccWanVpnRemoteSubnet,
       "ccWanVpnRemoteSubnetMask": ccWanVpnRemoteSubnetMask,
       "ccWanVpnRemoteGateway": ccWanVpnRemoteGateway,
       "ccWanVpnKeyExchange": ccWanVpnKeyExchange,
       "ccWanVpnRowStatus": ccWanVpnRowStatus,
       "ccWanVpnKeyManualTable": ccWanVpnKeyManualTable,
       "ccWanVpnKeyManualEntry": ccWanVpnKeyManualEntry,
       "ccWanVpnKeyManualAhAuth": ccWanVpnKeyManualAhAuth,
       "ccWanVpnKeyManualInAhAuthKey": ccWanVpnKeyManualInAhAuthKey,
       "ccWanVpnKeyManualOutAhAuthKey": ccWanVpnKeyManualOutAhAuthKey,
       "ccWanVpnKeyManualInAhSpi": ccWanVpnKeyManualInAhSpi,
       "ccWanVpnKeyManualOutAhSpi": ccWanVpnKeyManualOutAhSpi,
       "ccWanVpnKeyManualEspType": ccWanVpnKeyManualEspType,
       "ccWanVpnKeyManualEspEncrypAlg": ccWanVpnKeyManualEspEncrypAlg,
       "ccWanVpnKeyManualInEspEncrypKey": ccWanVpnKeyManualInEspEncrypKey,
       "ccWanVpnKeyManualOutEspEncrypKey": ccWanVpnKeyManualOutEspEncrypKey,
       "ccWanVpnKeyManualEspAuthAlg": ccWanVpnKeyManualEspAuthAlg,
       "ccWanVpnKeyManualInEspAuthKey": ccWanVpnKeyManualInEspAuthKey,
       "ccWanVpnKeyManualOutEspAuthKey": ccWanVpnKeyManualOutEspAuthKey,
       "ccWanVpnKeyManualInEspSpi": ccWanVpnKeyManualInEspSpi,
       "ccWanVpnKeyManualOutEspSpi": ccWanVpnKeyManualOutEspSpi,
       "ccWanVpnKeyAutoTable": ccWanVpnKeyAutoTable,
       "ccWanVpnKeyAutoEntry": ccWanVpnKeyAutoEntry,
       "ccWanVpnKeyAutoUsePerfectSecrecy": ccWanVpnKeyAutoUsePerfectSecrecy,
       "ccWanVpnKeyAutoAhAuth": ccWanVpnKeyAutoAhAuth,
       "ccWanVpnKeyAutoEspType": ccWanVpnKeyAutoEspType,
       "ccWanVpnKeyAutoEspEncrypAlg": ccWanVpnKeyAutoEspEncrypAlg,
       "ccWanVpnKeyAutoEspAuthAlg": ccWanVpnKeyAutoEspAuthAlg,
       "ccWanVpnKeyAutoIkeOperationMode": ccWanVpnKeyAutoIkeOperationMode,
       "ccWanVpnKeyAutoIkeLocalIdType": ccWanVpnKeyAutoIkeLocalIdType,
       "ccWanVpnKeyAutoIkeLocalIdData": ccWanVpnKeyAutoIkeLocalIdData,
       "ccWanVpnKeyAutoIkeRemoteIdType": ccWanVpnKeyAutoIkeRemoteIdType,
       "ccWanVpnKeyAutoIkeRemoteIdData": ccWanVpnKeyAutoIkeRemoteIdData,
       "ccWanVpnKeyAutoIkeAuthType": ccWanVpnKeyAutoIkeAuthType,
       "ccWanVpnKeyAutoIkeAuthAlg": ccWanVpnKeyAutoIkeAuthAlg,
       "ccWanVpnKeyAutoIkeAuthPassphrase": ccWanVpnKeyAutoIkeAuthPassphrase,
       "ccWanVpnKeyAutoIkeEncrypAlg": ccWanVpnKeyAutoIkeEncrypAlg,
       "ccWanVpnKeyAutoIkeXauthMode": ccWanVpnKeyAutoIkeXauthMode,
       "ccWanVpnKeyAutoIkeXauthUsername": ccWanVpnKeyAutoIkeXauthUsername,
       "ccWanVpnKeyAutoIkeXauthPassword": ccWanVpnKeyAutoIkeXauthPassword,
       "ccWanVpnKeyAutoIkeKeyLifetime": ccWanVpnKeyAutoIkeKeyLifetime,
       "ccWanVpnKeyAutoIkeDiffieHelmanGroup": ccWanVpnKeyAutoIkeDiffieHelmanGroup,
       "ccWanVpnTunnelStatus": ccWanVpnTunnelStatus,
       "ccWanVpnSaTable": ccWanVpnSaTable,
       "ccWanVpnSaEntry": ccWanVpnSaEntry,
       "ccWanVpnSaTunnelName": ccWanVpnSaTunnelName,
       "ccWanVpnSaStatus": ccWanVpnSaStatus,
       "ccWanVpnSaInSpi": ccWanVpnSaInSpi,
       "ccWanVpnSaOutSpi": ccWanVpnSaOutSpi,
       "ccWanVpnSaLifetime": ccWanVpnSaLifetime,
       "ccWanVpnSaTxBytes": ccWanVpnSaTxBytes,
       "ccWanVpnSaRxBytes": ccWanVpnSaRxBytes,
       "ccWanVpnIkeTable": ccWanVpnIkeTable,
       "ccWanVpnIkeEntry": ccWanVpnIkeEntry,
       "ccWanVpnIkeTunnelName": ccWanVpnIkeTunnelName,
       "ccWanVpnIkeState": ccWanVpnIkeState,
       "ccWanVpnIkeRemainingLife": ccWanVpnIkeRemainingLife,
       "ccWanContentBlock": ccWanContentBlock,
       "ccWanContentBlockSmtp": ccWanContentBlockSmtp,
       "ccWanContentBlockFtp": ccWanContentBlockFtp,
       "ccWanContentBlockHttp": ccWanContentBlockHttp,
       "ccWanContentBlockOutUrlTable": ccWanContentBlockOutUrlTable,
       "ccWanContentBlockOutUrlEntry": ccWanContentBlockOutUrlEntry,
       "ccWanContentBlockOutUrlIndex": ccWanContentBlockOutUrlIndex,
       "ccWanContentBlockOutUrlExtension": ccWanContentBlockOutUrlExtension,
       "ccWanContentBlockOutUrlRowStatus": ccWanContentBlockOutUrlRowStatus,
       "ccPort": ccPort,
       "ccPortTable": ccPortTable,
       "ccPortEntry": ccPortEntry,
       "ccPortIndex": ccPortIndex,
       "ccPortType": ccPortType,
       "ccPortPoeEquipped": ccPortPoeEquipped,
       "ccPortStatus": ccPortStatus,
       "ccPortDuplex": ccPortDuplex,
       "ccPortSpeed": ccPortSpeed,
       "ccLan": ccLan,
       "ccSubnet": ccSubnet,
       "ccSubnetTable": ccSubnetTable,
       "ccSubnetEntry": ccSubnetEntry,
       "ccSubnetIndex": ccSubnetIndex,
       "ccSubnetEnable": ccSubnetEnable,
       "ccSubnetName": ccSubnetName,
       "ccSubnetIpAddress": ccSubnetIpAddress,
       "ccSubnetIpSubnetMask": ccSubnetIpSubnetMask,
       "ccSubnetPortMembers": ccSubnetPortMembers,
       "ccSubnetWlanMembers": ccSubnetWlanMembers,
       "ccSubnetDhcpState": ccSubnetDhcpState,
       "ccSubnetDhcpIpAddress": ccSubnetDhcpIpAddress,
       "ccSubnetDhcpSubnetMask": ccSubnetDhcpSubnetMask,
       "ccSubnetDhcpServerTable": ccSubnetDhcpServerTable,
       "ccSubnetDhcpServerEntry": ccSubnetDhcpServerEntry,
       "ccSubnetDhcpServerEnable": ccSubnetDhcpServerEnable,
       "ccSubnetDhcpServerPoolStart": ccSubnetDhcpServerPoolStart,
       "ccSubnetDhcpServerPoolEnd": ccSubnetDhcpServerPoolEnd,
       "ccSubnetDhcpServerPrimaryDns": ccSubnetDhcpServerPrimaryDns,
       "ccSubnetDhcpServerSecondaryDns": ccSubnetDhcpServerSecondaryDns,
       "ccSubnetDhcpServerDefaultGateway": ccSubnetDhcpServerDefaultGateway,
       "ccSubnetDhcpServerLeaseTime": ccSubnetDhcpServerLeaseTime,
       "ccSubnetDhcpServerWinsServer": ccSubnetDhcpServerWinsServer,
       "ccSubnetDhcpServerDomainName": ccSubnetDhcpServerDomainName,
       "ccSubnetDhcpServerStaticMapTable": ccSubnetDhcpServerStaticMapTable,
       "ccSubnetDhcpServerStaticMapEntry": ccSubnetDhcpServerStaticMapEntry,
       "ccSubnetDhcpServerStaticMapMac": ccSubnetDhcpServerStaticMapMac,
       "ccSubnetDhcpServerStaticMapIpAddr": ccSubnetDhcpServerStaticMapIpAddr,
       "ccSubnetDhcpServerStaticMapEnable": ccSubnetDhcpServerStaticMapEnable,
       "ccSubnetAccess": ccSubnetAccess,
       "ccSubnetAccessTable": ccSubnetAccessTable,
       "ccSubnetAccessEntry": ccSubnetAccessEntry,
       "ccSubnetAccessDestIndex": ccSubnetAccessDestIndex,
       "ccSubnetAccessDestType": ccSubnetAccessDestType,
       "ccSubnetAccessDestPtrToDest": ccSubnetAccessDestPtrToDest,
       "ccSubnetAccessRuleType": ccSubnetAccessRuleType,
       "ccSubnetAccessPtrToRules": ccSubnetAccessPtrToRules,
       "ccSubnetAccessRuleTable": ccSubnetAccessRuleTable,
       "ccSubnetAccessRuleEntry": ccSubnetAccessRuleEntry,
       "ccSubnetAccessRuleIndex": ccSubnetAccessRuleIndex,
       "ccSubnetAccessRuleSrcPtr": ccSubnetAccessRuleSrcPtr,
       "ccSubnetAccessRuleDestPtr": ccSubnetAccessRuleDestPtr,
       "ccSubnetAccessRuleName": ccSubnetAccessRuleName,
       "ccSubnetAccessRuleTransport": ccSubnetAccessRuleTransport,
       "ccSubnetAccessRuleStartPort": ccSubnetAccessRuleStartPort,
       "ccSubnetAccessRuleEndPort": ccSubnetAccessRuleEndPort,
       "ccSubnetAccessRuleRowStatus": ccSubnetAccessRuleRowStatus,
       "ccSubnetAccessAdvInTable": ccSubnetAccessAdvInTable,
       "ccSubnetAccessAdvInEntry": ccSubnetAccessAdvInEntry,
       "ccSubnetAccessAdvInIndex": ccSubnetAccessAdvInIndex,
       "ccSubnetAccessAdvInSrcIp": ccSubnetAccessAdvInSrcIp,
       "ccSubnetAccessAdvInSrcIpLength": ccSubnetAccessAdvInSrcIpLength,
       "ccSubnetAccessAdvInDestIp": ccSubnetAccessAdvInDestIp,
       "ccSubnetAccessAdvInDestIpLength": ccSubnetAccessAdvInDestIpLength,
       "ccSubnetAccessAdvInTransport": ccSubnetAccessAdvInTransport,
       "ccSubnetAccessAdvInSrcPortStart": ccSubnetAccessAdvInSrcPortStart,
       "ccSubnetAccessAdvInSrcPortEnd": ccSubnetAccessAdvInSrcPortEnd,
       "ccSubnetAccessAdvInDestPortStart": ccSubnetAccessAdvInDestPortStart,
       "ccSubnetAccessAdvInDestPortEnd": ccSubnetAccessAdvInDestPortEnd,
       "ccSubnetAccessAdvInReverseNatIp": ccSubnetAccessAdvInReverseNatIp,
       "ccSubnetAccessAdvInReverseNatPort": ccSubnetAccessAdvInReverseNatPort,
       "ccSubnetAccessAdvInAction": ccSubnetAccessAdvInAction,
       "ccSubnetAccessAdvInRowStatus": ccSubnetAccessAdvInRowStatus,
       "ccSubnetAccessAdvOutTable": ccSubnetAccessAdvOutTable,
       "ccSubnetAccessAdvOutEntry": ccSubnetAccessAdvOutEntry,
       "ccSubnetAccessAdvOutIndex": ccSubnetAccessAdvOutIndex,
       "ccSubnetAccessAdvOutSrcIp": ccSubnetAccessAdvOutSrcIp,
       "ccSubnetAccessAdvOutSrcIpLength": ccSubnetAccessAdvOutSrcIpLength,
       "ccSubnetAccessAdvOutDestIp": ccSubnetAccessAdvOutDestIp,
       "ccSubnetAccessAdvOutDestIpLength": ccSubnetAccessAdvOutDestIpLength,
       "ccSubnetAccessAdvOutTransport": ccSubnetAccessAdvOutTransport,
       "ccSubnetAccessAdvOutSrcPortStart": ccSubnetAccessAdvOutSrcPortStart,
       "ccSubnetAccessAdvOutSrcPortEnd": ccSubnetAccessAdvOutSrcPortEnd,
       "ccSubnetAccessAdvOutDestPortStart": ccSubnetAccessAdvOutDestPortStart,
       "ccSubnetAccessAdvOutDestPortEnd": ccSubnetAccessAdvOutDestPortEnd,
       "ccSubnetAccessAdvOutReverseNat": ccSubnetAccessAdvOutReverseNat,
       "ccSubnetAccessAdvOutAction": ccSubnetAccessAdvOutAction,
       "ccSubnetAccessAdvOutRowStatus": ccSubnetAccessAdvOutRowStatus,
       "ccSubnetAccessAdvOverrideMode": ccSubnetAccessAdvOverrideMode,
       "ccSubnetAccessAdvImportRules": ccSubnetAccessAdvImportRules,
       "ccLanVlan": ccLanVlan,
       "ccLanVlanType": ccLanVlanType,
       "ccLanVlanTrunkPort": ccLanVlanTrunkPort,
       "ccLanVlanDefaultTag": ccLanVlanDefaultTag,
       "ccLanVlanTrunked": ccLanVlanTrunked,
       "ccLanVlanTable": ccLanVlanTable,
       "ccLanVlanEntry": ccLanVlanEntry,
       "ccLanVlanId": ccLanVlanId,
       "ccRouter": ccRouter,
       "ccRouterRip": ccRouterRip,
       "ccRouterRipType": ccRouterRipType,
       "ccRouterRipDirection": ccRouterRipDirection,
       "ccRouterRip2": ccRouterRip2,
       "ccRouterRip2AuthType": ccRouterRip2AuthType,
       "ccRouterRip2SimplePassword": ccRouterRip2SimplePassword,
       "ccRouterRip2Md5Key1Id": ccRouterRip2Md5Key1Id,
       "ccRouterRip2Md5Key1AuthKey": ccRouterRip2Md5Key1AuthKey,
       "ccRouterRip2Md5Key2Id": ccRouterRip2Md5Key2Id,
       "ccRouterRip2Md5Key2AuthKey": ccRouterRip2Md5Key2AuthKey,
       "ccRouterRoutesTable": ccRouterRoutesTable,
       "ccRouterRoutesEntry": ccRouterRoutesEntry,
       "ccRouterRoutesIndex": ccRouterRoutesIndex,
       "ccRouterRoutesDest": ccRouterRoutesDest,
       "ccRouterRoutesDestMask": ccRouterRoutesDestMask,
       "ccRouterRoutesGateway": ccRouterRoutesGateway,
       "ccRouterRoutesInterface": ccRouterRoutesInterface,
       "ccRouterRoutesMetric": ccRouterRoutesMetric,
       "ccRouterUserRoutesTable": ccRouterUserRoutesTable,
       "ccRouterUserRoutesEntry": ccRouterUserRoutesEntry,
       "ccRouterUserRoutesIndex": ccRouterUserRoutesIndex,
       "ccRouterUserRoutesDest": ccRouterUserRoutesDest,
       "ccRouterUserRoutesDestMask": ccRouterUserRoutesDestMask,
       "ccRouterUserRoutesGateway": ccRouterUserRoutesGateway,
       "ccRouterUserRoutesInterface": ccRouterUserRoutesInterface,
       "ccRouterUserRoutesMetric": ccRouterUserRoutesMetric,
       "ccRouterUserRoutesRowStatus": ccRouterUserRoutesRowStatus,
       "ccRap": ccRap,
       "ccRapControl": ccRapControl,
       "ccRapControlPollSymbolMus": ccRapControlPollSymbolMus,
       "ccRapPollSymbolMusEnable": ccRapPollSymbolMusEnable,
       "ccRapPollSymbolMusInterval": ccRapPollSymbolMusInterval,
       "ccRapControlOnChannel": ccRapControlOnChannel,
       "ccRapOnChannelEnable": ccRapOnChannelEnable,
       "ccRapOnChannelInterval": ccRapOnChannelInterval,
       "ccRapControlDetectors": ccRapControlDetectors,
       "ccRapDetectorsEnable": ccRapDetectorsEnable,
       "ccRapDetectorsInterval": ccRapDetectorsInterval,
       "ccRapAuth": ccRapAuth,
       "ccRapAuthList": ccRapAuthList,
       "ccRapAuthAllSymbolMac": ccRapAuthAllSymbolMac,
       "ccRapAuthTable": ccRapAuthTable,
       "ccRapAuthEntry": ccRapAuthEntry,
       "ccRapAuthIndex": ccRapAuthIndex,
       "ccRapAuthMacFilter": ccRapAuthMacFilter,
       "ccRapAuthEssidFilter": ccRapAuthEssidFilter,
       "ccRapAuthRowExists": ccRapAuthRowExists,
       "ccRapAuthErase": ccRapAuthErase,
       "ccRapAuthCopyAllApproved": ccRapAuthCopyAllApproved,
       "ccRapAuthCopyAllRogue": ccRapAuthCopyAllRogue,
       "ccRapResults": ccRapResults,
       "ccRapResultsApproved": ccRapResultsApproved,
       "ccRapResultsApprovedAgeOut": ccRapResultsApprovedAgeOut,
       "ccRapResultsApprovedTable": ccRapResultsApprovedTable,
       "ccRapResultsApprovedEntry": ccRapResultsApprovedEntry,
       "ccRapResultsApprovedIndex": ccRapResultsApprovedIndex,
       "ccRapResultsApprovedApMac": ccRapResultsApprovedApMac,
       "ccRapResultsApprovedEssid": ccRapResultsApprovedEssid,
       "ccRapResultsApprovedCopyToAuthTable": ccRapResultsApprovedCopyToAuthTable,
       "ccRapResultsApprovedFirstHeard": ccRapResultsApprovedFirstHeard,
       "ccRapResultsApprovedLastHeard": ccRapResultsApprovedLastHeard,
       "ccRapResultsApprovedPortalPtr": ccRapResultsApprovedPortalPtr,
       "ccRapResultsApprovedHowFound": ccRapResultsApprovedHowFound,
       "ccRapResultsApprovedHowAuth": ccRapResultsApprovedHowAuth,
       "ccRapResultsApprovedChannel": ccRapResultsApprovedChannel,
       "ccRapResultsApprovedErase": ccRapResultsApprovedErase,
       "ccRapNewApprovedAp": ccRapNewApprovedAp,
       "ccRapResultsRogue": ccRapResultsRogue,
       "ccRapResultsRogueAgeOut": ccRapResultsRogueAgeOut,
       "ccRapResultsRogueTable": ccRapResultsRogueTable,
       "ccRapResultsRogueEntry": ccRapResultsRogueEntry,
       "ccRapResultsRogueIndex": ccRapResultsRogueIndex,
       "ccRapResultsRogueApMac": ccRapResultsRogueApMac,
       "ccRapResultsRogueEssid": ccRapResultsRogueEssid,
       "ccRapResultsRogueCopyToAuthTable": ccRapResultsRogueCopyToAuthTable,
       "ccRapResultsRogueFirstHeard": ccRapResultsRogueFirstHeard,
       "ccRapResultsRogueLastHeard": ccRapResultsRogueLastHeard,
       "ccRapResultsRoguePortalPtr": ccRapResultsRoguePortalPtr,
       "ccRapResultsRogueHowFound": ccRapResultsRogueHowFound,
       "ccRapResultsRogueClosestPortalPtr": ccRapResultsRogueClosestPortalPtr,
       "ccRapResultsRogueClosestPortalRssi": ccRapResultsRogueClosestPortalRssi,
       "ccRapResultsRogueChannel": ccRapResultsRogueChannel,
       "ccRapResultsRogueErase": ccRapResultsRogueErase,
       "ccRapNewRogueAp": ccRapNewRogueAp,
       "ccRapLocate": ccRapLocate,
       "ccRapPortalResults": ccRapPortalResults,
       "ccRapPortalResultsApMac": ccRapPortalResultsApMac,
       "ccRapPortalResultsApEssid": ccRapPortalResultsApEssid,
       "ccRapPortalResultsInProcess": ccRapPortalResultsInProcess,
       "ccRapPortalResultsTable": ccRapPortalResultsTable,
       "ccRapPortalResultsEntry": ccRapPortalResultsEntry,
       "ccRapPortalResultsIndex": ccRapPortalResultsIndex,
       "ccRapPortalResultsPortalMac": ccRapPortalResultsPortalMac,
       "ccRapPortalResultsRssi": ccRapPortalResultsRssi,
       "ccRapPollOneMu": ccRapPollOneMu,
       "ccRapPollOneMuMac": ccRapPollOneMuMac,
       "ccRapPollOneMuInProcess": ccRapPollOneMuInProcess,
       "ccRapPollOneMuStatus": ccRapPollOneMuStatus,
       "ccRapPollOneMuResultsTable": ccRapPollOneMuResultsTable,
       "ccRapPollOneMuResultsEntry": ccRapPollOneMuResultsEntry,
       "ccRapPollOneMuResultsIndex": ccRapPollOneMuResultsIndex,
       "ccRapPollOneMuResultsRssi": ccRapPollOneMuResultsRssi,
       "ccRapPollOneMuResultsEssid": ccRapPollOneMuResultsEssid,
       "ccRapPollOneMuResultsApMac": ccRapPollOneMuResultsApMac,
       "ccRadiusServer": ccRadiusServer,
       "ccRadius": ccRadius,
       "ccRadiusDataSource": ccRadiusDataSource,
       "ccRadiusDefaultEapType": ccRadiusDefaultEapType,
       "ccRadiusAuthTypePeap": ccRadiusAuthTypePeap,
       "ccRadiusAuthTypeTtls": ccRadiusAuthTypeTtls,
       "ccRadiusServerCertificate": ccRadiusServerCertificate,
       "ccRadiusCACertificate": ccRadiusCACertificate,
       "ccRadiusClientAuthTable": ccRadiusClientAuthTable,
       "ccRadiusClientAuthEntry": ccRadiusClientAuthEntry,
       "ccRadiusClientAuthIndex": ccRadiusClientAuthIndex,
       "ccRadiusClientAuthIpAddr": ccRadiusClientAuthIpAddr,
       "ccRadiusClientAuthMask": ccRadiusClientAuthMask,
       "ccRadiusClientAuthSharedSecret": ccRadiusClientAuthSharedSecret,
       "ccRadiusClientAuthRowStatus": ccRadiusClientAuthRowStatus,
       "ccRadiusProxy": ccRadiusProxy,
       "ccRadiusProxyRetryCount": ccRadiusProxyRetryCount,
       "ccRadiusProxyTimeout": ccRadiusProxyTimeout,
       "ccRadiusProxyServerTable": ccRadiusProxyServerTable,
       "ccRadiusProxyServerEntry": ccRadiusProxyServerEntry,
       "ccRadiusProxyServerIndex": ccRadiusProxyServerIndex,
       "ccRadiusProxyServerPrefixOrSuffix": ccRadiusProxyServerPrefixOrSuffix,
       "ccRadiusProxyServerIp": ccRadiusProxyServerIp,
       "ccRadiusProxyServerPort": ccRadiusProxyServerPort,
       "ccRadiusProxyServerSharedSecret": ccRadiusProxyServerSharedSecret,
       "ccRadiusProxyServerRowStatus": ccRadiusProxyServerRowStatus,
       "ccRadiusLdap": ccRadiusLdap,
       "ccRadiusLdapServerIp": ccRadiusLdapServerIp,
       "ccRadiusLdapServerPort": ccRadiusLdapServerPort,
       "ccRadiusLdapLoginAttribute": ccRadiusLdapLoginAttribute,
       "ccRadiusLdapPasswordAttribute": ccRadiusLdapPasswordAttribute,
       "ccRadiusLdapBindDistinguishedName": ccRadiusLdapBindDistinguishedName,
       "ccRadiusLdapBindDistinguishedPassword": ccRadiusLdapBindDistinguishedPassword,
       "ccRadiusLdapBaseDistinguishedName": ccRadiusLdapBaseDistinguishedName,
       "ccRadiusLdapGroupAttribute": ccRadiusLdapGroupAttribute,
       "ccRadiusLdapGroupFilter": ccRadiusLdapGroupFilter,
       "ccRadiusLdapGroupMembershipAttribute": ccRadiusLdapGroupMembershipAttribute,
       "ccRadiusUsers": ccRadiusUsers,
       "ccRadiusUsersGroupTable": ccRadiusUsersGroupTable,
       "ccRadiusUsersGroupEntry": ccRadiusUsersGroupEntry,
       "ccRadiusUsersGroup": ccRadiusUsersGroup,
       "ccRadiusUsersGroupRowStatus": ccRadiusUsersGroupRowStatus,
       "ccRadiusUsersGroupId": ccRadiusUsersGroupId,
       "ccRadiusUsersTable": ccRadiusUsersTable,
       "ccRadiusUsersEntry": ccRadiusUsersEntry,
       "ccRadiusUsersId": ccRadiusUsersId,
       "ccRadiusUsersPassword": ccRadiusUsersPassword,
       "ccRadiusUsersGroups": ccRadiusUsersGroups,
       "ccRadiusUsersRowStatus": ccRadiusUsersRowStatus,
       "ccRadiusAccess": ccRadiusAccess,
       "ccRadiusAccessTable": ccRadiusAccessTable,
       "ccRadiusAccessEntry": ccRadiusAccessEntry,
       "ccRadiusAccessWlanPtrs": ccRadiusAccessWlanPtrs,
       "ccGroups": ccGroups,
       "ccGroupsV1dot0": ccGroupsV1dot0,
       "ccAdminGroup": ccAdminGroup,
       "ccNotificationsGroup": ccNotificationsGroup,
       "ccApGroup": ccApGroup,
       "ccPortalGroup": ccPortalGroup,
       "ccAssociationGroup": ccAssociationGroup,
       "ccMuGroup": ccMuGroup,
       "ccGroupsV1dot5": ccGroupsV1dot5,
       "ccGroupsV1dot5variables": ccGroupsV1dot5variables,
       "ccGroupsV1dot5obsoleted": ccGroupsV1dot5obsoleted,
       "ccGroupsV1dot5notifications": ccGroupsV1dot5notifications,
       "ccGroupsV2dot0": ccGroupsV2dot0,
       "ccGroupsV2dot0variables": ccGroupsV2dot0variables,
       "ccGroupsV2dot0obsoleted": ccGroupsV2dot0obsoleted,
       "ccGroupsV2dot0notifications": ccGroupsV2dot0notifications}
)
