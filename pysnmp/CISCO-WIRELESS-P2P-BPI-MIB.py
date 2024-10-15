# SNMP MIB module (CISCO-WIRELESS-P2P-BPI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WIRELESS-P2P-BPI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:41 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

ciscoWirelessP2pBpiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 135)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CwrBpiMIBObjects_ObjectIdentity = ObjectIdentity
cwrBpiMIBObjects = _CwrBpiMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1)
)
_CwrBpiRsObjects_ObjectIdentity = ObjectIdentity
cwrBpiRsObjects = _CwrBpiRsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1)
)
_CwrBpiRsBaseTable_Object = MibTable
cwrBpiRsBaseTable = _CwrBpiRsBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cwrBpiRsBaseTable.setStatus("current")
_CwrBpiRsBaseEntry_Object = MibTableRow
cwrBpiRsBaseEntry = _CwrBpiRsBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 1, 1)
)
cwrBpiRsBaseEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwrBpiRsBaseEntry.setStatus("current")
_CwrBpiRsPrivacyEnable_Type = TruthValue
_CwrBpiRsPrivacyEnable_Object = MibTableColumn
cwrBpiRsPrivacyEnable = _CwrBpiRsPrivacyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 1, 1, 1),
    _CwrBpiRsPrivacyEnable_Type()
)
cwrBpiRsPrivacyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrBpiRsPrivacyEnable.setStatus("current")


class _CwrBpiRsPublicKey_Type(OctetString):
    """Custom type cwrBpiRsPublicKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 126),
    )


_CwrBpiRsPublicKey_Type.__name__ = "OctetString"
_CwrBpiRsPublicKey_Object = MibTableColumn
cwrBpiRsPublicKey = _CwrBpiRsPublicKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 1, 1, 2),
    _CwrBpiRsPublicKey_Type()
)
cwrBpiRsPublicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRsPublicKey.setStatus("current")


class _CwrBpiRsAuthState_Type(Integer32):
    """Custom type cwrBpiRsAuthState based on Integer32"""
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
        *(("authRejectWait", 5),
          ("authWait", 2),
          ("authorized", 3),
          ("reauthWait", 4),
          ("start", 1))
    )


_CwrBpiRsAuthState_Type.__name__ = "Integer32"
_CwrBpiRsAuthState_Object = MibTableColumn
cwrBpiRsAuthState = _CwrBpiRsAuthState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 1, 1, 3),
    _CwrBpiRsAuthState_Type()
)
cwrBpiRsAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRsAuthState.setStatus("current")


class _CwrBpiRsAuthKeySequenceNumber_Type(Integer32):
    """Custom type cwrBpiRsAuthKeySequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CwrBpiRsAuthKeySequenceNumber_Type.__name__ = "Integer32"
_CwrBpiRsAuthKeySequenceNumber_Object = MibTableColumn
cwrBpiRsAuthKeySequenceNumber = _CwrBpiRsAuthKeySequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 1, 1, 4),
    _CwrBpiRsAuthKeySequenceNumber_Type()
)
cwrBpiRsAuthKeySequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRsAuthKeySequenceNumber.setStatus("current")
_CwrBpiRsAuthExpires_Type = TimeInterval
_CwrBpiRsAuthExpires_Object = MibTableColumn
cwrBpiRsAuthExpires = _CwrBpiRsAuthExpires_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 1, 1, 5),
    _CwrBpiRsAuthExpires_Type()
)
cwrBpiRsAuthExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRsAuthExpires.setStatus("current")
_CwrBpiRsAuthReset_Type = TruthValue
_CwrBpiRsAuthReset_Object = MibTableColumn
cwrBpiRsAuthReset = _CwrBpiRsAuthReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 1, 1, 6),
    _CwrBpiRsAuthReset_Type()
)
cwrBpiRsAuthReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrBpiRsAuthReset.setStatus("current")


class _CwrBpiRsAuthGraceTime_Type(Integer32):
    """Custom type cwrBpiRsAuthGraceTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_CwrBpiRsAuthGraceTime_Type.__name__ = "Integer32"
_CwrBpiRsAuthGraceTime_Object = MibTableColumn
cwrBpiRsAuthGraceTime = _CwrBpiRsAuthGraceTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 1, 1, 7),
    _CwrBpiRsAuthGraceTime_Type()
)
cwrBpiRsAuthGraceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrBpiRsAuthGraceTime.setStatus("current")
if mibBuilder.loadTexts:
    cwrBpiRsAuthGraceTime.setUnits("seconds")


class _CwrBpiRsTEKGraceTime_Type(Integer32):
    """Custom type cwrBpiRsTEKGraceTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_CwrBpiRsTEKGraceTime_Type.__name__ = "Integer32"
