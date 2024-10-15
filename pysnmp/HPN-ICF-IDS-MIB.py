# SNMP MIB module (HPN-ICF-IDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-IDS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:31 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfIDSMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfIds_ObjectIdentity = ObjectIdentity
hpnicfIds = _HpnicfIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47)
)
_HpnicfIDSTrapGroup_ObjectIdentity = ObjectIdentity
hpnicfIDSTrapGroup = _HpnicfIDSTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1)
)
_HpnicfIDSTrapInfo_ObjectIdentity = ObjectIdentity
hpnicfIDSTrapInfo = _HpnicfIDSTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1)
)
_HpnicfIDSTrapIPFragmentQueueLen_Type = Unsigned32
_HpnicfIDSTrapIPFragmentQueueLen_Object = MibScalar
hpnicfIDSTrapIPFragmentQueueLen = _HpnicfIDSTrapIPFragmentQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1, 1),
    _HpnicfIDSTrapIPFragmentQueueLen_Type()
)
hpnicfIDSTrapIPFragmentQueueLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIDSTrapIPFragmentQueueLen.setStatus("current")
_HpnicfIDSTrapStatSessionTabLen_Type = Unsigned32
_HpnicfIDSTrapStatSessionTabLen_Object = MibScalar
hpnicfIDSTrapStatSessionTabLen = _HpnicfIDSTrapStatSessionTabLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1, 2),
    _HpnicfIDSTrapStatSessionTabLen_Type()
)
hpnicfIDSTrapStatSessionTabLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIDSTrapStatSessionTabLen.setStatus("current")
_HpnicfIDSTrapIPAddressType_Type = InetAddressType
_HpnicfIDSTrapIPAddressType_Object = MibScalar
hpnicfIDSTrapIPAddressType = _HpnicfIDSTrapIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1, 3),
    _HpnicfIDSTrapIPAddressType_Type()
)
hpnicfIDSTrapIPAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIDSTrapIPAddressType.setStatus("current")
_HpnicfIDSTrapIPAddress_Type = InetAddress
_HpnicfIDSTrapIPAddress_Object = MibScalar
hpnicfIDSTrapIPAddress = _HpnicfIDSTrapIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1, 4),
    _HpnicfIDSTrapIPAddress_Type()
)
hpnicfIDSTrapIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIDSTrapIPAddress.setStatus("current")


class _HpnicfIDSTrapUserName_Type(OctetString):
    """Custom type hpnicfIDSTrapUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfIDSTrapUserName_Type.__name__ = "OctetString"
_HpnicfIDSTrapUserName_Object = MibScalar
hpnicfIDSTrapUserName = _HpnicfIDSTrapUserName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1, 5),
    _HpnicfIDSTrapUserName_Type()
)
hpnicfIDSTrapUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIDSTrapUserName.setStatus("current")


class _HpnicfIDSTrapLoginType_Type(Integer32):
    """Custom type hpnicfIDSTrapLoginType based on Integer32"""
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


_HpnicfIDSTrapLoginType_Type.__name__ = "Integer32"
_HpnicfIDSTrapLoginType_Object = MibScalar
hpnicfIDSTrapLoginType = _HpnicfIDSTrapLoginType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1, 6),
    _HpnicfIDSTrapLoginType_Type()
)
hpnicfIDSTrapLoginType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIDSTrapLoginType.setStatus("current")


class _HpnicfIDSTrapUpgradeType_Type(Integer32):
    """Custom type hpnicfIDSTrapUpgradeType based on Integer32"""
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


_HpnicfIDSTrapUpgradeType_Type.__name__ = "Integer32"
_HpnicfIDSTrapUpgradeType_Object = MibScalar
hpnicfIDSTrapUpgradeType = _HpnicfIDSTrapUpgradeType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1, 7),
    _HpnicfIDSTrapUpgradeType_Type()
)
hpnicfIDSTrapUpgradeType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIDSTrapUpgradeType.setStatus("current")


class _HpnicfIDSTrapCRLName_Type(OctetString):
    """Custom type hpnicfIDSTrapCRLName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfIDSTrapCRLName_Type.__name__ = "OctetString"
