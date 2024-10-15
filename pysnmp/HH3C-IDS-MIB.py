# SNMP MIB module (HH3C-IDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-IDS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:31 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hh3cIDSMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cIds_ObjectIdentity = ObjectIdentity
hh3cIds = _Hh3cIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47)
)
_Hh3cIDSTrapGroup_ObjectIdentity = ObjectIdentity
hh3cIDSTrapGroup = _Hh3cIDSTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1)
)
_Hh3cIDSTrapInfo_ObjectIdentity = ObjectIdentity
hh3cIDSTrapInfo = _Hh3cIDSTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1)
)
_Hh3cIDSTrapIPFragmentQueueLen_Type = Unsigned32
_Hh3cIDSTrapIPFragmentQueueLen_Object = MibScalar
hh3cIDSTrapIPFragmentQueueLen = _Hh3cIDSTrapIPFragmentQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1, 1),
    _Hh3cIDSTrapIPFragmentQueueLen_Type()
)
hh3cIDSTrapIPFragmentQueueLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIDSTrapIPFragmentQueueLen.setStatus("current")
_Hh3cIDSTrapStatSessionTabLen_Type = Unsigned32
_Hh3cIDSTrapStatSessionTabLen_Object = MibScalar
hh3cIDSTrapStatSessionTabLen = _Hh3cIDSTrapStatSessionTabLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1, 2),
    _Hh3cIDSTrapStatSessionTabLen_Type()
)
hh3cIDSTrapStatSessionTabLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIDSTrapStatSessionTabLen.setStatus("current")
_Hh3cIDSTrapIPAddressType_Type = InetAddressType
_Hh3cIDSTrapIPAddressType_Object = MibScalar
hh3cIDSTrapIPAddressType = _Hh3cIDSTrapIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1, 3),
    _Hh3cIDSTrapIPAddressType_Type()
)
hh3cIDSTrapIPAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIDSTrapIPAddressType.setStatus("current")
_Hh3cIDSTrapIPAddress_Type = InetAddress
_Hh3cIDSTrapIPAddress_Object = MibScalar
hh3cIDSTrapIPAddress = _Hh3cIDSTrapIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1, 4),
    _Hh3cIDSTrapIPAddress_Type()
)
hh3cIDSTrapIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIDSTrapIPAddress.setStatus("current")


class _Hh3cIDSTrapUserName_Type(OctetString):
    """Custom type hh3cIDSTrapUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cIDSTrapUserName_Type.__name__ = "OctetString"
_Hh3cIDSTrapUserName_Object = MibScalar
hh3cIDSTrapUserName = _Hh3cIDSTrapUserName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1, 5),
    _Hh3cIDSTrapUserName_Type()
)
hh3cIDSTrapUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIDSTrapUserName.setStatus("current")


class _Hh3cIDSTrapLoginType_Type(Integer32):
    """Custom type hh3cIDSTrapLoginType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ssh", 2),
          ("telnet", 1),
          ("web", 3))
    )


_Hh3cIDSTrapLoginType_Type.__name__ = "Integer32"
_Hh3cIDSTrapLoginType_Object = MibScalar
hh3cIDSTrapLoginType = _Hh3cIDSTrapLoginType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1, 6),
    _Hh3cIDSTrapLoginType_Type()
)
hh3cIDSTrapLoginType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIDSTrapLoginType.setStatus("current")


class _Hh3cIDSTrapUpgradeType_Type(Integer32):
    """Custom type hh3cIDSTrapUpgradeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crb", 2),
          ("programme", 1),
          ("vrb", 3))
    )


_Hh3cIDSTrapUpgradeType_Type.__name__ = "Integer32"
_Hh3cIDSTrapUpgradeType_Object = MibScalar
hh3cIDSTrapUpgradeType = _Hh3cIDSTrapUpgradeType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1, 7),
    _Hh3cIDSTrapUpgradeType_Type()
)
hh3cIDSTrapUpgradeType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIDSTrapUpgradeType.setStatus("current")


class _Hh3cIDSTrapCRLName_Type(OctetString):
    """Custom type hh3cIDSTrapCRLName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cIDSTrapCRLName_Type.__name__ = "OctetString"