_CwrBpiRsTEKGraceTime_Object = MibTableColumn
cwrBpiRsTEKGraceTime = _CwrBpiRsTEKGraceTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 1, 1, 8),
    _CwrBpiRsTEKGraceTime_Type()
)
cwrBpiRsTEKGraceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrBpiRsTEKGraceTime.setStatus("current")
if mibBuilder.loadTexts:
    cwrBpiRsTEKGraceTime.setUnits("seconds")


class _CwrBpiRsAuthWaitTimeout_Type(Integer32):
    """Custom type cwrBpiRsAuthWaitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_CwrBpiRsAuthWaitTimeout_Type.__name__ = "Integer32"
_CwrBpiRsAuthWaitTimeout_Object = MibTableColumn
cwrBpiRsAuthWaitTimeout = _CwrBpiRsAuthWaitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 1, 1, 9),
    _CwrBpiRsAuthWaitTimeout_Type()
)
cwrBpiRsAuthWaitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrBpiRsAuthWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cwrBpiRsAuthWaitTimeout.setUnits("seconds")


class _CwrBpiRsReauthWaitTimeout_Type(Integer32):
    """Custom type cwrBpiRsReauthWaitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_CwrBpiRsReauthWaitTimeout_Type.__name__ = "Integer32"
_CwrBpiRsReauthWaitTimeout_Object = MibTableColumn
cwrBpiRsReauthWaitTimeout = _CwrBpiRsReauthWaitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 1, 1, 10),
    _CwrBpiRsReauthWaitTimeout_Type()
)
cwrBpiRsReauthWaitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrBpiRsReauthWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cwrBpiRsReauthWaitTimeout.setUnits("seconds")


class _CwrBpiRsOpWaitTimeout_Type(Integer32):
    """Custom type cwrBpiRsOpWaitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CwrBpiRsOpWaitTimeout_Type.__name__ = "Integer32"
_CwrBpiRsOpWaitTimeout_Object = MibTableColumn
cwrBpiRsOpWaitTimeout = _CwrBpiRsOpWaitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 1, 1, 11),
    _CwrBpiRsOpWaitTimeout_Type()
)
cwrBpiRsOpWaitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrBpiRsOpWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cwrBpiRsOpWaitTimeout.setUnits("seconds")


class _CwrBpiRsRekeyWaitTimeout_Type(Integer32):
    """Custom type cwrBpiRsRekeyWaitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CwrBpiRsRekeyWaitTimeout_Type.__name__ = "Integer32"
_CwrBpiRsRekeyWaitTimeout_Object = MibTableColumn
cwrBpiRsRekeyWaitTimeout = _CwrBpiRsRekeyWaitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 1, 1, 12),
    _CwrBpiRsRekeyWaitTimeout_Type()
)
cwrBpiRsRekeyWaitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrBpiRsRekeyWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cwrBpiRsRekeyWaitTimeout.setUnits("seconds")
_CwrBpiRsAuthRequests_Type = Counter32
_CwrBpiRsAuthRequests_Object = MibTableColumn
cwrBpiRsAuthRequests = _CwrBpiRsAuthRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 1, 1, 13),
    _CwrBpiRsAuthRequests_Type()
)
cwrBpiRsAuthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRsAuthRequests.setStatus("current")
_CwrBpiRsAuthReplies_Type = Counter32
_CwrBpiRsAuthReplies_Object = MibTableColumn
cwrBpiRsAuthReplies = _CwrBpiRsAuthReplies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 1, 1, 14),
    _CwrBpiRsAuthReplies_Type()
)
cwrBpiRsAuthReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRsAuthReplies.setStatus("current")
_CwrBpiRsAuthInvalids_Type = Counter32
_CwrBpiRsAuthInvalids_Object = MibTableColumn
cwrBpiRsAuthInvalids = _CwrBpiRsAuthInvalids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 1, 1, 15),
    _CwrBpiRsAuthInvalids_Type()
)
cwrBpiRsAuthInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRsAuthInvalids.setStatus("current")


class _CwrBpiRsAuthInvalidErrorCode_Type(Integer32):
    """Custom type cwrBpiRsAuthInvalidErrorCode based on Integer32"""
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
        *(("invalidKeySequence", 4),
          ("keyRequestAuthenticationFailure", 5),
          ("noInformation", 0),
          ("unauthorizedSlave", 1),
          ("undefined", 2),
          ("unsolicited", 3))
    )


