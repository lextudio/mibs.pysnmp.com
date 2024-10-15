# SNMP MIB module (ASCEND-MIBXAUTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBXAUTH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:36 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibradStatProfile_ObjectIdentity = ObjectIdentity
mibradStatProfile = _MibradStatProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 141)
)
_MibradStatProfileTable_Object = MibTable
mibradStatProfileTable = _MibradStatProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 141, 1)
)
if mibBuilder.loadTexts:
    mibradStatProfileTable.setStatus("mandatory")
_MibradStatProfileEntry_Object = MibTableRow
mibradStatProfileEntry = _MibradStatProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 141, 1, 1)
)
mibradStatProfileEntry.setIndexNames(
    (0, "ASCEND-MIBXAUTH-MIB", "radStatProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibradStatProfileEntry.setStatus("mandatory")
_RadStatProfile_Index_o_Type = Integer32
_RadStatProfile_Index_o_Object = MibScalar
radStatProfile_Index_o = _RadStatProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 141, 1, 1, 1),
    _RadStatProfile_Index_o_Type()
)
radStatProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radStatProfile_Index_o.setStatus("mandatory")
_RadStatProfile_CurrentAuthServer_Type = Integer32
_RadStatProfile_CurrentAuthServer_Object = MibScalar
radStatProfile_CurrentAuthServer = _RadStatProfile_CurrentAuthServer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 141, 1, 1, 2),
    _RadStatProfile_CurrentAuthServer_Type()
)
radStatProfile_CurrentAuthServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radStatProfile_CurrentAuthServer.setStatus("mandatory")
_RadStatProfile_CurrentAcctServer_Type = Integer32
_RadStatProfile_CurrentAcctServer_Object = MibScalar
radStatProfile_CurrentAcctServer = _RadStatProfile_CurrentAcctServer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 141, 1, 1, 3),
    _RadStatProfile_CurrentAcctServer_Type()
)
radStatProfile_CurrentAcctServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radStatProfile_CurrentAcctServer.setStatus("mandatory")


class _RadStatProfile_Action_o_Type(Integer32):
    """Custom type radStatProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_RadStatProfile_Action_o_Type.__name__ = "Integer32"
_RadStatProfile_Action_o_Object = MibScalar
radStatProfile_Action_o = _RadStatProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 141, 1, 1, 4),
    _RadStatProfile_Action_o_Type()
)
radStatProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radStatProfile_Action_o.setStatus("mandatory")
_MibexternalAuthProfile_ObjectIdentity = ObjectIdentity
mibexternalAuthProfile = _MibexternalAuthProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 142)
)
_MibexternalAuthProfileTable_Object = MibTable
mibexternalAuthProfileTable = _MibexternalAuthProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1)
)
if mibBuilder.loadTexts:
    mibexternalAuthProfileTable.setStatus("mandatory")
_MibexternalAuthProfileEntry_Object = MibTableRow
mibexternalAuthProfileEntry = _MibexternalAuthProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1)
)
mibexternalAuthProfileEntry.setIndexNames(
    (0, "ASCEND-MIBXAUTH-MIB", "externalAuthProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibexternalAuthProfileEntry.setStatus("mandatory")
_ExternalAuthProfile_Index_o_Type = Integer32
_ExternalAuthProfile_Index_o_Object = MibScalar
externalAuthProfile_Index_o = _ExternalAuthProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 1),
    _ExternalAuthProfile_Index_o_Type()
)
externalAuthProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalAuthProfile_Index_o.setStatus("mandatory")


class _ExternalAuthProfile_AuthType_Type(Integer32):
    """Custom type externalAuthProfile_AuthType based on Integer32"""
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
        *(("dEFENDER", 7),
          ("none", 1),
          ("rADIUS", 3),
          ("rADIUS-LOGOUT", 4),
          ("sECURID", 5),
          ("tACACS", 2),
          ("tACACSPLUS", 6))
    )


_ExternalAuthProfile_AuthType_Type.__name__ = "Integer32"
_ExternalAuthProfile_AuthType_Object = MibScalar
externalAuthProfile_AuthType = _ExternalAuthProfile_AuthType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 2),
    _ExternalAuthProfile_AuthType_Type()
)
externalAuthProfile_AuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_AuthType.setStatus("mandatory")


class _ExternalAuthProfile_AcctType_Type(Integer32):
    """Custom type externalAuthProfile_AcctType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("radius", 2),
          ("tacacsplus", 3))
    )


_ExternalAuthProfile_AcctType_Type.__name__ = "Integer32"
_ExternalAuthProfile_AcctType_Object = MibScalar
externalAuthProfile_AcctType = _ExternalAuthProfile_AcctType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 3),
    _ExternalAuthProfile_AcctType_Type()
)
externalAuthProfile_AcctType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_AcctType.setStatus("mandatory")


class _ExternalAuthProfile_RadServEnable_Type(Integer32):
    """Custom type externalAuthProfile_RadServEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ExternalAuthProfile_RadServEnable_Type.__name__ = "Integer32"
_ExternalAuthProfile_RadServEnable_Object = MibScalar
externalAuthProfile_RadServEnable = _ExternalAuthProfile_RadServEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 4),
    _ExternalAuthProfile_RadServEnable_Type()
)
externalAuthProfile_RadServEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadServEnable.setStatus("mandatory")
_ExternalAuthProfile_RadAuthClient_AuthPort_Type = Integer32
_ExternalAuthProfile_RadAuthClient_AuthPort_Object = MibScalar
externalAuthProfile_RadAuthClient_AuthPort = _ExternalAuthProfile_RadAuthClient_AuthPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 8),
    _ExternalAuthProfile_RadAuthClient_AuthPort_Type()
)
externalAuthProfile_RadAuthClient_AuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AuthPort.setStatus("mandatory")
_ExternalAuthProfile_RadAuthClient_AuthSrcPort_Type = Integer32
_ExternalAuthProfile_RadAuthClient_AuthSrcPort_Object = MibScalar
externalAuthProfile_RadAuthClient_AuthSrcPort = _ExternalAuthProfile_RadAuthClient_AuthSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 9),
    _ExternalAuthProfile_RadAuthClient_AuthSrcPort_Type()
)
externalAuthProfile_RadAuthClient_AuthSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AuthSrcPort.setStatus("mandatory")
_ExternalAuthProfile_RadAuthClient_AuthKey_Type = DisplayString
_ExternalAuthProfile_RadAuthClient_AuthKey_Object = MibScalar
externalAuthProfile_RadAuthClient_AuthKey = _ExternalAuthProfile_RadAuthClient_AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 10),
    _ExternalAuthProfile_RadAuthClient_AuthKey_Type()
)
externalAuthProfile_RadAuthClient_AuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AuthKey.setStatus("mandatory")


class _ExternalAuthProfile_RadAuthClient_AuthPool_Type(Integer32):
    """Custom type externalAuthProfile_RadAuthClient_AuthPool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ExternalAuthProfile_RadAuthClient_AuthPool_Type.__name__ = "Integer32"
_ExternalAuthProfile_RadAuthClient_AuthPool_Object = MibScalar
externalAuthProfile_RadAuthClient_AuthPool = _ExternalAuthProfile_RadAuthClient_AuthPool_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 11),
    _ExternalAuthProfile_RadAuthClient_AuthPool_Type()
)
externalAuthProfile_RadAuthClient_AuthPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AuthPool.setStatus("mandatory")
_ExternalAuthProfile_RadAuthClient_AuthTimeout_Type = Integer32
_ExternalAuthProfile_RadAuthClient_AuthTimeout_Object = MibScalar
externalAuthProfile_RadAuthClient_AuthTimeout = _ExternalAuthProfile_RadAuthClient_AuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 12),
    _ExternalAuthProfile_RadAuthClient_AuthTimeout_Type()
)
externalAuthProfile_RadAuthClient_AuthTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AuthTimeout.setStatus("mandatory")


class _ExternalAuthProfile_RadAuthClient_AuthRspRequired_Type(Integer32):
    """Custom type externalAuthProfile_RadAuthClient_AuthRspRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ExternalAuthProfile_RadAuthClient_AuthRspRequired_Type.__name__ = "Integer32"
_ExternalAuthProfile_RadAuthClient_AuthRspRequired_Object = MibScalar
externalAuthProfile_RadAuthClient_AuthRspRequired = _ExternalAuthProfile_RadAuthClient_AuthRspRequired_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 13),
    _ExternalAuthProfile_RadAuthClient_AuthRspRequired_Type()
)
externalAuthProfile_RadAuthClient_AuthRspRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AuthRspRequired.setStatus("mandatory")


class _ExternalAuthProfile_RadAuthClient_AuthIdFailReturnBusy_Type(Integer32):
    """Custom type externalAuthProfile_RadAuthClient_AuthIdFailReturnBusy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ExternalAuthProfile_RadAuthClient_AuthIdFailReturnBusy_Type.__name__ = "Integer32"
_ExternalAuthProfile_RadAuthClient_AuthIdFailReturnBusy_Object = MibScalar
externalAuthProfile_RadAuthClient_AuthIdFailReturnBusy = _ExternalAuthProfile_RadAuthClient_AuthIdFailReturnBusy_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 14),
    _ExternalAuthProfile_RadAuthClient_AuthIdFailReturnBusy_Type()
)
externalAuthProfile_RadAuthClient_AuthIdFailReturnBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AuthIdFailReturnBusy.setStatus("mandatory")


class _ExternalAuthProfile_RadAuthClient_AuthIdTimeoutReturnBusy_Type(Integer32):
    """Custom type externalAuthProfile_RadAuthClient_AuthIdTimeoutReturnBusy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ExternalAuthProfile_RadAuthClient_AuthIdTimeoutReturnBusy_Type.__name__ = "Integer32"
_ExternalAuthProfile_RadAuthClient_AuthIdTimeoutReturnBusy_Object = MibScalar
externalAuthProfile_RadAuthClient_AuthIdTimeoutReturnBusy = _ExternalAuthProfile_RadAuthClient_AuthIdTimeoutReturnBusy_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 15),
    _ExternalAuthProfile_RadAuthClient_AuthIdTimeoutReturnBusy_Type()
)
externalAuthProfile_RadAuthClient_AuthIdTimeoutReturnBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AuthIdTimeoutReturnBusy.setStatus("mandatory")
_ExternalAuthProfile_RadAuthClient_AuthSessInterval_Type = Integer32
_ExternalAuthProfile_RadAuthClient_AuthSessInterval_Object = MibScalar
externalAuthProfile_RadAuthClient_AuthSessInterval = _ExternalAuthProfile_RadAuthClient_AuthSessInterval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 16),
    _ExternalAuthProfile_RadAuthClient_AuthSessInterval_Type()
)
externalAuthProfile_RadAuthClient_AuthSessInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AuthSessInterval.setStatus("mandatory")


class _ExternalAuthProfile_RadAuthClient_AuthTSSecure_Type(Integer32):
    """Custom type externalAuthProfile_RadAuthClient_AuthTSSecure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ExternalAuthProfile_RadAuthClient_AuthTSSecure_Type.__name__ = "Integer32"
_ExternalAuthProfile_RadAuthClient_AuthTSSecure_Object = MibScalar
externalAuthProfile_RadAuthClient_AuthTSSecure = _ExternalAuthProfile_RadAuthClient_AuthTSSecure_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 17),
    _ExternalAuthProfile_RadAuthClient_AuthTSSecure_Type()
)
externalAuthProfile_RadAuthClient_AuthTSSecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AuthTSSecure.setStatus("mandatory")


class _ExternalAuthProfile_RadAuthClient_AuthSend67_Type(Integer32):
    """Custom type externalAuthProfile_RadAuthClient_AuthSend67 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ExternalAuthProfile_RadAuthClient_AuthSend67_Type.__name__ = "Integer32"
_ExternalAuthProfile_RadAuthClient_AuthSend67_Object = MibScalar
externalAuthProfile_RadAuthClient_AuthSend67 = _ExternalAuthProfile_RadAuthClient_AuthSend67_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 18),
    _ExternalAuthProfile_RadAuthClient_AuthSend67_Type()
)
externalAuthProfile_RadAuthClient_AuthSend67.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AuthSend67.setStatus("mandatory")


class _ExternalAuthProfile_RadAuthClient_AuthFrmAdrStart_Type(Integer32):
    """Custom type externalAuthProfile_RadAuthClient_AuthFrmAdrStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ExternalAuthProfile_RadAuthClient_AuthFrmAdrStart_Type.__name__ = "Integer32"
