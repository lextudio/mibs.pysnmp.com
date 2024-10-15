# SNMP MIB module (DOCS-BPI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOCS-BPI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:28 2024
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

(docsIfCmServiceId,
 docsIfCmtsServiceId,
 docsIfMib) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "docsIfCmServiceId",
    "docsIfCmtsServiceId",
    "docsIfMib")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

docsBpiMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 5)
)
docsBpiMIB.setRevisions(
        ("2001-03-13 00:00",
         "2000-11-03 19:30",
         "2000-02-16 19:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DocsBpiMIBObjects_ObjectIdentity = ObjectIdentity
docsBpiMIBObjects = _DocsBpiMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1)
)
_DocsBpiCmObjects_ObjectIdentity = ObjectIdentity
docsBpiCmObjects = _DocsBpiCmObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1)
)
_DocsBpiCmBaseTable_Object = MibTable
docsBpiCmBaseTable = _DocsBpiCmBaseTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    docsBpiCmBaseTable.setStatus("current")
_DocsBpiCmBaseEntry_Object = MibTableRow
docsBpiCmBaseEntry = _DocsBpiCmBaseEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1)
)
docsBpiCmBaseEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsBpiCmBaseEntry.setStatus("current")
_DocsBpiCmPrivacyEnable_Type = TruthValue
_DocsBpiCmPrivacyEnable_Object = MibTableColumn
docsBpiCmPrivacyEnable = _DocsBpiCmPrivacyEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 1),
    _DocsBpiCmPrivacyEnable_Type()
)
docsBpiCmPrivacyEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmPrivacyEnable.setStatus("current")


class _DocsBpiCmPublicKey_Type(OctetString):
    """Custom type docsBpiCmPublicKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(74, 74),
        ValueSizeConstraint(106, 106),
        ValueSizeConstraint(140, 140),
        ValueSizeConstraint(270, 270),
    )


_DocsBpiCmPublicKey_Type.__name__ = "OctetString"
_DocsBpiCmPublicKey_Object = MibTableColumn
docsBpiCmPublicKey = _DocsBpiCmPublicKey_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 2),
    _DocsBpiCmPublicKey_Type()
)
docsBpiCmPublicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmPublicKey.setStatus("current")


class _DocsBpiCmAuthState_Type(Integer32):
    """Custom type docsBpiCmAuthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("authRejectWait", 5),
          ("authWait", 2),
          ("authorized", 3),
          ("reauthWait", 4))
    )


_DocsBpiCmAuthState_Type.__name__ = "Integer32"
_DocsBpiCmAuthState_Object = MibTableColumn
docsBpiCmAuthState = _DocsBpiCmAuthState_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 3),
    _DocsBpiCmAuthState_Type()
)
docsBpiCmAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmAuthState.setStatus("current")


class _DocsBpiCmAuthKeySequenceNumber_Type(Integer32):
    """Custom type docsBpiCmAuthKeySequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DocsBpiCmAuthKeySequenceNumber_Type.__name__ = "Integer32"
_DocsBpiCmAuthKeySequenceNumber_Object = MibTableColumn
docsBpiCmAuthKeySequenceNumber = _DocsBpiCmAuthKeySequenceNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 4),
    _DocsBpiCmAuthKeySequenceNumber_Type()
)
docsBpiCmAuthKeySequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmAuthKeySequenceNumber.setStatus("current")
_DocsBpiCmAuthExpires_Type = DateAndTime
_DocsBpiCmAuthExpires_Object = MibTableColumn
docsBpiCmAuthExpires = _DocsBpiCmAuthExpires_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 5),
    _DocsBpiCmAuthExpires_Type()
)
docsBpiCmAuthExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmAuthExpires.setStatus("current")
_DocsBpiCmAuthReset_Type = TruthValue
_DocsBpiCmAuthReset_Object = MibTableColumn
docsBpiCmAuthReset = _DocsBpiCmAuthReset_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 6),
    _DocsBpiCmAuthReset_Type()
)
docsBpiCmAuthReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsBpiCmAuthReset.setStatus("current")


class _DocsBpiCmAuthGraceTime_Type(Integer32):
    """Custom type docsBpiCmAuthGraceTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_DocsBpiCmAuthGraceTime_Type.__name__ = "Integer32"
_DocsBpiCmAuthGraceTime_Object = MibTableColumn
docsBpiCmAuthGraceTime = _DocsBpiCmAuthGraceTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 7),
    _DocsBpiCmAuthGraceTime_Type()
)
docsBpiCmAuthGraceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmAuthGraceTime.setStatus("current")
if mibBuilder.loadTexts:
    docsBpiCmAuthGraceTime.setUnits("seconds")


class _DocsBpiCmTEKGraceTime_Type(Integer32):
    """Custom type docsBpiCmTEKGraceTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_DocsBpiCmTEKGraceTime_Type.__name__ = "Integer32"
_DocsBpiCmTEKGraceTime_Object = MibTableColumn
docsBpiCmTEKGraceTime = _DocsBpiCmTEKGraceTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 8),
    _DocsBpiCmTEKGraceTime_Type()
)
docsBpiCmTEKGraceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmTEKGraceTime.setStatus("current")
if mibBuilder.loadTexts:
    docsBpiCmTEKGraceTime.setUnits("seconds")


class _DocsBpiCmAuthWaitTimeout_Type(Integer32):
    """Custom type docsBpiCmAuthWaitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_DocsBpiCmAuthWaitTimeout_Type.__name__ = "Integer32"
_DocsBpiCmAuthWaitTimeout_Object = MibTableColumn
docsBpiCmAuthWaitTimeout = _DocsBpiCmAuthWaitTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 9),
    _DocsBpiCmAuthWaitTimeout_Type()
)
docsBpiCmAuthWaitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmAuthWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    docsBpiCmAuthWaitTimeout.setUnits("seconds")


class _DocsBpiCmReauthWaitTimeout_Type(Integer32):
    """Custom type docsBpiCmReauthWaitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_DocsBpiCmReauthWaitTimeout_Type.__name__ = "Integer32"
_DocsBpiCmReauthWaitTimeout_Object = MibTableColumn
docsBpiCmReauthWaitTimeout = _DocsBpiCmReauthWaitTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 10),
    _DocsBpiCmReauthWaitTimeout_Type()
)
docsBpiCmReauthWaitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmReauthWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    docsBpiCmReauthWaitTimeout.setUnits("seconds")


class _DocsBpiCmOpWaitTimeout_Type(Integer32):
    """Custom type docsBpiCmOpWaitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_DocsBpiCmOpWaitTimeout_Type.__name__ = "Integer32"
_DocsBpiCmOpWaitTimeout_Object = MibTableColumn
docsBpiCmOpWaitTimeout = _DocsBpiCmOpWaitTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 11),
    _DocsBpiCmOpWaitTimeout_Type()
)
docsBpiCmOpWaitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmOpWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    docsBpiCmOpWaitTimeout.setUnits("seconds")


class _DocsBpiCmRekeyWaitTimeout_Type(Integer32):
    """Custom type docsBpiCmRekeyWaitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_DocsBpiCmRekeyWaitTimeout_Type.__name__ = "Integer32"
_DocsBpiCmRekeyWaitTimeout_Object = MibTableColumn
docsBpiCmRekeyWaitTimeout = _DocsBpiCmRekeyWaitTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 12),
    _DocsBpiCmRekeyWaitTimeout_Type()
)
docsBpiCmRekeyWaitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmRekeyWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    docsBpiCmRekeyWaitTimeout.setUnits("seconds")


class _DocsBpiCmAuthRejectWaitTimeout_Type(Integer32):
    """Custom type docsBpiCmAuthRejectWaitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_DocsBpiCmAuthRejectWaitTimeout_Type.__name__ = "Integer32"