_CwrBpiRsAuthInvalidErrorCode_Type.__name__ = "Integer32"
_CwrBpiRsAuthInvalidErrorCode_Object = MibTableColumn
cwrBpiRsAuthInvalidErrorCode = _CwrBpiRsAuthInvalidErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 1, 1, 16),
    _CwrBpiRsAuthInvalidErrorCode_Type()
)
cwrBpiRsAuthInvalidErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRsAuthInvalidErrorCode.setStatus("current")
_CwrBpiRsAuthInvalidErrorString_Type = DisplayString
_CwrBpiRsAuthInvalidErrorString_Object = MibTableColumn
cwrBpiRsAuthInvalidErrorString = _CwrBpiRsAuthInvalidErrorString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 1, 1, 17),
    _CwrBpiRsAuthInvalidErrorString_Type()
)
cwrBpiRsAuthInvalidErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRsAuthInvalidErrorString.setStatus("current")
_CwrBpiRsTEKTable_Object = MibTable
cwrBpiRsTEKTable = _CwrBpiRsTEKTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cwrBpiRsTEKTable.setStatus("current")
_CwrBpiRsTEKEntry_Object = MibTableRow
cwrBpiRsTEKEntry = _CwrBpiRsTEKEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 2, 1)
)
cwrBpiRsTEKEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwrBpiRsTEKEntry.setStatus("current")
_CwrBpiRsTEKEncryptionNegotiated_Type = TruthValue
_CwrBpiRsTEKEncryptionNegotiated_Object = MibTableColumn
cwrBpiRsTEKEncryptionNegotiated = _CwrBpiRsTEKEncryptionNegotiated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 2, 1, 1),
    _CwrBpiRsTEKEncryptionNegotiated_Type()
)
cwrBpiRsTEKEncryptionNegotiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRsTEKEncryptionNegotiated.setStatus("current")


class _CwrBpiRsTEKState_Type(Integer32):
    """Custom type cwrBpiRsTEKState based on Integer32"""
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
        *(("opReauthWait", 3),
          ("opWait", 2),
          ("operational", 4),
          ("rekeyReauthWait", 6),
          ("rekeyWait", 5),
          ("start", 1))
    )


_CwrBpiRsTEKState_Type.__name__ = "Integer32"
_CwrBpiRsTEKState_Object = MibTableColumn
cwrBpiRsTEKState = _CwrBpiRsTEKState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 2, 1, 2),
    _CwrBpiRsTEKState_Type()
)
cwrBpiRsTEKState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRsTEKState.setStatus("current")
_CwrBpiRsTEKExpiresOld_Type = TimeInterval
_CwrBpiRsTEKExpiresOld_Object = MibTableColumn
cwrBpiRsTEKExpiresOld = _CwrBpiRsTEKExpiresOld_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 2, 1, 3),
    _CwrBpiRsTEKExpiresOld_Type()
)
cwrBpiRsTEKExpiresOld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRsTEKExpiresOld.setStatus("current")
_CwrBpiRsTEKExpiresNew_Type = TimeInterval
_CwrBpiRsTEKExpiresNew_Object = MibTableColumn
cwrBpiRsTEKExpiresNew = _CwrBpiRsTEKExpiresNew_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 2, 1, 4),
    _CwrBpiRsTEKExpiresNew_Type()
)
cwrBpiRsTEKExpiresNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRsTEKExpiresNew.setStatus("current")
_CwrBpiRsTEKKeyRequests_Type = Counter32
_CwrBpiRsTEKKeyRequests_Object = MibTableColumn
cwrBpiRsTEKKeyRequests = _CwrBpiRsTEKKeyRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 2, 1, 5),
    _CwrBpiRsTEKKeyRequests_Type()
)
cwrBpiRsTEKKeyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRsTEKKeyRequests.setStatus("current")
_CwrBpiRsTEKKeyReplies_Type = Counter32
_CwrBpiRsTEKKeyReplies_Object = MibTableColumn
cwrBpiRsTEKKeyReplies = _CwrBpiRsTEKKeyReplies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 2, 1, 6),
    _CwrBpiRsTEKKeyReplies_Type()
)
cwrBpiRsTEKKeyReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRsTEKKeyReplies.setStatus("current")
_CwrBpiRsTEKInvalids_Type = Counter32
_CwrBpiRsTEKInvalids_Object = MibTableColumn
cwrBpiRsTEKInvalids = _CwrBpiRsTEKInvalids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 2, 1, 7),
    _CwrBpiRsTEKInvalids_Type()
)
cwrBpiRsTEKInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRsTEKInvalids.setStatus("current")
_CwrBpiRsTEKAuthPends_Type = Counter32
_CwrBpiRsTEKAuthPends_Object = MibTableColumn
cwrBpiRsTEKAuthPends = _CwrBpiRsTEKAuthPends_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 2, 1, 8),
    _CwrBpiRsTEKAuthPends_Type()
)
cwrBpiRsTEKAuthPends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRsTEKAuthPends.setStatus("current")


