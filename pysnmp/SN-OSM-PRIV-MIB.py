# SNMP MIB module (SN-OSM-PRIV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SN-OSM-PRIV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:55:43 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 internet,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "internet",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class IANAifType(Integer32):
    """Custom type IANAifType based on Integer32"""
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
              53,
              54)
        )
    )
    namedValues = NamedValues(
        *(("aal5", 49),
          ("arcnet", 35),
          ("arcnetPlus", 36),
          ("atm", 37),
          ("basicISDN", 20),
          ("ddnX25", 4),
          ("ds1", 18),
          ("ds3", 30),
          ("e1", 19),
          ("eon", 25),
          ("ethernet3Mbit", 26),
          ("ethernetCsmacd", 6),
          ("fddi", 15),
          ("frameRelay", 32),
          ("frameRelayService", 44),
          ("hdh1822", 3),
          ("hippi", 47),
          ("hssi", 46),
          ("hyperchannel", 14),
          ("iso88022llc", 41),
          ("iso88023Csmacd", 7),
          ("iso88024TokenBus", 8),
          ("iso88025TokenRing", 9),
          ("iso88026Man", 10),
          ("lapb", 16),
          ("localTalk", 42),
          ("miox25", 38),
          ("modem", 48),
          ("nsip", 27),
          ("other", 1),
          ("para", 34),
          ("ppp", 23),
          ("primaryISDN", 21),
          ("propMultiplexor", 54),
          ("propPointToPointSerial", 22),
          ("propVirtual", 53),
          ("proteon10Mbit", 12),
          ("proteon80Mbit", 13),
          ("regular1822", 2),
          ("rfc877x25", 5),
          ("rs232", 33),
          ("sdlc", 17),
          ("sip", 31),
          ("slip", 28),
          ("smdsDxi", 43),
          ("smdsIcip", 52),
          ("softwareLoopback", 24),
          ("sonet", 39),
          ("sonetPath", 50),
          ("sonetVT", 51),
          ("starLan", 11),
          ("ultra", 29),
          ("v35", 45),
          ("x25ple", 40))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ad_ObjectIdentity = ObjectIdentity
ad = _Ad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196)
)
_AdProductMibs_ObjectIdentity = ObjectIdentity
adProductMibs = _AdProductMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1)
)
_SimaticNet_ObjectIdentity = ObjectIdentity
simaticNet = _SimaticNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1)
)
_IHub_ObjectIdentity = ObjectIdentity
iHub = _IHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 1)
)
_ISwitch_ObjectIdentity = ObjectIdentity
iSwitch = _ISwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2)
)
_SnOsmItp62_ObjectIdentity = ObjectIdentity
snOsmItp62 = _SnOsmItp62_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 1)
)
_SnOsmItp53_ObjectIdentity = ObjectIdentity
snOsmItp53 = _SnOsmItp53_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 2)
)
_SnOsmItpLd62_ObjectIdentity = ObjectIdentity
snOsmItpLd62 = _SnOsmItpLd62_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 3)
)
_SnEsmItp80_ObjectIdentity = ObjectIdentity
snEsmItp80 = _SnEsmItp80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 4)
)
_SnOsmTp62_ObjectIdentity = ObjectIdentity
snOsmTp62 = _SnOsmTp62_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 5)
)
_SnEsmTp80_ObjectIdentity = ObjectIdentity
snEsmTp80 = _SnEsmTp80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 6)
)
_SnOsmBC08_ObjectIdentity = ObjectIdentity
snOsmBC08 = _SnOsmBC08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 7)
)
_SnOsmTpLd62_ObjectIdentity = ObjectIdentity
snOsmTpLd62 = _SnOsmTpLd62_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 8)
)
_SnOsmTp22_ObjectIdentity = ObjectIdentity
snOsmTp22 = _SnOsmTp22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 9)
)
_SnEsmTp40_ObjectIdentity = ObjectIdentity
snEsmTp40 = _SnEsmTp40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 10)
)
_SnOsmTp62_Advanced_ObjectIdentity = ObjectIdentity
snOsmTp62_Advanced = _SnOsmTp62_Advanced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 11)
)
_SnEsmItp80_Advanced_ObjectIdentity = ObjectIdentity
snEsmItp80_Advanced = _SnEsmItp80_Advanced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 12)
)
_SnEsmTp80_Advanced_ObjectIdentity = ObjectIdentity
snEsmTp80_Advanced = _SnEsmTp80_Advanced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 13)
)
_SnOsmItpLd62_Advanced_ObjectIdentity = ObjectIdentity
snOsmItpLd62_Advanced = _SnOsmItpLd62_Advanced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 14)
)
_SnOsmItp62_Advanced_ObjectIdentity = ObjectIdentity
snOsmItp62_Advanced = _SnOsmItp62_Advanced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 15)
)
_SnOsmItp53_Advanced_ObjectIdentity = ObjectIdentity
snOsmItp53_Advanced = _SnOsmItp53_Advanced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 16)
)
_SnOsmTp53_ObjectIdentity = ObjectIdentity
snOsmTp53 = _SnOsmTp53_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 17)
)
_ISwitchMib_ObjectIdentity = ObjectIdentity
iSwitchMib = _ISwitchMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100)
)
_SnCommon_ObjectIdentity = ObjectIdentity
snCommon = _SnCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1)
)
_SnDownload_ObjectIdentity = ObjectIdentity
snDownload = _SnDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 5)
)
_SnDownloadParams_ObjectIdentity = ObjectIdentity
snDownloadParams = _SnDownloadParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 5, 1)
)


class _SnDownloadParamsTftpServerHostName_Type(DisplayString):
    """Custom type snDownloadParamsTftpServerHostName based on DisplayString"""
    defaultValue = OctetString("0.0.0.0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SnDownloadParamsTftpServerHostName_Type.__name__ = "DisplayString"
_SnDownloadParamsTftpServerHostName_Object = MibScalar
snDownloadParamsTftpServerHostName = _SnDownloadParamsTftpServerHostName_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 5, 1, 2),
    _SnDownloadParamsTftpServerHostName_Type()
)
snDownloadParamsTftpServerHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDownloadParamsTftpServerHostName.setStatus("mandatory")


class _SnDownloadParamsFile_Type(DisplayString):
    """Custom type snDownloadParamsFile based on DisplayString"""
    defaultValue = OctetString("Not Defined Yet")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnDownloadParamsFile_Type.__name__ = "DisplayString"
_SnDownloadParamsFile_Object = MibScalar
snDownloadParamsFile = _SnDownloadParamsFile_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 5, 1, 3),
    _SnDownloadParamsFile_Type()
)
snDownloadParamsFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDownloadParamsFile.setStatus("mandatory")


class _SnDownloadParamsControl_Type(Integer32):
    """Custom type snDownloadParamsControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cancel-load", 3),
          ("start-load", 2))
    )


_SnDownloadParamsControl_Type.__name__ = "Integer32"
_SnDownloadParamsControl_Object = MibScalar
snDownloadParamsControl = _SnDownloadParamsControl_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 5, 1, 4),
    _SnDownloadParamsControl_Type()
)
snDownloadParamsControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    snDownloadParamsControl.setStatus("mandatory")


class _SnDownloadParamsStatus_Type(Integer32):
    """Custom type snDownloadParamsStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("load-in-progress", 2),
          ("load-inactive", 3),
          ("load-interrupted", 4))
    )


_SnDownloadParamsStatus_Type.__name__ = "Integer32"
_SnDownloadParamsStatus_Object = MibScalar
snDownloadParamsStatus = _SnDownloadParamsStatus_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 5, 1, 5),
    _SnDownloadParamsStatus_Type()
)
snDownloadParamsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDownloadParamsStatus.setStatus("mandatory")


class _SnDownloadNextBlockId_Type(Integer32):
    """Custom type snDownloadNextBlockId based on Integer32"""
    defaultValue = 0


_SnDownloadNextBlockId_Object = MibScalar
snDownloadNextBlockId = _SnDownloadNextBlockId_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 5, 1, 6),
    _SnDownloadNextBlockId_Type()
)
snDownloadNextBlockId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDownloadNextBlockId.setStatus("mandatory")
_SnDownloadParamsError_Type = DisplayString
_SnDownloadParamsError_Object = MibScalar
snDownloadParamsError = _SnDownloadParamsError_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 5, 1, 7),
    _SnDownloadParamsError_Type()
)
snDownloadParamsError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDownloadParamsError.setStatus("mandatory")


class _SnDownloadAutoLoad_Type(Integer32):
    """Custom type snDownloadAutoLoad based on Integer32"""
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


_SnDownloadAutoLoad_Type.__name__ = "Integer32"
_SnDownloadAutoLoad_Object = MibScalar
snDownloadAutoLoad = _SnDownloadAutoLoad_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 5, 1, 8),
    _SnDownloadAutoLoad_Type()
)
snDownloadAutoLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDownloadAutoLoad.setStatus("mandatory")


class _SnDownloadEventLogTableFile_Type(DisplayString):
    """Custom type snDownloadEventLogTableFile based on DisplayString"""
    defaultValue = OctetString("Not Defined Yet")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnDownloadEventLogTableFile_Type.__name__ = "DisplayString"