_ExternalAuthProfile_RadAuthClient_AuthFrmAdrStart_Object = MibScalar
externalAuthProfile_RadAuthClient_AuthFrmAdrStart = _ExternalAuthProfile_RadAuthClient_AuthFrmAdrStart_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 19),
    _ExternalAuthProfile_RadAuthClient_AuthFrmAdrStart_Type()
)
externalAuthProfile_RadAuthClient_AuthFrmAdrStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AuthFrmAdrStart.setStatus("mandatory")
_ExternalAuthProfile_RadAuthClient_AuthBootHost_Type = IpAddress
_ExternalAuthProfile_RadAuthClient_AuthBootHost_Object = MibScalar
externalAuthProfile_RadAuthClient_AuthBootHost = _ExternalAuthProfile_RadAuthClient_AuthBootHost_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 20),
    _ExternalAuthProfile_RadAuthClient_AuthBootHost_Type()
)
externalAuthProfile_RadAuthClient_AuthBootHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AuthBootHost.setStatus("mandatory")
_ExternalAuthProfile_RadAuthClient_AuthBootHost2_Type = IpAddress
_ExternalAuthProfile_RadAuthClient_AuthBootHost2_Object = MibScalar
externalAuthProfile_RadAuthClient_AuthBootHost2 = _ExternalAuthProfile_RadAuthClient_AuthBootHost2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 21),
    _ExternalAuthProfile_RadAuthClient_AuthBootHost2_Type()
)
externalAuthProfile_RadAuthClient_AuthBootHost2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AuthBootHost2.setStatus("mandatory")
_ExternalAuthProfile_RadAuthClient_AuthBootPort_Type = Integer32
_ExternalAuthProfile_RadAuthClient_AuthBootPort_Object = MibScalar
externalAuthProfile_RadAuthClient_AuthBootPort = _ExternalAuthProfile_RadAuthClient_AuthBootPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 22),
    _ExternalAuthProfile_RadAuthClient_AuthBootPort_Type()
)
externalAuthProfile_RadAuthClient_AuthBootPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AuthBootPort.setStatus("mandatory")
_ExternalAuthProfile_RadAuthClient_AuthResetTime_Type = Integer32
_ExternalAuthProfile_RadAuthClient_AuthResetTime_Object = MibScalar
externalAuthProfile_RadAuthClient_AuthResetTime = _ExternalAuthProfile_RadAuthClient_AuthResetTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 23),
    _ExternalAuthProfile_RadAuthClient_AuthResetTime_Type()
)
externalAuthProfile_RadAuthClient_AuthResetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AuthResetTime.setStatus("mandatory")
_ExternalAuthProfile_RadAuthClient_AuthIdMaxRetryTime_Type = Integer32
_ExternalAuthProfile_RadAuthClient_AuthIdMaxRetryTime_Object = MibScalar
externalAuthProfile_RadAuthClient_AuthIdMaxRetryTime = _ExternalAuthProfile_RadAuthClient_AuthIdMaxRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 24),
    _ExternalAuthProfile_RadAuthClient_AuthIdMaxRetryTime_Type()
)
externalAuthProfile_RadAuthClient_AuthIdMaxRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AuthIdMaxRetryTime.setStatus("mandatory")


class _ExternalAuthProfile_RadAuthClient_AuthRadiusCompat_Type(Integer32):
    """Custom type externalAuthProfile_RadAuthClient_AuthRadiusCompat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("n-16BitVendorSpecific", 3),
          ("oldAscend", 1),
          ("vendorSpecific", 2))
    )


_ExternalAuthProfile_RadAuthClient_AuthRadiusCompat_Type.__name__ = "Integer32"
_ExternalAuthProfile_RadAuthClient_AuthRadiusCompat_Object = MibScalar
externalAuthProfile_RadAuthClient_AuthRadiusCompat = _ExternalAuthProfile_RadAuthClient_AuthRadiusCompat_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 25),
    _ExternalAuthProfile_RadAuthClient_AuthRadiusCompat_Type()
)
externalAuthProfile_RadAuthClient_AuthRadiusCompat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AuthRadiusCompat.setStatus("mandatory")


class _ExternalAuthProfile_RadAuthClient_AuthKeepUserName_Type(Integer32):
    """Custom type externalAuthProfile_RadAuthClient_AuthKeepUserName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("changeName", 1),
          ("keepName", 2),
          ("keepRealmName", 3))
    )


_ExternalAuthProfile_RadAuthClient_AuthKeepUserName_Type.__name__ = "Integer32"
_ExternalAuthProfile_RadAuthClient_AuthKeepUserName_Object = MibScalar
externalAuthProfile_RadAuthClient_AuthKeepUserName = _ExternalAuthProfile_RadAuthClient_AuthKeepUserName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 26),
    _ExternalAuthProfile_RadAuthClient_AuthKeepUserName_Type()
)
externalAuthProfile_RadAuthClient_AuthKeepUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AuthKeepUserName.setStatus("mandatory")
_ExternalAuthProfile_RadAuthClient_AuthRealmDelimiters_Type = DisplayString
_ExternalAuthProfile_RadAuthClient_AuthRealmDelimiters_Object = MibScalar
externalAuthProfile_RadAuthClient_AuthRealmDelimiters = _ExternalAuthProfile_RadAuthClient_AuthRealmDelimiters_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 27),
    _ExternalAuthProfile_RadAuthClient_AuthRealmDelimiters_Type()
)
externalAuthProfile_RadAuthClient_AuthRealmDelimiters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AuthRealmDelimiters.setStatus("mandatory")
_ExternalAuthProfile_RadAuthClient_IdAuthPrefix_Type = DisplayString
_ExternalAuthProfile_RadAuthClient_IdAuthPrefix_Object = MibScalar
externalAuthProfile_RadAuthClient_IdAuthPrefix = _ExternalAuthProfile_RadAuthClient_IdAuthPrefix_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 28),
    _ExternalAuthProfile_RadAuthClient_IdAuthPrefix_Type()
)
externalAuthProfile_RadAuthClient_IdAuthPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_IdAuthPrefix.setStatus("mandatory")


class _ExternalAuthProfile_RadAuthClient_AllowAuthConfigRqsts_Type(Integer32):
    """Custom type externalAuthProfile_RadAuthClient_AllowAuthConfigRqsts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ExternalAuthProfile_RadAuthClient_AllowAuthConfigRqsts_Type.__name__ = "Integer32"
_ExternalAuthProfile_RadAuthClient_AllowAuthConfigRqsts_Object = MibScalar
externalAuthProfile_RadAuthClient_AllowAuthConfigRqsts = _ExternalAuthProfile_RadAuthClient_AllowAuthConfigRqsts_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 29),
    _ExternalAuthProfile_RadAuthClient_AllowAuthConfigRqsts_Type()
)
externalAuthProfile_RadAuthClient_AllowAuthConfigRqsts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AllowAuthConfigRqsts.setStatus("mandatory")
_ExternalAuthProfile_RadAuthClient_AuthReqDelimCount_Type = Integer32
_ExternalAuthProfile_RadAuthClient_AuthReqDelimCount_Object = MibScalar
externalAuthProfile_RadAuthClient_AuthReqDelimCount = _ExternalAuthProfile_RadAuthClient_AuthReqDelimCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 30),
    _ExternalAuthProfile_RadAuthClient_AuthReqDelimCount_Type()
)
externalAuthProfile_RadAuthClient_AuthReqDelimCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AuthReqDelimCount.setStatus("mandatory")


class _ExternalAuthProfile_RadAuthClient_AuthReqStripSide_Type(Integer32):
    """Custom type externalAuthProfile_RadAuthClient_AuthReqStripSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("left", 2),
          ("none", 1),
          ("right", 3))
    )


_ExternalAuthProfile_RadAuthClient_AuthReqStripSide_Type.__name__ = "Integer32"
_ExternalAuthProfile_RadAuthClient_AuthReqStripSide_Object = MibScalar
externalAuthProfile_RadAuthClient_AuthReqStripSide = _ExternalAuthProfile_RadAuthClient_AuthReqStripSide_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 31),
    _ExternalAuthProfile_RadAuthClient_AuthReqStripSide_Type()
)
externalAuthProfile_RadAuthClient_AuthReqStripSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AuthReqStripSide.setStatus("mandatory")
_ExternalAuthProfile_RadAcctClient_AcctPort_Type = Integer32
_ExternalAuthProfile_RadAcctClient_AcctPort_Object = MibScalar
externalAuthProfile_RadAcctClient_AcctPort = _ExternalAuthProfile_RadAcctClient_AcctPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 35),
    _ExternalAuthProfile_RadAcctClient_AcctPort_Type()
)
externalAuthProfile_RadAcctClient_AcctPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAcctClient_AcctPort.setStatus("mandatory")
_ExternalAuthProfile_RadAcctClient_AcctSrcPort_Type = Integer32
_ExternalAuthProfile_RadAcctClient_AcctSrcPort_Object = MibScalar
externalAuthProfile_RadAcctClient_AcctSrcPort = _ExternalAuthProfile_RadAcctClient_AcctSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 36),
    _ExternalAuthProfile_RadAcctClient_AcctSrcPort_Type()
)
externalAuthProfile_RadAcctClient_AcctSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAcctClient_AcctSrcPort.setStatus("mandatory")
_ExternalAuthProfile_RadAcctClient_AcctKey_Type = DisplayString
_ExternalAuthProfile_RadAcctClient_AcctKey_Object = MibScalar
externalAuthProfile_RadAcctClient_AcctKey = _ExternalAuthProfile_RadAcctClient_AcctKey_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 37),
    _ExternalAuthProfile_RadAcctClient_AcctKey_Type()
)
externalAuthProfile_RadAcctClient_AcctKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAcctClient_AcctKey.setStatus("mandatory")
_ExternalAuthProfile_RadAcctClient_AcctTimeout_Type = Integer32
_ExternalAuthProfile_RadAcctClient_AcctTimeout_Object = MibScalar
externalAuthProfile_RadAcctClient_AcctTimeout = _ExternalAuthProfile_RadAcctClient_AcctTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 38),
    _ExternalAuthProfile_RadAcctClient_AcctTimeout_Type()
)
externalAuthProfile_RadAcctClient_AcctTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAcctClient_AcctTimeout.setStatus("mandatory")
_ExternalAuthProfile_RadAcctClient_AcctSessInterval_Type = Integer32
_ExternalAuthProfile_RadAcctClient_AcctSessInterval_Object = MibScalar
externalAuthProfile_RadAcctClient_AcctSessInterval = _ExternalAuthProfile_RadAcctClient_AcctSessInterval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 39),
    _ExternalAuthProfile_RadAcctClient_AcctSessInterval_Type()
)
externalAuthProfile_RadAcctClient_AcctSessInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAcctClient_AcctSessInterval.setStatus("mandatory")


class _ExternalAuthProfile_RadAcctClient_AcctIdBase_Type(Integer32):
    """Custom type externalAuthProfile_RadAcctClient_AcctIdBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acctBase10", 1),
          ("acctBase16", 2))
    )


_ExternalAuthProfile_RadAcctClient_AcctIdBase_Type.__name__ = "Integer32"
_ExternalAuthProfile_RadAcctClient_AcctIdBase_Object = MibScalar
externalAuthProfile_RadAcctClient_AcctIdBase = _ExternalAuthProfile_RadAcctClient_AcctIdBase_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 40),
    _ExternalAuthProfile_RadAcctClient_AcctIdBase_Type()
)
externalAuthProfile_RadAcctClient_AcctIdBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAcctClient_AcctIdBase.setStatus("mandatory")
_ExternalAuthProfile_RadAcctClient_AcctResetTime_Type = Integer32
_ExternalAuthProfile_RadAcctClient_AcctResetTime_Object = MibScalar
externalAuthProfile_RadAcctClient_AcctResetTime = _ExternalAuthProfile_RadAcctClient_AcctResetTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 41),
    _ExternalAuthProfile_RadAcctClient_AcctResetTime_Type()
)
externalAuthProfile_RadAcctClient_AcctResetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAcctClient_AcctResetTime.setStatus("mandatory")
_ExternalAuthProfile_RadAcctClient_AcctCheckpoint_Type = Integer32
_ExternalAuthProfile_RadAcctClient_AcctCheckpoint_Object = MibScalar
externalAuthProfile_RadAcctClient_AcctCheckpoint = _ExternalAuthProfile_RadAcctClient_AcctCheckpoint_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 42),
    _ExternalAuthProfile_RadAcctClient_AcctCheckpoint_Type()
)
externalAuthProfile_RadAcctClient_AcctCheckpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAcctClient_AcctCheckpoint.setStatus("mandatory")


class _ExternalAuthProfile_RadAcctClient_AcctCheckpointTimer_Type(Integer32):
    """Custom type externalAuthProfile_RadAcctClient_AcctCheckpointTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allSessions", 2),
          ("perSession", 1))
    )


_ExternalAuthProfile_RadAcctClient_AcctCheckpointTimer_Type.__name__ = "Integer32"
_ExternalAuthProfile_RadAcctClient_AcctCheckpointTimer_Object = MibScalar
externalAuthProfile_RadAcctClient_AcctCheckpointTimer = _ExternalAuthProfile_RadAcctClient_AcctCheckpointTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 43),
    _ExternalAuthProfile_RadAcctClient_AcctCheckpointTimer_Type()
)
externalAuthProfile_RadAcctClient_AcctCheckpointTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAcctClient_AcctCheckpointTimer.setStatus("mandatory")