class _CwrBpiRsTEKInvalidErrorCode_Type(Integer32):
    """Custom type cwrBpiRsTEKInvalidErrorCode based on Integer32"""
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
        *(("invalidKeySequence", 4),
          ("keyRequestAuthenticationFailure", 5),
          ("noInformation", 0),
          ("unauthorizedSlave", 1),
          ("undefined", 2),
          ("unsolicited", 3))
    )


_CwrBpiRsTEKInvalidErrorCode_Type.__name__ = "Integer32"
_CwrBpiRsTEKInvalidErrorCode_Object = MibTableColumn
cwrBpiRsTEKInvalidErrorCode = _CwrBpiRsTEKInvalidErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 2, 1, 9),
    _CwrBpiRsTEKInvalidErrorCode_Type()
)
cwrBpiRsTEKInvalidErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRsTEKInvalidErrorCode.setStatus("current")
_CwrBpiRsTEKInvalidErrorString_Type = DisplayString
_CwrBpiRsTEKInvalidErrorString_Object = MibTableColumn
cwrBpiRsTEKInvalidErrorString = _CwrBpiRsTEKInvalidErrorString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 1, 2, 1, 10),
    _CwrBpiRsTEKInvalidErrorString_Type()
)
cwrBpiRsTEKInvalidErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRsTEKInvalidErrorString.setStatus("current")
_CwrBpiRmObjects_ObjectIdentity = ObjectIdentity
cwrBpiRmObjects = _CwrBpiRmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 2)
)
_CwrBpiRmAuthTable_Object = MibTable
cwrBpiRmAuthTable = _CwrBpiRmAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cwrBpiRmAuthTable.setStatus("current")
_CwrBpiRmAuthEntry_Object = MibTableRow
cwrBpiRmAuthEntry = _CwrBpiRmAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 2, 1, 1)
)
cwrBpiRmAuthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwrBpiRmAuthEntry.setStatus("current")
_CwrBpiRmAuthPrivacyEnable_Type = TruthValue
_CwrBpiRmAuthPrivacyEnable_Object = MibTableColumn
cwrBpiRmAuthPrivacyEnable = _CwrBpiRmAuthPrivacyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 2, 1, 1, 1),
    _CwrBpiRmAuthPrivacyEnable_Type()
)
cwrBpiRmAuthPrivacyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrBpiRmAuthPrivacyEnable.setStatus("current")


class _CwrBpiRmAuthRsPublicKey_Type(OctetString):
    """Custom type cwrBpiRmAuthRsPublicKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 126),
    )


_CwrBpiRmAuthRsPublicKey_Type.__name__ = "OctetString"
_CwrBpiRmAuthRsPublicKey_Object = MibTableColumn
cwrBpiRmAuthRsPublicKey = _CwrBpiRmAuthRsPublicKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 2, 1, 1, 2),
    _CwrBpiRmAuthRsPublicKey_Type()
)
cwrBpiRmAuthRsPublicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRmAuthRsPublicKey.setStatus("current")


class _CwrBpiRmAuthRsKeySequenceNumber_Type(Integer32):
    """Custom type cwrBpiRmAuthRsKeySequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CwrBpiRmAuthRsKeySequenceNumber_Type.__name__ = "Integer32"
_CwrBpiRmAuthRsKeySequenceNumber_Object = MibTableColumn
cwrBpiRmAuthRsKeySequenceNumber = _CwrBpiRmAuthRsKeySequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 2, 1, 1, 3),
    _CwrBpiRmAuthRsKeySequenceNumber_Type()
)
cwrBpiRmAuthRsKeySequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRmAuthRsKeySequenceNumber.setStatus("current")
_CwrBpiRmAuthRsExpires_Type = TimeInterval
_CwrBpiRmAuthRsExpires_Object = MibTableColumn
cwrBpiRmAuthRsExpires = _CwrBpiRmAuthRsExpires_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 2, 1, 1, 4),
    _CwrBpiRmAuthRsExpires_Type()
)
cwrBpiRmAuthRsExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRmAuthRsExpires.setStatus("current")