_SnDownloadEventLogTableFile_Object = MibScalar
snDownloadEventLogTableFile = _SnDownloadEventLogTableFile_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 5, 1, 9),
    _SnDownloadEventLogTableFile_Type()
)
snDownloadEventLogTableFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDownloadEventLogTableFile.setStatus("mandatory")


class _SnDownloadEventLogTableControl_Type(Integer32):
    """Custom type snDownloadEventLogTableControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("abort-process", 6),
          ("cancel", 4),
          ("continue-process", 5),
          ("start-load", 2),
          ("start-save", 3))
    )


_SnDownloadEventLogTableControl_Type.__name__ = "Integer32"
_SnDownloadEventLogTableControl_Object = MibScalar
snDownloadEventLogTableControl = _SnDownloadEventLogTableControl_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 5, 1, 10),
    _SnDownloadEventLogTableControl_Type()
)
snDownloadEventLogTableControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    snDownloadEventLogTableControl.setStatus("mandatory")


class _SnDownloadConfigFile_Type(DisplayString):
    """Custom type snDownloadConfigFile based on DisplayString"""
    defaultValue = OctetString("Not Defined Yet")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnDownloadConfigFile_Type.__name__ = "DisplayString"
_SnDownloadConfigFile_Object = MibScalar
snDownloadConfigFile = _SnDownloadConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 5, 1, 11),
    _SnDownloadConfigFile_Type()
)
snDownloadConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDownloadConfigFile.setStatus("mandatory")


class _SnDownloadConfigControl_Type(Integer32):
    """Custom type snDownloadConfigControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("abort-process", 6),
          ("cancel", 4),
          ("continue-process", 5),
          ("start-load", 2),
          ("start-save", 3))
    )


_SnDownloadConfigControl_Type.__name__ = "Integer32"
_SnDownloadConfigControl_Object = MibScalar
snDownloadConfigControl = _SnDownloadConfigControl_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 5, 1, 12),
    _SnDownloadConfigControl_Type()
)
snDownloadConfigControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    snDownloadConfigControl.setStatus("mandatory")
_SnNvLog_ObjectIdentity = ObjectIdentity
snNvLog = _SnNvLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 6)
)


class _SnNvLogMaxEntries_Type(Integer32):
    """Custom type snNvLogMaxEntries based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 400),
    )


_SnNvLogMaxEntries_Type.__name__ = "Integer32"
_SnNvLogMaxEntries_Object = MibScalar
snNvLogMaxEntries = _SnNvLogMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 6, 1),
    _SnNvLogMaxEntries_Type()
)
snNvLogMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snNvLogMaxEntries.setStatus("mandatory")


class _SnNvLogCurrentEntries_Type(Integer32):
    """Custom type snNvLogCurrentEntries based on Integer32"""
    defaultValue = 0


_SnNvLogCurrentEntries_Object = MibScalar
snNvLogCurrentEntries = _SnNvLogCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 6, 2),
    _SnNvLogCurrentEntries_Type()
)
snNvLogCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snNvLogCurrentEntries.setStatus("mandatory")


class _SnNvLogNewEntries_Type(Integer32):
    """Custom type snNvLogNewEntries based on Integer32"""
    defaultValue = 0


_SnNvLogNewEntries_Object = MibScalar
snNvLogNewEntries = _SnNvLogNewEntries_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 6, 3),
    _SnNvLogNewEntries_Type()
)
snNvLogNewEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snNvLogNewEntries.setStatus("mandatory")


class _SnNvLogClear_Type(Integer32):
    """Custom type snNvLogClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_SnNvLogClear_Type.__name__ = "Integer32"
_SnNvLogClear_Object = MibScalar
snNvLogClear = _SnNvLogClear_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 6, 4),
    _SnNvLogClear_Type()
)
snNvLogClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    snNvLogClear.setStatus("mandatory")
_SnNvLogTable_Object = MibTable
snNvLogTable = _SnNvLogTable_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 6, 5)
)
if mibBuilder.loadTexts:
    snNvLogTable.setStatus("mandatory")
_SnNvLogEntry_Object = MibTableRow
snNvLogEntry = _SnNvLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 6, 5, 1)
)
snNvLogEntry.setIndexNames(
    (0, "SN-OSM-PRIV-MIB", "snNvLogPowerUpCount"),
    (0, "SN-OSM-PRIV-MIB", "snNvLogTime"),
    (0, "SN-OSM-PRIV-MIB", "snNvLogSequenceNumber"),
)
if mibBuilder.loadTexts:
    snNvLogEntry.setStatus("mandatory")


class _SnNvLogPowerUpCount_Type(Integer32):
    """Custom type snNvLogPowerUpCount based on Integer32"""
    defaultValue = 0


_SnNvLogPowerUpCount_Object = MibTableColumn
snNvLogPowerUpCount = _SnNvLogPowerUpCount_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 6, 5, 1, 1),
    _SnNvLogPowerUpCount_Type()
)
snNvLogPowerUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snNvLogPowerUpCount.setStatus("mandatory")


class _SnNvLogTime_Type(TimeTicks):
    """Custom type snNvLogTime based on TimeTicks"""
    defaultValue = 0


_SnNvLogTime_Object = MibTableColumn
snNvLogTime = _SnNvLogTime_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 6, 5, 1, 2),
    _SnNvLogTime_Type()
)
snNvLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snNvLogTime.setStatus("mandatory")


class _SnNvLogSequenceNumber_Type(Integer32):
    """Custom type snNvLogSequenceNumber based on Integer32"""
    defaultValue = 0


_SnNvLogSequenceNumber_Object = MibTableColumn
snNvLogSequenceNumber = _SnNvLogSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 6, 5, 1, 3),
    _SnNvLogSequenceNumber_Type()
)
snNvLogSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snNvLogSequenceNumber.setStatus("mandatory")


class _SnNvLogDescr_Type(DisplayString):
    """Custom type snNvLogDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SnNvLogDescr_Type.__name__ = "DisplayString"
_SnNvLogDescr_Object = MibTableColumn
snNvLogDescr = _SnNvLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 6, 5, 1, 4),
    _SnNvLogDescr_Type()
)
snNvLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snNvLogDescr.setStatus("mandatory")


class _SnNvLogPositionDescr_Type(DisplayString):
    """Custom type snNvLogPositionDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnNvLogPositionDescr_Type.__name__ = "DisplayString"
_SnNvLogPositionDescr_Object = MibScalar
snNvLogPositionDescr = _SnNvLogPositionDescr_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 6, 6),
    _SnNvLogPositionDescr_Type()
)
snNvLogPositionDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snNvLogPositionDescr.setStatus("mandatory")
_SnTrapInfo_ObjectIdentity = ObjectIdentity
snTrapInfo = _SnTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 7)
)


class _SnSwitchTrapsEnable_Type(Integer32):
    """Custom type snSwitchTrapsEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("not-supported", 10))
    )


_SnSwitchTrapsEnable_Type.__name__ = "Integer32"
_SnSwitchTrapsEnable_Object = MibScalar
snSwitchTrapsEnable = _SnSwitchTrapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 7, 1),
    _SnSwitchTrapsEnable_Type()
)
snSwitchTrapsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwitchTrapsEnable.setStatus("mandatory")


class _SnTrapTimeLastGenerated_Type(TimeTicks):
    """Custom type snTrapTimeLastGenerated based on TimeTicks"""
    defaultValue = 0


_SnTrapTimeLastGenerated_Object = MibScalar
snTrapTimeLastGenerated = _SnTrapTimeLastGenerated_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 7, 5),
    _SnTrapTimeLastGenerated_Type()
)
snTrapTimeLastGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snTrapTimeLastGenerated.setStatus("mandatory")


class _SnTrapMaxManagers_Type(Integer32):
    """Custom type snTrapMaxManagers based on Integer32"""
    defaultValue = 10


_SnTrapMaxManagers_Object = MibScalar
snTrapMaxManagers = _SnTrapMaxManagers_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 7, 6),
    _SnTrapMaxManagers_Type()
)
snTrapMaxManagers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snTrapMaxManagers.setStatus("mandatory")
_SnTrapTable_Object = MibTable
snTrapTable = _SnTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 7, 7)
)
if mibBuilder.loadTexts:
    snTrapTable.setStatus("mandatory")
_SnTrapEntry_Object = MibTableRow
snTrapEntry = _SnTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 7, 7, 1)
)
snTrapEntry.setIndexNames(
    (0, "SN-OSM-PRIV-MIB", "snTrapIndex"),
)
if mibBuilder.loadTexts:
    snTrapEntry.setStatus("mandatory")


class _SnTrapAddress_Type(IpAddress):
    """Custom type snTrapAddress based on IpAddress"""
    defaultValue = 0


_SnTrapAddress_Object = MibTableColumn
snTrapAddress = _SnTrapAddress_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 7, 7, 1, 1),
    _SnTrapAddress_Type()
)
snTrapAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snTrapAddress.setStatus("mandatory")


class _SnTrapState_Type(Integer32):
    """Custom type snTrapState based on Integer32"""
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
        *(("active", 2),
          ("inactive", 3),
          ("other", 1))
    )


_SnTrapState_Type.__name__ = "Integer32"
_SnTrapState_Object = MibTableColumn
snTrapState = _SnTrapState_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 7, 7, 1, 3),
    _SnTrapState_Type()
)
snTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snTrapState.setStatus("mandatory")


class _SnTrapIndex_Type(Integer32):
    """Custom type snTrapIndex based on Integer32"""
    defaultValue = 0


_SnTrapIndex_Object = MibTableColumn
snTrapIndex = _SnTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 7, 7, 1, 6),
    _SnTrapIndex_Type()
)
snTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snTrapIndex.setStatus("mandatory")
_SnGen_ObjectIdentity = ObjectIdentity
snGen = _SnGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 8)
)


class _SnUserDescription_Type(DisplayString):
    """Custom type snUserDescription based on DisplayString"""
    defaultValue = OctetString("Not Defined Yet")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnUserDescription_Type.__name__ = "DisplayString"
_SnUserDescription_Object = MibScalar
snUserDescription = _SnUserDescription_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 8, 1),
    _SnUserDescription_Type()
)
snUserDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snUserDescription.setStatus("mandatory")


class _SnHwVersion_Type(DisplayString):
    """Custom type snHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SnHwVersion_Type.__name__ = "DisplayString"