_DocsBpiCmAuthRejectWaitTimeout_Object = MibTableColumn
docsBpiCmAuthRejectWaitTimeout = _DocsBpiCmAuthRejectWaitTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 13),
    _DocsBpiCmAuthRejectWaitTimeout_Type()
)
docsBpiCmAuthRejectWaitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmAuthRejectWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    docsBpiCmAuthRejectWaitTimeout.setUnits("seconds")
_DocsBpiCmAuthRequests_Type = Counter32
_DocsBpiCmAuthRequests_Object = MibTableColumn
docsBpiCmAuthRequests = _DocsBpiCmAuthRequests_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 14),
    _DocsBpiCmAuthRequests_Type()
)
docsBpiCmAuthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmAuthRequests.setStatus("current")
_DocsBpiCmAuthReplies_Type = Counter32
_DocsBpiCmAuthReplies_Object = MibTableColumn
docsBpiCmAuthReplies = _DocsBpiCmAuthReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 15),
    _DocsBpiCmAuthReplies_Type()
)
docsBpiCmAuthReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmAuthReplies.setStatus("current")
_DocsBpiCmAuthRejects_Type = Counter32
_DocsBpiCmAuthRejects_Object = MibTableColumn
docsBpiCmAuthRejects = _DocsBpiCmAuthRejects_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 16),
    _DocsBpiCmAuthRejects_Type()
)
docsBpiCmAuthRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmAuthRejects.setStatus("current")
_DocsBpiCmAuthInvalids_Type = Counter32
_DocsBpiCmAuthInvalids_Object = MibTableColumn
docsBpiCmAuthInvalids = _DocsBpiCmAuthInvalids_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 17),
    _DocsBpiCmAuthInvalids_Type()
)
docsBpiCmAuthInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmAuthInvalids.setStatus("current")


class _DocsBpiCmAuthRejectErrorCode_Type(Integer32):
    """Custom type docsBpiCmAuthRejectErrorCode based on Integer32"""
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
        *(("none", 1),
          ("unauthorizedCm", 3),
          ("unauthorizedSid", 4),
          ("unknown", 2))
    )


_DocsBpiCmAuthRejectErrorCode_Type.__name__ = "Integer32"
_DocsBpiCmAuthRejectErrorCode_Object = MibTableColumn
docsBpiCmAuthRejectErrorCode = _DocsBpiCmAuthRejectErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 18),
    _DocsBpiCmAuthRejectErrorCode_Type()
)
docsBpiCmAuthRejectErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmAuthRejectErrorCode.setStatus("current")


class _DocsBpiCmAuthRejectErrorString_Type(DisplayString):
    """Custom type docsBpiCmAuthRejectErrorString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DocsBpiCmAuthRejectErrorString_Type.__name__ = "DisplayString"
_DocsBpiCmAuthRejectErrorString_Object = MibTableColumn
docsBpiCmAuthRejectErrorString = _DocsBpiCmAuthRejectErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 19),
    _DocsBpiCmAuthRejectErrorString_Type()
)
docsBpiCmAuthRejectErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmAuthRejectErrorString.setStatus("current")


class _DocsBpiCmAuthInvalidErrorCode_Type(Integer32):
    """Custom type docsBpiCmAuthInvalidErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("invalidKeySequence", 6),
          ("keyRequestAuthenticationFailure", 7),
          ("none", 1),
          ("unauthorizedCm", 3),
          ("unknown", 2),
          ("unsolicited", 5))
    )


_DocsBpiCmAuthInvalidErrorCode_Type.__name__ = "Integer32"
_DocsBpiCmAuthInvalidErrorCode_Object = MibTableColumn
docsBpiCmAuthInvalidErrorCode = _DocsBpiCmAuthInvalidErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 20),
    _DocsBpiCmAuthInvalidErrorCode_Type()
)
docsBpiCmAuthInvalidErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmAuthInvalidErrorCode.setStatus("current")


class _DocsBpiCmAuthInvalidErrorString_Type(DisplayString):
    """Custom type docsBpiCmAuthInvalidErrorString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DocsBpiCmAuthInvalidErrorString_Type.__name__ = "DisplayString"
_DocsBpiCmAuthInvalidErrorString_Object = MibTableColumn
docsBpiCmAuthInvalidErrorString = _DocsBpiCmAuthInvalidErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 1, 1, 21),
    _DocsBpiCmAuthInvalidErrorString_Type()
)
docsBpiCmAuthInvalidErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmAuthInvalidErrorString.setStatus("current")
_DocsBpiCmTEKTable_Object = MibTable
docsBpiCmTEKTable = _DocsBpiCmTEKTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    docsBpiCmTEKTable.setStatus("current")
_DocsBpiCmTEKEntry_Object = MibTableRow
docsBpiCmTEKEntry = _DocsBpiCmTEKEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2, 1)
)
docsBpiCmTEKEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF-MIB", "docsIfCmServiceId"),
)
if mibBuilder.loadTexts:
    docsBpiCmTEKEntry.setStatus("current")
_DocsBpiCmTEKPrivacyEnable_Type = TruthValue
_DocsBpiCmTEKPrivacyEnable_Object = MibTableColumn
docsBpiCmTEKPrivacyEnable = _DocsBpiCmTEKPrivacyEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2, 1, 1),
    _DocsBpiCmTEKPrivacyEnable_Type()
)
docsBpiCmTEKPrivacyEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmTEKPrivacyEnable.setStatus("current")


class _DocsBpiCmTEKState_Type(Integer32):
    """Custom type docsBpiCmTEKState based on Integer32"""
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


_DocsBpiCmTEKState_Type.__name__ = "Integer32"
_DocsBpiCmTEKState_Object = MibTableColumn
docsBpiCmTEKState = _DocsBpiCmTEKState_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2, 1, 2),
    _DocsBpiCmTEKState_Type()
)
docsBpiCmTEKState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmTEKState.setStatus("current")
_DocsBpiCmTEKExpiresOld_Type = DateAndTime
_DocsBpiCmTEKExpiresOld_Object = MibTableColumn
docsBpiCmTEKExpiresOld = _DocsBpiCmTEKExpiresOld_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2, 1, 3),
    _DocsBpiCmTEKExpiresOld_Type()
)
docsBpiCmTEKExpiresOld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmTEKExpiresOld.setStatus("current")
_DocsBpiCmTEKExpiresNew_Type = DateAndTime
_DocsBpiCmTEKExpiresNew_Object = MibTableColumn
docsBpiCmTEKExpiresNew = _DocsBpiCmTEKExpiresNew_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2, 1, 4),
    _DocsBpiCmTEKExpiresNew_Type()
)
docsBpiCmTEKExpiresNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmTEKExpiresNew.setStatus("current")
_DocsBpiCmTEKKeyRequests_Type = Counter32
_DocsBpiCmTEKKeyRequests_Object = MibTableColumn
docsBpiCmTEKKeyRequests = _DocsBpiCmTEKKeyRequests_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2, 1, 5),
    _DocsBpiCmTEKKeyRequests_Type()
)
docsBpiCmTEKKeyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmTEKKeyRequests.setStatus("current")
_DocsBpiCmTEKKeyReplies_Type = Counter32
_DocsBpiCmTEKKeyReplies_Object = MibTableColumn
docsBpiCmTEKKeyReplies = _DocsBpiCmTEKKeyReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2, 1, 6),
    _DocsBpiCmTEKKeyReplies_Type()
)
docsBpiCmTEKKeyReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmTEKKeyReplies.setStatus("current")
_DocsBpiCmTEKKeyRejects_Type = Counter32
_DocsBpiCmTEKKeyRejects_Object = MibTableColumn
docsBpiCmTEKKeyRejects = _DocsBpiCmTEKKeyRejects_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2, 1, 7),
    _DocsBpiCmTEKKeyRejects_Type()
)
docsBpiCmTEKKeyRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmTEKKeyRejects.setStatus("current")
_DocsBpiCmTEKInvalids_Type = Counter32
_DocsBpiCmTEKInvalids_Object = MibTableColumn
docsBpiCmTEKInvalids = _DocsBpiCmTEKInvalids_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2, 1, 8),
    _DocsBpiCmTEKInvalids_Type()
)
docsBpiCmTEKInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmTEKInvalids.setStatus("current")
_DocsBpiCmTEKAuthPends_Type = Counter32
_DocsBpiCmTEKAuthPends_Object = MibTableColumn
docsBpiCmTEKAuthPends = _DocsBpiCmTEKAuthPends_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2, 1, 9),
    _DocsBpiCmTEKAuthPends_Type()
)
docsBpiCmTEKAuthPends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmTEKAuthPends.setStatus("current")


class _DocsBpiCmTEKKeyRejectErrorCode_Type(Integer32):
    """Custom type docsBpiCmTEKKeyRejectErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("unauthorizedSid", 4),
          ("unknown", 2))
    )