class _ExternalAuthProfile_RadAcctClient_AcctStopOnly_Type(Integer32):
    """Custom type externalAuthProfile_RadAcctClient_AcctStopOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ExternalAuthProfile_RadAcctClient_AcctStopOnly_Type.__name__ = "Integer32"
_ExternalAuthProfile_RadAcctClient_AcctStopOnly_Object = MibScalar
externalAuthProfile_RadAcctClient_AcctStopOnly = _ExternalAuthProfile_RadAcctClient_AcctStopOnly_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 44),
    _ExternalAuthProfile_RadAcctClient_AcctStopOnly_Type()
)
externalAuthProfile_RadAcctClient_AcctStopOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAcctClient_AcctStopOnly.setStatus("mandatory")
_ExternalAuthProfile_RadAcctClient_AcctLimitRetry_Type = Integer32
_ExternalAuthProfile_RadAcctClient_AcctLimitRetry_Object = MibScalar
externalAuthProfile_RadAcctClient_AcctLimitRetry = _ExternalAuthProfile_RadAcctClient_AcctLimitRetry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 45),
    _ExternalAuthProfile_RadAcctClient_AcctLimitRetry_Type()
)
externalAuthProfile_RadAcctClient_AcctLimitRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAcctClient_AcctLimitRetry.setStatus("mandatory")


class _ExternalAuthProfile_RadAcctClient_AcctDropStopOnAuthFail_Type(Integer32):
    """Custom type externalAuthProfile_RadAcctClient_AcctDropStopOnAuthFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ExternalAuthProfile_RadAcctClient_AcctDropStopOnAuthFail_Type.__name__ = "Integer32"
_ExternalAuthProfile_RadAcctClient_AcctDropStopOnAuthFail_Object = MibScalar
externalAuthProfile_RadAcctClient_AcctDropStopOnAuthFail = _ExternalAuthProfile_RadAcctClient_AcctDropStopOnAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 46),
    _ExternalAuthProfile_RadAcctClient_AcctDropStopOnAuthFail_Type()
)
externalAuthProfile_RadAcctClient_AcctDropStopOnAuthFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAcctClient_AcctDropStopOnAuthFail.setStatus("mandatory")


class _ExternalAuthProfile_RadAcctClient_AcctRadiusCompat_Type(Integer32):
    """Custom type externalAuthProfile_RadAcctClient_AcctRadiusCompat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("n-16BitVendorSpecific", 3),
          ("oldAscend", 1),
          ("vendorSpecific", 2))
    )


_ExternalAuthProfile_RadAcctClient_AcctRadiusCompat_Type.__name__ = "Integer32"
_ExternalAuthProfile_RadAcctClient_AcctRadiusCompat_Object = MibScalar
externalAuthProfile_RadAcctClient_AcctRadiusCompat = _ExternalAuthProfile_RadAcctClient_AcctRadiusCompat_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 47),
    _ExternalAuthProfile_RadAcctClient_AcctRadiusCompat_Type()
)
externalAuthProfile_RadAcctClient_AcctRadiusCompat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAcctClient_AcctRadiusCompat.setStatus("mandatory")


class _ExternalAuthProfile_RadAcctClient_TunnelAccounting_Type(Integer32):
    """Custom type externalAuthProfile_RadAcctClient_TunnelAccounting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ExternalAuthProfile_RadAcctClient_TunnelAccounting_Type.__name__ = "Integer32"
_ExternalAuthProfile_RadAcctClient_TunnelAccounting_Object = MibScalar
externalAuthProfile_RadAcctClient_TunnelAccounting = _ExternalAuthProfile_RadAcctClient_TunnelAccounting_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 48),
    _ExternalAuthProfile_RadAcctClient_TunnelAccounting_Type()
)
externalAuthProfile_RadAcctClient_TunnelAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAcctClient_TunnelAccounting.setStatus("mandatory")
_ExternalAuthProfile_RadAuthServer_AuthPort_Type = Integer32
_ExternalAuthProfile_RadAuthServer_AuthPort_Object = MibScalar
externalAuthProfile_RadAuthServer_AuthPort = _ExternalAuthProfile_RadAuthServer_AuthPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 49),
    _ExternalAuthProfile_RadAuthServer_AuthPort_Type()
)
externalAuthProfile_RadAuthServer_AuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthServer_AuthPort.setStatus("mandatory")


class _ExternalAuthProfile_RadAuthServer_AuthSessionKey_Type(Integer32):
    """Custom type externalAuthProfile_RadAuthServer_AuthSessionKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ExternalAuthProfile_RadAuthServer_AuthSessionKey_Type.__name__ = "Integer32"
_ExternalAuthProfile_RadAuthServer_AuthSessionKey_Object = MibScalar
externalAuthProfile_RadAuthServer_AuthSessionKey = _ExternalAuthProfile_RadAuthServer_AuthSessionKey_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 50),
    _ExternalAuthProfile_RadAuthServer_AuthSessionKey_Type()
)
externalAuthProfile_RadAuthServer_AuthSessionKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthServer_AuthSessionKey.setStatus("mandatory")


class _ExternalAuthProfile_RadAuthServer_AuthAttributeType_Type(Integer32):
    """Custom type externalAuthProfile_RadAuthServer_AuthAttributeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("radServAttrAll", 3),
          ("radServAttrAny", 1),
          ("radServAttrKey", 2))
    )


_ExternalAuthProfile_RadAuthServer_AuthAttributeType_Type.__name__ = "Integer32"
_ExternalAuthProfile_RadAuthServer_AuthAttributeType_Object = MibScalar
externalAuthProfile_RadAuthServer_AuthAttributeType = _ExternalAuthProfile_RadAuthServer_AuthAttributeType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 51),
    _ExternalAuthProfile_RadAuthServer_AuthAttributeType_Type()
)
externalAuthProfile_RadAuthServer_AuthAttributeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthServer_AuthAttributeType.setStatus("mandatory")


class _ExternalAuthProfile_RadAuthServer_AuthRadiusCompat_Type(Integer32):
    """Custom type externalAuthProfile_RadAuthServer_AuthRadiusCompat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("n-16BitVendorSpecific", 3),
          ("oldAscend", 1),
          ("vendorSpecific", 2))
    )


_ExternalAuthProfile_RadAuthServer_AuthRadiusCompat_Type.__name__ = "Integer32"
_ExternalAuthProfile_RadAuthServer_AuthRadiusCompat_Object = MibScalar
externalAuthProfile_RadAuthServer_AuthRadiusCompat = _ExternalAuthProfile_RadAuthServer_AuthRadiusCompat_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 52),
    _ExternalAuthProfile_RadAuthServer_AuthRadiusCompat_Type()
)
externalAuthProfile_RadAuthServer_AuthRadiusCompat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthServer_AuthRadiusCompat.setStatus("mandatory")
_ExternalAuthProfile_TacAuthClient_AuthServer1_Type = IpAddress
_ExternalAuthProfile_TacAuthClient_AuthServer1_Object = MibScalar
externalAuthProfile_TacAuthClient_AuthServer1 = _ExternalAuthProfile_TacAuthClient_AuthServer1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 53),
    _ExternalAuthProfile_TacAuthClient_AuthServer1_Type()
)
externalAuthProfile_TacAuthClient_AuthServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_TacAuthClient_AuthServer1.setStatus("mandatory")
_ExternalAuthProfile_TacAuthClient_AuthServer2_Type = IpAddress
_ExternalAuthProfile_TacAuthClient_AuthServer2_Object = MibScalar
externalAuthProfile_TacAuthClient_AuthServer2 = _ExternalAuthProfile_TacAuthClient_AuthServer2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 54),
    _ExternalAuthProfile_TacAuthClient_AuthServer2_Type()
)
externalAuthProfile_TacAuthClient_AuthServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_TacAuthClient_AuthServer2.setStatus("mandatory")
_ExternalAuthProfile_TacAuthClient_AuthServer3_Type = IpAddress
_ExternalAuthProfile_TacAuthClient_AuthServer3_Object = MibScalar
externalAuthProfile_TacAuthClient_AuthServer3 = _ExternalAuthProfile_TacAuthClient_AuthServer3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 55),
    _ExternalAuthProfile_TacAuthClient_AuthServer3_Type()
)
externalAuthProfile_TacAuthClient_AuthServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_TacAuthClient_AuthServer3.setStatus("mandatory")
_ExternalAuthProfile_TacAuthClient_AuthPort_Type = Integer32
_ExternalAuthProfile_TacAuthClient_AuthPort_Object = MibScalar
externalAuthProfile_TacAuthClient_AuthPort = _ExternalAuthProfile_TacAuthClient_AuthPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 56),
    _ExternalAuthProfile_TacAuthClient_AuthPort_Type()
)
externalAuthProfile_TacAuthClient_AuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_TacAuthClient_AuthPort.setStatus("mandatory")
_ExternalAuthProfile_TacAuthClient_AuthSrcPort_Type = Integer32
_ExternalAuthProfile_TacAuthClient_AuthSrcPort_Object = MibScalar
externalAuthProfile_TacAuthClient_AuthSrcPort = _ExternalAuthProfile_TacAuthClient_AuthSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 57),
    _ExternalAuthProfile_TacAuthClient_AuthSrcPort_Type()
)
externalAuthProfile_TacAuthClient_AuthSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_TacAuthClient_AuthSrcPort.setStatus("mandatory")
_ExternalAuthProfile_TacAuthClient_AuthKey_Type = DisplayString
_ExternalAuthProfile_TacAuthClient_AuthKey_Object = MibScalar
externalAuthProfile_TacAuthClient_AuthKey = _ExternalAuthProfile_TacAuthClient_AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 58),
    _ExternalAuthProfile_TacAuthClient_AuthKey_Type()
)
externalAuthProfile_TacAuthClient_AuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_TacAuthClient_AuthKey.setStatus("mandatory")
_ExternalAuthProfile_TacAuthClient_AuthTimeout_Type = Integer32
_ExternalAuthProfile_TacAuthClient_AuthTimeout_Object = MibScalar
externalAuthProfile_TacAuthClient_AuthTimeout = _ExternalAuthProfile_TacAuthClient_AuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 59),
    _ExternalAuthProfile_TacAuthClient_AuthTimeout_Type()
)
externalAuthProfile_TacAuthClient_AuthTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_TacAuthClient_AuthTimeout.setStatus("mandatory")
_ExternalAuthProfile_TacplusAuthClient_AuthServer1_Type = IpAddress
_ExternalAuthProfile_TacplusAuthClient_AuthServer1_Object = MibScalar
externalAuthProfile_TacplusAuthClient_AuthServer1 = _ExternalAuthProfile_TacplusAuthClient_AuthServer1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 60),
    _ExternalAuthProfile_TacplusAuthClient_AuthServer1_Type()
)
externalAuthProfile_TacplusAuthClient_AuthServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_TacplusAuthClient_AuthServer1.setStatus("mandatory")
_ExternalAuthProfile_TacplusAuthClient_AuthServer2_Type = IpAddress
_ExternalAuthProfile_TacplusAuthClient_AuthServer2_Object = MibScalar
externalAuthProfile_TacplusAuthClient_AuthServer2 = _ExternalAuthProfile_TacplusAuthClient_AuthServer2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 61),
    _ExternalAuthProfile_TacplusAuthClient_AuthServer2_Type()
)
externalAuthProfile_TacplusAuthClient_AuthServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_TacplusAuthClient_AuthServer2.setStatus("mandatory")
_ExternalAuthProfile_TacplusAuthClient_AuthServer3_Type = IpAddress
_ExternalAuthProfile_TacplusAuthClient_AuthServer3_Object = MibScalar
externalAuthProfile_TacplusAuthClient_AuthServer3 = _ExternalAuthProfile_TacplusAuthClient_AuthServer3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 62),
    _ExternalAuthProfile_TacplusAuthClient_AuthServer3_Type()
)
externalAuthProfile_TacplusAuthClient_AuthServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_TacplusAuthClient_AuthServer3.setStatus("mandatory")
_ExternalAuthProfile_TacplusAuthClient_AuthPort_Type = Integer32
_ExternalAuthProfile_TacplusAuthClient_AuthPort_Object = MibScalar
externalAuthProfile_TacplusAuthClient_AuthPort = _ExternalAuthProfile_TacplusAuthClient_AuthPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 63),
    _ExternalAuthProfile_TacplusAuthClient_AuthPort_Type()
)
externalAuthProfile_TacplusAuthClient_AuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_TacplusAuthClient_AuthPort.setStatus("mandatory")
_ExternalAuthProfile_TacplusAuthClient_AuthSrcPort_Type = Integer32
_ExternalAuthProfile_TacplusAuthClient_AuthSrcPort_Object = MibScalar
externalAuthProfile_TacplusAuthClient_AuthSrcPort = _ExternalAuthProfile_TacplusAuthClient_AuthSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 64),
    _ExternalAuthProfile_TacplusAuthClient_AuthSrcPort_Type()
)
externalAuthProfile_TacplusAuthClient_AuthSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_TacplusAuthClient_AuthSrcPort.setStatus("mandatory")
_ExternalAuthProfile_TacplusAuthClient_AuthKey_Type = DisplayString
_ExternalAuthProfile_TacplusAuthClient_AuthKey_Object = MibScalar
externalAuthProfile_TacplusAuthClient_AuthKey = _ExternalAuthProfile_TacplusAuthClient_AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 65),
    _ExternalAuthProfile_TacplusAuthClient_AuthKey_Type()
)
externalAuthProfile_TacplusAuthClient_AuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_TacplusAuthClient_AuthKey.setStatus("mandatory")
_ExternalAuthProfile_TacplusAuthClient_AuthTimeoutTime_Type = Integer32
_ExternalAuthProfile_TacplusAuthClient_AuthTimeoutTime_Object = MibScalar
externalAuthProfile_TacplusAuthClient_AuthTimeoutTime = _ExternalAuthProfile_TacplusAuthClient_AuthTimeoutTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 66),
    _ExternalAuthProfile_TacplusAuthClient_AuthTimeoutTime_Type()
)
externalAuthProfile_TacplusAuthClient_AuthTimeoutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_TacplusAuthClient_AuthTimeoutTime.setStatus("mandatory")
_ExternalAuthProfile_TacplusAuthClient_AuthRetries_Type = Integer32
_ExternalAuthProfile_TacplusAuthClient_AuthRetries_Object = MibScalar
externalAuthProfile_TacplusAuthClient_AuthRetries = _ExternalAuthProfile_TacplusAuthClient_AuthRetries_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 67),
    _ExternalAuthProfile_TacplusAuthClient_AuthRetries_Type()
)
externalAuthProfile_TacplusAuthClient_AuthRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_TacplusAuthClient_AuthRetries.setStatus("mandatory")
_ExternalAuthProfile_TacplusAcctClient_AcctServer1_Type = IpAddress
_ExternalAuthProfile_TacplusAcctClient_AcctServer1_Object = MibScalar
externalAuthProfile_TacplusAcctClient_AcctServer1 = _ExternalAuthProfile_TacplusAcctClient_AcctServer1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 68),
    _ExternalAuthProfile_TacplusAcctClient_AcctServer1_Type()
)
externalAuthProfile_TacplusAcctClient_AcctServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_TacplusAcctClient_AcctServer1.setStatus("mandatory")
_ExternalAuthProfile_TacplusAcctClient_AcctServer2_Type = IpAddress
_ExternalAuthProfile_TacplusAcctClient_AcctServer2_Object = MibScalar
externalAuthProfile_TacplusAcctClient_AcctServer2 = _ExternalAuthProfile_TacplusAcctClient_AcctServer2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 69),
    _ExternalAuthProfile_TacplusAcctClient_AcctServer2_Type()
)
externalAuthProfile_TacplusAcctClient_AcctServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_TacplusAcctClient_AcctServer2.setStatus("mandatory")
_ExternalAuthProfile_TacplusAcctClient_AcctServer3_Type = IpAddress
_ExternalAuthProfile_TacplusAcctClient_AcctServer3_Object = MibScalar
externalAuthProfile_TacplusAcctClient_AcctServer3 = _ExternalAuthProfile_TacplusAcctClient_AcctServer3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 70),
    _ExternalAuthProfile_TacplusAcctClient_AcctServer3_Type()
)
externalAuthProfile_TacplusAcctClient_AcctServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_TacplusAcctClient_AcctServer3.setStatus("mandatory")
_ExternalAuthProfile_TacplusAcctClient_AcctPort_Type = Integer32
_ExternalAuthProfile_TacplusAcctClient_AcctPort_Object = MibScalar
externalAuthProfile_TacplusAcctClient_AcctPort = _ExternalAuthProfile_TacplusAcctClient_AcctPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 71),
    _ExternalAuthProfile_TacplusAcctClient_AcctPort_Type()
)
externalAuthProfile_TacplusAcctClient_AcctPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_TacplusAcctClient_AcctPort.setStatus("mandatory")
_ExternalAuthProfile_TacplusAcctClient_AcctSrcPort_Type = Integer32
_ExternalAuthProfile_TacplusAcctClient_AcctSrcPort_Object = MibScalar
externalAuthProfile_TacplusAcctClient_AcctSrcPort = _ExternalAuthProfile_TacplusAcctClient_AcctSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 72),
    _ExternalAuthProfile_TacplusAcctClient_AcctSrcPort_Type()
)
externalAuthProfile_TacplusAcctClient_AcctSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_TacplusAcctClient_AcctSrcPort.setStatus("mandatory")
_ExternalAuthProfile_TacplusAcctClient_AcctKey_Type = DisplayString
_ExternalAuthProfile_TacplusAcctClient_AcctKey_Object = MibScalar
externalAuthProfile_TacplusAcctClient_AcctKey = _ExternalAuthProfile_TacplusAcctClient_AcctKey_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 73),
    _ExternalAuthProfile_TacplusAcctClient_AcctKey_Type()
)
externalAuthProfile_TacplusAcctClient_AcctKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_TacplusAcctClient_AcctKey.setStatus("mandatory")
_ExternalAuthProfile_SecureidAuthClient_AuthServer1_Type = IpAddress
_ExternalAuthProfile_SecureidAuthClient_AuthServer1_Object = MibScalar
externalAuthProfile_SecureidAuthClient_AuthServer1 = _ExternalAuthProfile_SecureidAuthClient_AuthServer1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 74),
    _ExternalAuthProfile_SecureidAuthClient_AuthServer1_Type()
)
externalAuthProfile_SecureidAuthClient_AuthServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_SecureidAuthClient_AuthServer1.setStatus("mandatory")
_ExternalAuthProfile_SecureidAuthClient_AuthServer2_Type = IpAddress
_ExternalAuthProfile_SecureidAuthClient_AuthServer2_Object = MibScalar
externalAuthProfile_SecureidAuthClient_AuthServer2 = _ExternalAuthProfile_SecureidAuthClient_AuthServer2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 75),
    _ExternalAuthProfile_SecureidAuthClient_AuthServer2_Type()
)
externalAuthProfile_SecureidAuthClient_AuthServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_SecureidAuthClient_AuthServer2.setStatus("mandatory")
_ExternalAuthProfile_SecureidAuthClient_AuthServer3_Type = IpAddress
_ExternalAuthProfile_SecureidAuthClient_AuthServer3_Object = MibScalar
externalAuthProfile_SecureidAuthClient_AuthServer3 = _ExternalAuthProfile_SecureidAuthClient_AuthServer3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 76),
    _ExternalAuthProfile_SecureidAuthClient_AuthServer3_Type()
)
externalAuthProfile_SecureidAuthClient_AuthServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_SecureidAuthClient_AuthServer3.setStatus("mandatory")
_ExternalAuthProfile_SecureidAuthClient_AuthPort_Type = Integer32
_ExternalAuthProfile_SecureidAuthClient_AuthPort_Object = MibScalar
externalAuthProfile_SecureidAuthClient_AuthPort = _ExternalAuthProfile_SecureidAuthClient_AuthPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 77),
    _ExternalAuthProfile_SecureidAuthClient_AuthPort_Type()
)
externalAuthProfile_SecureidAuthClient_AuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_SecureidAuthClient_AuthPort.setStatus("mandatory")
_ExternalAuthProfile_SecureidAuthClient_AuthTimeout_Type = Integer32
_ExternalAuthProfile_SecureidAuthClient_AuthTimeout_Object = MibScalar
externalAuthProfile_SecureidAuthClient_AuthTimeout = _ExternalAuthProfile_SecureidAuthClient_AuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 78),
    _ExternalAuthProfile_SecureidAuthClient_AuthTimeout_Type()
)
externalAuthProfile_SecureidAuthClient_AuthTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_SecureidAuthClient_AuthTimeout.setStatus("mandatory")
_ExternalAuthProfile_SecureidAuthClient_AuthRetrycount_Type = Integer32
_ExternalAuthProfile_SecureidAuthClient_AuthRetrycount_Object = MibScalar
externalAuthProfile_SecureidAuthClient_AuthRetrycount = _ExternalAuthProfile_SecureidAuthClient_AuthRetrycount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 79),
    _ExternalAuthProfile_SecureidAuthClient_AuthRetrycount_Type()
)
externalAuthProfile_SecureidAuthClient_AuthRetrycount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_SecureidAuthClient_AuthRetrycount.setStatus("mandatory")


class _ExternalAuthProfile_SecureidAuthClient_AuthDes_Type(Integer32):
    """Custom type externalAuthProfile_SecureidAuthClient_AuthDes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ExternalAuthProfile_SecureidAuthClient_AuthDes_Type.__name__ = "Integer32"