_SnHwVersion_Object = MibScalar
snHwVersion = _SnHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 8, 2),
    _SnHwVersion_Type()
)
snHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snHwVersion.setStatus("mandatory")


class _SnBootStrapVersion_Type(DisplayString):
    """Custom type snBootStrapVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SnBootStrapVersion_Type.__name__ = "DisplayString"
_SnBootStrapVersion_Object = MibScalar
snBootStrapVersion = _SnBootStrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 8, 3),
    _SnBootStrapVersion_Type()
)
snBootStrapVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBootStrapVersion.setStatus("mandatory")


class _SnSwVersion_Type(DisplayString):
    """Custom type snSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnSwVersion_Type.__name__ = "DisplayString"
_SnSwVersion_Object = MibScalar
snSwVersion = _SnSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 8, 4),
    _SnSwVersion_Type()
)
snSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwVersion.setStatus("mandatory")


class _SnInfoOrderNr_Type(DisplayString):
    """Custom type snInfoOrderNr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SnInfoOrderNr_Type.__name__ = "DisplayString"
_SnInfoOrderNr_Object = MibScalar
snInfoOrderNr = _SnInfoOrderNr_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 8, 6),
    _SnInfoOrderNr_Type()
)
snInfoOrderNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snInfoOrderNr.setStatus("mandatory")


class _SnSerialPortSpeed_Type(Integer32):
    """Custom type snSerialPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("o115200bps", 9),
          ("o19200bps", 6),
          ("o38400bps", 7),
          ("o9600bps", 5),
          ("other", 1))
    )


_SnSerialPortSpeed_Type.__name__ = "Integer32"
_SnSerialPortSpeed_Object = MibScalar
snSerialPortSpeed = _SnSerialPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 8, 8),
    _SnSerialPortSpeed_Type()
)
snSerialPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSerialPortSpeed.setStatus("mandatory")


class _SnSwitchTelnetEnable_Type(Integer32):
    """Custom type snSwitchTelnetEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("not-supported", 10))
    )


_SnSwitchTelnetEnable_Type.__name__ = "Integer32"
_SnSwitchTelnetEnable_Object = MibScalar
snSwitchTelnetEnable = _SnSwitchTelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 8, 9),
    _SnSwitchTelnetEnable_Type()
)
snSwitchTelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwitchTelnetEnable.setStatus("mandatory")


class _SnSwitchTelnetTimeOutEnable_Type(Integer32):
    """Custom type snSwitchTelnetTimeOutEnable based on Integer32"""
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


_SnSwitchTelnetTimeOutEnable_Type.__name__ = "Integer32"
_SnSwitchTelnetTimeOutEnable_Object = MibScalar
snSwitchTelnetTimeOutEnable = _SnSwitchTelnetTimeOutEnable_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 8, 10),
    _SnSwitchTelnetTimeOutEnable_Type()
)
snSwitchTelnetTimeOutEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwitchTelnetTimeOutEnable.setStatus("mandatory")


class _SnSwitchTelnetTimeOut_Type(Integer32):
    """Custom type snSwitchTelnetTimeOut based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_SnSwitchTelnetTimeOut_Type.__name__ = "Integer32"
_SnSwitchTelnetTimeOut_Object = MibScalar
snSwitchTelnetTimeOut = _SnSwitchTelnetTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 8, 11),
    _SnSwitchTelnetTimeOut_Type()
)
snSwitchTelnetTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwitchTelnetTimeOut.setStatus("mandatory")


class _SnSwitchSNMPEnable_Type(Integer32):
    """Custom type snSwitchSNMPEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("not-supported", 10))
    )


_SnSwitchSNMPEnable_Type.__name__ = "Integer32"
_SnSwitchSNMPEnable_Object = MibScalar
snSwitchSNMPEnable = _SnSwitchSNMPEnable_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 8, 12),
    _SnSwitchSNMPEnable_Type()
)
snSwitchSNMPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwitchSNMPEnable.setStatus("mandatory")


class _SnSysReset_Type(Integer32):
    """Custom type snSysReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cold-reset", 1),
          ("warm-reset", 2))
    )


_SnSysReset_Type.__name__ = "Integer32"
_SnSysReset_Object = MibScalar
snSysReset = _SnSysReset_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 8, 13),
    _SnSysReset_Type()
)
snSysReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    snSysReset.setStatus("mandatory")
_SnResetPowerUpCount_Type = Integer32
_SnResetPowerUpCount_Object = MibScalar
snResetPowerUpCount = _SnResetPowerUpCount_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 8, 14),
    _SnResetPowerUpCount_Type()
)
snResetPowerUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snResetPowerUpCount.setStatus("mandatory")


class _SnSetFactoryDefs_Type(Integer32):
    """Custom type snSetFactoryDefs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set-factory-defaults", 1),
          ("set-factory-defaults-complete", 2))
    )


_SnSetFactoryDefs_Type.__name__ = "Integer32"
_SnSetFactoryDefs_Object = MibScalar
snSetFactoryDefs = _SnSetFactoryDefs_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 8, 15),
    _SnSetFactoryDefs_Type()
)
snSetFactoryDefs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSetFactoryDefs.setStatus("mandatory")


class _SnResetCounters_Type(Integer32):
    """Custom type snResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset-counters", 1)
    )


_SnResetCounters_Type.__name__ = "Integer32"
_SnResetCounters_Object = MibScalar
snResetCounters = _SnResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 8, 16),
    _SnResetCounters_Type()
)
snResetCounters.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    snResetCounters.setStatus("mandatory")


class _SnEraseDataStoreFlash_Type(Integer32):
    """Custom type snEraseDataStoreFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("erase-datastore", 1)
    )


_SnEraseDataStoreFlash_Type.__name__ = "Integer32"
_SnEraseDataStoreFlash_Object = MibScalar
snEraseDataStoreFlash = _SnEraseDataStoreFlash_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 8, 17),
    _SnEraseDataStoreFlash_Type()
)
snEraseDataStoreFlash.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    snEraseDataStoreFlash.setStatus("mandatory")


class _SnSetMemoryDefs_Type(Integer32):
    """Custom type snSetMemoryDefs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set-memory-defaults", 1),
          ("set-memory-defaults-complete", 2))
    )


_SnSetMemoryDefs_Type.__name__ = "Integer32"
_SnSetMemoryDefs_Object = MibScalar
snSetMemoryDefs = _SnSetMemoryDefs_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 8, 18),
    _SnSetMemoryDefs_Type()
)
snSetMemoryDefs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSetMemoryDefs.setStatus("mandatory")


class _SnEmailSMTPIpAddress_Type(IpAddress):
    """Custom type snEmailSMTPIpAddress based on IpAddress"""
    defaultValue = 0


_SnEmailSMTPIpAddress_Object = MibScalar
snEmailSMTPIpAddress = _SnEmailSMTPIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 8, 20),
    _SnEmailSMTPIpAddress_Type()
)
snEmailSMTPIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snEmailSMTPIpAddress.setStatus("mandatory")