_DocsBpiCmTEKKeyRejectErrorCode_Type.__name__ = "Integer32"
_DocsBpiCmTEKKeyRejectErrorCode_Object = MibTableColumn
docsBpiCmTEKKeyRejectErrorCode = _DocsBpiCmTEKKeyRejectErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2, 1, 10),
    _DocsBpiCmTEKKeyRejectErrorCode_Type()
)
docsBpiCmTEKKeyRejectErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmTEKKeyRejectErrorCode.setStatus("current")


class _DocsBpiCmTEKKeyRejectErrorString_Type(DisplayString):
    """Custom type docsBpiCmTEKKeyRejectErrorString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DocsBpiCmTEKKeyRejectErrorString_Type.__name__ = "DisplayString"
_DocsBpiCmTEKKeyRejectErrorString_Object = MibTableColumn
docsBpiCmTEKKeyRejectErrorString = _DocsBpiCmTEKKeyRejectErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2, 1, 11),
    _DocsBpiCmTEKKeyRejectErrorString_Type()
)
docsBpiCmTEKKeyRejectErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmTEKKeyRejectErrorString.setStatus("current")


class _DocsBpiCmTEKInvalidErrorCode_Type(Integer32):
    """Custom type docsBpiCmTEKInvalidErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6)
        )
    )
    namedValues = NamedValues(
        *(("invalidKeySequence", 6),
          ("none", 1),
          ("unknown", 2))
    )


_DocsBpiCmTEKInvalidErrorCode_Type.__name__ = "Integer32"
_DocsBpiCmTEKInvalidErrorCode_Object = MibTableColumn
docsBpiCmTEKInvalidErrorCode = _DocsBpiCmTEKInvalidErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2, 1, 12),
    _DocsBpiCmTEKInvalidErrorCode_Type()
)
docsBpiCmTEKInvalidErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmTEKInvalidErrorCode.setStatus("current")


class _DocsBpiCmTEKInvalidErrorString_Type(DisplayString):
    """Custom type docsBpiCmTEKInvalidErrorString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DocsBpiCmTEKInvalidErrorString_Type.__name__ = "DisplayString"
_DocsBpiCmTEKInvalidErrorString_Object = MibTableColumn
docsBpiCmTEKInvalidErrorString = _DocsBpiCmTEKInvalidErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 1, 2, 1, 13),
    _DocsBpiCmTEKInvalidErrorString_Type()
)
docsBpiCmTEKInvalidErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmTEKInvalidErrorString.setStatus("current")
_DocsBpiCmtsObjects_ObjectIdentity = ObjectIdentity
docsBpiCmtsObjects = _DocsBpiCmtsObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2)
)
_DocsBpiCmtsBaseTable_Object = MibTable
docsBpiCmtsBaseTable = _DocsBpiCmtsBaseTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    docsBpiCmtsBaseTable.setStatus("current")
_DocsBpiCmtsBaseEntry_Object = MibTableRow
docsBpiCmtsBaseEntry = _DocsBpiCmtsBaseEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 1, 1)
)
docsBpiCmtsBaseEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsBpiCmtsBaseEntry.setStatus("current")


class _DocsBpiCmtsDefaultAuthLifetime_Type(Integer32):
    """Custom type docsBpiCmtsDefaultAuthLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6048000),
    )


_DocsBpiCmtsDefaultAuthLifetime_Type.__name__ = "Integer32"
_DocsBpiCmtsDefaultAuthLifetime_Object = MibTableColumn
docsBpiCmtsDefaultAuthLifetime = _DocsBpiCmtsDefaultAuthLifetime_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 1, 1, 1),
    _DocsBpiCmtsDefaultAuthLifetime_Type()
)
docsBpiCmtsDefaultAuthLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsBpiCmtsDefaultAuthLifetime.setStatus("current")
if mibBuilder.loadTexts:
    docsBpiCmtsDefaultAuthLifetime.setUnits("seconds")


class _DocsBpiCmtsDefaultTEKLifetime_Type(Integer32):
    """Custom type docsBpiCmtsDefaultTEKLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_DocsBpiCmtsDefaultTEKLifetime_Type.__name__ = "Integer32"
_DocsBpiCmtsDefaultTEKLifetime_Object = MibTableColumn
docsBpiCmtsDefaultTEKLifetime = _DocsBpiCmtsDefaultTEKLifetime_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 1, 1, 2),
    _DocsBpiCmtsDefaultTEKLifetime_Type()
)
docsBpiCmtsDefaultTEKLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsBpiCmtsDefaultTEKLifetime.setStatus("current")
if mibBuilder.loadTexts:
    docsBpiCmtsDefaultTEKLifetime.setUnits("seconds")


class _DocsBpiCmtsDefaultAuthGraceTime_Type(Integer32):
    """Custom type docsBpiCmtsDefaultAuthGraceTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_DocsBpiCmtsDefaultAuthGraceTime_Type.__name__ = "Integer32"
_DocsBpiCmtsDefaultAuthGraceTime_Object = MibTableColumn
docsBpiCmtsDefaultAuthGraceTime = _DocsBpiCmtsDefaultAuthGraceTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 1, 1, 3),
    _DocsBpiCmtsDefaultAuthGraceTime_Type()
)
docsBpiCmtsDefaultAuthGraceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsBpiCmtsDefaultAuthGraceTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    docsBpiCmtsDefaultAuthGraceTime.setUnits("seconds")