_ExternalAuthProfile_SecureidAuthClient_AuthDes_Object = MibScalar
externalAuthProfile_SecureidAuthClient_AuthDes = _ExternalAuthProfile_SecureidAuthClient_AuthDes_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 80),
    _ExternalAuthProfile_SecureidAuthClient_AuthDes_Type()
)
externalAuthProfile_SecureidAuthClient_AuthDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_SecureidAuthClient_AuthDes.setStatus("mandatory")
_ExternalAuthProfile_SecureidAuthClient_AuthNodeSecret_Type = DisplayString
_ExternalAuthProfile_SecureidAuthClient_AuthNodeSecret_Object = MibScalar
externalAuthProfile_SecureidAuthClient_AuthNodeSecret = _ExternalAuthProfile_SecureidAuthClient_AuthNodeSecret_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 81),
    _ExternalAuthProfile_SecureidAuthClient_AuthNodeSecret_Type()
)
externalAuthProfile_SecureidAuthClient_AuthNodeSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_SecureidAuthClient_AuthNodeSecret.setStatus("mandatory")
_ExternalAuthProfile_PasswordProfile_Clid_Type = DisplayString
_ExternalAuthProfile_PasswordProfile_Clid_Object = MibScalar
externalAuthProfile_PasswordProfile_Clid = _ExternalAuthProfile_PasswordProfile_Clid_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 82),
    _ExternalAuthProfile_PasswordProfile_Clid_Type()
)
externalAuthProfile_PasswordProfile_Clid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_PasswordProfile_Clid.setStatus("mandatory")
_ExternalAuthProfile_PasswordProfile_Dnis_Type = DisplayString
_ExternalAuthProfile_PasswordProfile_Dnis_Object = MibScalar
externalAuthProfile_PasswordProfile_Dnis = _ExternalAuthProfile_PasswordProfile_Dnis_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 83),
    _ExternalAuthProfile_PasswordProfile_Dnis_Type()
)
externalAuthProfile_PasswordProfile_Dnis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_PasswordProfile_Dnis.setStatus("mandatory")
_ExternalAuthProfile_PasswordProfile_Banner_Type = DisplayString
_ExternalAuthProfile_PasswordProfile_Banner_Object = MibScalar
externalAuthProfile_PasswordProfile_Banner = _ExternalAuthProfile_PasswordProfile_Banner_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 84),
    _ExternalAuthProfile_PasswordProfile_Banner_Type()
)
externalAuthProfile_PasswordProfile_Banner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_PasswordProfile_Banner.setStatus("mandatory")
_ExternalAuthProfile_PasswordProfile_InitBanner_Type = DisplayString
_ExternalAuthProfile_PasswordProfile_InitBanner_Object = MibScalar
externalAuthProfile_PasswordProfile_InitBanner = _ExternalAuthProfile_PasswordProfile_InitBanner_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 85),
    _ExternalAuthProfile_PasswordProfile_InitBanner_Type()
)
externalAuthProfile_PasswordProfile_InitBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_PasswordProfile_InitBanner.setStatus("mandatory")
_ExternalAuthProfile_PasswordProfile_Pool_Type = DisplayString
_ExternalAuthProfile_PasswordProfile_Pool_Object = MibScalar
externalAuthProfile_PasswordProfile_Pool = _ExternalAuthProfile_PasswordProfile_Pool_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 86),
    _ExternalAuthProfile_PasswordProfile_Pool_Type()
)
externalAuthProfile_PasswordProfile_Pool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_PasswordProfile_Pool.setStatus("mandatory")
_ExternalAuthProfile_PasswordProfile_Frdl_Type = DisplayString
_ExternalAuthProfile_PasswordProfile_Frdl_Object = MibScalar
externalAuthProfile_PasswordProfile_Frdl = _ExternalAuthProfile_PasswordProfile_Frdl_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 87),
    _ExternalAuthProfile_PasswordProfile_Frdl_Type()
)
externalAuthProfile_PasswordProfile_Frdl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_PasswordProfile_Frdl.setStatus("mandatory")
_ExternalAuthProfile_PasswordProfile_Dialout_Type = DisplayString
_ExternalAuthProfile_PasswordProfile_Dialout_Object = MibScalar
externalAuthProfile_PasswordProfile_Dialout = _ExternalAuthProfile_PasswordProfile_Dialout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 88),
    _ExternalAuthProfile_PasswordProfile_Dialout_Type()
)
externalAuthProfile_PasswordProfile_Dialout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_PasswordProfile_Dialout.setStatus("mandatory")
_ExternalAuthProfile_PasswordProfile_DialoutRoutes_Type = DisplayString
_ExternalAuthProfile_PasswordProfile_DialoutRoutes_Object = MibScalar
externalAuthProfile_PasswordProfile_DialoutRoutes = _ExternalAuthProfile_PasswordProfile_DialoutRoutes_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 89),
    _ExternalAuthProfile_PasswordProfile_DialoutRoutes_Type()
)
externalAuthProfile_PasswordProfile_DialoutRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_PasswordProfile_DialoutRoutes.setStatus("mandatory")
_ExternalAuthProfile_PasswordProfile_DialoutIpxRoutes_Type = DisplayString
_ExternalAuthProfile_PasswordProfile_DialoutIpxRoutes_Object = MibScalar
externalAuthProfile_PasswordProfile_DialoutIpxRoutes = _ExternalAuthProfile_PasswordProfile_DialoutIpxRoutes_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 90),
    _ExternalAuthProfile_PasswordProfile_DialoutIpxRoutes_Type()
)
externalAuthProfile_PasswordProfile_DialoutIpxRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_PasswordProfile_DialoutIpxRoutes.setStatus("mandatory")
_ExternalAuthProfile_PasswordProfile_DialoutAtalkRoutes_Type = DisplayString
_ExternalAuthProfile_PasswordProfile_DialoutAtalkRoutes_Object = MibScalar
externalAuthProfile_PasswordProfile_DialoutAtalkRoutes = _ExternalAuthProfile_PasswordProfile_DialoutAtalkRoutes_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 91),
    _ExternalAuthProfile_PasswordProfile_DialoutAtalkRoutes_Type()
)
externalAuthProfile_PasswordProfile_DialoutAtalkRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_PasswordProfile_DialoutAtalkRoutes.setStatus("mandatory")
_ExternalAuthProfile_PasswordProfile_SourceAuth_Type = DisplayString
_ExternalAuthProfile_PasswordProfile_SourceAuth_Object = MibScalar
externalAuthProfile_PasswordProfile_SourceAuth = _ExternalAuthProfile_PasswordProfile_SourceAuth_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 92),
    _ExternalAuthProfile_PasswordProfile_SourceAuth_Type()
)
externalAuthProfile_PasswordProfile_SourceAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_PasswordProfile_SourceAuth.setStatus("mandatory")