class _SnEmailSMTPPort_Type(Integer32):
    """Custom type snEmailSMTPPort based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnEmailSMTPPort_Type.__name__ = "Integer32"
_SnEmailSMTPPort_Object = MibScalar
snEmailSMTPPort = _SnEmailSMTPPort_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 8, 21),
    _SnEmailSMTPPort_Type()
)
snEmailSMTPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snEmailSMTPPort.setStatus("mandatory")


class _SnEmailEnable_Type(Integer32):
    """Custom type snEmailEnable based on Integer32"""
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


_SnEmailEnable_Type.__name__ = "Integer32"
_SnEmailEnable_Object = MibScalar
snEmailEnable = _SnEmailEnable_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 8, 22),
    _SnEmailEnable_Type()
)
snEmailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snEmailEnable.setStatus("mandatory")


class _SnEmailAddress_Type(DisplayString):
    """Custom type snEmailAddress based on DisplayString"""
    defaultValue = OctetString("user@host.domain")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnEmailAddress_Type.__name__ = "DisplayString"
_SnEmailAddress_Object = MibScalar
snEmailAddress = _SnEmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 8, 23),
    _SnEmailAddress_Type()
)
snEmailAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snEmailAddress.setStatus("mandatory")
_SnTcpip_ObjectIdentity = ObjectIdentity
snTcpip = _SnTcpip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 10)
)


class _SnIpAddress_Type(IpAddress):
    """Custom type snIpAddress based on IpAddress"""
    defaultValue = 0


_SnIpAddress_Object = MibScalar
snIpAddress = _SnIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 10, 2),
    _SnIpAddress_Type()
)
snIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpAddress.setStatus("mandatory")


class _SnIpSubnetMask_Type(IpAddress):
    """Custom type snIpSubnetMask based on IpAddress"""
    defaultValue = 0


_SnIpSubnetMask_Object = MibScalar
snIpSubnetMask = _SnIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 10, 3),
    _SnIpSubnetMask_Type()
)
snIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpSubnetMask.setStatus("mandatory")


class _SnIpDefaultGateway_Type(IpAddress):
    """Custom type snIpDefaultGateway based on IpAddress"""
    defaultValue = 0


_SnIpDefaultGateway_Object = MibScalar
snIpDefaultGateway = _SnIpDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 10, 4),
    _SnIpDefaultGateway_Type()
)
snIpDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpDefaultGateway.setStatus("mandatory")


class _SnBootP_Type(Integer32):
    """Custom type snBootP based on Integer32"""
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


_SnBootP_Type.__name__ = "Integer32"
_SnBootP_Object = MibScalar
snBootP = _SnBootP_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 10, 5),
    _SnBootP_Type()
)
snBootP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBootP.setStatus("mandatory")
_SnMacAddressBase_Type = MacAddress
_SnMacAddressBase_Object = MibScalar
snMacAddressBase = _SnMacAddressBase_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 1, 10, 10),
    _SnMacAddressBase_Type()
)
snMacAddressBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snMacAddressBase.setStatus("mandatory")
_SnProductSpecific_ObjectIdentity = ObjectIdentity
snProductSpecific = _SnProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2)
)
_SnOsm_ObjectIdentity = ObjectIdentity
snOsm = _SnOsm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1)
)


class _SnOsmFaultState_Type(Integer32):
    """Custom type snOsmFaultState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("noFault", 1))
    )


_SnOsmFaultState_Type.__name__ = "Integer32"
_SnOsmFaultState_Object = MibScalar
snOsmFaultState = _SnOsmFaultState_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 2),
    _SnOsmFaultState_Type()
)
snOsmFaultState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOsmFaultState.setStatus("mandatory")


class _SnOsmSignalledFaults_Type(Counter32):
    """Custom type snOsmSignalledFaults based on Counter32"""
    defaultValue = 0


_SnOsmSignalledFaults_Object = MibScalar
snOsmSignalledFaults = _SnOsmSignalledFaults_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 3),
    _SnOsmSignalledFaults_Type()
)
snOsmSignalledFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOsmSignalledFaults.setStatus("mandatory")


class _SnOsmFaultValue_Type(OctetString):
    """Custom type snOsmFaultValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SnOsmFaultValue_Type.__name__ = "OctetString"
_SnOsmFaultValue_Object = MibScalar
snOsmFaultValue = _SnOsmFaultValue_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 4),
    _SnOsmFaultValue_Type()
)
snOsmFaultValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOsmFaultValue.setStatus("mandatory")


class _SnOsmDigitalInputChange_Type(OctetString):
    """Custom type snOsmDigitalInputChange based on OctetString"""
    defaultValue = OctetString("00000000")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SnOsmDigitalInputChange_Type.__name__ = "OctetString"
_SnOsmDigitalInputChange_Object = MibScalar
snOsmDigitalInputChange = _SnOsmDigitalInputChange_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 5),
    _SnOsmDigitalInputChange_Type()
)
snOsmDigitalInputChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOsmDigitalInputChange.setStatus("mandatory")


class _SnOsmDigitalInputState_Type(Integer32):
    """Custom type snOsmDigitalInputState based on Integer32"""
    defaultValue = 0


_SnOsmDigitalInputState_Object = MibScalar
snOsmDigitalInputState = _SnOsmDigitalInputState_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 6),
    _SnOsmDigitalInputState_Type()
)
snOsmDigitalInputState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOsmDigitalInputState.setStatus("mandatory")


class _SnOsmRmMode_Type(Integer32):
    """Custom type snOsmRmMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rmOff", 1),
          ("rmOn", 2))
    )


_SnOsmRmMode_Type.__name__ = "Integer32"
_SnOsmRmMode_Object = MibScalar
snOsmRmMode = _SnOsmRmMode_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 11),
    _SnOsmRmMode_Type()
)
snOsmRmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOsmRmMode.setStatus("mandatory")


class _SnOsmRmState_Type(Integer32):
    """Custom type snOsmRmState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rmActive", 2),
          ("rmPassive", 1))
    )


_SnOsmRmState_Type.__name__ = "Integer32"
_SnOsmRmState_Object = MibScalar
snOsmRmState = _SnOsmRmState_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 12),
    _SnOsmRmState_Type()
)
snOsmRmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOsmRmState.setStatus("mandatory")


class _SnOsmRmStateChanges_Type(Counter32):
    """Custom type snOsmRmStateChanges based on Counter32"""
    defaultValue = 0


_SnOsmRmStateChanges_Object = MibScalar
snOsmRmStateChanges = _SnOsmRmStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 13),
    _SnOsmRmStateChanges_Type()
)
snOsmRmStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOsmRmStateChanges.setStatus("mandatory")


class _SnOsmRmObserverMode_Type(Integer32):
    """Custom type snOsmRmObserverMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("not-supported", 10),
          ("restart", 3))
    )


_SnOsmRmObserverMode_Type.__name__ = "Integer32"
_SnOsmRmObserverMode_Object = MibScalar
snOsmRmObserverMode = _SnOsmRmObserverMode_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 14),
    _SnOsmRmObserverMode_Type()
)
snOsmRmObserverMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOsmRmObserverMode.setStatus("mandatory")


class _SnOsmStandbyMode_Type(Integer32):
    """Custom type snOsmStandbyMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("not-supported", 10),
          ("standbyOff", 1),
          ("standbyOn", 2))
    )


_SnOsmStandbyMode_Type.__name__ = "Integer32"
_SnOsmStandbyMode_Object = MibScalar
snOsmStandbyMode = _SnOsmStandbyMode_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 21),
    _SnOsmStandbyMode_Type()
)
snOsmStandbyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOsmStandbyMode.setStatus("mandatory")


class _SnOsmStandbyState_Type(Integer32):
    """Custom type snOsmStandbyState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("not-supported", 10),
          ("standbyActive", 2),
          ("standbyPassive", 1))
    )


_SnOsmStandbyState_Type.__name__ = "Integer32"
_SnOsmStandbyState_Object = MibScalar
snOsmStandbyState = _SnOsmStandbyState_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 22),
    _SnOsmStandbyState_Type()
)
snOsmStandbyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOsmStandbyState.setStatus("mandatory")


class _SnOsmStandbyCableState_Type(Integer32):
    """Custom type snOsmStandbyCableState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 2),
          ("not-supported", 10))
    )


_SnOsmStandbyCableState_Type.__name__ = "Integer32"
_SnOsmStandbyCableState_Object = MibScalar
snOsmStandbyCableState = _SnOsmStandbyCableState_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 24),
    _SnOsmStandbyCableState_Type()
)
snOsmStandbyCableState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOsmStandbyCableState.setStatus("mandatory")


class _SnOsmStandbyStateChanges_Type(Counter32):
    """Custom type snOsmStandbyStateChanges based on Counter32"""
    defaultValue = 0


_SnOsmStandbyStateChanges_Object = MibScalar
snOsmStandbyStateChanges = _SnOsmStandbyStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 25),
    _SnOsmStandbyStateChanges_Type()
)
snOsmStandbyStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOsmStandbyStateChanges.setStatus("mandatory")
_SnOsmPort7TestMac_Type = MacAddress
_SnOsmPort7TestMac_Object = MibScalar
snOsmPort7TestMac = _SnOsmPort7TestMac_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 31),
    _SnOsmPort7TestMac_Type()
)
snOsmPort7TestMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOsmPort7TestMac.setStatus("mandatory")
_SnOsmPort8TestMac_Type = MacAddress
_SnOsmPort8TestMac_Object = MibScalar
snOsmPort8TestMac = _SnOsmPort8TestMac_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 32),
    _SnOsmPort8TestMac_Type()
)
snOsmPort8TestMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOsmPort8TestMac.setStatus("mandatory")
_SnOsmMulticastTestMac_Type = MacAddress
_SnOsmMulticastTestMac_Object = MibScalar
snOsmMulticastTestMac = _SnOsmMulticastTestMac_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 33),
    _SnOsmMulticastTestMac_Type()
)
snOsmMulticastTestMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOsmMulticastTestMac.setStatus("mandatory")
_SnOsmMulticastLinkMac_Type = MacAddress
_SnOsmMulticastLinkMac_Object = MibScalar
snOsmMulticastLinkMac = _SnOsmMulticastLinkMac_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 34),
    _SnOsmMulticastLinkMac_Type()
)
snOsmMulticastLinkMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOsmMulticastLinkMac.setStatus("mandatory")
_SnOsmUnicastLinkMac_Type = MacAddress
_SnOsmUnicastLinkMac_Object = MibScalar
snOsmUnicastLinkMac = _SnOsmUnicastLinkMac_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 35),
    _SnOsmUnicastLinkMac_Type()
)
snOsmUnicastLinkMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOsmUnicastLinkMac.setStatus("mandatory")
_SnOsmMulticastSyncMac_Type = MacAddress
_SnOsmMulticastSyncMac_Object = MibScalar
snOsmMulticastSyncMac = _SnOsmMulticastSyncMac_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 36),
    _SnOsmMulticastSyncMac_Type()
)
snOsmMulticastSyncMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOsmMulticastSyncMac.setStatus("mandatory")
_SnOsmMulticastFlowControlMac_Type = MacAddress
_SnOsmMulticastFlowControlMac_Object = MibScalar
snOsmMulticastFlowControlMac = _SnOsmMulticastFlowControlMac_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 37),
    _SnOsmMulticastFlowControlMac_Type()
)
snOsmMulticastFlowControlMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOsmMulticastFlowControlMac.setStatus("mandatory")


class _SnOsmTestMaxDelay_Type(Integer32):
    """Custom type snOsmTestMaxDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_SnOsmTestMaxDelay_Type.__name__ = "Integer32"