class _DocsBpiCmtsDefaultTEKGraceTime_Type(Integer32):
    """Custom type docsBpiCmtsDefaultTEKGraceTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_DocsBpiCmtsDefaultTEKGraceTime_Type.__name__ = "Integer32"
_DocsBpiCmtsDefaultTEKGraceTime_Object = MibTableColumn
docsBpiCmtsDefaultTEKGraceTime = _DocsBpiCmtsDefaultTEKGraceTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 1, 1, 4),
    _DocsBpiCmtsDefaultTEKGraceTime_Type()
)
docsBpiCmtsDefaultTEKGraceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsBpiCmtsDefaultTEKGraceTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    docsBpiCmtsDefaultTEKGraceTime.setUnits("seconds")
_DocsBpiCmtsAuthRequests_Type = Counter32
_DocsBpiCmtsAuthRequests_Object = MibTableColumn
docsBpiCmtsAuthRequests = _DocsBpiCmtsAuthRequests_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 1, 1, 5),
    _DocsBpiCmtsAuthRequests_Type()
)
docsBpiCmtsAuthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmtsAuthRequests.setStatus("current")
_DocsBpiCmtsAuthReplies_Type = Counter32
_DocsBpiCmtsAuthReplies_Object = MibTableColumn
docsBpiCmtsAuthReplies = _DocsBpiCmtsAuthReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 1, 1, 6),
    _DocsBpiCmtsAuthReplies_Type()
)
docsBpiCmtsAuthReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmtsAuthReplies.setStatus("current")
_DocsBpiCmtsAuthRejects_Type = Counter32
_DocsBpiCmtsAuthRejects_Object = MibTableColumn
docsBpiCmtsAuthRejects = _DocsBpiCmtsAuthRejects_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 1, 1, 7),
    _DocsBpiCmtsAuthRejects_Type()
)
docsBpiCmtsAuthRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmtsAuthRejects.setStatus("current")
_DocsBpiCmtsAuthInvalids_Type = Counter32
_DocsBpiCmtsAuthInvalids_Object = MibTableColumn
docsBpiCmtsAuthInvalids = _DocsBpiCmtsAuthInvalids_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 1, 1, 8),
    _DocsBpiCmtsAuthInvalids_Type()
)
docsBpiCmtsAuthInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmtsAuthInvalids.setStatus("current")
_DocsBpiCmtsAuthTable_Object = MibTable
docsBpiCmtsAuthTable = _DocsBpiCmtsAuthTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2)
)
if mibBuilder.loadTexts:
    docsBpiCmtsAuthTable.setStatus("current")
_DocsBpiCmtsAuthEntry_Object = MibTableRow
docsBpiCmtsAuthEntry = _DocsBpiCmtsAuthEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1)
)
docsBpiCmtsAuthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-BPI-MIB", "docsBpiCmtsAuthCmMacAddress"),
)
if mibBuilder.loadTexts:
    docsBpiCmtsAuthEntry.setStatus("current")
_DocsBpiCmtsAuthCmMacAddress_Type = MacAddress
_DocsBpiCmtsAuthCmMacAddress_Object = MibTableColumn
docsBpiCmtsAuthCmMacAddress = _DocsBpiCmtsAuthCmMacAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 1),
    _DocsBpiCmtsAuthCmMacAddress_Type()
)
docsBpiCmtsAuthCmMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsBpiCmtsAuthCmMacAddress.setStatus("current")


class _DocsBpiCmtsAuthCmPublicKey_Type(OctetString):
    """Custom type docsBpiCmtsAuthCmPublicKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(74, 74),
        ValueSizeConstraint(106, 106),
        ValueSizeConstraint(140, 140),
        ValueSizeConstraint(270, 270),
    )


_DocsBpiCmtsAuthCmPublicKey_Type.__name__ = "OctetString"
_DocsBpiCmtsAuthCmPublicKey_Object = MibTableColumn
docsBpiCmtsAuthCmPublicKey = _DocsBpiCmtsAuthCmPublicKey_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 2),
    _DocsBpiCmtsAuthCmPublicKey_Type()
)
docsBpiCmtsAuthCmPublicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmtsAuthCmPublicKey.setStatus("current")


class _DocsBpiCmtsAuthCmKeySequenceNumber_Type(Integer32):
    """Custom type docsBpiCmtsAuthCmKeySequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DocsBpiCmtsAuthCmKeySequenceNumber_Type.__name__ = "Integer32"
_DocsBpiCmtsAuthCmKeySequenceNumber_Object = MibTableColumn
docsBpiCmtsAuthCmKeySequenceNumber = _DocsBpiCmtsAuthCmKeySequenceNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 3),
    _DocsBpiCmtsAuthCmKeySequenceNumber_Type()
)
docsBpiCmtsAuthCmKeySequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmtsAuthCmKeySequenceNumber.setStatus("current")
_DocsBpiCmtsAuthCmExpires_Type = DateAndTime
_DocsBpiCmtsAuthCmExpires_Object = MibTableColumn
docsBpiCmtsAuthCmExpires = _DocsBpiCmtsAuthCmExpires_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 4),
    _DocsBpiCmtsAuthCmExpires_Type()
)
docsBpiCmtsAuthCmExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmtsAuthCmExpires.setStatus("current")


class _DocsBpiCmtsAuthCmLifetime_Type(Integer32):
    """Custom type docsBpiCmtsAuthCmLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6048000),
    )


_DocsBpiCmtsAuthCmLifetime_Type.__name__ = "Integer32"
_DocsBpiCmtsAuthCmLifetime_Object = MibTableColumn
docsBpiCmtsAuthCmLifetime = _DocsBpiCmtsAuthCmLifetime_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 5),
    _DocsBpiCmtsAuthCmLifetime_Type()
)
docsBpiCmtsAuthCmLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsBpiCmtsAuthCmLifetime.setStatus("current")
if mibBuilder.loadTexts:
    docsBpiCmtsAuthCmLifetime.setUnits("seconds")


class _DocsBpiCmtsAuthCmGraceTime_Type(Integer32):
    """Custom type docsBpiCmtsAuthCmGraceTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_DocsBpiCmtsAuthCmGraceTime_Type.__name__ = "Integer32"
_DocsBpiCmtsAuthCmGraceTime_Object = MibTableColumn
docsBpiCmtsAuthCmGraceTime = _DocsBpiCmtsAuthCmGraceTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 6),
    _DocsBpiCmtsAuthCmGraceTime_Type()
)
docsBpiCmtsAuthCmGraceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmtsAuthCmGraceTime.setStatus("current")
if mibBuilder.loadTexts:
    docsBpiCmtsAuthCmGraceTime.setUnits("seconds")


class _DocsBpiCmtsAuthCmReset_Type(Integer32):
    """Custom type docsBpiCmtsAuthCmReset based on Integer32"""
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
        *(("invalidateAuth", 2),
          ("invalidateTeks", 4),
          ("noResetRequested", 1),
          ("sendAuthInvalid", 3))
    )


_DocsBpiCmtsAuthCmReset_Type.__name__ = "Integer32"
_DocsBpiCmtsAuthCmReset_Object = MibTableColumn
docsBpiCmtsAuthCmReset = _DocsBpiCmtsAuthCmReset_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 7),
    _DocsBpiCmtsAuthCmReset_Type()
)
docsBpiCmtsAuthCmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsBpiCmtsAuthCmReset.setStatus("current")
_DocsBpiCmtsAuthCmRequests_Type = Counter32
_DocsBpiCmtsAuthCmRequests_Object = MibTableColumn
docsBpiCmtsAuthCmRequests = _DocsBpiCmtsAuthCmRequests_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 8),
    _DocsBpiCmtsAuthCmRequests_Type()
)
docsBpiCmtsAuthCmRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmtsAuthCmRequests.setStatus("current")
_DocsBpiCmtsAuthCmReplies_Type = Counter32
_DocsBpiCmtsAuthCmReplies_Object = MibTableColumn
docsBpiCmtsAuthCmReplies = _DocsBpiCmtsAuthCmReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 9),
    _DocsBpiCmtsAuthCmReplies_Type()
)
docsBpiCmtsAuthCmReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmtsAuthCmReplies.setStatus("current")
_DocsBpiCmtsAuthCmRejects_Type = Counter32
_DocsBpiCmtsAuthCmRejects_Object = MibTableColumn
docsBpiCmtsAuthCmRejects = _DocsBpiCmtsAuthCmRejects_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 10),
    _DocsBpiCmtsAuthCmRejects_Type()
)
docsBpiCmtsAuthCmRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmtsAuthCmRejects.setStatus("current")
_DocsBpiCmtsAuthCmInvalids_Type = Counter32
_DocsBpiCmtsAuthCmInvalids_Object = MibTableColumn
docsBpiCmtsAuthCmInvalids = _DocsBpiCmtsAuthCmInvalids_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 11),
    _DocsBpiCmtsAuthCmInvalids_Type()
)
docsBpiCmtsAuthCmInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmtsAuthCmInvalids.setStatus("current")


class _DocsBpiCmtsAuthRejectErrorCode_Type(Integer32):
    """Custom type docsBpiCmtsAuthRejectErrorCode based on Integer32"""
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
        *(("none", 1),
          ("unauthorizedCm", 3),
          ("unauthorizedSid", 4),
          ("unknown", 2))
    )


_DocsBpiCmtsAuthRejectErrorCode_Type.__name__ = "Integer32"
_DocsBpiCmtsAuthRejectErrorCode_Object = MibTableColumn
docsBpiCmtsAuthRejectErrorCode = _DocsBpiCmtsAuthRejectErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 12),
    _DocsBpiCmtsAuthRejectErrorCode_Type()
)
docsBpiCmtsAuthRejectErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmtsAuthRejectErrorCode.setStatus("current")


class _DocsBpiCmtsAuthRejectErrorString_Type(DisplayString):
    """Custom type docsBpiCmtsAuthRejectErrorString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DocsBpiCmtsAuthRejectErrorString_Type.__name__ = "DisplayString"