_Hh3cIDSTrapCRLName_Object = MibScalar
hh3cIDSTrapCRLName = _Hh3cIDSTrapCRLName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1, 8),
    _Hh3cIDSTrapCRLName_Type()
)
hh3cIDSTrapCRLName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIDSTrapCRLName.setStatus("current")


class _Hh3cIDSTrapCertName_Type(OctetString):
    """Custom type hh3cIDSTrapCertName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cIDSTrapCertName_Type.__name__ = "OctetString"
_Hh3cIDSTrapCertName_Object = MibScalar
hh3cIDSTrapCertName = _Hh3cIDSTrapCertName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1, 9),
    _Hh3cIDSTrapCertName_Type()
)
hh3cIDSTrapCertName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIDSTrapCertName.setStatus("current")
_Hh3cIDSTrapDetectRuleID_Type = Unsigned32
_Hh3cIDSTrapDetectRuleID_Object = MibScalar
hh3cIDSTrapDetectRuleID = _Hh3cIDSTrapDetectRuleID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1, 10),
    _Hh3cIDSTrapDetectRuleID_Type()
)
hh3cIDSTrapDetectRuleID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIDSTrapDetectRuleID.setStatus("current")
_Hh3cIDSTrapEngineID_Type = Integer32
_Hh3cIDSTrapEngineID_Object = MibScalar
hh3cIDSTrapEngineID = _Hh3cIDSTrapEngineID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1, 11),
    _Hh3cIDSTrapEngineID_Type()
)
hh3cIDSTrapEngineID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIDSTrapEngineID.setStatus("current")


class _Hh3cIDSTrapFileName_Type(OctetString):
    """Custom type hh3cIDSTrapFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hh3cIDSTrapFileName_Type.__name__ = "OctetString"
_Hh3cIDSTrapFileName_Object = MibScalar
hh3cIDSTrapFileName = _Hh3cIDSTrapFileName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1, 12),
    _Hh3cIDSTrapFileName_Type()
)
hh3cIDSTrapFileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIDSTrapFileName.setStatus("current")
_Hh3cIDSTrapCfgLineInFile_Type = Unsigned32
_Hh3cIDSTrapCfgLineInFile_Object = MibScalar
hh3cIDSTrapCfgLineInFile = _Hh3cIDSTrapCfgLineInFile_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1, 13),
    _Hh3cIDSTrapCfgLineInFile_Type()
)
hh3cIDSTrapCfgLineInFile.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIDSTrapCfgLineInFile.setStatus("current")