_SnOsmTestMaxDelay_Object = MibScalar
snOsmTestMaxDelay = _SnOsmTestMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 38),
    _SnOsmTestMaxDelay_Type()
)
snOsmTestMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOsmTestMaxDelay.setStatus("mandatory")


class _SnOsmPowerSupply1State_Type(Integer32):
    """Custom type snOsmPowerSupply1State based on Integer32"""
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
          ("inactive", 1))
    )


_SnOsmPowerSupply1State_Type.__name__ = "Integer32"
_SnOsmPowerSupply1State_Object = MibScalar
snOsmPowerSupply1State = _SnOsmPowerSupply1State_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 41),
    _SnOsmPowerSupply1State_Type()
)
snOsmPowerSupply1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOsmPowerSupply1State.setStatus("mandatory")


class _SnOsmPowerSupply2State_Type(Integer32):
    """Custom type snOsmPowerSupply2State based on Integer32"""
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
          ("inactive", 1))
    )


_SnOsmPowerSupply2State_Type.__name__ = "Integer32"
_SnOsmPowerSupply2State_Object = MibScalar
snOsmPowerSupply2State = _SnOsmPowerSupply2State_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 42),
    _SnOsmPowerSupply2State_Type()
)
snOsmPowerSupply2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOsmPowerSupply2State.setStatus("mandatory")


class _SnOsmPowerSupply1Mask_Type(Integer32):
    """Custom type snOsmPowerSupply1Mask based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("checked", 1),
          ("notChecked", 2))
    )


_SnOsmPowerSupply1Mask_Type.__name__ = "Integer32"
_SnOsmPowerSupply1Mask_Object = MibScalar
snOsmPowerSupply1Mask = _SnOsmPowerSupply1Mask_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 43),
    _SnOsmPowerSupply1Mask_Type()
)
snOsmPowerSupply1Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOsmPowerSupply1Mask.setStatus("mandatory")


class _SnOsmPowerSupply2Mask_Type(Integer32):
    """Custom type snOsmPowerSupply2Mask based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("checked", 1),
          ("notChecked", 2))
    )


_SnOsmPowerSupply2Mask_Type.__name__ = "Integer32"
_SnOsmPowerSupply2Mask_Object = MibScalar
snOsmPowerSupply2Mask = _SnOsmPowerSupply2Mask_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 44),
    _SnOsmPowerSupply2Mask_Type()
)
snOsmPowerSupply2Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOsmPowerSupply2Mask.setStatus("mandatory")


class _SnOsmChangedPowerLine_Type(Integer32):
    """Custom type snOsmChangedPowerLine based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("line1", 1),
          ("line2", 2),
          ("nochange", 0))
    )


_SnOsmChangedPowerLine_Type.__name__ = "Integer32"
_SnOsmChangedPowerLine_Object = MibScalar
snOsmChangedPowerLine = _SnOsmChangedPowerLine_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 45),
    _SnOsmChangedPowerLine_Type()
)
snOsmChangedPowerLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOsmChangedPowerLine.setStatus("mandatory")


class _SnOsmResetCounters_Type(Integer32):
    """Custom type snOsmResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_SnOsmResetCounters_Type.__name__ = "Integer32"
_SnOsmResetCounters_Object = MibScalar
snOsmResetCounters = _SnOsmResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 51),
    _SnOsmResetCounters_Type()
)
snOsmResetCounters.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    snOsmResetCounters.setStatus("mandatory")
_SnOsmPortTable_Object = MibTable
snOsmPortTable = _SnOsmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 61)
)
if mibBuilder.loadTexts:
    snOsmPortTable.setStatus("mandatory")
_SnOsmPortEntry_Object = MibTableRow
snOsmPortEntry = _SnOsmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 61, 1)
)
snOsmPortEntry.setIndexNames(
    (0, "SN-OSM-PRIV-MIB", "snOsmPortIndex"),
)
if mibBuilder.loadTexts:
    snOsmPortEntry.setStatus("mandatory")
_SnOsmPortIndex_Type = Integer32
_SnOsmPortIndex_Object = MibTableColumn
snOsmPortIndex = _SnOsmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 61, 1, 1),
    _SnOsmPortIndex_Type()
)
snOsmPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snOsmPortIndex.setStatus("mandatory")


class _SnOsmPortFaultMaskState_Type(Integer32):
    """Custom type snOsmPortFaultMaskState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("checked", 1),
          ("notChecked", 2))
    )


_SnOsmPortFaultMaskState_Type.__name__ = "Integer32"
_SnOsmPortFaultMaskState_Object = MibTableColumn
snOsmPortFaultMaskState = _SnOsmPortFaultMaskState_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 61, 1, 2),
    _SnOsmPortFaultMaskState_Type()
)
snOsmPortFaultMaskState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOsmPortFaultMaskState.setStatus("mandatory")


class _SnOsmPortStandbyMaskState_Type(Integer32):
    """Custom type snOsmPortStandbyMaskState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("checked", 1),
          ("notChecked", 2))
    )


_SnOsmPortStandbyMaskState_Type.__name__ = "Integer32"
_SnOsmPortStandbyMaskState_Object = MibTableColumn
snOsmPortStandbyMaskState = _SnOsmPortStandbyMaskState_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 61, 1, 3),
    _SnOsmPortStandbyMaskState_Type()
)
snOsmPortStandbyMaskState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOsmPortStandbyMaskState.setStatus("mandatory")


class _SnOsmPortLockState_Type(Integer32):
    """Custom type snOsmPortLockState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 2),
          ("unlocked", 1))
    )


_SnOsmPortLockState_Type.__name__ = "Integer32"
_SnOsmPortLockState_Object = MibTableColumn
snOsmPortLockState = _SnOsmPortLockState_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 61, 1, 4),
    _SnOsmPortLockState_Type()
)
snOsmPortLockState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOsmPortLockState.setStatus("mandatory")


class _SnOsmPortPartitionState_Type(Integer32):
    """Custom type snOsmPortPartitionState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPartition", 1),
          ("partition", 2))
    )


_SnOsmPortPartitionState_Type.__name__ = "Integer32"
_SnOsmPortPartitionState_Object = MibTableColumn
snOsmPortPartitionState = _SnOsmPortPartitionState_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 61, 1, 5),
    _SnOsmPortPartitionState_Type()
)
snOsmPortPartitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOsmPortPartitionState.setStatus("mandatory")


class _SnOsmPortBackPressure_Type(Integer32):
    """Custom type snOsmPortBackPressure based on Integer32"""
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


_SnOsmPortBackPressure_Type.__name__ = "Integer32"
_SnOsmPortBackPressure_Object = MibTableColumn
snOsmPortBackPressure = _SnOsmPortBackPressure_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 61, 1, 6),
    _SnOsmPortBackPressure_Type()
)
snOsmPortBackPressure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOsmPortBackPressure.setStatus("mandatory")
_SnOsmEventTable_Object = MibTable
snOsmEventTable = _SnOsmEventTable_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 62)
)
if mibBuilder.loadTexts:
    snOsmEventTable.setStatus("mandatory")
_SnOsmEventEntry_Object = MibTableRow
snOsmEventEntry = _SnOsmEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 62, 1)
)
snOsmEventEntry.setIndexNames(
    (0, "SN-OSM-PRIV-MIB", "snOsmEventIndex"),
)
if mibBuilder.loadTexts:
    snOsmEventEntry.setStatus("mandatory")


class _SnOsmEventIndex_Type(Integer32):
    """Custom type snOsmEventIndex based on Integer32"""
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
        *(("eMail", 1),
          ("logTabel", 3),
          ("trap", 2))
    )