class _CwrBpiRmAuthRsLifetime_Type(Integer32):
    """Custom type cwrBpiRmAuthRsLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6048000),
    )


_CwrBpiRmAuthRsLifetime_Type.__name__ = "Integer32"
_CwrBpiRmAuthRsLifetime_Object = MibTableColumn
cwrBpiRmAuthRsLifetime = _CwrBpiRmAuthRsLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 2, 1, 1, 5),
    _CwrBpiRmAuthRsLifetime_Type()
)
cwrBpiRmAuthRsLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrBpiRmAuthRsLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cwrBpiRmAuthRsLifetime.setUnits("seconds")
_CwrBpiRmAuthRsReset_Type = TruthValue
_CwrBpiRmAuthRsReset_Object = MibTableColumn
cwrBpiRmAuthRsReset = _CwrBpiRmAuthRsReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 2, 1, 1, 6),
    _CwrBpiRmAuthRsReset_Type()
)
cwrBpiRmAuthRsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrBpiRmAuthRsReset.setStatus("current")
_CwrBpiRmAuthRsRequests_Type = Counter32
_CwrBpiRmAuthRsRequests_Object = MibTableColumn
cwrBpiRmAuthRsRequests = _CwrBpiRmAuthRsRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 2, 1, 1, 7),
    _CwrBpiRmAuthRsRequests_Type()
)
cwrBpiRmAuthRsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRmAuthRsRequests.setStatus("current")
_CwrBpiRmAuthRsReplies_Type = Counter32
_CwrBpiRmAuthRsReplies_Object = MibTableColumn
cwrBpiRmAuthRsReplies = _CwrBpiRmAuthRsReplies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 2, 1, 1, 8),
    _CwrBpiRmAuthRsReplies_Type()
)
cwrBpiRmAuthRsReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRmAuthRsReplies.setStatus("current")
_CwrBpiRmAuthRsInvalids_Type = Counter32
_CwrBpiRmAuthRsInvalids_Object = MibTableColumn
cwrBpiRmAuthRsInvalids = _CwrBpiRmAuthRsInvalids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 2, 1, 1, 9),
    _CwrBpiRmAuthRsInvalids_Type()
)
cwrBpiRmAuthRsInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRmAuthRsInvalids.setStatus("current")


class _CwrBpiRmAuthInvalidErrorCode_Type(Integer32):
    """Custom type cwrBpiRmAuthInvalidErrorCode based on Integer32"""
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
        *(("invalidKeySequence", 4),
          ("keyRequestAuthenticationFailure", 5),
          ("noInformation", 0),
          ("unauthorizedSlave", 1),
          ("undefined", 2),
          ("unsolicited", 3))
    )


_CwrBpiRmAuthInvalidErrorCode_Type.__name__ = "Integer32"
_CwrBpiRmAuthInvalidErrorCode_Object = MibTableColumn
cwrBpiRmAuthInvalidErrorCode = _CwrBpiRmAuthInvalidErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 2, 1, 1, 10),
    _CwrBpiRmAuthInvalidErrorCode_Type()
)
cwrBpiRmAuthInvalidErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRmAuthInvalidErrorCode.setStatus("current")
_CwrBpiRmAuthInvalidErrorString_Type = DisplayString
_CwrBpiRmAuthInvalidErrorString_Object = MibTableColumn
cwrBpiRmAuthInvalidErrorString = _CwrBpiRmAuthInvalidErrorString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 2, 1, 1, 11),
    _CwrBpiRmAuthInvalidErrorString_Type()
)
cwrBpiRmAuthInvalidErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRmAuthInvalidErrorString.setStatus("current")
_CwrBpiRmTEKTable_Object = MibTable
cwrBpiRmTEKTable = _CwrBpiRmTEKTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cwrBpiRmTEKTable.setStatus("current")
_CwrBpiRmTEKEntry_Object = MibTableRow
cwrBpiRmTEKEntry = _CwrBpiRmTEKEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 2, 2, 1)
)
cwrBpiRmTEKEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwrBpiRmTEKEntry.setStatus("current")
_CwrBpiRmTEKEncryptionNegotiated_Type = TruthValue
_CwrBpiRmTEKEncryptionNegotiated_Object = MibTableColumn
cwrBpiRmTEKEncryptionNegotiated = _CwrBpiRmTEKEncryptionNegotiated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 2, 2, 1, 1),
    _CwrBpiRmTEKEncryptionNegotiated_Type()
)
cwrBpiRmTEKEncryptionNegotiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRmTEKEncryptionNegotiated.setStatus("current")


class _CwrBpiRmTEKLifetime_Type(Integer32):
    """Custom type cwrBpiRmTEKLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_CwrBpiRmTEKLifetime_Type.__name__ = "Integer32"
