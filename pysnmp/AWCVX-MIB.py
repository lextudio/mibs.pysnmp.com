# SNMP MIB module (AWCVX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AWCVX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:51 2024
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

(dot1dTpPort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dTpPort")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

awcVx = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3)
)
awcVx.setRevisions(
        ("2003-04-21 00:00",
         "2002-12-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AwcVlanId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )



class AwcPolId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )



class WEPKeytype128(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 13),
    )



class AwcInvokeCommand(Integer32, TextualConvention):
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
        *(("cancel", 6),
          ("inactive", 1),
          ("restart", 4),
          ("restartNotify", 5),
          ("start", 2),
          ("startNotify", 3))
    )



class AwcDot11MicAlgorithm(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("micMMH", 2),
          ("micNone", 1))
    )



class AwcDot11WEPKeyPermuteAlgorithm(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wepPermuteIV", 2),
          ("wepPermuteNone", 1))
    )



class AwcEventDisposition(Integer32, TextualConvention):
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
        *(("count", 1),
          ("displayConsole", 2),
          ("notify", 4),
          ("record", 3))
    )



class AwcDot11EventDisposition(Integer32, TextualConvention):
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
        *(("eventLogAndIeeeTrap", 4),
          ("eventLogOnly", 2),
          ("ieeeTrapOnly", 3),
          ("noNotification", 1))
    )



class AwcHotStandbyStatus(Integer32, TextualConvention):
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
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("associating", 4),
          ("associationFail", 7),
          ("error", 10),
          ("etherTestFail", 8),
          ("initializing", 1),
          ("interfaceMerge", 6),
          ("normal", 0),
          ("radioTestFail", 9),
          ("rootMacFailed", 5),
          ("stopped", 3),
          ("takeover", 2))
    )



class AwcTpFdbClassID(Integer32, TextualConvention):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("accessPoint", 8),
          ("bridge", 6),
          ("bridgeHost", 4),
          ("bridgeRoot", 9),
          ("clientStation", 5),
          ("dsHost", 3),
          ("multicast", 2),
          ("repeater", 7),
          ("unknown", 1))
    )



class AwcDdpProdDevID(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(74,
              76,
              77,
              78,
              84,
              85,
              86,
              101,
              102,
              104,
              109,
              110,
              111,
              112,
              113,
              117,
              120,
              121,
              122,
              123,
              124,
              127,
              128,
              240,
              241,
              253,
              255)
        )
    )
    namedValues = NamedValues(
        *(("emc", 124),
          ("emcNoDiversity", 123),
          ("ethernetAP", 76),
          ("ethernetBridge", 77),
          ("ethernetClient", 112),
          ("ethernetHost", 255),
          ("ethernetUC", 86),
          ("euc", 120),
          ("eucNoDiversity", 122),
          ("generic80211Client", 104),
          ("homeAP", 121),
          ("mc", 111),
          ("multicast", 240),
          ("pc2500Client", 113),
          ("pc3000Client", 84),
          ("pc3100Client", 110),
          ("pc3500Client", 101),
          ("pc4500Client", 102),
          ("pc4800Client", 109),
          ("pc4800bClient", 117),
          ("serialUC", 85),
          ("series350Client", 127),
          ("series370Client", 128),
          ("tokenRingAP", 74),
          ("tokenRingBridge", 78),
          ("tokenRingHost", 253),
          ("unknown", 241))
    )



class AwcDdpRadioDevID(Integer32, TextualConvention):
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
              12,
              13,
              34,
              35)
        )
    )
    namedValues = NamedValues(
        *(("pc3000", 4),
          ("pc3100", 13),
          ("pc3500", 3),
          ("pc4500", 6),
          ("pc4800", 12),
          ("series350", 34),
          ("series370", 35),
          ("tma2040", 5),
          ("tma2400", 2),
          ("tma900", 1),
          ("unknown", 0))
    )



class AwcDot11ClientState(Integer32, TextualConvention):
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
        *(("state0", 1),
          ("state1", 2),
          ("state2", 3),
          ("state3", 4))
    )



class AwcEventSeverity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("externalAlert", 8),
          ("externalInfo", 16),
          ("externalWarning", 12),
          ("portAlert", 7),
          ("portFatal", 4),
          ("portInfo", 15),
          ("portWarning", 11),
          ("protocolAlert", 6),
          ("protocolFatal", 3),
          ("protocolInfo", 14),
          ("protocolWarning", 10),
          ("systemAlert", 5),
          ("systemFatal", 2),
          ("systemInfo", 13),
          ("systemWarning", 9))
    )



class AwcHotStandbyState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("initializing", 1),
          ("notRunning", 3),
          ("running", 0),
          ("stopped", 2))
    )



class AwcPfDisposition(Integer32, TextualConvention):
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
        *(("block", 2),
          ("default", 3),
          ("forward", 1))
    )



class AwcPfPriority(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("background", 2),
          ("controlledLoad", 5),
          ("default", 1),
          ("excellentEffort", 4),
          ("interactiveVideo", 6),
          ("interactiveVoice", 7),
          ("networkControl", 8),
          ("spare", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Aironet_ObjectIdentity = ObjectIdentity
aironet = _Aironet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522)
)
_AwcSystem_ObjectIdentity = ObjectIdentity
awcSystem = _AwcSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 1)
)


class _VxWorksVersion_Type(DisplayString):
    """Custom type vxWorksVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VxWorksVersion_Type.__name__ = "DisplayString"
_VxWorksVersion_Object = MibScalar
vxWorksVersion = _VxWorksVersion_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 1, 1),
    _VxWorksVersion_Type()
)
vxWorksVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxWorksVersion.setStatus("current")


class _CreationDate_Type(DisplayString):
    """Custom type creationDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CreationDate_Type.__name__ = "DisplayString"
_CreationDate_Object = MibScalar
creationDate = _CreationDate_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 1, 2),
    _CreationDate_Type()
)
creationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creationDate.setStatus("current")


class _AwcVxVersion_Type(DisplayString):
    """Custom type awcVxVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AwcVxVersion_Type.__name__ = "DisplayString"
_AwcVxVersion_Object = MibScalar
awcVxVersion = _AwcVxVersion_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 1, 3),
    _AwcVxVersion_Type()
)
awcVxVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcVxVersion.setStatus("current")


class _SysFlags_Type(Unsigned32):
    """Custom type sysFlags based on Unsigned32"""
    defaultValue = 192


_SysFlags_Object = MibScalar
sysFlags = _SysFlags_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 1, 4),
    _SysFlags_Type()
)
sysFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFlags.setStatus("current")


class _LanguageCode_Type(DisplayString):
    """Custom type languageCode based on DisplayString"""
    defaultValue = OctetString("en-US")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_LanguageCode_Type.__name__ = "DisplayString"
_LanguageCode_Object = MibScalar
languageCode = _LanguageCode_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 1, 5),
    _LanguageCode_Type()
)
languageCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    languageCode.setStatus("current")
_AwcDevID_Type = Unsigned32
_AwcDevID_Object = MibScalar
awcDevID = _AwcDevID_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 1, 6),
    _AwcDevID_Type()
)
awcDevID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDevID.setStatus("current")


class _AwcDevIDtxt_Type(DisplayString):
    """Custom type awcDevIDtxt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AwcDevIDtxt_Type.__name__ = "DisplayString"
_AwcDevIDtxt_Object = MibScalar
awcDevIDtxt = _AwcDevIDtxt_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 1, 7),
    _AwcDevIDtxt_Type()
)
awcDevIDtxt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDevIDtxt.setStatus("current")


class _EnableHTTP_Type(TruthValue):
    """Custom type enableHTTP based on TruthValue"""


_EnableHTTP_Object = MibScalar
enableHTTP = _EnableHTTP_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 1, 8),
    _EnableHTTP_Type()
)
enableHTTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableHTTP.setStatus("current")


class _EnableTelnet_Type(TruthValue):
    """Custom type enableTelnet based on TruthValue"""


_EnableTelnet_Object = MibScalar
enableTelnet = _EnableTelnet_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 1, 9),
    _EnableTelnet_Type()
)
enableTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableTelnet.setStatus("current")


class _EnableSNMP_Type(TruthValue):
    """Custom type enableSNMP based on TruthValue"""


_EnableSNMP_Object = MibScalar
enableSNMP = _EnableSNMP_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 1, 10),
    _EnableSNMP_Type()
)
enableSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableSNMP.setStatus("current")


class _EnableDnsResolver_Type(TruthValue):
    """Custom type enableDnsResolver based on TruthValue"""


_EnableDnsResolver_Object = MibScalar
enableDnsResolver = _EnableDnsResolver_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 1, 11),
    _EnableDnsResolver_Type()
)
enableDnsResolver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableDnsResolver.setStatus("current")


class _EnableSNTP_Type(TruthValue):
    """Custom type enableSNTP based on TruthValue"""


_EnableSNTP_Object = MibScalar
enableSNTP = _EnableSNTP_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 1, 13),
    _EnableSNTP_Type()
)
enableSNTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableSNTP.setStatus("current")


class _EnableWDB_Type(TruthValue):
    """Custom type enableWDB based on TruthValue"""


_EnableWDB_Object = MibScalar
enableWDB = _EnableWDB_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 1, 14),
    _EnableWDB_Type()
)
enableWDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableWDB.setStatus("current")


class _PingTxLen_Type(Unsigned32):
    """Custom type pingTxLen based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(12, 4096),
    )


_PingTxLen_Type.__name__ = "Unsigned32"
_PingTxLen_Object = MibScalar
pingTxLen = _PingTxLen_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 1, 15),
    _PingTxLen_Type()
)
pingTxLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingTxLen.setStatus("current")


class _AwcFirstBoot_Type(TruthValue):
    """Custom type awcFirstBoot based on TruthValue"""


_AwcFirstBoot_Object = MibScalar
awcFirstBoot = _AwcFirstBoot_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 1, 16),
    _AwcFirstBoot_Type()
)
awcFirstBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFirstBoot.setStatus("current")
_AwcOemOUI_Type = MacAddress
_AwcOemOUI_Object = MibScalar
awcOemOUI = _AwcOemOUI_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 1, 17),
    _AwcOemOUI_Type()
)
awcOemOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcOemOUI.setStatus("current")


class _AwcOemName_Type(DisplayString):
    """Custom type awcOemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AwcOemName_Type.__name__ = "DisplayString"
_AwcOemName_Object = MibScalar
awcOemName = _AwcOemName_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 1, 18),
    _AwcOemName_Type()
)
awcOemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcOemName.setStatus("current")


class _AwcOemNameShort_Type(DisplayString):
    """Custom type awcOemNameShort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AwcOemNameShort_Type.__name__ = "DisplayString"
_AwcOemNameShort_Object = MibScalar
awcOemNameShort = _AwcOemNameShort_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 1, 19),
    _AwcOemNameShort_Type()
)
awcOemNameShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcOemNameShort.setStatus("current")


class _AwcOemHomeURL_Type(DisplayString):
    """Custom type awcOemHomeURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AwcOemHomeURL_Type.__name__ = "DisplayString"
_AwcOemHomeURL_Object = MibScalar
awcOemHomeURL = _AwcOemHomeURL_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 1, 20),
    _AwcOemHomeURL_Type()
)
awcOemHomeURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcOemHomeURL.setStatus("current")


class _EnablePSPF_Type(TruthValue):
    """Custom type enablePSPF based on TruthValue"""


_EnablePSPF_Object = MibScalar
enablePSPF = _EnablePSPF_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 1, 21),
    _EnablePSPF_Type()
)
enablePSPF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enablePSPF.setStatus("current")


class _SysExceptionReboot_Type(TruthValue):
    """Custom type sysExceptionReboot based on TruthValue"""


_SysExceptionReboot_Object = MibScalar
sysExceptionReboot = _SysExceptionReboot_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 1, 24),
    _SysExceptionReboot_Type()
)
sysExceptionReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysExceptionReboot.setStatus("current")


class _BootblockVersion_Type(DisplayString):
    """Custom type bootblockVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BootblockVersion_Type.__name__ = "DisplayString"
_BootblockVersion_Object = MibScalar
bootblockVersion = _BootblockVersion_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 1, 25),
    _BootblockVersion_Type()
)
bootblockVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootblockVersion.setStatus("current")
_MotherboardRevision_Type = Unsigned32
_MotherboardRevision_Object = MibScalar
motherboardRevision = _MotherboardRevision_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 1, 26),
    _MotherboardRevision_Type()
)
motherboardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motherboardRevision.setStatus("current")
_EnableSTP_Type = TruthValue
_EnableSTP_Object = MibScalar
enableSTP = _EnableSTP_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 1, 27),
    _EnableSTP_Type()
)
enableSTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableSTP.setStatus("current")


class _EnableRebootKey_Type(TruthValue):
    """Custom type enableRebootKey based on TruthValue"""


_EnableRebootKey_Object = MibScalar
enableRebootKey = _EnableRebootKey_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 1, 28),
    _EnableRebootKey_Type()
)
enableRebootKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableRebootKey.setStatus("current")


class _AwcLocateUnit_Type(TruthValue):
    """Custom type awcLocateUnit based on TruthValue"""


_AwcLocateUnit_Object = MibScalar
awcLocateUnit = _AwcLocateUnit_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 1, 29),
    _AwcLocateUnit_Type()
)
awcLocateUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcLocateUnit.setStatus("current")
_BootconfigVx_ObjectIdentity = ObjectIdentity
bootconfigVx = _BootconfigVx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 2)
)


class _BootconfigBootProtocol_Type(Integer32):
    """Custom type bootconfigBootProtocol based on Integer32"""
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
        *(("bootp", 2),
          ("dhcp", 3),
          ("none", 1))
    )


_BootconfigBootProtocol_Type.__name__ = "Integer32"
_BootconfigBootProtocol_Object = MibScalar
bootconfigBootProtocol = _BootconfigBootProtocol_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 1),
    _BootconfigBootProtocol_Type()
)
bootconfigBootProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootconfigBootProtocol.setStatus("current")


class _BootconfigReadINI_Type(Integer32):
    """Custom type bootconfigReadINI based on Integer32"""
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
        *(("always", 1),
          ("ifSpecified", 3),
          ("never", 2))
    )


_BootconfigReadINI_Type.__name__ = "Integer32"
_BootconfigReadINI_Object = MibScalar
bootconfigReadINI = _BootconfigReadINI_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 2),
    _BootconfigReadINI_Type()
)
bootconfigReadINI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootconfigReadINI.setStatus("current")


class _BootconfigServerConfigTimeout_Type(Unsigned32):
    """Custom type bootconfigServerConfigTimeout based on Unsigned32"""
    defaultValue = 120


_BootconfigServerConfigTimeout_Object = MibScalar
bootconfigServerConfigTimeout = _BootconfigServerConfigTimeout_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 3),
    _BootconfigServerConfigTimeout_Type()
)
bootconfigServerConfigTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootconfigServerConfigTimeout.setStatus("current")
if mibBuilder.loadTexts:
    bootconfigServerConfigTimeout.setUnits("seconds")


class _BootconfigMultOfferTimeout_Type(Unsigned32):
    """Custom type bootconfigMultOfferTimeout based on Unsigned32"""
    defaultValue = 5


_BootconfigMultOfferTimeout_Object = MibScalar
bootconfigMultOfferTimeout = _BootconfigMultOfferTimeout_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 4),
    _BootconfigMultOfferTimeout_Type()
)
bootconfigMultOfferTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootconfigMultOfferTimeout.setStatus("current")
if mibBuilder.loadTexts:
    bootconfigMultOfferTimeout.setUnits("seconds")


class _BootconfigReqLeaseDuration_Type(Unsigned32):
    """Custom type bootconfigReqLeaseDuration based on Unsigned32"""
    defaultValue = 1440


_BootconfigReqLeaseDuration_Object = MibScalar
bootconfigReqLeaseDuration = _BootconfigReqLeaseDuration_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 5),
    _BootconfigReqLeaseDuration_Type()
)
bootconfigReqLeaseDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootconfigReqLeaseDuration.setStatus("current")
if mibBuilder.loadTexts:
    bootconfigReqLeaseDuration.setUnits("minutes")


class _BootconfigMinLeaseDuration_Type(Unsigned32):
    """Custom type bootconfigMinLeaseDuration based on Unsigned32"""
    defaultValue = 0


_BootconfigMinLeaseDuration_Object = MibScalar
bootconfigMinLeaseDuration = _BootconfigMinLeaseDuration_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 6),
    _BootconfigMinLeaseDuration_Type()
)
bootconfigMinLeaseDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootconfigMinLeaseDuration.setStatus("current")
if mibBuilder.loadTexts:
    bootconfigMinLeaseDuration.setUnits("minutes")


class _BootconfigDev_Type(DisplayString):
    """Custom type bootconfigDev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BootconfigDev_Type.__name__ = "DisplayString"
_BootconfigDev_Object = MibScalar
bootconfigDev = _BootconfigDev_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 7),
    _BootconfigDev_Type()
)
bootconfigDev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootconfigDev.setStatus("current")
_BootconfigClientAddr_Type = IpAddress
_BootconfigClientAddr_Object = MibScalar
bootconfigClientAddr = _BootconfigClientAddr_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 8),
    _BootconfigClientAddr_Type()
)
bootconfigClientAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootconfigClientAddr.setStatus("current")
_BootconfigHostAddr_Type = IpAddress
_BootconfigHostAddr_Object = MibScalar
bootconfigHostAddr = _BootconfigHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 9),
    _BootconfigHostAddr_Type()
)
bootconfigHostAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootconfigHostAddr.setStatus("current")


class _BootconfigBootFile_Type(DisplayString):
    """Custom type bootconfigBootFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BootconfigBootFile_Type.__name__ = "DisplayString"
_BootconfigBootFile_Object = MibScalar
bootconfigBootFile = _BootconfigBootFile_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 10),
    _BootconfigBootFile_Type()
)
bootconfigBootFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootconfigBootFile.setStatus("current")
_BootconfigSubnetMask_Type = IpAddress
_BootconfigSubnetMask_Object = MibScalar
bootconfigSubnetMask = _BootconfigSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 11),
    _BootconfigSubnetMask_Type()
)
bootconfigSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootconfigSubnetMask.setStatus("current")
_BootconfigGateway_Type = IpAddress
_BootconfigGateway_Object = MibScalar
bootconfigGateway = _BootconfigGateway_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 12),
    _BootconfigGateway_Type()
)
bootconfigGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootconfigGateway.setStatus("current")


class _BootconfigHostName_Type(DisplayString):
    """Custom type bootconfigHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BootconfigHostName_Type.__name__ = "DisplayString"
_BootconfigHostName_Object = MibScalar
bootconfigHostName = _BootconfigHostName_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 13),
    _BootconfigHostName_Type()
)
bootconfigHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootconfigHostName.setStatus("current")


class _BootconfigClientName_Type(DisplayString):
    """Custom type bootconfigClientName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BootconfigClientName_Type.__name__ = "DisplayString"
_BootconfigClientName_Object = MibScalar
bootconfigClientName = _BootconfigClientName_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 14),
    _BootconfigClientName_Type()
)
bootconfigClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootconfigClientName.setStatus("current")
_BootconfigNameServerTable_Object = MibTable
bootconfigNameServerTable = _BootconfigNameServerTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 15)
)
if mibBuilder.loadTexts:
    bootconfigNameServerTable.setStatus("current")
_BootconfigNameServerEntry_Object = MibTableRow
bootconfigNameServerEntry = _BootconfigNameServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 15, 1)
)
bootconfigNameServerEntry.setIndexNames(
    (0, "AWCVX-MIB", "bootconfigNameServerPriority"),
)
if mibBuilder.loadTexts:
    bootconfigNameServerEntry.setStatus("current")


class _BootconfigNameServerPriority_Type(Integer32):
    """Custom type bootconfigNameServerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_BootconfigNameServerPriority_Type.__name__ = "Integer32"
_BootconfigNameServerPriority_Object = MibTableColumn
bootconfigNameServerPriority = _BootconfigNameServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 15, 1, 1),
    _BootconfigNameServerPriority_Type()
)
bootconfigNameServerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootconfigNameServerPriority.setStatus("current")
_BootconfigNameServer_Type = IpAddress
_BootconfigNameServer_Object = MibTableColumn
bootconfigNameServer = _BootconfigNameServer_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 15, 1, 2),
    _BootconfigNameServer_Type()
)
bootconfigNameServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootconfigNameServer.setStatus("current")


class _BootconfigDomainName_Type(DisplayString):
    """Custom type bootconfigDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BootconfigDomainName_Type.__name__ = "DisplayString"
_BootconfigDomainName_Object = MibScalar
bootconfigDomainName = _BootconfigDomainName_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 16),
    _BootconfigDomainName_Type()
)
bootconfigDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootconfigDomainName.setStatus("current")
_BootconfigSntpServer_Type = IpAddress
_BootconfigSntpServer_Object = MibScalar
bootconfigSntpServer = _BootconfigSntpServer_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 17),
    _BootconfigSntpServer_Type()
)
bootconfigSntpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootconfigSntpServer.setStatus("current")


class _BootconfigSaveServerResponse_Type(TruthValue):
    """Custom type bootconfigSaveServerResponse based on TruthValue"""


_BootconfigSaveServerResponse_Object = MibScalar
bootconfigSaveServerResponse = _BootconfigSaveServerResponse_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 18),
    _BootconfigSaveServerResponse_Type()
)
bootconfigSaveServerResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootconfigSaveServerResponse.setStatus("current")
_BootconfigCmdInvokeIniLoad_Type = AwcInvokeCommand
_BootconfigCmdInvokeIniLoad_Object = MibScalar
bootconfigCmdInvokeIniLoad = _BootconfigCmdInvokeIniLoad_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 19),
    _BootconfigCmdInvokeIniLoad_Type()
)
bootconfigCmdInvokeIniLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootconfigCmdInvokeIniLoad.setStatus("current")
_BootconfigCmdStatusIniLoad_Type = Integer32
_BootconfigCmdStatusIniLoad_Object = MibScalar
bootconfigCmdStatusIniLoad = _BootconfigCmdStatusIniLoad_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 20),
    _BootconfigCmdStatusIniLoad_Type()
)
bootconfigCmdStatusIniLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootconfigCmdStatusIniLoad.setStatus("current")


class _BootconfigDhcpClassID_Type(DisplayString):
    """Custom type bootconfigDhcpClassID based on DisplayString"""
    defaultValue = OctetString("AP4800E")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BootconfigDhcpClassID_Type.__name__ = "DisplayString"
_BootconfigDhcpClassID_Object = MibScalar
bootconfigDhcpClassID = _BootconfigDhcpClassID_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 24),
    _BootconfigDhcpClassID_Type()
)
bootconfigDhcpClassID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootconfigDhcpClassID.setStatus("current")
_BootconfigFileServerAddr_Type = IpAddress
_BootconfigFileServerAddr_Object = MibScalar
bootconfigFileServerAddr = _BootconfigFileServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 25),
    _BootconfigFileServerAddr_Type()
)
bootconfigFileServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootconfigFileServerAddr.setStatus("current")
_BootconfigLogServerAddr_Type = IpAddress
_BootconfigLogServerAddr_Object = MibScalar
bootconfigLogServerAddr = _BootconfigLogServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 26),
    _BootconfigLogServerAddr_Type()
)
bootconfigLogServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootconfigLogServerAddr.setStatus("current")
_BootconfigBootCount_Type = Unsigned32
_BootconfigBootCount_Object = MibScalar
bootconfigBootCount = _BootconfigBootCount_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 27),
    _BootconfigBootCount_Type()
)
bootconfigBootCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootconfigBootCount.setStatus("current")


class _BootconfigDhcpClientIdType_Type(Integer32):
    """Custom type bootconfigDhcpClientIdType based on Integer32"""
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
              128)
        )
    )
    namedValues = NamedValues(
        *(("amateurRadioAxDot25", 3),
          ("arcnet", 7),
          ("autonet", 10),
          ("chaos", 5),
          ("ethernet10Mb", 1),
          ("experimentalEthernet3Mb", 2),
          ("hyperchannel", 8),
          ("ieee802Networks", 6),
          ("lanstar", 9),
          ("localNet", 12),
          ("localTalk", 11),
          ("nonHardware", 128),
          ("proteonProNetTokenRing", 4))
    )


_BootconfigDhcpClientIdType_Type.__name__ = "Integer32"
_BootconfigDhcpClientIdType_Object = MibScalar
bootconfigDhcpClientIdType = _BootconfigDhcpClientIdType_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 28),
    _BootconfigDhcpClientIdType_Type()
)
bootconfigDhcpClientIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootconfigDhcpClientIdType.setStatus("current")


class _BootconfigDhcpClientIdValue_Type(DisplayString):
    """Custom type bootconfigDhcpClientIdValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BootconfigDhcpClientIdValue_Type.__name__ = "DisplayString"
_BootconfigDhcpClientIdValue_Object = MibScalar
bootconfigDhcpClientIdValue = _BootconfigDhcpClientIdValue_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 2, 29),
    _BootconfigDhcpClientIdValue_Type()
)
bootconfigDhcpClientIdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootconfigDhcpClientIdValue.setStatus("current")
_AwcSerialDev_ObjectIdentity = ObjectIdentity
awcSerialDev = _AwcSerialDev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 3)
)
_AwcSerialConfigTable_Object = MibTable
awcSerialConfigTable = _AwcSerialConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 3, 1)
)
if mibBuilder.loadTexts:
    awcSerialConfigTable.setStatus("current")
_AwcSerialConfigEntry_Object = MibTableRow
awcSerialConfigEntry = _AwcSerialConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 3, 1, 1)
)
awcSerialConfigEntry.setIndexNames(
    (0, "AWCVX-MIB", "serialDevIndex"),
)
if mibBuilder.loadTexts:
    awcSerialConfigEntry.setStatus("current")


class _SerialDevIndex_Type(Integer32):
    """Custom type serialDevIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SerialDevIndex_Type.__name__ = "Integer32"
_SerialDevIndex_Object = MibTableColumn
serialDevIndex = _SerialDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 3, 1, 1, 1),
    _SerialDevIndex_Type()
)
serialDevIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialDevIndex.setStatus("current")


class _SerialAdminStatus_Type(Integer32):
    """Custom type serialAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("error", 4),
          ("testing", 3),
          ("up", 1))
    )


_SerialAdminStatus_Type.__name__ = "Integer32"
_SerialAdminStatus_Object = MibTableColumn
serialAdminStatus = _SerialAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 3, 1, 1, 2),
    _SerialAdminStatus_Type()
)
serialAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialAdminStatus.setStatus("current")


class _SerialOperStatus_Type(Integer32):
    """Custom type serialOperStatus based on Integer32"""
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
        *(("down", 2),
          ("error", 4),
          ("testing", 3),
          ("up", 1))
    )


_SerialOperStatus_Type.__name__ = "Integer32"
_SerialOperStatus_Object = MibTableColumn
serialOperStatus = _SerialOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 3, 1, 1, 3),
    _SerialOperStatus_Type()
)
serialOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialOperStatus.setStatus("current")


class _SerialBaud_Type(Unsigned32):
    """Custom type serialBaud based on Unsigned32"""
    defaultValue = 9600


_SerialBaud_Object = MibTableColumn
serialBaud = _SerialBaud_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 3, 1, 1, 4),
    _SerialBaud_Type()
)
serialBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialBaud.setStatus("current")


class _SerialParity_Type(Integer32):
    """Custom type serialParity based on Integer32"""
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
        *(("even", 2),
          ("none", 1),
          ("odd", 3),
          ("one", 4),
          ("zero", 5))
    )


_SerialParity_Type.__name__ = "Integer32"
_SerialParity_Object = MibTableColumn
serialParity = _SerialParity_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 3, 1, 1, 5),
    _SerialParity_Type()
)
serialParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialParity.setStatus("current")


class _SerialDataBits_Type(Unsigned32):
    """Custom type serialDataBits based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 8),
    )


_SerialDataBits_Type.__name__ = "Unsigned32"
_SerialDataBits_Object = MibTableColumn
serialDataBits = _SerialDataBits_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 3, 1, 1, 6),
    _SerialDataBits_Type()
)
serialDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDataBits.setStatus("current")
if mibBuilder.loadTexts:
    serialDataBits.setUnits("bits")


class _SerialStopBits_Type(Unsigned32):
    """Custom type serialStopBits based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SerialStopBits_Type.__name__ = "Unsigned32"
_SerialStopBits_Object = MibTableColumn
serialStopBits = _SerialStopBits_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 3, 1, 1, 7),
    _SerialStopBits_Type()
)
serialStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialStopBits.setStatus("current")
if mibBuilder.loadTexts:
    serialStopBits.setUnits("bits")


class _SerialFlowControl_Type(Integer32):
    """Custom type serialFlowControl based on Integer32"""
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
        *(("hwRtsCts", 3),
          ("none", 1),
          ("swHwBoth", 4),
          ("swXonXoff", 2))
    )


_SerialFlowControl_Type.__name__ = "Integer32"
_SerialFlowControl_Object = MibTableColumn
serialFlowControl = _SerialFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 3, 1, 1, 8),
    _SerialFlowControl_Type()
)
serialFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialFlowControl.setStatus("current")


class _SerialTerminalType_Type(Integer32):
    """Custom type serialTerminalType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 2),
          ("teletype", 1))
    )


_SerialTerminalType_Type.__name__ = "Integer32"
_SerialTerminalType_Object = MibTableColumn
serialTerminalType = _SerialTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 3, 1, 1, 9),
    _SerialTerminalType_Type()
)
serialTerminalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialTerminalType.setStatus("current")


class _SerialTerminalLines_Type(Unsigned32):
    """Custom type serialTerminalLines based on Unsigned32"""
    defaultValue = 24

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 50),
    )


_SerialTerminalLines_Type.__name__ = "Unsigned32"
_SerialTerminalLines_Object = MibTableColumn
serialTerminalLines = _SerialTerminalLines_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 3, 1, 1, 10),
    _SerialTerminalLines_Type()
)
serialTerminalLines.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialTerminalLines.setStatus("current")


class _SerialTerminalColumns_Type(Unsigned32):
    """Custom type serialTerminalColumns based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 132),
    )


_SerialTerminalColumns_Type.__name__ = "Unsigned32"
_SerialTerminalColumns_Object = MibTableColumn
serialTerminalColumns = _SerialTerminalColumns_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 3, 1, 1, 11),
    _SerialTerminalColumns_Type()
)
serialTerminalColumns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialTerminalColumns.setStatus("current")
_SerialDevFd_Type = Integer32
_SerialDevFd_Object = MibTableColumn
serialDevFd = _SerialDevFd_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 3, 1, 1, 12),
    _SerialDevFd_Type()
)
serialDevFd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialDevFd.setStatus("current")
_AwcFtp_ObjectIdentity = ObjectIdentity
awcFtp = _AwcFtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 4)
)


class _DefaultFileServer_Type(DisplayString):
    """Custom type defaultFileServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DefaultFileServer_Type.__name__ = "DisplayString"
_DefaultFileServer_Object = MibScalar
defaultFileServer = _DefaultFileServer_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 4, 1),
    _DefaultFileServer_Type()
)
defaultFileServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultFileServer.setStatus("current")


class _AwcFileXferProtocol_Type(Integer32):
    """Custom type awcFileXferProtocol based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 2),
          ("tftp", 1))
    )


_AwcFileXferProtocol_Type.__name__ = "Integer32"
_AwcFileXferProtocol_Object = MibScalar
awcFileXferProtocol = _AwcFileXferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 4, 2),
    _AwcFileXferProtocol_Type()
)
awcFileXferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFileXferProtocol.setStatus("current")


class _AwcFileXferUser_Type(DisplayString):
    """Custom type awcFileXferUser based on DisplayString"""
    defaultValue = OctetString("anonymous")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AwcFileXferUser_Type.__name__ = "DisplayString"
_AwcFileXferUser_Object = MibScalar
awcFileXferUser = _AwcFileXferUser_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 4, 3),
    _AwcFileXferUser_Type()
)
awcFileXferUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFileXferUser.setStatus("current")


class _AwcFileXferPassword_Type(DisplayString):
    """Custom type awcFileXferPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AwcFileXferPassword_Type.__name__ = "DisplayString"
_AwcFileXferPassword_Object = MibScalar
awcFileXferPassword = _AwcFileXferPassword_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 4, 4),
    _AwcFileXferPassword_Type()
)
awcFileXferPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFileXferPassword.setStatus("current")
_AwcFileXferCmdInvokeFileLoad_Type = AwcInvokeCommand
_AwcFileXferCmdInvokeFileLoad_Object = MibScalar
awcFileXferCmdInvokeFileLoad = _AwcFileXferCmdInvokeFileLoad_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 4, 5),
    _AwcFileXferCmdInvokeFileLoad_Type()
)
awcFileXferCmdInvokeFileLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFileXferCmdInvokeFileLoad.setStatus("current")
_AwcFileXferCmdStatusFileLoad_Type = Integer32
_AwcFileXferCmdStatusFileLoad_Object = MibScalar
awcFileXferCmdStatusFileLoad = _AwcFileXferCmdStatusFileLoad_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 4, 6),
    _AwcFileXferCmdStatusFileLoad_Type()
)
awcFileXferCmdStatusFileLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcFileXferCmdStatusFileLoad.setStatus("current")
_AwcFileXferCmdInvokeFileSave_Type = AwcInvokeCommand
_AwcFileXferCmdInvokeFileSave_Object = MibScalar
awcFileXferCmdInvokeFileSave = _AwcFileXferCmdInvokeFileSave_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 4, 7),
    _AwcFileXferCmdInvokeFileSave_Type()
)
awcFileXferCmdInvokeFileSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFileXferCmdInvokeFileSave.setStatus("current")
_AwcFileXferCmdStatusFileSave_Type = Integer32
_AwcFileXferCmdStatusFileSave_Object = MibScalar
awcFileXferCmdStatusFileSave = _AwcFileXferCmdStatusFileSave_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 4, 8),
    _AwcFileXferCmdStatusFileSave_Type()
)
awcFileXferCmdStatusFileSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcFileXferCmdStatusFileSave.setStatus("current")


class _AwcFileXferFileFirmwareSystem_Type(DisplayString):
    """Custom type awcFileXferFileFirmwareSystem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AwcFileXferFileFirmwareSystem_Type.__name__ = "DisplayString"
_AwcFileXferFileFirmwareSystem_Object = MibScalar
awcFileXferFileFirmwareSystem = _AwcFileXferFileFirmwareSystem_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 4, 9),
    _AwcFileXferFileFirmwareSystem_Type()
)
awcFileXferFileFirmwareSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFileXferFileFirmwareSystem.setStatus("current")


class _AwcFileXferFileFirmwareRadio0_Type(DisplayString):
    """Custom type awcFileXferFileFirmwareRadio0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AwcFileXferFileFirmwareRadio0_Type.__name__ = "DisplayString"
_AwcFileXferFileFirmwareRadio0_Object = MibScalar
awcFileXferFileFirmwareRadio0 = _AwcFileXferFileFirmwareRadio0_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 4, 10),
    _AwcFileXferFileFirmwareRadio0_Type()
)
awcFileXferFileFirmwareRadio0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFileXferFileFirmwareRadio0.setStatus("current")


class _AwcFileXferFileWebUI_Type(DisplayString):
    """Custom type awcFileXferFileWebUI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AwcFileXferFileWebUI_Type.__name__ = "DisplayString"
_AwcFileXferFileWebUI_Object = MibScalar
awcFileXferFileWebUI = _AwcFileXferFileWebUI_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 4, 11),
    _AwcFileXferFileWebUI_Type()
)
awcFileXferFileWebUI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFileXferFileWebUI.setStatus("current")


class _AwcFileXferFileFpgaPcmcia_Type(DisplayString):
    """Custom type awcFileXferFileFpgaPcmcia based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AwcFileXferFileFpgaPcmcia_Type.__name__ = "DisplayString"
_AwcFileXferFileFpgaPcmcia_Object = MibScalar
awcFileXferFileFpgaPcmcia = _AwcFileXferFileFpgaPcmcia_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 4, 12),
    _AwcFileXferFileFpgaPcmcia_Type()
)
awcFileXferFileFpgaPcmcia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFileXferFileFpgaPcmcia.setStatus("current")


class _AwcFileXferTftpPort_Type(Integer32):
    """Custom type awcFileXferTftpPort based on Integer32"""
    defaultValue = 69

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AwcFileXferTftpPort_Type.__name__ = "Integer32"
_AwcFileXferTftpPort_Object = MibScalar
awcFileXferTftpPort = _AwcFileXferTftpPort_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 4, 13),
    _AwcFileXferTftpPort_Type()
)
awcFileXferTftpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFileXferTftpPort.setStatus("current")


class _AwcFileXferFtpDirectory_Type(DisplayString):
    """Custom type awcFileXferFtpDirectory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AwcFileXferFtpDirectory_Type.__name__ = "DisplayString"
_AwcFileXferFtpDirectory_Object = MibScalar
awcFileXferFtpDirectory = _AwcFileXferFtpDirectory_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 4, 14),
    _AwcFileXferFtpDirectory_Type()
)
awcFileXferFtpDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFileXferFtpDirectory.setStatus("current")


class _AwcFileXferFilesFLASH_Type(DisplayString):
    """Custom type awcFileXferFilesFLASH based on DisplayString"""
    defaultValue = OctetString("AP340_latest.img")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AwcFileXferFilesFLASH_Type.__name__ = "DisplayString"
_AwcFileXferFilesFLASH_Object = MibScalar
awcFileXferFilesFLASH = _AwcFileXferFilesFLASH_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 4, 17),
    _AwcFileXferFilesFLASH_Type()
)
awcFileXferFilesFLASH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFileXferFilesFLASH.setStatus("current")


class _AwcFileXferFileFirmwareRadio1_Type(DisplayString):
    """Custom type awcFileXferFileFirmwareRadio1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AwcFileXferFileFirmwareRadio1_Type.__name__ = "DisplayString"
_AwcFileXferFileFirmwareRadio1_Object = MibScalar
awcFileXferFileFirmwareRadio1 = _AwcFileXferFileFirmwareRadio1_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 4, 18),
    _AwcFileXferFileFirmwareRadio1_Type()
)
awcFileXferFileFirmwareRadio1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFileXferFileFirmwareRadio1.setStatus("current")
_AwcIfTable_Object = MibTable
awcIfTable = _AwcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 5)
)
if mibBuilder.loadTexts:
    awcIfTable.setStatus("current")
_AwcIfEntry_Object = MibTableRow
awcIfEntry = _AwcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 5, 1)
)
awcIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    awcIfEntry.setStatus("current")
_AwcIfDefaultPhysAddress_Type = MacAddress
_AwcIfDefaultPhysAddress_Object = MibTableColumn
awcIfDefaultPhysAddress = _AwcIfDefaultPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 5, 1, 1),
    _AwcIfDefaultPhysAddress_Type()
)
awcIfDefaultPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcIfDefaultPhysAddress.setStatus("current")


class _AwcIfPhysAddress_Type(MacAddress):
    """Custom type awcIfPhysAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_AwcIfPhysAddress_Object = MibTableColumn
awcIfPhysAddress = _AwcIfPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 5, 1, 2),
    _AwcIfPhysAddress_Type()
)
awcIfPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcIfPhysAddress.setStatus("current")


class _AwcIfAdoptPrimaryIdentity_Type(TruthValue):
    """Custom type awcIfAdoptPrimaryIdentity based on TruthValue"""


_AwcIfAdoptPrimaryIdentity_Object = MibTableColumn
awcIfAdoptPrimaryIdentity = _AwcIfAdoptPrimaryIdentity_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 5, 1, 3),
    _AwcIfAdoptPrimaryIdentity_Type()
)
awcIfAdoptPrimaryIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcIfAdoptPrimaryIdentity.setStatus("current")


class _AwcIfDefaultIpAddress_Type(IpAddress):
    """Custom type awcIfDefaultIpAddress based on IpAddress"""
    defaultHexValue = "0A000001"


_AwcIfDefaultIpAddress_Object = MibTableColumn
awcIfDefaultIpAddress = _AwcIfDefaultIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 5, 1, 4),
    _AwcIfDefaultIpAddress_Type()
)
awcIfDefaultIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcIfDefaultIpAddress.setStatus("current")


class _AwcIfDefaultIpNetMask_Type(IpAddress):
    """Custom type awcIfDefaultIpNetMask based on IpAddress"""
    defaultHexValue = "FFFFFF00"


_AwcIfDefaultIpNetMask_Object = MibTableColumn
awcIfDefaultIpNetMask = _AwcIfDefaultIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 5, 1, 5),
    _AwcIfDefaultIpNetMask_Type()
)
awcIfDefaultIpNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcIfDefaultIpNetMask.setStatus("current")
_AwcIfIpAddress_Type = IpAddress
_AwcIfIpAddress_Object = MibTableColumn
awcIfIpAddress = _AwcIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 5, 1, 6),
    _AwcIfIpAddress_Type()
)
awcIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcIfIpAddress.setStatus("current")
_AwcIfIpNetMask_Type = IpAddress
_AwcIfIpNetMask_Object = MibTableColumn
awcIfIpNetMask = _AwcIfIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 5, 1, 7),
    _AwcIfIpNetMask_Type()
)
awcIfIpNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcIfIpNetMask.setStatus("current")
_AwcIfMSDUMaxLength_Type = Unsigned32
_AwcIfMSDUMaxLength_Object = MibTableColumn
awcIfMSDUMaxLength = _AwcIfMSDUMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 5, 1, 8),
    _AwcIfMSDUMaxLength_Type()
)
awcIfMSDUMaxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcIfMSDUMaxLength.setStatus("current")
_AwcIfOutDiscardsCoS0_Type = Counter32
_AwcIfOutDiscardsCoS0_Object = MibTableColumn
awcIfOutDiscardsCoS0 = _AwcIfOutDiscardsCoS0_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 5, 1, 9),
    _AwcIfOutDiscardsCoS0_Type()
)
awcIfOutDiscardsCoS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcIfOutDiscardsCoS0.setStatus("current")
_AwcIfOutDiscardsCoS1_Type = Counter32
_AwcIfOutDiscardsCoS1_Object = MibTableColumn
awcIfOutDiscardsCoS1 = _AwcIfOutDiscardsCoS1_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 5, 1, 10),
    _AwcIfOutDiscardsCoS1_Type()
)
awcIfOutDiscardsCoS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcIfOutDiscardsCoS1.setStatus("current")
_AwcIfOutDiscardsCoS2_Type = Counter32
_AwcIfOutDiscardsCoS2_Object = MibTableColumn
awcIfOutDiscardsCoS2 = _AwcIfOutDiscardsCoS2_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 5, 1, 11),
    _AwcIfOutDiscardsCoS2_Type()
)
awcIfOutDiscardsCoS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcIfOutDiscardsCoS2.setStatus("current")
_AwcIfOutDiscardsCoS3_Type = Counter32
_AwcIfOutDiscardsCoS3_Object = MibTableColumn
awcIfOutDiscardsCoS3 = _AwcIfOutDiscardsCoS3_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 5, 1, 12),
    _AwcIfOutDiscardsCoS3_Type()
)
awcIfOutDiscardsCoS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcIfOutDiscardsCoS3.setStatus("current")
_AwcIfOutDiscardsCoS4_Type = Counter32
_AwcIfOutDiscardsCoS4_Object = MibTableColumn
awcIfOutDiscardsCoS4 = _AwcIfOutDiscardsCoS4_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 5, 1, 13),
    _AwcIfOutDiscardsCoS4_Type()
)
awcIfOutDiscardsCoS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcIfOutDiscardsCoS4.setStatus("current")
_AwcIfOutDiscardsCoS5_Type = Counter32
_AwcIfOutDiscardsCoS5_Object = MibTableColumn
awcIfOutDiscardsCoS5 = _AwcIfOutDiscardsCoS5_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 5, 1, 14),
    _AwcIfOutDiscardsCoS5_Type()
)
awcIfOutDiscardsCoS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcIfOutDiscardsCoS5.setStatus("current")
_AwcIfOutDiscardsCoS6_Type = Counter32
_AwcIfOutDiscardsCoS6_Object = MibTableColumn
awcIfOutDiscardsCoS6 = _AwcIfOutDiscardsCoS6_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 5, 1, 15),
    _AwcIfOutDiscardsCoS6_Type()
)
awcIfOutDiscardsCoS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcIfOutDiscardsCoS6.setStatus("current")
_AwcIfOutDiscardsCoS7_Type = Counter32
_AwcIfOutDiscardsCoS7_Object = MibTableColumn
awcIfOutDiscardsCoS7 = _AwcIfOutDiscardsCoS7_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 5, 1, 16),
    _AwcIfOutDiscardsCoS7_Type()
)
awcIfOutDiscardsCoS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcIfOutDiscardsCoS7.setStatus("current")
_Awc802dot11_ObjectIdentity = ObjectIdentity
awc802dot11 = _Awc802dot11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 6)
)
_AwcDot11smt_ObjectIdentity = ObjectIdentity
awcDot11smt = _AwcDot11smt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1)
)
_AwcDot11StationConfigTable_Object = MibTable
awcDot11StationConfigTable = _AwcDot11StationConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1)
)
if mibBuilder.loadTexts:
    awcDot11StationConfigTable.setStatus("current")
_AwcDot11StationConfigEntry_Object = MibTableRow
awcDot11StationConfigEntry = _AwcDot11StationConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1, 1)
)
awcDot11StationConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    awcDot11StationConfigEntry.setStatus("current")


class _AwcDot11StationRole_Type(Integer32):
    """Custom type awcDot11StationRole based on Integer32"""
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
        *(("roleAP", 4),
          ("roleClient", 1),
          ("roleIBSS", 2),
          ("roleRepeater", 3))
    )


_AwcDot11StationRole_Type.__name__ = "Integer32"
_AwcDot11StationRole_Object = MibTableColumn
awcDot11StationRole = _AwcDot11StationRole_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1, 1, 1),
    _AwcDot11StationRole_Type()
)
awcDot11StationRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11StationRole.setStatus("current")


class _AwcDot11PowerManagementSubMode_Type(Unsigned32):
    """Custom type awcDot11PowerManagementSubMode based on Unsigned32"""
    defaultValue = 0


_AwcDot11PowerManagementSubMode_Object = MibTableColumn
awcDot11PowerManagementSubMode = _AwcDot11PowerManagementSubMode_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1, 1, 2),
    _AwcDot11PowerManagementSubMode_Type()
)
awcDot11PowerManagementSubMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11PowerManagementSubMode.setStatus("current")


class _AwcDot11UseAWCExtensions_Type(TruthValue):
    """Custom type awcDot11UseAWCExtensions based on TruthValue"""


_AwcDot11UseAWCExtensions_Object = MibTableColumn
awcDot11UseAWCExtensions = _AwcDot11UseAWCExtensions_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1, 1, 3),
    _AwcDot11UseAWCExtensions_Type()
)
awcDot11UseAWCExtensions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11UseAWCExtensions.setStatus("current")


class _AwcDot11AllowAssocBroadcastSSID_Type(TruthValue):
    """Custom type awcDot11AllowAssocBroadcastSSID based on TruthValue"""


_AwcDot11AllowAssocBroadcastSSID_Object = MibTableColumn
awcDot11AllowAssocBroadcastSSID = _AwcDot11AllowAssocBroadcastSSID_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1, 1, 4),
    _AwcDot11AllowAssocBroadcastSSID_Type()
)
awcDot11AllowAssocBroadcastSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11AllowAssocBroadcastSSID.setStatus("current")


class _AwcDot11PrivacyOptionImplementedMaxRate_Type(Integer32):
    """Custom type awcDot11PrivacyOptionImplementedMaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 127),
    )


_AwcDot11PrivacyOptionImplementedMaxRate_Type.__name__ = "Integer32"
_AwcDot11PrivacyOptionImplementedMaxRate_Object = MibTableColumn
awcDot11PrivacyOptionImplementedMaxRate = _AwcDot11PrivacyOptionImplementedMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1, 1, 5),
    _AwcDot11PrivacyOptionImplementedMaxRate_Type()
)
awcDot11PrivacyOptionImplementedMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11PrivacyOptionImplementedMaxRate.setStatus("current")


class _AwcDot11DesiredBSSLength_Type(Integer32):
    """Custom type awcDot11DesiredBSSLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AwcDot11DesiredBSSLength_Type.__name__ = "Integer32"
_AwcDot11DesiredBSSLength_Object = MibTableColumn
awcDot11DesiredBSSLength = _AwcDot11DesiredBSSLength_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1, 1, 6),
    _AwcDot11DesiredBSSLength_Type()
)
awcDot11DesiredBSSLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11DesiredBSSLength.setStatus("current")


class _AwcDot11EnetEncapsulationDefault_Type(Integer32):
    """Custom type awcDot11EnetEncapsulationDefault based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("encap802dot1H", 1),
          ("encapRfc1042", 2))
    )


_AwcDot11EnetEncapsulationDefault_Type.__name__ = "Integer32"
_AwcDot11EnetEncapsulationDefault_Object = MibTableColumn
awcDot11EnetEncapsulationDefault = _AwcDot11EnetEncapsulationDefault_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1, 1, 7),
    _AwcDot11EnetEncapsulationDefault_Type()
)
awcDot11EnetEncapsulationDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11EnetEncapsulationDefault.setStatus("current")


class _AwcDot11ForceReqFirmwareVersion_Type(TruthValue):
    """Custom type awcDot11ForceReqFirmwareVersion based on TruthValue"""


_AwcDot11ForceReqFirmwareVersion_Object = MibTableColumn
awcDot11ForceReqFirmwareVersion = _AwcDot11ForceReqFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1, 1, 8),
    _AwcDot11ForceReqFirmwareVersion_Type()
)
awcDot11ForceReqFirmwareVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11ForceReqFirmwareVersion.setStatus("current")


class _AwcDot11BridgeSpacing_Type(Unsigned32):
    """Custom type awcDot11BridgeSpacing based on Unsigned32"""
    defaultValue = 0


_AwcDot11BridgeSpacing_Object = MibTableColumn
awcDot11BridgeSpacing = _AwcDot11BridgeSpacing_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1, 1, 9),
    _AwcDot11BridgeSpacing_Type()
)
awcDot11BridgeSpacing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11BridgeSpacing.setStatus("current")


class _AwcDot11DesiredSSIDMaxAssociatedSTA_Type(Integer32):
    """Custom type awcDot11DesiredSSIDMaxAssociatedSTA based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2007),
    )


_AwcDot11DesiredSSIDMaxAssociatedSTA_Type.__name__ = "Integer32"
_AwcDot11DesiredSSIDMaxAssociatedSTA_Object = MibTableColumn
awcDot11DesiredSSIDMaxAssociatedSTA = _AwcDot11DesiredSSIDMaxAssociatedSTA_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1, 1, 10),
    _AwcDot11DesiredSSIDMaxAssociatedSTA_Type()
)
awcDot11DesiredSSIDMaxAssociatedSTA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11DesiredSSIDMaxAssociatedSTA.setStatus("current")


class _AwcDot11DesiredSSIDNumAssociatedSTA_Type(Integer32):
    """Custom type awcDot11DesiredSSIDNumAssociatedSTA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2007),
    )


_AwcDot11DesiredSSIDNumAssociatedSTA_Type.__name__ = "Integer32"
_AwcDot11DesiredSSIDNumAssociatedSTA_Object = MibTableColumn
awcDot11DesiredSSIDNumAssociatedSTA = _AwcDot11DesiredSSIDNumAssociatedSTA_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1, 1, 11),
    _AwcDot11DesiredSSIDNumAssociatedSTA_Type()
)
awcDot11DesiredSSIDNumAssociatedSTA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11DesiredSSIDNumAssociatedSTA.setStatus("current")


class _AwcDot11AuxiliarySSIDLength_Type(Integer32):
    """Custom type awcDot11AuxiliarySSIDLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2007),
    )


_AwcDot11AuxiliarySSIDLength_Type.__name__ = "Integer32"
_AwcDot11AuxiliarySSIDLength_Object = MibTableColumn
awcDot11AuxiliarySSIDLength = _AwcDot11AuxiliarySSIDLength_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1, 1, 12),
    _AwcDot11AuxiliarySSIDLength_Type()
)
awcDot11AuxiliarySSIDLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11AuxiliarySSIDLength.setStatus("current")
_AwcDot11MultipleSSIDPerBSSImplemented_Type = TruthValue
_AwcDot11MultipleSSIDPerBSSImplemented_Object = MibTableColumn
awcDot11MultipleSSIDPerBSSImplemented = _AwcDot11MultipleSSIDPerBSSImplemented_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1, 1, 13),
    _AwcDot11MultipleSSIDPerBSSImplemented_Type()
)
awcDot11MultipleSSIDPerBSSImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11MultipleSSIDPerBSSImplemented.setStatus("current")
_AwcDot11SymbolExtensionsImplemented_Type = TruthValue
_AwcDot11SymbolExtensionsImplemented_Object = MibTableColumn
awcDot11SymbolExtensionsImplemented = _AwcDot11SymbolExtensionsImplemented_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1, 1, 14),
    _AwcDot11SymbolExtensionsImplemented_Type()
)
awcDot11SymbolExtensionsImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11SymbolExtensionsImplemented.setStatus("current")


class _AwcDot11SymbolExtensionsEnabled_Type(TruthValue):
    """Custom type awcDot11SymbolExtensionsEnabled based on TruthValue"""


_AwcDot11SymbolExtensionsEnabled_Object = MibTableColumn
awcDot11SymbolExtensionsEnabled = _AwcDot11SymbolExtensionsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1, 1, 15),
    _AwcDot11SymbolExtensionsEnabled_Type()
)
awcDot11SymbolExtensionsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11SymbolExtensionsEnabled.setStatus("current")


class _AwcDot11DesiredSSIDMicAlgorithm_Type(AwcDot11MicAlgorithm):
    """Custom type awcDot11DesiredSSIDMicAlgorithm based on AwcDot11MicAlgorithm"""


_AwcDot11DesiredSSIDMicAlgorithm_Object = MibTableColumn
awcDot11DesiredSSIDMicAlgorithm = _AwcDot11DesiredSSIDMicAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1, 1, 16),
    _AwcDot11DesiredSSIDMicAlgorithm_Type()
)
awcDot11DesiredSSIDMicAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11DesiredSSIDMicAlgorithm.setStatus("current")


class _AwcDot11DesiredSSIDWEPKeyPermuteAlgorithm_Type(AwcDot11WEPKeyPermuteAlgorithm):
    """Custom type awcDot11DesiredSSIDWEPKeyPermuteAlgorithm based on AwcDot11WEPKeyPermuteAlgorithm"""


_AwcDot11DesiredSSIDWEPKeyPermuteAlgorithm_Object = MibTableColumn
awcDot11DesiredSSIDWEPKeyPermuteAlgorithm = _AwcDot11DesiredSSIDWEPKeyPermuteAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1, 1, 17),
    _AwcDot11DesiredSSIDWEPKeyPermuteAlgorithm_Type()
)
awcDot11DesiredSSIDWEPKeyPermuteAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11DesiredSSIDWEPKeyPermuteAlgorithm.setStatus("current")


class _AwcDot11DesiredSSIDInfrastructureWGB_Type(TruthValue):
    """Custom type awcDot11DesiredSSIDInfrastructureWGB based on TruthValue"""


_AwcDot11DesiredSSIDInfrastructureWGB_Object = MibTableColumn
awcDot11DesiredSSIDInfrastructureWGB = _AwcDot11DesiredSSIDInfrastructureWGB_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1, 1, 18),
    _AwcDot11DesiredSSIDInfrastructureWGB_Type()
)
awcDot11DesiredSSIDInfrastructureWGB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11DesiredSSIDInfrastructureWGB.setStatus("current")


class _AwcDot11DesiredSSIDDefaultPolId_Type(AwcPolId):
    """Custom type awcDot11DesiredSSIDDefaultPolId based on AwcPolId"""
    defaultValue = 0


_AwcDot11DesiredSSIDDefaultPolId_Object = MibTableColumn
awcDot11DesiredSSIDDefaultPolId = _AwcDot11DesiredSSIDDefaultPolId_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1, 1, 19),
    _AwcDot11DesiredSSIDDefaultPolId_Type()
)
awcDot11DesiredSSIDDefaultPolId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11DesiredSSIDDefaultPolId.setStatus("current")


class _AwcDot11DesiredSSIDDefaultVlanId_Type(AwcVlanId):
    """Custom type awcDot11DesiredSSIDDefaultVlanId based on AwcVlanId"""
    defaultValue = 0


_AwcDot11DesiredSSIDDefaultVlanId_Object = MibTableColumn
awcDot11DesiredSSIDDefaultVlanId = _AwcDot11DesiredSSIDDefaultVlanId_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1, 1, 20),
    _AwcDot11DesiredSSIDDefaultVlanId_Type()
)
awcDot11DesiredSSIDDefaultVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11DesiredSSIDDefaultVlanId.setStatus("current")


class _AwcDot11DesiredSSIDEnableProxyMobileIP_Type(TruthValue):
    """Custom type awcDot11DesiredSSIDEnableProxyMobileIP based on TruthValue"""


_AwcDot11DesiredSSIDEnableProxyMobileIP_Object = MibTableColumn
awcDot11DesiredSSIDEnableProxyMobileIP = _AwcDot11DesiredSSIDEnableProxyMobileIP_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1, 1, 21),
    _AwcDot11DesiredSSIDEnableProxyMobileIP_Type()
)
awcDot11DesiredSSIDEnableProxyMobileIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11DesiredSSIDEnableProxyMobileIP.setStatus("current")


class _AwcDot11InfrastructureSSID_Type(Integer32):
    """Custom type awcDot11InfrastructureSSID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2007),
    )


_AwcDot11InfrastructureSSID_Type.__name__ = "Integer32"
_AwcDot11InfrastructureSSID_Object = MibTableColumn
awcDot11InfrastructureSSID = _AwcDot11InfrastructureSSID_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1, 1, 22),
    _AwcDot11InfrastructureSSID_Type()
)
awcDot11InfrastructureSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11InfrastructureSSID.setStatus("current")
_AwcDot11QBSSElementImplemented_Type = TruthValue
_AwcDot11QBSSElementImplemented_Object = MibTableColumn
awcDot11QBSSElementImplemented = _AwcDot11QBSSElementImplemented_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1, 1, 23),
    _AwcDot11QBSSElementImplemented_Type()
)
awcDot11QBSSElementImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11QBSSElementImplemented.setStatus("current")


class _AwcDot11QBSSElementEnabled_Type(TruthValue):
    """Custom type awcDot11QBSSElementEnabled based on TruthValue"""


_AwcDot11QBSSElementEnabled_Object = MibTableColumn
awcDot11QBSSElementEnabled = _AwcDot11QBSSElementEnabled_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1, 1, 24),
    _AwcDot11QBSSElementEnabled_Type()
)
awcDot11QBSSElementEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11QBSSElementEnabled.setStatus("current")


class _AwcDot11InfrastructureSSIDExclusive_Type(TruthValue):
    """Custom type awcDot11InfrastructureSSIDExclusive based on TruthValue"""


_AwcDot11InfrastructureSSIDExclusive_Object = MibTableColumn
awcDot11InfrastructureSSIDExclusive = _AwcDot11InfrastructureSSIDExclusive_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1, 1, 25),
    _AwcDot11InfrastructureSSIDExclusive_Type()
)
awcDot11InfrastructureSSIDExclusive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11InfrastructureSSIDExclusive.setStatus("current")


class _AwcDot11SendIGMPGeneralQuery_Type(TruthValue):
    """Custom type awcDot11SendIGMPGeneralQuery based on TruthValue"""


_AwcDot11SendIGMPGeneralQuery_Object = MibTableColumn
awcDot11SendIGMPGeneralQuery = _AwcDot11SendIGMPGeneralQuery_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1, 1, 26),
    _AwcDot11SendIGMPGeneralQuery_Type()
)
awcDot11SendIGMPGeneralQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11SendIGMPGeneralQuery.setStatus("current")


class _AwcDot11NonRootMobility_Type(Integer32):
    """Custom type awcDot11NonRootMobility based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mobile", 1),
          ("stationary", 2))
    )


_AwcDot11NonRootMobility_Type.__name__ = "Integer32"
_AwcDot11NonRootMobility_Object = MibTableColumn
awcDot11NonRootMobility = _AwcDot11NonRootMobility_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 1, 1, 27),
    _AwcDot11NonRootMobility_Type()
)
awcDot11NonRootMobility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11NonRootMobility.setStatus("current")
_AwcDot11AuthenticationAlgorithmsTable_Object = MibTable
awcDot11AuthenticationAlgorithmsTable = _AwcDot11AuthenticationAlgorithmsTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 2)
)
if mibBuilder.loadTexts:
    awcDot11AuthenticationAlgorithmsTable.setStatus("current")
_AwcDot11AuthenticationAlgorithmsEntry_Object = MibTableRow
awcDot11AuthenticationAlgorithmsEntry = _AwcDot11AuthenticationAlgorithmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 2, 1)
)
awcDot11AuthenticationAlgorithmsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "AWCVX-MIB", "awcDot11AuthenticationAlgorithmsIndex"),
)
if mibBuilder.loadTexts:
    awcDot11AuthenticationAlgorithmsEntry.setStatus("current")


class _AwcDot11AuthenticationAlgorithmsIndex_Type(Integer32):
    """Custom type awcDot11AuthenticationAlgorithmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_AwcDot11AuthenticationAlgorithmsIndex_Type.__name__ = "Integer32"
_AwcDot11AuthenticationAlgorithmsIndex_Object = MibTableColumn
awcDot11AuthenticationAlgorithmsIndex = _AwcDot11AuthenticationAlgorithmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 2, 1, 1),
    _AwcDot11AuthenticationAlgorithmsIndex_Type()
)
awcDot11AuthenticationAlgorithmsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    awcDot11AuthenticationAlgorithmsIndex.setStatus("current")
_AwcDot11AuthenticationRequireEAP_Type = TruthValue
_AwcDot11AuthenticationRequireEAP_Object = MibTableColumn
awcDot11AuthenticationRequireEAP = _AwcDot11AuthenticationRequireEAP_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 2, 1, 2),
    _AwcDot11AuthenticationRequireEAP_Type()
)
awcDot11AuthenticationRequireEAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11AuthenticationRequireEAP.setStatus("current")
_AwcDot11AuthenticationDefaultUcastAllowedToGoTo_Type = OctetString
_AwcDot11AuthenticationDefaultUcastAllowedToGoTo_Object = MibTableColumn
awcDot11AuthenticationDefaultUcastAllowedToGoTo = _AwcDot11AuthenticationDefaultUcastAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 2, 1, 3),
    _AwcDot11AuthenticationDefaultUcastAllowedToGoTo_Type()
)
awcDot11AuthenticationDefaultUcastAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11AuthenticationDefaultUcastAllowedToGoTo.setStatus("current")
_AwcDot11WEPDefaultKeysTable_Object = MibTable
awcDot11WEPDefaultKeysTable = _AwcDot11WEPDefaultKeysTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 3)
)
if mibBuilder.loadTexts:
    awcDot11WEPDefaultKeysTable.setStatus("current")
_AwcDot11WEPDefaultKeysEntry_Object = MibTableRow
awcDot11WEPDefaultKeysEntry = _AwcDot11WEPDefaultKeysEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 3, 1)
)
awcDot11WEPDefaultKeysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "AWCVX-MIB", "awcDot11WEPDefaultKeyIndex"),
)
if mibBuilder.loadTexts:
    awcDot11WEPDefaultKeysEntry.setStatus("current")


class _AwcDot11WEPDefaultKeyIndex_Type(Integer32):
    """Custom type awcDot11WEPDefaultKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AwcDot11WEPDefaultKeyIndex_Type.__name__ = "Integer32"
_AwcDot11WEPDefaultKeyIndex_Object = MibTableColumn
awcDot11WEPDefaultKeyIndex = _AwcDot11WEPDefaultKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 3, 1, 1),
    _AwcDot11WEPDefaultKeyIndex_Type()
)
awcDot11WEPDefaultKeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11WEPDefaultKeyIndex.setStatus("current")


class _AwcDot11WEPDefaultKeyLen_Type(Integer32):
    """Custom type awcDot11WEPDefaultKeyLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 13),
    )


_AwcDot11WEPDefaultKeyLen_Type.__name__ = "Integer32"
_AwcDot11WEPDefaultKeyLen_Object = MibTableColumn
awcDot11WEPDefaultKeyLen = _AwcDot11WEPDefaultKeyLen_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 3, 1, 2),
    _AwcDot11WEPDefaultKeyLen_Type()
)
awcDot11WEPDefaultKeyLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11WEPDefaultKeyLen.setStatus("current")
_AwcDot11WEPDefaultKeyValue_Type = WEPKeytype128
_AwcDot11WEPDefaultKeyValue_Object = MibTableColumn
awcDot11WEPDefaultKeyValue = _AwcDot11WEPDefaultKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 3, 1, 3),
    _AwcDot11WEPDefaultKeyValue_Type()
)
awcDot11WEPDefaultKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11WEPDefaultKeyValue.setStatus("current")
_AwcDot11PrivacyTable_Object = MibTable
awcDot11PrivacyTable = _AwcDot11PrivacyTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 5)
)
if mibBuilder.loadTexts:
    awcDot11PrivacyTable.setStatus("current")
_AwcDot11PrivacyEntry_Object = MibTableRow
awcDot11PrivacyEntry = _AwcDot11PrivacyEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 5, 1)
)
awcDot11PrivacyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    awcDot11PrivacyEntry.setStatus("current")


class _AwcDot11WEPDefaultKeyMaxIndex_Type(Integer32):
    """Custom type awcDot11WEPDefaultKeyMaxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AwcDot11WEPDefaultKeyMaxIndex_Type.__name__ = "Integer32"
_AwcDot11WEPDefaultKeyMaxIndex_Object = MibTableColumn
awcDot11WEPDefaultKeyMaxIndex = _AwcDot11WEPDefaultKeyMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 5, 1, 1),
    _AwcDot11WEPDefaultKeyMaxIndex_Type()
)
awcDot11WEPDefaultKeyMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11WEPDefaultKeyMaxIndex.setStatus("current")


class _AwcDot11AllowEncrypted_Type(TruthValue):
    """Custom type awcDot11AllowEncrypted based on TruthValue"""


_AwcDot11AllowEncrypted_Object = MibTableColumn
awcDot11AllowEncrypted = _AwcDot11AllowEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 5, 1, 2),
    _AwcDot11AllowEncrypted_Type()
)
awcDot11AllowEncrypted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11AllowEncrypted.setStatus("current")


class _AwcDot11WEPKeyMaxLen_Type(Integer32):
    """Custom type awcDot11WEPKeyMaxLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AwcDot11WEPKeyMaxLen_Type.__name__ = "Integer32"
_AwcDot11WEPKeyMaxLen_Object = MibTableColumn
awcDot11WEPKeyMaxLen = _AwcDot11WEPKeyMaxLen_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 5, 1, 3),
    _AwcDot11WEPKeyMaxLen_Type()
)
awcDot11WEPKeyMaxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11WEPKeyMaxLen.setStatus("current")
_AwcDot11LEAPUserName_Type = OctetString
_AwcDot11LEAPUserName_Object = MibTableColumn
awcDot11LEAPUserName = _AwcDot11LEAPUserName_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 5, 1, 4),
    _AwcDot11LEAPUserName_Type()
)
awcDot11LEAPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11LEAPUserName.setStatus("current")


class _AwcDot11LEAPPassword_Type(OctetString):
    """Custom type awcDot11LEAPPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AwcDot11LEAPPassword_Type.__name__ = "OctetString"
_AwcDot11LEAPPassword_Object = MibTableColumn
awcDot11LEAPPassword = _AwcDot11LEAPPassword_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 5, 1, 5),
    _AwcDot11LEAPPassword_Type()
)
awcDot11LEAPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11LEAPPassword.setStatus("current")
_AwcDot11DesiredBSSTable_Object = MibTable
awcDot11DesiredBSSTable = _AwcDot11DesiredBSSTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 6)
)
if mibBuilder.loadTexts:
    awcDot11DesiredBSSTable.setStatus("current")
_AwcDot11DesiredBSSEntry_Object = MibTableRow
awcDot11DesiredBSSEntry = _AwcDot11DesiredBSSEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 6, 1)
)
awcDot11DesiredBSSEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "AWCVX-MIB", "awcDot11DesiredBSSIndex"),
)
if mibBuilder.loadTexts:
    awcDot11DesiredBSSEntry.setStatus("current")


class _AwcDot11DesiredBSSIndex_Type(Integer32):
    """Custom type awcDot11DesiredBSSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AwcDot11DesiredBSSIndex_Type.__name__ = "Integer32"
_AwcDot11DesiredBSSIndex_Object = MibTableColumn
awcDot11DesiredBSSIndex = _AwcDot11DesiredBSSIndex_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 6, 1, 1),
    _AwcDot11DesiredBSSIndex_Type()
)
awcDot11DesiredBSSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11DesiredBSSIndex.setStatus("current")


class _AwcDot11DesiredBSS_Type(MacAddress):
    """Custom type awcDot11DesiredBSS based on MacAddress"""
    defaultHexValue = "000000000000"


_AwcDot11DesiredBSS_Object = MibTableColumn
awcDot11DesiredBSS = _AwcDot11DesiredBSS_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 6, 1, 2),
    _AwcDot11DesiredBSS_Type()
)
awcDot11DesiredBSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11DesiredBSS.setStatus("current")
_AwcDot11AuxiliarySSIDTable_Object = MibTable
awcDot11AuxiliarySSIDTable = _AwcDot11AuxiliarySSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 7)
)
if mibBuilder.loadTexts:
    awcDot11AuxiliarySSIDTable.setStatus("current")
_AwcDot11AuxiliarySSIDEntry_Object = MibTableRow
awcDot11AuxiliarySSIDEntry = _AwcDot11AuxiliarySSIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 7, 1)
)
awcDot11AuxiliarySSIDEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "AWCVX-MIB", "awcDot11AuxSSIDIndex"),
)
if mibBuilder.loadTexts:
    awcDot11AuxiliarySSIDEntry.setStatus("current")


class _AwcDot11AuxSSIDIndex_Type(Integer32):
    """Custom type awcDot11AuxSSIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2007),
    )


_AwcDot11AuxSSIDIndex_Type.__name__ = "Integer32"
_AwcDot11AuxSSIDIndex_Object = MibTableColumn
awcDot11AuxSSIDIndex = _AwcDot11AuxSSIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 7, 1, 1),
    _AwcDot11AuxSSIDIndex_Type()
)
awcDot11AuxSSIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11AuxSSIDIndex.setStatus("current")


class _AwcDot11AuxSSID_Type(OctetString):
    """Custom type awcDot11AuxSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AwcDot11AuxSSID_Type.__name__ = "OctetString"
_AwcDot11AuxSSID_Object = MibTableColumn
awcDot11AuxSSID = _AwcDot11AuxSSID_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 7, 1, 2),
    _AwcDot11AuxSSID_Type()
)
awcDot11AuxSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11AuxSSID.setStatus("current")


class _AwcDot11AuxSSIDMaxAssociatedSTA_Type(Integer32):
    """Custom type awcDot11AuxSSIDMaxAssociatedSTA based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2007),
    )


_AwcDot11AuxSSIDMaxAssociatedSTA_Type.__name__ = "Integer32"
_AwcDot11AuxSSIDMaxAssociatedSTA_Object = MibTableColumn
awcDot11AuxSSIDMaxAssociatedSTA = _AwcDot11AuxSSIDMaxAssociatedSTA_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 7, 1, 3),
    _AwcDot11AuxSSIDMaxAssociatedSTA_Type()
)
awcDot11AuxSSIDMaxAssociatedSTA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11AuxSSIDMaxAssociatedSTA.setStatus("current")


class _AwcDot11AuxSSIDNumAssociatedSTA_Type(Integer32):
    """Custom type awcDot11AuxSSIDNumAssociatedSTA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2007),
    )


_AwcDot11AuxSSIDNumAssociatedSTA_Type.__name__ = "Integer32"
_AwcDot11AuxSSIDNumAssociatedSTA_Object = MibTableColumn
awcDot11AuxSSIDNumAssociatedSTA = _AwcDot11AuxSSIDNumAssociatedSTA_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 7, 1, 4),
    _AwcDot11AuxSSIDNumAssociatedSTA_Type()
)
awcDot11AuxSSIDNumAssociatedSTA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11AuxSSIDNumAssociatedSTA.setStatus("current")


class _AwcDot11AuxSSIDDefaultPolId_Type(AwcPolId):
    """Custom type awcDot11AuxSSIDDefaultPolId based on AwcPolId"""
    defaultValue = 0


_AwcDot11AuxSSIDDefaultPolId_Object = MibTableColumn
awcDot11AuxSSIDDefaultPolId = _AwcDot11AuxSSIDDefaultPolId_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 7, 1, 6),
    _AwcDot11AuxSSIDDefaultPolId_Type()
)
awcDot11AuxSSIDDefaultPolId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11AuxSSIDDefaultPolId.setStatus("current")


class _AwcDot11AuxSSIDDefaultVlanId_Type(AwcVlanId):
    """Custom type awcDot11AuxSSIDDefaultVlanId based on AwcVlanId"""
    defaultValue = 0


_AwcDot11AuxSSIDDefaultVlanId_Object = MibTableColumn
awcDot11AuxSSIDDefaultVlanId = _AwcDot11AuxSSIDDefaultVlanId_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 7, 1, 7),
    _AwcDot11AuxSSIDDefaultVlanId_Type()
)
awcDot11AuxSSIDDefaultVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11AuxSSIDDefaultVlanId.setStatus("current")


class _AwcDot11AuxSSIDEnableProxyMobileIP_Type(TruthValue):
    """Custom type awcDot11AuxSSIDEnableProxyMobileIP based on TruthValue"""


_AwcDot11AuxSSIDEnableProxyMobileIP_Object = MibTableColumn
awcDot11AuxSSIDEnableProxyMobileIP = _AwcDot11AuxSSIDEnableProxyMobileIP_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 7, 1, 8),
    _AwcDot11AuxSSIDEnableProxyMobileIP_Type()
)
awcDot11AuxSSIDEnableProxyMobileIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11AuxSSIDEnableProxyMobileIP.setStatus("current")
_AwcDot11AuxSSIDAuthAlgTable_Object = MibTable
awcDot11AuxSSIDAuthAlgTable = _AwcDot11AuxSSIDAuthAlgTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 8)
)
if mibBuilder.loadTexts:
    awcDot11AuxSSIDAuthAlgTable.setStatus("current")
_AwcDot11AuxSSIDAuthAlgEntry_Object = MibTableRow
awcDot11AuxSSIDAuthAlgEntry = _AwcDot11AuxSSIDAuthAlgEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 8, 1)
)
awcDot11AuxSSIDAuthAlgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "AWCVX-MIB", "awcDot11AuxSSIDIndex"),
    (0, "AWCVX-MIB", "awcDot11AuxSSIDAuthAlgIndex"),
)
if mibBuilder.loadTexts:
    awcDot11AuxSSIDAuthAlgEntry.setStatus("current")


class _AwcDot11AuxSSIDAuthAlgIndex_Type(Integer32):
    """Custom type awcDot11AuxSSIDAuthAlgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_AwcDot11AuxSSIDAuthAlgIndex_Type.__name__ = "Integer32"
_AwcDot11AuxSSIDAuthAlgIndex_Object = MibTableColumn
awcDot11AuxSSIDAuthAlgIndex = _AwcDot11AuxSSIDAuthAlgIndex_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 8, 1, 1),
    _AwcDot11AuxSSIDAuthAlgIndex_Type()
)
awcDot11AuxSSIDAuthAlgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    awcDot11AuxSSIDAuthAlgIndex.setStatus("current")
_AwcDot11AuxSSIDAuthAlgEnable_Type = TruthValue
_AwcDot11AuxSSIDAuthAlgEnable_Object = MibTableColumn
awcDot11AuxSSIDAuthAlgEnable = _AwcDot11AuxSSIDAuthAlgEnable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 8, 1, 2),
    _AwcDot11AuxSSIDAuthAlgEnable_Type()
)
awcDot11AuxSSIDAuthAlgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11AuxSSIDAuthAlgEnable.setStatus("current")
_AwcDot11AuxSSIDAuthAlgRequireEAP_Type = TruthValue
_AwcDot11AuxSSIDAuthAlgRequireEAP_Object = MibTableColumn
awcDot11AuxSSIDAuthAlgRequireEAP = _AwcDot11AuxSSIDAuthAlgRequireEAP_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 8, 1, 3),
    _AwcDot11AuxSSIDAuthAlgRequireEAP_Type()
)
awcDot11AuxSSIDAuthAlgRequireEAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11AuxSSIDAuthAlgRequireEAP.setStatus("current")
_AwcDot11AuxSSIDAuthAlgDefaultUcastAllowedToGoTo_Type = OctetString
_AwcDot11AuxSSIDAuthAlgDefaultUcastAllowedToGoTo_Object = MibTableColumn
awcDot11AuxSSIDAuthAlgDefaultUcastAllowedToGoTo = _AwcDot11AuxSSIDAuthAlgDefaultUcastAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 8, 1, 4),
    _AwcDot11AuxSSIDAuthAlgDefaultUcastAllowedToGoTo_Type()
)
awcDot11AuxSSIDAuthAlgDefaultUcastAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11AuxSSIDAuthAlgDefaultUcastAllowedToGoTo.setStatus("current")
_AwcDot11AssignedAIDTable_Object = MibTable
awcDot11AssignedAIDTable = _AwcDot11AssignedAIDTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 9)
)
if mibBuilder.loadTexts:
    awcDot11AssignedAIDTable.setStatus("current")
_AwcDot11AssignedAIDEntry_Object = MibTableRow
awcDot11AssignedAIDEntry = _AwcDot11AssignedAIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 9, 1)
)
awcDot11AssignedAIDEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "AWCVX-MIB", "awcDot11AssignedAID"),
)
if mibBuilder.loadTexts:
    awcDot11AssignedAIDEntry.setStatus("current")


class _AwcDot11AssignedAID_Type(Integer32):
    """Custom type awcDot11AssignedAID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2007),
    )


_AwcDot11AssignedAID_Type.__name__ = "Integer32"
_AwcDot11AssignedAID_Object = MibTableColumn
awcDot11AssignedAID = _AwcDot11AssignedAID_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 9, 1, 1),
    _AwcDot11AssignedAID_Type()
)
awcDot11AssignedAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11AssignedAID.setStatus("current")


class _AwcDot11AssignedSTA_Type(MacAddress):
    """Custom type awcDot11AssignedSTA based on MacAddress"""
    defaultHexValue = "000000000000"


_AwcDot11AssignedSTA_Object = MibTableColumn
awcDot11AssignedSTA = _AwcDot11AssignedSTA_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 9, 1, 2),
    _AwcDot11AssignedSTA_Type()
)
awcDot11AssignedSTA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11AssignedSTA.setStatus("current")
_AwcDot11AccessPointCountersTable_Object = MibTable
awcDot11AccessPointCountersTable = _AwcDot11AccessPointCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 10)
)
if mibBuilder.loadTexts:
    awcDot11AccessPointCountersTable.setStatus("current")
_AwcDot11AccessPointCountersEntry_Object = MibTableRow
awcDot11AccessPointCountersEntry = _AwcDot11AccessPointCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 10, 1)
)
awcDot11AccessPointCountersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    awcDot11AccessPointCountersEntry.setStatus("current")
_AwcDot11AssociatedStationCount_Type = Counter32
_AwcDot11AssociatedStationCount_Object = MibTableColumn
awcDot11AssociatedStationCount = _AwcDot11AssociatedStationCount_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 10, 1, 1),
    _AwcDot11AssociatedStationCount_Type()
)
awcDot11AssociatedStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11AssociatedStationCount.setStatus("current")
_AwcDot11AuthenticatedStationCount_Type = Counter32
_AwcDot11AuthenticatedStationCount_Object = MibTableColumn
awcDot11AuthenticatedStationCount = _AwcDot11AuthenticatedStationCount_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 10, 1, 2),
    _AwcDot11AuthenticatedStationCount_Type()
)
awcDot11AuthenticatedStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11AuthenticatedStationCount.setStatus("current")
_AwcDot11ReassociatedStationCount_Type = Counter32
_AwcDot11ReassociatedStationCount_Object = MibTableColumn
awcDot11ReassociatedStationCount = _AwcDot11ReassociatedStationCount_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 10, 1, 3),
    _AwcDot11ReassociatedStationCount_Type()
)
awcDot11ReassociatedStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11ReassociatedStationCount.setStatus("current")
_AwcDot11RoamedStationCount_Type = Counter32
_AwcDot11RoamedStationCount_Object = MibTableColumn
awcDot11RoamedStationCount = _AwcDot11RoamedStationCount_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 10, 1, 4),
    _AwcDot11RoamedStationCount_Type()
)
awcDot11RoamedStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11RoamedStationCount.setStatus("current")
_AwcDot11DeauthenticateCount_Type = Counter32
_AwcDot11DeauthenticateCount_Object = MibTableColumn
awcDot11DeauthenticateCount = _AwcDot11DeauthenticateCount_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 10, 1, 5),
    _AwcDot11DeauthenticateCount_Type()
)
awcDot11DeauthenticateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11DeauthenticateCount.setStatus("current")
_AwcDot11DisassociateCount_Type = Counter32
_AwcDot11DisassociateCount_Object = MibTableColumn
awcDot11DisassociateCount = _AwcDot11DisassociateCount_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 10, 1, 6),
    _AwcDot11DisassociateCount_Type()
)
awcDot11DisassociateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11DisassociateCount.setStatus("current")
_AwcDot11EncapPktsMMH_Type = Counter32
_AwcDot11EncapPktsMMH_Object = MibTableColumn
awcDot11EncapPktsMMH = _AwcDot11EncapPktsMMH_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 10, 1, 7),
    _AwcDot11EncapPktsMMH_Type()
)
awcDot11EncapPktsMMH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11EncapPktsMMH.setStatus("current")
_AwcDot11DecapPktsMMH_Type = Counter32
_AwcDot11DecapPktsMMH_Object = MibTableColumn
awcDot11DecapPktsMMH = _AwcDot11DecapPktsMMH_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 10, 1, 8),
    _AwcDot11DecapPktsMMH_Type()
)
awcDot11DecapPktsMMH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11DecapPktsMMH.setStatus("current")
_AwcDot11EncapErrorsMMH_Type = Counter32
_AwcDot11EncapErrorsMMH_Object = MibTableColumn
awcDot11EncapErrorsMMH = _AwcDot11EncapErrorsMMH_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 10, 1, 9),
    _AwcDot11EncapErrorsMMH_Type()
)
awcDot11EncapErrorsMMH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11EncapErrorsMMH.setStatus("current")
_AwcDot11DecapErrorsMMH_Type = Counter32
_AwcDot11DecapErrorsMMH_Object = MibTableColumn
awcDot11DecapErrorsMMH = _AwcDot11DecapErrorsMMH_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 10, 1, 10),
    _AwcDot11DecapErrorsMMH_Type()
)
awcDot11DecapErrorsMMH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11DecapErrorsMMH.setStatus("current")
_AwcDot11DecapExistsMMH_Type = Counter32
_AwcDot11DecapExistsMMH_Object = MibTableColumn
awcDot11DecapExistsMMH = _AwcDot11DecapExistsMMH_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 10, 1, 11),
    _AwcDot11DecapExistsMMH_Type()
)
awcDot11DecapExistsMMH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11DecapExistsMMH.setStatus("current")
_AwcDot11DecapAccessMMH_Type = Counter32
_AwcDot11DecapAccessMMH_Object = MibTableColumn
awcDot11DecapAccessMMH = _AwcDot11DecapAccessMMH_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 1, 10, 1, 12),
    _AwcDot11DecapAccessMMH_Type()
)
awcDot11DecapAccessMMH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11DecapAccessMMH.setStatus("current")
_AwcDot11mac_ObjectIdentity = ObjectIdentity
awcDot11mac = _AwcDot11mac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 2)
)
_AwcDot11CountersTable_Object = MibTable
awcDot11CountersTable = _AwcDot11CountersTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 2, 2)
)
if mibBuilder.loadTexts:
    awcDot11CountersTable.setStatus("current")
_AwcDot11CountersEntry_Object = MibTableRow
awcDot11CountersEntry = _AwcDot11CountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 2, 2, 1)
)
awcDot11CountersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    awcDot11CountersEntry.setStatus("current")
_AwcDot11TxDeferEnergyCount_Type = Counter32
_AwcDot11TxDeferEnergyCount_Object = MibTableColumn
awcDot11TxDeferEnergyCount = _AwcDot11TxDeferEnergyCount_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 2, 2, 1, 1),
    _AwcDot11TxDeferEnergyCount_Type()
)
awcDot11TxDeferEnergyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11TxDeferEnergyCount.setStatus("current")
_AwcDot11RxMacCrcErrorCount_Type = Counter32
_AwcDot11RxMacCrcErrorCount_Object = MibTableColumn
awcDot11RxMacCrcErrorCount = _AwcDot11RxMacCrcErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 2, 2, 1, 2),
    _AwcDot11RxMacCrcErrorCount_Type()
)
awcDot11RxMacCrcErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11RxMacCrcErrorCount.setStatus("current")
_AwcDot11SsidMismatchCount_Type = Counter32
_AwcDot11SsidMismatchCount_Object = MibTableColumn
awcDot11SsidMismatchCount = _AwcDot11SsidMismatchCount_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 2, 2, 1, 3),
    _AwcDot11SsidMismatchCount_Type()
)
awcDot11SsidMismatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11SsidMismatchCount.setStatus("current")
_AwcDot11QoSTable_Object = MibTable
awcDot11QoSTable = _AwcDot11QoSTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 2, 4)
)
if mibBuilder.loadTexts:
    awcDot11QoSTable.setStatus("current")
_AwcDot11QoSEntry_Object = MibTableRow
awcDot11QoSEntry = _AwcDot11QoSEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 2, 4, 1)
)
awcDot11QoSEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "AWCVX-MIB", "awcDot11QoSCoS"),
)
if mibBuilder.loadTexts:
    awcDot11QoSEntry.setStatus("current")


class _AwcDot11QoSCoS_Type(Integer32):
    """Custom type awcDot11QoSCoS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AwcDot11QoSCoS_Type.__name__ = "Integer32"
_AwcDot11QoSCoS_Object = MibTableColumn
awcDot11QoSCoS = _AwcDot11QoSCoS_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 2, 4, 1, 1),
    _AwcDot11QoSCoS_Type()
)
awcDot11QoSCoS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    awcDot11QoSCoS.setStatus("current")


class _AwcDot11QoSCWmin_Type(Integer32):
    """Custom type awcDot11QoSCWmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_AwcDot11QoSCWmin_Type.__name__ = "Integer32"
_AwcDot11QoSCWmin_Object = MibTableColumn
awcDot11QoSCWmin = _AwcDot11QoSCWmin_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 2, 4, 1, 2),
    _AwcDot11QoSCWmin_Type()
)
awcDot11QoSCWmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11QoSCWmin.setStatus("current")


class _AwcDot11QoSCWmax_Type(Integer32):
    """Custom type awcDot11QoSCWmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_AwcDot11QoSCWmax_Type.__name__ = "Integer32"
_AwcDot11QoSCWmax_Object = MibTableColumn
awcDot11QoSCWmax = _AwcDot11QoSCWmax_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 2, 4, 1, 3),
    _AwcDot11QoSCWmax_Type()
)
awcDot11QoSCWmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11QoSCWmax.setStatus("current")
_AwcDot11res_ObjectIdentity = ObjectIdentity
awcDot11res = _AwcDot11res_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 3)
)
_AwcDot11resAttribute_ObjectIdentity = ObjectIdentity
awcDot11resAttribute = _AwcDot11resAttribute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 3, 1)
)
_AwcDot11ResourceInfoTable_Object = MibTable
awcDot11ResourceInfoTable = _AwcDot11ResourceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 3, 1, 2)
)
if mibBuilder.loadTexts:
    awcDot11ResourceInfoTable.setStatus("current")
_AwcDot11ResourceInfoEntry_Object = MibTableRow
awcDot11ResourceInfoEntry = _AwcDot11ResourceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 3, 1, 2, 1)
)
awcDot11ResourceInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    awcDot11ResourceInfoEntry.setStatus("current")


class _AwcDot11FirmwareBootstrapVersion_Type(DisplayString):
    """Custom type awcDot11FirmwareBootstrapVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AwcDot11FirmwareBootstrapVersion_Type.__name__ = "DisplayString"
_AwcDot11FirmwareBootstrapVersion_Object = MibTableColumn
awcDot11FirmwareBootstrapVersion = _AwcDot11FirmwareBootstrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 3, 1, 2, 1, 1),
    _AwcDot11FirmwareBootstrapVersion_Type()
)
awcDot11FirmwareBootstrapVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11FirmwareBootstrapVersion.setStatus("current")
_AwcDot11phy_ObjectIdentity = ObjectIdentity
awcDot11phy = _AwcDot11phy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 4)
)
_AwcDot11PhyOperationTable_Object = MibTable
awcDot11PhyOperationTable = _AwcDot11PhyOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 4, 1)
)
if mibBuilder.loadTexts:
    awcDot11PhyOperationTable.setStatus("current")
_AwcDot11PhyOperationEntry_Object = MibTableRow
awcDot11PhyOperationEntry = _AwcDot11PhyOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 4, 1, 1)
)
awcDot11PhyOperationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    awcDot11PhyOperationEntry.setStatus("current")


class _AwcDot11CurrentCarrierSet_Type(Integer32):
    """Custom type awcDot11CurrentCarrierSet based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("australia", 8),
          ("belgium", 5),
          ("canada", 7),
          ("china", 16),
          ("europe", 1),
          ("europe5GHz", 12),
          ("france", 4),
          ("israel", 6),
          ("japan", 2),
          ("japan5GHz", 13),
          ("japanWide", 9),
          ("singapore5GHz", 14),
          ("spain", 3),
          ("taiwan5GHz", 15),
          ("usa", 0),
          ("usa5GHz", 11))
    )


_AwcDot11CurrentCarrierSet_Type.__name__ = "Integer32"
_AwcDot11CurrentCarrierSet_Object = MibTableColumn
awcDot11CurrentCarrierSet = _AwcDot11CurrentCarrierSet_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 4, 1, 1, 1),
    _AwcDot11CurrentCarrierSet_Type()
)
awcDot11CurrentCarrierSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11CurrentCarrierSet.setStatus("current")


class _AwcDot11ModulationType_Type(Integer32):
    """Custom type awcDot11ModulationType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mok", 2),
          ("standard", 1))
    )


_AwcDot11ModulationType_Type.__name__ = "Integer32"
_AwcDot11ModulationType_Object = MibTableColumn
awcDot11ModulationType = _AwcDot11ModulationType_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 4, 1, 1, 2),
    _AwcDot11ModulationType_Type()
)
awcDot11ModulationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11ModulationType.setStatus("current")


class _AwcDot11PreambleType_Type(Integer32):
    """Custom type awcDot11PreambleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 1),
          ("short", 2))
    )


_AwcDot11PreambleType_Type.__name__ = "Integer32"
_AwcDot11PreambleType_Object = MibTableColumn
awcDot11PreambleType = _AwcDot11PreambleType_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 4, 1, 1, 3),
    _AwcDot11PreambleType_Type()
)
awcDot11PreambleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11PreambleType.setStatus("current")


class _AwcDot11PHYType_Type(Integer32):
    """Custom type awcDot11PHYType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              11)
        )
    )
    namedValues = NamedValues(
        *(("dsss", 2),
          ("dsssDot11A", 11),
          ("fhss", 1),
          ("irbaseband", 3))
    )


_AwcDot11PHYType_Type.__name__ = "Integer32"
_AwcDot11PHYType_Object = MibTableColumn
awcDot11PHYType = _AwcDot11PHYType_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 4, 1, 1, 5),
    _AwcDot11PHYType_Type()
)
awcDot11PHYType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11PHYType.setStatus("current")
_AwcDot11PhyFHSSTable_Object = MibTable
awcDot11PhyFHSSTable = _AwcDot11PhyFHSSTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 4, 4)
)
if mibBuilder.loadTexts:
    awcDot11PhyFHSSTable.setStatus("current")
_AwcDot11PhyFHSSEntry_Object = MibTableRow
awcDot11PhyFHSSEntry = _AwcDot11PhyFHSSEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 4, 4, 1)
)
awcDot11PhyFHSSEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    awcDot11PhyFHSSEntry.setStatus("current")


class _AwcDot11Compatible3100_Type(TruthValue):
    """Custom type awcDot11Compatible3100 based on TruthValue"""


_AwcDot11Compatible3100_Object = MibTableColumn
awcDot11Compatible3100 = _AwcDot11Compatible3100_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 4, 4, 1, 1),
    _AwcDot11Compatible3100_Type()
)
awcDot11Compatible3100.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11Compatible3100.setStatus("current")
_AwcDot11PhyDSSSTable_Object = MibTable
awcDot11PhyDSSSTable = _AwcDot11PhyDSSSTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 4, 5)
)
if mibBuilder.loadTexts:
    awcDot11PhyDSSSTable.setStatus("current")
_AwcDot11PhyDSSSEntry_Object = MibTableRow
awcDot11PhyDSSSEntry = _AwcDot11PhyDSSSEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 4, 5, 1)
)
awcDot11PhyDSSSEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    awcDot11PhyDSSSEntry.setStatus("current")


class _AwcDot11Compatible4500_Type(TruthValue):
    """Custom type awcDot11Compatible4500 based on TruthValue"""


_AwcDot11Compatible4500_Object = MibTableColumn
awcDot11Compatible4500 = _AwcDot11Compatible4500_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 4, 5, 1, 1),
    _AwcDot11Compatible4500_Type()
)
awcDot11Compatible4500.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11Compatible4500.setStatus("current")
_AwcDot11ChannelAutoImplemented_Type = TruthValue
_AwcDot11ChannelAutoImplemented_Object = MibTableColumn
awcDot11ChannelAutoImplemented = _AwcDot11ChannelAutoImplemented_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 4, 5, 1, 2),
    _AwcDot11ChannelAutoImplemented_Type()
)
awcDot11ChannelAutoImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11ChannelAutoImplemented.setStatus("current")


class _AwcDot11ChannelAutoEnabled_Type(TruthValue):
    """Custom type awcDot11ChannelAutoEnabled based on TruthValue"""


_AwcDot11ChannelAutoEnabled_Object = MibTableColumn
awcDot11ChannelAutoEnabled = _AwcDot11ChannelAutoEnabled_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 4, 5, 1, 3),
    _AwcDot11ChannelAutoEnabled_Type()
)
awcDot11ChannelAutoEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11ChannelAutoEnabled.setStatus("current")


class _AwcDot11CurrentChannel_Type(Integer32):
    """Custom type awcDot11CurrentChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_AwcDot11CurrentChannel_Type.__name__ = "Integer32"
_AwcDot11CurrentChannel_Object = MibTableColumn
awcDot11CurrentChannel = _AwcDot11CurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 4, 5, 1, 4),
    _AwcDot11CurrentChannel_Type()
)
awcDot11CurrentChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11CurrentChannel.setStatus("current")
_AwcDot11SupportedDataRatesPrivacyTable_Object = MibTable
awcDot11SupportedDataRatesPrivacyTable = _AwcDot11SupportedDataRatesPrivacyTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 4, 11)
)
if mibBuilder.loadTexts:
    awcDot11SupportedDataRatesPrivacyTable.setStatus("current")
_AwcDot11SupportedDataRatesPrivacyEntry_Object = MibTableRow
awcDot11SupportedDataRatesPrivacyEntry = _AwcDot11SupportedDataRatesPrivacyEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 4, 11, 1)
)
awcDot11SupportedDataRatesPrivacyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "AWCVX-MIB", "awcDot11SupportedDataRatesPrivacyIndex"),
)
if mibBuilder.loadTexts:
    awcDot11SupportedDataRatesPrivacyEntry.setStatus("current")


class _AwcDot11SupportedDataRatesPrivacyIndex_Type(Integer32):
    """Custom type awcDot11SupportedDataRatesPrivacyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AwcDot11SupportedDataRatesPrivacyIndex_Type.__name__ = "Integer32"
_AwcDot11SupportedDataRatesPrivacyIndex_Object = MibTableColumn
awcDot11SupportedDataRatesPrivacyIndex = _AwcDot11SupportedDataRatesPrivacyIndex_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 4, 11, 1, 1),
    _AwcDot11SupportedDataRatesPrivacyIndex_Type()
)
awcDot11SupportedDataRatesPrivacyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11SupportedDataRatesPrivacyIndex.setStatus("current")


class _AwcDot11SupportedDataRatesPrivacyValue_Type(Integer32):
    """Custom type awcDot11SupportedDataRatesPrivacyValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 127),
    )


_AwcDot11SupportedDataRatesPrivacyValue_Type.__name__ = "Integer32"
_AwcDot11SupportedDataRatesPrivacyValue_Object = MibTableColumn
awcDot11SupportedDataRatesPrivacyValue = _AwcDot11SupportedDataRatesPrivacyValue_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 4, 11, 1, 2),
    _AwcDot11SupportedDataRatesPrivacyValue_Type()
)
awcDot11SupportedDataRatesPrivacyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11SupportedDataRatesPrivacyValue.setStatus("current")
_AwcDot11SupportedDataRatesPrivacyImplemented_Type = TruthValue
_AwcDot11SupportedDataRatesPrivacyImplemented_Object = MibTableColumn
awcDot11SupportedDataRatesPrivacyImplemented = _AwcDot11SupportedDataRatesPrivacyImplemented_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 4, 11, 1, 3),
    _AwcDot11SupportedDataRatesPrivacyImplemented_Type()
)
awcDot11SupportedDataRatesPrivacyImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11SupportedDataRatesPrivacyImplemented.setStatus("current")
_AwcDot11ChanSelectTable_Object = MibTable
awcDot11ChanSelectTable = _AwcDot11ChanSelectTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 4, 12)
)
if mibBuilder.loadTexts:
    awcDot11ChanSelectTable.setStatus("current")
_AwcDot11ChanSelectEntry_Object = MibTableRow
awcDot11ChanSelectEntry = _AwcDot11ChanSelectEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 4, 12, 1)
)
awcDot11ChanSelectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "AWCVX-MIB", "awcDot11ChanSelectChannel"),
)
if mibBuilder.loadTexts:
    awcDot11ChanSelectEntry.setStatus("current")


class _AwcDot11ChanSelectChannel_Type(Integer32):
    """Custom type awcDot11ChanSelectChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_AwcDot11ChanSelectChannel_Type.__name__ = "Integer32"
_AwcDot11ChanSelectChannel_Object = MibTableColumn
awcDot11ChanSelectChannel = _AwcDot11ChanSelectChannel_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 4, 12, 1, 1),
    _AwcDot11ChanSelectChannel_Type()
)
awcDot11ChanSelectChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11ChanSelectChannel.setStatus("current")


class _AwcDot11ChanSelectEnable_Type(TruthValue):
    """Custom type awcDot11ChanSelectEnable based on TruthValue"""


_AwcDot11ChanSelectEnable_Object = MibTableColumn
awcDot11ChanSelectEnable = _AwcDot11ChanSelectEnable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 6, 4, 12, 1, 2),
    _AwcDot11ChanSelectEnable_Type()
)
awcDot11ChanSelectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11ChanSelectEnable.setStatus("current")
_AwcUserMgr_ObjectIdentity = ObjectIdentity
awcUserMgr = _AwcUserMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 7)
)
_UserMgrConfigTable_Object = MibTable
userMgrConfigTable = _UserMgrConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 7, 1)
)
if mibBuilder.loadTexts:
    userMgrConfigTable.setStatus("current")
_UserMgrConfigEntry_Object = MibTableRow
userMgrConfigEntry = _UserMgrConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 7, 1, 1)
)
userMgrConfigEntry.setIndexNames(
    (0, "AWCVX-MIB", "userMgrUserIndex"),
)
if mibBuilder.loadTexts:
    userMgrConfigEntry.setStatus("current")
_UserMgrUserIndex_Type = Unsigned32
_UserMgrUserIndex_Object = MibTableColumn
userMgrUserIndex = _UserMgrUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 7, 1, 1, 1),
    _UserMgrUserIndex_Type()
)
userMgrUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userMgrUserIndex.setStatus("current")


class _UserMgrUserName_Type(DisplayString):
    """Custom type userMgrUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UserMgrUserName_Type.__name__ = "DisplayString"
_UserMgrUserName_Object = MibTableColumn
userMgrUserName = _UserMgrUserName_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 7, 1, 1, 2),
    _UserMgrUserName_Type()
)
userMgrUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userMgrUserName.setStatus("current")


class _UserMgrPassword_Type(OctetString):
    """Custom type userMgrPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_UserMgrPassword_Type.__name__ = "OctetString"
_UserMgrPassword_Object = MibTableColumn
userMgrPassword = _UserMgrPassword_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 7, 1, 1, 3),
    _UserMgrPassword_Type()
)
userMgrPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userMgrPassword.setStatus("current")
_UserMgrCapabilities_Type = Unsigned32
_UserMgrCapabilities_Object = MibTableColumn
userMgrCapabilities = _UserMgrCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 7, 1, 1, 4),
    _UserMgrCapabilities_Type()
)
userMgrCapabilities.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userMgrCapabilities.setStatus("current")
_UserMgrStatus_Type = RowStatus
_UserMgrStatus_Object = MibTableColumn
userMgrStatus = _UserMgrStatus_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 7, 1, 1, 5),
    _UserMgrStatus_Type()
)
userMgrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userMgrStatus.setStatus("current")


class _EnableUserMgr_Type(TruthValue):
    """Custom type enableUserMgr based on TruthValue"""


_EnableUserMgr_Object = MibScalar
enableUserMgr = _EnableUserMgr_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 7, 2),
    _EnableUserMgr_Type()
)
enableUserMgr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableUserMgr.setStatus("current")


class _AllowBrowseWithoutLogin_Type(TruthValue):
    """Custom type allowBrowseWithoutLogin based on TruthValue"""


_AllowBrowseWithoutLogin_Object = MibScalar
allowBrowseWithoutLogin = _AllowBrowseWithoutLogin_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 7, 3),
    _AllowBrowseWithoutLogin_Type()
)
allowBrowseWithoutLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allowBrowseWithoutLogin.setStatus("current")


class _ProtectLegalPage_Type(TruthValue):
    """Custom type protectLegalPage based on TruthValue"""


_ProtectLegalPage_Object = MibScalar
protectLegalPage = _ProtectLegalPage_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 7, 4),
    _ProtectLegalPage_Type()
)
protectLegalPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protectLegalPage.setStatus("current")
_AwcHttpd_ObjectIdentity = ObjectIdentity
awcHttpd = _AwcHttpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 8)
)


class _DefaultWebRoot_Type(DisplayString):
    """Custom type defaultWebRoot based on DisplayString"""
    defaultValue = OctetString("mfs0:/StdUI/")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DefaultWebRoot_Type.__name__ = "DisplayString"
_DefaultWebRoot_Object = MibScalar
defaultWebRoot = _DefaultWebRoot_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 8, 1),
    _DefaultWebRoot_Type()
)
defaultWebRoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultWebRoot.setStatus("current")


class _DefaultHelpRoot_Type(DisplayString):
    """Custom type defaultHelpRoot based on DisplayString"""
    defaultValue = OctetString("http://www.cisco.com/warp/public/779/smbiz/prodconfig/help/eag/air/ap3xx")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DefaultHelpRoot_Type.__name__ = "DisplayString"
_DefaultHelpRoot_Object = MibScalar
defaultHelpRoot = _DefaultHelpRoot_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 8, 2),
    _DefaultHelpRoot_Type()
)
defaultHelpRoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultHelpRoot.setStatus("current")


class _GetWebUI_Type(DisplayString):
    """Custom type getWebUI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_GetWebUI_Type.__name__ = "DisplayString"
_GetWebUI_Object = MibScalar
getWebUI = _GetWebUI_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 8, 3),
    _GetWebUI_Type()
)
getWebUI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    getWebUI.setStatus("current")
_CmdInvokeGetWebUI_Type = AwcInvokeCommand
_CmdInvokeGetWebUI_Object = MibScalar
cmdInvokeGetWebUI = _CmdInvokeGetWebUI_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 8, 4),
    _CmdInvokeGetWebUI_Type()
)
cmdInvokeGetWebUI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdInvokeGetWebUI.setStatus("current")
_CmdStatusGetWebUI_Type = Integer32
_CmdStatusGetWebUI_Object = MibScalar
cmdStatusGetWebUI = _CmdStatusGetWebUI_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 8, 5),
    _CmdStatusGetWebUI_Type()
)
cmdStatusGetWebUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmdStatusGetWebUI.setStatus("current")


class _AwcHttpdPort_Type(Integer32):
    """Custom type awcHttpdPort based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AwcHttpdPort_Type.__name__ = "Integer32"
_AwcHttpdPort_Object = MibScalar
awcHttpdPort = _AwcHttpdPort_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 8, 6),
    _AwcHttpdPort_Type()
)
awcHttpdPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcHttpdPort.setStatus("current")


class _AwcConsoleAutoApply_Type(TruthValue):
    """Custom type awcConsoleAutoApply based on TruthValue"""


_AwcConsoleAutoApply_Object = MibScalar
awcConsoleAutoApply = _AwcConsoleAutoApply_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 8, 7),
    _AwcConsoleAutoApply_Type()
)
awcConsoleAutoApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcConsoleAutoApply.setStatus("current")
_AwcDnsRes_ObjectIdentity = ObjectIdentity
awcDnsRes = _AwcDnsRes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 9)
)


class _ResolverDomain_Type(DisplayString):
    """Custom type resolverDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ResolverDomain_Type.__name__ = "DisplayString"
_ResolverDomain_Object = MibScalar
resolverDomain = _ResolverDomain_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 9, 1),
    _ResolverDomain_Type()
)
resolverDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resolverDomain.setStatus("current")


class _ResolverDomainSuffix_Type(DisplayString):
    """Custom type resolverDomainSuffix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ResolverDomainSuffix_Type.__name__ = "DisplayString"
_ResolverDomainSuffix_Object = MibScalar
resolverDomainSuffix = _ResolverDomainSuffix_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 9, 2),
    _ResolverDomainSuffix_Type()
)
resolverDomainSuffix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resolverDomainSuffix.setStatus("current")
_ResolverDomainServerTable_Object = MibTable
resolverDomainServerTable = _ResolverDomainServerTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 9, 3)
)
if mibBuilder.loadTexts:
    resolverDomainServerTable.setStatus("current")
_ResolverDomainServerEntry_Object = MibTableRow
resolverDomainServerEntry = _ResolverDomainServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 9, 3, 1)
)
resolverDomainServerEntry.setIndexNames(
    (0, "AWCVX-MIB", "resolverDomainServerPriority"),
)
if mibBuilder.loadTexts:
    resolverDomainServerEntry.setStatus("current")


class _ResolverDomainServerPriority_Type(Integer32):
    """Custom type resolverDomainServerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ResolverDomainServerPriority_Type.__name__ = "Integer32"
_ResolverDomainServerPriority_Object = MibTableColumn
resolverDomainServerPriority = _ResolverDomainServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 9, 3, 1, 1),
    _ResolverDomainServerPriority_Type()
)
resolverDomainServerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resolverDomainServerPriority.setStatus("current")
_ResolverDomainServer_Type = DisplayString
_ResolverDomainServer_Object = MibTableColumn
resolverDomainServer = _ResolverDomainServer_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 9, 3, 1, 2),
    _ResolverDomainServer_Type()
)
resolverDomainServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resolverDomainServer.setStatus("current")


class _DefaultResolverDomain_Type(DisplayString):
    """Custom type defaultResolverDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DefaultResolverDomain_Type.__name__ = "DisplayString"
_DefaultResolverDomain_Object = MibScalar
defaultResolverDomain = _DefaultResolverDomain_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 9, 4),
    _DefaultResolverDomain_Type()
)
defaultResolverDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultResolverDomain.setStatus("current")
_DefaultResolverDomainServerTable_Object = MibTable
defaultResolverDomainServerTable = _DefaultResolverDomainServerTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 9, 5)
)
if mibBuilder.loadTexts:
    defaultResolverDomainServerTable.setStatus("current")
_DefaultResolverDomainServerEntry_Object = MibTableRow
defaultResolverDomainServerEntry = _DefaultResolverDomainServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 9, 5, 1)
)
defaultResolverDomainServerEntry.setIndexNames(
    (0, "AWCVX-MIB", "defaultResolverDomainServerPriority"),
)
if mibBuilder.loadTexts:
    defaultResolverDomainServerEntry.setStatus("current")


class _DefaultResolverDomainServerPriority_Type(Integer32):
    """Custom type defaultResolverDomainServerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_DefaultResolverDomainServerPriority_Type.__name__ = "Integer32"
_DefaultResolverDomainServerPriority_Object = MibTableColumn
defaultResolverDomainServerPriority = _DefaultResolverDomainServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 9, 5, 1, 1),
    _DefaultResolverDomainServerPriority_Type()
)
defaultResolverDomainServerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultResolverDomainServerPriority.setStatus("current")
_DefaultResolverDomainServer_Type = DisplayString
_DefaultResolverDomainServer_Object = MibTableColumn
defaultResolverDomainServer = _DefaultResolverDomainServer_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 9, 5, 1, 2),
    _DefaultResolverDomainServer_Type()
)
defaultResolverDomainServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultResolverDomainServer.setStatus("current")
_AwcSnmp_ObjectIdentity = ObjectIdentity
awcSnmp = _AwcSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 10)
)


class _SnmpTrapDest_Type(DisplayString):
    """Custom type snmpTrapDest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnmpTrapDest_Type.__name__ = "DisplayString"
_SnmpTrapDest_Object = MibScalar
snmpTrapDest = _SnmpTrapDest_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 10, 1),
    _SnmpTrapDest_Type()
)
snmpTrapDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapDest.setStatus("current")


class _SnmpTrapCommunity_Type(DisplayString):
    """Custom type snmpTrapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnmpTrapCommunity_Type.__name__ = "DisplayString"
_SnmpTrapCommunity_Object = MibScalar
snmpTrapCommunity = _SnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 10, 2),
    _SnmpTrapCommunity_Type()
)
snmpTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapCommunity.setStatus("current")
_AwcSntp_ObjectIdentity = ObjectIdentity
awcSntp = _AwcSntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 11)
)


class _DefaultSntpServer_Type(DisplayString):
    """Custom type defaultSntpServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DefaultSntpServer_Type.__name__ = "DisplayString"
_DefaultSntpServer_Object = MibScalar
defaultSntpServer = _DefaultSntpServer_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 11, 1),
    _DefaultSntpServer_Type()
)
defaultSntpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultSntpServer.setStatus("current")


class _SntpServer_Type(DisplayString):
    """Custom type sntpServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SntpServer_Type.__name__ = "DisplayString"
_SntpServer_Object = MibScalar
sntpServer = _SntpServer_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 11, 2),
    _SntpServer_Type()
)
sntpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpServer.setStatus("current")
_AwcForwardTbl_ObjectIdentity = ObjectIdentity
awcForwardTbl = _AwcForwardTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 12)
)
_AwcFtStatistics_ObjectIdentity = ObjectIdentity
awcFtStatistics = _AwcFtStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 1)
)
_AwcFtMcastAddr_Type = Integer32
_AwcFtMcastAddr_Object = MibScalar
awcFtMcastAddr = _AwcFtMcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 1, 1),
    _AwcFtMcastAddr_Type()
)
awcFtMcastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcFtMcastAddr.setStatus("current")
_AwcFtDsHost_Type = Integer32
_AwcFtDsHost_Object = MibScalar
awcFtDsHost = _AwcFtDsHost_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 1, 3),
    _AwcFtDsHost_Type()
)
awcFtDsHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcFtDsHost.setStatus("current")
_AwcFtBridgeHost_Type = Integer32
_AwcFtBridgeHost_Object = MibScalar
awcFtBridgeHost = _AwcFtBridgeHost_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 1, 5),
    _AwcFtBridgeHost_Type()
)
awcFtBridgeHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcFtBridgeHost.setStatus("current")
_AwcFtClientSTA_Type = Integer32
_AwcFtClientSTA_Object = MibScalar
awcFtClientSTA = _AwcFtClientSTA_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 1, 7),
    _AwcFtClientSTA_Type()
)
awcFtClientSTA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcFtClientSTA.setStatus("current")
_AwcFtClientSTASelf_Type = Integer32
_AwcFtClientSTASelf_Object = MibScalar
awcFtClientSTASelf = _AwcFtClientSTASelf_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 1, 8),
    _AwcFtClientSTASelf_Type()
)
awcFtClientSTASelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcFtClientSTASelf.setStatus("current")
_AwcFtBridge_Type = Integer32
_AwcFtBridge_Object = MibScalar
awcFtBridge = _AwcFtBridge_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 1, 9),
    _AwcFtBridge_Type()
)
awcFtBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcFtBridge.setStatus("current")
_AwcFtBridgeSelf_Type = Integer32
_AwcFtBridgeSelf_Object = MibScalar
awcFtBridgeSelf = _AwcFtBridgeSelf_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 1, 10),
    _AwcFtBridgeSelf_Type()
)
awcFtBridgeSelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcFtBridgeSelf.setStatus("current")
_AwcFtRepeater_Type = Integer32
_AwcFtRepeater_Object = MibScalar
awcFtRepeater = _AwcFtRepeater_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 1, 11),
    _AwcFtRepeater_Type()
)
awcFtRepeater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcFtRepeater.setStatus("current")
_AwcFtRepeaterSelf_Type = Integer32
_AwcFtRepeaterSelf_Object = MibScalar
awcFtRepeaterSelf = _AwcFtRepeaterSelf_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 1, 12),
    _AwcFtRepeaterSelf_Type()
)
awcFtRepeaterSelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcFtRepeaterSelf.setStatus("current")
_AwcFtAccessPoint_Type = Integer32
_AwcFtAccessPoint_Object = MibScalar
awcFtAccessPoint = _AwcFtAccessPoint_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 1, 13),
    _AwcFtAccessPoint_Type()
)
awcFtAccessPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcFtAccessPoint.setStatus("current")
_AwcFtBridgeRoot_Type = Integer32
_AwcFtBridgeRoot_Object = MibScalar
awcFtBridgeRoot = _AwcFtBridgeRoot_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 1, 15),
    _AwcFtBridgeRoot_Type()
)
awcFtBridgeRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcFtBridgeRoot.setStatus("current")
_AwcFtConfig_ObjectIdentity = ObjectIdentity
awcFtConfig = _AwcFtConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 2)
)


class _AwcFtMaxNumEntries_Type(Integer32):
    """Custom type awcFtMaxNumEntries based on Integer32"""
    defaultValue = 8192


_AwcFtMaxNumEntries_Object = MibScalar
awcFtMaxNumEntries = _AwcFtMaxNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 2, 1),
    _AwcFtMaxNumEntries_Type()
)
awcFtMaxNumEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFtMaxNumEntries.setStatus("current")


class _AwcFtTimeoutSecUnknown_Type(Unsigned32):
    """Custom type awcFtTimeoutSecUnknown based on Unsigned32"""
    defaultValue = 300


_AwcFtTimeoutSecUnknown_Object = MibScalar
awcFtTimeoutSecUnknown = _AwcFtTimeoutSecUnknown_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 2, 2),
    _AwcFtTimeoutSecUnknown_Type()
)
awcFtTimeoutSecUnknown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFtTimeoutSecUnknown.setStatus("current")
if mibBuilder.loadTexts:
    awcFtTimeoutSecUnknown.setUnits("seconds")


class _AwcFtTimeoutSecMcastAddr_Type(Unsigned32):
    """Custom type awcFtTimeoutSecMcastAddr based on Unsigned32"""
    defaultValue = 28800


_AwcFtTimeoutSecMcastAddr_Object = MibScalar
awcFtTimeoutSecMcastAddr = _AwcFtTimeoutSecMcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 2, 3),
    _AwcFtTimeoutSecMcastAddr_Type()
)
awcFtTimeoutSecMcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFtTimeoutSecMcastAddr.setStatus("current")
if mibBuilder.loadTexts:
    awcFtTimeoutSecMcastAddr.setUnits("seconds")


class _AwcFtTimeoutSecDsHost_Type(Unsigned32):
    """Custom type awcFtTimeoutSecDsHost based on Unsigned32"""
    defaultValue = 1800


_AwcFtTimeoutSecDsHost_Object = MibScalar
awcFtTimeoutSecDsHost = _AwcFtTimeoutSecDsHost_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 2, 4),
    _AwcFtTimeoutSecDsHost_Type()
)
awcFtTimeoutSecDsHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFtTimeoutSecDsHost.setStatus("current")
if mibBuilder.loadTexts:
    awcFtTimeoutSecDsHost.setUnits("seconds")


class _AwcFtTimeoutSecBridgeHost_Type(Unsigned32):
    """Custom type awcFtTimeoutSecBridgeHost based on Unsigned32"""
    defaultValue = 1800


_AwcFtTimeoutSecBridgeHost_Object = MibScalar
awcFtTimeoutSecBridgeHost = _AwcFtTimeoutSecBridgeHost_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 2, 5),
    _AwcFtTimeoutSecBridgeHost_Type()
)
awcFtTimeoutSecBridgeHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFtTimeoutSecBridgeHost.setStatus("current")
if mibBuilder.loadTexts:
    awcFtTimeoutSecBridgeHost.setUnits("seconds")


class _AwcFtTimeoutSecClientSTA_Type(Unsigned32):
    """Custom type awcFtTimeoutSecClientSTA based on Unsigned32"""
    defaultValue = 1800


_AwcFtTimeoutSecClientSTA_Object = MibScalar
awcFtTimeoutSecClientSTA = _AwcFtTimeoutSecClientSTA_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 2, 6),
    _AwcFtTimeoutSecClientSTA_Type()
)
awcFtTimeoutSecClientSTA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFtTimeoutSecClientSTA.setStatus("current")
if mibBuilder.loadTexts:
    awcFtTimeoutSecClientSTA.setUnits("seconds")


class _AwcFtTimeoutSecBridge_Type(Unsigned32):
    """Custom type awcFtTimeoutSecBridge based on Unsigned32"""
    defaultValue = 28800


_AwcFtTimeoutSecBridge_Object = MibScalar
awcFtTimeoutSecBridge = _AwcFtTimeoutSecBridge_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 2, 7),
    _AwcFtTimeoutSecBridge_Type()
)
awcFtTimeoutSecBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFtTimeoutSecBridge.setStatus("current")
if mibBuilder.loadTexts:
    awcFtTimeoutSecBridge.setUnits("seconds")


class _AwcFtTimeoutSecRepeater_Type(Unsigned32):
    """Custom type awcFtTimeoutSecRepeater based on Unsigned32"""
    defaultValue = 28800


_AwcFtTimeoutSecRepeater_Object = MibScalar
awcFtTimeoutSecRepeater = _AwcFtTimeoutSecRepeater_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 2, 8),
    _AwcFtTimeoutSecRepeater_Type()
)
awcFtTimeoutSecRepeater.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFtTimeoutSecRepeater.setStatus("current")
if mibBuilder.loadTexts:
    awcFtTimeoutSecRepeater.setUnits("seconds")


class _AwcFtTimeoutSecAccessPoint_Type(Unsigned32):
    """Custom type awcFtTimeoutSecAccessPoint based on Unsigned32"""
    defaultValue = 28800


_AwcFtTimeoutSecAccessPoint_Object = MibScalar
awcFtTimeoutSecAccessPoint = _AwcFtTimeoutSecAccessPoint_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 2, 9),
    _AwcFtTimeoutSecAccessPoint_Type()
)
awcFtTimeoutSecAccessPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFtTimeoutSecAccessPoint.setStatus("current")
if mibBuilder.loadTexts:
    awcFtTimeoutSecAccessPoint.setUnits("seconds")


class _AwcFtTimeoutSecBridgeRoot_Type(Unsigned32):
    """Custom type awcFtTimeoutSecBridgeRoot based on Unsigned32"""
    defaultValue = 28800


_AwcFtTimeoutSecBridgeRoot_Object = MibScalar
awcFtTimeoutSecBridgeRoot = _AwcFtTimeoutSecBridgeRoot_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 2, 10),
    _AwcFtTimeoutSecBridgeRoot_Type()
)
awcFtTimeoutSecBridgeRoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFtTimeoutSecBridgeRoot.setStatus("current")
if mibBuilder.loadTexts:
    awcFtTimeoutSecBridgeRoot.setUnits("seconds")


class _AwcFtEnableAwcTpFdbTable_Type(TruthValue):
    """Custom type awcFtEnableAwcTpFdbTable based on TruthValue"""


_AwcFtEnableAwcTpFdbTable_Object = MibScalar
awcFtEnableAwcTpFdbTable = _AwcFtEnableAwcTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 2, 11),
    _AwcFtEnableAwcTpFdbTable_Type()
)
awcFtEnableAwcTpFdbTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFtEnableAwcTpFdbTable.setStatus("current")


class _AwcFtEnableMacAuthServer_Type(TruthValue):
    """Custom type awcFtEnableMacAuthServer based on TruthValue"""


_AwcFtEnableMacAuthServer_Object = MibScalar
awcFtEnableMacAuthServer = _AwcFtEnableMacAuthServer_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 2, 12),
    _AwcFtEnableMacAuthServer_Type()
)
awcFtEnableMacAuthServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFtEnableMacAuthServer.setStatus("current")


class _AwcFtRogueApAlertTimeout_Type(Integer32):
    """Custom type awcFtRogueApAlertTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_AwcFtRogueApAlertTimeout_Type.__name__ = "Integer32"
_AwcFtRogueApAlertTimeout_Object = MibScalar
awcFtRogueApAlertTimeout = _AwcFtRogueApAlertTimeout_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 2, 13),
    _AwcFtRogueApAlertTimeout_Type()
)
awcFtRogueApAlertTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFtRogueApAlertTimeout.setStatus("current")


class _AwcFtEnableMacOrEapAuth_Type(TruthValue):
    """Custom type awcFtEnableMacOrEapAuth based on TruthValue"""


_AwcFtEnableMacOrEapAuth_Object = MibScalar
awcFtEnableMacOrEapAuth = _AwcFtEnableMacOrEapAuth_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 2, 14),
    _AwcFtEnableMacOrEapAuth_Type()
)
awcFtEnableMacOrEapAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFtEnableMacOrEapAuth.setStatus("current")


class _AwcFtDot1dTpFdbTableEnable_Type(TruthValue):
    """Custom type awcFtDot1dTpFdbTableEnable based on TruthValue"""


_AwcFtDot1dTpFdbTableEnable_Object = MibScalar
awcFtDot1dTpFdbTableEnable = _AwcFtDot1dTpFdbTableEnable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 2, 15),
    _AwcFtDot1dTpFdbTableEnable_Type()
)
awcFtDot1dTpFdbTableEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFtDot1dTpFdbTableEnable.setStatus("current")


class _AwcFtEnableMcastMapping_Type(TruthValue):
    """Custom type awcFtEnableMcastMapping based on TruthValue"""


_AwcFtEnableMcastMapping_Object = MibScalar
awcFtEnableMcastMapping = _AwcFtEnableMcastMapping_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 2, 16),
    _AwcFtEnableMcastMapping_Type()
)
awcFtEnableMcastMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcFtEnableMcastMapping.setStatus("current")
_AwcTpFdbTable_Object = MibTable
awcTpFdbTable = _AwcTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 3)
)
if mibBuilder.loadTexts:
    awcTpFdbTable.setStatus("current")
_AwcTpFdbEntry_Object = MibTableRow
awcTpFdbEntry = _AwcTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 3, 1)
)
awcTpFdbEntry.setIndexNames(
    (0, "AWCVX-MIB", "awcTpFdbAddress"),
)
if mibBuilder.loadTexts:
    awcTpFdbEntry.setStatus("current")
_AwcTpFdbAddress_Type = MacAddress
_AwcTpFdbAddress_Object = MibTableColumn
awcTpFdbAddress = _AwcTpFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 3, 1, 1),
    _AwcTpFdbAddress_Type()
)
awcTpFdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbAddress.setStatus("current")
_AwcTpFdbClassID_Type = AwcTpFdbClassID
_AwcTpFdbClassID_Object = MibTableColumn
awcTpFdbClassID = _AwcTpFdbClassID_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 3, 1, 2),
    _AwcTpFdbClassID_Type()
)
awcTpFdbClassID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbClassID.setStatus("current")
_AwcTpFdbSrcPktsImmed_Type = Counter32
_AwcTpFdbSrcPktsImmed_Object = MibTableColumn
awcTpFdbSrcPktsImmed = _AwcTpFdbSrcPktsImmed_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 3, 1, 3),
    _AwcTpFdbSrcPktsImmed_Type()
)
awcTpFdbSrcPktsImmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbSrcPktsImmed.setStatus("current")
_AwcTpFdbSrcOctetsImmed_Type = Counter32
_AwcTpFdbSrcOctetsImmed_Object = MibTableColumn
awcTpFdbSrcOctetsImmed = _AwcTpFdbSrcOctetsImmed_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 3, 1, 4),
    _AwcTpFdbSrcOctetsImmed_Type()
)
awcTpFdbSrcOctetsImmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbSrcOctetsImmed.setStatus("current")
_AwcTpFdbSrcErrorPktsImmed_Type = Counter32
_AwcTpFdbSrcErrorPktsImmed_Object = MibTableColumn
awcTpFdbSrcErrorPktsImmed = _AwcTpFdbSrcErrorPktsImmed_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 3, 1, 5),
    _AwcTpFdbSrcErrorPktsImmed_Type()
)
awcTpFdbSrcErrorPktsImmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbSrcErrorPktsImmed.setStatus("current")
_AwcTpFdbSrcErrorOctetsImmed_Type = Counter32
_AwcTpFdbSrcErrorOctetsImmed_Object = MibTableColumn
awcTpFdbSrcErrorOctetsImmed = _AwcTpFdbSrcErrorOctetsImmed_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 3, 1, 6),
    _AwcTpFdbSrcErrorOctetsImmed_Type()
)
awcTpFdbSrcErrorOctetsImmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbSrcErrorOctetsImmed.setStatus("current")
_AwcTpFdbDestPktsImmed_Type = Counter32
_AwcTpFdbDestPktsImmed_Object = MibTableColumn
awcTpFdbDestPktsImmed = _AwcTpFdbDestPktsImmed_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 3, 1, 7),
    _AwcTpFdbDestPktsImmed_Type()
)
awcTpFdbDestPktsImmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbDestPktsImmed.setStatus("current")
_AwcTpFdbDestOctetsImmed_Type = Counter32
_AwcTpFdbDestOctetsImmed_Object = MibTableColumn
awcTpFdbDestOctetsImmed = _AwcTpFdbDestOctetsImmed_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 3, 1, 8),
    _AwcTpFdbDestOctetsImmed_Type()
)
awcTpFdbDestOctetsImmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbDestOctetsImmed.setStatus("current")
_AwcTpFdbDestErrorPktsImmed_Type = Counter32
_AwcTpFdbDestErrorPktsImmed_Object = MibTableColumn
awcTpFdbDestErrorPktsImmed = _AwcTpFdbDestErrorPktsImmed_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 3, 1, 9),
    _AwcTpFdbDestErrorPktsImmed_Type()
)
awcTpFdbDestErrorPktsImmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbDestErrorPktsImmed.setStatus("current")
_AwcTpFdbDestErrorOctetsImmed_Type = Counter32
_AwcTpFdbDestErrorOctetsImmed_Object = MibTableColumn
awcTpFdbDestErrorOctetsImmed = _AwcTpFdbDestErrorOctetsImmed_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 3, 1, 10),
    _AwcTpFdbDestErrorOctetsImmed_Type()
)
awcTpFdbDestErrorOctetsImmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbDestErrorOctetsImmed.setStatus("current")
_AwcTpFdbDestMaxRetryErrorsImmed_Type = Counter32
_AwcTpFdbDestMaxRetryErrorsImmed_Object = MibTableColumn
awcTpFdbDestMaxRetryErrorsImmed = _AwcTpFdbDestMaxRetryErrorsImmed_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 3, 1, 11),
    _AwcTpFdbDestMaxRetryErrorsImmed_Type()
)
awcTpFdbDestMaxRetryErrorsImmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbDestMaxRetryErrorsImmed.setStatus("current")
_AwcTpFdbIPv4Addr_Type = IpAddress
_AwcTpFdbIPv4Addr_Object = MibTableColumn
awcTpFdbIPv4Addr = _AwcTpFdbIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 3, 1, 16),
    _AwcTpFdbIPv4Addr_Type()
)
awcTpFdbIPv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbIPv4Addr.setStatus("current")
_AwcTpFdbDdpTable_Object = MibTable
awcTpFdbDdpTable = _AwcTpFdbDdpTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 4)
)
if mibBuilder.loadTexts:
    awcTpFdbDdpTable.setStatus("current")
_AwcTpFdbDdpEntry_Object = MibTableRow
awcTpFdbDdpEntry = _AwcTpFdbDdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 4, 1)
)
awcTpFdbDdpEntry.setIndexNames(
    (0, "AWCVX-MIB", "awcTpFdbDdpAddress"),
)
if mibBuilder.loadTexts:
    awcTpFdbDdpEntry.setStatus("current")
_AwcTpFdbDdpAddress_Type = MacAddress
_AwcTpFdbDdpAddress_Object = MibTableColumn
awcTpFdbDdpAddress = _AwcTpFdbDdpAddress_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 4, 1, 1),
    _AwcTpFdbDdpAddress_Type()
)
awcTpFdbDdpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbDdpAddress.setStatus("current")


class _AwcTpFdbDdpSysName_Type(DisplayString):
    """Custom type awcTpFdbDdpSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AwcTpFdbDdpSysName_Type.__name__ = "DisplayString"
_AwcTpFdbDdpSysName_Object = MibTableColumn
awcTpFdbDdpSysName = _AwcTpFdbDdpSysName_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 4, 1, 2),
    _AwcTpFdbDdpSysName_Type()
)
awcTpFdbDdpSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbDdpSysName.setStatus("current")
_AwcTpFdbDdpProdDevID_Type = AwcDdpProdDevID
_AwcTpFdbDdpProdDevID_Object = MibTableColumn
awcTpFdbDdpProdDevID = _AwcTpFdbDdpProdDevID_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 4, 1, 3),
    _AwcTpFdbDdpProdDevID_Type()
)
awcTpFdbDdpProdDevID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbDdpProdDevID.setStatus("current")
_AwcTpFdbDdpRadioDevID_Type = AwcDdpRadioDevID
_AwcTpFdbDdpRadioDevID_Object = MibTableColumn
awcTpFdbDdpRadioDevID = _AwcTpFdbDdpRadioDevID_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 4, 1, 4),
    _AwcTpFdbDdpRadioDevID_Type()
)
awcTpFdbDdpRadioDevID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbDdpRadioDevID.setStatus("current")


class _AwcTpFdbDdpSwVerMajor_Type(Integer32):
    """Custom type awcTpFdbDdpSwVerMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AwcTpFdbDdpSwVerMajor_Type.__name__ = "Integer32"
_AwcTpFdbDdpSwVerMajor_Object = MibTableColumn
awcTpFdbDdpSwVerMajor = _AwcTpFdbDdpSwVerMajor_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 4, 1, 5),
    _AwcTpFdbDdpSwVerMajor_Type()
)
awcTpFdbDdpSwVerMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbDdpSwVerMajor.setStatus("current")


class _AwcTpFdbDdpSwVerMinor_Type(Integer32):
    """Custom type awcTpFdbDdpSwVerMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AwcTpFdbDdpSwVerMinor_Type.__name__ = "Integer32"
_AwcTpFdbDdpSwVerMinor_Object = MibTableColumn
awcTpFdbDdpSwVerMinor = _AwcTpFdbDdpSwVerMinor_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 4, 1, 6),
    _AwcTpFdbDdpSwVerMinor_Type()
)
awcTpFdbDdpSwVerMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbDdpSwVerMinor.setStatus("current")


class _AwcTpFdbDdpSwVerBeta_Type(Integer32):
    """Custom type awcTpFdbDdpSwVerBeta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AwcTpFdbDdpSwVerBeta_Type.__name__ = "Integer32"
_AwcTpFdbDdpSwVerBeta_Object = MibTableColumn
awcTpFdbDdpSwVerBeta = _AwcTpFdbDdpSwVerBeta_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 4, 1, 7),
    _AwcTpFdbDdpSwVerBeta_Type()
)
awcTpFdbDdpSwVerBeta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbDdpSwVerBeta.setStatus("current")
_AwcTpFdbDdpUptime_Type = Unsigned32
_AwcTpFdbDdpUptime_Object = MibTableColumn
awcTpFdbDdpUptime = _AwcTpFdbDdpUptime_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 4, 1, 8),
    _AwcTpFdbDdpUptime_Type()
)
awcTpFdbDdpUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbDdpUptime.setStatus("current")
if mibBuilder.loadTexts:
    awcTpFdbDdpUptime.setUnits("seconds")
_AwcTpFdbDdpNumAnnounceSent_Type = Unsigned32
_AwcTpFdbDdpNumAnnounceSent_Object = MibTableColumn
awcTpFdbDdpNumAnnounceSent = _AwcTpFdbDdpNumAnnounceSent_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 4, 1, 9),
    _AwcTpFdbDdpNumAnnounceSent_Type()
)
awcTpFdbDdpNumAnnounceSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbDdpNumAnnounceSent.setStatus("current")


class _AwcTpFdbDdpNumAssociated_Type(Integer32):
    """Custom type awcTpFdbDdpNumAssociated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2007),
    )


_AwcTpFdbDdpNumAssociated_Type.__name__ = "Integer32"
_AwcTpFdbDdpNumAssociated_Object = MibTableColumn
awcTpFdbDdpNumAssociated = _AwcTpFdbDdpNumAssociated_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 4, 1, 10),
    _AwcTpFdbDdpNumAssociated_Type()
)
awcTpFdbDdpNumAssociated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbDdpNumAssociated.setStatus("current")


class _AwcTpFdbDdpLoad_Type(Integer32):
    """Custom type awcTpFdbDdpLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AwcTpFdbDdpLoad_Type.__name__ = "Integer32"
_AwcTpFdbDdpLoad_Object = MibTableColumn
awcTpFdbDdpLoad = _AwcTpFdbDdpLoad_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 4, 1, 11),
    _AwcTpFdbDdpLoad_Type()
)
awcTpFdbDdpLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbDdpLoad.setStatus("current")


class _AwcTpFdbDdpDistFromDS_Type(Integer32):
    """Custom type awcTpFdbDdpDistFromDS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AwcTpFdbDdpDistFromDS_Type.__name__ = "Integer32"
_AwcTpFdbDdpDistFromDS_Object = MibTableColumn
awcTpFdbDdpDistFromDS = _AwcTpFdbDdpDistFromDS_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 4, 1, 12),
    _AwcTpFdbDdpDistFromDS_Type()
)
awcTpFdbDdpDistFromDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbDdpDistFromDS.setStatus("current")
_AwcDot11TpFdbTable_Object = MibTable
awcDot11TpFdbTable = _AwcDot11TpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 5)
)
if mibBuilder.loadTexts:
    awcDot11TpFdbTable.setStatus("current")
_AwcDot11TpFdbEntry_Object = MibTableRow
awcDot11TpFdbEntry = _AwcDot11TpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 5, 1)
)
awcDot11TpFdbEntry.setIndexNames(
    (0, "AWCVX-MIB", "awcDot11TpFdbAddress"),
)
if mibBuilder.loadTexts:
    awcDot11TpFdbEntry.setStatus("current")
_AwcDot11TpFdbAddress_Type = MacAddress
_AwcDot11TpFdbAddress_Object = MibTableColumn
awcDot11TpFdbAddress = _AwcDot11TpFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 5, 1, 1),
    _AwcDot11TpFdbAddress_Type()
)
awcDot11TpFdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11TpFdbAddress.setStatus("current")
_AwcDot11TpFdbAID_Type = Unsigned32
_AwcDot11TpFdbAID_Object = MibTableColumn
awcDot11TpFdbAID = _AwcDot11TpFdbAID_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 5, 1, 2),
    _AwcDot11TpFdbAID_Type()
)
awcDot11TpFdbAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11TpFdbAID.setStatus("current")
_AwcDot11TpFdbClientState_Type = AwcDot11ClientState
_AwcDot11TpFdbClientState_Object = MibTableColumn
awcDot11TpFdbClientState = _AwcDot11TpFdbClientState_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 5, 1, 3),
    _AwcDot11TpFdbClientState_Type()
)
awcDot11TpFdbClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11TpFdbClientState.setStatus("current")
_AwcDot11TpFdbTxShortRetries_Type = Counter32
_AwcDot11TpFdbTxShortRetries_Object = MibTableColumn
awcDot11TpFdbTxShortRetries = _AwcDot11TpFdbTxShortRetries_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 5, 1, 4),
    _AwcDot11TpFdbTxShortRetries_Type()
)
awcDot11TpFdbTxShortRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11TpFdbTxShortRetries.setStatus("current")
_AwcDot11TpFdbTxLongRetries_Type = Counter32
_AwcDot11TpFdbTxLongRetries_Object = MibTableColumn
awcDot11TpFdbTxLongRetries = _AwcDot11TpFdbTxLongRetries_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 5, 1, 5),
    _AwcDot11TpFdbTxLongRetries_Type()
)
awcDot11TpFdbTxLongRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11TpFdbTxLongRetries.setStatus("current")
_AwcDot11TpFdbLatestTxShortRetries_Type = Counter32
_AwcDot11TpFdbLatestTxShortRetries_Object = MibTableColumn
awcDot11TpFdbLatestTxShortRetries = _AwcDot11TpFdbLatestTxShortRetries_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 5, 1, 6),
    _AwcDot11TpFdbLatestTxShortRetries_Type()
)
awcDot11TpFdbLatestTxShortRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11TpFdbLatestTxShortRetries.setStatus("current")
_AwcDot11TpFdbLatestTxLongRetries_Type = Counter32
_AwcDot11TpFdbLatestTxLongRetries_Object = MibTableColumn
awcDot11TpFdbLatestTxLongRetries = _AwcDot11TpFdbLatestTxLongRetries_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 5, 1, 7),
    _AwcDot11TpFdbLatestTxLongRetries_Type()
)
awcDot11TpFdbLatestTxLongRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11TpFdbLatestTxLongRetries.setStatus("current")
_AwcDot11TpFdbRxWEPErrors_Type = Counter32
_AwcDot11TpFdbRxWEPErrors_Object = MibTableColumn
awcDot11TpFdbRxWEPErrors = _AwcDot11TpFdbRxWEPErrors_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 5, 1, 8),
    _AwcDot11TpFdbRxWEPErrors_Type()
)
awcDot11TpFdbRxWEPErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11TpFdbRxWEPErrors.setStatus("current")
_AwcDot11TpFdbLatestRxSignalStrength_Type = Unsigned32
_AwcDot11TpFdbLatestRxSignalStrength_Object = MibTableColumn
awcDot11TpFdbLatestRxSignalStrength = _AwcDot11TpFdbLatestRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 5, 1, 9),
    _AwcDot11TpFdbLatestRxSignalStrength_Type()
)
awcDot11TpFdbLatestRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11TpFdbLatestRxSignalStrength.setStatus("current")
_AwcDot11TpFdbLatestRxSignalQuality_Type = Unsigned32
_AwcDot11TpFdbLatestRxSignalQuality_Object = MibTableColumn
awcDot11TpFdbLatestRxSignalQuality = _AwcDot11TpFdbLatestRxSignalQuality_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 5, 1, 10),
    _AwcDot11TpFdbLatestRxSignalQuality_Type()
)
awcDot11TpFdbLatestRxSignalQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11TpFdbLatestRxSignalQuality.setStatus("current")
_AwcDot11TpFdbCapabilities_Type = Unsigned32
_AwcDot11TpFdbCapabilities_Object = MibTableColumn
awcDot11TpFdbCapabilities = _AwcDot11TpFdbCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 5, 1, 11),
    _AwcDot11TpFdbCapabilities_Type()
)
awcDot11TpFdbCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11TpFdbCapabilities.setStatus("current")
_AwcDot11TpFdbListenInterval_Type = Unsigned32
_AwcDot11TpFdbListenInterval_Object = MibTableColumn
awcDot11TpFdbListenInterval = _AwcDot11TpFdbListenInterval_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 5, 1, 12),
    _AwcDot11TpFdbListenInterval_Type()
)
awcDot11TpFdbListenInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11TpFdbListenInterval.setStatus("current")


class _AwcDot11TpFdbSupportedDataRates_Type(OctetString):
    """Custom type awcDot11TpFdbSupportedDataRates based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 126),
    )


_AwcDot11TpFdbSupportedDataRates_Type.__name__ = "OctetString"
_AwcDot11TpFdbSupportedDataRates_Object = MibTableColumn
awcDot11TpFdbSupportedDataRates = _AwcDot11TpFdbSupportedDataRates_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 5, 1, 13),
    _AwcDot11TpFdbSupportedDataRates_Type()
)
awcDot11TpFdbSupportedDataRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11TpFdbSupportedDataRates.setStatus("current")
_AwcDot11TpFdbPreferredTxRate_Type = Unsigned32
_AwcDot11TpFdbPreferredTxRate_Object = MibTableColumn
awcDot11TpFdbPreferredTxRate = _AwcDot11TpFdbPreferredTxRate_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 5, 1, 14),
    _AwcDot11TpFdbPreferredTxRate_Type()
)
awcDot11TpFdbPreferredTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11TpFdbPreferredTxRate.setStatus("current")
_AwcDot11TpFdbCurrentBSS_Type = MacAddress
_AwcDot11TpFdbCurrentBSS_Object = MibTableColumn
awcDot11TpFdbCurrentBSS = _AwcDot11TpFdbCurrentBSS_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 5, 1, 15),
    _AwcDot11TpFdbCurrentBSS_Type()
)
awcDot11TpFdbCurrentBSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11TpFdbCurrentBSS.setStatus("current")


class _AwcDot11TpFdbSSID_Type(Integer32):
    """Custom type awcDot11TpFdbSSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2007),
    )


_AwcDot11TpFdbSSID_Type.__name__ = "Integer32"
_AwcDot11TpFdbSSID_Object = MibTableColumn
awcDot11TpFdbSSID = _AwcDot11TpFdbSSID_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 5, 1, 16),
    _AwcDot11TpFdbSSID_Type()
)
awcDot11TpFdbSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11TpFdbSSID.setStatus("current")
_AwcDot11TpFdbVlanId_Type = AwcVlanId
_AwcDot11TpFdbVlanId_Object = MibTableColumn
awcDot11TpFdbVlanId = _AwcDot11TpFdbVlanId_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 5, 1, 17),
    _AwcDot11TpFdbVlanId_Type()
)
awcDot11TpFdbVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcDot11TpFdbVlanId.setStatus("current")
_AwcDot1dTpPortTable_Object = MibTable
awcDot1dTpPortTable = _AwcDot1dTpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 6)
)
if mibBuilder.loadTexts:
    awcDot1dTpPortTable.setStatus("current")
_AwcDot1dTpPortEntry_Object = MibTableRow
awcDot1dTpPortEntry = _AwcDot1dTpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 6, 1)
)
awcDot1dTpPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dTpPort"),
)
if mibBuilder.loadTexts:
    awcDot1dTpPortEntry.setStatus("current")
_AwcDot1dTpPortDefaultUcastAllowedToGoTo_Type = OctetString
_AwcDot1dTpPortDefaultUcastAllowedToGoTo_Object = MibTableColumn
awcDot1dTpPortDefaultUcastAllowedToGoTo = _AwcDot1dTpPortDefaultUcastAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 6, 1, 1),
    _AwcDot1dTpPortDefaultUcastAllowedToGoTo_Type()
)
awcDot1dTpPortDefaultUcastAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot1dTpPortDefaultUcastAllowedToGoTo.setStatus("current")
_AwcDot1dTpPortDefaultNUcastAllowedToGoTo_Type = OctetString
_AwcDot1dTpPortDefaultNUcastAllowedToGoTo_Object = MibTableColumn
awcDot1dTpPortDefaultNUcastAllowedToGoTo = _AwcDot1dTpPortDefaultNUcastAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 6, 1, 2),
    _AwcDot1dTpPortDefaultNUcastAllowedToGoTo_Type()
)
awcDot1dTpPortDefaultNUcastAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot1dTpPortDefaultNUcastAllowedToGoTo.setStatus("current")


class _AwcDot1dTpPortMaxNUcastPerSecond_Type(Unsigned32):
    """Custom type awcDot1dTpPortMaxNUcastPerSecond based on Unsigned32"""
    defaultValue = 0


_AwcDot1dTpPortMaxNUcastPerSecond_Object = MibTableColumn
awcDot1dTpPortMaxNUcastPerSecond = _AwcDot1dTpPortMaxNUcastPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 6, 1, 3),
    _AwcDot1dTpPortMaxNUcastPerSecond_Type()
)
awcDot1dTpPortMaxNUcastPerSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot1dTpPortMaxNUcastPerSecond.setStatus("current")


class _AwcDot1dTpPortDefaultInEthertypeFilterId_Type(Unsigned32):
    """Custom type awcDot1dTpPortDefaultInEthertypeFilterId based on Unsigned32"""
    defaultValue = 0


_AwcDot1dTpPortDefaultInEthertypeFilterId_Object = MibTableColumn
awcDot1dTpPortDefaultInEthertypeFilterId = _AwcDot1dTpPortDefaultInEthertypeFilterId_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 6, 1, 4),
    _AwcDot1dTpPortDefaultInEthertypeFilterId_Type()
)
awcDot1dTpPortDefaultInEthertypeFilterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot1dTpPortDefaultInEthertypeFilterId.setStatus("current")


class _AwcDot1dTpPortDefaultOutEthertypeFilterId_Type(Unsigned32):
    """Custom type awcDot1dTpPortDefaultOutEthertypeFilterId based on Unsigned32"""
    defaultValue = 0


_AwcDot1dTpPortDefaultOutEthertypeFilterId_Object = MibTableColumn
awcDot1dTpPortDefaultOutEthertypeFilterId = _AwcDot1dTpPortDefaultOutEthertypeFilterId_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 6, 1, 5),
    _AwcDot1dTpPortDefaultOutEthertypeFilterId_Type()
)
awcDot1dTpPortDefaultOutEthertypeFilterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot1dTpPortDefaultOutEthertypeFilterId.setStatus("current")


class _AwcDot1dTpPortDefaultInIpProtoFilterId_Type(Unsigned32):
    """Custom type awcDot1dTpPortDefaultInIpProtoFilterId based on Unsigned32"""
    defaultValue = 0


_AwcDot1dTpPortDefaultInIpProtoFilterId_Object = MibTableColumn
awcDot1dTpPortDefaultInIpProtoFilterId = _AwcDot1dTpPortDefaultInIpProtoFilterId_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 6, 1, 6),
    _AwcDot1dTpPortDefaultInIpProtoFilterId_Type()
)
awcDot1dTpPortDefaultInIpProtoFilterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot1dTpPortDefaultInIpProtoFilterId.setStatus("current")


class _AwcDot1dTpPortDefaultOutIpProtoFilterId_Type(Unsigned32):
    """Custom type awcDot1dTpPortDefaultOutIpProtoFilterId based on Unsigned32"""
    defaultValue = 0


_AwcDot1dTpPortDefaultOutIpProtoFilterId_Object = MibTableColumn
awcDot1dTpPortDefaultOutIpProtoFilterId = _AwcDot1dTpPortDefaultOutIpProtoFilterId_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 6, 1, 7),
    _AwcDot1dTpPortDefaultOutIpProtoFilterId_Type()
)
awcDot1dTpPortDefaultOutIpProtoFilterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot1dTpPortDefaultOutIpProtoFilterId.setStatus("current")


class _AwcDot1dTpPortDefaultInIpPortFilterId_Type(Unsigned32):
    """Custom type awcDot1dTpPortDefaultInIpPortFilterId based on Unsigned32"""
    defaultValue = 0


_AwcDot1dTpPortDefaultInIpPortFilterId_Object = MibTableColumn
awcDot1dTpPortDefaultInIpPortFilterId = _AwcDot1dTpPortDefaultInIpPortFilterId_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 6, 1, 8),
    _AwcDot1dTpPortDefaultInIpPortFilterId_Type()
)
awcDot1dTpPortDefaultInIpPortFilterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot1dTpPortDefaultInIpPortFilterId.setStatus("current")


class _AwcDot1dTpPortDefaultOutIpPortFilterId_Type(Unsigned32):
    """Custom type awcDot1dTpPortDefaultOutIpPortFilterId based on Unsigned32"""
    defaultValue = 0


_AwcDot1dTpPortDefaultOutIpPortFilterId_Object = MibTableColumn
awcDot1dTpPortDefaultOutIpPortFilterId = _AwcDot1dTpPortDefaultOutIpPortFilterId_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 6, 1, 9),
    _AwcDot1dTpPortDefaultOutIpPortFilterId_Type()
)
awcDot1dTpPortDefaultOutIpPortFilterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot1dTpPortDefaultOutIpPortFilterId.setStatus("current")
_AwcTpFdbAlertTable_Object = MibTable
awcTpFdbAlertTable = _AwcTpFdbAlertTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 7)
)
if mibBuilder.loadTexts:
    awcTpFdbAlertTable.setStatus("current")
_AwcTpFdbAlertEntry_Object = MibTableRow
awcTpFdbAlertEntry = _AwcTpFdbAlertEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 7, 1)
)
awcTpFdbAlertEntry.setIndexNames(
    (0, "AWCVX-MIB", "awcTpFdbAlertAddress"),
)
if mibBuilder.loadTexts:
    awcTpFdbAlertEntry.setStatus("current")
_AwcTpFdbAlertAddress_Type = MacAddress
_AwcTpFdbAlertAddress_Object = MibTableColumn
awcTpFdbAlertAddress = _AwcTpFdbAlertAddress_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 7, 1, 1),
    _AwcTpFdbAlertAddress_Type()
)
awcTpFdbAlertAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbAlertAddress.setStatus("current")
_AwcTpFdbFromAlertSrcPktsImmed_Type = Counter32
_AwcTpFdbFromAlertSrcPktsImmed_Object = MibTableColumn
awcTpFdbFromAlertSrcPktsImmed = _AwcTpFdbFromAlertSrcPktsImmed_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 7, 1, 2),
    _AwcTpFdbFromAlertSrcPktsImmed_Type()
)
awcTpFdbFromAlertSrcPktsImmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbFromAlertSrcPktsImmed.setStatus("current")
_AwcTpFdbFromAlertSrcOctetsImmed_Type = Counter32
_AwcTpFdbFromAlertSrcOctetsImmed_Object = MibTableColumn
awcTpFdbFromAlertSrcOctetsImmed = _AwcTpFdbFromAlertSrcOctetsImmed_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 7, 1, 3),
    _AwcTpFdbFromAlertSrcOctetsImmed_Type()
)
awcTpFdbFromAlertSrcOctetsImmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbFromAlertSrcOctetsImmed.setStatus("current")
_AwcTpFdbToAlertDestPktsImmed_Type = Counter32
_AwcTpFdbToAlertDestPktsImmed_Object = MibTableColumn
awcTpFdbToAlertDestPktsImmed = _AwcTpFdbToAlertDestPktsImmed_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 7, 1, 4),
    _AwcTpFdbToAlertDestPktsImmed_Type()
)
awcTpFdbToAlertDestPktsImmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbToAlertDestPktsImmed.setStatus("current")
_AwcTpFdbToAlertDestOctetsImmed_Type = Counter32
_AwcTpFdbToAlertDestOctetsImmed_Object = MibTableColumn
awcTpFdbToAlertDestOctetsImmed = _AwcTpFdbToAlertDestOctetsImmed_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 7, 1, 5),
    _AwcTpFdbToAlertDestOctetsImmed_Type()
)
awcTpFdbToAlertDestOctetsImmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbToAlertDestOctetsImmed.setStatus("current")
_AwcTpFdbAlertSentAlertTypePktsImmed_Type = Counter32
_AwcTpFdbAlertSentAlertTypePktsImmed_Object = MibTableColumn
awcTpFdbAlertSentAlertTypePktsImmed = _AwcTpFdbAlertSentAlertTypePktsImmed_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 7, 1, 6),
    _AwcTpFdbAlertSentAlertTypePktsImmed_Type()
)
awcTpFdbAlertSentAlertTypePktsImmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbAlertSentAlertTypePktsImmed.setStatus("current")
_AwcTpFdbAlertSentAlertTypeOctetsImmed_Type = Counter32
_AwcTpFdbAlertSentAlertTypeOctetsImmed_Object = MibTableColumn
awcTpFdbAlertSentAlertTypeOctetsImmed = _AwcTpFdbAlertSentAlertTypeOctetsImmed_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 7, 1, 7),
    _AwcTpFdbAlertSentAlertTypeOctetsImmed_Type()
)
awcTpFdbAlertSentAlertTypeOctetsImmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbAlertSentAlertTypeOctetsImmed.setStatus("current")
_AwcTpFdbAlertRcvdAlertTypePktsImmed_Type = Counter32
_AwcTpFdbAlertRcvdAlertTypePktsImmed_Object = MibTableColumn
awcTpFdbAlertRcvdAlertTypePktsImmed = _AwcTpFdbAlertRcvdAlertTypePktsImmed_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 7, 1, 8),
    _AwcTpFdbAlertRcvdAlertTypePktsImmed_Type()
)
awcTpFdbAlertRcvdAlertTypePktsImmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbAlertRcvdAlertTypePktsImmed.setStatus("current")
_AwcTpFdbAlertRcvdAlertTypeOctetsImmed_Type = Counter32
_AwcTpFdbAlertRcvdAlertTypeOctetsImmed_Object = MibTableColumn
awcTpFdbAlertRcvdAlertTypeOctetsImmed = _AwcTpFdbAlertRcvdAlertTypeOctetsImmed_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 12, 7, 1, 9),
    _AwcTpFdbAlertRcvdAlertTypeOctetsImmed_Type()
)
awcTpFdbAlertRcvdAlertTypeOctetsImmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcTpFdbAlertRcvdAlertTypeOctetsImmed.setStatus("current")
_AwcRipConfig_ObjectIdentity = ObjectIdentity
awcRipConfig = _AwcRipConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 13)
)
_AwcEventLog_ObjectIdentity = ObjectIdentity
awcEventLog = _AwcEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 14)
)


class _AwcEventOffsetGMT_Type(Integer32):
    """Custom type awcEventOffsetGMT based on Integer32"""
    defaultValue = -300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-720, 720),
    )


_AwcEventOffsetGMT_Type.__name__ = "Integer32"
_AwcEventOffsetGMT_Object = MibScalar
awcEventOffsetGMT = _AwcEventOffsetGMT_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 1),
    _AwcEventOffsetGMT_Type()
)
awcEventOffsetGMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventOffsetGMT.setStatus("current")
if mibBuilder.loadTexts:
    awcEventOffsetGMT.setUnits("minutes")


class _AwcEventUseDaylightSavingsTime_Type(TruthValue):
    """Custom type awcEventUseDaylightSavingsTime based on TruthValue"""


_AwcEventUseDaylightSavingsTime_Object = MibScalar
awcEventUseDaylightSavingsTime = _AwcEventUseDaylightSavingsTime_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 2),
    _AwcEventUseDaylightSavingsTime_Type()
)
awcEventUseDaylightSavingsTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventUseDaylightSavingsTime.setStatus("current")


class _AwcEventTimestampGMT_Type(Integer32):
    """Custom type awcEventTimestampGMT based on Integer32"""
    defaultValue = 0


_AwcEventTimestampGMT_Object = MibScalar
awcEventTimestampGMT = _AwcEventTimestampGMT_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 3),
    _AwcEventTimestampGMT_Type()
)
awcEventTimestampGMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventTimestampGMT.setStatus("current")
if mibBuilder.loadTexts:
    awcEventTimestampGMT.setUnits("seconds")
_AwcEventUptimeModifiedGMT_Type = Integer32
_AwcEventUptimeModifiedGMT_Object = MibScalar
awcEventUptimeModifiedGMT = _AwcEventUptimeModifiedGMT_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 4),
    _AwcEventUptimeModifiedGMT_Type()
)
awcEventUptimeModifiedGMT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcEventUptimeModifiedGMT.setStatus("current")
if mibBuilder.loadTexts:
    awcEventUptimeModifiedGMT.setUnits("seconds")


class _AwcEventDisplayWallClockTime_Type(TruthValue):
    """Custom type awcEventDisplayWallClockTime based on TruthValue"""


_AwcEventDisplayWallClockTime_Object = MibScalar
awcEventDisplayWallClockTime = _AwcEventDisplayWallClockTime_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 5),
    _AwcEventDisplayWallClockTime_Type()
)
awcEventDisplayWallClockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventDisplayWallClockTime.setStatus("current")


class _AwcEventDisplayUptimeAscending_Type(TruthValue):
    """Custom type awcEventDisplayUptimeAscending based on TruthValue"""


_AwcEventDisplayUptimeAscending_Object = MibScalar
awcEventDisplayUptimeAscending = _AwcEventDisplayUptimeAscending_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 6),
    _AwcEventDisplayUptimeAscending_Type()
)
awcEventDisplayUptimeAscending.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventDisplayUptimeAscending.setStatus("current")


class _AwcEventDetailDefault_Type(Integer32):
    """Custom type awcEventDetailDefault based on Integer32"""
    defaultValue = 24


_AwcEventDetailDefault_Object = MibScalar
awcEventDetailDefault = _AwcEventDetailDefault_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 7),
    _AwcEventDetailDefault_Type()
)
awcEventDetailDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventDetailDefault.setStatus("current")


class _AwcEventSeverityDispConsole_Type(AwcEventSeverity):
    """Custom type awcEventSeverityDispConsole based on AwcEventSeverity"""


_AwcEventSeverityDispConsole_Object = MibScalar
awcEventSeverityDispConsole = _AwcEventSeverityDispConsole_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 8),
    _AwcEventSeverityDispConsole_Type()
)
awcEventSeverityDispConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventSeverityDispConsole.setStatus("current")


class _AwcEventSeverityDispHtmlGUI_Type(AwcEventSeverity):
    """Custom type awcEventSeverityDispHtmlGUI based on AwcEventSeverity"""


_AwcEventSeverityDispHtmlGUI_Object = MibScalar
awcEventSeverityDispHtmlGUI = _AwcEventSeverityDispHtmlGUI_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 9),
    _AwcEventSeverityDispHtmlGUI_Type()
)
awcEventSeverityDispHtmlGUI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventSeverityDispHtmlGUI.setStatus("current")


class _AwcEventSeverityDispHtmlConsole_Type(AwcEventSeverity):
    """Custom type awcEventSeverityDispHtmlConsole based on AwcEventSeverity"""


_AwcEventSeverityDispHtmlConsole_Object = MibScalar
awcEventSeverityDispHtmlConsole = _AwcEventSeverityDispHtmlConsole_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 10),
    _AwcEventSeverityDispHtmlConsole_Type()
)
awcEventSeverityDispHtmlConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventSeverityDispHtmlConsole.setStatus("current")


class _AwcEventAlertSNMP_Type(TruthValue):
    """Custom type awcEventAlertSNMP based on TruthValue"""


_AwcEventAlertSNMP_Object = MibScalar
awcEventAlertSNMP = _AwcEventAlertSNMP_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 11),
    _AwcEventAlertSNMP_Type()
)
awcEventAlertSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventAlertSNMP.setStatus("current")


class _AwcEventAlertSyslog_Type(TruthValue):
    """Custom type awcEventAlertSyslog based on TruthValue"""


_AwcEventAlertSyslog_Object = MibScalar
awcEventAlertSyslog = _AwcEventAlertSyslog_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 12),
    _AwcEventAlertSyslog_Type()
)
awcEventAlertSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventAlertSyslog.setStatus("current")
_AwcEventStatistics_ObjectIdentity = ObjectIdentity
awcEventStatistics = _AwcEventStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 14)
)
_AwcEventCntSeverityNULL_Type = Counter32
_AwcEventCntSeverityNULL_Object = MibScalar
awcEventCntSeverityNULL = _AwcEventCntSeverityNULL_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 14, 1),
    _AwcEventCntSeverityNULL_Type()
)
awcEventCntSeverityNULL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcEventCntSeverityNULL.setStatus("current")
_AwcEventCntSeveritySilent_Type = Counter32
_AwcEventCntSeveritySilent_Object = MibScalar
awcEventCntSeveritySilent = _AwcEventCntSeveritySilent_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 14, 2),
    _AwcEventCntSeveritySilent_Type()
)
awcEventCntSeveritySilent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcEventCntSeveritySilent.setStatus("current")
_AwcEventCntSeveritySystemFatal_Type = Counter32
_AwcEventCntSeveritySystemFatal_Object = MibScalar
awcEventCntSeveritySystemFatal = _AwcEventCntSeveritySystemFatal_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 14, 3),
    _AwcEventCntSeveritySystemFatal_Type()
)
awcEventCntSeveritySystemFatal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcEventCntSeveritySystemFatal.setStatus("current")
_AwcEventCntSeverityProtocolFatal_Type = Counter32
_AwcEventCntSeverityProtocolFatal_Object = MibScalar
awcEventCntSeverityProtocolFatal = _AwcEventCntSeverityProtocolFatal_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 14, 4),
    _AwcEventCntSeverityProtocolFatal_Type()
)
awcEventCntSeverityProtocolFatal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcEventCntSeverityProtocolFatal.setStatus("current")
_AwcEventCntSeverityPortFatal_Type = Counter32
_AwcEventCntSeverityPortFatal_Object = MibScalar
awcEventCntSeverityPortFatal = _AwcEventCntSeverityPortFatal_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 14, 5),
    _AwcEventCntSeverityPortFatal_Type()
)
awcEventCntSeverityPortFatal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcEventCntSeverityPortFatal.setStatus("current")
_AwcEventCntSeveritySystemAlert_Type = Counter32
_AwcEventCntSeveritySystemAlert_Object = MibScalar
awcEventCntSeveritySystemAlert = _AwcEventCntSeveritySystemAlert_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 14, 6),
    _AwcEventCntSeveritySystemAlert_Type()
)
awcEventCntSeveritySystemAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcEventCntSeveritySystemAlert.setStatus("current")
_AwcEventCntSeverityProtocolAlert_Type = Counter32
_AwcEventCntSeverityProtocolAlert_Object = MibScalar
awcEventCntSeverityProtocolAlert = _AwcEventCntSeverityProtocolAlert_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 14, 7),
    _AwcEventCntSeverityProtocolAlert_Type()
)
awcEventCntSeverityProtocolAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcEventCntSeverityProtocolAlert.setStatus("current")
_AwcEventCntSeverityPortAlert_Type = Counter32
_AwcEventCntSeverityPortAlert_Object = MibScalar
awcEventCntSeverityPortAlert = _AwcEventCntSeverityPortAlert_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 14, 8),
    _AwcEventCntSeverityPortAlert_Type()
)
awcEventCntSeverityPortAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcEventCntSeverityPortAlert.setStatus("current")
_AwcEventCntSeverityExternalAlert_Type = Counter32
_AwcEventCntSeverityExternalAlert_Object = MibScalar
awcEventCntSeverityExternalAlert = _AwcEventCntSeverityExternalAlert_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 14, 9),
    _AwcEventCntSeverityExternalAlert_Type()
)
awcEventCntSeverityExternalAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcEventCntSeverityExternalAlert.setStatus("current")
_AwcEventCntSeveritySystemWarning_Type = Counter32
_AwcEventCntSeveritySystemWarning_Object = MibScalar
awcEventCntSeveritySystemWarning = _AwcEventCntSeveritySystemWarning_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 14, 10),
    _AwcEventCntSeveritySystemWarning_Type()
)
awcEventCntSeveritySystemWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcEventCntSeveritySystemWarning.setStatus("current")
_AwcEventCntSeverityProtocolWarning_Type = Counter32
_AwcEventCntSeverityProtocolWarning_Object = MibScalar
awcEventCntSeverityProtocolWarning = _AwcEventCntSeverityProtocolWarning_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 14, 11),
    _AwcEventCntSeverityProtocolWarning_Type()
)
awcEventCntSeverityProtocolWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcEventCntSeverityProtocolWarning.setStatus("current")
_AwcEventCntSeverityPortWarning_Type = Counter32
_AwcEventCntSeverityPortWarning_Object = MibScalar
awcEventCntSeverityPortWarning = _AwcEventCntSeverityPortWarning_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 14, 12),
    _AwcEventCntSeverityPortWarning_Type()
)
awcEventCntSeverityPortWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcEventCntSeverityPortWarning.setStatus("current")
_AwcEventCntSeverityExternalWarning_Type = Counter32
_AwcEventCntSeverityExternalWarning_Object = MibScalar
awcEventCntSeverityExternalWarning = _AwcEventCntSeverityExternalWarning_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 14, 13),
    _AwcEventCntSeverityExternalWarning_Type()
)
awcEventCntSeverityExternalWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcEventCntSeverityExternalWarning.setStatus("current")
_AwcEventCntSeveritySystemInfo_Type = Counter32
_AwcEventCntSeveritySystemInfo_Object = MibScalar
awcEventCntSeveritySystemInfo = _AwcEventCntSeveritySystemInfo_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 14, 14),
    _AwcEventCntSeveritySystemInfo_Type()
)
awcEventCntSeveritySystemInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcEventCntSeveritySystemInfo.setStatus("current")
_AwcEventCntSeverityProtocolInfo_Type = Counter32
_AwcEventCntSeverityProtocolInfo_Object = MibScalar
awcEventCntSeverityProtocolInfo = _AwcEventCntSeverityProtocolInfo_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 14, 15),
    _AwcEventCntSeverityProtocolInfo_Type()
)
awcEventCntSeverityProtocolInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcEventCntSeverityProtocolInfo.setStatus("current")
_AwcEventCntSeverityPortInfo_Type = Counter32
_AwcEventCntSeverityPortInfo_Object = MibScalar
awcEventCntSeverityPortInfo = _AwcEventCntSeverityPortInfo_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 14, 16),
    _AwcEventCntSeverityPortInfo_Type()
)
awcEventCntSeverityPortInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcEventCntSeverityPortInfo.setStatus("current")
_AwcEventCntSeverityExternalInfo_Type = Counter32
_AwcEventCntSeverityExternalInfo_Object = MibScalar
awcEventCntSeverityExternalInfo = _AwcEventCntSeverityExternalInfo_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 14, 17),
    _AwcEventCntSeverityExternalInfo_Type()
)
awcEventCntSeverityExternalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcEventCntSeverityExternalInfo.setStatus("current")
_AwcEventDisposition_ObjectIdentity = ObjectIdentity
awcEventDisposition = _AwcEventDisposition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 15)
)
_AwcEventDispSeverityNULL_Type = AwcEventDisposition
_AwcEventDispSeverityNULL_Object = MibScalar
awcEventDispSeverityNULL = _AwcEventDispSeverityNULL_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 15, 1),
    _AwcEventDispSeverityNULL_Type()
)
awcEventDispSeverityNULL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventDispSeverityNULL.setStatus("current")
_AwcEventDispSeveritySilent_Type = AwcEventDisposition
_AwcEventDispSeveritySilent_Object = MibScalar
awcEventDispSeveritySilent = _AwcEventDispSeveritySilent_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 15, 2),
    _AwcEventDispSeveritySilent_Type()
)
awcEventDispSeveritySilent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventDispSeveritySilent.setStatus("current")
_AwcEventDispSeveritySystemFatal_Type = AwcEventDisposition
_AwcEventDispSeveritySystemFatal_Object = MibScalar
awcEventDispSeveritySystemFatal = _AwcEventDispSeveritySystemFatal_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 15, 3),
    _AwcEventDispSeveritySystemFatal_Type()
)
awcEventDispSeveritySystemFatal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventDispSeveritySystemFatal.setStatus("current")
_AwcEventDispSeverityProtocolFatal_Type = AwcEventDisposition
_AwcEventDispSeverityProtocolFatal_Object = MibScalar
awcEventDispSeverityProtocolFatal = _AwcEventDispSeverityProtocolFatal_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 15, 4),
    _AwcEventDispSeverityProtocolFatal_Type()
)
awcEventDispSeverityProtocolFatal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventDispSeverityProtocolFatal.setStatus("current")
_AwcEventDispSeverityPortFatal_Type = AwcEventDisposition
_AwcEventDispSeverityPortFatal_Object = MibScalar
awcEventDispSeverityPortFatal = _AwcEventDispSeverityPortFatal_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 15, 5),
    _AwcEventDispSeverityPortFatal_Type()
)
awcEventDispSeverityPortFatal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventDispSeverityPortFatal.setStatus("current")
_AwcEventDispSeveritySystemAlert_Type = AwcEventDisposition
_AwcEventDispSeveritySystemAlert_Object = MibScalar
awcEventDispSeveritySystemAlert = _AwcEventDispSeveritySystemAlert_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 15, 6),
    _AwcEventDispSeveritySystemAlert_Type()
)
awcEventDispSeveritySystemAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventDispSeveritySystemAlert.setStatus("current")
_AwcEventDispSeverityProtocolAlert_Type = AwcEventDisposition
_AwcEventDispSeverityProtocolAlert_Object = MibScalar
awcEventDispSeverityProtocolAlert = _AwcEventDispSeverityProtocolAlert_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 15, 7),
    _AwcEventDispSeverityProtocolAlert_Type()
)
awcEventDispSeverityProtocolAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventDispSeverityProtocolAlert.setStatus("current")
_AwcEventDispSeverityPortAlert_Type = AwcEventDisposition
_AwcEventDispSeverityPortAlert_Object = MibScalar
awcEventDispSeverityPortAlert = _AwcEventDispSeverityPortAlert_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 15, 8),
    _AwcEventDispSeverityPortAlert_Type()
)
awcEventDispSeverityPortAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventDispSeverityPortAlert.setStatus("current")
_AwcEventDispSeverityExternalAlert_Type = AwcEventDisposition
_AwcEventDispSeverityExternalAlert_Object = MibScalar
awcEventDispSeverityExternalAlert = _AwcEventDispSeverityExternalAlert_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 15, 9),
    _AwcEventDispSeverityExternalAlert_Type()
)
awcEventDispSeverityExternalAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventDispSeverityExternalAlert.setStatus("current")
_AwcEventDispSeveritySystemWarning_Type = AwcEventDisposition
_AwcEventDispSeveritySystemWarning_Object = MibScalar
awcEventDispSeveritySystemWarning = _AwcEventDispSeveritySystemWarning_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 15, 10),
    _AwcEventDispSeveritySystemWarning_Type()
)
awcEventDispSeveritySystemWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventDispSeveritySystemWarning.setStatus("current")
_AwcEventDispSeverityProtocolWarning_Type = AwcEventDisposition
_AwcEventDispSeverityProtocolWarning_Object = MibScalar
awcEventDispSeverityProtocolWarning = _AwcEventDispSeverityProtocolWarning_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 15, 11),
    _AwcEventDispSeverityProtocolWarning_Type()
)
awcEventDispSeverityProtocolWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventDispSeverityProtocolWarning.setStatus("current")
_AwcEventDispSeverityPortWarning_Type = AwcEventDisposition
_AwcEventDispSeverityPortWarning_Object = MibScalar
awcEventDispSeverityPortWarning = _AwcEventDispSeverityPortWarning_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 15, 12),
    _AwcEventDispSeverityPortWarning_Type()
)
awcEventDispSeverityPortWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventDispSeverityPortWarning.setStatus("current")
_AwcEventDispSeverityExternalWarning_Type = AwcEventDisposition
_AwcEventDispSeverityExternalWarning_Object = MibScalar
awcEventDispSeverityExternalWarning = _AwcEventDispSeverityExternalWarning_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 15, 13),
    _AwcEventDispSeverityExternalWarning_Type()
)
awcEventDispSeverityExternalWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventDispSeverityExternalWarning.setStatus("current")
_AwcEventDispSeveritySystemInfo_Type = AwcEventDisposition
_AwcEventDispSeveritySystemInfo_Object = MibScalar
awcEventDispSeveritySystemInfo = _AwcEventDispSeveritySystemInfo_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 15, 14),
    _AwcEventDispSeveritySystemInfo_Type()
)
awcEventDispSeveritySystemInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventDispSeveritySystemInfo.setStatus("current")
_AwcEventDispSeverityProtocolInfo_Type = AwcEventDisposition
_AwcEventDispSeverityProtocolInfo_Object = MibScalar
awcEventDispSeverityProtocolInfo = _AwcEventDispSeverityProtocolInfo_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 15, 15),
    _AwcEventDispSeverityProtocolInfo_Type()
)
awcEventDispSeverityProtocolInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventDispSeverityProtocolInfo.setStatus("current")
_AwcEventDispSeverityPortInfo_Type = AwcEventDisposition
_AwcEventDispSeverityPortInfo_Object = MibScalar
awcEventDispSeverityPortInfo = _AwcEventDispSeverityPortInfo_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 15, 16),
    _AwcEventDispSeverityPortInfo_Type()
)
awcEventDispSeverityPortInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventDispSeverityPortInfo.setStatus("current")
_AwcEventDispSeverityExternalInfo_Type = AwcEventDisposition
_AwcEventDispSeverityExternalInfo_Object = MibScalar
awcEventDispSeverityExternalInfo = _AwcEventDispSeverityExternalInfo_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 15, 17),
    _AwcEventDispSeverityExternalInfo_Type()
)
awcEventDispSeverityExternalInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventDispSeverityExternalInfo.setStatus("current")


class _AwcEventSyslogAddr_Type(DisplayString):
    """Custom type awcEventSyslogAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AwcEventSyslogAddr_Type.__name__ = "DisplayString"
_AwcEventSyslogAddr_Object = MibScalar
awcEventSyslogAddr = _AwcEventSyslogAddr_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 16),
    _AwcEventSyslogAddr_Type()
)
awcEventSyslogAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventSyslogAddr.setStatus("current")


class _AwcEventSyslogFacility_Type(Integer32):
    """Custom type awcEventSyslogFacility based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_AwcEventSyslogFacility_Type.__name__ = "Integer32"
_AwcEventSyslogFacility_Object = MibScalar
awcEventSyslogFacility = _AwcEventSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 17),
    _AwcEventSyslogFacility_Type()
)
awcEventSyslogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventSyslogFacility.setStatus("current")


class _AwcEventTraceStationSeverity_Type(AwcEventSeverity):
    """Custom type awcEventTraceStationSeverity based on AwcEventSeverity"""


_AwcEventTraceStationSeverity_Object = MibScalar
awcEventTraceStationSeverity = _AwcEventTraceStationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 20),
    _AwcEventTraceStationSeverity_Type()
)
awcEventTraceStationSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventTraceStationSeverity.setStatus("current")


class _AwcEventTraceLogSize_Type(Unsigned32):
    """Custom type awcEventTraceLogSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8388608),
    )


_AwcEventTraceLogSize_Type.__name__ = "Unsigned32"
_AwcEventTraceLogSize_Object = MibScalar
awcEventTraceLogSize = _AwcEventTraceLogSize_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 21),
    _AwcEventTraceLogSize_Type()
)
awcEventTraceLogSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventTraceLogSize.setStatus("current")


class _AwcEventTracePacketLen_Type(Unsigned32):
    """Custom type awcEventTracePacketLen based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2312),
    )


_AwcEventTracePacketLen_Type.__name__ = "Unsigned32"
_AwcEventTracePacketLen_Object = MibScalar
awcEventTracePacketLen = _AwcEventTracePacketLen_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 22),
    _AwcEventTracePacketLen_Type()
)
awcEventTracePacketLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventTracePacketLen.setStatus("current")
_AwcEventTable_Object = MibTable
awcEventTable = _AwcEventTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 23)
)
if mibBuilder.loadTexts:
    awcEventTable.setStatus("current")
_AwcEventEntry_Object = MibTableRow
awcEventEntry = _AwcEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 23, 1)
)
awcEventEntry.setIndexNames(
    (0, "AWCVX-MIB", "awcEventID"),
)
if mibBuilder.loadTexts:
    awcEventEntry.setStatus("current")
_AwcEventID_Type = Unsigned32
_AwcEventID_Object = MibTableColumn
awcEventID = _AwcEventID_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 23, 1, 1),
    _AwcEventID_Type()
)
awcEventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcEventID.setStatus("current")
_AwcEventTime_Type = DisplayString
_AwcEventTime_Object = MibTableColumn
awcEventTime = _AwcEventTime_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 23, 1, 2),
    _AwcEventTime_Type()
)
awcEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcEventTime.setStatus("current")
_AwcEventSeverity_Type = AwcEventSeverity
_AwcEventSeverity_Object = MibTableColumn
awcEventSeverity = _AwcEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 23, 1, 3),
    _AwcEventSeverity_Type()
)
awcEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcEventSeverity.setStatus("current")
_AwcEventDescription_Type = DisplayString
_AwcEventDescription_Object = MibTableColumn
awcEventDescription = _AwcEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 23, 1, 4),
    _AwcEventDescription_Type()
)
awcEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcEventDescription.setStatus("current")
_AwcEventType_Type = DisplayString
_AwcEventType_Object = MibTableColumn
awcEventType = _AwcEventType_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 23, 1, 5),
    _AwcEventType_Type()
)
awcEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcEventType.setStatus("current")


class _AwcEventUseCiscoFormat_Type(TruthValue):
    """Custom type awcEventUseCiscoFormat based on TruthValue"""


_AwcEventUseCiscoFormat_Object = MibScalar
awcEventUseCiscoFormat = _AwcEventUseCiscoFormat_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 25),
    _AwcEventUseCiscoFormat_Type()
)
awcEventUseCiscoFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEventUseCiscoFormat.setStatus("current")


class _AwcDot11AuthenticateFailDisposition_Type(AwcDot11EventDisposition):
    """Custom type awcDot11AuthenticateFailDisposition based on AwcDot11EventDisposition"""


_AwcDot11AuthenticateFailDisposition_Object = MibScalar
awcDot11AuthenticateFailDisposition = _AwcDot11AuthenticateFailDisposition_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 26),
    _AwcDot11AuthenticateFailDisposition_Type()
)
awcDot11AuthenticateFailDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11AuthenticateFailDisposition.setStatus("current")


class _AwcDot11DeauthenticateDisposition_Type(AwcDot11EventDisposition):
    """Custom type awcDot11DeauthenticateDisposition based on AwcDot11EventDisposition"""


_AwcDot11DeauthenticateDisposition_Object = MibScalar
awcDot11DeauthenticateDisposition = _AwcDot11DeauthenticateDisposition_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 27),
    _AwcDot11DeauthenticateDisposition_Type()
)
awcDot11DeauthenticateDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11DeauthenticateDisposition.setStatus("current")


class _AwcDot11DisassociateDisposition_Type(AwcDot11EventDisposition):
    """Custom type awcDot11DisassociateDisposition based on AwcDot11EventDisposition"""


_AwcDot11DisassociateDisposition_Object = MibScalar
awcDot11DisassociateDisposition = _AwcDot11DisassociateDisposition_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 14, 28),
    _AwcDot11DisassociateDisposition_Type()
)
awcDot11DisassociateDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDot11DisassociateDisposition.setStatus("current")
_AwcEtherMIB_ObjectIdentity = ObjectIdentity
awcEtherMIB = _AwcEtherMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 15)
)


class _AwcEtherIfSpeedSelect_Type(Integer32):
    """Custom type awcEtherIfSpeedSelect based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("autoDetect", 8),
          ("oneHundredBaseT", 5),
          ("oneHundredBaseTfull", 7),
          ("tenBaseT", 3),
          ("tenBaseTfull", 6))
    )


_AwcEtherIfSpeedSelect_Type.__name__ = "Integer32"
_AwcEtherIfSpeedSelect_Object = MibScalar
awcEtherIfSpeedSelect = _AwcEtherIfSpeedSelect_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 15, 1),
    _AwcEtherIfSpeedSelect_Type()
)
awcEtherIfSpeedSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEtherIfSpeedSelect.setStatus("current")


class _AwcEtherDuplex_Type(Integer32):
    """Custom type awcEtherDuplex based on Integer32"""
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


_AwcEtherDuplex_Type.__name__ = "Integer32"
_AwcEtherDuplex_Object = MibScalar
awcEtherDuplex = _AwcEtherDuplex_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 15, 5),
    _AwcEtherDuplex_Type()
)
awcEtherDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcEtherDuplex.setStatus("current")
_AwcEtherCamSize_Type = Unsigned32
_AwcEtherCamSize_Object = MibScalar
awcEtherCamSize = _AwcEtherCamSize_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 15, 7),
    _AwcEtherCamSize_Type()
)
awcEtherCamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcEtherCamSize.setStatus("current")


class _AwcEtherEnableSwCam_Type(TruthValue):
    """Custom type awcEtherEnableSwCam based on TruthValue"""


_AwcEtherEnableSwCam_Object = MibScalar
awcEtherEnableSwCam = _AwcEtherEnableSwCam_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 15, 8),
    _AwcEtherEnableSwCam_Type()
)
awcEtherEnableSwCam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEtherEnableSwCam.setStatus("current")


class _AwcEtherForcePortUnblock_Type(TruthValue):
    """Custom type awcEtherForcePortUnblock based on TruthValue"""


_AwcEtherForcePortUnblock_Object = MibScalar
awcEtherForcePortUnblock = _AwcEtherForcePortUnblock_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 15, 9),
    _AwcEtherForcePortUnblock_Type()
)
awcEtherForcePortUnblock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEtherForcePortUnblock.setStatus("current")


class _AwcEtherLostEthernetSeconds_Type(Integer32):
    """Custom type awcEtherLostEthernetSeconds based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_AwcEtherLostEthernetSeconds_Type.__name__ = "Integer32"
_AwcEtherLostEthernetSeconds_Object = MibScalar
awcEtherLostEthernetSeconds = _AwcEtherLostEthernetSeconds_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 15, 10),
    _AwcEtherLostEthernetSeconds_Type()
)
awcEtherLostEthernetSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEtherLostEthernetSeconds.setStatus("current")


class _AwcEtherLostEthernetAction_Type(Integer32):
    """Custom type awcEtherLostEthernetAction based on Integer32"""
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
        *(("noAction", 1),
          ("radioOff", 3),
          ("restrictSSID", 4),
          ("switchRepeater", 2))
    )


_AwcEtherLostEthernetAction_Type.__name__ = "Integer32"
_AwcEtherLostEthernetAction_Object = MibScalar
awcEtherLostEthernetAction = _AwcEtherLostEthernetAction_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 15, 11),
    _AwcEtherLostEthernetAction_Type()
)
awcEtherLostEthernetAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEtherLostEthernetAction.setStatus("current")


class _AwcEtherLostEthernetSSID_Type(Unsigned32):
    """Custom type awcEtherLostEthernetSSID based on Unsigned32"""
    defaultValue = 0


_AwcEtherLostEthernetSSID_Object = MibScalar
awcEtherLostEthernetSSID = _AwcEtherLostEthernetSSID_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 15, 12),
    _AwcEtherLostEthernetSSID_Type()
)
awcEtherLostEthernetSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcEtherLostEthernetSSID.setStatus("current")
_AwcPolicyGroups_ObjectIdentity = ObjectIdentity
awcPolicyGroups = _AwcPolicyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 16)
)
_AwcPolGrpTable_Object = MibTable
awcPolGrpTable = _AwcPolGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 16, 1)
)
if mibBuilder.loadTexts:
    awcPolGrpTable.setStatus("current")
_AwcPolGrpEntry_Object = MibTableRow
awcPolGrpEntry = _AwcPolGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 16, 1, 1)
)
awcPolGrpEntry.setIndexNames(
    (0, "AWCVX-MIB", "awcPolGrpId"),
)
if mibBuilder.loadTexts:
    awcPolGrpEntry.setStatus("current")


class _AwcPolGrpId_Type(Unsigned32):
    """Custom type awcPolGrpId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_AwcPolGrpId_Type.__name__ = "Unsigned32"
_AwcPolGrpId_Object = MibTableColumn
awcPolGrpId = _AwcPolGrpId_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 16, 1, 1, 1),
    _AwcPolGrpId_Type()
)
awcPolGrpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    awcPolGrpId.setStatus("current")


class _AwcPolGrpName_Type(DisplayString):
    """Custom type awcPolGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AwcPolGrpName_Type.__name__ = "DisplayString"
_AwcPolGrpName_Object = MibTableColumn
awcPolGrpName = _AwcPolGrpName_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 16, 1, 1, 2),
    _AwcPolGrpName_Type()
)
awcPolGrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPolGrpName.setStatus("current")
_AwcPolGrpStatus_Type = RowStatus
_AwcPolGrpStatus_Object = MibTableColumn
awcPolGrpStatus = _AwcPolGrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 16, 1, 1, 3),
    _AwcPolGrpStatus_Type()
)
awcPolGrpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPolGrpStatus.setStatus("current")


class _AwcPolGrpInEthertypeFilterId_Type(Unsigned32):
    """Custom type awcPolGrpInEthertypeFilterId based on Unsigned32"""
    defaultValue = 0


_AwcPolGrpInEthertypeFilterId_Object = MibTableColumn
awcPolGrpInEthertypeFilterId = _AwcPolGrpInEthertypeFilterId_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 16, 1, 1, 4),
    _AwcPolGrpInEthertypeFilterId_Type()
)
awcPolGrpInEthertypeFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPolGrpInEthertypeFilterId.setStatus("current")


class _AwcPolGrpOutEthertypeFilterId_Type(Unsigned32):
    """Custom type awcPolGrpOutEthertypeFilterId based on Unsigned32"""
    defaultValue = 0


_AwcPolGrpOutEthertypeFilterId_Object = MibTableColumn
awcPolGrpOutEthertypeFilterId = _AwcPolGrpOutEthertypeFilterId_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 16, 1, 1, 5),
    _AwcPolGrpOutEthertypeFilterId_Type()
)
awcPolGrpOutEthertypeFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPolGrpOutEthertypeFilterId.setStatus("current")


class _AwcPolGrpInIpProtoFilterId_Type(Unsigned32):
    """Custom type awcPolGrpInIpProtoFilterId based on Unsigned32"""
    defaultValue = 0


_AwcPolGrpInIpProtoFilterId_Object = MibTableColumn
awcPolGrpInIpProtoFilterId = _AwcPolGrpInIpProtoFilterId_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 16, 1, 1, 6),
    _AwcPolGrpInIpProtoFilterId_Type()
)
awcPolGrpInIpProtoFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPolGrpInIpProtoFilterId.setStatus("current")


class _AwcPolGrpOutIpProtoFilterId_Type(Unsigned32):
    """Custom type awcPolGrpOutIpProtoFilterId based on Unsigned32"""
    defaultValue = 0


_AwcPolGrpOutIpProtoFilterId_Object = MibTableColumn
awcPolGrpOutIpProtoFilterId = _AwcPolGrpOutIpProtoFilterId_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 16, 1, 1, 7),
    _AwcPolGrpOutIpProtoFilterId_Type()
)
awcPolGrpOutIpProtoFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPolGrpOutIpProtoFilterId.setStatus("current")


class _AwcPolGrpInIpPortFilterId_Type(Unsigned32):
    """Custom type awcPolGrpInIpPortFilterId based on Unsigned32"""
    defaultValue = 0


_AwcPolGrpInIpPortFilterId_Object = MibTableColumn
awcPolGrpInIpPortFilterId = _AwcPolGrpInIpPortFilterId_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 16, 1, 1, 8),
    _AwcPolGrpInIpPortFilterId_Type()
)
awcPolGrpInIpPortFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPolGrpInIpPortFilterId.setStatus("current")


class _AwcPolGrpOutIpPortFilterId_Type(Unsigned32):
    """Custom type awcPolGrpOutIpPortFilterId based on Unsigned32"""
    defaultValue = 0


_AwcPolGrpOutIpPortFilterId_Object = MibTableColumn
awcPolGrpOutIpPortFilterId = _AwcPolGrpOutIpPortFilterId_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 16, 1, 1, 9),
    _AwcPolGrpOutIpPortFilterId_Type()
)
awcPolGrpOutIpPortFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPolGrpOutIpPortFilterId.setStatus("current")


class _AwcDscpToCosMapEnable_Type(TruthValue):
    """Custom type awcDscpToCosMapEnable based on TruthValue"""


_AwcDscpToCosMapEnable_Object = MibScalar
awcDscpToCosMapEnable = _AwcDscpToCosMapEnable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 16, 2),
    _AwcDscpToCosMapEnable_Type()
)
awcDscpToCosMapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDscpToCosMapEnable.setStatus("current")
_AwcDscpToCosMapTable_Object = MibTable
awcDscpToCosMapTable = _AwcDscpToCosMapTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 16, 3)
)
if mibBuilder.loadTexts:
    awcDscpToCosMapTable.setStatus("current")
_AwcDscpToCosMapEntry_Object = MibTableRow
awcDscpToCosMapEntry = _AwcDscpToCosMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 16, 3, 1)
)
awcDscpToCosMapEntry.setIndexNames(
    (0, "AWCVX-MIB", "awcDscpToCosMapDscp"),
)
if mibBuilder.loadTexts:
    awcDscpToCosMapEntry.setStatus("current")


class _AwcDscpToCosMapDscp_Type(Integer32):
    """Custom type awcDscpToCosMapDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AwcDscpToCosMapDscp_Type.__name__ = "Integer32"
_AwcDscpToCosMapDscp_Object = MibTableColumn
awcDscpToCosMapDscp = _AwcDscpToCosMapDscp_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 16, 3, 1, 1),
    _AwcDscpToCosMapDscp_Type()
)
awcDscpToCosMapDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    awcDscpToCosMapDscp.setStatus("current")


class _AwcDscpToCosMapCos_Type(Integer32):
    """Custom type awcDscpToCosMapCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_AwcDscpToCosMapCos_Type.__name__ = "Integer32"
_AwcDscpToCosMapCos_Object = MibTableColumn
awcDscpToCosMapCos = _AwcDscpToCosMapCos_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 16, 3, 1, 2),
    _AwcDscpToCosMapCos_Type()
)
awcDscpToCosMapCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcDscpToCosMapCos.setStatus("current")
_AwcDdpIAPP_ObjectIdentity = ObjectIdentity
awcDdpIAPP = _AwcDdpIAPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 17)
)


class _AwcIappMcastIpAddr_Type(IpAddress):
    """Custom type awcIappMcastIpAddr based on IpAddress"""
    defaultHexValue = "E0000128"


_AwcIappMcastIpAddr_Object = MibScalar
awcIappMcastIpAddr = _AwcIappMcastIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 17, 1),
    _AwcIappMcastIpAddr_Type()
)
awcIappMcastIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcIappMcastIpAddr.setStatus("current")


class _AwcIappPort_Type(Integer32):
    """Custom type awcIappPort based on Integer32"""
    defaultValue = 2887

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AwcIappPort_Type.__name__ = "Integer32"
_AwcIappPort_Object = MibScalar
awcIappPort = _AwcIappPort_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 17, 2),
    _AwcIappPort_Type()
)
awcIappPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcIappPort.setStatus("current")


class _AwcP802dot1XVersion_Type(Integer32):
    """Custom type awcP802dot1XVersion based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8,
              10)
        )
    )
    namedValues = NamedValues(
        *(("d10", 10),
          ("d7", 7),
          ("d8", 8))
    )


_AwcP802dot1XVersion_Type.__name__ = "Integer32"
_AwcP802dot1XVersion_Object = MibScalar
awcP802dot1XVersion = _AwcP802dot1XVersion_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 17, 100),
    _AwcP802dot1XVersion_Type()
)
awcP802dot1XVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcP802dot1XVersion.setStatus("current")
_AwcHotStandby_ObjectIdentity = ObjectIdentity
awcHotStandby = _AwcHotStandby_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 18)
)


class _AwcHotStandbyMACAddr_Type(MacAddress):
    """Custom type awcHotStandbyMACAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_AwcHotStandbyMACAddr_Object = MibScalar
awcHotStandbyMACAddr = _AwcHotStandbyMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 18, 1),
    _AwcHotStandbyMACAddr_Type()
)
awcHotStandbyMACAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcHotStandbyMACAddr.setStatus("current")


class _AwcHotStandbyPollingFrequency_Type(Integer32):
    """Custom type awcHotStandbyPollingFrequency based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AwcHotStandbyPollingFrequency_Type.__name__ = "Integer32"
_AwcHotStandbyPollingFrequency_Object = MibScalar
awcHotStandbyPollingFrequency = _AwcHotStandbyPollingFrequency_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 18, 2),
    _AwcHotStandbyPollingFrequency_Type()
)
awcHotStandbyPollingFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcHotStandbyPollingFrequency.setStatus("current")
if mibBuilder.loadTexts:
    awcHotStandbyPollingFrequency.setUnits("seconds")


class _AwcHotStandbyPollingTimeOut_Type(Integer32):
    """Custom type awcHotStandbyPollingTimeOut based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_AwcHotStandbyPollingTimeOut_Type.__name__ = "Integer32"
_AwcHotStandbyPollingTimeOut_Object = MibScalar
awcHotStandbyPollingTimeOut = _AwcHotStandbyPollingTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 18, 3),
    _AwcHotStandbyPollingTimeOut_Type()
)
awcHotStandbyPollingTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcHotStandbyPollingTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    awcHotStandbyPollingTimeOut.setUnits("seconds")


class _AwcHotStandbyInHotStandby_Type(TruthValue):
    """Custom type awcHotStandbyInHotStandby based on TruthValue"""


_AwcHotStandbyInHotStandby_Object = MibScalar
awcHotStandbyInHotStandby = _AwcHotStandbyInHotStandby_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 18, 4),
    _AwcHotStandbyInHotStandby_Type()
)
awcHotStandbyInHotStandby.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcHotStandbyInHotStandby.setStatus("current")
_AwcHotStandbyState_Type = AwcHotStandbyState
_AwcHotStandbyState_Object = MibScalar
awcHotStandbyState = _AwcHotStandbyState_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 18, 5),
    _AwcHotStandbyState_Type()
)
awcHotStandbyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcHotStandbyState.setStatus("current")
_AwcHotStandbyStatus_Type = AwcHotStandbyStatus
_AwcHotStandbyStatus_Object = MibScalar
awcHotStandbyStatus = _AwcHotStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 18, 6),
    _AwcHotStandbyStatus_Type()
)
awcHotStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcHotStandbyStatus.setStatus("current")
_AwcAaa_ObjectIdentity = ObjectIdentity
awcAaa = _AwcAaa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 19)
)
_AwcAaaServerTable_Object = MibTable
awcAaaServerTable = _AwcAaaServerTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 1)
)
if mibBuilder.loadTexts:
    awcAaaServerTable.setStatus("current")
_AwcAaaServerEntry_Object = MibTableRow
awcAaaServerEntry = _AwcAaaServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 1, 1)
)
awcAaaServerEntry.setIndexNames(
    (0, "AWCVX-MIB", "awcAaaServerPriority"),
)
if mibBuilder.loadTexts:
    awcAaaServerEntry.setStatus("current")


class _AwcAaaServerPriority_Type(Integer32):
    """Custom type awcAaaServerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AwcAaaServerPriority_Type.__name__ = "Integer32"
_AwcAaaServerPriority_Object = MibTableColumn
awcAaaServerPriority = _AwcAaaServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 1, 1, 1),
    _AwcAaaServerPriority_Type()
)
awcAaaServerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcAaaServerPriority.setStatus("current")


class _AwcAaaServerProtocol_Type(Integer32):
    """Custom type awcAaaServerProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("radius", 1),
          ("tacacsPlus", 2))
    )


_AwcAaaServerProtocol_Type.__name__ = "Integer32"
_AwcAaaServerProtocol_Object = MibTableColumn
awcAaaServerProtocol = _AwcAaaServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 1, 1, 2),
    _AwcAaaServerProtocol_Type()
)
awcAaaServerProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcAaaServerProtocol.setStatus("current")
_AwcAaaServerName_Type = DisplayString
_AwcAaaServerName_Object = MibTableColumn
awcAaaServerName = _AwcAaaServerName_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 1, 1, 3),
    _AwcAaaServerName_Type()
)
awcAaaServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcAaaServerName.setStatus("current")
_AwcAaaServerPort_Type = Unsigned32
_AwcAaaServerPort_Object = MibTableColumn
awcAaaServerPort = _AwcAaaServerPort_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 1, 1, 4),
    _AwcAaaServerPort_Type()
)
awcAaaServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcAaaServerPort.setStatus("current")
_AwcAaaServerTimeout_Type = Unsigned32
_AwcAaaServerTimeout_Object = MibTableColumn
awcAaaServerTimeout = _AwcAaaServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 1, 1, 5),
    _AwcAaaServerTimeout_Type()
)
awcAaaServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcAaaServerTimeout.setStatus("current")
_AwcAaaClientName_Type = DisplayString
_AwcAaaClientName_Object = MibTableColumn
awcAaaClientName = _AwcAaaClientName_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 1, 1, 6),
    _AwcAaaClientName_Type()
)
awcAaaClientName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcAaaClientName.setStatus("current")
_AwcAaaServerSharedSecret_Type = DisplayString
_AwcAaaServerSharedSecret_Object = MibTableColumn
awcAaaServerSharedSecret = _AwcAaaServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 1, 1, 7),
    _AwcAaaServerSharedSecret_Type()
)
awcAaaServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcAaaServerSharedSecret.setStatus("current")
_AwcAaaServer8021xCapabilityEnabled_Type = TruthValue
_AwcAaaServer8021xCapabilityEnabled_Object = MibTableColumn
awcAaaServer8021xCapabilityEnabled = _AwcAaaServer8021xCapabilityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 1, 1, 8),
    _AwcAaaServer8021xCapabilityEnabled_Type()
)
awcAaaServer8021xCapabilityEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcAaaServer8021xCapabilityEnabled.setStatus("current")
_AwcAaaServerMacAddrAuthEnabled_Type = TruthValue
_AwcAaaServerMacAddrAuthEnabled_Object = MibTableColumn
awcAaaServerMacAddrAuthEnabled = _AwcAaaServerMacAddrAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 1, 1, 9),
    _AwcAaaServerMacAddrAuthEnabled_Type()
)
awcAaaServerMacAddrAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcAaaServerMacAddrAuthEnabled.setStatus("current")
_AwcAaaServerAdminAuthEnabled_Type = TruthValue
_AwcAaaServerAdminAuthEnabled_Object = MibTableColumn
awcAaaServerAdminAuthEnabled = _AwcAaaServerAdminAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 1, 1, 10),
    _AwcAaaServerAdminAuthEnabled_Type()
)
awcAaaServerAdminAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcAaaServerAdminAuthEnabled.setStatus("current")
_AwcAaaServerMipAuthEnabled_Type = TruthValue
_AwcAaaServerMipAuthEnabled_Object = MibTableColumn
awcAaaServerMipAuthEnabled = _AwcAaaServerMipAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 1, 1, 11),
    _AwcAaaServerMipAuthEnabled_Type()
)
awcAaaServerMipAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcAaaServerMipAuthEnabled.setStatus("current")
_AwcAaaServerMaxRetransmission_Type = Unsigned32
_AwcAaaServerMaxRetransmission_Object = MibTableColumn
awcAaaServerMaxRetransmission = _AwcAaaServerMaxRetransmission_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 1, 1, 12),
    _AwcAaaServerMaxRetransmission_Type()
)
awcAaaServerMaxRetransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcAaaServerMaxRetransmission.setStatus("current")
_AwcAcctServerTable_Object = MibTable
awcAcctServerTable = _AwcAcctServerTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 2)
)
if mibBuilder.loadTexts:
    awcAcctServerTable.setStatus("current")
_AwcAcctServerEntry_Object = MibTableRow
awcAcctServerEntry = _AwcAcctServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 2, 1)
)
awcAcctServerEntry.setIndexNames(
    (0, "AWCVX-MIB", "awcAcctServerPriority"),
)
if mibBuilder.loadTexts:
    awcAcctServerEntry.setStatus("current")


class _AwcAcctServerPriority_Type(Integer32):
    """Custom type awcAcctServerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AwcAcctServerPriority_Type.__name__ = "Integer32"
_AwcAcctServerPriority_Object = MibTableColumn
awcAcctServerPriority = _AwcAcctServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 2, 1, 1),
    _AwcAcctServerPriority_Type()
)
awcAcctServerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcAcctServerPriority.setStatus("current")


class _AwcAcctServerProtocol_Type(Integer32):
    """Custom type awcAcctServerProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("radius", 1),
          ("tacacsPlus", 2))
    )


_AwcAcctServerProtocol_Type.__name__ = "Integer32"
_AwcAcctServerProtocol_Object = MibTableColumn
awcAcctServerProtocol = _AwcAcctServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 2, 1, 2),
    _AwcAcctServerProtocol_Type()
)
awcAcctServerProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcAcctServerProtocol.setStatus("current")
_AwcAcctServerName_Type = DisplayString
_AwcAcctServerName_Object = MibTableColumn
awcAcctServerName = _AwcAcctServerName_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 2, 1, 3),
    _AwcAcctServerName_Type()
)
awcAcctServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcAcctServerName.setStatus("current")
_AwcAcctServerPort_Type = Unsigned32
_AwcAcctServerPort_Object = MibTableColumn
awcAcctServerPort = _AwcAcctServerPort_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 2, 1, 4),
    _AwcAcctServerPort_Type()
)
awcAcctServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcAcctServerPort.setStatus("current")
_AwcAcctServerTimeout_Type = Unsigned32
_AwcAcctServerTimeout_Object = MibTableColumn
awcAcctServerTimeout = _AwcAcctServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 2, 1, 5),
    _AwcAcctServerTimeout_Type()
)
awcAcctServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcAcctServerTimeout.setStatus("current")
_AwcAcctServerUpdateEnable_Type = TruthValue
_AwcAcctServerUpdateEnable_Object = MibTableColumn
awcAcctServerUpdateEnable = _AwcAcctServerUpdateEnable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 2, 1, 6),
    _AwcAcctServerUpdateEnable_Type()
)
awcAcctServerUpdateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcAcctServerUpdateEnable.setStatus("current")


class _AwcAcctServerUpdateDelay_Type(Unsigned32):
    """Custom type awcAcctServerUpdateDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 2592000),
    )


_AwcAcctServerUpdateDelay_Type.__name__ = "Unsigned32"
_AwcAcctServerUpdateDelay_Object = MibTableColumn
awcAcctServerUpdateDelay = _AwcAcctServerUpdateDelay_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 2, 1, 7),
    _AwcAcctServerUpdateDelay_Type()
)
awcAcctServerUpdateDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcAcctServerUpdateDelay.setStatus("current")
_AwcAcctClientName_Type = DisplayString
_AwcAcctClientName_Object = MibTableColumn
awcAcctClientName = _AwcAcctClientName_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 2, 1, 8),
    _AwcAcctClientName_Type()
)
awcAcctClientName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcAcctClientName.setStatus("current")
_AwcAcctSecureEnabled_Type = TruthValue
_AwcAcctSecureEnabled_Object = MibTableColumn
awcAcctSecureEnabled = _AwcAcctSecureEnabled_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 2, 1, 9),
    _AwcAcctSecureEnabled_Type()
)
awcAcctSecureEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcAcctSecureEnabled.setStatus("current")
_AwcAcctGeneralEnabled_Type = TruthValue
_AwcAcctGeneralEnabled_Object = MibTableColumn
awcAcctGeneralEnabled = _AwcAcctGeneralEnabled_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 2, 1, 10),
    _AwcAcctGeneralEnabled_Type()
)
awcAcctGeneralEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcAcctGeneralEnabled.setStatus("current")
_AwcAcctServerSharedSecret_Type = DisplayString
_AwcAcctServerSharedSecret_Object = MibTableColumn
awcAcctServerSharedSecret = _AwcAcctServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 2, 1, 11),
    _AwcAcctServerSharedSecret_Type()
)
awcAcctServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcAcctServerSharedSecret.setStatus("current")
_AwcAcctServerMaxRetransmission_Type = Unsigned32
_AwcAcctServerMaxRetransmission_Object = MibTableColumn
awcAcctServerMaxRetransmission = _AwcAcctServerMaxRetransmission_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 2, 1, 12),
    _AwcAcctServerMaxRetransmission_Type()
)
awcAcctServerMaxRetransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcAcctServerMaxRetransmission.setStatus("current")
_AwcAcctConfig_ObjectIdentity = ObjectIdentity
awcAcctConfig = _AwcAcctConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 3)
)


class _AwcAcctEnable_Type(TruthValue):
    """Custom type awcAcctEnable based on TruthValue"""


_AwcAcctEnable_Object = MibScalar
awcAcctEnable = _AwcAcctEnable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 3, 1),
    _AwcAcctEnable_Type()
)
awcAcctEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcAcctEnable.setStatus("current")


class _AwcAcctStopDelayEnable_Type(TruthValue):
    """Custom type awcAcctStopDelayEnable based on TruthValue"""


_AwcAcctStopDelayEnable_Object = MibScalar
awcAcctStopDelayEnable = _AwcAcctStopDelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 3, 2),
    _AwcAcctStopDelayEnable_Type()
)
awcAcctStopDelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcAcctStopDelayEnable.setStatus("current")


class _AwcAcctStopDelayTime_Type(Unsigned32):
    """Custom type awcAcctStopDelayTime based on Unsigned32"""
    defaultValue = 2


_AwcAcctStopDelayTime_Object = MibScalar
awcAcctStopDelayTime = _AwcAcctStopDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 3, 3),
    _AwcAcctStopDelayTime_Type()
)
awcAcctStopDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcAcctStopDelayTime.setStatus("current")
_AwcAaaAuthConfig_ObjectIdentity = ObjectIdentity
awcAaaAuthConfig = _AwcAaaAuthConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 4)
)
_AwcAaaServerPrimaryReattemptPeriod_Type = Unsigned32
_AwcAaaServerPrimaryReattemptPeriod_Object = MibScalar
awcAaaServerPrimaryReattemptPeriod = _AwcAaaServerPrimaryReattemptPeriod_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 4, 1),
    _AwcAaaServerPrimaryReattemptPeriod_Type()
)
awcAaaServerPrimaryReattemptPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcAaaServerPrimaryReattemptPeriod.setStatus("current")


class _AwcAaaServerDot1xAuthCurrent_Type(Integer32):
    """Custom type awcAaaServerDot1xAuthCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AwcAaaServerDot1xAuthCurrent_Type.__name__ = "Integer32"
_AwcAaaServerDot1xAuthCurrent_Object = MibScalar
awcAaaServerDot1xAuthCurrent = _AwcAaaServerDot1xAuthCurrent_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 4, 2),
    _AwcAaaServerDot1xAuthCurrent_Type()
)
awcAaaServerDot1xAuthCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcAaaServerDot1xAuthCurrent.setStatus("current")


class _AwcAaaServerMacAddrAuthCurrent_Type(Integer32):
    """Custom type awcAaaServerMacAddrAuthCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AwcAaaServerMacAddrAuthCurrent_Type.__name__ = "Integer32"
_AwcAaaServerMacAddrAuthCurrent_Object = MibScalar
awcAaaServerMacAddrAuthCurrent = _AwcAaaServerMacAddrAuthCurrent_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 4, 3),
    _AwcAaaServerMacAddrAuthCurrent_Type()
)
awcAaaServerMacAddrAuthCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcAaaServerMacAddrAuthCurrent.setStatus("current")


class _AwcAaaServerAdminAuthCurrent_Type(Integer32):
    """Custom type awcAaaServerAdminAuthCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AwcAaaServerAdminAuthCurrent_Type.__name__ = "Integer32"
_AwcAaaServerAdminAuthCurrent_Object = MibScalar
awcAaaServerAdminAuthCurrent = _AwcAaaServerAdminAuthCurrent_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 4, 4),
    _AwcAaaServerAdminAuthCurrent_Type()
)
awcAaaServerAdminAuthCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcAaaServerAdminAuthCurrent.setStatus("current")


class _AwcAaaServerMipAuthCurrent_Type(Integer32):
    """Custom type awcAaaServerMipAuthCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AwcAaaServerMipAuthCurrent_Type.__name__ = "Integer32"
_AwcAaaServerMipAuthCurrent_Object = MibScalar
awcAaaServerMipAuthCurrent = _AwcAaaServerMipAuthCurrent_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 19, 4, 5),
    _AwcAaaServerMipAuthCurrent_Type()
)
awcAaaServerMipAuthCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcAaaServerMipAuthCurrent.setStatus("current")
_AwcProtocolFilters_ObjectIdentity = ObjectIdentity
awcProtocolFilters = _AwcProtocolFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 20)
)
_AwcPrFltEthertypeSetTable_Object = MibTable
awcPrFltEthertypeSetTable = _AwcPrFltEthertypeSetTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 1)
)
if mibBuilder.loadTexts:
    awcPrFltEthertypeSetTable.setStatus("current")
_AwcPrFltEthertypeSetEntry_Object = MibTableRow
awcPrFltEthertypeSetEntry = _AwcPrFltEthertypeSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 1, 1)
)
awcPrFltEthertypeSetEntry.setIndexNames(
    (0, "AWCVX-MIB", "awcPfEtSetId"),
)
if mibBuilder.loadTexts:
    awcPrFltEthertypeSetEntry.setStatus("current")
_AwcPfEtSetId_Type = Unsigned32
_AwcPfEtSetId_Object = MibTableColumn
awcPfEtSetId = _AwcPfEtSetId_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 1, 1, 1),
    _AwcPfEtSetId_Type()
)
awcPfEtSetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcPfEtSetId.setStatus("current")


class _AwcPfEtSetName_Type(DisplayString):
    """Custom type awcPfEtSetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AwcPfEtSetName_Type.__name__ = "DisplayString"
_AwcPfEtSetName_Object = MibTableColumn
awcPfEtSetName = _AwcPfEtSetName_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 1, 1, 2),
    _AwcPfEtSetName_Type()
)
awcPfEtSetName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfEtSetName.setStatus("current")


class _AwcPfEtDefaultDisposition_Type(AwcPfDisposition):
    """Custom type awcPfEtDefaultDisposition based on AwcPfDisposition"""


_AwcPfEtDefaultDisposition_Object = MibTableColumn
awcPfEtDefaultDisposition = _AwcPfEtDefaultDisposition_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 1, 1, 3),
    _AwcPfEtDefaultDisposition_Type()
)
awcPfEtDefaultDisposition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfEtDefaultDisposition.setStatus("current")


class _AwcPfEtDefaultUcastTimeToLive_Type(Unsigned32):
    """Custom type awcPfEtDefaultUcastTimeToLive based on Unsigned32"""
    defaultValue = 0


_AwcPfEtDefaultUcastTimeToLive_Object = MibTableColumn
awcPfEtDefaultUcastTimeToLive = _AwcPfEtDefaultUcastTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 1, 1, 4),
    _AwcPfEtDefaultUcastTimeToLive_Type()
)
awcPfEtDefaultUcastTimeToLive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfEtDefaultUcastTimeToLive.setStatus("current")


class _AwcPfEtDefaultNUcastTimeToLive_Type(Unsigned32):
    """Custom type awcPfEtDefaultNUcastTimeToLive based on Unsigned32"""
    defaultValue = 0


_AwcPfEtDefaultNUcastTimeToLive_Object = MibTableColumn
awcPfEtDefaultNUcastTimeToLive = _AwcPfEtDefaultNUcastTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 1, 1, 5),
    _AwcPfEtDefaultNUcastTimeToLive_Type()
)
awcPfEtDefaultNUcastTimeToLive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfEtDefaultNUcastTimeToLive.setStatus("current")
_AwcPfEtSetStatus_Type = RowStatus
_AwcPfEtSetStatus_Object = MibTableColumn
awcPfEtSetStatus = _AwcPfEtSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 1, 1, 6),
    _AwcPfEtSetStatus_Type()
)
awcPfEtSetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfEtSetStatus.setStatus("current")
_AwcPrFltEthertypeTable_Object = MibTable
awcPrFltEthertypeTable = _AwcPrFltEthertypeTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 2)
)
if mibBuilder.loadTexts:
    awcPrFltEthertypeTable.setStatus("current")
_AwcPrFltEthertypeEntry_Object = MibTableRow
awcPrFltEthertypeEntry = _AwcPrFltEthertypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 2, 1)
)
awcPrFltEthertypeEntry.setIndexNames(
    (0, "AWCVX-MIB", "awcPfEtSetId"),
    (0, "AWCVX-MIB", "awcPfEtEthertype"),
)
if mibBuilder.loadTexts:
    awcPrFltEthertypeEntry.setStatus("current")


class _AwcPfEtEthertype_Type(Integer32):
    """Custom type awcPfEtEthertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
        ValueRangeConstraint(1501, 65535),
    )


_AwcPfEtEthertype_Type.__name__ = "Integer32"
_AwcPfEtEthertype_Object = MibTableColumn
awcPfEtEthertype = _AwcPfEtEthertype_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 2, 1, 1),
    _AwcPfEtEthertype_Type()
)
awcPfEtEthertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcPfEtEthertype.setStatus("current")


class _AwcPfEtDisposition_Type(AwcPfDisposition):
    """Custom type awcPfEtDisposition based on AwcPfDisposition"""


_AwcPfEtDisposition_Object = MibTableColumn
awcPfEtDisposition = _AwcPfEtDisposition_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 2, 1, 2),
    _AwcPfEtDisposition_Type()
)
awcPfEtDisposition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfEtDisposition.setStatus("current")


class _AwcPfEtUserPriority_Type(AwcPfPriority):
    """Custom type awcPfEtUserPriority based on AwcPfPriority"""


_AwcPfEtUserPriority_Object = MibTableColumn
awcPfEtUserPriority = _AwcPfEtUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 2, 1, 3),
    _AwcPfEtUserPriority_Type()
)
awcPfEtUserPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfEtUserPriority.setStatus("current")


class _AwcPfEtUcastTimeToLive_Type(Unsigned32):
    """Custom type awcPfEtUcastTimeToLive based on Unsigned32"""
    defaultValue = 0


_AwcPfEtUcastTimeToLive_Object = MibTableColumn
awcPfEtUcastTimeToLive = _AwcPfEtUcastTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 2, 1, 4),
    _AwcPfEtUcastTimeToLive_Type()
)
awcPfEtUcastTimeToLive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfEtUcastTimeToLive.setStatus("current")


class _AwcPfEtNUcastTimeToLive_Type(Unsigned32):
    """Custom type awcPfEtNUcastTimeToLive based on Unsigned32"""
    defaultValue = 0


_AwcPfEtNUcastTimeToLive_Object = MibTableColumn
awcPfEtNUcastTimeToLive = _AwcPfEtNUcastTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 2, 1, 5),
    _AwcPfEtNUcastTimeToLive_Type()
)
awcPfEtNUcastTimeToLive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfEtNUcastTimeToLive.setStatus("current")


class _AwcPfEtAlert_Type(TruthValue):
    """Custom type awcPfEtAlert based on TruthValue"""


_AwcPfEtAlert_Object = MibTableColumn
awcPfEtAlert = _AwcPfEtAlert_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 2, 1, 6),
    _AwcPfEtAlert_Type()
)
awcPfEtAlert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfEtAlert.setStatus("current")
_AwcPfEtStatus_Type = RowStatus
_AwcPfEtStatus_Object = MibTableColumn
awcPfEtStatus = _AwcPfEtStatus_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 2, 1, 7),
    _AwcPfEtStatus_Type()
)
awcPfEtStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfEtStatus.setStatus("current")
_AwcPrFltIpProtocolSetTable_Object = MibTable
awcPrFltIpProtocolSetTable = _AwcPrFltIpProtocolSetTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 3)
)
if mibBuilder.loadTexts:
    awcPrFltIpProtocolSetTable.setStatus("current")
_AwcPrFltIpProtocolSetEntry_Object = MibTableRow
awcPrFltIpProtocolSetEntry = _AwcPrFltIpProtocolSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 3, 1)
)
awcPrFltIpProtocolSetEntry.setIndexNames(
    (0, "AWCVX-MIB", "awcPfIppSetId"),
)
if mibBuilder.loadTexts:
    awcPrFltIpProtocolSetEntry.setStatus("current")
_AwcPfIppSetId_Type = Unsigned32
_AwcPfIppSetId_Object = MibTableColumn
awcPfIppSetId = _AwcPfIppSetId_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 3, 1, 1),
    _AwcPfIppSetId_Type()
)
awcPfIppSetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcPfIppSetId.setStatus("current")


class _AwcPfIppSetName_Type(DisplayString):
    """Custom type awcPfIppSetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AwcPfIppSetName_Type.__name__ = "DisplayString"
_AwcPfIppSetName_Object = MibTableColumn
awcPfIppSetName = _AwcPfIppSetName_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 3, 1, 2),
    _AwcPfIppSetName_Type()
)
awcPfIppSetName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfIppSetName.setStatus("current")


class _AwcPfIppDefaultDisposition_Type(AwcPfDisposition):
    """Custom type awcPfIppDefaultDisposition based on AwcPfDisposition"""


_AwcPfIppDefaultDisposition_Object = MibTableColumn
awcPfIppDefaultDisposition = _AwcPfIppDefaultDisposition_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 3, 1, 3),
    _AwcPfIppDefaultDisposition_Type()
)
awcPfIppDefaultDisposition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfIppDefaultDisposition.setStatus("current")


class _AwcPfIppDefaultUcastTimeToLive_Type(Unsigned32):
    """Custom type awcPfIppDefaultUcastTimeToLive based on Unsigned32"""
    defaultValue = 0


_AwcPfIppDefaultUcastTimeToLive_Object = MibTableColumn
awcPfIppDefaultUcastTimeToLive = _AwcPfIppDefaultUcastTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 3, 1, 4),
    _AwcPfIppDefaultUcastTimeToLive_Type()
)
awcPfIppDefaultUcastTimeToLive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfIppDefaultUcastTimeToLive.setStatus("current")


class _AwcPfIppDefaultNUcastTimeToLive_Type(Unsigned32):
    """Custom type awcPfIppDefaultNUcastTimeToLive based on Unsigned32"""
    defaultValue = 0


_AwcPfIppDefaultNUcastTimeToLive_Object = MibTableColumn
awcPfIppDefaultNUcastTimeToLive = _AwcPfIppDefaultNUcastTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 3, 1, 5),
    _AwcPfIppDefaultNUcastTimeToLive_Type()
)
awcPfIppDefaultNUcastTimeToLive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfIppDefaultNUcastTimeToLive.setStatus("current")
_AwcPfIppSetStatus_Type = RowStatus
_AwcPfIppSetStatus_Object = MibTableColumn
awcPfIppSetStatus = _AwcPfIppSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 3, 1, 6),
    _AwcPfIppSetStatus_Type()
)
awcPfIppSetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfIppSetStatus.setStatus("current")
_AwcPrFltIpProtocolTable_Object = MibTable
awcPrFltIpProtocolTable = _AwcPrFltIpProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 4)
)
if mibBuilder.loadTexts:
    awcPrFltIpProtocolTable.setStatus("current")
_AwcPrFltIpProtocolEntry_Object = MibTableRow
awcPrFltIpProtocolEntry = _AwcPrFltIpProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 4, 1)
)
awcPrFltIpProtocolEntry.setIndexNames(
    (0, "AWCVX-MIB", "awcPfIppSetId"),
    (0, "AWCVX-MIB", "awcPfIppIpProtocol"),
)
if mibBuilder.loadTexts:
    awcPrFltIpProtocolEntry.setStatus("current")


class _AwcPfIppIpProtocol_Type(Integer32):
    """Custom type awcPfIppIpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AwcPfIppIpProtocol_Type.__name__ = "Integer32"
_AwcPfIppIpProtocol_Object = MibTableColumn
awcPfIppIpProtocol = _AwcPfIppIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 4, 1, 1),
    _AwcPfIppIpProtocol_Type()
)
awcPfIppIpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcPfIppIpProtocol.setStatus("current")


class _AwcPfIppDisposition_Type(AwcPfDisposition):
    """Custom type awcPfIppDisposition based on AwcPfDisposition"""


_AwcPfIppDisposition_Object = MibTableColumn
awcPfIppDisposition = _AwcPfIppDisposition_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 4, 1, 2),
    _AwcPfIppDisposition_Type()
)
awcPfIppDisposition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfIppDisposition.setStatus("current")


class _AwcPfIppUserPriority_Type(AwcPfPriority):
    """Custom type awcPfIppUserPriority based on AwcPfPriority"""


_AwcPfIppUserPriority_Object = MibTableColumn
awcPfIppUserPriority = _AwcPfIppUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 4, 1, 3),
    _AwcPfIppUserPriority_Type()
)
awcPfIppUserPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfIppUserPriority.setStatus("current")


class _AwcPfIppUcastTimeToLive_Type(Unsigned32):
    """Custom type awcPfIppUcastTimeToLive based on Unsigned32"""
    defaultValue = 0


_AwcPfIppUcastTimeToLive_Object = MibTableColumn
awcPfIppUcastTimeToLive = _AwcPfIppUcastTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 4, 1, 4),
    _AwcPfIppUcastTimeToLive_Type()
)
awcPfIppUcastTimeToLive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfIppUcastTimeToLive.setStatus("current")


class _AwcPfIppNUcastTimeToLive_Type(Unsigned32):
    """Custom type awcPfIppNUcastTimeToLive based on Unsigned32"""
    defaultValue = 0


_AwcPfIppNUcastTimeToLive_Object = MibTableColumn
awcPfIppNUcastTimeToLive = _AwcPfIppNUcastTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 4, 1, 5),
    _AwcPfIppNUcastTimeToLive_Type()
)
awcPfIppNUcastTimeToLive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfIppNUcastTimeToLive.setStatus("current")


class _AwcPfIppAlert_Type(TruthValue):
    """Custom type awcPfIppAlert based on TruthValue"""


_AwcPfIppAlert_Object = MibTableColumn
awcPfIppAlert = _AwcPfIppAlert_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 4, 1, 6),
    _AwcPfIppAlert_Type()
)
awcPfIppAlert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfIppAlert.setStatus("current")
_AwcPfIppStatus_Type = RowStatus
_AwcPfIppStatus_Object = MibTableColumn
awcPfIppStatus = _AwcPfIppStatus_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 4, 1, 7),
    _AwcPfIppStatus_Type()
)
awcPfIppStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfIppStatus.setStatus("current")
_AwcPrFltIpPortSetTable_Object = MibTable
awcPrFltIpPortSetTable = _AwcPrFltIpPortSetTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 5)
)
if mibBuilder.loadTexts:
    awcPrFltIpPortSetTable.setStatus("current")
_AwcPrFltIpPortSetEntry_Object = MibTableRow
awcPrFltIpPortSetEntry = _AwcPrFltIpPortSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 5, 1)
)
awcPrFltIpPortSetEntry.setIndexNames(
    (0, "AWCVX-MIB", "awcPfIptSetId"),
)
if mibBuilder.loadTexts:
    awcPrFltIpPortSetEntry.setStatus("current")
_AwcPfIptSetId_Type = Unsigned32
_AwcPfIptSetId_Object = MibTableColumn
awcPfIptSetId = _AwcPfIptSetId_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 5, 1, 1),
    _AwcPfIptSetId_Type()
)
awcPfIptSetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcPfIptSetId.setStatus("current")


class _AwcPfIptSetName_Type(DisplayString):
    """Custom type awcPfIptSetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AwcPfIptSetName_Type.__name__ = "DisplayString"
_AwcPfIptSetName_Object = MibTableColumn
awcPfIptSetName = _AwcPfIptSetName_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 5, 1, 2),
    _AwcPfIptSetName_Type()
)
awcPfIptSetName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfIptSetName.setStatus("current")


class _AwcPfIptDefaultDisposition_Type(AwcPfDisposition):
    """Custom type awcPfIptDefaultDisposition based on AwcPfDisposition"""


_AwcPfIptDefaultDisposition_Object = MibTableColumn
awcPfIptDefaultDisposition = _AwcPfIptDefaultDisposition_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 5, 1, 3),
    _AwcPfIptDefaultDisposition_Type()
)
awcPfIptDefaultDisposition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfIptDefaultDisposition.setStatus("current")


class _AwcPfIptDefaultUcastTimeToLive_Type(Unsigned32):
    """Custom type awcPfIptDefaultUcastTimeToLive based on Unsigned32"""
    defaultValue = 0


_AwcPfIptDefaultUcastTimeToLive_Object = MibTableColumn
awcPfIptDefaultUcastTimeToLive = _AwcPfIptDefaultUcastTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 5, 1, 4),
    _AwcPfIptDefaultUcastTimeToLive_Type()
)
awcPfIptDefaultUcastTimeToLive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfIptDefaultUcastTimeToLive.setStatus("current")


class _AwcPfIptDefaultNUcastTimeToLive_Type(Unsigned32):
    """Custom type awcPfIptDefaultNUcastTimeToLive based on Unsigned32"""
    defaultValue = 0


_AwcPfIptDefaultNUcastTimeToLive_Object = MibTableColumn
awcPfIptDefaultNUcastTimeToLive = _AwcPfIptDefaultNUcastTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 5, 1, 5),
    _AwcPfIptDefaultNUcastTimeToLive_Type()
)
awcPfIptDefaultNUcastTimeToLive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfIptDefaultNUcastTimeToLive.setStatus("current")
_AwcPfIptSetStatus_Type = RowStatus
_AwcPfIptSetStatus_Object = MibTableColumn
awcPfIptSetStatus = _AwcPfIptSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 5, 1, 6),
    _AwcPfIptSetStatus_Type()
)
awcPfIptSetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfIptSetStatus.setStatus("current")
_AwcPrFltIpPortTable_Object = MibTable
awcPrFltIpPortTable = _AwcPrFltIpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 6)
)
if mibBuilder.loadTexts:
    awcPrFltIpPortTable.setStatus("current")
_AwcPrFltIpPortEntry_Object = MibTableRow
awcPrFltIpPortEntry = _AwcPrFltIpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 6, 1)
)
awcPrFltIpPortEntry.setIndexNames(
    (0, "AWCVX-MIB", "awcPfIptSetId"),
    (0, "AWCVX-MIB", "awcPfIptIpPort"),
)
if mibBuilder.loadTexts:
    awcPrFltIpPortEntry.setStatus("current")


class _AwcPfIptIpPort_Type(Integer32):
    """Custom type awcPfIptIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AwcPfIptIpPort_Type.__name__ = "Integer32"
_AwcPfIptIpPort_Object = MibTableColumn
awcPfIptIpPort = _AwcPfIptIpPort_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 6, 1, 1),
    _AwcPfIptIpPort_Type()
)
awcPfIptIpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcPfIptIpPort.setStatus("current")


class _AwcPfIptDisposition_Type(AwcPfDisposition):
    """Custom type awcPfIptDisposition based on AwcPfDisposition"""


_AwcPfIptDisposition_Object = MibTableColumn
awcPfIptDisposition = _AwcPfIptDisposition_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 6, 1, 2),
    _AwcPfIptDisposition_Type()
)
awcPfIptDisposition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfIptDisposition.setStatus("current")


class _AwcPfIptUserPriority_Type(AwcPfPriority):
    """Custom type awcPfIptUserPriority based on AwcPfPriority"""


_AwcPfIptUserPriority_Object = MibTableColumn
awcPfIptUserPriority = _AwcPfIptUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 6, 1, 3),
    _AwcPfIptUserPriority_Type()
)
awcPfIptUserPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfIptUserPriority.setStatus("current")


class _AwcPfIptUcastTimeToLive_Type(Unsigned32):
    """Custom type awcPfIptUcastTimeToLive based on Unsigned32"""
    defaultValue = 0


_AwcPfIptUcastTimeToLive_Object = MibTableColumn
awcPfIptUcastTimeToLive = _AwcPfIptUcastTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 6, 1, 4),
    _AwcPfIptUcastTimeToLive_Type()
)
awcPfIptUcastTimeToLive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfIptUcastTimeToLive.setStatus("current")


class _AwcPfIptNUcastTimeToLive_Type(Unsigned32):
    """Custom type awcPfIptNUcastTimeToLive based on Unsigned32"""
    defaultValue = 0


_AwcPfIptNUcastTimeToLive_Object = MibTableColumn
awcPfIptNUcastTimeToLive = _AwcPfIptNUcastTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 6, 1, 5),
    _AwcPfIptNUcastTimeToLive_Type()
)
awcPfIptNUcastTimeToLive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfIptNUcastTimeToLive.setStatus("current")


class _AwcPfIptAlert_Type(TruthValue):
    """Custom type awcPfIptAlert based on TruthValue"""


_AwcPfIptAlert_Object = MibTableColumn
awcPfIptAlert = _AwcPfIptAlert_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 6, 1, 6),
    _AwcPfIptAlert_Type()
)
awcPfIptAlert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfIptAlert.setStatus("current")
_AwcPfIptStatus_Type = RowStatus
_AwcPfIptStatus_Object = MibTableColumn
awcPfIptStatus = _AwcPfIptStatus_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 20, 6, 1, 7),
    _AwcPfIptStatus_Type()
)
awcPfIptStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcPfIptStatus.setStatus("current")
_AwcMobileIP_ObjectIdentity = ObjectIdentity
awcMobileIP = _AwcMobileIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 22)
)


class _EnableMobileIP_Type(TruthValue):
    """Custom type enableMobileIP based on TruthValue"""


_EnableMobileIP_Object = MibScalar
enableMobileIP = _EnableMobileIP_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 22, 1),
    _EnableMobileIP_Type()
)
enableMobileIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableMobileIP.setStatus("current")


class _AwcprimAAP_Type(DisplayString):
    """Custom type awcprimAAP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AwcprimAAP_Type.__name__ = "DisplayString"
_AwcprimAAP_Object = MibScalar
awcprimAAP = _AwcprimAAP_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 22, 2),
    _AwcprimAAP_Type()
)
awcprimAAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcprimAAP.setStatus("current")


class _Awcsec1AAP_Type(DisplayString):
    """Custom type awcsec1AAP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Awcsec1AAP_Type.__name__ = "DisplayString"
_Awcsec1AAP_Object = MibScalar
awcsec1AAP = _Awcsec1AAP_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 22, 3),
    _Awcsec1AAP_Type()
)
awcsec1AAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcsec1AAP.setStatus("current")


class _Awcsec2AAP_Type(DisplayString):
    """Custom type awcsec2AAP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Awcsec2AAP_Type.__name__ = "DisplayString"
_Awcsec2AAP_Object = MibScalar
awcsec2AAP = _Awcsec2AAP_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 22, 4),
    _Awcsec2AAP_Type()
)
awcsec2AAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcsec2AAP.setStatus("current")
_MipSATable_Object = MibTable
mipSATable = _MipSATable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 22, 5)
)
if mibBuilder.loadTexts:
    mipSATable.setStatus("current")
_MipSAEntry_Object = MibTableRow
mipSAEntry = _MipSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 22, 5, 1)
)
mipSAEntry.setIndexNames(
    (0, "AWCVX-MIB", "mipSAIpStart"),
)
if mibBuilder.loadTexts:
    mipSAEntry.setStatus("current")
_MipSAIpStart_Type = IpAddress
_MipSAIpStart_Object = MibTableColumn
mipSAIpStart = _MipSAIpStart_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 22, 5, 1, 1),
    _MipSAIpStart_Type()
)
mipSAIpStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mipSAIpStart.setStatus("current")
_MipSAIpEnd_Type = IpAddress
_MipSAIpEnd_Object = MibTableColumn
mipSAIpEnd = _MipSAIpEnd_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 22, 5, 1, 2),
    _MipSAIpEnd_Type()
)
mipSAIpEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mipSAIpEnd.setStatus("current")


class _MipSAGroupSPI_Type(DisplayString):
    """Custom type mipSAGroupSPI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MipSAGroupSPI_Type.__name__ = "DisplayString"
_MipSAGroupSPI_Object = MibTableColumn
mipSAGroupSPI = _MipSAGroupSPI_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 22, 5, 1, 3),
    _MipSAGroupSPI_Type()
)
mipSAGroupSPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mipSAGroupSPI.setStatus("current")


class _MipSAGroupKey_Type(DisplayString):
    """Custom type mipSAGroupKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MipSAGroupKey_Type.__name__ = "DisplayString"
_MipSAGroupKey_Object = MibTableColumn
mipSAGroupKey = _MipSAGroupKey_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 22, 5, 1, 4),
    _MipSAGroupKey_Type()
)
mipSAGroupKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mipSAGroupKey.setStatus("current")
_MipSAStatus_Type = RowStatus
_MipSAStatus_Object = MibTableColumn
mipSAStatus = _MipSAStatus_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 22, 5, 1, 5),
    _MipSAStatus_Type()
)
mipSAStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mipSAStatus.setStatus("current")


class _AwcmipDebug_Type(TruthValue):
    """Custom type awcmipDebug based on TruthValue"""


_AwcmipDebug_Object = MibScalar
awcmipDebug = _AwcmipDebug_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 22, 6),
    _AwcmipDebug_Type()
)
awcmipDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcmipDebug.setStatus("current")
_AwcVxConformance_ObjectIdentity = ObjectIdentity
awcVxConformance = _AwcVxConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 100)
)
_AwcVxCompliances_ObjectIdentity = ObjectIdentity
awcVxCompliances = _AwcVxCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 100, 1)
)
_AwcVxGroups_ObjectIdentity = ObjectIdentity
awcVxGroups = _AwcVxGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 100, 2)
)

# Managed Objects groups

awcSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 522, 3, 100, 2, 1)
)
awcSystemGroup.setObjects(
      *(("AWCVX-MIB", "vxWorksVersion"),
        ("AWCVX-MIB", "creationDate"),
        ("AWCVX-MIB", "awcVxVersion"),
        ("AWCVX-MIB", "sysFlags"),
        ("AWCVX-MIB", "languageCode"),
        ("AWCVX-MIB", "awcDevID"),
        ("AWCVX-MIB", "awcDevIDtxt"),
        ("AWCVX-MIB", "enableHTTP"),
        ("AWCVX-MIB", "enableTelnet"),
        ("AWCVX-MIB", "enableSNMP"),
        ("AWCVX-MIB", "enableDnsResolver"),
        ("AWCVX-MIB", "enableSNTP"),
        ("AWCVX-MIB", "enableWDB"),
        ("AWCVX-MIB", "pingTxLen"),
        ("AWCVX-MIB", "awcFirstBoot"),
        ("AWCVX-MIB", "awcOemOUI"),
        ("AWCVX-MIB", "awcOemName"),
        ("AWCVX-MIB", "awcOemNameShort"),
        ("AWCVX-MIB", "awcOemHomeURL"),
        ("AWCVX-MIB", "enablePSPF"),
        ("AWCVX-MIB", "sysExceptionReboot"),
        ("AWCVX-MIB", "bootblockVersion"),
        ("AWCVX-MIB", "motherboardRevision"),
        ("AWCVX-MIB", "enableSTP"),
        ("AWCVX-MIB", "enableRebootKey"),
        ("AWCVX-MIB", "awcLocateUnit"))
)
if mibBuilder.loadTexts:
    awcSystemGroup.setStatus("current")

bootconfigVxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 522, 3, 100, 2, 2)
)
bootconfigVxGroup.setObjects(
      *(("AWCVX-MIB", "bootconfigBootProtocol"),
        ("AWCVX-MIB", "bootconfigReadINI"),
        ("AWCVX-MIB", "bootconfigServerConfigTimeout"),
        ("AWCVX-MIB", "bootconfigMultOfferTimeout"),
        ("AWCVX-MIB", "bootconfigReqLeaseDuration"),
        ("AWCVX-MIB", "bootconfigMinLeaseDuration"),
        ("AWCVX-MIB", "bootconfigDev"),
        ("AWCVX-MIB", "bootconfigClientAddr"),
        ("AWCVX-MIB", "bootconfigHostAddr"),
        ("AWCVX-MIB", "bootconfigBootFile"),
        ("AWCVX-MIB", "bootconfigSubnetMask"),
        ("AWCVX-MIB", "bootconfigGateway"),
        ("AWCVX-MIB", "bootconfigHostName"),
        ("AWCVX-MIB", "bootconfigClientName"),
        ("AWCVX-MIB", "bootconfigNameServerPriority"),
        ("AWCVX-MIB", "bootconfigNameServer"),
        ("AWCVX-MIB", "bootconfigDomainName"),
        ("AWCVX-MIB", "bootconfigSntpServer"),
        ("AWCVX-MIB", "bootconfigSaveServerResponse"),
        ("AWCVX-MIB", "bootconfigCmdInvokeIniLoad"),
        ("AWCVX-MIB", "bootconfigCmdStatusIniLoad"),
        ("AWCVX-MIB", "bootconfigDhcpClassID"),
        ("AWCVX-MIB", "bootconfigFileServerAddr"),
        ("AWCVX-MIB", "bootconfigLogServerAddr"),
        ("AWCVX-MIB", "bootconfigBootCount"),
        ("AWCVX-MIB", "bootconfigDhcpClientIdType"),
        ("AWCVX-MIB", "bootconfigDhcpClientIdValue"))
)
if mibBuilder.loadTexts:
    bootconfigVxGroup.setStatus("current")

awcSerialDevGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 522, 3, 100, 2, 3)
)
awcSerialDevGroup.setObjects(
      *(("AWCVX-MIB", "serialDevIndex"),
        ("AWCVX-MIB", "serialAdminStatus"),
        ("AWCVX-MIB", "serialOperStatus"),
        ("AWCVX-MIB", "serialBaud"),
        ("AWCVX-MIB", "serialParity"),
        ("AWCVX-MIB", "serialDataBits"),
        ("AWCVX-MIB", "serialStopBits"),
        ("AWCVX-MIB", "serialFlowControl"),
        ("AWCVX-MIB", "serialTerminalType"),
        ("AWCVX-MIB", "serialTerminalLines"),
        ("AWCVX-MIB", "serialTerminalColumns"),
        ("AWCVX-MIB", "serialDevFd"))
)
if mibBuilder.loadTexts:
    awcSerialDevGroup.setStatus("current")

awcFtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 522, 3, 100, 2, 4)
)
awcFtpGroup.setObjects(
      *(("AWCVX-MIB", "defaultFileServer"),
        ("AWCVX-MIB", "awcFileXferProtocol"),
        ("AWCVX-MIB", "awcFileXferUser"),
        ("AWCVX-MIB", "awcFileXferPassword"),
        ("AWCVX-MIB", "awcFileXferCmdInvokeFileLoad"),
        ("AWCVX-MIB", "awcFileXferCmdStatusFileLoad"),
        ("AWCVX-MIB", "awcFileXferCmdInvokeFileSave"),
        ("AWCVX-MIB", "awcFileXferCmdStatusFileSave"),
        ("AWCVX-MIB", "awcFileXferFileFirmwareSystem"),
        ("AWCVX-MIB", "awcFileXferFileFirmwareRadio0"),
        ("AWCVX-MIB", "awcFileXferFileWebUI"),
        ("AWCVX-MIB", "awcFileXferFileFpgaPcmcia"),
        ("AWCVX-MIB", "awcFileXferTftpPort"),
        ("AWCVX-MIB", "awcFileXferFtpDirectory"),
        ("AWCVX-MIB", "awcFileXferFilesFLASH"),
        ("AWCVX-MIB", "awcFileXferFileFirmwareRadio1"))
)
if mibBuilder.loadTexts:
    awcFtpGroup.setStatus("current")

awcIfTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 522, 3, 100, 2, 5)
)
awcIfTableGroup.setObjects(
      *(("AWCVX-MIB", "awcIfDefaultPhysAddress"),
        ("AWCVX-MIB", "awcIfPhysAddress"),
        ("AWCVX-MIB", "awcIfAdoptPrimaryIdentity"),
        ("AWCVX-MIB", "awcIfDefaultIpAddress"),
        ("AWCVX-MIB", "awcIfDefaultIpNetMask"),
        ("AWCVX-MIB", "awcIfIpAddress"),
        ("AWCVX-MIB", "awcIfIpNetMask"),
        ("AWCVX-MIB", "awcIfMSDUMaxLength"),
        ("AWCVX-MIB", "awcIfOutDiscardsCoS0"),
        ("AWCVX-MIB", "awcIfOutDiscardsCoS1"),
        ("AWCVX-MIB", "awcIfOutDiscardsCoS2"),
        ("AWCVX-MIB", "awcIfOutDiscardsCoS3"),
        ("AWCVX-MIB", "awcIfOutDiscardsCoS4"),
        ("AWCVX-MIB", "awcIfOutDiscardsCoS5"),
        ("AWCVX-MIB", "awcIfOutDiscardsCoS6"),
        ("AWCVX-MIB", "awcIfOutDiscardsCoS7"))
)
if mibBuilder.loadTexts:
    awcIfTableGroup.setStatus("current")

awc802dot11Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 522, 3, 100, 2, 6)
)
awc802dot11Group.setObjects(
      *(("AWCVX-MIB", "awcDot11StationRole"),
        ("AWCVX-MIB", "awcDot11PowerManagementSubMode"),
        ("AWCVX-MIB", "awcDot11UseAWCExtensions"),
        ("AWCVX-MIB", "awcDot11AllowAssocBroadcastSSID"),
        ("AWCVX-MIB", "awcDot11PrivacyOptionImplementedMaxRate"),
        ("AWCVX-MIB", "awcDot11DesiredBSSLength"),
        ("AWCVX-MIB", "awcDot11EnetEncapsulationDefault"),
        ("AWCVX-MIB", "awcDot11ForceReqFirmwareVersion"),
        ("AWCVX-MIB", "awcDot11BridgeSpacing"),
        ("AWCVX-MIB", "awcDot11DesiredSSIDMaxAssociatedSTA"),
        ("AWCVX-MIB", "awcDot11DesiredSSIDNumAssociatedSTA"),
        ("AWCVX-MIB", "awcDot11AuxiliarySSIDLength"),
        ("AWCVX-MIB", "awcDot11MultipleSSIDPerBSSImplemented"),
        ("AWCVX-MIB", "awcDot11SymbolExtensionsImplemented"),
        ("AWCVX-MIB", "awcDot11SymbolExtensionsEnabled"),
        ("AWCVX-MIB", "awcDot11DesiredSSIDMicAlgorithm"),
        ("AWCVX-MIB", "awcDot11DesiredSSIDWEPKeyPermuteAlgorithm"),
        ("AWCVX-MIB", "awcDot11DesiredSSIDInfrastructureWGB"),
        ("AWCVX-MIB", "awcDot11DesiredSSIDDefaultPolId"),
        ("AWCVX-MIB", "awcDot11DesiredSSIDDefaultVlanId"),
        ("AWCVX-MIB", "awcDot11DesiredSSIDEnableProxyMobileIP"),
        ("AWCVX-MIB", "awcDot11InfrastructureSSID"),
        ("AWCVX-MIB", "awcDot11QBSSElementImplemented"),
        ("AWCVX-MIB", "awcDot11QBSSElementEnabled"),
        ("AWCVX-MIB", "awcDot11InfrastructureSSIDExclusive"),
        ("AWCVX-MIB", "awcDot11SendIGMPGeneralQuery"),
        ("AWCVX-MIB", "awcDot11AuthenticationRequireEAP"),
        ("AWCVX-MIB", "awcDot11AuthenticationDefaultUcastAllowedToGoTo"),
        ("AWCVX-MIB", "awcDot11WEPDefaultKeyIndex"),
        ("AWCVX-MIB", "awcDot11WEPDefaultKeyLen"),
        ("AWCVX-MIB", "awcDot11WEPDefaultKeyValue"),
        ("AWCVX-MIB", "awcDot11WEPDefaultKeyMaxIndex"),
        ("AWCVX-MIB", "awcDot11AllowEncrypted"),
        ("AWCVX-MIB", "awcDot11WEPKeyMaxLen"),
        ("AWCVX-MIB", "awcDot11LEAPUserName"),
        ("AWCVX-MIB", "awcDot11LEAPPassword"),
        ("AWCVX-MIB", "awcDot11DesiredBSSIndex"),
        ("AWCVX-MIB", "awcDot11DesiredBSS"),
        ("AWCVX-MIB", "awcDot11AuxSSIDIndex"),
        ("AWCVX-MIB", "awcDot11AuxSSID"),
        ("AWCVX-MIB", "awcDot11AuxSSIDMaxAssociatedSTA"),
        ("AWCVX-MIB", "awcDot11AuxSSIDNumAssociatedSTA"),
        ("AWCVX-MIB", "awcDot11AuxSSIDDefaultPolId"),
        ("AWCVX-MIB", "awcDot11AuxSSIDDefaultVlanId"),
        ("AWCVX-MIB", "awcDot11AuxSSIDEnableProxyMobileIP"),
        ("AWCVX-MIB", "awcDot11AuxSSIDAuthAlgEnable"),
        ("AWCVX-MIB", "awcDot11AuxSSIDAuthAlgRequireEAP"),
        ("AWCVX-MIB", "awcDot11AuxSSIDAuthAlgDefaultUcastAllowedToGoTo"),
        ("AWCVX-MIB", "awcDot11AssignedAID"),
        ("AWCVX-MIB", "awcDot11AssignedSTA"),
        ("AWCVX-MIB", "awcDot11FirmwareBootstrapVersion"),
        ("AWCVX-MIB", "awcDot11CurrentCarrierSet"),
        ("AWCVX-MIB", "awcDot11ModulationType"),
        ("AWCVX-MIB", "awcDot11PreambleType"),
        ("AWCVX-MIB", "awcDot11PHYType"),
        ("AWCVX-MIB", "awcDot11Compatible3100"),
        ("AWCVX-MIB", "awcDot11Compatible4500"),
        ("AWCVX-MIB", "awcDot11ChannelAutoImplemented"),
        ("AWCVX-MIB", "awcDot11ChannelAutoEnabled"),
        ("AWCVX-MIB", "awcDot11CurrentChannel"),
        ("AWCVX-MIB", "awcDot11SupportedDataRatesPrivacyIndex"),
        ("AWCVX-MIB", "awcDot11SupportedDataRatesPrivacyValue"),
        ("AWCVX-MIB", "awcDot11SupportedDataRatesPrivacyImplemented"),
        ("AWCVX-MIB", "awcDot11ChanSelectChannel"),
        ("AWCVX-MIB", "awcDot11ChanSelectEnable"),
        ("AWCVX-MIB", "awcDot11AssociatedStationCount"),
        ("AWCVX-MIB", "awcDot11AuthenticatedStationCount"),
        ("AWCVX-MIB", "awcDot11ReassociatedStationCount"),
        ("AWCVX-MIB", "awcDot11RoamedStationCount"),
        ("AWCVX-MIB", "awcDot11DeauthenticateCount"),
        ("AWCVX-MIB", "awcDot11DisassociateCount"),
        ("AWCVX-MIB", "awcDot11EncapPktsMMH"),
        ("AWCVX-MIB", "awcDot11DecapPktsMMH"),
        ("AWCVX-MIB", "awcDot11EncapErrorsMMH"),
        ("AWCVX-MIB", "awcDot11DecapErrorsMMH"),
        ("AWCVX-MIB", "awcDot11DecapExistsMMH"),
        ("AWCVX-MIB", "awcDot11DecapAccessMMH"),
        ("AWCVX-MIB", "awcDot11TxDeferEnergyCount"),
        ("AWCVX-MIB", "awcDot11RxMacCrcErrorCount"),
        ("AWCVX-MIB", "awcDot11SsidMismatchCount"),
        ("AWCVX-MIB", "awcDot11QoSCWmin"),
        ("AWCVX-MIB", "awcDot11QoSCWmax"))
)
if mibBuilder.loadTexts:
    awc802dot11Group.setStatus("current")

awcUserMgrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 522, 3, 100, 2, 7)
)
awcUserMgrGroup.setObjects(
      *(("AWCVX-MIB", "userMgrUserIndex"),
        ("AWCVX-MIB", "userMgrUserName"),
        ("AWCVX-MIB", "userMgrPassword"),
        ("AWCVX-MIB", "userMgrCapabilities"),
        ("AWCVX-MIB", "userMgrStatus"),
        ("AWCVX-MIB", "enableUserMgr"),
        ("AWCVX-MIB", "allowBrowseWithoutLogin"),
        ("AWCVX-MIB", "protectLegalPage"))
)
if mibBuilder.loadTexts:
    awcUserMgrGroup.setStatus("current")

awcHttpdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 522, 3, 100, 2, 8)
)
awcHttpdGroup.setObjects(
      *(("AWCVX-MIB", "defaultWebRoot"),
        ("AWCVX-MIB", "defaultHelpRoot"),
        ("AWCVX-MIB", "getWebUI"),
        ("AWCVX-MIB", "cmdInvokeGetWebUI"),
        ("AWCVX-MIB", "cmdStatusGetWebUI"),
        ("AWCVX-MIB", "awcHttpdPort"),
        ("AWCVX-MIB", "awcConsoleAutoApply"))
)
if mibBuilder.loadTexts:
    awcHttpdGroup.setStatus("current")

awcDnsResGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 522, 3, 100, 2, 9)
)
awcDnsResGroup.setObjects(
      *(("AWCVX-MIB", "resolverDomain"),
        ("AWCVX-MIB", "resolverDomainSuffix"),
        ("AWCVX-MIB", "resolverDomainServerPriority"),
        ("AWCVX-MIB", "resolverDomainServer"),
        ("AWCVX-MIB", "defaultResolverDomain"),
        ("AWCVX-MIB", "defaultResolverDomainServerPriority"),
        ("AWCVX-MIB", "defaultResolverDomainServer"))
)
if mibBuilder.loadTexts:
    awcDnsResGroup.setStatus("current")

awcSnmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 522, 3, 100, 2, 10)
)
awcSnmpGroup.setObjects(
      *(("AWCVX-MIB", "snmpTrapDest"),
        ("AWCVX-MIB", "snmpTrapCommunity"))
)
if mibBuilder.loadTexts:
    awcSnmpGroup.setStatus("current")

awcSntpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 522, 3, 100, 2, 11)
)
awcSntpGroup.setObjects(
      *(("AWCVX-MIB", "defaultSntpServer"),
        ("AWCVX-MIB", "sntpServer"))
)
if mibBuilder.loadTexts:
    awcSntpGroup.setStatus("current")

awcForwardTblGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 522, 3, 100, 2, 12)
)
awcForwardTblGroup.setObjects(
      *(("AWCVX-MIB", "awcFtMcastAddr"),
        ("AWCVX-MIB", "awcFtDsHost"),
        ("AWCVX-MIB", "awcFtBridgeHost"),
        ("AWCVX-MIB", "awcFtClientSTA"),
        ("AWCVX-MIB", "awcFtClientSTASelf"),
        ("AWCVX-MIB", "awcFtBridge"),
        ("AWCVX-MIB", "awcFtBridgeSelf"),
        ("AWCVX-MIB", "awcFtRepeater"),
        ("AWCVX-MIB", "awcFtRepeaterSelf"),
        ("AWCVX-MIB", "awcFtAccessPoint"),
        ("AWCVX-MIB", "awcFtBridgeRoot"),
        ("AWCVX-MIB", "awcFtMaxNumEntries"),
        ("AWCVX-MIB", "awcFtTimeoutSecUnknown"),
        ("AWCVX-MIB", "awcFtTimeoutSecMcastAddr"),
        ("AWCVX-MIB", "awcFtTimeoutSecDsHost"),
        ("AWCVX-MIB", "awcFtTimeoutSecBridgeHost"),
        ("AWCVX-MIB", "awcFtTimeoutSecClientSTA"),
        ("AWCVX-MIB", "awcFtTimeoutSecBridge"),
        ("AWCVX-MIB", "awcFtTimeoutSecRepeater"),
        ("AWCVX-MIB", "awcFtTimeoutSecAccessPoint"),
        ("AWCVX-MIB", "awcFtTimeoutSecBridgeRoot"),
        ("AWCVX-MIB", "awcFtEnableAwcTpFdbTable"),
        ("AWCVX-MIB", "awcFtEnableMacAuthServer"),
        ("AWCVX-MIB", "awcFtRogueApAlertTimeout"),
        ("AWCVX-MIB", "awcFtEnableMacOrEapAuth"),
        ("AWCVX-MIB", "awcFtDot1dTpFdbTableEnable"),
        ("AWCVX-MIB", "awcTpFdbAddress"),
        ("AWCVX-MIB", "awcTpFdbClassID"),
        ("AWCVX-MIB", "awcTpFdbSrcPktsImmed"),
        ("AWCVX-MIB", "awcTpFdbSrcOctetsImmed"),
        ("AWCVX-MIB", "awcTpFdbSrcErrorPktsImmed"),
        ("AWCVX-MIB", "awcTpFdbSrcErrorOctetsImmed"),
        ("AWCVX-MIB", "awcTpFdbDestPktsImmed"),
        ("AWCVX-MIB", "awcTpFdbDestOctetsImmed"),
        ("AWCVX-MIB", "awcTpFdbDestErrorPktsImmed"),
        ("AWCVX-MIB", "awcTpFdbDestErrorOctetsImmed"),
        ("AWCVX-MIB", "awcTpFdbDestMaxRetryErrorsImmed"),
        ("AWCVX-MIB", "awcTpFdbIPv4Addr"),
        ("AWCVX-MIB", "awcTpFdbDdpAddress"),
        ("AWCVX-MIB", "awcTpFdbDdpSysName"),
        ("AWCVX-MIB", "awcTpFdbDdpProdDevID"),
        ("AWCVX-MIB", "awcTpFdbDdpRadioDevID"),
        ("AWCVX-MIB", "awcTpFdbDdpSwVerMajor"),
        ("AWCVX-MIB", "awcTpFdbDdpSwVerMinor"),
        ("AWCVX-MIB", "awcTpFdbDdpSwVerBeta"),
        ("AWCVX-MIB", "awcTpFdbDdpUptime"),
        ("AWCVX-MIB", "awcTpFdbDdpNumAnnounceSent"),
        ("AWCVX-MIB", "awcTpFdbDdpNumAssociated"),
        ("AWCVX-MIB", "awcTpFdbDdpLoad"),
        ("AWCVX-MIB", "awcTpFdbDdpDistFromDS"),
        ("AWCVX-MIB", "awcDot11TpFdbAddress"),
        ("AWCVX-MIB", "awcDot11TpFdbAID"),
        ("AWCVX-MIB", "awcDot11TpFdbClientState"),
        ("AWCVX-MIB", "awcDot11TpFdbTxShortRetries"),
        ("AWCVX-MIB", "awcDot11TpFdbTxLongRetries"),
        ("AWCVX-MIB", "awcDot11TpFdbLatestTxShortRetries"),
        ("AWCVX-MIB", "awcDot11TpFdbLatestTxLongRetries"),
        ("AWCVX-MIB", "awcDot11TpFdbRxWEPErrors"),
        ("AWCVX-MIB", "awcDot11TpFdbLatestRxSignalStrength"),
        ("AWCVX-MIB", "awcDot11TpFdbLatestRxSignalQuality"),
        ("AWCVX-MIB", "awcDot11TpFdbCapabilities"),
        ("AWCVX-MIB", "awcDot11TpFdbListenInterval"),
        ("AWCVX-MIB", "awcDot11TpFdbSupportedDataRates"),
        ("AWCVX-MIB", "awcDot11TpFdbPreferredTxRate"),
        ("AWCVX-MIB", "awcDot11TpFdbCurrentBSS"),
        ("AWCVX-MIB", "awcDot11TpFdbSSID"),
        ("AWCVX-MIB", "awcDot11TpFdbVlanId"),
        ("AWCVX-MIB", "awcDot1dTpPortDefaultUcastAllowedToGoTo"),
        ("AWCVX-MIB", "awcDot1dTpPortDefaultNUcastAllowedToGoTo"),
        ("AWCVX-MIB", "awcDot1dTpPortMaxNUcastPerSecond"),
        ("AWCVX-MIB", "awcDot1dTpPortDefaultInEthertypeFilterId"),
        ("AWCVX-MIB", "awcDot1dTpPortDefaultOutEthertypeFilterId"),
        ("AWCVX-MIB", "awcDot1dTpPortDefaultInIpProtoFilterId"),
        ("AWCVX-MIB", "awcDot1dTpPortDefaultOutIpProtoFilterId"),
        ("AWCVX-MIB", "awcDot1dTpPortDefaultInIpPortFilterId"),
        ("AWCVX-MIB", "awcDot1dTpPortDefaultOutIpPortFilterId"),
        ("AWCVX-MIB", "awcTpFdbAlertAddress"),
        ("AWCVX-MIB", "awcTpFdbFromAlertSrcPktsImmed"),
        ("AWCVX-MIB", "awcTpFdbFromAlertSrcOctetsImmed"),
        ("AWCVX-MIB", "awcTpFdbToAlertDestPktsImmed"),
        ("AWCVX-MIB", "awcTpFdbToAlertDestOctetsImmed"),
        ("AWCVX-MIB", "awcTpFdbAlertSentAlertTypePktsImmed"),
        ("AWCVX-MIB", "awcTpFdbAlertSentAlertTypeOctetsImmed"),
        ("AWCVX-MIB", "awcTpFdbAlertRcvdAlertTypePktsImmed"),
        ("AWCVX-MIB", "awcTpFdbAlertRcvdAlertTypeOctetsImmed"))
)
if mibBuilder.loadTexts:
    awcForwardTblGroup.setStatus("current")

awcEventLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 522, 3, 100, 2, 14)
)
awcEventLogGroup.setObjects(
      *(("AWCVX-MIB", "awcEventOffsetGMT"),
        ("AWCVX-MIB", "awcEventUseDaylightSavingsTime"),
        ("AWCVX-MIB", "awcEventTimestampGMT"),
        ("AWCVX-MIB", "awcEventUptimeModifiedGMT"),
        ("AWCVX-MIB", "awcEventDisplayWallClockTime"),
        ("AWCVX-MIB", "awcEventDisplayUptimeAscending"),
        ("AWCVX-MIB", "awcEventDetailDefault"),
        ("AWCVX-MIB", "awcEventSeverityDispConsole"),
        ("AWCVX-MIB", "awcEventSeverityDispHtmlGUI"),
        ("AWCVX-MIB", "awcEventSeverityDispHtmlConsole"),
        ("AWCVX-MIB", "awcEventAlertSNMP"),
        ("AWCVX-MIB", "awcEventAlertSyslog"),
        ("AWCVX-MIB", "awcEventCntSeverityNULL"),
        ("AWCVX-MIB", "awcEventCntSeveritySilent"),
        ("AWCVX-MIB", "awcEventCntSeveritySystemFatal"),
        ("AWCVX-MIB", "awcEventCntSeverityProtocolFatal"),
        ("AWCVX-MIB", "awcEventCntSeverityPortFatal"),
        ("AWCVX-MIB", "awcEventCntSeveritySystemAlert"),
        ("AWCVX-MIB", "awcEventCntSeverityProtocolAlert"),
        ("AWCVX-MIB", "awcEventCntSeverityPortAlert"),
        ("AWCVX-MIB", "awcEventCntSeverityExternalAlert"),
        ("AWCVX-MIB", "awcEventCntSeveritySystemWarning"),
        ("AWCVX-MIB", "awcEventCntSeverityProtocolWarning"),
        ("AWCVX-MIB", "awcEventCntSeverityPortWarning"),
        ("AWCVX-MIB", "awcEventCntSeverityExternalWarning"),
        ("AWCVX-MIB", "awcEventCntSeveritySystemInfo"),
        ("AWCVX-MIB", "awcEventCntSeverityProtocolInfo"),
        ("AWCVX-MIB", "awcEventCntSeverityPortInfo"),
        ("AWCVX-MIB", "awcEventCntSeverityExternalInfo"),
        ("AWCVX-MIB", "awcEventDispSeverityNULL"),
        ("AWCVX-MIB", "awcEventDispSeveritySilent"),
        ("AWCVX-MIB", "awcEventDispSeveritySystemFatal"),
        ("AWCVX-MIB", "awcEventDispSeverityProtocolFatal"),
        ("AWCVX-MIB", "awcEventDispSeverityPortFatal"),
        ("AWCVX-MIB", "awcEventDispSeveritySystemAlert"),
        ("AWCVX-MIB", "awcEventDispSeverityProtocolAlert"),
        ("AWCVX-MIB", "awcEventDispSeverityPortAlert"),
        ("AWCVX-MIB", "awcEventDispSeverityExternalAlert"),
        ("AWCVX-MIB", "awcEventDispSeveritySystemWarning"),
        ("AWCVX-MIB", "awcEventDispSeverityProtocolWarning"),
        ("AWCVX-MIB", "awcEventDispSeverityPortWarning"),
        ("AWCVX-MIB", "awcEventDispSeverityExternalWarning"),
        ("AWCVX-MIB", "awcEventDispSeveritySystemInfo"),
        ("AWCVX-MIB", "awcEventDispSeverityProtocolInfo"),
        ("AWCVX-MIB", "awcEventDispSeverityPortInfo"),
        ("AWCVX-MIB", "awcEventDispSeverityExternalInfo"),
        ("AWCVX-MIB", "awcEventSyslogAddr"),
        ("AWCVX-MIB", "awcEventSyslogFacility"),
        ("AWCVX-MIB", "awcEventTraceStationSeverity"),
        ("AWCVX-MIB", "awcEventTraceLogSize"),
        ("AWCVX-MIB", "awcEventTracePacketLen"),
        ("AWCVX-MIB", "awcEventID"),
        ("AWCVX-MIB", "awcEventTime"),
        ("AWCVX-MIB", "awcEventSeverity"),
        ("AWCVX-MIB", "awcEventDescription"),
        ("AWCVX-MIB", "awcEventType"),
        ("AWCVX-MIB", "awcEventUseCiscoFormat"),
        ("AWCVX-MIB", "awcDot11AuthenticateFailDisposition"),
        ("AWCVX-MIB", "awcDot11DeauthenticateDisposition"),
        ("AWCVX-MIB", "awcDot11DisassociateDisposition"))
)
if mibBuilder.loadTexts:
    awcEventLogGroup.setStatus("current")

awcEtherMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 522, 3, 100, 2, 15)
)
awcEtherMIBGroup.setObjects(
      *(("AWCVX-MIB", "awcEtherIfSpeedSelect"),
        ("AWCVX-MIB", "awcEtherDuplex"),
        ("AWCVX-MIB", "awcEtherCamSize"),
        ("AWCVX-MIB", "awcEtherEnableSwCam"),
        ("AWCVX-MIB", "awcEtherForcePortUnblock"))
)
if mibBuilder.loadTexts:
    awcEtherMIBGroup.setStatus("current")

awcPolicyGroupsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 522, 3, 100, 2, 16)
)
awcPolicyGroupsGroup.setObjects(
      *(("AWCVX-MIB", "awcPolGrpName"),
        ("AWCVX-MIB", "awcPolGrpStatus"),
        ("AWCVX-MIB", "awcPolGrpInEthertypeFilterId"),
        ("AWCVX-MIB", "awcPolGrpOutEthertypeFilterId"),
        ("AWCVX-MIB", "awcPolGrpInIpProtoFilterId"),
        ("AWCVX-MIB", "awcPolGrpOutIpProtoFilterId"),
        ("AWCVX-MIB", "awcPolGrpInIpPortFilterId"),
        ("AWCVX-MIB", "awcPolGrpOutIpPortFilterId"),
        ("AWCVX-MIB", "awcDscpToCosMapEnable"),
        ("AWCVX-MIB", "awcDscpToCosMapCos"))
)
if mibBuilder.loadTexts:
    awcPolicyGroupsGroup.setStatus("current")

awcDdpIAPPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 522, 3, 100, 2, 17)
)
awcDdpIAPPGroup.setObjects(
      *(("AWCVX-MIB", "awcIappMcastIpAddr"),
        ("AWCVX-MIB", "awcIappPort"),
        ("AWCVX-MIB", "awcP802dot1XVersion"))
)
if mibBuilder.loadTexts:
    awcDdpIAPPGroup.setStatus("current")

awcHotStandbyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 522, 3, 100, 2, 18)
)
awcHotStandbyGroup.setObjects(
      *(("AWCVX-MIB", "awcHotStandbyMACAddr"),
        ("AWCVX-MIB", "awcHotStandbyPollingFrequency"),
        ("AWCVX-MIB", "awcHotStandbyPollingTimeOut"),
        ("AWCVX-MIB", "awcHotStandbyInHotStandby"),
        ("AWCVX-MIB", "awcHotStandbyState"),
        ("AWCVX-MIB", "awcHotStandbyStatus"))
)
if mibBuilder.loadTexts:
    awcHotStandbyGroup.setStatus("current")

awcAaaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 522, 3, 100, 2, 19)
)
awcAaaGroup.setObjects(
      *(("AWCVX-MIB", "awcAaaServerPriority"),
        ("AWCVX-MIB", "awcAaaServerProtocol"),
        ("AWCVX-MIB", "awcAaaServerName"),
        ("AWCVX-MIB", "awcAaaServerPort"),
        ("AWCVX-MIB", "awcAaaServerTimeout"),
        ("AWCVX-MIB", "awcAaaClientName"),
        ("AWCVX-MIB", "awcAaaServerSharedSecret"),
        ("AWCVX-MIB", "awcAaaServer8021xCapabilityEnabled"),
        ("AWCVX-MIB", "awcAaaServerMacAddrAuthEnabled"),
        ("AWCVX-MIB", "awcAaaServerAdminAuthEnabled"),
        ("AWCVX-MIB", "awcAaaServerMipAuthEnabled"),
        ("AWCVX-MIB", "awcAaaServerMaxRetransmission"),
        ("AWCVX-MIB", "awcAcctServerPriority"),
        ("AWCVX-MIB", "awcAcctServerProtocol"),
        ("AWCVX-MIB", "awcAcctServerName"),
        ("AWCVX-MIB", "awcAcctServerPort"),
        ("AWCVX-MIB", "awcAcctServerTimeout"),
        ("AWCVX-MIB", "awcAcctServerUpdateEnable"),
        ("AWCVX-MIB", "awcAcctServerUpdateDelay"),
        ("AWCVX-MIB", "awcAcctClientName"),
        ("AWCVX-MIB", "awcAcctSecureEnabled"),
        ("AWCVX-MIB", "awcAcctGeneralEnabled"),
        ("AWCVX-MIB", "awcAcctServerSharedSecret"),
        ("AWCVX-MIB", "awcAcctServerMaxRetransmission"),
        ("AWCVX-MIB", "awcAcctEnable"),
        ("AWCVX-MIB", "awcAcctStopDelayEnable"),
        ("AWCVX-MIB", "awcAcctStopDelayTime"),
        ("AWCVX-MIB", "awcAaaServerPrimaryReattemptPeriod"),
        ("AWCVX-MIB", "awcAaaServerDot1xAuthCurrent"),
        ("AWCVX-MIB", "awcAaaServerMacAddrAuthCurrent"),
        ("AWCVX-MIB", "awcAaaServerAdminAuthCurrent"),
        ("AWCVX-MIB", "awcAaaServerMipAuthCurrent"))
)
if mibBuilder.loadTexts:
    awcAaaGroup.setStatus("current")

awcProtocolFiltersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 522, 3, 100, 2, 20)
)
awcProtocolFiltersGroup.setObjects(
      *(("AWCVX-MIB", "awcPfEtSetId"),
        ("AWCVX-MIB", "awcPfEtSetName"),
        ("AWCVX-MIB", "awcPfEtDefaultDisposition"),
        ("AWCVX-MIB", "awcPfEtDefaultUcastTimeToLive"),
        ("AWCVX-MIB", "awcPfEtDefaultNUcastTimeToLive"),
        ("AWCVX-MIB", "awcPfEtSetStatus"),
        ("AWCVX-MIB", "awcPfEtEthertype"),
        ("AWCVX-MIB", "awcPfEtDisposition"),
        ("AWCVX-MIB", "awcPfEtUserPriority"),
        ("AWCVX-MIB", "awcPfEtUcastTimeToLive"),
        ("AWCVX-MIB", "awcPfEtNUcastTimeToLive"),
        ("AWCVX-MIB", "awcPfEtAlert"),
        ("AWCVX-MIB", "awcPfEtStatus"),
        ("AWCVX-MIB", "awcPfIppSetId"),
        ("AWCVX-MIB", "awcPfIppSetName"),
        ("AWCVX-MIB", "awcPfIppDefaultDisposition"),
        ("AWCVX-MIB", "awcPfIppDefaultUcastTimeToLive"),
        ("AWCVX-MIB", "awcPfIppDefaultNUcastTimeToLive"),
        ("AWCVX-MIB", "awcPfIppSetStatus"),
        ("AWCVX-MIB", "awcPfIppIpProtocol"),
        ("AWCVX-MIB", "awcPfIppDisposition"),
        ("AWCVX-MIB", "awcPfIppUserPriority"),
        ("AWCVX-MIB", "awcPfIppUcastTimeToLive"),
        ("AWCVX-MIB", "awcPfIppNUcastTimeToLive"),
        ("AWCVX-MIB", "awcPfIppAlert"),
        ("AWCVX-MIB", "awcPfIppStatus"),
        ("AWCVX-MIB", "awcPfIptSetId"),
        ("AWCVX-MIB", "awcPfIptSetName"),
        ("AWCVX-MIB", "awcPfIptDefaultDisposition"),
        ("AWCVX-MIB", "awcPfIptDefaultUcastTimeToLive"),
        ("AWCVX-MIB", "awcPfIptDefaultNUcastTimeToLive"),
        ("AWCVX-MIB", "awcPfIptSetStatus"),
        ("AWCVX-MIB", "awcPfIptIpPort"),
        ("AWCVX-MIB", "awcPfIptDisposition"),
        ("AWCVX-MIB", "awcPfIptUserPriority"),
        ("AWCVX-MIB", "awcPfIptUcastTimeToLive"),
        ("AWCVX-MIB", "awcPfIptNUcastTimeToLive"),
        ("AWCVX-MIB", "awcPfIptAlert"),
        ("AWCVX-MIB", "awcPfIptStatus"))
)
if mibBuilder.loadTexts:
    awcProtocolFiltersGroup.setStatus("current")

awcMobileIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 522, 3, 100, 2, 21)
)
awcMobileIpGroup.setObjects(
      *(("AWCVX-MIB", "enableMobileIP"),
        ("AWCVX-MIB", "mipSAIpEnd"),
        ("AWCVX-MIB", "mipSAGroupSPI"),
        ("AWCVX-MIB", "mipSAGroupKey"),
        ("AWCVX-MIB", "mipSAStatus"),
        ("AWCVX-MIB", "awcmipDebug"),
        ("AWCVX-MIB", "awcprimAAP"),
        ("AWCVX-MIB", "awcsec1AAP"),
        ("AWCVX-MIB", "awcsec2AAP"))
)
if mibBuilder.loadTexts:
    awcMobileIpGroup.setStatus("current")

awcEthernetLostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 522, 3, 100, 2, 22)
)
awcEthernetLostGroup.setObjects(
      *(("AWCVX-MIB", "awcEtherLostEthernetSeconds"),
        ("AWCVX-MIB", "awcEtherLostEthernetAction"),
        ("AWCVX-MIB", "awcEtherLostEthernetSSID"))
)
if mibBuilder.loadTexts:
    awcEthernetLostGroup.setStatus("current")

awc802dot11GroupExt1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 522, 3, 100, 2, 23)
)
awc802dot11GroupExt1.setObjects(
    ("AWCVX-MIB", "awcDot11NonRootMobility")
)
if mibBuilder.loadTexts:
    awc802dot11GroupExt1.setStatus("current")

awcForwardTblGroupExt1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 522, 3, 100, 2, 24)
)
awcForwardTblGroupExt1.setObjects(
    ("AWCVX-MIB", "awcFtEnableMcastMapping")
)
if mibBuilder.loadTexts:
    awcForwardTblGroupExt1.setStatus("current")


# Notification objects

awcTrapLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 522, 4)
)
awcTrapLog.setObjects(
      *(("AWCVX-MIB", "awcEventTime"),
        ("AWCVX-MIB", "awcEventSeverity"),
        ("AWCVX-MIB", "awcEventDescription"),
        ("AWCVX-MIB", "awcEventType"))
)
if mibBuilder.loadTexts:
    awcTrapLog.setStatus(
        "current"
    )


# Notifications groups

awcTrapLogGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 522, 3, 100, 2, 100)
)
awcTrapLogGroup.setObjects(
    ("AWCVX-MIB", "awcTrapLog")
)
if mibBuilder.loadTexts:
    awcTrapLogGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

awcVxCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 522, 3, 100, 1, 1)
)
if mibBuilder.loadTexts:
    awcVxCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AWCVX-MIB",
    **{"AwcVlanId": AwcVlanId,
       "AwcPolId": AwcPolId,
       "WEPKeytype128": WEPKeytype128,
       "AwcInvokeCommand": AwcInvokeCommand,
       "AwcDot11MicAlgorithm": AwcDot11MicAlgorithm,
       "AwcDot11WEPKeyPermuteAlgorithm": AwcDot11WEPKeyPermuteAlgorithm,
       "AwcEventDisposition": AwcEventDisposition,
       "AwcDot11EventDisposition": AwcDot11EventDisposition,
       "AwcHotStandbyStatus": AwcHotStandbyStatus,
       "AwcTpFdbClassID": AwcTpFdbClassID,
       "AwcDdpProdDevID": AwcDdpProdDevID,
       "AwcDdpRadioDevID": AwcDdpRadioDevID,
       "AwcDot11ClientState": AwcDot11ClientState,
       "AwcEventSeverity": AwcEventSeverity,
       "AwcHotStandbyState": AwcHotStandbyState,
       "AwcPfDisposition": AwcPfDisposition,
       "AwcPfPriority": AwcPfPriority,
       "aironet": aironet,
       "awcVx": awcVx,
       "awcSystem": awcSystem,
       "vxWorksVersion": vxWorksVersion,
       "creationDate": creationDate,
       "awcVxVersion": awcVxVersion,
       "sysFlags": sysFlags,
       "languageCode": languageCode,
       "awcDevID": awcDevID,
       "awcDevIDtxt": awcDevIDtxt,
       "enableHTTP": enableHTTP,
       "enableTelnet": enableTelnet,
       "enableSNMP": enableSNMP,
       "enableDnsResolver": enableDnsResolver,
       "enableSNTP": enableSNTP,
       "enableWDB": enableWDB,
       "pingTxLen": pingTxLen,
       "awcFirstBoot": awcFirstBoot,
       "awcOemOUI": awcOemOUI,
       "awcOemName": awcOemName,
       "awcOemNameShort": awcOemNameShort,
       "awcOemHomeURL": awcOemHomeURL,
       "enablePSPF": enablePSPF,
       "sysExceptionReboot": sysExceptionReboot,
       "bootblockVersion": bootblockVersion,
       "motherboardRevision": motherboardRevision,
       "enableSTP": enableSTP,
       "enableRebootKey": enableRebootKey,
       "awcLocateUnit": awcLocateUnit,
       "bootconfigVx": bootconfigVx,
       "bootconfigBootProtocol": bootconfigBootProtocol,
       "bootconfigReadINI": bootconfigReadINI,
       "bootconfigServerConfigTimeout": bootconfigServerConfigTimeout,
       "bootconfigMultOfferTimeout": bootconfigMultOfferTimeout,
       "bootconfigReqLeaseDuration": bootconfigReqLeaseDuration,
       "bootconfigMinLeaseDuration": bootconfigMinLeaseDuration,
       "bootconfigDev": bootconfigDev,
       "bootconfigClientAddr": bootconfigClientAddr,
       "bootconfigHostAddr": bootconfigHostAddr,
       "bootconfigBootFile": bootconfigBootFile,
       "bootconfigSubnetMask": bootconfigSubnetMask,
       "bootconfigGateway": bootconfigGateway,
       "bootconfigHostName": bootconfigHostName,
       "bootconfigClientName": bootconfigClientName,
       "bootconfigNameServerTable": bootconfigNameServerTable,
       "bootconfigNameServerEntry": bootconfigNameServerEntry,
       "bootconfigNameServerPriority": bootconfigNameServerPriority,
       "bootconfigNameServer": bootconfigNameServer,
       "bootconfigDomainName": bootconfigDomainName,
       "bootconfigSntpServer": bootconfigSntpServer,
       "bootconfigSaveServerResponse": bootconfigSaveServerResponse,
       "bootconfigCmdInvokeIniLoad": bootconfigCmdInvokeIniLoad,
       "bootconfigCmdStatusIniLoad": bootconfigCmdStatusIniLoad,
       "bootconfigDhcpClassID": bootconfigDhcpClassID,
       "bootconfigFileServerAddr": bootconfigFileServerAddr,
       "bootconfigLogServerAddr": bootconfigLogServerAddr,
       "bootconfigBootCount": bootconfigBootCount,
       "bootconfigDhcpClientIdType": bootconfigDhcpClientIdType,
       "bootconfigDhcpClientIdValue": bootconfigDhcpClientIdValue,
       "awcSerialDev": awcSerialDev,
       "awcSerialConfigTable": awcSerialConfigTable,
       "awcSerialConfigEntry": awcSerialConfigEntry,
       "serialDevIndex": serialDevIndex,
       "serialAdminStatus": serialAdminStatus,
       "serialOperStatus": serialOperStatus,
       "serialBaud": serialBaud,
       "serialParity": serialParity,
       "serialDataBits": serialDataBits,
       "serialStopBits": serialStopBits,
       "serialFlowControl": serialFlowControl,
       "serialTerminalType": serialTerminalType,
       "serialTerminalLines": serialTerminalLines,
       "serialTerminalColumns": serialTerminalColumns,
       "serialDevFd": serialDevFd,
       "awcFtp": awcFtp,
       "defaultFileServer": defaultFileServer,
       "awcFileXferProtocol": awcFileXferProtocol,
       "awcFileXferUser": awcFileXferUser,
       "awcFileXferPassword": awcFileXferPassword,
       "awcFileXferCmdInvokeFileLoad": awcFileXferCmdInvokeFileLoad,
       "awcFileXferCmdStatusFileLoad": awcFileXferCmdStatusFileLoad,
       "awcFileXferCmdInvokeFileSave": awcFileXferCmdInvokeFileSave,
       "awcFileXferCmdStatusFileSave": awcFileXferCmdStatusFileSave,
       "awcFileXferFileFirmwareSystem": awcFileXferFileFirmwareSystem,
       "awcFileXferFileFirmwareRadio0": awcFileXferFileFirmwareRadio0,
       "awcFileXferFileWebUI": awcFileXferFileWebUI,
       "awcFileXferFileFpgaPcmcia": awcFileXferFileFpgaPcmcia,
       "awcFileXferTftpPort": awcFileXferTftpPort,
       "awcFileXferFtpDirectory": awcFileXferFtpDirectory,
       "awcFileXferFilesFLASH": awcFileXferFilesFLASH,
       "awcFileXferFileFirmwareRadio1": awcFileXferFileFirmwareRadio1,
       "awcIfTable": awcIfTable,
       "awcIfEntry": awcIfEntry,
       "awcIfDefaultPhysAddress": awcIfDefaultPhysAddress,
       "awcIfPhysAddress": awcIfPhysAddress,
       "awcIfAdoptPrimaryIdentity": awcIfAdoptPrimaryIdentity,
       "awcIfDefaultIpAddress": awcIfDefaultIpAddress,
       "awcIfDefaultIpNetMask": awcIfDefaultIpNetMask,
       "awcIfIpAddress": awcIfIpAddress,
       "awcIfIpNetMask": awcIfIpNetMask,
       "awcIfMSDUMaxLength": awcIfMSDUMaxLength,
       "awcIfOutDiscardsCoS0": awcIfOutDiscardsCoS0,
       "awcIfOutDiscardsCoS1": awcIfOutDiscardsCoS1,
       "awcIfOutDiscardsCoS2": awcIfOutDiscardsCoS2,
       "awcIfOutDiscardsCoS3": awcIfOutDiscardsCoS3,
       "awcIfOutDiscardsCoS4": awcIfOutDiscardsCoS4,
       "awcIfOutDiscardsCoS5": awcIfOutDiscardsCoS5,
       "awcIfOutDiscardsCoS6": awcIfOutDiscardsCoS6,
       "awcIfOutDiscardsCoS7": awcIfOutDiscardsCoS7,
       "awc802dot11": awc802dot11,
       "awcDot11smt": awcDot11smt,
       "awcDot11StationConfigTable": awcDot11StationConfigTable,
       "awcDot11StationConfigEntry": awcDot11StationConfigEntry,
       "awcDot11StationRole": awcDot11StationRole,
       "awcDot11PowerManagementSubMode": awcDot11PowerManagementSubMode,
       "awcDot11UseAWCExtensions": awcDot11UseAWCExtensions,
       "awcDot11AllowAssocBroadcastSSID": awcDot11AllowAssocBroadcastSSID,
       "awcDot11PrivacyOptionImplementedMaxRate": awcDot11PrivacyOptionImplementedMaxRate,
       "awcDot11DesiredBSSLength": awcDot11DesiredBSSLength,
       "awcDot11EnetEncapsulationDefault": awcDot11EnetEncapsulationDefault,
       "awcDot11ForceReqFirmwareVersion": awcDot11ForceReqFirmwareVersion,
       "awcDot11BridgeSpacing": awcDot11BridgeSpacing,
       "awcDot11DesiredSSIDMaxAssociatedSTA": awcDot11DesiredSSIDMaxAssociatedSTA,
       "awcDot11DesiredSSIDNumAssociatedSTA": awcDot11DesiredSSIDNumAssociatedSTA,
       "awcDot11AuxiliarySSIDLength": awcDot11AuxiliarySSIDLength,
       "awcDot11MultipleSSIDPerBSSImplemented": awcDot11MultipleSSIDPerBSSImplemented,
       "awcDot11SymbolExtensionsImplemented": awcDot11SymbolExtensionsImplemented,
       "awcDot11SymbolExtensionsEnabled": awcDot11SymbolExtensionsEnabled,
       "awcDot11DesiredSSIDMicAlgorithm": awcDot11DesiredSSIDMicAlgorithm,
       "awcDot11DesiredSSIDWEPKeyPermuteAlgorithm": awcDot11DesiredSSIDWEPKeyPermuteAlgorithm,
       "awcDot11DesiredSSIDInfrastructureWGB": awcDot11DesiredSSIDInfrastructureWGB,
       "awcDot11DesiredSSIDDefaultPolId": awcDot11DesiredSSIDDefaultPolId,
       "awcDot11DesiredSSIDDefaultVlanId": awcDot11DesiredSSIDDefaultVlanId,
       "awcDot11DesiredSSIDEnableProxyMobileIP": awcDot11DesiredSSIDEnableProxyMobileIP,
       "awcDot11InfrastructureSSID": awcDot11InfrastructureSSID,
       "awcDot11QBSSElementImplemented": awcDot11QBSSElementImplemented,
       "awcDot11QBSSElementEnabled": awcDot11QBSSElementEnabled,
       "awcDot11InfrastructureSSIDExclusive": awcDot11InfrastructureSSIDExclusive,
       "awcDot11SendIGMPGeneralQuery": awcDot11SendIGMPGeneralQuery,
       "awcDot11NonRootMobility": awcDot11NonRootMobility,
       "awcDot11AuthenticationAlgorithmsTable": awcDot11AuthenticationAlgorithmsTable,
       "awcDot11AuthenticationAlgorithmsEntry": awcDot11AuthenticationAlgorithmsEntry,
       "awcDot11AuthenticationAlgorithmsIndex": awcDot11AuthenticationAlgorithmsIndex,
       "awcDot11AuthenticationRequireEAP": awcDot11AuthenticationRequireEAP,
       "awcDot11AuthenticationDefaultUcastAllowedToGoTo": awcDot11AuthenticationDefaultUcastAllowedToGoTo,
       "awcDot11WEPDefaultKeysTable": awcDot11WEPDefaultKeysTable,
       "awcDot11WEPDefaultKeysEntry": awcDot11WEPDefaultKeysEntry,
       "awcDot11WEPDefaultKeyIndex": awcDot11WEPDefaultKeyIndex,
       "awcDot11WEPDefaultKeyLen": awcDot11WEPDefaultKeyLen,
       "awcDot11WEPDefaultKeyValue": awcDot11WEPDefaultKeyValue,
       "awcDot11PrivacyTable": awcDot11PrivacyTable,
       "awcDot11PrivacyEntry": awcDot11PrivacyEntry,
       "awcDot11WEPDefaultKeyMaxIndex": awcDot11WEPDefaultKeyMaxIndex,
       "awcDot11AllowEncrypted": awcDot11AllowEncrypted,
       "awcDot11WEPKeyMaxLen": awcDot11WEPKeyMaxLen,
       "awcDot11LEAPUserName": awcDot11LEAPUserName,
       "awcDot11LEAPPassword": awcDot11LEAPPassword,
       "awcDot11DesiredBSSTable": awcDot11DesiredBSSTable,
       "awcDot11DesiredBSSEntry": awcDot11DesiredBSSEntry,
       "awcDot11DesiredBSSIndex": awcDot11DesiredBSSIndex,
       "awcDot11DesiredBSS": awcDot11DesiredBSS,
       "awcDot11AuxiliarySSIDTable": awcDot11AuxiliarySSIDTable,
       "awcDot11AuxiliarySSIDEntry": awcDot11AuxiliarySSIDEntry,
       "awcDot11AuxSSIDIndex": awcDot11AuxSSIDIndex,
       "awcDot11AuxSSID": awcDot11AuxSSID,
       "awcDot11AuxSSIDMaxAssociatedSTA": awcDot11AuxSSIDMaxAssociatedSTA,
       "awcDot11AuxSSIDNumAssociatedSTA": awcDot11AuxSSIDNumAssociatedSTA,
       "awcDot11AuxSSIDDefaultPolId": awcDot11AuxSSIDDefaultPolId,
       "awcDot11AuxSSIDDefaultVlanId": awcDot11AuxSSIDDefaultVlanId,
       "awcDot11AuxSSIDEnableProxyMobileIP": awcDot11AuxSSIDEnableProxyMobileIP,
       "awcDot11AuxSSIDAuthAlgTable": awcDot11AuxSSIDAuthAlgTable,
       "awcDot11AuxSSIDAuthAlgEntry": awcDot11AuxSSIDAuthAlgEntry,
       "awcDot11AuxSSIDAuthAlgIndex": awcDot11AuxSSIDAuthAlgIndex,
       "awcDot11AuxSSIDAuthAlgEnable": awcDot11AuxSSIDAuthAlgEnable,
       "awcDot11AuxSSIDAuthAlgRequireEAP": awcDot11AuxSSIDAuthAlgRequireEAP,
       "awcDot11AuxSSIDAuthAlgDefaultUcastAllowedToGoTo": awcDot11AuxSSIDAuthAlgDefaultUcastAllowedToGoTo,
       "awcDot11AssignedAIDTable": awcDot11AssignedAIDTable,
       "awcDot11AssignedAIDEntry": awcDot11AssignedAIDEntry,
       "awcDot11AssignedAID": awcDot11AssignedAID,
       "awcDot11AssignedSTA": awcDot11AssignedSTA,
       "awcDot11AccessPointCountersTable": awcDot11AccessPointCountersTable,
       "awcDot11AccessPointCountersEntry": awcDot11AccessPointCountersEntry,
       "awcDot11AssociatedStationCount": awcDot11AssociatedStationCount,
       "awcDot11AuthenticatedStationCount": awcDot11AuthenticatedStationCount,
       "awcDot11ReassociatedStationCount": awcDot11ReassociatedStationCount,
       "awcDot11RoamedStationCount": awcDot11RoamedStationCount,
       "awcDot11DeauthenticateCount": awcDot11DeauthenticateCount,
       "awcDot11DisassociateCount": awcDot11DisassociateCount,
       "awcDot11EncapPktsMMH": awcDot11EncapPktsMMH,
       "awcDot11DecapPktsMMH": awcDot11DecapPktsMMH,
       "awcDot11EncapErrorsMMH": awcDot11EncapErrorsMMH,
       "awcDot11DecapErrorsMMH": awcDot11DecapErrorsMMH,
       "awcDot11DecapExistsMMH": awcDot11DecapExistsMMH,
       "awcDot11DecapAccessMMH": awcDot11DecapAccessMMH,
       "awcDot11mac": awcDot11mac,
       "awcDot11CountersTable": awcDot11CountersTable,
       "awcDot11CountersEntry": awcDot11CountersEntry,
       "awcDot11TxDeferEnergyCount": awcDot11TxDeferEnergyCount,
       "awcDot11RxMacCrcErrorCount": awcDot11RxMacCrcErrorCount,
       "awcDot11SsidMismatchCount": awcDot11SsidMismatchCount,
       "awcDot11QoSTable": awcDot11QoSTable,
       "awcDot11QoSEntry": awcDot11QoSEntry,
       "awcDot11QoSCoS": awcDot11QoSCoS,
       "awcDot11QoSCWmin": awcDot11QoSCWmin,
       "awcDot11QoSCWmax": awcDot11QoSCWmax,
       "awcDot11res": awcDot11res,
       "awcDot11resAttribute": awcDot11resAttribute,
       "awcDot11ResourceInfoTable": awcDot11ResourceInfoTable,
       "awcDot11ResourceInfoEntry": awcDot11ResourceInfoEntry,
       "awcDot11FirmwareBootstrapVersion": awcDot11FirmwareBootstrapVersion,
       "awcDot11phy": awcDot11phy,
       "awcDot11PhyOperationTable": awcDot11PhyOperationTable,
       "awcDot11PhyOperationEntry": awcDot11PhyOperationEntry,
       "awcDot11CurrentCarrierSet": awcDot11CurrentCarrierSet,
       "awcDot11ModulationType": awcDot11ModulationType,
       "awcDot11PreambleType": awcDot11PreambleType,
       "awcDot11PHYType": awcDot11PHYType,
       "awcDot11PhyFHSSTable": awcDot11PhyFHSSTable,
       "awcDot11PhyFHSSEntry": awcDot11PhyFHSSEntry,
       "awcDot11Compatible3100": awcDot11Compatible3100,
       "awcDot11PhyDSSSTable": awcDot11PhyDSSSTable,
       "awcDot11PhyDSSSEntry": awcDot11PhyDSSSEntry,
       "awcDot11Compatible4500": awcDot11Compatible4500,
       "awcDot11ChannelAutoImplemented": awcDot11ChannelAutoImplemented,
       "awcDot11ChannelAutoEnabled": awcDot11ChannelAutoEnabled,
       "awcDot11CurrentChannel": awcDot11CurrentChannel,
       "awcDot11SupportedDataRatesPrivacyTable": awcDot11SupportedDataRatesPrivacyTable,
       "awcDot11SupportedDataRatesPrivacyEntry": awcDot11SupportedDataRatesPrivacyEntry,
       "awcDot11SupportedDataRatesPrivacyIndex": awcDot11SupportedDataRatesPrivacyIndex,
       "awcDot11SupportedDataRatesPrivacyValue": awcDot11SupportedDataRatesPrivacyValue,
       "awcDot11SupportedDataRatesPrivacyImplemented": awcDot11SupportedDataRatesPrivacyImplemented,
       "awcDot11ChanSelectTable": awcDot11ChanSelectTable,
       "awcDot11ChanSelectEntry": awcDot11ChanSelectEntry,
       "awcDot11ChanSelectChannel": awcDot11ChanSelectChannel,
       "awcDot11ChanSelectEnable": awcDot11ChanSelectEnable,
       "awcUserMgr": awcUserMgr,
       "userMgrConfigTable": userMgrConfigTable,
       "userMgrConfigEntry": userMgrConfigEntry,
       "userMgrUserIndex": userMgrUserIndex,
       "userMgrUserName": userMgrUserName,
       "userMgrPassword": userMgrPassword,
       "userMgrCapabilities": userMgrCapabilities,
       "userMgrStatus": userMgrStatus,
       "enableUserMgr": enableUserMgr,
       "allowBrowseWithoutLogin": allowBrowseWithoutLogin,
       "protectLegalPage": protectLegalPage,
       "awcHttpd": awcHttpd,
       "defaultWebRoot": defaultWebRoot,
       "defaultHelpRoot": defaultHelpRoot,
       "getWebUI": getWebUI,
       "cmdInvokeGetWebUI": cmdInvokeGetWebUI,
       "cmdStatusGetWebUI": cmdStatusGetWebUI,
       "awcHttpdPort": awcHttpdPort,
       "awcConsoleAutoApply": awcConsoleAutoApply,
       "awcDnsRes": awcDnsRes,
       "resolverDomain": resolverDomain,
       "resolverDomainSuffix": resolverDomainSuffix,
       "resolverDomainServerTable": resolverDomainServerTable,
       "resolverDomainServerEntry": resolverDomainServerEntry,
       "resolverDomainServerPriority": resolverDomainServerPriority,
       "resolverDomainServer": resolverDomainServer,
       "defaultResolverDomain": defaultResolverDomain,
       "defaultResolverDomainServerTable": defaultResolverDomainServerTable,
       "defaultResolverDomainServerEntry": defaultResolverDomainServerEntry,
       "defaultResolverDomainServerPriority": defaultResolverDomainServerPriority,
       "defaultResolverDomainServer": defaultResolverDomainServer,
       "awcSnmp": awcSnmp,
       "snmpTrapDest": snmpTrapDest,
       "snmpTrapCommunity": snmpTrapCommunity,
       "awcSntp": awcSntp,
       "defaultSntpServer": defaultSntpServer,
       "sntpServer": sntpServer,
       "awcForwardTbl": awcForwardTbl,
       "awcFtStatistics": awcFtStatistics,
       "awcFtMcastAddr": awcFtMcastAddr,
       "awcFtDsHost": awcFtDsHost,
       "awcFtBridgeHost": awcFtBridgeHost,
       "awcFtClientSTA": awcFtClientSTA,
       "awcFtClientSTASelf": awcFtClientSTASelf,
       "awcFtBridge": awcFtBridge,
       "awcFtBridgeSelf": awcFtBridgeSelf,
       "awcFtRepeater": awcFtRepeater,
       "awcFtRepeaterSelf": awcFtRepeaterSelf,
       "awcFtAccessPoint": awcFtAccessPoint,
       "awcFtBridgeRoot": awcFtBridgeRoot,
       "awcFtConfig": awcFtConfig,
       "awcFtMaxNumEntries": awcFtMaxNumEntries,
       "awcFtTimeoutSecUnknown": awcFtTimeoutSecUnknown,
       "awcFtTimeoutSecMcastAddr": awcFtTimeoutSecMcastAddr,
       "awcFtTimeoutSecDsHost": awcFtTimeoutSecDsHost,
       "awcFtTimeoutSecBridgeHost": awcFtTimeoutSecBridgeHost,
       "awcFtTimeoutSecClientSTA": awcFtTimeoutSecClientSTA,
       "awcFtTimeoutSecBridge": awcFtTimeoutSecBridge,
       "awcFtTimeoutSecRepeater": awcFtTimeoutSecRepeater,
       "awcFtTimeoutSecAccessPoint": awcFtTimeoutSecAccessPoint,
       "awcFtTimeoutSecBridgeRoot": awcFtTimeoutSecBridgeRoot,
       "awcFtEnableAwcTpFdbTable": awcFtEnableAwcTpFdbTable,
       "awcFtEnableMacAuthServer": awcFtEnableMacAuthServer,
       "awcFtRogueApAlertTimeout": awcFtRogueApAlertTimeout,
       "awcFtEnableMacOrEapAuth": awcFtEnableMacOrEapAuth,
       "awcFtDot1dTpFdbTableEnable": awcFtDot1dTpFdbTableEnable,
       "awcFtEnableMcastMapping": awcFtEnableMcastMapping,
       "awcTpFdbTable": awcTpFdbTable,
       "awcTpFdbEntry": awcTpFdbEntry,
       "awcTpFdbAddress": awcTpFdbAddress,
       "awcTpFdbClassID": awcTpFdbClassID,
       "awcTpFdbSrcPktsImmed": awcTpFdbSrcPktsImmed,
       "awcTpFdbSrcOctetsImmed": awcTpFdbSrcOctetsImmed,
       "awcTpFdbSrcErrorPktsImmed": awcTpFdbSrcErrorPktsImmed,
       "awcTpFdbSrcErrorOctetsImmed": awcTpFdbSrcErrorOctetsImmed,
       "awcTpFdbDestPktsImmed": awcTpFdbDestPktsImmed,
       "awcTpFdbDestOctetsImmed": awcTpFdbDestOctetsImmed,
       "awcTpFdbDestErrorPktsImmed": awcTpFdbDestErrorPktsImmed,
       "awcTpFdbDestErrorOctetsImmed": awcTpFdbDestErrorOctetsImmed,
       "awcTpFdbDestMaxRetryErrorsImmed": awcTpFdbDestMaxRetryErrorsImmed,
       "awcTpFdbIPv4Addr": awcTpFdbIPv4Addr,
       "awcTpFdbDdpTable": awcTpFdbDdpTable,
       "awcTpFdbDdpEntry": awcTpFdbDdpEntry,
       "awcTpFdbDdpAddress": awcTpFdbDdpAddress,
       "awcTpFdbDdpSysName": awcTpFdbDdpSysName,
       "awcTpFdbDdpProdDevID": awcTpFdbDdpProdDevID,
       "awcTpFdbDdpRadioDevID": awcTpFdbDdpRadioDevID,
       "awcTpFdbDdpSwVerMajor": awcTpFdbDdpSwVerMajor,
       "awcTpFdbDdpSwVerMinor": awcTpFdbDdpSwVerMinor,
       "awcTpFdbDdpSwVerBeta": awcTpFdbDdpSwVerBeta,
       "awcTpFdbDdpUptime": awcTpFdbDdpUptime,
       "awcTpFdbDdpNumAnnounceSent": awcTpFdbDdpNumAnnounceSent,
       "awcTpFdbDdpNumAssociated": awcTpFdbDdpNumAssociated,
       "awcTpFdbDdpLoad": awcTpFdbDdpLoad,
       "awcTpFdbDdpDistFromDS": awcTpFdbDdpDistFromDS,
       "awcDot11TpFdbTable": awcDot11TpFdbTable,
       "awcDot11TpFdbEntry": awcDot11TpFdbEntry,
       "awcDot11TpFdbAddress": awcDot11TpFdbAddress,
       "awcDot11TpFdbAID": awcDot11TpFdbAID,
       "awcDot11TpFdbClientState": awcDot11TpFdbClientState,
       "awcDot11TpFdbTxShortRetries": awcDot11TpFdbTxShortRetries,
       "awcDot11TpFdbTxLongRetries": awcDot11TpFdbTxLongRetries,
       "awcDot11TpFdbLatestTxShortRetries": awcDot11TpFdbLatestTxShortRetries,
       "awcDot11TpFdbLatestTxLongRetries": awcDot11TpFdbLatestTxLongRetries,
       "awcDot11TpFdbRxWEPErrors": awcDot11TpFdbRxWEPErrors,
       "awcDot11TpFdbLatestRxSignalStrength": awcDot11TpFdbLatestRxSignalStrength,
       "awcDot11TpFdbLatestRxSignalQuality": awcDot11TpFdbLatestRxSignalQuality,
       "awcDot11TpFdbCapabilities": awcDot11TpFdbCapabilities,
       "awcDot11TpFdbListenInterval": awcDot11TpFdbListenInterval,
       "awcDot11TpFdbSupportedDataRates": awcDot11TpFdbSupportedDataRates,
       "awcDot11TpFdbPreferredTxRate": awcDot11TpFdbPreferredTxRate,
       "awcDot11TpFdbCurrentBSS": awcDot11TpFdbCurrentBSS,
       "awcDot11TpFdbSSID": awcDot11TpFdbSSID,
       "awcDot11TpFdbVlanId": awcDot11TpFdbVlanId,
       "awcDot1dTpPortTable": awcDot1dTpPortTable,
       "awcDot1dTpPortEntry": awcDot1dTpPortEntry,
       "awcDot1dTpPortDefaultUcastAllowedToGoTo": awcDot1dTpPortDefaultUcastAllowedToGoTo,
       "awcDot1dTpPortDefaultNUcastAllowedToGoTo": awcDot1dTpPortDefaultNUcastAllowedToGoTo,
       "awcDot1dTpPortMaxNUcastPerSecond": awcDot1dTpPortMaxNUcastPerSecond,
       "awcDot1dTpPortDefaultInEthertypeFilterId": awcDot1dTpPortDefaultInEthertypeFilterId,
       "awcDot1dTpPortDefaultOutEthertypeFilterId": awcDot1dTpPortDefaultOutEthertypeFilterId,
       "awcDot1dTpPortDefaultInIpProtoFilterId": awcDot1dTpPortDefaultInIpProtoFilterId,
       "awcDot1dTpPortDefaultOutIpProtoFilterId": awcDot1dTpPortDefaultOutIpProtoFilterId,
       "awcDot1dTpPortDefaultInIpPortFilterId": awcDot1dTpPortDefaultInIpPortFilterId,
       "awcDot1dTpPortDefaultOutIpPortFilterId": awcDot1dTpPortDefaultOutIpPortFilterId,
       "awcTpFdbAlertTable": awcTpFdbAlertTable,
       "awcTpFdbAlertEntry": awcTpFdbAlertEntry,
       "awcTpFdbAlertAddress": awcTpFdbAlertAddress,
       "awcTpFdbFromAlertSrcPktsImmed": awcTpFdbFromAlertSrcPktsImmed,
       "awcTpFdbFromAlertSrcOctetsImmed": awcTpFdbFromAlertSrcOctetsImmed,
       "awcTpFdbToAlertDestPktsImmed": awcTpFdbToAlertDestPktsImmed,
       "awcTpFdbToAlertDestOctetsImmed": awcTpFdbToAlertDestOctetsImmed,
       "awcTpFdbAlertSentAlertTypePktsImmed": awcTpFdbAlertSentAlertTypePktsImmed,
       "awcTpFdbAlertSentAlertTypeOctetsImmed": awcTpFdbAlertSentAlertTypeOctetsImmed,
       "awcTpFdbAlertRcvdAlertTypePktsImmed": awcTpFdbAlertRcvdAlertTypePktsImmed,
       "awcTpFdbAlertRcvdAlertTypeOctetsImmed": awcTpFdbAlertRcvdAlertTypeOctetsImmed,
       "awcRipConfig": awcRipConfig,
       "awcEventLog": awcEventLog,
       "awcEventOffsetGMT": awcEventOffsetGMT,
       "awcEventUseDaylightSavingsTime": awcEventUseDaylightSavingsTime,
       "awcEventTimestampGMT": awcEventTimestampGMT,
       "awcEventUptimeModifiedGMT": awcEventUptimeModifiedGMT,
       "awcEventDisplayWallClockTime": awcEventDisplayWallClockTime,
       "awcEventDisplayUptimeAscending": awcEventDisplayUptimeAscending,
       "awcEventDetailDefault": awcEventDetailDefault,
       "awcEventSeverityDispConsole": awcEventSeverityDispConsole,
       "awcEventSeverityDispHtmlGUI": awcEventSeverityDispHtmlGUI,
       "awcEventSeverityDispHtmlConsole": awcEventSeverityDispHtmlConsole,
       "awcEventAlertSNMP": awcEventAlertSNMP,
       "awcEventAlertSyslog": awcEventAlertSyslog,
       "awcEventStatistics": awcEventStatistics,
       "awcEventCntSeverityNULL": awcEventCntSeverityNULL,
       "awcEventCntSeveritySilent": awcEventCntSeveritySilent,
       "awcEventCntSeveritySystemFatal": awcEventCntSeveritySystemFatal,
       "awcEventCntSeverityProtocolFatal": awcEventCntSeverityProtocolFatal,
       "awcEventCntSeverityPortFatal": awcEventCntSeverityPortFatal,
       "awcEventCntSeveritySystemAlert": awcEventCntSeveritySystemAlert,
       "awcEventCntSeverityProtocolAlert": awcEventCntSeverityProtocolAlert,
       "awcEventCntSeverityPortAlert": awcEventCntSeverityPortAlert,
       "awcEventCntSeverityExternalAlert": awcEventCntSeverityExternalAlert,
       "awcEventCntSeveritySystemWarning": awcEventCntSeveritySystemWarning,
       "awcEventCntSeverityProtocolWarning": awcEventCntSeverityProtocolWarning,
       "awcEventCntSeverityPortWarning": awcEventCntSeverityPortWarning,
       "awcEventCntSeverityExternalWarning": awcEventCntSeverityExternalWarning,
       "awcEventCntSeveritySystemInfo": awcEventCntSeveritySystemInfo,
       "awcEventCntSeverityProtocolInfo": awcEventCntSeverityProtocolInfo,
       "awcEventCntSeverityPortInfo": awcEventCntSeverityPortInfo,
       "awcEventCntSeverityExternalInfo": awcEventCntSeverityExternalInfo,
       "awcEventDisposition": awcEventDisposition,
       "awcEventDispSeverityNULL": awcEventDispSeverityNULL,
       "awcEventDispSeveritySilent": awcEventDispSeveritySilent,
       "awcEventDispSeveritySystemFatal": awcEventDispSeveritySystemFatal,
       "awcEventDispSeverityProtocolFatal": awcEventDispSeverityProtocolFatal,
       "awcEventDispSeverityPortFatal": awcEventDispSeverityPortFatal,
       "awcEventDispSeveritySystemAlert": awcEventDispSeveritySystemAlert,
       "awcEventDispSeverityProtocolAlert": awcEventDispSeverityProtocolAlert,
       "awcEventDispSeverityPortAlert": awcEventDispSeverityPortAlert,
       "awcEventDispSeverityExternalAlert": awcEventDispSeverityExternalAlert,
       "awcEventDispSeveritySystemWarning": awcEventDispSeveritySystemWarning,
       "awcEventDispSeverityProtocolWarning": awcEventDispSeverityProtocolWarning,
       "awcEventDispSeverityPortWarning": awcEventDispSeverityPortWarning,
       "awcEventDispSeverityExternalWarning": awcEventDispSeverityExternalWarning,
       "awcEventDispSeveritySystemInfo": awcEventDispSeveritySystemInfo,
       "awcEventDispSeverityProtocolInfo": awcEventDispSeverityProtocolInfo,
       "awcEventDispSeverityPortInfo": awcEventDispSeverityPortInfo,
       "awcEventDispSeverityExternalInfo": awcEventDispSeverityExternalInfo,
       "awcEventSyslogAddr": awcEventSyslogAddr,
       "awcEventSyslogFacility": awcEventSyslogFacility,
       "awcEventTraceStationSeverity": awcEventTraceStationSeverity,
       "awcEventTraceLogSize": awcEventTraceLogSize,
       "awcEventTracePacketLen": awcEventTracePacketLen,
       "awcEventTable": awcEventTable,
       "awcEventEntry": awcEventEntry,
       "awcEventID": awcEventID,
       "awcEventTime": awcEventTime,
       "awcEventSeverity": awcEventSeverity,
       "awcEventDescription": awcEventDescription,
       "awcEventType": awcEventType,
       "awcEventUseCiscoFormat": awcEventUseCiscoFormat,
       "awcDot11AuthenticateFailDisposition": awcDot11AuthenticateFailDisposition,
       "awcDot11DeauthenticateDisposition": awcDot11DeauthenticateDisposition,
       "awcDot11DisassociateDisposition": awcDot11DisassociateDisposition,
       "awcEtherMIB": awcEtherMIB,
       "awcEtherIfSpeedSelect": awcEtherIfSpeedSelect,
       "awcEtherDuplex": awcEtherDuplex,
       "awcEtherCamSize": awcEtherCamSize,
       "awcEtherEnableSwCam": awcEtherEnableSwCam,
       "awcEtherForcePortUnblock": awcEtherForcePortUnblock,
       "awcEtherLostEthernetSeconds": awcEtherLostEthernetSeconds,
       "awcEtherLostEthernetAction": awcEtherLostEthernetAction,
       "awcEtherLostEthernetSSID": awcEtherLostEthernetSSID,
       "awcPolicyGroups": awcPolicyGroups,
       "awcPolGrpTable": awcPolGrpTable,
       "awcPolGrpEntry": awcPolGrpEntry,
       "awcPolGrpId": awcPolGrpId,
       "awcPolGrpName": awcPolGrpName,
       "awcPolGrpStatus": awcPolGrpStatus,
       "awcPolGrpInEthertypeFilterId": awcPolGrpInEthertypeFilterId,
       "awcPolGrpOutEthertypeFilterId": awcPolGrpOutEthertypeFilterId,
       "awcPolGrpInIpProtoFilterId": awcPolGrpInIpProtoFilterId,
       "awcPolGrpOutIpProtoFilterId": awcPolGrpOutIpProtoFilterId,
       "awcPolGrpInIpPortFilterId": awcPolGrpInIpPortFilterId,
       "awcPolGrpOutIpPortFilterId": awcPolGrpOutIpPortFilterId,
       "awcDscpToCosMapEnable": awcDscpToCosMapEnable,
       "awcDscpToCosMapTable": awcDscpToCosMapTable,
       "awcDscpToCosMapEntry": awcDscpToCosMapEntry,
       "awcDscpToCosMapDscp": awcDscpToCosMapDscp,
       "awcDscpToCosMapCos": awcDscpToCosMapCos,
       "awcDdpIAPP": awcDdpIAPP,
       "awcIappMcastIpAddr": awcIappMcastIpAddr,
       "awcIappPort": awcIappPort,
       "awcP802dot1XVersion": awcP802dot1XVersion,
       "awcHotStandby": awcHotStandby,
       "awcHotStandbyMACAddr": awcHotStandbyMACAddr,
       "awcHotStandbyPollingFrequency": awcHotStandbyPollingFrequency,
       "awcHotStandbyPollingTimeOut": awcHotStandbyPollingTimeOut,
       "awcHotStandbyInHotStandby": awcHotStandbyInHotStandby,
       "awcHotStandbyState": awcHotStandbyState,
       "awcHotStandbyStatus": awcHotStandbyStatus,
       "awcAaa": awcAaa,
       "awcAaaServerTable": awcAaaServerTable,
       "awcAaaServerEntry": awcAaaServerEntry,
       "awcAaaServerPriority": awcAaaServerPriority,
       "awcAaaServerProtocol": awcAaaServerProtocol,
       "awcAaaServerName": awcAaaServerName,
       "awcAaaServerPort": awcAaaServerPort,
       "awcAaaServerTimeout": awcAaaServerTimeout,
       "awcAaaClientName": awcAaaClientName,
       "awcAaaServerSharedSecret": awcAaaServerSharedSecret,
       "awcAaaServer8021xCapabilityEnabled": awcAaaServer8021xCapabilityEnabled,
       "awcAaaServerMacAddrAuthEnabled": awcAaaServerMacAddrAuthEnabled,
       "awcAaaServerAdminAuthEnabled": awcAaaServerAdminAuthEnabled,
       "awcAaaServerMipAuthEnabled": awcAaaServerMipAuthEnabled,
       "awcAaaServerMaxRetransmission": awcAaaServerMaxRetransmission,
       "awcAcctServerTable": awcAcctServerTable,
       "awcAcctServerEntry": awcAcctServerEntry,
       "awcAcctServerPriority": awcAcctServerPriority,
       "awcAcctServerProtocol": awcAcctServerProtocol,
       "awcAcctServerName": awcAcctServerName,
       "awcAcctServerPort": awcAcctServerPort,
       "awcAcctServerTimeout": awcAcctServerTimeout,
       "awcAcctServerUpdateEnable": awcAcctServerUpdateEnable,
       "awcAcctServerUpdateDelay": awcAcctServerUpdateDelay,
       "awcAcctClientName": awcAcctClientName,
       "awcAcctSecureEnabled": awcAcctSecureEnabled,
       "awcAcctGeneralEnabled": awcAcctGeneralEnabled,
       "awcAcctServerSharedSecret": awcAcctServerSharedSecret,
       "awcAcctServerMaxRetransmission": awcAcctServerMaxRetransmission,
       "awcAcctConfig": awcAcctConfig,
       "awcAcctEnable": awcAcctEnable,
       "awcAcctStopDelayEnable": awcAcctStopDelayEnable,
       "awcAcctStopDelayTime": awcAcctStopDelayTime,
       "awcAaaAuthConfig": awcAaaAuthConfig,
       "awcAaaServerPrimaryReattemptPeriod": awcAaaServerPrimaryReattemptPeriod,
       "awcAaaServerDot1xAuthCurrent": awcAaaServerDot1xAuthCurrent,
       "awcAaaServerMacAddrAuthCurrent": awcAaaServerMacAddrAuthCurrent,
       "awcAaaServerAdminAuthCurrent": awcAaaServerAdminAuthCurrent,
       "awcAaaServerMipAuthCurrent": awcAaaServerMipAuthCurrent,
       "awcProtocolFilters": awcProtocolFilters,
       "awcPrFltEthertypeSetTable": awcPrFltEthertypeSetTable,
       "awcPrFltEthertypeSetEntry": awcPrFltEthertypeSetEntry,
       "awcPfEtSetId": awcPfEtSetId,
       "awcPfEtSetName": awcPfEtSetName,
       "awcPfEtDefaultDisposition": awcPfEtDefaultDisposition,
       "awcPfEtDefaultUcastTimeToLive": awcPfEtDefaultUcastTimeToLive,
       "awcPfEtDefaultNUcastTimeToLive": awcPfEtDefaultNUcastTimeToLive,
       "awcPfEtSetStatus": awcPfEtSetStatus,
       "awcPrFltEthertypeTable": awcPrFltEthertypeTable,
       "awcPrFltEthertypeEntry": awcPrFltEthertypeEntry,
       "awcPfEtEthertype": awcPfEtEthertype,
       "awcPfEtDisposition": awcPfEtDisposition,
       "awcPfEtUserPriority": awcPfEtUserPriority,
       "awcPfEtUcastTimeToLive": awcPfEtUcastTimeToLive,
       "awcPfEtNUcastTimeToLive": awcPfEtNUcastTimeToLive,
       "awcPfEtAlert": awcPfEtAlert,
       "awcPfEtStatus": awcPfEtStatus,
       "awcPrFltIpProtocolSetTable": awcPrFltIpProtocolSetTable,
       "awcPrFltIpProtocolSetEntry": awcPrFltIpProtocolSetEntry,
       "awcPfIppSetId": awcPfIppSetId,
       "awcPfIppSetName": awcPfIppSetName,
       "awcPfIppDefaultDisposition": awcPfIppDefaultDisposition,
       "awcPfIppDefaultUcastTimeToLive": awcPfIppDefaultUcastTimeToLive,
       "awcPfIppDefaultNUcastTimeToLive": awcPfIppDefaultNUcastTimeToLive,
       "awcPfIppSetStatus": awcPfIppSetStatus,
       "awcPrFltIpProtocolTable": awcPrFltIpProtocolTable,
       "awcPrFltIpProtocolEntry": awcPrFltIpProtocolEntry,
       "awcPfIppIpProtocol": awcPfIppIpProtocol,
       "awcPfIppDisposition": awcPfIppDisposition,
       "awcPfIppUserPriority": awcPfIppUserPriority,
       "awcPfIppUcastTimeToLive": awcPfIppUcastTimeToLive,
       "awcPfIppNUcastTimeToLive": awcPfIppNUcastTimeToLive,
       "awcPfIppAlert": awcPfIppAlert,
       "awcPfIppStatus": awcPfIppStatus,
       "awcPrFltIpPortSetTable": awcPrFltIpPortSetTable,
       "awcPrFltIpPortSetEntry": awcPrFltIpPortSetEntry,
       "awcPfIptSetId": awcPfIptSetId,
       "awcPfIptSetName": awcPfIptSetName,
       "awcPfIptDefaultDisposition": awcPfIptDefaultDisposition,
       "awcPfIptDefaultUcastTimeToLive": awcPfIptDefaultUcastTimeToLive,
       "awcPfIptDefaultNUcastTimeToLive": awcPfIptDefaultNUcastTimeToLive,
       "awcPfIptSetStatus": awcPfIptSetStatus,
       "awcPrFltIpPortTable": awcPrFltIpPortTable,
       "awcPrFltIpPortEntry": awcPrFltIpPortEntry,
       "awcPfIptIpPort": awcPfIptIpPort,
       "awcPfIptDisposition": awcPfIptDisposition,
       "awcPfIptUserPriority": awcPfIptUserPriority,
       "awcPfIptUcastTimeToLive": awcPfIptUcastTimeToLive,
       "awcPfIptNUcastTimeToLive": awcPfIptNUcastTimeToLive,
       "awcPfIptAlert": awcPfIptAlert,
       "awcPfIptStatus": awcPfIptStatus,
       "awcMobileIP": awcMobileIP,
       "enableMobileIP": enableMobileIP,
       "awcprimAAP": awcprimAAP,
       "awcsec1AAP": awcsec1AAP,
       "awcsec2AAP": awcsec2AAP,
       "mipSATable": mipSATable,
       "mipSAEntry": mipSAEntry,
       "mipSAIpStart": mipSAIpStart,
       "mipSAIpEnd": mipSAIpEnd,
       "mipSAGroupSPI": mipSAGroupSPI,
       "mipSAGroupKey": mipSAGroupKey,
       "mipSAStatus": mipSAStatus,
       "awcmipDebug": awcmipDebug,
       "awcVxConformance": awcVxConformance,
       "awcVxCompliances": awcVxCompliances,
       "awcVxCompliance": awcVxCompliance,
       "awcVxGroups": awcVxGroups,
       "awcSystemGroup": awcSystemGroup,
       "bootconfigVxGroup": bootconfigVxGroup,
       "awcSerialDevGroup": awcSerialDevGroup,
       "awcFtpGroup": awcFtpGroup,
       "awcIfTableGroup": awcIfTableGroup,
       "awc802dot11Group": awc802dot11Group,
       "awcUserMgrGroup": awcUserMgrGroup,
       "awcHttpdGroup": awcHttpdGroup,
       "awcDnsResGroup": awcDnsResGroup,
       "awcSnmpGroup": awcSnmpGroup,
       "awcSntpGroup": awcSntpGroup,
       "awcForwardTblGroup": awcForwardTblGroup,
       "awcEventLogGroup": awcEventLogGroup,
       "awcEtherMIBGroup": awcEtherMIBGroup,
       "awcPolicyGroupsGroup": awcPolicyGroupsGroup,
       "awcDdpIAPPGroup": awcDdpIAPPGroup,
       "awcHotStandbyGroup": awcHotStandbyGroup,
       "awcAaaGroup": awcAaaGroup,
       "awcProtocolFiltersGroup": awcProtocolFiltersGroup,
       "awcMobileIpGroup": awcMobileIpGroup,
       "awcEthernetLostGroup": awcEthernetLostGroup,
       "awc802dot11GroupExt1": awc802dot11GroupExt1,
       "awcForwardTblGroupExt1": awcForwardTblGroupExt1,
       "awcTrapLogGroup": awcTrapLogGroup,
       "awcTrapLog": awcTrapLog}
)