_SnOsmEventIndex_Type.__name__ = "Integer32"
_SnOsmEventIndex_Object = MibTableColumn
snOsmEventIndex = _SnOsmEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 62, 1, 1),
    _SnOsmEventIndex_Type()
)
snOsmEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOsmEventIndex.setStatus("mandatory")


class _SnOsmEventColdWarmStart_Type(Integer32):
    """Custom type snOsmEventColdWarmStart based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("checked", 1),
          ("notChecked", 2))
    )


_SnOsmEventColdWarmStart_Type.__name__ = "Integer32"
_SnOsmEventColdWarmStart_Object = MibTableColumn
snOsmEventColdWarmStart = _SnOsmEventColdWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 62, 1, 2),
    _SnOsmEventColdWarmStart_Type()
)
snOsmEventColdWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOsmEventColdWarmStart.setStatus("mandatory")


class _SnOsmEventLinkChange_Type(Integer32):
    """Custom type snOsmEventLinkChange based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("checked", 1),
          ("notChecked", 2))
    )


_SnOsmEventLinkChange_Type.__name__ = "Integer32"
_SnOsmEventLinkChange_Object = MibTableColumn
snOsmEventLinkChange = _SnOsmEventLinkChange_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 62, 1, 3),
    _SnOsmEventLinkChange_Type()
)
snOsmEventLinkChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOsmEventLinkChange.setStatus("mandatory")


class _SnOsmEventAuthenticationFailure_Type(Integer32):
    """Custom type snOsmEventAuthenticationFailure based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("checked", 1),
          ("notChecked", 2))
    )


_SnOsmEventAuthenticationFailure_Type.__name__ = "Integer32"
_SnOsmEventAuthenticationFailure_Object = MibTableColumn
snOsmEventAuthenticationFailure = _SnOsmEventAuthenticationFailure_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 62, 1, 4),
    _SnOsmEventAuthenticationFailure_Type()
)
snOsmEventAuthenticationFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOsmEventAuthenticationFailure.setStatus("mandatory")


class _SnOsmEventRmonAlarm_Type(Integer32):
    """Custom type snOsmEventRmonAlarm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("checked", 1),
          ("notChecked", 2))
    )


_SnOsmEventRmonAlarm_Type.__name__ = "Integer32"
_SnOsmEventRmonAlarm_Object = MibTableColumn
snOsmEventRmonAlarm = _SnOsmEventRmonAlarm_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 62, 1, 5),
    _SnOsmEventRmonAlarm_Type()
)
snOsmEventRmonAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOsmEventRmonAlarm.setStatus("mandatory")


class _SnOsmEventPowerChange_Type(Integer32):
    """Custom type snOsmEventPowerChange based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("checked", 1),
          ("notChecked", 2))
    )


_SnOsmEventPowerChange_Type.__name__ = "Integer32"
_SnOsmEventPowerChange_Object = MibTableColumn
snOsmEventPowerChange = _SnOsmEventPowerChange_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 62, 1, 6),
    _SnOsmEventPowerChange_Type()
)
snOsmEventPowerChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOsmEventPowerChange.setStatus("mandatory")


class _SnOsmEventRmStateChange_Type(Integer32):
    """Custom type snOsmEventRmStateChange based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("checked", 1),
          ("notChecked", 2))
    )


_SnOsmEventRmStateChange_Type.__name__ = "Integer32"
_SnOsmEventRmStateChange_Object = MibTableColumn
snOsmEventRmStateChange = _SnOsmEventRmStateChange_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 62, 1, 7),
    _SnOsmEventRmStateChange_Type()
)
snOsmEventRmStateChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOsmEventRmStateChange.setStatus("mandatory")


class _SnOsmEventStandbyStateChange_Type(Integer32):
    """Custom type snOsmEventStandbyStateChange based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("checked", 1),
          ("notChecked", 2))
    )


_SnOsmEventStandbyStateChange_Type.__name__ = "Integer32"
_SnOsmEventStandbyStateChange_Object = MibTableColumn
snOsmEventStandbyStateChange = _SnOsmEventStandbyStateChange_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 62, 1, 8),
    _SnOsmEventStandbyStateChange_Type()
)
snOsmEventStandbyStateChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOsmEventStandbyStateChange.setStatus("mandatory")


class _SnOsmEventFault_Type(Integer32):
    """Custom type snOsmEventFault based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("checked", 1),
          ("notChecked", 2))
    )


_SnOsmEventFault_Type.__name__ = "Integer32"
_SnOsmEventFault_Object = MibTableColumn
snOsmEventFault = _SnOsmEventFault_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 62, 1, 9),
    _SnOsmEventFault_Type()
)
snOsmEventFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOsmEventFault.setStatus("mandatory")
_SnOsmDigitalInEventTable_Object = MibTable
snOsmDigitalInEventTable = _SnOsmDigitalInEventTable_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 63)
)
if mibBuilder.loadTexts:
    snOsmDigitalInEventTable.setStatus("mandatory")
_SnOsmDigitalInEventEntry_Object = MibTableRow
snOsmDigitalInEventEntry = _SnOsmDigitalInEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 63, 1)
)
snOsmDigitalInEventEntry.setIndexNames(
    (0, "SN-OSM-PRIV-MIB", "snOsmDigitalInIndex"),
)
if mibBuilder.loadTexts:
    snOsmDigitalInEventEntry.setStatus("mandatory")


class _SnOsmDigitalInIndex_Type(Integer32):
    """Custom type snOsmDigitalInIndex based on Integer32"""
    defaultValue = 0


_SnOsmDigitalInIndex_Object = MibTableColumn
snOsmDigitalInIndex = _SnOsmDigitalInIndex_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 63, 1, 1),
    _SnOsmDigitalInIndex_Type()
)
snOsmDigitalInIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOsmDigitalInIndex.setStatus("mandatory")


class _SnOsmDigitalInName_Type(DisplayString):
    """Custom type snOsmDigitalInName based on DisplayString"""
    defaultValue = OctetString("Digital XX")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SnOsmDigitalInName_Type.__name__ = "DisplayString"
_SnOsmDigitalInName_Object = MibTableColumn
snOsmDigitalInName = _SnOsmDigitalInName_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 63, 1, 2),
    _SnOsmDigitalInName_Type()
)
snOsmDigitalInName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOsmDigitalInName.setStatus("mandatory")


class _SnOsmDigitalInMailEvent_Type(Integer32):
    """Custom type snOsmDigitalInMailEvent based on Integer32"""
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
        *(("checked", 1),
          ("notChecked", 2),
          ("notSupported", 3))
    )


_SnOsmDigitalInMailEvent_Type.__name__ = "Integer32"
_SnOsmDigitalInMailEvent_Object = MibTableColumn
snOsmDigitalInMailEvent = _SnOsmDigitalInMailEvent_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 63, 1, 3),
    _SnOsmDigitalInMailEvent_Type()
)
snOsmDigitalInMailEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOsmDigitalInMailEvent.setStatus("mandatory")


class _SnOsmDigitalInTrapEvent_Type(Integer32):
    """Custom type snOsmDigitalInTrapEvent based on Integer32"""
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
        *(("checked", 1),
          ("notChecked", 2),
          ("notSupported", 3))
    )


_SnOsmDigitalInTrapEvent_Type.__name__ = "Integer32"
_SnOsmDigitalInTrapEvent_Object = MibTableColumn
snOsmDigitalInTrapEvent = _SnOsmDigitalInTrapEvent_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 63, 1, 4),
    _SnOsmDigitalInTrapEvent_Type()
)
snOsmDigitalInTrapEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOsmDigitalInTrapEvent.setStatus("mandatory")


class _SnOsmDigitalInLogEvent_Type(Integer32):
    """Custom type snOsmDigitalInLogEvent based on Integer32"""
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
        *(("checked", 1),
          ("notChecked", 2),
          ("notSupported", 3))
    )


_SnOsmDigitalInLogEvent_Type.__name__ = "Integer32"
_SnOsmDigitalInLogEvent_Object = MibTableColumn
snOsmDigitalInLogEvent = _SnOsmDigitalInLogEvent_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 63, 1, 5),
    _SnOsmDigitalInLogEvent_Type()
)
snOsmDigitalInLogEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOsmDigitalInLogEvent.setStatus("mandatory")


class _SnOsmDigitalInState_Type(Integer32):
    """Custom type snOsmDigitalInState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 3),
          ("off", 2),
          ("on", 1))
    )


_SnOsmDigitalInState_Type.__name__ = "Integer32"
_SnOsmDigitalInState_Object = MibTableColumn
snOsmDigitalInState = _SnOsmDigitalInState_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 63, 1, 6),
    _SnOsmDigitalInState_Type()
)
snOsmDigitalInState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOsmDigitalInState.setStatus("mandatory")


class _SnConfigId_Type(Integer32):
    """Custom type snConfigId based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("esmItp80", 3),
          ("esmItp80-Advanced", 11),
          ("esmTp40", 9),
          ("esmTp80", 4),
          ("esmTp80-Advanced", 12),
          ("osmBC08", 7),
          ("osmItp53", 1),
          ("osmItp53-Advanced", 15),
          ("osmItp62", 0),
          ("osmItp62-Advanced", 14),
          ("osmItpLd62", 5),
          ("osmItpLd62-Advanced", 13),
          ("osmTp22", 8),
          ("osmTp53", 16),
          ("osmTp62", 2),
          ("osmTp62-Advanced", 10),
          ("osmTpLd62", 6))
    )