class _ExternalAuthProfile_LocalProfilesFirst_Type(Integer32):
    """Custom type externalAuthProfile_LocalProfilesFirst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lpfNo", 1),
          ("lpfRno", 3),
          ("lpfYes", 2))
    )


_ExternalAuthProfile_LocalProfilesFirst_Type.__name__ = "Integer32"
_ExternalAuthProfile_LocalProfilesFirst_Object = MibScalar
externalAuthProfile_LocalProfilesFirst = _ExternalAuthProfile_LocalProfilesFirst_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 93),
    _ExternalAuthProfile_LocalProfilesFirst_Type()
)
externalAuthProfile_LocalProfilesFirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_LocalProfilesFirst.setStatus("mandatory")


class _ExternalAuthProfile_Noattr6UseTermsrv_Type(Integer32):
    """Custom type externalAuthProfile_Noattr6UseTermsrv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ExternalAuthProfile_Noattr6UseTermsrv_Type.__name__ = "Integer32"
_ExternalAuthProfile_Noattr6UseTermsrv_Object = MibScalar
externalAuthProfile_Noattr6UseTermsrv = _ExternalAuthProfile_Noattr6UseTermsrv_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 94),
    _ExternalAuthProfile_Noattr6UseTermsrv_Type()
)
externalAuthProfile_Noattr6UseTermsrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_Noattr6UseTermsrv.setStatus("mandatory")
_ExternalAuthProfile_Clid_Type = DisplayString
_ExternalAuthProfile_Clid_Object = MibScalar
externalAuthProfile_Clid = _ExternalAuthProfile_Clid_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 95),
    _ExternalAuthProfile_Clid_Type()
)
externalAuthProfile_Clid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_Clid.setStatus("mandatory")
_ExternalAuthProfile_Dnis_Type = DisplayString
_ExternalAuthProfile_Dnis_Object = MibScalar
externalAuthProfile_Dnis = _ExternalAuthProfile_Dnis_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 96),
    _ExternalAuthProfile_Dnis_Type()
)
externalAuthProfile_Dnis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_Dnis.setStatus("mandatory")


class _ExternalAuthProfile_Action_o_Type(Integer32):
    """Custom type externalAuthProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_ExternalAuthProfile_Action_o_Type.__name__ = "Integer32"
_ExternalAuthProfile_Action_o_Object = MibScalar
externalAuthProfile_Action_o = _ExternalAuthProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 97),
    _ExternalAuthProfile_Action_o_Type()
)
externalAuthProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_Action_o.setStatus("mandatory")


class _ExternalAuthProfile_RadAuthClient_AuthNetworkRouteServer_Type(Integer32):
    """Custom type externalAuthProfile_RadAuthClient_AuthNetworkRouteServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ExternalAuthProfile_RadAuthClient_AuthNetworkRouteServer_Type.__name__ = "Integer32"
_ExternalAuthProfile_RadAuthClient_AuthNetworkRouteServer_Object = MibScalar
externalAuthProfile_RadAuthClient_AuthNetworkRouteServer = _ExternalAuthProfile_RadAuthClient_AuthNetworkRouteServer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 98),
    _ExternalAuthProfile_RadAuthClient_AuthNetworkRouteServer_Type()
)
externalAuthProfile_RadAuthClient_AuthNetworkRouteServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AuthNetworkRouteServer.setStatus("mandatory")
_ExternalAuthProfile_RadAuthClient_IdAuthPrefixX25_Type = DisplayString
_ExternalAuthProfile_RadAuthClient_IdAuthPrefixX25_Object = MibScalar
externalAuthProfile_RadAuthClient_IdAuthPrefixX25 = _ExternalAuthProfile_RadAuthClient_IdAuthPrefixX25_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 99),
    _ExternalAuthProfile_RadAuthClient_IdAuthPrefixX25_Type()
)
externalAuthProfile_RadAuthClient_IdAuthPrefixX25.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_IdAuthPrefixX25.setStatus("mandatory")


class _ExternalAuthProfile_CliUserAuth_Type(Integer32):
    """Custom type externalAuthProfile_CliUserAuth based on Integer32"""
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
        *(("externalOnly", 3),
          ("externalThenLocal", 4),
          ("externalThenLocalIfTimeout", 5),
          ("localOnly", 1),
          ("localThenExternal", 2))
    )


_ExternalAuthProfile_CliUserAuth_Type.__name__ = "Integer32"
_ExternalAuthProfile_CliUserAuth_Object = MibScalar
externalAuthProfile_CliUserAuth = _ExternalAuthProfile_CliUserAuth_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 100),
    _ExternalAuthProfile_CliUserAuth_Type()
)
externalAuthProfile_CliUserAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_CliUserAuth.setStatus("mandatory")


class _ExternalAuthProfile_RadAuthClient_AllowUnencryptedTunnelPassword_Type(Integer32):
    """Custom type externalAuthProfile_RadAuthClient_AllowUnencryptedTunnelPassword based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ExternalAuthProfile_RadAuthClient_AllowUnencryptedTunnelPassword_Type.__name__ = "Integer32"
_ExternalAuthProfile_RadAuthClient_AllowUnencryptedTunnelPassword_Object = MibScalar
externalAuthProfile_RadAuthClient_AllowUnencryptedTunnelPassword = _ExternalAuthProfile_RadAuthClient_AllowUnencryptedTunnelPassword_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 101),
    _ExternalAuthProfile_RadAuthClient_AllowUnencryptedTunnelPassword_Type()
)
externalAuthProfile_RadAuthClient_AllowUnencryptedTunnelPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AllowUnencryptedTunnelPassword.setStatus("mandatory")
_ExternalAuthProfile_RadAuthClient_AuthCliUserDnis_Type = DisplayString
_ExternalAuthProfile_RadAuthClient_AuthCliUserDnis_Object = MibScalar
externalAuthProfile_RadAuthClient_AuthCliUserDnis = _ExternalAuthProfile_RadAuthClient_AuthCliUserDnis_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 102),
    _ExternalAuthProfile_RadAuthClient_AuthCliUserDnis_Type()
)
externalAuthProfile_RadAuthClient_AuthCliUserDnis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AuthCliUserDnis.setStatus("mandatory")


class _ExternalAuthProfile_RadAuthClient_AllowNasPortTypeInCliUserAuth_Type(Integer32):
    """Custom type externalAuthProfile_RadAuthClient_AllowNasPortTypeInCliUserAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ExternalAuthProfile_RadAuthClient_AllowNasPortTypeInCliUserAuth_Type.__name__ = "Integer32"
_ExternalAuthProfile_RadAuthClient_AllowNasPortTypeInCliUserAuth_Object = MibScalar
externalAuthProfile_RadAuthClient_AllowNasPortTypeInCliUserAuth = _ExternalAuthProfile_RadAuthClient_AllowNasPortTypeInCliUserAuth_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 103),
    _ExternalAuthProfile_RadAuthClient_AllowNasPortTypeInCliUserAuth_Type()
)
externalAuthProfile_RadAuthClient_AllowNasPortTypeInCliUserAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AllowNasPortTypeInCliUserAuth.setStatus("mandatory")
_ExternalAuthProfile_RadAuthClient_AuthHost1_Type = DisplayString
_ExternalAuthProfile_RadAuthClient_AuthHost1_Object = MibScalar
externalAuthProfile_RadAuthClient_AuthHost1 = _ExternalAuthProfile_RadAuthClient_AuthHost1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 104),
    _ExternalAuthProfile_RadAuthClient_AuthHost1_Type()
)
externalAuthProfile_RadAuthClient_AuthHost1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AuthHost1.setStatus("mandatory")
_ExternalAuthProfile_RadAuthClient_AuthHost2_Type = DisplayString
_ExternalAuthProfile_RadAuthClient_AuthHost2_Object = MibScalar
externalAuthProfile_RadAuthClient_AuthHost2 = _ExternalAuthProfile_RadAuthClient_AuthHost2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 105),
    _ExternalAuthProfile_RadAuthClient_AuthHost2_Type()
)
externalAuthProfile_RadAuthClient_AuthHost2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AuthHost2.setStatus("mandatory")
_ExternalAuthProfile_RadAuthClient_AuthHost3_Type = DisplayString
_ExternalAuthProfile_RadAuthClient_AuthHost3_Object = MibScalar
externalAuthProfile_RadAuthClient_AuthHost3 = _ExternalAuthProfile_RadAuthClient_AuthHost3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 106),
    _ExternalAuthProfile_RadAuthClient_AuthHost3_Type()
)
externalAuthProfile_RadAuthClient_AuthHost3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthClient_AuthHost3.setStatus("mandatory")
_ExternalAuthProfile_RadAcctClient_AcctHost1_Type = DisplayString
_ExternalAuthProfile_RadAcctClient_AcctHost1_Object = MibScalar
externalAuthProfile_RadAcctClient_AcctHost1 = _ExternalAuthProfile_RadAcctClient_AcctHost1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 107),
    _ExternalAuthProfile_RadAcctClient_AcctHost1_Type()
)
externalAuthProfile_RadAcctClient_AcctHost1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAcctClient_AcctHost1.setStatus("mandatory")
_ExternalAuthProfile_RadAcctClient_AcctHost2_Type = DisplayString
_ExternalAuthProfile_RadAcctClient_AcctHost2_Object = MibScalar
externalAuthProfile_RadAcctClient_AcctHost2 = _ExternalAuthProfile_RadAcctClient_AcctHost2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 108),
    _ExternalAuthProfile_RadAcctClient_AcctHost2_Type()
)
externalAuthProfile_RadAcctClient_AcctHost2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAcctClient_AcctHost2.setStatus("mandatory")
_ExternalAuthProfile_RadAcctClient_AcctHost3_Type = DisplayString
_ExternalAuthProfile_RadAcctClient_AcctHost3_Object = MibScalar
externalAuthProfile_RadAcctClient_AcctHost3 = _ExternalAuthProfile_RadAcctClient_AcctHost3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 109),
    _ExternalAuthProfile_RadAcctClient_AcctHost3_Type()
)
externalAuthProfile_RadAcctClient_AcctHost3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAcctClient_AcctHost3.setStatus("mandatory")


class _ExternalAuthProfile_RadAcctClient_VoipAccounting_Type(Integer32):
    """Custom type externalAuthProfile_RadAcctClient_VoipAccounting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ExternalAuthProfile_RadAcctClient_VoipAccounting_Type.__name__ = "Integer32"
_ExternalAuthProfile_RadAcctClient_VoipAccounting_Object = MibScalar
externalAuthProfile_RadAcctClient_VoipAccounting = _ExternalAuthProfile_RadAcctClient_VoipAccounting_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 110),
    _ExternalAuthProfile_RadAcctClient_VoipAccounting_Type()
)
externalAuthProfile_RadAcctClient_VoipAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAcctClient_VoipAccounting.setStatus("mandatory")


class _ExternalAuthProfile_RadAcctClient_AcctOnSwitchover_Type(Integer32):
    """Custom type externalAuthProfile_RadAcctClient_AcctOnSwitchover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ExternalAuthProfile_RadAcctClient_AcctOnSwitchover_Type.__name__ = "Integer32"
_ExternalAuthProfile_RadAcctClient_AcctOnSwitchover_Object = MibScalar
externalAuthProfile_RadAcctClient_AcctOnSwitchover = _ExternalAuthProfile_RadAcctClient_AcctOnSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 1, 1, 111),
    _ExternalAuthProfile_RadAcctClient_AcctOnSwitchover_Type()
)
externalAuthProfile_RadAcctClient_AcctOnSwitchover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAcctClient_AcctOnSwitchover.setStatus("mandatory")
_MibexternalAuthProfile_RadAuthServer_AuthKeyTable_Object = MibTable
mibexternalAuthProfile_RadAuthServer_AuthKeyTable = _MibexternalAuthProfile_RadAuthServer_AuthKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 2)
)
if mibBuilder.loadTexts:
    mibexternalAuthProfile_RadAuthServer_AuthKeyTable.setStatus("mandatory")
_MibexternalAuthProfile_RadAuthServer_AuthKeyEntry_Object = MibTableRow
mibexternalAuthProfile_RadAuthServer_AuthKeyEntry = _MibexternalAuthProfile_RadAuthServer_AuthKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 2, 1)
)
mibexternalAuthProfile_RadAuthServer_AuthKeyEntry.setIndexNames(
    (0, "ASCEND-MIBXAUTH-MIB", "externalAuthProfile-RadAuthServer-AuthKey-Index-o"),
    (0, "ASCEND-MIBXAUTH-MIB", "externalAuthProfile-RadAuthServer-AuthKey-Index1-o"),
)
if mibBuilder.loadTexts:
    mibexternalAuthProfile_RadAuthServer_AuthKeyEntry.setStatus("mandatory")