_DocsBpiCmtsAuthRejectErrorString_Object = MibTableColumn
docsBpiCmtsAuthRejectErrorString = _DocsBpiCmtsAuthRejectErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 13),
    _DocsBpiCmtsAuthRejectErrorString_Type()
)
docsBpiCmtsAuthRejectErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmtsAuthRejectErrorString.setStatus("current")


class _DocsBpiCmtsAuthInvalidErrorCode_Type(Integer32):
    """Custom type docsBpiCmtsAuthInvalidErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("invalidKeySequence", 6),
          ("keyRequestAuthenticationFailure", 7),
          ("none", 1),
          ("unauthorizedCm", 3),
          ("unknown", 2),
          ("unsolicited", 5))
    )


_DocsBpiCmtsAuthInvalidErrorCode_Type.__name__ = "Integer32"
_DocsBpiCmtsAuthInvalidErrorCode_Object = MibTableColumn
docsBpiCmtsAuthInvalidErrorCode = _DocsBpiCmtsAuthInvalidErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 14),
    _DocsBpiCmtsAuthInvalidErrorCode_Type()
)
docsBpiCmtsAuthInvalidErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmtsAuthInvalidErrorCode.setStatus("current")


class _DocsBpiCmtsAuthInvalidErrorString_Type(DisplayString):
    """Custom type docsBpiCmtsAuthInvalidErrorString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DocsBpiCmtsAuthInvalidErrorString_Type.__name__ = "DisplayString"
_DocsBpiCmtsAuthInvalidErrorString_Object = MibTableColumn
docsBpiCmtsAuthInvalidErrorString = _DocsBpiCmtsAuthInvalidErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 2, 1, 15),
    _DocsBpiCmtsAuthInvalidErrorString_Type()
)
docsBpiCmtsAuthInvalidErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmtsAuthInvalidErrorString.setStatus("current")
_DocsBpiCmtsTEKTable_Object = MibTable
docsBpiCmtsTEKTable = _DocsBpiCmtsTEKTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3)
)
if mibBuilder.loadTexts:
    docsBpiCmtsTEKTable.setStatus("current")
_DocsBpiCmtsTEKEntry_Object = MibTableRow
docsBpiCmtsTEKEntry = _DocsBpiCmtsTEKEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3, 1)
)
docsBpiCmtsTEKEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF-MIB", "docsIfCmtsServiceId"),
)
if mibBuilder.loadTexts:
    docsBpiCmtsTEKEntry.setStatus("current")


class _DocsBpiCmtsTEKLifetime_Type(Integer32):
    """Custom type docsBpiCmtsTEKLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_DocsBpiCmtsTEKLifetime_Type.__name__ = "Integer32"
_DocsBpiCmtsTEKLifetime_Object = MibTableColumn
docsBpiCmtsTEKLifetime = _DocsBpiCmtsTEKLifetime_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3, 1, 1),
    _DocsBpiCmtsTEKLifetime_Type()
)
docsBpiCmtsTEKLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsBpiCmtsTEKLifetime.setStatus("current")
if mibBuilder.loadTexts:
    docsBpiCmtsTEKLifetime.setUnits("seconds")


class _DocsBpiCmtsTEKGraceTime_Type(Integer32):
    """Custom type docsBpiCmtsTEKGraceTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_DocsBpiCmtsTEKGraceTime_Type.__name__ = "Integer32"
_DocsBpiCmtsTEKGraceTime_Object = MibTableColumn
docsBpiCmtsTEKGraceTime = _DocsBpiCmtsTEKGraceTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3, 1, 2),
    _DocsBpiCmtsTEKGraceTime_Type()
)
docsBpiCmtsTEKGraceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmtsTEKGraceTime.setStatus("current")
if mibBuilder.loadTexts:
    docsBpiCmtsTEKGraceTime.setUnits("seconds")
_DocsBpiCmtsTEKExpiresOld_Type = DateAndTime
_DocsBpiCmtsTEKExpiresOld_Object = MibTableColumn
docsBpiCmtsTEKExpiresOld = _DocsBpiCmtsTEKExpiresOld_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3, 1, 3),
    _DocsBpiCmtsTEKExpiresOld_Type()
)
docsBpiCmtsTEKExpiresOld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmtsTEKExpiresOld.setStatus("current")
_DocsBpiCmtsTEKExpiresNew_Type = DateAndTime
_DocsBpiCmtsTEKExpiresNew_Object = MibTableColumn
docsBpiCmtsTEKExpiresNew = _DocsBpiCmtsTEKExpiresNew_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3, 1, 4),
    _DocsBpiCmtsTEKExpiresNew_Type()
)
docsBpiCmtsTEKExpiresNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmtsTEKExpiresNew.setStatus("current")
_DocsBpiCmtsTEKReset_Type = TruthValue
_DocsBpiCmtsTEKReset_Object = MibTableColumn
docsBpiCmtsTEKReset = _DocsBpiCmtsTEKReset_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3, 1, 5),
    _DocsBpiCmtsTEKReset_Type()
)
docsBpiCmtsTEKReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsBpiCmtsTEKReset.setStatus("current")
_DocsBpiCmtsKeyRequests_Type = Counter32
_DocsBpiCmtsKeyRequests_Object = MibTableColumn
docsBpiCmtsKeyRequests = _DocsBpiCmtsKeyRequests_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3, 1, 6),
    _DocsBpiCmtsKeyRequests_Type()
)
docsBpiCmtsKeyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmtsKeyRequests.setStatus("current")
_DocsBpiCmtsKeyReplies_Type = Counter32
_DocsBpiCmtsKeyReplies_Object = MibTableColumn
docsBpiCmtsKeyReplies = _DocsBpiCmtsKeyReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3, 1, 7),
    _DocsBpiCmtsKeyReplies_Type()
)
docsBpiCmtsKeyReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmtsKeyReplies.setStatus("current")
_DocsBpiCmtsKeyRejects_Type = Counter32
_DocsBpiCmtsKeyRejects_Object = MibTableColumn
docsBpiCmtsKeyRejects = _DocsBpiCmtsKeyRejects_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3, 1, 8),
    _DocsBpiCmtsKeyRejects_Type()
)
docsBpiCmtsKeyRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmtsKeyRejects.setStatus("current")
_DocsBpiCmtsTEKInvalids_Type = Counter32
_DocsBpiCmtsTEKInvalids_Object = MibTableColumn
docsBpiCmtsTEKInvalids = _DocsBpiCmtsTEKInvalids_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3, 1, 9),
    _DocsBpiCmtsTEKInvalids_Type()
)
docsBpiCmtsTEKInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmtsTEKInvalids.setStatus("current")


class _DocsBpiCmtsKeyRejectErrorCode_Type(Integer32):
    """Custom type docsBpiCmtsKeyRejectErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("unauthorizedSid", 4),
          ("unknown", 2))
    )


_DocsBpiCmtsKeyRejectErrorCode_Type.__name__ = "Integer32"
_DocsBpiCmtsKeyRejectErrorCode_Object = MibTableColumn
docsBpiCmtsKeyRejectErrorCode = _DocsBpiCmtsKeyRejectErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3, 1, 10),
    _DocsBpiCmtsKeyRejectErrorCode_Type()
)
docsBpiCmtsKeyRejectErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmtsKeyRejectErrorCode.setStatus("current")


class _DocsBpiCmtsKeyRejectErrorString_Type(DisplayString):
    """Custom type docsBpiCmtsKeyRejectErrorString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DocsBpiCmtsKeyRejectErrorString_Type.__name__ = "DisplayString"