_SnConfigId_Type.__name__ = "Integer32"
_SnConfigId_Object = MibScalar
snConfigId = _SnConfigId_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 100),
    _SnConfigId_Type()
)
snConfigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snConfigId.setStatus("mandatory")


class _SnSwitchFlowControl_Type(Integer32):
    """Custom type snSwitchFlowControl based on Integer32"""
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


_SnSwitchFlowControl_Type.__name__ = "Integer32"
_SnSwitchFlowControl_Object = MibScalar
snSwitchFlowControl = _SnSwitchFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 101),
    _SnSwitchFlowControl_Type()
)
snSwitchFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwitchFlowControl.setStatus("mandatory")


class _SnSwitchSnifferSrc_Type(Integer32):
    """Custom type snSwitchSnifferSrc based on Integer32"""
    defaultValue = 2


_SnSwitchSnifferSrc_Object = MibScalar
snSwitchSnifferSrc = _SnSwitchSnifferSrc_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 102),
    _SnSwitchSnifferSrc_Type()
)
snSwitchSnifferSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwitchSnifferSrc.setStatus("mandatory")


class _SnSwitchSnifferDest_Type(Integer32):
    """Custom type snSwitchSnifferDest based on Integer32"""
    defaultValue = 1


_SnSwitchSnifferDest_Object = MibScalar
snSwitchSnifferDest = _SnSwitchSnifferDest_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 103),
    _SnSwitchSnifferDest_Type()
)
snSwitchSnifferDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwitchSnifferDest.setStatus("mandatory")


class _SnSwitchSnifferEnable_Type(Integer32):
    """Custom type snSwitchSnifferEnable based on Integer32"""
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


_SnSwitchSnifferEnable_Type.__name__ = "Integer32"
_SnSwitchSnifferEnable_Object = MibScalar
snSwitchSnifferEnable = _SnSwitchSnifferEnable_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 104),
    _SnSwitchSnifferEnable_Type()
)
snSwitchSnifferEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwitchSnifferEnable.setStatus("mandatory")


class _SnSwitchAgingEnable_Type(Integer32):
    """Custom type snSwitchAgingEnable based on Integer32"""
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


_SnSwitchAgingEnable_Type.__name__ = "Integer32"
_SnSwitchAgingEnable_Object = MibScalar
snSwitchAgingEnable = _SnSwitchAgingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 105),
    _SnSwitchAgingEnable_Type()
)
snSwitchAgingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwitchAgingEnable.setStatus("mandatory")


class _SnSwitchRmonMode_Type(Integer32):
    """Custom type snSwitchRmonMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("not-supported", 10))
    )


_SnSwitchRmonMode_Type.__name__ = "Integer32"
_SnSwitchRmonMode_Object = MibScalar
snSwitchRmonMode = _SnSwitchRmonMode_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 106),
    _SnSwitchRmonMode_Type()
)
snSwitchRmonMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwitchRmonMode.setStatus("mandatory")


class _SnSwitchFdbImagePollTime_Type(Integer32):
    """Custom type snSwitchFdbImagePollTime based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_SnSwitchFdbImagePollTime_Type.__name__ = "Integer32"
_SnSwitchFdbImagePollTime_Object = MibScalar
snSwitchFdbImagePollTime = _SnSwitchFdbImagePollTime_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 107),
    _SnSwitchFdbImagePollTime_Type()
)
snSwitchFdbImagePollTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwitchFdbImagePollTime.setStatus("mandatory")


class _SnSwitchLearningTableEntries_Type(Integer32):
    """Custom type snSwitchLearningTableEntries based on Integer32"""
    defaultValue = 0


_SnSwitchLearningTableEntries_Object = MibScalar
snSwitchLearningTableEntries = _SnSwitchLearningTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 108),
    _SnSwitchLearningTableEntries_Type()
)
snSwitchLearningTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwitchLearningTableEntries.setStatus("mandatory")


class _SnSwitchTimeToNextDataStore_Type(Integer32):
    """Custom type snSwitchTimeToNextDataStore based on Integer32"""
    defaultValue = 0


_SnSwitchTimeToNextDataStore_Object = MibScalar
snSwitchTimeToNextDataStore = _SnSwitchTimeToNextDataStore_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 109),
    _SnSwitchTimeToNextDataStore_Type()
)
snSwitchTimeToNextDataStore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwitchTimeToNextDataStore.setStatus("mandatory")


class _SnSwitchFlushDataStore_Type(Integer32):
    """Custom type snSwitchFlushDataStore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("flush", 1)
    )


_SnSwitchFlushDataStore_Type.__name__ = "Integer32"
_SnSwitchFlushDataStore_Object = MibScalar
snSwitchFlushDataStore = _SnSwitchFlushDataStore_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 110),
    _SnSwitchFlushDataStore_Type()
)
snSwitchFlushDataStore.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    snSwitchFlushDataStore.setStatus("mandatory")


class _SnLastObject_Type(Integer32):
    """Custom type snLastObject based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("last-object", 1)
    )


_SnLastObject_Type.__name__ = "Integer32"
_SnLastObject_Object = MibScalar
snLastObject = _SnLastObject_Object(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 999),
    _SnLastObject_Type()
)
snLastObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snLastObject.setStatus("mandatory")
_SnmpV2_ObjectIdentity = ObjectIdentity
snmpV2 = _SnmpV2_ObjectIdentity(
    (1, 3, 6, 1, 6)
)
_SnmpModules_ObjectIdentity = ObjectIdentity
snmpModules = _SnmpModules_ObjectIdentity(
    (1, 3, 6, 1, 6, 3)
)
_SnmpMIB_ObjectIdentity = ObjectIdentity
snmpMIB = _SnmpMIB_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 1)
)
_SnmpMIBObjects_ObjectIdentity = ObjectIdentity
snmpMIBObjects = _SnmpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 1, 1)
)
_SnmpTraps_ObjectIdentity = ObjectIdentity
snmpTraps = _SnmpTraps_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 1, 1, 5)
)

# Managed Objects groups


# Notification objects

snOsmRmActiveState = NotificationType(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 0, 11)
)
if mibBuilder.loadTexts:
    snOsmRmActiveState.setStatus(
        ""
    )

snOsmRmPassiveState = NotificationType(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 0, 12)
)
if mibBuilder.loadTexts:
    snOsmRmPassiveState.setStatus(
        ""
    )

snOsmStandbyActiveState = NotificationType(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 0, 21)
)
if mibBuilder.loadTexts:
    snOsmStandbyActiveState.setStatus(
        ""
    )

snOsmStandbyPassiveState = NotificationType(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 0, 22)
)
if mibBuilder.loadTexts:
    snOsmStandbyPassiveState.setStatus(
        ""
    )

snOsmPowerLineDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 0, 31)
)
snOsmPowerLineDown.setObjects(
    ("SN-OSM-PRIV-MIB", "snOsmChangedPowerLine")
)
if mibBuilder.loadTexts:
    snOsmPowerLineDown.setStatus(
        ""
    )

snOsmPowerLineUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 0, 32)
)
snOsmPowerLineUp.setObjects(
    ("SN-OSM-PRIV-MIB", "snOsmChangedPowerLine")
)
if mibBuilder.loadTexts:
    snOsmPowerLineUp.setStatus(
        ""
    )

snOsmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 0, 41)
)
snOsmFault.setObjects(
    ("SN-OSM-PRIV-MIB", "snOsmFaultValue")
)
if mibBuilder.loadTexts:
    snOsmFault.setStatus(
        ""
    )