_ExternalAuthProfile_RadAuthServer_AuthKey_Index_o_Type = Integer32
_ExternalAuthProfile_RadAuthServer_AuthKey_Index_o_Object = MibScalar
externalAuthProfile_RadAuthServer_AuthKey_Index_o = _ExternalAuthProfile_RadAuthServer_AuthKey_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 2, 1, 1),
    _ExternalAuthProfile_RadAuthServer_AuthKey_Index_o_Type()
)
externalAuthProfile_RadAuthServer_AuthKey_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthServer_AuthKey_Index_o.setStatus("mandatory")
_ExternalAuthProfile_RadAuthServer_AuthKey_Index1_o_Type = Integer32
_ExternalAuthProfile_RadAuthServer_AuthKey_Index1_o_Object = MibScalar
externalAuthProfile_RadAuthServer_AuthKey_Index1_o = _ExternalAuthProfile_RadAuthServer_AuthKey_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 2, 1, 2),
    _ExternalAuthProfile_RadAuthServer_AuthKey_Index1_o_Type()
)
externalAuthProfile_RadAuthServer_AuthKey_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthServer_AuthKey_Index1_o.setStatus("mandatory")
_ExternalAuthProfile_RadAuthServer_AuthKey_Type = DisplayString
_ExternalAuthProfile_RadAuthServer_AuthKey_Object = MibScalar
externalAuthProfile_RadAuthServer_AuthKey = _ExternalAuthProfile_RadAuthServer_AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 2, 1, 3),
    _ExternalAuthProfile_RadAuthServer_AuthKey_Type()
)
externalAuthProfile_RadAuthServer_AuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthServer_AuthKey.setStatus("mandatory")
_MibexternalAuthProfile_RadAuthServer_AuthNetmaskTable_Object = MibTable
mibexternalAuthProfile_RadAuthServer_AuthNetmaskTable = _MibexternalAuthProfile_RadAuthServer_AuthNetmaskTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 3)
)
if mibBuilder.loadTexts:
    mibexternalAuthProfile_RadAuthServer_AuthNetmaskTable.setStatus("mandatory")
_MibexternalAuthProfile_RadAuthServer_AuthNetmaskEntry_Object = MibTableRow
mibexternalAuthProfile_RadAuthServer_AuthNetmaskEntry = _MibexternalAuthProfile_RadAuthServer_AuthNetmaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 3, 1)
)
mibexternalAuthProfile_RadAuthServer_AuthNetmaskEntry.setIndexNames(
    (0, "ASCEND-MIBXAUTH-MIB", "externalAuthProfile-RadAuthServer-AuthNetmask-Index-o"),
    (0, "ASCEND-MIBXAUTH-MIB", "externalAuthProfile-RadAuthServer-AuthNetmask-Index1-o"),
)
if mibBuilder.loadTexts:
    mibexternalAuthProfile_RadAuthServer_AuthNetmaskEntry.setStatus("mandatory")
_ExternalAuthProfile_RadAuthServer_AuthNetmask_Index_o_Type = Integer32
_ExternalAuthProfile_RadAuthServer_AuthNetmask_Index_o_Object = MibScalar
externalAuthProfile_RadAuthServer_AuthNetmask_Index_o = _ExternalAuthProfile_RadAuthServer_AuthNetmask_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 3, 1, 1),
    _ExternalAuthProfile_RadAuthServer_AuthNetmask_Index_o_Type()
)
externalAuthProfile_RadAuthServer_AuthNetmask_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthServer_AuthNetmask_Index_o.setStatus("mandatory")
_ExternalAuthProfile_RadAuthServer_AuthNetmask_Index1_o_Type = Integer32
_ExternalAuthProfile_RadAuthServer_AuthNetmask_Index1_o_Object = MibScalar
externalAuthProfile_RadAuthServer_AuthNetmask_Index1_o = _ExternalAuthProfile_RadAuthServer_AuthNetmask_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 3, 1, 2),
    _ExternalAuthProfile_RadAuthServer_AuthNetmask_Index1_o_Type()
)
externalAuthProfile_RadAuthServer_AuthNetmask_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthServer_AuthNetmask_Index1_o.setStatus("mandatory")
_ExternalAuthProfile_RadAuthServer_AuthNetmask_Type = IpAddress
_ExternalAuthProfile_RadAuthServer_AuthNetmask_Object = MibScalar
externalAuthProfile_RadAuthServer_AuthNetmask = _ExternalAuthProfile_RadAuthServer_AuthNetmask_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 3, 1, 3),
    _ExternalAuthProfile_RadAuthServer_AuthNetmask_Type()
)
externalAuthProfile_RadAuthServer_AuthNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthServer_AuthNetmask.setStatus("mandatory")
_MibexternalAuthProfile_RadAuthServer_AuthClientTable_Object = MibTable
mibexternalAuthProfile_RadAuthServer_AuthClientTable = _MibexternalAuthProfile_RadAuthServer_AuthClientTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 4)
)
if mibBuilder.loadTexts:
    mibexternalAuthProfile_RadAuthServer_AuthClientTable.setStatus("mandatory")
_MibexternalAuthProfile_RadAuthServer_AuthClientEntry_Object = MibTableRow
mibexternalAuthProfile_RadAuthServer_AuthClientEntry = _MibexternalAuthProfile_RadAuthServer_AuthClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 4, 1)
)
mibexternalAuthProfile_RadAuthServer_AuthClientEntry.setIndexNames(
    (0, "ASCEND-MIBXAUTH-MIB", "externalAuthProfile-RadAuthServer-AuthClient-Index-o"),
    (0, "ASCEND-MIBXAUTH-MIB", "externalAuthProfile-RadAuthServer-AuthClient-Index1-o"),
)
if mibBuilder.loadTexts:
    mibexternalAuthProfile_RadAuthServer_AuthClientEntry.setStatus("mandatory")
_ExternalAuthProfile_RadAuthServer_AuthClient_Index_o_Type = Integer32
_ExternalAuthProfile_RadAuthServer_AuthClient_Index_o_Object = MibScalar
externalAuthProfile_RadAuthServer_AuthClient_Index_o = _ExternalAuthProfile_RadAuthServer_AuthClient_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 4, 1, 1),
    _ExternalAuthProfile_RadAuthServer_AuthClient_Index_o_Type()
)
externalAuthProfile_RadAuthServer_AuthClient_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthServer_AuthClient_Index_o.setStatus("mandatory")
_ExternalAuthProfile_RadAuthServer_AuthClient_Index1_o_Type = Integer32
_ExternalAuthProfile_RadAuthServer_AuthClient_Index1_o_Object = MibScalar
externalAuthProfile_RadAuthServer_AuthClient_Index1_o = _ExternalAuthProfile_RadAuthServer_AuthClient_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 4, 1, 2),
    _ExternalAuthProfile_RadAuthServer_AuthClient_Index1_o_Type()
)
externalAuthProfile_RadAuthServer_AuthClient_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthServer_AuthClient_Index1_o.setStatus("mandatory")
_ExternalAuthProfile_RadAuthServer_AuthClient_Type = IpAddress
_ExternalAuthProfile_RadAuthServer_AuthClient_Object = MibScalar
externalAuthProfile_RadAuthServer_AuthClient = _ExternalAuthProfile_RadAuthServer_AuthClient_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 142, 4, 1, 3),
    _ExternalAuthProfile_RadAuthServer_AuthClient_Type()
)
externalAuthProfile_RadAuthServer_AuthClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalAuthProfile_RadAuthServer_AuthClient.setStatus("mandatory")
_MibradAcctCallLogProfile_ObjectIdentity = ObjectIdentity
mibradAcctCallLogProfile = _MibradAcctCallLogProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 143)
)
_MibradAcctCallLogProfileTable_Object = MibTable
mibradAcctCallLogProfileTable = _MibradAcctCallLogProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 143, 1)
)
if mibBuilder.loadTexts:
    mibradAcctCallLogProfileTable.setStatus("mandatory")
_MibradAcctCallLogProfileEntry_Object = MibTableRow
mibradAcctCallLogProfileEntry = _MibradAcctCallLogProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 143, 1, 1)
)
mibradAcctCallLogProfileEntry.setIndexNames(
    (0, "ASCEND-MIBXAUTH-MIB", "radAcctCallLogProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibradAcctCallLogProfileEntry.setStatus("mandatory")
_RadAcctCallLogProfile_Index_o_Type = Integer32
_RadAcctCallLogProfile_Index_o_Object = MibScalar
radAcctCallLogProfile_Index_o = _RadAcctCallLogProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 143, 1, 1, 1),
    _RadAcctCallLogProfile_Index_o_Type()
)
radAcctCallLogProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radAcctCallLogProfile_Index_o.setStatus("mandatory")


class _RadAcctCallLogProfile_CallLogEnable_Type(Integer32):
    """Custom type radAcctCallLogProfile_CallLogEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RadAcctCallLogProfile_CallLogEnable_Type.__name__ = "Integer32"
_RadAcctCallLogProfile_CallLogEnable_Object = MibScalar
radAcctCallLogProfile_CallLogEnable = _RadAcctCallLogProfile_CallLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 143, 1, 1, 2),
    _RadAcctCallLogProfile_CallLogEnable_Type()
)
radAcctCallLogProfile_CallLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAcctCallLogProfile_CallLogEnable.setStatus("mandatory")
_RadAcctCallLogProfile_CallLogHost1_Type = IpAddress
_RadAcctCallLogProfile_CallLogHost1_Object = MibScalar
radAcctCallLogProfile_CallLogHost1 = _RadAcctCallLogProfile_CallLogHost1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 143, 1, 1, 3),
    _RadAcctCallLogProfile_CallLogHost1_Type()
)
radAcctCallLogProfile_CallLogHost1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAcctCallLogProfile_CallLogHost1.setStatus("mandatory")
_RadAcctCallLogProfile_CallLogHost2_Type = IpAddress
_RadAcctCallLogProfile_CallLogHost2_Object = MibScalar
radAcctCallLogProfile_CallLogHost2 = _RadAcctCallLogProfile_CallLogHost2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 143, 1, 1, 4),
    _RadAcctCallLogProfile_CallLogHost2_Type()
)
radAcctCallLogProfile_CallLogHost2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAcctCallLogProfile_CallLogHost2.setStatus("mandatory")
_RadAcctCallLogProfile_CallLogHost3_Type = IpAddress
_RadAcctCallLogProfile_CallLogHost3_Object = MibScalar
radAcctCallLogProfile_CallLogHost3 = _RadAcctCallLogProfile_CallLogHost3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 143, 1, 1, 5),
    _RadAcctCallLogProfile_CallLogHost3_Type()
)
radAcctCallLogProfile_CallLogHost3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAcctCallLogProfile_CallLogHost3.setStatus("mandatory")
_RadAcctCallLogProfile_CallLogPort_Type = Integer32
_RadAcctCallLogProfile_CallLogPort_Object = MibScalar
radAcctCallLogProfile_CallLogPort = _RadAcctCallLogProfile_CallLogPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 143, 1, 1, 6),
    _RadAcctCallLogProfile_CallLogPort_Type()
)
radAcctCallLogProfile_CallLogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAcctCallLogProfile_CallLogPort.setStatus("mandatory")
_RadAcctCallLogProfile_CallLogKey_Type = DisplayString
_RadAcctCallLogProfile_CallLogKey_Object = MibScalar
radAcctCallLogProfile_CallLogKey = _RadAcctCallLogProfile_CallLogKey_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 143, 1, 1, 7),
    _RadAcctCallLogProfile_CallLogKey_Type()
)
radAcctCallLogProfile_CallLogKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAcctCallLogProfile_CallLogKey.setStatus("mandatory")
_RadAcctCallLogProfile_CallLogTimeout_Type = Integer32
_RadAcctCallLogProfile_CallLogTimeout_Object = MibScalar
radAcctCallLogProfile_CallLogTimeout = _RadAcctCallLogProfile_CallLogTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 143, 1, 1, 8),
    _RadAcctCallLogProfile_CallLogTimeout_Type()
)
radAcctCallLogProfile_CallLogTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAcctCallLogProfile_CallLogTimeout.setStatus("mandatory")


class _RadAcctCallLogProfile_CallLogIdBase_Type(Integer32):
    """Custom type radAcctCallLogProfile_CallLogIdBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acctBase10", 1),
          ("acctBase16", 2))
    )


_RadAcctCallLogProfile_CallLogIdBase_Type.__name__ = "Integer32"
_RadAcctCallLogProfile_CallLogIdBase_Object = MibScalar
radAcctCallLogProfile_CallLogIdBase = _RadAcctCallLogProfile_CallLogIdBase_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 143, 1, 1, 9),
    _RadAcctCallLogProfile_CallLogIdBase_Type()
)
radAcctCallLogProfile_CallLogIdBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAcctCallLogProfile_CallLogIdBase.setStatus("mandatory")
_RadAcctCallLogProfile_CallLogResetTime_Type = Integer32
_RadAcctCallLogProfile_CallLogResetTime_Object = MibScalar
radAcctCallLogProfile_CallLogResetTime = _RadAcctCallLogProfile_CallLogResetTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 143, 1, 1, 10),
    _RadAcctCallLogProfile_CallLogResetTime_Type()
)
radAcctCallLogProfile_CallLogResetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAcctCallLogProfile_CallLogResetTime.setStatus("mandatory")