_DocsBpiCmtsKeyRejectErrorString_Object = MibTableColumn
docsBpiCmtsKeyRejectErrorString = _DocsBpiCmtsKeyRejectErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3, 1, 11),
    _DocsBpiCmtsKeyRejectErrorString_Type()
)
docsBpiCmtsKeyRejectErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmtsKeyRejectErrorString.setStatus("current")


class _DocsBpiCmtsTEKInvalidErrorCode_Type(Integer32):
    """Custom type docsBpiCmtsTEKInvalidErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6)
        )
    )
    namedValues = NamedValues(
        *(("invalidKeySequence", 6),
          ("none", 1),
          ("unknown", 2))
    )


_DocsBpiCmtsTEKInvalidErrorCode_Type.__name__ = "Integer32"
_DocsBpiCmtsTEKInvalidErrorCode_Object = MibTableColumn
docsBpiCmtsTEKInvalidErrorCode = _DocsBpiCmtsTEKInvalidErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3, 1, 12),
    _DocsBpiCmtsTEKInvalidErrorCode_Type()
)
docsBpiCmtsTEKInvalidErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmtsTEKInvalidErrorCode.setStatus("current")


class _DocsBpiCmtsTEKInvalidErrorString_Type(DisplayString):
    """Custom type docsBpiCmtsTEKInvalidErrorString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DocsBpiCmtsTEKInvalidErrorString_Type.__name__ = "DisplayString"
_DocsBpiCmtsTEKInvalidErrorString_Object = MibTableColumn
docsBpiCmtsTEKInvalidErrorString = _DocsBpiCmtsTEKInvalidErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 3, 1, 13),
    _DocsBpiCmtsTEKInvalidErrorString_Type()
)
docsBpiCmtsTEKInvalidErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpiCmtsTEKInvalidErrorString.setStatus("current")
_DocsBpiMulticastControl_ObjectIdentity = ObjectIdentity
docsBpiMulticastControl = _DocsBpiMulticastControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 4)
)
_DocsBpiIpMulticastMapTable_Object = MibTable
docsBpiIpMulticastMapTable = _DocsBpiIpMulticastMapTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    docsBpiIpMulticastMapTable.setStatus("current")
_DocsBpiIpMulticastMapEntry_Object = MibTableRow
docsBpiIpMulticastMapEntry = _DocsBpiIpMulticastMapEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 4, 1, 1)
)
docsBpiIpMulticastMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-BPI-MIB", "docsBpiIpMulticastAddress"),
    (0, "DOCS-BPI-MIB", "docsBpiIpMulticastPrefixLength"),
)
if mibBuilder.loadTexts:
    docsBpiIpMulticastMapEntry.setStatus("current")
_DocsBpiIpMulticastAddress_Type = IpAddress
_DocsBpiIpMulticastAddress_Object = MibTableColumn
docsBpiIpMulticastAddress = _DocsBpiIpMulticastAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 4, 1, 1, 1),
    _DocsBpiIpMulticastAddress_Type()
)
docsBpiIpMulticastAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsBpiIpMulticastAddress.setStatus("current")


class _DocsBpiIpMulticastPrefixLength_Type(Integer32):
    """Custom type docsBpiIpMulticastPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_DocsBpiIpMulticastPrefixLength_Type.__name__ = "Integer32"
_DocsBpiIpMulticastPrefixLength_Object = MibTableColumn
docsBpiIpMulticastPrefixLength = _DocsBpiIpMulticastPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 4, 1, 1, 2),
    _DocsBpiIpMulticastPrefixLength_Type()
)
docsBpiIpMulticastPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsBpiIpMulticastPrefixLength.setStatus("current")


class _DocsBpiIpMulticastServiceId_Type(Integer32):
    """Custom type docsBpiIpMulticastServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8192, 16368),
    )


_DocsBpiIpMulticastServiceId_Type.__name__ = "Integer32"
_DocsBpiIpMulticastServiceId_Object = MibTableColumn
docsBpiIpMulticastServiceId = _DocsBpiIpMulticastServiceId_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 4, 1, 1, 3),
    _DocsBpiIpMulticastServiceId_Type()
)
docsBpiIpMulticastServiceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsBpiIpMulticastServiceId.setStatus("current")
_DocsBpiIpMulticastMapControl_Type = RowStatus
_DocsBpiIpMulticastMapControl_Object = MibTableColumn
docsBpiIpMulticastMapControl = _DocsBpiIpMulticastMapControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 4, 1, 1, 4),
    _DocsBpiIpMulticastMapControl_Type()
)
docsBpiIpMulticastMapControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsBpiIpMulticastMapControl.setStatus("current")
_DocsBpiMulticastAuthTable_Object = MibTable
docsBpiMulticastAuthTable = _DocsBpiMulticastAuthTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    docsBpiMulticastAuthTable.setStatus("current")
_DocsBpiMulticastAuthEntry_Object = MibTableRow
docsBpiMulticastAuthEntry = _DocsBpiMulticastAuthEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 4, 2, 1)
)
docsBpiMulticastAuthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-BPI-MIB", "docsBpiMulticastServiceId"),
    (0, "DOCS-BPI-MIB", "docsBpiMulticastCmMacAddress"),
)
if mibBuilder.loadTexts:
    docsBpiMulticastAuthEntry.setStatus("current")