_CwrBpiRmTEKLifetime_Object = MibTableColumn
cwrBpiRmTEKLifetime = _CwrBpiRmTEKLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 2, 2, 1, 2),
    _CwrBpiRmTEKLifetime_Type()
)
cwrBpiRmTEKLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrBpiRmTEKLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cwrBpiRmTEKLifetime.setUnits("seconds")
_CwrBpiRmTEKExpiresOld_Type = TimeInterval
_CwrBpiRmTEKExpiresOld_Object = MibTableColumn
cwrBpiRmTEKExpiresOld = _CwrBpiRmTEKExpiresOld_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 2, 2, 1, 3),
    _CwrBpiRmTEKExpiresOld_Type()
)
cwrBpiRmTEKExpiresOld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRmTEKExpiresOld.setStatus("current")
_CwrBpiRmTEKExpiresNew_Type = TimeInterval
_CwrBpiRmTEKExpiresNew_Object = MibTableColumn
cwrBpiRmTEKExpiresNew = _CwrBpiRmTEKExpiresNew_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 2, 2, 1, 4),
    _CwrBpiRmTEKExpiresNew_Type()
)
cwrBpiRmTEKExpiresNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRmTEKExpiresNew.setStatus("current")
_CwrBpiRmTEKReset_Type = TruthValue
_CwrBpiRmTEKReset_Object = MibTableColumn
cwrBpiRmTEKReset = _CwrBpiRmTEKReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 2, 2, 1, 5),
    _CwrBpiRmTEKReset_Type()
)
cwrBpiRmTEKReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwrBpiRmTEKReset.setStatus("current")
_CwrBpiRmKeyRequests_Type = Counter32
_CwrBpiRmKeyRequests_Object = MibTableColumn
cwrBpiRmKeyRequests = _CwrBpiRmKeyRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 2, 2, 1, 6),
    _CwrBpiRmKeyRequests_Type()
)
cwrBpiRmKeyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRmKeyRequests.setStatus("current")
_CwrBpiRmKeyReplies_Type = Counter32
_CwrBpiRmKeyReplies_Object = MibTableColumn
cwrBpiRmKeyReplies = _CwrBpiRmKeyReplies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 2, 2, 1, 7),
    _CwrBpiRmKeyReplies_Type()
)
cwrBpiRmKeyReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRmKeyReplies.setStatus("current")
_CwrBpiRmTEKInvalids_Type = Counter32
_CwrBpiRmTEKInvalids_Object = MibTableColumn
cwrBpiRmTEKInvalids = _CwrBpiRmTEKInvalids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 2, 2, 1, 8),
    _CwrBpiRmTEKInvalids_Type()
)
cwrBpiRmTEKInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRmTEKInvalids.setStatus("current")


class _CwrBpiRmTEKInvalidErrorCode_Type(Integer32):
    """Custom type cwrBpiRmTEKInvalidErrorCode based on Integer32"""
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
        *(("invalidKeySequence", 4),
          ("keyRequestAuthenticationFailure", 5),
          ("noInformation", 0),
          ("unauthorizedSlave", 1),
          ("undefined", 2),
          ("unsolicited", 3))
    )


_CwrBpiRmTEKInvalidErrorCode_Type.__name__ = "Integer32"
_CwrBpiRmTEKInvalidErrorCode_Object = MibTableColumn
cwrBpiRmTEKInvalidErrorCode = _CwrBpiRmTEKInvalidErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 2, 2, 1, 9),
    _CwrBpiRmTEKInvalidErrorCode_Type()
)
cwrBpiRmTEKInvalidErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRmTEKInvalidErrorCode.setStatus("current")
_CwrBpiRmTEKInvalidErrorString_Type = DisplayString
_CwrBpiRmTEKInvalidErrorString_Object = MibTableColumn
cwrBpiRmTEKInvalidErrorString = _CwrBpiRmTEKInvalidErrorString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 1, 2, 2, 1, 10),
    _CwrBpiRmTEKInvalidErrorString_Type()
)
cwrBpiRmTEKInvalidErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrBpiRmTEKInvalidErrorString.setStatus("current")
_CwrBpiNotification_ObjectIdentity = ObjectIdentity
cwrBpiNotification = _CwrBpiNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 2)
)
_CwrBpiConformance_ObjectIdentity = ObjectIdentity
cwrBpiConformance = _CwrBpiConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 3)
)
_CwrBpiCompliances_ObjectIdentity = ObjectIdentity
cwrBpiCompliances = _CwrBpiCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 3, 1)
)
_CwrBpiGroups_ObjectIdentity = ObjectIdentity
cwrBpiGroups = _CwrBpiGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 3, 2)
)