snOsmDigitalInput = NotificationType(
    (1, 3, 6, 1, 4, 1, 4196, 1, 1, 2, 100, 2, 1, 0, 51)
)
snOsmDigitalInput.setObjects(
      *(("SN-OSM-PRIV-MIB", "snOsmDigitalInputChange"),
        ("SN-OSM-PRIV-MIB", "snOsmDigitalInputState"))
)
if mibBuilder.loadTexts:
    snOsmDigitalInput.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SN-OSM-PRIV-MIB",
    **{"MacAddress": MacAddress,
       "IANAifType": IANAifType,
       "ad": ad,
       "adProductMibs": adProductMibs,
       "simaticNet": simaticNet,
       "iHub": iHub,
       "iSwitch": iSwitch,
       "snOsmItp62": snOsmItp62,
       "snOsmItp53": snOsmItp53,
       "snOsmItpLd62": snOsmItpLd62,
       "snEsmItp80": snEsmItp80,
       "snOsmTp62": snOsmTp62,
       "snEsmTp80": snEsmTp80,
       "snOsmBC08": snOsmBC08,
       "snOsmTpLd62": snOsmTpLd62,
       "snOsmTp22": snOsmTp22,
       "snEsmTp40": snEsmTp40,
       "snOsmTp62-Advanced": snOsmTp62_Advanced,
       "snEsmItp80-Advanced": snEsmItp80_Advanced,
       "snEsmTp80-Advanced": snEsmTp80_Advanced,
       "snOsmItpLd62-Advanced": snOsmItpLd62_Advanced,
       "snOsmItp62-Advanced": snOsmItp62_Advanced,
       "snOsmItp53-Advanced": snOsmItp53_Advanced,
       "snOsmTp53": snOsmTp53,
       "iSwitchMib": iSwitchMib,
       "snCommon": snCommon,
       "snDownload": snDownload,
       "snDownloadParams": snDownloadParams,
       "snDownloadParamsTftpServerHostName": snDownloadParamsTftpServerHostName,
       "snDownloadParamsFile": snDownloadParamsFile,
       "snDownloadParamsControl": snDownloadParamsControl,
       "snDownloadParamsStatus": snDownloadParamsStatus,
       "snDownloadNextBlockId": snDownloadNextBlockId,
       "snDownloadParamsError": snDownloadParamsError,
       "snDownloadAutoLoad": snDownloadAutoLoad,
       "snDownloadEventLogTableFile": snDownloadEventLogTableFile,
       "snDownloadEventLogTableControl": snDownloadEventLogTableControl,
       "snDownloadConfigFile": snDownloadConfigFile,
       "snDownloadConfigControl": snDownloadConfigControl,
       "snNvLog": snNvLog,
       "snNvLogMaxEntries": snNvLogMaxEntries,
       "snNvLogCurrentEntries": snNvLogCurrentEntries,
       "snNvLogNewEntries": snNvLogNewEntries,
       "snNvLogClear": snNvLogClear,
       "snNvLogTable": snNvLogTable,
       "snNvLogEntry": snNvLogEntry,
       "snNvLogPowerUpCount": snNvLogPowerUpCount,
       "snNvLogTime": snNvLogTime,
       "snNvLogSequenceNumber": snNvLogSequenceNumber,
       "snNvLogDescr": snNvLogDescr,
       "snNvLogPositionDescr": snNvLogPositionDescr,
       "snTrapInfo": snTrapInfo,
       "snSwitchTrapsEnable": snSwitchTrapsEnable,
       "snTrapTimeLastGenerated": snTrapTimeLastGenerated,
       "snTrapMaxManagers": snTrapMaxManagers,
       "snTrapTable": snTrapTable,
       "snTrapEntry": snTrapEntry,
       "snTrapAddress": snTrapAddress,
       "snTrapState": snTrapState,
       "snTrapIndex": snTrapIndex,
       "snGen": snGen,
       "snUserDescription": snUserDescription,
       "snHwVersion": snHwVersion,
       "snBootStrapVersion": snBootStrapVersion,
       "snSwVersion": snSwVersion,
       "snInfoOrderNr": snInfoOrderNr,
       "snSerialPortSpeed": snSerialPortSpeed,
       "snSwitchTelnetEnable": snSwitchTelnetEnable,
       "snSwitchTelnetTimeOutEnable": snSwitchTelnetTimeOutEnable,
       "snSwitchTelnetTimeOut": snSwitchTelnetTimeOut,
       "snSwitchSNMPEnable": snSwitchSNMPEnable,
       "snSysReset": snSysReset,
       "snResetPowerUpCount": snResetPowerUpCount,
       "snSetFactoryDefs": snSetFactoryDefs,
       "snResetCounters": snResetCounters,
       "snEraseDataStoreFlash": snEraseDataStoreFlash,
       "snSetMemoryDefs": snSetMemoryDefs,
       "snEmailSMTPIpAddress": snEmailSMTPIpAddress,
       "snEmailSMTPPort": snEmailSMTPPort,
       "snEmailEnable": snEmailEnable,
       "snEmailAddress": snEmailAddress,
       "snTcpip": snTcpip,
       "snIpAddress": snIpAddress,
       "snIpSubnetMask": snIpSubnetMask,
       "snIpDefaultGateway": snIpDefaultGateway,
       "snBootP": snBootP,
       "snMacAddressBase": snMacAddressBase,
       "snProductSpecific": snProductSpecific,
       "snOsm": snOsm,
       "snOsmRmActiveState": snOsmRmActiveState,
       "snOsmRmPassiveState": snOsmRmPassiveState,
       "snOsmStandbyActiveState": snOsmStandbyActiveState,
       "snOsmStandbyPassiveState": snOsmStandbyPassiveState,
       "snOsmPowerLineDown": snOsmPowerLineDown,
       "snOsmPowerLineUp": snOsmPowerLineUp,
       "snOsmFault": snOsmFault,
       "snOsmDigitalInput": snOsmDigitalInput,
       "snOsmFaultState": snOsmFaultState,
       "snOsmSignalledFaults": snOsmSignalledFaults,
       "snOsmFaultValue": snOsmFaultValue,
       "snOsmDigitalInputChange": snOsmDigitalInputChange,
       "snOsmDigitalInputState": snOsmDigitalInputState,
       "snOsmRmMode": snOsmRmMode,
       "snOsmRmState": snOsmRmState,
       "snOsmRmStateChanges": snOsmRmStateChanges,
       "snOsmRmObserverMode": snOsmRmObserverMode,
       "snOsmStandbyMode": snOsmStandbyMode,
       "snOsmStandbyState": snOsmStandbyState,
       "snOsmStandbyCableState": snOsmStandbyCableState,
       "snOsmStandbyStateChanges": snOsmStandbyStateChanges,
       "snOsmPort7TestMac": snOsmPort7TestMac,
       "snOsmPort8TestMac": snOsmPort8TestMac,
       "snOsmMulticastTestMac": snOsmMulticastTestMac,
       "snOsmMulticastLinkMac": snOsmMulticastLinkMac,
       "snOsmUnicastLinkMac": snOsmUnicastLinkMac,
       "snOsmMulticastSyncMac": snOsmMulticastSyncMac,
       "snOsmMulticastFlowControlMac": snOsmMulticastFlowControlMac,
       "snOsmTestMaxDelay": snOsmTestMaxDelay,
       "snOsmPowerSupply1State": snOsmPowerSupply1State,
       "snOsmPowerSupply2State": snOsmPowerSupply2State,
       "snOsmPowerSupply1Mask": snOsmPowerSupply1Mask,
       "snOsmPowerSupply2Mask": snOsmPowerSupply2Mask,
       "snOsmChangedPowerLine": snOsmChangedPowerLine,
       "snOsmResetCounters": snOsmResetCounters,
       "snOsmPortTable": snOsmPortTable,
       "snOsmPortEntry": snOsmPortEntry,
       "snOsmPortIndex": snOsmPortIndex,
       "snOsmPortFaultMaskState": snOsmPortFaultMaskState,
       "snOsmPortStandbyMaskState": snOsmPortStandbyMaskState,
       "snOsmPortLockState": snOsmPortLockState,
       "snOsmPortPartitionState": snOsmPortPartitionState,
       "snOsmPortBackPressure": snOsmPortBackPressure,
       "snOsmEventTable": snOsmEventTable,
       "snOsmEventEntry": snOsmEventEntry,
       "snOsmEventIndex": snOsmEventIndex,
       "snOsmEventColdWarmStart": snOsmEventColdWarmStart,
       "snOsmEventLinkChange": snOsmEventLinkChange,
       "snOsmEventAuthenticationFailure": snOsmEventAuthenticationFailure,
       "snOsmEventRmonAlarm": snOsmEventRmonAlarm,
       "snOsmEventPowerChange": snOsmEventPowerChange,
       "snOsmEventRmStateChange": snOsmEventRmStateChange,
       "snOsmEventStandbyStateChange": snOsmEventStandbyStateChange,
       "snOsmEventFault": snOsmEventFault,
       "snOsmDigitalInEventTable": snOsmDigitalInEventTable,
       "snOsmDigitalInEventEntry": snOsmDigitalInEventEntry,
       "snOsmDigitalInIndex": snOsmDigitalInIndex,
       "snOsmDigitalInName": snOsmDigitalInName,
       "snOsmDigitalInMailEvent": snOsmDigitalInMailEvent,
       "snOsmDigitalInTrapEvent": snOsmDigitalInTrapEvent,
       "snOsmDigitalInLogEvent": snOsmDigitalInLogEvent,
       "snOsmDigitalInState": snOsmDigitalInState,
       "snConfigId": snConfigId,
       "snSwitchFlowControl": snSwitchFlowControl,
       "snSwitchSnifferSrc": snSwitchSnifferSrc,
       "snSwitchSnifferDest": snSwitchSnifferDest,
       "snSwitchSnifferEnable": snSwitchSnifferEnable,
       "snSwitchAgingEnable": snSwitchAgingEnable,
       "snSwitchRmonMode": snSwitchRmonMode,
       "snSwitchFdbImagePollTime": snSwitchFdbImagePollTime,
       "snSwitchLearningTableEntries": snSwitchLearningTableEntries,
       "snSwitchTimeToNextDataStore": snSwitchTimeToNextDataStore,
       "snSwitchFlushDataStore": snSwitchFlushDataStore,
       "snLastObject": snLastObject,
       "snmpV2": snmpV2,
       "snmpModules": snmpModules,
       "snmpMIB": snmpMIB,
       "snmpMIBObjects": snmpMIBObjects,
       "snmpTraps": snmpTraps}
)