_HpnicfIDSTrapCRLName_Object = MibScalar
hpnicfIDSTrapCRLName = _HpnicfIDSTrapCRLName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1, 8),
    _HpnicfIDSTrapCRLName_Type()
)
hpnicfIDSTrapCRLName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIDSTrapCRLName.setStatus("current")


class _HpnicfIDSTrapCertName_Type(OctetString):
    """Custom type hpnicfIDSTrapCertName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfIDSTrapCertName_Type.__name__ = "OctetString"
_HpnicfIDSTrapCertName_Object = MibScalar
hpnicfIDSTrapCertName = _HpnicfIDSTrapCertName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1, 9),
    _HpnicfIDSTrapCertName_Type()
)
hpnicfIDSTrapCertName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIDSTrapCertName.setStatus("current")
_HpnicfIDSTrapDetectRuleID_Type = Unsigned32
_HpnicfIDSTrapDetectRuleID_Object = MibScalar
hpnicfIDSTrapDetectRuleID = _HpnicfIDSTrapDetectRuleID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1, 10),
    _HpnicfIDSTrapDetectRuleID_Type()
)
hpnicfIDSTrapDetectRuleID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIDSTrapDetectRuleID.setStatus("current")
_HpnicfIDSTrapEngineID_Type = Integer32
_HpnicfIDSTrapEngineID_Object = MibScalar
hpnicfIDSTrapEngineID = _HpnicfIDSTrapEngineID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1, 11),
    _HpnicfIDSTrapEngineID_Type()
)
hpnicfIDSTrapEngineID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIDSTrapEngineID.setStatus("current")


class _HpnicfIDSTrapFileName_Type(OctetString):
    """Custom type hpnicfIDSTrapFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpnicfIDSTrapFileName_Type.__name__ = "OctetString"
_HpnicfIDSTrapFileName_Object = MibScalar
hpnicfIDSTrapFileName = _HpnicfIDSTrapFileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1, 12),
    _HpnicfIDSTrapFileName_Type()
)
hpnicfIDSTrapFileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIDSTrapFileName.setStatus("current")
_HpnicfIDSTrapCfgLineInFile_Type = Unsigned32
_HpnicfIDSTrapCfgLineInFile_Object = MibScalar
hpnicfIDSTrapCfgLineInFile = _HpnicfIDSTrapCfgLineInFile_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1, 13),
    _HpnicfIDSTrapCfgLineInFile_Type()
)
hpnicfIDSTrapCfgLineInFile.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIDSTrapCfgLineInFile.setStatus("current")