# Managed Objects groups

cwrBpiRsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 3, 2, 1)
)
cwrBpiRsGroup.setObjects(
      *(("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRsPrivacyEnable"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRsPublicKey"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRsAuthState"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRsAuthKeySequenceNumber"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRsAuthExpires"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRsAuthReset"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRsAuthGraceTime"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRsTEKGraceTime"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRsAuthWaitTimeout"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRsReauthWaitTimeout"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRsOpWaitTimeout"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRsRekeyWaitTimeout"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRsAuthRequests"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRsAuthReplies"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRsAuthInvalids"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRsAuthInvalidErrorCode"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRsAuthInvalidErrorString"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRsTEKEncryptionNegotiated"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRsTEKState"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRsTEKExpiresOld"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRsTEKExpiresNew"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRsTEKKeyRequests"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRsTEKKeyReplies"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRsTEKInvalids"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRsTEKAuthPends"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRsTEKInvalidErrorCode"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRsTEKInvalidErrorString"))
)
if mibBuilder.loadTexts:
    cwrBpiRsGroup.setStatus("current")

cwrBpiRmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 3, 2, 2)
)
cwrBpiRmGroup.setObjects(
      *(("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRmAuthPrivacyEnable"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRmAuthRsPublicKey"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRmAuthRsKeySequenceNumber"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRmAuthRsExpires"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRmAuthRsLifetime"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRmAuthRsReset"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRmAuthRsRequests"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRmAuthRsReplies"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRmAuthRsInvalids"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRmAuthInvalidErrorCode"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRmAuthInvalidErrorString"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRmTEKEncryptionNegotiated"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRmTEKLifetime"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRmTEKExpiresOld"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRmTEKExpiresNew"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRmTEKReset"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRmKeyRequests"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRmKeyReplies"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRmTEKInvalids"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRmTEKInvalidErrorCode"),
        ("CISCO-WIRELESS-P2P-BPI-MIB", "cwrBpiRmTEKInvalidErrorString"))
)
if mibBuilder.loadTexts:
    cwrBpiRmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cwrBpiBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 135, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cwrBpiBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WIRELESS-P2P-BPI-MIB",
    **{"ciscoWirelessP2pBpiMIB": ciscoWirelessP2pBpiMIB,
       "cwrBpiMIBObjects": cwrBpiMIBObjects,
       "cwrBpiRsObjects": cwrBpiRsObjects,
       "cwrBpiRsBaseTable": cwrBpiRsBaseTable,
       "cwrBpiRsBaseEntry": cwrBpiRsBaseEntry,
       "cwrBpiRsPrivacyEnable": cwrBpiRsPrivacyEnable,
       "cwrBpiRsPublicKey": cwrBpiRsPublicKey,
       "cwrBpiRsAuthState": cwrBpiRsAuthState,
       "cwrBpiRsAuthKeySequenceNumber": cwrBpiRsAuthKeySequenceNumber,
       "cwrBpiRsAuthExpires": cwrBpiRsAuthExpires,
       "cwrBpiRsAuthReset": cwrBpiRsAuthReset,
       "cwrBpiRsAuthGraceTime": cwrBpiRsAuthGraceTime,
       "cwrBpiRsTEKGraceTime": cwrBpiRsTEKGraceTime,
       "cwrBpiRsAuthWaitTimeout": cwrBpiRsAuthWaitTimeout,
       "cwrBpiRsReauthWaitTimeout": cwrBpiRsReauthWaitTimeout,
       "cwrBpiRsOpWaitTimeout": cwrBpiRsOpWaitTimeout,
       "cwrBpiRsRekeyWaitTimeout": cwrBpiRsRekeyWaitTimeout,
       "cwrBpiRsAuthRequests": cwrBpiRsAuthRequests,
       "cwrBpiRsAuthReplies": cwrBpiRsAuthReplies,
       "cwrBpiRsAuthInvalids": cwrBpiRsAuthInvalids,
       "cwrBpiRsAuthInvalidErrorCode": cwrBpiRsAuthInvalidErrorCode,
       "cwrBpiRsAuthInvalidErrorString": cwrBpiRsAuthInvalidErrorString,
       "cwrBpiRsTEKTable": cwrBpiRsTEKTable,
       "cwrBpiRsTEKEntry": cwrBpiRsTEKEntry,
       "cwrBpiRsTEKEncryptionNegotiated": cwrBpiRsTEKEncryptionNegotiated,
       "cwrBpiRsTEKState": cwrBpiRsTEKState,
       "cwrBpiRsTEKExpiresOld": cwrBpiRsTEKExpiresOld,
       "cwrBpiRsTEKExpiresNew": cwrBpiRsTEKExpiresNew,
       "cwrBpiRsTEKKeyRequests": cwrBpiRsTEKKeyRequests,
       "cwrBpiRsTEKKeyReplies": cwrBpiRsTEKKeyReplies,
       "cwrBpiRsTEKInvalids": cwrBpiRsTEKInvalids,
       "cwrBpiRsTEKAuthPends": cwrBpiRsTEKAuthPends,
       "cwrBpiRsTEKInvalidErrorCode": cwrBpiRsTEKInvalidErrorCode,
       "cwrBpiRsTEKInvalidErrorString": cwrBpiRsTEKInvalidErrorString,
       "cwrBpiRmObjects": cwrBpiRmObjects,
       "cwrBpiRmAuthTable": cwrBpiRmAuthTable,
       "cwrBpiRmAuthEntry": cwrBpiRmAuthEntry,
       "cwrBpiRmAuthPrivacyEnable": cwrBpiRmAuthPrivacyEnable,
       "cwrBpiRmAuthRsPublicKey": cwrBpiRmAuthRsPublicKey,
       "cwrBpiRmAuthRsKeySequenceNumber": cwrBpiRmAuthRsKeySequenceNumber,
       "cwrBpiRmAuthRsExpires": cwrBpiRmAuthRsExpires,
       "cwrBpiRmAuthRsLifetime": cwrBpiRmAuthRsLifetime,
       "cwrBpiRmAuthRsReset": cwrBpiRmAuthRsReset,
       "cwrBpiRmAuthRsRequests": cwrBpiRmAuthRsRequests,
       "cwrBpiRmAuthRsReplies": cwrBpiRmAuthRsReplies,
       "cwrBpiRmAuthRsInvalids": cwrBpiRmAuthRsInvalids,
       "cwrBpiRmAuthInvalidErrorCode": cwrBpiRmAuthInvalidErrorCode,
       "cwrBpiRmAuthInvalidErrorString": cwrBpiRmAuthInvalidErrorString,
       "cwrBpiRmTEKTable": cwrBpiRmTEKTable,
       "cwrBpiRmTEKEntry": cwrBpiRmTEKEntry,
       "cwrBpiRmTEKEncryptionNegotiated": cwrBpiRmTEKEncryptionNegotiated,
       "cwrBpiRmTEKLifetime": cwrBpiRmTEKLifetime,
       "cwrBpiRmTEKExpiresOld": cwrBpiRmTEKExpiresOld,
       "cwrBpiRmTEKExpiresNew": cwrBpiRmTEKExpiresNew,
       "cwrBpiRmTEKReset": cwrBpiRmTEKReset,
       "cwrBpiRmKeyRequests": cwrBpiRmKeyRequests,
       "cwrBpiRmKeyReplies": cwrBpiRmKeyReplies,
       "cwrBpiRmTEKInvalids": cwrBpiRmTEKInvalids,
       "cwrBpiRmTEKInvalidErrorCode": cwrBpiRmTEKInvalidErrorCode,
       "cwrBpiRmTEKInvalidErrorString": cwrBpiRmTEKInvalidErrorString,
       "cwrBpiNotification": cwrBpiNotification,
       "cwrBpiConformance": cwrBpiConformance,
       "cwrBpiCompliances": cwrBpiCompliances,
       "cwrBpiBasicCompliance": cwrBpiBasicCompliance,
       "cwrBpiGroups": cwrBpiGroups,
       "cwrBpiRsGroup": cwrBpiRsGroup,
       "cwrBpiRmGroup": cwrBpiRmGroup}
)