class _RadAcctCallLogProfile_CallLogStopOnly_Type(Integer32):
    """Custom type radAcctCallLogProfile_CallLogStopOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RadAcctCallLogProfile_CallLogStopOnly_Type.__name__ = "Integer32"
_RadAcctCallLogProfile_CallLogStopOnly_Object = MibScalar
radAcctCallLogProfile_CallLogStopOnly = _RadAcctCallLogProfile_CallLogStopOnly_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 143, 1, 1, 11),
    _RadAcctCallLogProfile_CallLogStopOnly_Type()
)
radAcctCallLogProfile_CallLogStopOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAcctCallLogProfile_CallLogStopOnly.setStatus("mandatory")
_RadAcctCallLogProfile_CallLogLimitRetry_Type = Integer32
_RadAcctCallLogProfile_CallLogLimitRetry_Object = MibScalar
radAcctCallLogProfile_CallLogLimitRetry = _RadAcctCallLogProfile_CallLogLimitRetry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 143, 1, 1, 12),
    _RadAcctCallLogProfile_CallLogLimitRetry_Type()
)
radAcctCallLogProfile_CallLogLimitRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAcctCallLogProfile_CallLogLimitRetry.setStatus("mandatory")


class _RadAcctCallLogProfile_CallLogRadiusCompat_Type(Integer32):
    """Custom type radAcctCallLogProfile_CallLogRadiusCompat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("n-16BitVendorSpecific", 2),
          ("vendorSpecific", 1))
    )


_RadAcctCallLogProfile_CallLogRadiusCompat_Type.__name__ = "Integer32"
_RadAcctCallLogProfile_CallLogRadiusCompat_Object = MibScalar
radAcctCallLogProfile_CallLogRadiusCompat = _RadAcctCallLogProfile_CallLogRadiusCompat_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 143, 1, 1, 13),
    _RadAcctCallLogProfile_CallLogRadiusCompat_Type()
)
radAcctCallLogProfile_CallLogRadiusCompat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAcctCallLogProfile_CallLogRadiusCompat.setStatus("mandatory")


class _RadAcctCallLogProfile_CallLogServerIndex_Type(Integer32):
    """Custom type radAcctCallLogProfile_CallLogServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("host1", 1),
          ("host2", 2),
          ("host3", 3))
    )


_RadAcctCallLogProfile_CallLogServerIndex_Type.__name__ = "Integer32"
_RadAcctCallLogProfile_CallLogServerIndex_Object = MibScalar
radAcctCallLogProfile_CallLogServerIndex = _RadAcctCallLogProfile_CallLogServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 143, 1, 1, 14),
    _RadAcctCallLogProfile_CallLogServerIndex_Type()
)
radAcctCallLogProfile_CallLogServerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAcctCallLogProfile_CallLogServerIndex.setStatus("mandatory")


class _RadAcctCallLogProfile_CallLogMultiPacket_Type(Integer32):
    """Custom type radAcctCallLogProfile_CallLogMultiPacket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RadAcctCallLogProfile_CallLogMultiPacket_Type.__name__ = "Integer32"
_RadAcctCallLogProfile_CallLogMultiPacket_Object = MibScalar
radAcctCallLogProfile_CallLogMultiPacket = _RadAcctCallLogProfile_CallLogMultiPacket_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 143, 1, 1, 15),
    _RadAcctCallLogProfile_CallLogMultiPacket_Type()
)
radAcctCallLogProfile_CallLogMultiPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAcctCallLogProfile_CallLogMultiPacket.setStatus("mandatory")
_RadAcctCallLogProfile_CallLogStreamPeriod_Type = Integer32
_RadAcctCallLogProfile_CallLogStreamPeriod_Object = MibScalar
radAcctCallLogProfile_CallLogStreamPeriod = _RadAcctCallLogProfile_CallLogStreamPeriod_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 143, 1, 1, 16),
    _RadAcctCallLogProfile_CallLogStreamPeriod_Type()
)
radAcctCallLogProfile_CallLogStreamPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAcctCallLogProfile_CallLogStreamPeriod.setStatus("mandatory")


class _RadAcctCallLogProfile_CallLogConnectionPacketsEnable_Type(Integer32):
    """Custom type radAcctCallLogProfile_CallLogConnectionPacketsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RadAcctCallLogProfile_CallLogConnectionPacketsEnable_Type.__name__ = "Integer32"
_RadAcctCallLogProfile_CallLogConnectionPacketsEnable_Object = MibScalar
radAcctCallLogProfile_CallLogConnectionPacketsEnable = _RadAcctCallLogProfile_CallLogConnectionPacketsEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 143, 1, 1, 17),
    _RadAcctCallLogProfile_CallLogConnectionPacketsEnable_Type()
)
radAcctCallLogProfile_CallLogConnectionPacketsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAcctCallLogProfile_CallLogConnectionPacketsEnable.setStatus("mandatory")


class _RadAcctCallLogProfile_CallLogCsmModemDiag_Type(Integer32):
    """Custom type radAcctCallLogProfile_CallLogCsmModemDiag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RadAcctCallLogProfile_CallLogCsmModemDiag_Type.__name__ = "Integer32"
_RadAcctCallLogProfile_CallLogCsmModemDiag_Object = MibScalar
radAcctCallLogProfile_CallLogCsmModemDiag = _RadAcctCallLogProfile_CallLogCsmModemDiag_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 143, 1, 1, 18),
    _RadAcctCallLogProfile_CallLogCsmModemDiag_Type()
)
radAcctCallLogProfile_CallLogCsmModemDiag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAcctCallLogProfile_CallLogCsmModemDiag.setStatus("mandatory")


class _RadAcctCallLogProfile_Action_o_Type(Integer32):
    """Custom type radAcctCallLogProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_RadAcctCallLogProfile_Action_o_Type.__name__ = "Integer32"
_RadAcctCallLogProfile_Action_o_Object = MibScalar
radAcctCallLogProfile_Action_o = _RadAcctCallLogProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 143, 1, 1, 19),
    _RadAcctCallLogProfile_Action_o_Type()
)
radAcctCallLogProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAcctCallLogProfile_Action_o.setStatus("mandatory")


class _RadAcctCallLogProfile_VoipCallLogging_Type(Integer32):
    """Custom type radAcctCallLogProfile_VoipCallLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RadAcctCallLogProfile_VoipCallLogging_Type.__name__ = "Integer32"
_RadAcctCallLogProfile_VoipCallLogging_Object = MibScalar
radAcctCallLogProfile_VoipCallLogging = _RadAcctCallLogProfile_VoipCallLogging_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 143, 1, 1, 20),
    _RadAcctCallLogProfile_VoipCallLogging_Type()
)
radAcctCallLogProfile_VoipCallLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAcctCallLogProfile_VoipCallLogging.setStatus("mandatory")