class _HpnicfIDSTrapReasonForError_Type(OctetString):
    """Custom type hpnicfIDSTrapReasonForError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpnicfIDSTrapReasonForError_Type.__name__ = "OctetString"
_HpnicfIDSTrapReasonForError_Object = MibScalar
hpnicfIDSTrapReasonForError = _HpnicfIDSTrapReasonForError_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 1, 14),
    _HpnicfIDSTrapReasonForError_Type()
)
hpnicfIDSTrapReasonForError.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIDSTrapReasonForError.setStatus("current")
_HpnicfIDSTrap_ObjectIdentity = ObjectIdentity
hpnicfIDSTrap = _HpnicfIDSTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2)
)
_HpnicfIDSTrapPrefix_ObjectIdentity = ObjectIdentity
hpnicfIDSTrapPrefix = _HpnicfIDSTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2, 0)
)

# Managed Objects groups


# Notification objects

hpnicfIDSTrapIPFragQueueFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2, 0, 1)
)
hpnicfIDSTrapIPFragQueueFull.setObjects(
      *(("HPN-ICF-IDS-MIB", "hpnicfIDSTrapIPFragmentQueueLen"),
        ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapReasonForError"))
)
if mibBuilder.loadTexts:
    hpnicfIDSTrapIPFragQueueFull.setStatus(
        "current"
    )

hpnicfIDSTrapStatSessTabFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2, 0, 2)
)
hpnicfIDSTrapStatSessTabFull.setObjects(
      *(("HPN-ICF-IDS-MIB", "hpnicfIDSTrapStatSessionTabLen"),
        ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapReasonForError"))
)
if mibBuilder.loadTexts:
    hpnicfIDSTrapStatSessTabFull.setStatus(
        "current"
    )

hpnicfIDSTrapDetectRuleParseFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2, 0, 3)
)
hpnicfIDSTrapDetectRuleParseFail.setObjects(
      *(("HPN-ICF-IDS-MIB", "hpnicfIDSTrapDetectRuleID"),
        ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapEngineID"),
        ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapReasonForError"))
)
if mibBuilder.loadTexts:
    hpnicfIDSTrapDetectRuleParseFail.setStatus(
        "current"
    )

hpnicfIDSTrapDBConnLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2, 0, 4)
)
hpnicfIDSTrapDBConnLost.setObjects(
      *(("HPN-ICF-IDS-MIB", "hpnicfIDSTrapIPAddressType"),
        ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapIPAddress"),
        ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapReasonForError"))
)
if mibBuilder.loadTexts:
    hpnicfIDSTrapDBConnLost.setStatus(
        "current"
    )

hpnicfIDSTrapCRLNeedUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2, 0, 5)
)
hpnicfIDSTrapCRLNeedUpdate.setObjects(
      *(("HPN-ICF-IDS-MIB", "hpnicfIDSTrapCRLName"),
        ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapReasonForError"))
)
if mibBuilder.loadTexts:
    hpnicfIDSTrapCRLNeedUpdate.setStatus(
        "current"
    )

hpnicfIDSTrapCertOverdue = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2, 0, 6)
)
hpnicfIDSTrapCertOverdue.setObjects(
      *(("HPN-ICF-IDS-MIB", "hpnicfIDSTrapCertName"),
        ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapReasonForError"))
)
if mibBuilder.loadTexts:
    hpnicfIDSTrapCertOverdue.setStatus(
        "current"
    )

hpnicfIDSTrapTooManyLoginFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2, 0, 7)
)
hpnicfIDSTrapTooManyLoginFail.setObjects(
      *(("HPN-ICF-IDS-MIB", "hpnicfIDSTrapUserName"),
        ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapIPAddressType"),
        ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapIPAddress"),
        ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapLoginType"),
        ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapReasonForError"))
)
if mibBuilder.loadTexts:
    hpnicfIDSTrapTooManyLoginFail.setStatus(
        "current"
    )

hpnicfIDSTrapUpgradeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2, 0, 8)
)
hpnicfIDSTrapUpgradeError.setObjects(
      *(("HPN-ICF-IDS-MIB", "hpnicfIDSTrapUpgradeType"),
        ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapReasonForError"))
)
if mibBuilder.loadTexts:
    hpnicfIDSTrapUpgradeError.setStatus(
        "current"
    )

hpnicfIDSTrapFileAccessError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2, 0, 9)
)
hpnicfIDSTrapFileAccessError.setObjects(
      *(("HPN-ICF-IDS-MIB", "hpnicfIDSTrapFileName"),
        ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapReasonForError"))
)
if mibBuilder.loadTexts:
    hpnicfIDSTrapFileAccessError.setStatus(
        "current"
    )

hpnicfIDSTrapConsArithMemLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2, 0, 10)
)
hpnicfIDSTrapConsArithMemLow.setObjects(
    ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapReasonForError")
)
if mibBuilder.loadTexts:
    hpnicfIDSTrapConsArithMemLow.setStatus(
        "current"
    )

hpnicfIDSTrapSSRAMOperFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2, 0, 11)
)
hpnicfIDSTrapSSRAMOperFail.setObjects(
    ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapReasonForError")
)
if mibBuilder.loadTexts:
    hpnicfIDSTrapSSRAMOperFail.setStatus(
        "current"
    )

hpnicfIDSTrapPacketProcessDisorder = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2, 0, 12)
)
hpnicfIDSTrapPacketProcessDisorder.setObjects(
    ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapReasonForError")
)
if mibBuilder.loadTexts:
    hpnicfIDSTrapPacketProcessDisorder.setStatus(
        "current"
    )

hpnicfIDSTrapCfgFileFormatError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47, 1, 1, 2, 0, 13)
)
hpnicfIDSTrapCfgFileFormatError.setObjects(
      *(("HPN-ICF-IDS-MIB", "hpnicfIDSTrapFileName"),
        ("HPN-ICF-IDS-MIB", "hpnicfIDSTrapCfgLineInFile"))
)
if mibBuilder.loadTexts:
    hpnicfIDSTrapCfgFileFormatError.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-IDS-MIB",
    **{"hpnicfIds": hpnicfIds,
       "hpnicfIDSMib": hpnicfIDSMib,
       "hpnicfIDSTrapGroup": hpnicfIDSTrapGroup,
       "hpnicfIDSTrapInfo": hpnicfIDSTrapInfo,
       "hpnicfIDSTrapIPFragmentQueueLen": hpnicfIDSTrapIPFragmentQueueLen,
       "hpnicfIDSTrapStatSessionTabLen": hpnicfIDSTrapStatSessionTabLen,
       "hpnicfIDSTrapIPAddressType": hpnicfIDSTrapIPAddressType,
       "hpnicfIDSTrapIPAddress": hpnicfIDSTrapIPAddress,
       "hpnicfIDSTrapUserName": hpnicfIDSTrapUserName,
       "hpnicfIDSTrapLoginType": hpnicfIDSTrapLoginType,
       "hpnicfIDSTrapUpgradeType": hpnicfIDSTrapUpgradeType,
       "hpnicfIDSTrapCRLName": hpnicfIDSTrapCRLName,
       "hpnicfIDSTrapCertName": hpnicfIDSTrapCertName,
       "hpnicfIDSTrapDetectRuleID": hpnicfIDSTrapDetectRuleID,
       "hpnicfIDSTrapEngineID": hpnicfIDSTrapEngineID,
       "hpnicfIDSTrapFileName": hpnicfIDSTrapFileName,
       "hpnicfIDSTrapCfgLineInFile": hpnicfIDSTrapCfgLineInFile,
       "hpnicfIDSTrapReasonForError": hpnicfIDSTrapReasonForError,
       "hpnicfIDSTrap": hpnicfIDSTrap,
       "hpnicfIDSTrapPrefix": hpnicfIDSTrapPrefix,
       "hpnicfIDSTrapIPFragQueueFull": hpnicfIDSTrapIPFragQueueFull,
       "hpnicfIDSTrapStatSessTabFull": hpnicfIDSTrapStatSessTabFull,
       "hpnicfIDSTrapDetectRuleParseFail": hpnicfIDSTrapDetectRuleParseFail,
       "hpnicfIDSTrapDBConnLost": hpnicfIDSTrapDBConnLost,
       "hpnicfIDSTrapCRLNeedUpdate": hpnicfIDSTrapCRLNeedUpdate,
       "hpnicfIDSTrapCertOverdue": hpnicfIDSTrapCertOverdue,
       "hpnicfIDSTrapTooManyLoginFail": hpnicfIDSTrapTooManyLoginFail,
       "hpnicfIDSTrapUpgradeError": hpnicfIDSTrapUpgradeError,
       "hpnicfIDSTrapFileAccessError": hpnicfIDSTrapFileAccessError,
       "hpnicfIDSTrapConsArithMemLow": hpnicfIDSTrapConsArithMemLow,
       "hpnicfIDSTrapSSRAMOperFail": hpnicfIDSTrapSSRAMOperFail,
       "hpnicfIDSTrapPacketProcessDisorder": hpnicfIDSTrapPacketProcessDisorder,
       "hpnicfIDSTrapCfgFileFormatError": hpnicfIDSTrapCfgFileFormatError}
)