class _DocsBpiMulticastServiceId_Type(Integer32):
    """Custom type docsBpiMulticastServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8192, 16368),
    )


_DocsBpiMulticastServiceId_Type.__name__ = "Integer32"
_DocsBpiMulticastServiceId_Object = MibTableColumn
docsBpiMulticastServiceId = _DocsBpiMulticastServiceId_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 4, 2, 1, 1),
    _DocsBpiMulticastServiceId_Type()
)
docsBpiMulticastServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsBpiMulticastServiceId.setStatus("current")
_DocsBpiMulticastCmMacAddress_Type = MacAddress
_DocsBpiMulticastCmMacAddress_Object = MibTableColumn
docsBpiMulticastCmMacAddress = _DocsBpiMulticastCmMacAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 4, 2, 1, 2),
    _DocsBpiMulticastCmMacAddress_Type()
)
docsBpiMulticastCmMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsBpiMulticastCmMacAddress.setStatus("current")
_DocsBpiMulticastAuthControl_Type = RowStatus
_DocsBpiMulticastAuthControl_Object = MibTableColumn
docsBpiMulticastAuthControl = _DocsBpiMulticastAuthControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 1, 2, 4, 2, 1, 3),
    _DocsBpiMulticastAuthControl_Type()
)
docsBpiMulticastAuthControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsBpiMulticastAuthControl.setStatus("current")
_DocsBpiNotification_ObjectIdentity = ObjectIdentity
docsBpiNotification = _DocsBpiNotification_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 2)
)
_DocsBpiConformance_ObjectIdentity = ObjectIdentity
docsBpiConformance = _DocsBpiConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 3)
)
_DocsBpiCompliances_ObjectIdentity = ObjectIdentity
docsBpiCompliances = _DocsBpiCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 3, 1)
)
_DocsBpiGroups_ObjectIdentity = ObjectIdentity
docsBpiGroups = _DocsBpiGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 3, 2)
)

# Managed Objects groups

docsBpiCmGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 3, 2, 1)
)
docsBpiCmGroup.setObjects(
      *(("DOCS-BPI-MIB", "docsBpiCmPrivacyEnable"),
        ("DOCS-BPI-MIB", "docsBpiCmPublicKey"),
        ("DOCS-BPI-MIB", "docsBpiCmAuthState"),
        ("DOCS-BPI-MIB", "docsBpiCmAuthKeySequenceNumber"),
        ("DOCS-BPI-MIB", "docsBpiCmAuthExpires"),
        ("DOCS-BPI-MIB", "docsBpiCmAuthReset"),
        ("DOCS-BPI-MIB", "docsBpiCmAuthGraceTime"),
        ("DOCS-BPI-MIB", "docsBpiCmTEKGraceTime"),
        ("DOCS-BPI-MIB", "docsBpiCmAuthWaitTimeout"),
        ("DOCS-BPI-MIB", "docsBpiCmReauthWaitTimeout"),
        ("DOCS-BPI-MIB", "docsBpiCmOpWaitTimeout"),
        ("DOCS-BPI-MIB", "docsBpiCmRekeyWaitTimeout"),
        ("DOCS-BPI-MIB", "docsBpiCmAuthRejectWaitTimeout"),
        ("DOCS-BPI-MIB", "docsBpiCmAuthRequests"),
        ("DOCS-BPI-MIB", "docsBpiCmAuthReplies"),
        ("DOCS-BPI-MIB", "docsBpiCmAuthRejects"),
        ("DOCS-BPI-MIB", "docsBpiCmAuthInvalids"),
        ("DOCS-BPI-MIB", "docsBpiCmAuthRejectErrorCode"),
        ("DOCS-BPI-MIB", "docsBpiCmAuthRejectErrorString"),
        ("DOCS-BPI-MIB", "docsBpiCmAuthInvalidErrorCode"),
        ("DOCS-BPI-MIB", "docsBpiCmAuthInvalidErrorString"),
        ("DOCS-BPI-MIB", "docsBpiCmTEKPrivacyEnable"),
        ("DOCS-BPI-MIB", "docsBpiCmTEKState"),
        ("DOCS-BPI-MIB", "docsBpiCmTEKExpiresOld"),
        ("DOCS-BPI-MIB", "docsBpiCmTEKExpiresNew"),
        ("DOCS-BPI-MIB", "docsBpiCmTEKKeyRequests"),
        ("DOCS-BPI-MIB", "docsBpiCmTEKKeyReplies"),
        ("DOCS-BPI-MIB", "docsBpiCmTEKKeyRejects"),
        ("DOCS-BPI-MIB", "docsBpiCmTEKInvalids"),
        ("DOCS-BPI-MIB", "docsBpiCmTEKAuthPends"),
        ("DOCS-BPI-MIB", "docsBpiCmTEKKeyRejectErrorCode"),
        ("DOCS-BPI-MIB", "docsBpiCmTEKKeyRejectErrorString"),
        ("DOCS-BPI-MIB", "docsBpiCmTEKInvalidErrorCode"),
        ("DOCS-BPI-MIB", "docsBpiCmTEKInvalidErrorString"))
)
if mibBuilder.loadTexts:
    docsBpiCmGroup.setStatus("current")

docsBpiCmtsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 3, 2, 2)
)
docsBpiCmtsGroup.setObjects(
      *(("DOCS-BPI-MIB", "docsBpiCmtsDefaultAuthLifetime"),
        ("DOCS-BPI-MIB", "docsBpiCmtsDefaultTEKLifetime"),
        ("DOCS-BPI-MIB", "docsBpiCmtsAuthRequests"),
        ("DOCS-BPI-MIB", "docsBpiCmtsAuthReplies"),
        ("DOCS-BPI-MIB", "docsBpiCmtsAuthRejects"),
        ("DOCS-BPI-MIB", "docsBpiCmtsAuthInvalids"),
        ("DOCS-BPI-MIB", "docsBpiCmtsAuthCmPublicKey"),
        ("DOCS-BPI-MIB", "docsBpiCmtsAuthCmKeySequenceNumber"),
        ("DOCS-BPI-MIB", "docsBpiCmtsAuthCmExpires"),
        ("DOCS-BPI-MIB", "docsBpiCmtsAuthCmLifetime"),
        ("DOCS-BPI-MIB", "docsBpiCmtsAuthCmGraceTime"),
        ("DOCS-BPI-MIB", "docsBpiCmtsAuthCmReset"),
        ("DOCS-BPI-MIB", "docsBpiCmtsAuthCmRequests"),
        ("DOCS-BPI-MIB", "docsBpiCmtsAuthCmReplies"),
        ("DOCS-BPI-MIB", "docsBpiCmtsAuthCmRejects"),
        ("DOCS-BPI-MIB", "docsBpiCmtsAuthCmInvalids"),
        ("DOCS-BPI-MIB", "docsBpiCmtsAuthRejectErrorCode"),
        ("DOCS-BPI-MIB", "docsBpiCmtsAuthRejectErrorString"),
        ("DOCS-BPI-MIB", "docsBpiCmtsAuthInvalidErrorCode"),
        ("DOCS-BPI-MIB", "docsBpiCmtsAuthInvalidErrorString"),
        ("DOCS-BPI-MIB", "docsBpiCmtsTEKLifetime"),
        ("DOCS-BPI-MIB", "docsBpiCmtsTEKGraceTime"),
        ("DOCS-BPI-MIB", "docsBpiCmtsTEKExpiresOld"),
        ("DOCS-BPI-MIB", "docsBpiCmtsTEKExpiresNew"),
        ("DOCS-BPI-MIB", "docsBpiCmtsTEKReset"),
        ("DOCS-BPI-MIB", "docsBpiCmtsKeyRequests"),
        ("DOCS-BPI-MIB", "docsBpiCmtsKeyReplies"),
        ("DOCS-BPI-MIB", "docsBpiCmtsKeyRejects"),
        ("DOCS-BPI-MIB", "docsBpiCmtsTEKInvalids"),
        ("DOCS-BPI-MIB", "docsBpiCmtsKeyRejectErrorCode"),
        ("DOCS-BPI-MIB", "docsBpiCmtsKeyRejectErrorString"),
        ("DOCS-BPI-MIB", "docsBpiCmtsTEKInvalidErrorCode"),
        ("DOCS-BPI-MIB", "docsBpiCmtsTEKInvalidErrorString"),
        ("DOCS-BPI-MIB", "docsBpiIpMulticastServiceId"),
        ("DOCS-BPI-MIB", "docsBpiIpMulticastMapControl"),
        ("DOCS-BPI-MIB", "docsBpiMulticastAuthControl"))
)
if mibBuilder.loadTexts:
    docsBpiCmtsGroup.setStatus("current")

docsBpiObsoleteObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 3, 2, 3)
)
docsBpiObsoleteObjectsGroup.setObjects(
      *(("DOCS-BPI-MIB", "docsBpiCmtsDefaultAuthGraceTime"),
        ("DOCS-BPI-MIB", "docsBpiCmtsDefaultTEKGraceTime"))
)
if mibBuilder.loadTexts:
    docsBpiObsoleteObjectsGroup.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

docsBpiBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 127, 5, 3, 1, 1)
)
if mibBuilder.loadTexts:
    docsBpiBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-BPI-MIB",
    **{"docsBpiMIB": docsBpiMIB,
       "docsBpiMIBObjects": docsBpiMIBObjects,
       "docsBpiCmObjects": docsBpiCmObjects,
       "docsBpiCmBaseTable": docsBpiCmBaseTable,
       "docsBpiCmBaseEntry": docsBpiCmBaseEntry,
       "docsBpiCmPrivacyEnable": docsBpiCmPrivacyEnable,
       "docsBpiCmPublicKey": docsBpiCmPublicKey,
       "docsBpiCmAuthState": docsBpiCmAuthState,
       "docsBpiCmAuthKeySequenceNumber": docsBpiCmAuthKeySequenceNumber,
       "docsBpiCmAuthExpires": docsBpiCmAuthExpires,
       "docsBpiCmAuthReset": docsBpiCmAuthReset,
       "docsBpiCmAuthGraceTime": docsBpiCmAuthGraceTime,
       "docsBpiCmTEKGraceTime": docsBpiCmTEKGraceTime,
       "docsBpiCmAuthWaitTimeout": docsBpiCmAuthWaitTimeout,
       "docsBpiCmReauthWaitTimeout": docsBpiCmReauthWaitTimeout,
       "docsBpiCmOpWaitTimeout": docsBpiCmOpWaitTimeout,
       "docsBpiCmRekeyWaitTimeout": docsBpiCmRekeyWaitTimeout,
       "docsBpiCmAuthRejectWaitTimeout": docsBpiCmAuthRejectWaitTimeout,
       "docsBpiCmAuthRequests": docsBpiCmAuthRequests,
       "docsBpiCmAuthReplies": docsBpiCmAuthReplies,
       "docsBpiCmAuthRejects": docsBpiCmAuthRejects,
       "docsBpiCmAuthInvalids": docsBpiCmAuthInvalids,
       "docsBpiCmAuthRejectErrorCode": docsBpiCmAuthRejectErrorCode,
       "docsBpiCmAuthRejectErrorString": docsBpiCmAuthRejectErrorString,
       "docsBpiCmAuthInvalidErrorCode": docsBpiCmAuthInvalidErrorCode,
       "docsBpiCmAuthInvalidErrorString": docsBpiCmAuthInvalidErrorString,
       "docsBpiCmTEKTable": docsBpiCmTEKTable,
       "docsBpiCmTEKEntry": docsBpiCmTEKEntry,
       "docsBpiCmTEKPrivacyEnable": docsBpiCmTEKPrivacyEnable,
       "docsBpiCmTEKState": docsBpiCmTEKState,
       "docsBpiCmTEKExpiresOld": docsBpiCmTEKExpiresOld,
       "docsBpiCmTEKExpiresNew": docsBpiCmTEKExpiresNew,
       "docsBpiCmTEKKeyRequests": docsBpiCmTEKKeyRequests,
       "docsBpiCmTEKKeyReplies": docsBpiCmTEKKeyReplies,
       "docsBpiCmTEKKeyRejects": docsBpiCmTEKKeyRejects,
       "docsBpiCmTEKInvalids": docsBpiCmTEKInvalids,
       "docsBpiCmTEKAuthPends": docsBpiCmTEKAuthPends,
       "docsBpiCmTEKKeyRejectErrorCode": docsBpiCmTEKKeyRejectErrorCode,
       "docsBpiCmTEKKeyRejectErrorString": docsBpiCmTEKKeyRejectErrorString,
       "docsBpiCmTEKInvalidErrorCode": docsBpiCmTEKInvalidErrorCode,
       "docsBpiCmTEKInvalidErrorString": docsBpiCmTEKInvalidErrorString,
       "docsBpiCmtsObjects": docsBpiCmtsObjects,
       "docsBpiCmtsBaseTable": docsBpiCmtsBaseTable,
       "docsBpiCmtsBaseEntry": docsBpiCmtsBaseEntry,
       "docsBpiCmtsDefaultAuthLifetime": docsBpiCmtsDefaultAuthLifetime,
       "docsBpiCmtsDefaultTEKLifetime": docsBpiCmtsDefaultTEKLifetime,
       "docsBpiCmtsDefaultAuthGraceTime": docsBpiCmtsDefaultAuthGraceTime,
       "docsBpiCmtsDefaultTEKGraceTime": docsBpiCmtsDefaultTEKGraceTime,
       "docsBpiCmtsAuthRequests": docsBpiCmtsAuthRequests,
       "docsBpiCmtsAuthReplies": docsBpiCmtsAuthReplies,
       "docsBpiCmtsAuthRejects": docsBpiCmtsAuthRejects,
       "docsBpiCmtsAuthInvalids": docsBpiCmtsAuthInvalids,
       "docsBpiCmtsAuthTable": docsBpiCmtsAuthTable,
       "docsBpiCmtsAuthEntry": docsBpiCmtsAuthEntry,
       "docsBpiCmtsAuthCmMacAddress": docsBpiCmtsAuthCmMacAddress,
       "docsBpiCmtsAuthCmPublicKey": docsBpiCmtsAuthCmPublicKey,
       "docsBpiCmtsAuthCmKeySequenceNumber": docsBpiCmtsAuthCmKeySequenceNumber,
       "docsBpiCmtsAuthCmExpires": docsBpiCmtsAuthCmExpires,
       "docsBpiCmtsAuthCmLifetime": docsBpiCmtsAuthCmLifetime,
       "docsBpiCmtsAuthCmGraceTime": docsBpiCmtsAuthCmGraceTime,
       "docsBpiCmtsAuthCmReset": docsBpiCmtsAuthCmReset,
       "docsBpiCmtsAuthCmRequests": docsBpiCmtsAuthCmRequests,
       "docsBpiCmtsAuthCmReplies": docsBpiCmtsAuthCmReplies,
       "docsBpiCmtsAuthCmRejects": docsBpiCmtsAuthCmRejects,
       "docsBpiCmtsAuthCmInvalids": docsBpiCmtsAuthCmInvalids,
       "docsBpiCmtsAuthRejectErrorCode": docsBpiCmtsAuthRejectErrorCode,
       "docsBpiCmtsAuthRejectErrorString": docsBpiCmtsAuthRejectErrorString,
       "docsBpiCmtsAuthInvalidErrorCode": docsBpiCmtsAuthInvalidErrorCode,
       "docsBpiCmtsAuthInvalidErrorString": docsBpiCmtsAuthInvalidErrorString,
       "docsBpiCmtsTEKTable": docsBpiCmtsTEKTable,
       "docsBpiCmtsTEKEntry": docsBpiCmtsTEKEntry,
       "docsBpiCmtsTEKLifetime": docsBpiCmtsTEKLifetime,
       "docsBpiCmtsTEKGraceTime": docsBpiCmtsTEKGraceTime,
       "docsBpiCmtsTEKExpiresOld": docsBpiCmtsTEKExpiresOld,
       "docsBpiCmtsTEKExpiresNew": docsBpiCmtsTEKExpiresNew,
       "docsBpiCmtsTEKReset": docsBpiCmtsTEKReset,
       "docsBpiCmtsKeyRequests": docsBpiCmtsKeyRequests,
       "docsBpiCmtsKeyReplies": docsBpiCmtsKeyReplies,
       "docsBpiCmtsKeyRejects": docsBpiCmtsKeyRejects,
       "docsBpiCmtsTEKInvalids": docsBpiCmtsTEKInvalids,
       "docsBpiCmtsKeyRejectErrorCode": docsBpiCmtsKeyRejectErrorCode,
       "docsBpiCmtsKeyRejectErrorString": docsBpiCmtsKeyRejectErrorString,
       "docsBpiCmtsTEKInvalidErrorCode": docsBpiCmtsTEKInvalidErrorCode,
       "docsBpiCmtsTEKInvalidErrorString": docsBpiCmtsTEKInvalidErrorString,
       "docsBpiMulticastControl": docsBpiMulticastControl,
       "docsBpiIpMulticastMapTable": docsBpiIpMulticastMapTable,
       "docsBpiIpMulticastMapEntry": docsBpiIpMulticastMapEntry,
       "docsBpiIpMulticastAddress": docsBpiIpMulticastAddress,
       "docsBpiIpMulticastPrefixLength": docsBpiIpMulticastPrefixLength,
       "docsBpiIpMulticastServiceId": docsBpiIpMulticastServiceId,
       "docsBpiIpMulticastMapControl": docsBpiIpMulticastMapControl,
       "docsBpiMulticastAuthTable": docsBpiMulticastAuthTable,
       "docsBpiMulticastAuthEntry": docsBpiMulticastAuthEntry,
       "docsBpiMulticastServiceId": docsBpiMulticastServiceId,
       "docsBpiMulticastCmMacAddress": docsBpiMulticastCmMacAddress,
       "docsBpiMulticastAuthControl": docsBpiMulticastAuthControl,
       "docsBpiNotification": docsBpiNotification,
       "docsBpiConformance": docsBpiConformance,
       "docsBpiCompliances": docsBpiCompliances,
       "docsBpiBasicCompliance": docsBpiBasicCompliance,
       "docsBpiGroups": docsBpiGroups,
       "docsBpiCmGroup": docsBpiCmGroup,
       "docsBpiCmtsGroup": docsBpiCmtsGroup,
       "docsBpiObsoleteObjectsGroup": docsBpiObsoleteObjectsGroup}
)