class _RadAcctCallLogProfile_CallLogSwitchover_Type(Integer32):
    """Custom type radAcctCallLogProfile_CallLogSwitchover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RadAcctCallLogProfile_CallLogSwitchover_Type.__name__ = "Integer32"
_RadAcctCallLogProfile_CallLogSwitchover_Object = MibScalar
radAcctCallLogProfile_CallLogSwitchover = _RadAcctCallLogProfile_CallLogSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 143, 1, 1, 21),
    _RadAcctCallLogProfile_CallLogSwitchover_Type()
)
radAcctCallLogProfile_CallLogSwitchover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAcctCallLogProfile_CallLogSwitchover.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBXAUTH-MIB",
    **{"DisplayString": DisplayString,
       "mibradStatProfile": mibradStatProfile,
       "mibradStatProfileTable": mibradStatProfileTable,
       "mibradStatProfileEntry": mibradStatProfileEntry,
       "radStatProfile-Index-o": radStatProfile_Index_o,
       "radStatProfile-CurrentAuthServer": radStatProfile_CurrentAuthServer,
       "radStatProfile-CurrentAcctServer": radStatProfile_CurrentAcctServer,
       "radStatProfile-Action-o": radStatProfile_Action_o,
       "mibexternalAuthProfile": mibexternalAuthProfile,
       "mibexternalAuthProfileTable": mibexternalAuthProfileTable,
       "mibexternalAuthProfileEntry": mibexternalAuthProfileEntry,
       "externalAuthProfile-Index-o": externalAuthProfile_Index_o,
       "externalAuthProfile-AuthType": externalAuthProfile_AuthType,
       "externalAuthProfile-AcctType": externalAuthProfile_AcctType,
       "externalAuthProfile-RadServEnable": externalAuthProfile_RadServEnable,
       "externalAuthProfile-RadAuthClient-AuthPort": externalAuthProfile_RadAuthClient_AuthPort,
       "externalAuthProfile-RadAuthClient-AuthSrcPort": externalAuthProfile_RadAuthClient_AuthSrcPort,
       "externalAuthProfile-RadAuthClient-AuthKey": externalAuthProfile_RadAuthClient_AuthKey,
       "externalAuthProfile-RadAuthClient-AuthPool": externalAuthProfile_RadAuthClient_AuthPool,
       "externalAuthProfile-RadAuthClient-AuthTimeout": externalAuthProfile_RadAuthClient_AuthTimeout,
       "externalAuthProfile-RadAuthClient-AuthRspRequired": externalAuthProfile_RadAuthClient_AuthRspRequired,
       "externalAuthProfile-RadAuthClient-AuthIdFailReturnBusy": externalAuthProfile_RadAuthClient_AuthIdFailReturnBusy,
       "externalAuthProfile-RadAuthClient-AuthIdTimeoutReturnBusy": externalAuthProfile_RadAuthClient_AuthIdTimeoutReturnBusy,
       "externalAuthProfile-RadAuthClient-AuthSessInterval": externalAuthProfile_RadAuthClient_AuthSessInterval,
       "externalAuthProfile-RadAuthClient-AuthTSSecure": externalAuthProfile_RadAuthClient_AuthTSSecure,
       "externalAuthProfile-RadAuthClient-AuthSend67": externalAuthProfile_RadAuthClient_AuthSend67,
       "externalAuthProfile-RadAuthClient-AuthFrmAdrStart": externalAuthProfile_RadAuthClient_AuthFrmAdrStart,
       "externalAuthProfile-RadAuthClient-AuthBootHost": externalAuthProfile_RadAuthClient_AuthBootHost,
       "externalAuthProfile-RadAuthClient-AuthBootHost2": externalAuthProfile_RadAuthClient_AuthBootHost2,
       "externalAuthProfile-RadAuthClient-AuthBootPort": externalAuthProfile_RadAuthClient_AuthBootPort,
       "externalAuthProfile-RadAuthClient-AuthResetTime": externalAuthProfile_RadAuthClient_AuthResetTime,
       "externalAuthProfile-RadAuthClient-AuthIdMaxRetryTime": externalAuthProfile_RadAuthClient_AuthIdMaxRetryTime,
       "externalAuthProfile-RadAuthClient-AuthRadiusCompat": externalAuthProfile_RadAuthClient_AuthRadiusCompat,
       "externalAuthProfile-RadAuthClient-AuthKeepUserName": externalAuthProfile_RadAuthClient_AuthKeepUserName,
       "externalAuthProfile-RadAuthClient-AuthRealmDelimiters": externalAuthProfile_RadAuthClient_AuthRealmDelimiters,
       "externalAuthProfile-RadAuthClient-IdAuthPrefix": externalAuthProfile_RadAuthClient_IdAuthPrefix,
       "externalAuthProfile-RadAuthClient-AllowAuthConfigRqsts": externalAuthProfile_RadAuthClient_AllowAuthConfigRqsts,
       "externalAuthProfile-RadAuthClient-AuthReqDelimCount": externalAuthProfile_RadAuthClient_AuthReqDelimCount,
       "externalAuthProfile-RadAuthClient-AuthReqStripSide": externalAuthProfile_RadAuthClient_AuthReqStripSide,
       "externalAuthProfile-RadAcctClient-AcctPort": externalAuthProfile_RadAcctClient_AcctPort,
       "externalAuthProfile-RadAcctClient-AcctSrcPort": externalAuthProfile_RadAcctClient_AcctSrcPort,
       "externalAuthProfile-RadAcctClient-AcctKey": externalAuthProfile_RadAcctClient_AcctKey,
       "externalAuthProfile-RadAcctClient-AcctTimeout": externalAuthProfile_RadAcctClient_AcctTimeout,
       "externalAuthProfile-RadAcctClient-AcctSessInterval": externalAuthProfile_RadAcctClient_AcctSessInterval,
       "externalAuthProfile-RadAcctClient-AcctIdBase": externalAuthProfile_RadAcctClient_AcctIdBase,
       "externalAuthProfile-RadAcctClient-AcctResetTime": externalAuthProfile_RadAcctClient_AcctResetTime,
       "externalAuthProfile-RadAcctClient-AcctCheckpoint": externalAuthProfile_RadAcctClient_AcctCheckpoint,
       "externalAuthProfile-RadAcctClient-AcctCheckpointTimer": externalAuthProfile_RadAcctClient_AcctCheckpointTimer,
       "externalAuthProfile-RadAcctClient-AcctStopOnly": externalAuthProfile_RadAcctClient_AcctStopOnly,
       "externalAuthProfile-RadAcctClient-AcctLimitRetry": externalAuthProfile_RadAcctClient_AcctLimitRetry,
       "externalAuthProfile-RadAcctClient-AcctDropStopOnAuthFail": externalAuthProfile_RadAcctClient_AcctDropStopOnAuthFail,
       "externalAuthProfile-RadAcctClient-AcctRadiusCompat": externalAuthProfile_RadAcctClient_AcctRadiusCompat,
       "externalAuthProfile-RadAcctClient-TunnelAccounting": externalAuthProfile_RadAcctClient_TunnelAccounting,
       "externalAuthProfile-RadAuthServer-AuthPort": externalAuthProfile_RadAuthServer_AuthPort,
       "externalAuthProfile-RadAuthServer-AuthSessionKey": externalAuthProfile_RadAuthServer_AuthSessionKey,
       "externalAuthProfile-RadAuthServer-AuthAttributeType": externalAuthProfile_RadAuthServer_AuthAttributeType,
       "externalAuthProfile-RadAuthServer-AuthRadiusCompat": externalAuthProfile_RadAuthServer_AuthRadiusCompat,
       "externalAuthProfile-TacAuthClient-AuthServer1": externalAuthProfile_TacAuthClient_AuthServer1,
       "externalAuthProfile-TacAuthClient-AuthServer2": externalAuthProfile_TacAuthClient_AuthServer2,
       "externalAuthProfile-TacAuthClient-AuthServer3": externalAuthProfile_TacAuthClient_AuthServer3,
       "externalAuthProfile-TacAuthClient-AuthPort": externalAuthProfile_TacAuthClient_AuthPort,
       "externalAuthProfile-TacAuthClient-AuthSrcPort": externalAuthProfile_TacAuthClient_AuthSrcPort,
       "externalAuthProfile-TacAuthClient-AuthKey": externalAuthProfile_TacAuthClient_AuthKey,
       "externalAuthProfile-TacAuthClient-AuthTimeout": externalAuthProfile_TacAuthClient_AuthTimeout,
       "externalAuthProfile-TacplusAuthClient-AuthServer1": externalAuthProfile_TacplusAuthClient_AuthServer1,
       "externalAuthProfile-TacplusAuthClient-AuthServer2": externalAuthProfile_TacplusAuthClient_AuthServer2,
       "externalAuthProfile-TacplusAuthClient-AuthServer3": externalAuthProfile_TacplusAuthClient_AuthServer3,
       "externalAuthProfile-TacplusAuthClient-AuthPort": externalAuthProfile_TacplusAuthClient_AuthPort,
       "externalAuthProfile-TacplusAuthClient-AuthSrcPort": externalAuthProfile_TacplusAuthClient_AuthSrcPort,
       "externalAuthProfile-TacplusAuthClient-AuthKey": externalAuthProfile_TacplusAuthClient_AuthKey,
       "externalAuthProfile-TacplusAuthClient-AuthTimeoutTime": externalAuthProfile_TacplusAuthClient_AuthTimeoutTime,
       "externalAuthProfile-TacplusAuthClient-AuthRetries": externalAuthProfile_TacplusAuthClient_AuthRetries,
       "externalAuthProfile-TacplusAcctClient-AcctServer1": externalAuthProfile_TacplusAcctClient_AcctServer1,
       "externalAuthProfile-TacplusAcctClient-AcctServer2": externalAuthProfile_TacplusAcctClient_AcctServer2,
       "externalAuthProfile-TacplusAcctClient-AcctServer3": externalAuthProfile_TacplusAcctClient_AcctServer3,
       "externalAuthProfile-TacplusAcctClient-AcctPort": externalAuthProfile_TacplusAcctClient_AcctPort,
       "externalAuthProfile-TacplusAcctClient-AcctSrcPort": externalAuthProfile_TacplusAcctClient_AcctSrcPort,
       "externalAuthProfile-TacplusAcctClient-AcctKey": externalAuthProfile_TacplusAcctClient_AcctKey,
       "externalAuthProfile-SecureidAuthClient-AuthServer1": externalAuthProfile_SecureidAuthClient_AuthServer1,
       "externalAuthProfile-SecureidAuthClient-AuthServer2": externalAuthProfile_SecureidAuthClient_AuthServer2,
       "externalAuthProfile-SecureidAuthClient-AuthServer3": externalAuthProfile_SecureidAuthClient_AuthServer3,
       "externalAuthProfile-SecureidAuthClient-AuthPort": externalAuthProfile_SecureidAuthClient_AuthPort,
       "externalAuthProfile-SecureidAuthClient-AuthTimeout": externalAuthProfile_SecureidAuthClient_AuthTimeout,
       "externalAuthProfile-SecureidAuthClient-AuthRetrycount": externalAuthProfile_SecureidAuthClient_AuthRetrycount,
       "externalAuthProfile-SecureidAuthClient-AuthDes": externalAuthProfile_SecureidAuthClient_AuthDes,
       "externalAuthProfile-SecureidAuthClient-AuthNodeSecret": externalAuthProfile_SecureidAuthClient_AuthNodeSecret,
       "externalAuthProfile-PasswordProfile-Clid": externalAuthProfile_PasswordProfile_Clid,
       "externalAuthProfile-PasswordProfile-Dnis": externalAuthProfile_PasswordProfile_Dnis,
       "externalAuthProfile-PasswordProfile-Banner": externalAuthProfile_PasswordProfile_Banner,
       "externalAuthProfile-PasswordProfile-InitBanner": externalAuthProfile_PasswordProfile_InitBanner,
       "externalAuthProfile-PasswordProfile-Pool": externalAuthProfile_PasswordProfile_Pool,
       "externalAuthProfile-PasswordProfile-Frdl": externalAuthProfile_PasswordProfile_Frdl,
       "externalAuthProfile-PasswordProfile-Dialout": externalAuthProfile_PasswordProfile_Dialout,
       "externalAuthProfile-PasswordProfile-DialoutRoutes": externalAuthProfile_PasswordProfile_DialoutRoutes,
       "externalAuthProfile-PasswordProfile-DialoutIpxRoutes": externalAuthProfile_PasswordProfile_DialoutIpxRoutes,
       "externalAuthProfile-PasswordProfile-DialoutAtalkRoutes": externalAuthProfile_PasswordProfile_DialoutAtalkRoutes,
       "externalAuthProfile-PasswordProfile-SourceAuth": externalAuthProfile_PasswordProfile_SourceAuth,
       "externalAuthProfile-LocalProfilesFirst": externalAuthProfile_LocalProfilesFirst,
       "externalAuthProfile-Noattr6UseTermsrv": externalAuthProfile_Noattr6UseTermsrv,
       "externalAuthProfile-Clid": externalAuthProfile_Clid,
       "externalAuthProfile-Dnis": externalAuthProfile_Dnis,
       "externalAuthProfile-Action-o": externalAuthProfile_Action_o,
       "externalAuthProfile-RadAuthClient-AuthNetworkRouteServer": externalAuthProfile_RadAuthClient_AuthNetworkRouteServer,
       "externalAuthProfile-RadAuthClient-IdAuthPrefixX25": externalAuthProfile_RadAuthClient_IdAuthPrefixX25,
       "externalAuthProfile-CliUserAuth": externalAuthProfile_CliUserAuth,
       "externalAuthProfile-RadAuthClient-AllowUnencryptedTunnelPassword": externalAuthProfile_RadAuthClient_AllowUnencryptedTunnelPassword,
       "externalAuthProfile-RadAuthClient-AuthCliUserDnis": externalAuthProfile_RadAuthClient_AuthCliUserDnis,
       "externalAuthProfile-RadAuthClient-AllowNasPortTypeInCliUserAuth": externalAuthProfile_RadAuthClient_AllowNasPortTypeInCliUserAuth,
       "externalAuthProfile-RadAuthClient-AuthHost1": externalAuthProfile_RadAuthClient_AuthHost1,
       "externalAuthProfile-RadAuthClient-AuthHost2": externalAuthProfile_RadAuthClient_AuthHost2,
       "externalAuthProfile-RadAuthClient-AuthHost3": externalAuthProfile_RadAuthClient_AuthHost3,
       "externalAuthProfile-RadAcctClient-AcctHost1": externalAuthProfile_RadAcctClient_AcctHost1,
       "externalAuthProfile-RadAcctClient-AcctHost2": externalAuthProfile_RadAcctClient_AcctHost2,
       "externalAuthProfile-RadAcctClient-AcctHost3": externalAuthProfile_RadAcctClient_AcctHost3,
       "externalAuthProfile-RadAcctClient-VoipAccounting": externalAuthProfile_RadAcctClient_VoipAccounting,
       "externalAuthProfile-RadAcctClient-AcctOnSwitchover": externalAuthProfile_RadAcctClient_AcctOnSwitchover,
       "mibexternalAuthProfile-RadAuthServer-AuthKeyTable": mibexternalAuthProfile_RadAuthServer_AuthKeyTable,
       "mibexternalAuthProfile-RadAuthServer-AuthKeyEntry": mibexternalAuthProfile_RadAuthServer_AuthKeyEntry,
       "externalAuthProfile-RadAuthServer-AuthKey-Index-o": externalAuthProfile_RadAuthServer_AuthKey_Index_o,
       "externalAuthProfile-RadAuthServer-AuthKey-Index1-o": externalAuthProfile_RadAuthServer_AuthKey_Index1_o,
       "externalAuthProfile-RadAuthServer-AuthKey": externalAuthProfile_RadAuthServer_AuthKey,
       "mibexternalAuthProfile-RadAuthServer-AuthNetmaskTable": mibexternalAuthProfile_RadAuthServer_AuthNetmaskTable,
       "mibexternalAuthProfile-RadAuthServer-AuthNetmaskEntry": mibexternalAuthProfile_RadAuthServer_AuthNetmaskEntry,
       "externalAuthProfile-RadAuthServer-AuthNetmask-Index-o": externalAuthProfile_RadAuthServer_AuthNetmask_Index_o,
       "externalAuthProfile-RadAuthServer-AuthNetmask-Index1-o": externalAuthProfile_RadAuthServer_AuthNetmask_Index1_o,
       "externalAuthProfile-RadAuthServer-AuthNetmask": externalAuthProfile_RadAuthServer_AuthNetmask,
       "mibexternalAuthProfile-RadAuthServer-AuthClientTable": mibexternalAuthProfile_RadAuthServer_AuthClientTable,
       "mibexternalAuthProfile-RadAuthServer-AuthClientEntry": mibexternalAuthProfile_RadAuthServer_AuthClientEntry,
       "externalAuthProfile-RadAuthServer-AuthClient-Index-o": externalAuthProfile_RadAuthServer_AuthClient_Index_o,
       "externalAuthProfile-RadAuthServer-AuthClient-Index1-o": externalAuthProfile_RadAuthServer_AuthClient_Index1_o,
       "externalAuthProfile-RadAuthServer-AuthClient": externalAuthProfile_RadAuthServer_AuthClient,
       "mibradAcctCallLogProfile": mibradAcctCallLogProfile,
       "mibradAcctCallLogProfileTable": mibradAcctCallLogProfileTable,
       "mibradAcctCallLogProfileEntry": mibradAcctCallLogProfileEntry,
       "radAcctCallLogProfile-Index-o": radAcctCallLogProfile_Index_o,
       "radAcctCallLogProfile-CallLogEnable": radAcctCallLogProfile_CallLogEnable,
       "radAcctCallLogProfile-CallLogHost1": radAcctCallLogProfile_CallLogHost1,
       "radAcctCallLogProfile-CallLogHost2": radAcctCallLogProfile_CallLogHost2,
       "radAcctCallLogProfile-CallLogHost3": radAcctCallLogProfile_CallLogHost3,
       "radAcctCallLogProfile-CallLogPort": radAcctCallLogProfile_CallLogPort,
       "radAcctCallLogProfile-CallLogKey": radAcctCallLogProfile_CallLogKey,
       "radAcctCallLogProfile-CallLogTimeout": radAcctCallLogProfile_CallLogTimeout,
       "radAcctCallLogProfile-CallLogIdBase": radAcctCallLogProfile_CallLogIdBase,
       "radAcctCallLogProfile-CallLogResetTime": radAcctCallLogProfile_CallLogResetTime,
       "radAcctCallLogProfile-CallLogStopOnly": radAcctCallLogProfile_CallLogStopOnly,
       "radAcctCallLogProfile-CallLogLimitRetry": radAcctCallLogProfile_CallLogLimitRetry,
       "radAcctCallLogProfile-CallLogRadiusCompat": radAcctCallLogProfile_CallLogRadiusCompat,
       "radAcctCallLogProfile-CallLogServerIndex": radAcctCallLogProfile_CallLogServerIndex,
       "radAcctCallLogProfile-CallLogMultiPacket": radAcctCallLogProfile_CallLogMultiPacket,
       "radAcctCallLogProfile-CallLogStreamPeriod": radAcctCallLogProfile_CallLogStreamPeriod,
       "radAcctCallLogProfile-CallLogConnectionPacketsEnable": radAcctCallLogProfile_CallLogConnectionPacketsEnable,
       "radAcctCallLogProfile-CallLogCsmModemDiag": radAcctCallLogProfile_CallLogCsmModemDiag,
       "radAcctCallLogProfile-Action-o": radAcctCallLogProfile_Action_o,
       "radAcctCallLogProfile-VoipCallLogging": radAcctCallLogProfile_VoipCallLogging,
       "radAcctCallLogProfile-CallLogSwitchover": radAcctCallLogProfile_CallLogSwitchover}
)