class _Hh3cIDSTrapReasonForError_Type(OctetString):
    """Custom type hh3cIDSTrapReasonForError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hh3cIDSTrapReasonForError_Type.__name__ = "OctetString"
_Hh3cIDSTrapReasonForError_Object = MibScalar
hh3cIDSTrapReasonForError = _Hh3cIDSTrapReasonForError_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1, 14),
    _Hh3cIDSTrapReasonForError_Type()
)
hh3cIDSTrapReasonForError.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIDSTrapReasonForError.setStatus("current")
_Hh3cIDSTrap_ObjectIdentity = ObjectIdentity
hh3cIDSTrap = _Hh3cIDSTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2)
)
_Hh3cIDSTrapPrefix_ObjectIdentity = ObjectIdentity
hh3cIDSTrapPrefix = _Hh3cIDSTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2, 0)
)

# Managed Objects groups


# Notification objects

hh3cIDSTrapIPFragQueueFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2, 0, 1)
)
hh3cIDSTrapIPFragQueueFull.setObjects(
      *(("HH3C-IDS-MIB", "hh3cIDSTrapIPFragmentQueueLen"),
        ("HH3C-IDS-MIB", "hh3cIDSTrapReasonForError"))
)
if mibBuilder.loadTexts:
    hh3cIDSTrapIPFragQueueFull.setStatus(
        "current"
    )

hh3cIDSTrapStatSessTabFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2, 0, 2)
)
hh3cIDSTrapStatSessTabFull.setObjects(
      *(("HH3C-IDS-MIB", "hh3cIDSTrapStatSessionTabLen"),
        ("HH3C-IDS-MIB", "hh3cIDSTrapReasonForError"))
)
if mibBuilder.loadTexts:
    hh3cIDSTrapStatSessTabFull.setStatus(
        "current"
    )

hh3cIDSTrapDetectRuleParseFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2, 0, 3)
)
hh3cIDSTrapDetectRuleParseFail.setObjects(
      *(("HH3C-IDS-MIB", "hh3cIDSTrapDetectRuleID"),
        ("HH3C-IDS-MIB", "hh3cIDSTrapEngineID"),
        ("HH3C-IDS-MIB", "hh3cIDSTrapReasonForError"))
)
if mibBuilder.loadTexts:
    hh3cIDSTrapDetectRuleParseFail.setStatus(
        "current"
    )

hh3cIDSTrapDBConnLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2, 0, 4)
)
hh3cIDSTrapDBConnLost.setObjects(
      *(("HH3C-IDS-MIB", "hh3cIDSTrapIPAddressType"),
        ("HH3C-IDS-MIB", "hh3cIDSTrapIPAddress"),
        ("HH3C-IDS-MIB", "hh3cIDSTrapReasonForError"))
)
if mibBuilder.loadTexts:
    hh3cIDSTrapDBConnLost.setStatus(
        "current"
    )

hh3cIDSTrapCRLNeedUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2, 0, 5)
)
hh3cIDSTrapCRLNeedUpdate.setObjects(
      *(("HH3C-IDS-MIB", "hh3cIDSTrapCRLName"),
        ("HH3C-IDS-MIB", "hh3cIDSTrapReasonForError"))
)
if mibBuilder.loadTexts:
    hh3cIDSTrapCRLNeedUpdate.setStatus(
        "current"
    )

hh3cIDSTrapCertOverdue = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2, 0, 6)
)
hh3cIDSTrapCertOverdue.setObjects(
      *(("HH3C-IDS-MIB", "hh3cIDSTrapCertName"),
        ("HH3C-IDS-MIB", "hh3cIDSTrapReasonForError"))
)
if mibBuilder.loadTexts:
    hh3cIDSTrapCertOverdue.setStatus(
        "current"
    )

hh3cIDSTrapTooManyLoginFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2, 0, 7)
)
hh3cIDSTrapTooManyLoginFail.setObjects(
      *(("HH3C-IDS-MIB", "hh3cIDSTrapUserName"),
        ("HH3C-IDS-MIB", "hh3cIDSTrapIPAddressType"),
        ("HH3C-IDS-MIB", "hh3cIDSTrapIPAddress"),
        ("HH3C-IDS-MIB", "hh3cIDSTrapLoginType"),
        ("HH3C-IDS-MIB", "hh3cIDSTrapReasonForError"))
)
if mibBuilder.loadTexts:
    hh3cIDSTrapTooManyLoginFail.setStatus(
        "current"
    )

hh3cIDSTrapUpgradeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2, 0, 8)
)
hh3cIDSTrapUpgradeError.setObjects(
      *(("HH3C-IDS-MIB", "hh3cIDSTrapUpgradeType"),
        ("HH3C-IDS-MIB", "hh3cIDSTrapReasonForError"))
)
if mibBuilder.loadTexts:
    hh3cIDSTrapUpgradeError.setStatus(
        "current"
    )

hh3cIDSTrapFileAccessError = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2, 0, 9)
)
hh3cIDSTrapFileAccessError.setObjects(
      *(("HH3C-IDS-MIB", "hh3cIDSTrapFileName"),
        ("HH3C-IDS-MIB", "hh3cIDSTrapReasonForError"))
)
if mibBuilder.loadTexts:
    hh3cIDSTrapFileAccessError.setStatus(
        "current"
    )

hh3cIDSTrapConsArithMemLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2, 0, 10)
)
hh3cIDSTrapConsArithMemLow.setObjects(
    ("HH3C-IDS-MIB", "hh3cIDSTrapReasonForError")
)
if mibBuilder.loadTexts:
    hh3cIDSTrapConsArithMemLow.setStatus(
        "current"
    )

hh3cIDSTrapSSRAMOperFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2, 0, 11)
)
hh3cIDSTrapSSRAMOperFail.setObjects(
    ("HH3C-IDS-MIB", "hh3cIDSTrapReasonForError")
)
if mibBuilder.loadTexts:
    hh3cIDSTrapSSRAMOperFail.setStatus(
        "current"
    )

hh3cIDSTrapPacketProcessDisorder = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2, 0, 12)
)
hh3cIDSTrapPacketProcessDisorder.setObjects(
    ("HH3C-IDS-MIB", "hh3cIDSTrapReasonForError")
)
if mibBuilder.loadTexts:
    hh3cIDSTrapPacketProcessDisorder.setStatus(
        "current"
    )

hh3cIDSTrapCfgFileFormatError = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2, 0, 13)
)
hh3cIDSTrapCfgFileFormatError.setObjects(
      *(("HH3C-IDS-MIB", "hh3cIDSTrapFileName"),
        ("HH3C-IDS-MIB", "hh3cIDSTrapCfgLineInFile"))
)
if mibBuilder.loadTexts:
    hh3cIDSTrapCfgFileFormatError.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-IDS-MIB",
    **{"hh3cIds": hh3cIds,
       "hh3cIDSMib": hh3cIDSMib,
       "hh3cIDSTrapGroup": hh3cIDSTrapGroup,
       "hh3cIDSTrapInfo": hh3cIDSTrapInfo,
       "hh3cIDSTrapIPFragmentQueueLen": hh3cIDSTrapIPFragmentQueueLen,
       "hh3cIDSTrapStatSessionTabLen": hh3cIDSTrapStatSessionTabLen,
       "hh3cIDSTrapIPAddressType": hh3cIDSTrapIPAddressType,
       "hh3cIDSTrapIPAddress": hh3cIDSTrapIPAddress,
       "hh3cIDSTrapUserName": hh3cIDSTrapUserName,
       "hh3cIDSTrapLoginType": hh3cIDSTrapLoginType,
       "hh3cIDSTrapUpgradeType": hh3cIDSTrapUpgradeType,
       "hh3cIDSTrapCRLName": hh3cIDSTrapCRLName,
       "hh3cIDSTrapCertName": hh3cIDSTrapCertName,
       "hh3cIDSTrapDetectRuleID": hh3cIDSTrapDetectRuleID,
       "hh3cIDSTrapEngineID": hh3cIDSTrapEngineID,
       "hh3cIDSTrapFileName": hh3cIDSTrapFileName,
       "hh3cIDSTrapCfgLineInFile": hh3cIDSTrapCfgLineInFile,
       "hh3cIDSTrapReasonForError": hh3cIDSTrapReasonForError,
       "hh3cIDSTrap": hh3cIDSTrap,
       "hh3cIDSTrapPrefix": hh3cIDSTrapPrefix,
       "hh3cIDSTrapIPFragQueueFull": hh3cIDSTrapIPFragQueueFull,
       "hh3cIDSTrapStatSessTabFull": hh3cIDSTrapStatSessTabFull,
       "hh3cIDSTrapDetectRuleParseFail": hh3cIDSTrapDetectRuleParseFail,
       "hh3cIDSTrapDBConnLost": hh3cIDSTrapDBConnLost,
       "hh3cIDSTrapCRLNeedUpdate": hh3cIDSTrapCRLNeedUpdate,
       "hh3cIDSTrapCertOverdue": hh3cIDSTrapCertOverdue,
       "hh3cIDSTrapTooManyLoginFail": hh3cIDSTrapTooManyLoginFail,
       "hh3cIDSTrapUpgradeError": hh3cIDSTrapUpgradeError,
       "hh3cIDSTrapFileAccessError": hh3cIDSTrapFileAccessError,
       "hh3cIDSTrapConsArithMemLow": hh3cIDSTrapConsArithMemLow,
       "hh3cIDSTrapSSRAMOperFail": hh3cIDSTrapSSRAMOperFail,
       "hh3cIDSTrapPacketProcessDisorder": hh3cIDSTrapPacketProcessDisorder,
       "hh3cIDSTrapCfgFileFormatError": hh3cIDSTrapCfgFileFormatError}
)
