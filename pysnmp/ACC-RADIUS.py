# SNMP MIB module (ACC-RADIUS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-RADIUS
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:52 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccRadius_ObjectIdentity = ObjectIdentity
accRadius = _AccRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44)
)
_AccRadiusNASIdentifier_Type = OctetString
_AccRadiusNASIdentifier_Object = MibScalar
accRadiusNASIdentifier = _AccRadiusNASIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 1),
    _AccRadiusNASIdentifier_Type()
)
accRadiusNASIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusNASIdentifier.setStatus("mandatory")


class _AccRadiusInvAttribAction_Type(Integer32):
    """Custom type accRadiusInvAttribAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_AccRadiusInvAttribAction_Type.__name__ = "Integer32"
_AccRadiusInvAttribAction_Object = MibScalar
accRadiusInvAttribAction = _AccRadiusInvAttribAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 2),
    _AccRadiusInvAttribAction_Type()
)
accRadiusInvAttribAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusInvAttribAction.setStatus("mandatory")


class _AccRadiusMaxPort_Type(Integer32):
    """Custom type accRadiusMaxPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_AccRadiusMaxPort_Type.__name__ = "Integer32"
_AccRadiusMaxPort_Object = MibScalar
accRadiusMaxPort = _AccRadiusMaxPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 3),
    _AccRadiusMaxPort_Type()
)
accRadiusMaxPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusMaxPort.setStatus("mandatory")
_AccRadiusPortRangeStart_Type = Integer32
_AccRadiusPortRangeStart_Object = MibScalar
accRadiusPortRangeStart = _AccRadiusPortRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 4),
    _AccRadiusPortRangeStart_Type()
)
accRadiusPortRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRadiusPortRangeStart.setStatus("mandatory")
_AccRadiusPortRangeEnd_Type = Integer32
_AccRadiusPortRangeEnd_Object = MibScalar
accRadiusPortRangeEnd = _AccRadiusPortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 5),
    _AccRadiusPortRangeEnd_Type()
)
accRadiusPortRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRadiusPortRangeEnd.setStatus("mandatory")
_AccRadiusAuth_ObjectIdentity = ObjectIdentity
accRadiusAuth = _AccRadiusAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 6)
)
_AccRadiusAuthServTable_Object = MibTable
accRadiusAuthServTable = _AccRadiusAuthServTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 6, 1)
)
if mibBuilder.loadTexts:
    accRadiusAuthServTable.setStatus("mandatory")
_AccRadiusAuthServEntry_Object = MibTableRow
accRadiusAuthServEntry = _AccRadiusAuthServEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 6, 1, 1)
)
accRadiusAuthServEntry.setIndexNames(
    (0, "ACC-RADIUS", "accRadiusAuthServIndex"),
)
if mibBuilder.loadTexts:
    accRadiusAuthServEntry.setStatus("mandatory")


class _AccRadiusAuthServIndex_Type(Integer32):
    """Custom type accRadiusAuthServIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AccRadiusAuthServIndex_Type.__name__ = "Integer32"
_AccRadiusAuthServIndex_Object = MibTableColumn
accRadiusAuthServIndex = _AccRadiusAuthServIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 6, 1, 1, 1),
    _AccRadiusAuthServIndex_Type()
)
accRadiusAuthServIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAuthServIndex.setStatus("mandatory")


class _AccRadiusAuthServAdState_Type(Integer32):
    """Custom type accRadiusAuthServAdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_AccRadiusAuthServAdState_Type.__name__ = "Integer32"
_AccRadiusAuthServAdState_Object = MibTableColumn
accRadiusAuthServAdState = _AccRadiusAuthServAdState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 6, 1, 1, 2),
    _AccRadiusAuthServAdState_Type()
)
accRadiusAuthServAdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAuthServAdState.setStatus("mandatory")
_AccRadiusAuthServAddr_Type = IpAddress
_AccRadiusAuthServAddr_Object = MibTableColumn
accRadiusAuthServAddr = _AccRadiusAuthServAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 6, 1, 1, 3),
    _AccRadiusAuthServAddr_Type()
)
accRadiusAuthServAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAuthServAddr.setStatus("mandatory")
_AccRadiusAuthServPassword_Type = OctetString
_AccRadiusAuthServPassword_Object = MibTableColumn
accRadiusAuthServPassword = _AccRadiusAuthServPassword_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 6, 1, 1, 4),
    _AccRadiusAuthServPassword_Type()
)
accRadiusAuthServPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAuthServPassword.setStatus("mandatory")
_AccRadiusAuthServRetryInt_Type = TimeTicks
_AccRadiusAuthServRetryInt_Object = MibTableColumn
accRadiusAuthServRetryInt = _AccRadiusAuthServRetryInt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 6, 1, 1, 5),
    _AccRadiusAuthServRetryInt_Type()
)
accRadiusAuthServRetryInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAuthServRetryInt.setStatus("mandatory")


class _AccRadiusAuthServRetryCnts_Type(Integer32):
    """Custom type accRadiusAuthServRetryCnts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AccRadiusAuthServRetryCnts_Type.__name__ = "Integer32"
_AccRadiusAuthServRetryCnts_Object = MibTableColumn
accRadiusAuthServRetryCnts = _AccRadiusAuthServRetryCnts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 6, 1, 1, 6),
    _AccRadiusAuthServRetryCnts_Type()
)
accRadiusAuthServRetryCnts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAuthServRetryCnts.setStatus("mandatory")


class _AccRadiusAuthServUDPPort_Type(Integer32):
    """Custom type accRadiusAuthServUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccRadiusAuthServUDPPort_Type.__name__ = "Integer32"
_AccRadiusAuthServUDPPort_Object = MibTableColumn
accRadiusAuthServUDPPort = _AccRadiusAuthServUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 6, 1, 1, 7),
    _AccRadiusAuthServUDPPort_Type()
)
accRadiusAuthServUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAuthServUDPPort.setStatus("mandatory")


class _AccRadiusAuthServOpState_Type(Integer32):
    """Custom type accRadiusAuthServOpState based on Integer32"""
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
        *(("disabled", 4),
          ("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_AccRadiusAuthServOpState_Type.__name__ = "Integer32"
_AccRadiusAuthServOpState_Object = MibTableColumn
accRadiusAuthServOpState = _AccRadiusAuthServOpState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 6, 1, 1, 8),
    _AccRadiusAuthServOpState_Type()
)
accRadiusAuthServOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRadiusAuthServOpState.setStatus("mandatory")
_AccRadiusAuthServReqCnts_Type = Counter32
_AccRadiusAuthServReqCnts_Object = MibTableColumn
accRadiusAuthServReqCnts = _AccRadiusAuthServReqCnts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 6, 1, 1, 9),
    _AccRadiusAuthServReqCnts_Type()
)
accRadiusAuthServReqCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRadiusAuthServReqCnts.setStatus("mandatory")
_AccRadiusAuthServAccCnts_Type = Counter32
_AccRadiusAuthServAccCnts_Object = MibTableColumn
accRadiusAuthServAccCnts = _AccRadiusAuthServAccCnts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 6, 1, 1, 10),
    _AccRadiusAuthServAccCnts_Type()
)
accRadiusAuthServAccCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRadiusAuthServAccCnts.setStatus("mandatory")
_AccRadiusAuthServRejCnts_Type = Counter32
_AccRadiusAuthServRejCnts_Object = MibTableColumn
accRadiusAuthServRejCnts = _AccRadiusAuthServRejCnts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 6, 1, 1, 11),
    _AccRadiusAuthServRejCnts_Type()
)
accRadiusAuthServRejCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRadiusAuthServRejCnts.setStatus("mandatory")
_AccRadiusAuthServAccessPart_Type = DisplayString
_AccRadiusAuthServAccessPart_Object = MibTableColumn
accRadiusAuthServAccessPart = _AccRadiusAuthServAccessPart_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 6, 1, 1, 12),
    _AccRadiusAuthServAccessPart_Type()
)
accRadiusAuthServAccessPart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAuthServAccessPart.setStatus("obsolete")


class _AccRadiusAuthServSecure_Type(Integer32):
    """Custom type accRadiusAuthServSecure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("secure", 1),
          ("unsecure", 2))
    )


_AccRadiusAuthServSecure_Type.__name__ = "Integer32"
_AccRadiusAuthServSecure_Object = MibTableColumn
accRadiusAuthServSecure = _AccRadiusAuthServSecure_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 6, 1, 1, 13),
    _AccRadiusAuthServSecure_Type()
)
accRadiusAuthServSecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAuthServSecure.setStatus("mandatory")


class _AccRadiusAuthMsgLvl_Type(Integer32):
    """Custom type accRadiusAuthMsgLvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccRadiusAuthMsgLvl_Type.__name__ = "Integer32"
_AccRadiusAuthMsgLvl_Object = MibScalar
accRadiusAuthMsgLvl = _AccRadiusAuthMsgLvl_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 6, 2),
    _AccRadiusAuthMsgLvl_Type()
)
accRadiusAuthMsgLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAuthMsgLvl.setStatus("mandatory")
_AccRadiusAuthRecoverTO_Type = TimeTicks
_AccRadiusAuthRecoverTO_Object = MibScalar
accRadiusAuthRecoverTO = _AccRadiusAuthRecoverTO_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 6, 3),
    _AccRadiusAuthRecoverTO_Type()
)
accRadiusAuthRecoverTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAuthRecoverTO.setStatus("mandatory")
_AccRadiusAuthReqDiscs_Type = Counter32
_AccRadiusAuthReqDiscs_Object = MibScalar
accRadiusAuthReqDiscs = _AccRadiusAuthReqDiscs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 6, 4),
    _AccRadiusAuthReqDiscs_Type()
)
accRadiusAuthReqDiscs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAuthReqDiscs.setStatus("mandatory")
_AccRadiusAuthRespDiscs_Type = Counter32
_AccRadiusAuthRespDiscs_Object = MibScalar
accRadiusAuthRespDiscs = _AccRadiusAuthRespDiscs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 6, 5),
    _AccRadiusAuthRespDiscs_Type()
)
accRadiusAuthRespDiscs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAuthRespDiscs.setStatus("mandatory")
_AccRadiusAuthLastUser_Type = OctetString
_AccRadiusAuthLastUser_Object = MibScalar
accRadiusAuthLastUser = _AccRadiusAuthLastUser_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 6, 6),
    _AccRadiusAuthLastUser_Type()
)
accRadiusAuthLastUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRadiusAuthLastUser.setStatus("mandatory")


class _AccRadiusAuthLastType_Type(Integer32):
    """Custom type accRadiusAuthLastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("access-accept", 2),
          ("access-reject", 3),
          ("access-request", 1))
    )


_AccRadiusAuthLastType_Type.__name__ = "Integer32"
_AccRadiusAuthLastType_Object = MibScalar
accRadiusAuthLastType = _AccRadiusAuthLastType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 6, 7),
    _AccRadiusAuthLastType_Type()
)
accRadiusAuthLastType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAuthLastType.setStatus("mandatory")
_AccRadiusAuthCallsRejs_Type = Counter32
_AccRadiusAuthCallsRejs_Object = MibScalar
accRadiusAuthCallsRejs = _AccRadiusAuthCallsRejs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 6, 8),
    _AccRadiusAuthCallsRejs_Type()
)
accRadiusAuthCallsRejs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAuthCallsRejs.setStatus("mandatory")
_AccRadiusAuthConfigErrs_Type = Counter32
_AccRadiusAuthConfigErrs_Object = MibScalar
accRadiusAuthConfigErrs = _AccRadiusAuthConfigErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 6, 9),
    _AccRadiusAuthConfigErrs_Type()
)
accRadiusAuthConfigErrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAuthConfigErrs.setStatus("mandatory")
_AccRadiusAuthDebugTable_Object = MibTable
accRadiusAuthDebugTable = _AccRadiusAuthDebugTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 6, 10)
)
if mibBuilder.loadTexts:
    accRadiusAuthDebugTable.setStatus("mandatory")
_AccRadiusAuthDebugEntry_Object = MibTableRow
accRadiusAuthDebugEntry = _AccRadiusAuthDebugEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 6, 10, 1)
)
accRadiusAuthDebugEntry.setIndexNames(
    (0, "ACC-RADIUS", "accRadiusAuthDebugName"),
)
if mibBuilder.loadTexts:
    accRadiusAuthDebugEntry.setStatus("mandatory")
_AccRadiusAuthDebugName_Type = OctetString
_AccRadiusAuthDebugName_Object = MibTableColumn
accRadiusAuthDebugName = _AccRadiusAuthDebugName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 6, 10, 1, 1),
    _AccRadiusAuthDebugName_Type()
)
accRadiusAuthDebugName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAuthDebugName.setStatus("mandatory")
_AccRadiusAuthDebugMask_Type = Integer32
_AccRadiusAuthDebugMask_Object = MibTableColumn
accRadiusAuthDebugMask = _AccRadiusAuthDebugMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 6, 10, 1, 2),
    _AccRadiusAuthDebugMask_Type()
)
accRadiusAuthDebugMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAuthDebugMask.setStatus("mandatory")
_AccRadiusAcct_ObjectIdentity = ObjectIdentity
accRadiusAcct = _AccRadiusAcct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 7)
)
_AccRadiusAcctServTable_Object = MibTable
accRadiusAcctServTable = _AccRadiusAcctServTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 7, 1)
)
if mibBuilder.loadTexts:
    accRadiusAcctServTable.setStatus("mandatory")
_AccRadiusAcctServEntry_Object = MibTableRow
accRadiusAcctServEntry = _AccRadiusAcctServEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 7, 1, 1)
)
accRadiusAcctServEntry.setIndexNames(
    (0, "ACC-RADIUS", "accRadiusAcctServIndex"),
)
if mibBuilder.loadTexts:
    accRadiusAcctServEntry.setStatus("mandatory")


class _AccRadiusAcctServIndex_Type(Integer32):
    """Custom type accRadiusAcctServIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AccRadiusAcctServIndex_Type.__name__ = "Integer32"
_AccRadiusAcctServIndex_Object = MibTableColumn
accRadiusAcctServIndex = _AccRadiusAcctServIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 7, 1, 1, 1),
    _AccRadiusAcctServIndex_Type()
)
accRadiusAcctServIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAcctServIndex.setStatus("mandatory")


class _AccRadiusAcctServAdState_Type(Integer32):
    """Custom type accRadiusAcctServAdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_AccRadiusAcctServAdState_Type.__name__ = "Integer32"
_AccRadiusAcctServAdState_Object = MibTableColumn
accRadiusAcctServAdState = _AccRadiusAcctServAdState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 7, 1, 1, 2),
    _AccRadiusAcctServAdState_Type()
)
accRadiusAcctServAdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAcctServAdState.setStatus("mandatory")
_AccRadiusAcctServAddr_Type = IpAddress
_AccRadiusAcctServAddr_Object = MibTableColumn
accRadiusAcctServAddr = _AccRadiusAcctServAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 7, 1, 1, 3),
    _AccRadiusAcctServAddr_Type()
)
accRadiusAcctServAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAcctServAddr.setStatus("mandatory")
_AccRadiusAcctServPassword_Type = OctetString
_AccRadiusAcctServPassword_Object = MibTableColumn
accRadiusAcctServPassword = _AccRadiusAcctServPassword_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 7, 1, 1, 4),
    _AccRadiusAcctServPassword_Type()
)
accRadiusAcctServPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAcctServPassword.setStatus("mandatory")
_AccRadiusAcctServRetryInt_Type = TimeTicks
_AccRadiusAcctServRetryInt_Object = MibTableColumn
accRadiusAcctServRetryInt = _AccRadiusAcctServRetryInt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 7, 1, 1, 5),
    _AccRadiusAcctServRetryInt_Type()
)
accRadiusAcctServRetryInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAcctServRetryInt.setStatus("mandatory")


class _AccRadiusAcctServRetryCnts_Type(Integer32):
    """Custom type accRadiusAcctServRetryCnts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AccRadiusAcctServRetryCnts_Type.__name__ = "Integer32"
_AccRadiusAcctServRetryCnts_Object = MibTableColumn
accRadiusAcctServRetryCnts = _AccRadiusAcctServRetryCnts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 7, 1, 1, 6),
    _AccRadiusAcctServRetryCnts_Type()
)
accRadiusAcctServRetryCnts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAcctServRetryCnts.setStatus("mandatory")


class _AccRadiusAcctServUDPPort_Type(Integer32):
    """Custom type accRadiusAcctServUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccRadiusAcctServUDPPort_Type.__name__ = "Integer32"
_AccRadiusAcctServUDPPort_Object = MibTableColumn
accRadiusAcctServUDPPort = _AccRadiusAcctServUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 7, 1, 1, 7),
    _AccRadiusAcctServUDPPort_Type()
)
accRadiusAcctServUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAcctServUDPPort.setStatus("mandatory")


class _AccRadiusAcctServOpState_Type(Integer32):
    """Custom type accRadiusAcctServOpState based on Integer32"""
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
        *(("disabled", 4),
          ("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_AccRadiusAcctServOpState_Type.__name__ = "Integer32"
_AccRadiusAcctServOpState_Object = MibTableColumn
accRadiusAcctServOpState = _AccRadiusAcctServOpState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 7, 1, 1, 8),
    _AccRadiusAcctServOpState_Type()
)
accRadiusAcctServOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRadiusAcctServOpState.setStatus("mandatory")
_AccRadiusAcctServReqCnts_Type = Counter32
_AccRadiusAcctServReqCnts_Object = MibTableColumn
accRadiusAcctServReqCnts = _AccRadiusAcctServReqCnts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 7, 1, 1, 9),
    _AccRadiusAcctServReqCnts_Type()
)
accRadiusAcctServReqCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRadiusAcctServReqCnts.setStatus("mandatory")
_AccRadiusAcctServAccCnts_Type = Counter32
_AccRadiusAcctServAccCnts_Object = MibTableColumn
accRadiusAcctServAccCnts = _AccRadiusAcctServAccCnts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 7, 1, 1, 10),
    _AccRadiusAcctServAccCnts_Type()
)
accRadiusAcctServAccCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRadiusAcctServAccCnts.setStatus("mandatory")
_AccRadiusAcctServAccessPart_Type = DisplayString
_AccRadiusAcctServAccessPart_Object = MibTableColumn
accRadiusAcctServAccessPart = _AccRadiusAcctServAccessPart_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 7, 1, 1, 11),
    _AccRadiusAcctServAccessPart_Type()
)
accRadiusAcctServAccessPart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAcctServAccessPart.setStatus("obsolete")


class _AccRadiusAcctServIBCAttrSupp_Type(Integer32):
    """Custom type accRadiusAcctServIBCAttrSupp based on Integer32"""
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


_AccRadiusAcctServIBCAttrSupp_Type.__name__ = "Integer32"
_AccRadiusAcctServIBCAttrSupp_Object = MibTableColumn
accRadiusAcctServIBCAttrSupp = _AccRadiusAcctServIBCAttrSupp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 7, 1, 1, 13),
    _AccRadiusAcctServIBCAttrSupp_Type()
)
accRadiusAcctServIBCAttrSupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAcctServIBCAttrSupp.setStatus("mandatory")


class _AccRadiusAcctMsgLvl_Type(Integer32):
    """Custom type accRadiusAcctMsgLvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccRadiusAcctMsgLvl_Type.__name__ = "Integer32"
_AccRadiusAcctMsgLvl_Object = MibScalar
accRadiusAcctMsgLvl = _AccRadiusAcctMsgLvl_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 7, 2),
    _AccRadiusAcctMsgLvl_Type()
)
accRadiusAcctMsgLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAcctMsgLvl.setStatus("mandatory")
_AccRadiusAcctRecoverTO_Type = TimeTicks
_AccRadiusAcctRecoverTO_Object = MibScalar
accRadiusAcctRecoverTO = _AccRadiusAcctRecoverTO_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 7, 3),
    _AccRadiusAcctRecoverTO_Type()
)
accRadiusAcctRecoverTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusAcctRecoverTO.setStatus("mandatory")
_AccRadiusAcctReqDiscs_Type = Counter32
_AccRadiusAcctReqDiscs_Object = MibScalar
accRadiusAcctReqDiscs = _AccRadiusAcctReqDiscs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 7, 4),
    _AccRadiusAcctReqDiscs_Type()
)
accRadiusAcctReqDiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRadiusAcctReqDiscs.setStatus("mandatory")
_AccRadiusAcctRespDiscs_Type = Counter32
_AccRadiusAcctRespDiscs_Object = MibScalar
accRadiusAcctRespDiscs = _AccRadiusAcctRespDiscs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 7, 5),
    _AccRadiusAcctRespDiscs_Type()
)
accRadiusAcctRespDiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRadiusAcctRespDiscs.setStatus("mandatory")
_AccRadiusAcctLastUser_Type = OctetString
_AccRadiusAcctLastUser_Object = MibScalar
accRadiusAcctLastUser = _AccRadiusAcctLastUser_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 7, 6),
    _AccRadiusAcctLastUser_Type()
)
accRadiusAcctLastUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRadiusAcctLastUser.setStatus("mandatory")


class _AccRadiusAcctLastType_Type(Integer32):
    """Custom type accRadiusAcctLastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acct-request", 1),
          ("acct-response", 2))
    )


_AccRadiusAcctLastType_Type.__name__ = "Integer32"
_AccRadiusAcctLastType_Object = MibScalar
accRadiusAcctLastType = _AccRadiusAcctLastType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 7, 7),
    _AccRadiusAcctLastType_Type()
)
accRadiusAcctLastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRadiusAcctLastType.setStatus("mandatory")
_AccRadiusDebugMask_Type = Integer32
_AccRadiusDebugMask_Object = MibScalar
accRadiusDebugMask = _AccRadiusDebugMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 8),
    _AccRadiusDebugMask_Type()
)
accRadiusDebugMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusDebugMask.setStatus("mandatory")
_AccRadiusGroupRangeStart_Type = Integer32
_AccRadiusGroupRangeStart_Object = MibScalar
accRadiusGroupRangeStart = _AccRadiusGroupRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 9),
    _AccRadiusGroupRangeStart_Type()
)
accRadiusGroupRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusGroupRangeStart.setStatus("mandatory")
_AccRadiusGroupRangeEnd_Type = Integer32
_AccRadiusGroupRangeEnd_Object = MibScalar
accRadiusGroupRangeEnd = _AccRadiusGroupRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 10),
    _AccRadiusGroupRangeEnd_Type()
)
accRadiusGroupRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusGroupRangeEnd.setStatus("mandatory")
_AccRadiusNASIpAddress_Type = IpAddress
_AccRadiusNASIpAddress_Object = MibScalar
accRadiusNASIpAddress = _AccRadiusNASIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 11),
    _AccRadiusNASIpAddress_Type()
)
accRadiusNASIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRadiusNASIpAddress.setStatus("mandatory")
_AccRadiusTraps_ObjectIdentity = ObjectIdentity
accRadiusTraps = _AccRadiusTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 12)
)
_AccRadiusTrapMsg_Type = Integer32
_AccRadiusTrapMsg_Object = MibScalar
accRadiusTrapMsg = _AccRadiusTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 12, 1),
    _AccRadiusTrapMsg_Type()
)
accRadiusTrapMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRadiusTrapMsg.setStatus("mandatory")

# Managed Objects groups


# Notification objects

accRadiusServerDnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 12, 0, 1)
)
accRadiusServerDnTrap.setObjects(
      *(("ACC-RADIUS", "accRadiusTrapMsg"),
        ("ACC-RADIUS", "accRadiusAuthServAddr"),
        ("ACC-RADIUS", "accRadiusAuthServOpState"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRadiusServerDnTrap.setStatus(
        ""
    )

accRadiusUsrNameTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 12, 0, 2)
)
accRadiusUsrNameTrap.setObjects(
      *(("ACC-RADIUS", "accRadiusTrapMsg"),
        ("ACC-RADIUS", "accRadiusAuthLastUser"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRadiusUsrNameTrap.setStatus(
        ""
    )

accRadiusInOpportuneEvntTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 12, 0, 3)
)
accRadiusInOpportuneEvntTrap.setObjects(
      *(("ACC-RADIUS", "accRadiusTrapMsg"),
        ("ACC-RADIUS", "accRadiusNASIdentifier"),
        ("ACC-RADIUS", "accRadiusAuthServRetryCnts"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRadiusInOpportuneEvntTrap.setStatus(
        ""
    )

accRadiusEvntCfgAddNakTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 12, 0, 4)
)
accRadiusEvntCfgAddNakTrap.setObjects(
      *(("ACC-RADIUS", "accRadiusTrapMsg"),
        ("ACC-RADIUS", "accRadiusAuthConfigErrs"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRadiusEvntCfgAddNakTrap.setStatus(
        ""
    )

accRadiusEvntMutexAttribTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 12, 0, 5)
)
accRadiusEvntMutexAttribTrap.setObjects(
      *(("ACC-RADIUS", "accRadiusTrapMsg"),
        ("ACC-RADIUS", "accRadiusAuthConfigErrs"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRadiusEvntMutexAttribTrap.setStatus(
        ""
    )

accRadiusEvntReqTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 12, 0, 6)
)
accRadiusEvntReqTrap.setObjects(
      *(("ACC-RADIUS", "accRadiusTrapMsg"),
        ("ACC-RADIUS", "accRadiusAuthConfigErrs"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRadiusEvntReqTrap.setStatus(
        ""
    )

accRadiusEvntSPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 12, 0, 7)
)
accRadiusEvntSPTrap.setObjects(
      *(("ACC-RADIUS", "accRadiusTrapMsg"),
        ("ACC-RADIUS", "accRadiusAuthConfigErrs"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRadiusEvntSPTrap.setStatus(
        ""
    )

accRadiusEvntCfgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 12, 0, 8)
)
accRadiusEvntCfgTrap.setObjects(
      *(("ACC-RADIUS", "accRadiusTrapMsg"),
        ("ACC-RADIUS", "accRadiusAuthConfigErrs"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRadiusEvntCfgTrap.setStatus(
        ""
    )

accRadiusEvntAttribTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 12, 0, 9)
)
accRadiusEvntAttribTrap.setObjects(
      *(("ACC-RADIUS", "accRadiusTrapMsg"),
        ("ACC-RADIUS", "accRadiusAuthConfigErrs"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRadiusEvntAttribTrap.setStatus(
        ""
    )

accRadiusRedundantReqTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 12, 0, 10)
)
accRadiusRedundantReqTrap.setObjects(
      *(("ACC-RADIUS", "accRadiusTrapMsg"),
        ("ACC-RADIUS", "accRadiusAuthLastUser"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRadiusRedundantReqTrap.setStatus(
        ""
    )

accRadiusBindApTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 12, 0, 11)
)
accRadiusBindApTrap.setObjects(
      *(("ACC-RADIUS", "accRadiusTrapMsg"),
        ("ACC-RADIUS", "accRadiusAuthLastUser"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRadiusBindApTrap.setStatus(
        ""
    )

accRadiusAllocUsrSessionBlkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 12, 0, 12)
)
accRadiusAllocUsrSessionBlkTrap.setObjects(
      *(("ACC-RADIUS", "accRadiusTrapMsg"),
        ("ACC-RADIUS", "accRadiusAuthLastUser"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRadiusAllocUsrSessionBlkTrap.setStatus(
        ""
    )

accRadiusPktUnknwnServTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 12, 0, 13)
)
accRadiusPktUnknwnServTrap.setObjects(
      *(("ACC-RADIUS", "accRadiusTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRadiusPktUnknwnServTrap.setStatus(
        ""
    )

accRadiusUDPBindFaildTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 12, 0, 14)
)
accRadiusUDPBindFaildTrap.setObjects(
      *(("ACC-RADIUS", "accRadiusTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRadiusUDPBindFaildTrap.setStatus(
        ""
    )

accRadiusAccPartnBindTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 12, 0, 15)
)
accRadiusAccPartnBindTrap.setObjects(
      *(("ACC-RADIUS", "accRadiusTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRadiusAccPartnBindTrap.setStatus(
        ""
    )

accRadiusInvldLenAttrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 12, 0, 16)
)
accRadiusInvldLenAttrTrap.setObjects(
      *(("ACC-RADIUS", "accRadiusTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRadiusInvldLenAttrTrap.setStatus(
        ""
    )

accRadiusInvldLenHdrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 12, 0, 17)
)
accRadiusInvldLenHdrTrap.setObjects(
      *(("ACC-RADIUS", "accRadiusTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRadiusInvldLenHdrTrap.setStatus(
        ""
    )

accRadiusInvldAccChallPaktTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 12, 0, 18)
)
accRadiusInvldAccChallPaktTrap.setObjects(
      *(("ACC-RADIUS", "accRadiusTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRadiusInvldAccChallPaktTrap.setStatus(
        ""
    )

accRadiusNoChalMsgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 12, 0, 19)
)
accRadiusNoChalMsgTrap.setObjects(
      *(("ACC-RADIUS", "accRadiusTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRadiusNoChalMsgTrap.setStatus(
        ""
    )

accRadiusInvldAuthActResTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 12, 0, 20)
)
accRadiusInvldAuthActResTrap.setObjects(
      *(("ACC-RADIUS", "accRadiusTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRadiusInvldAuthActResTrap.setStatus(
        ""
    )

accRadiusInvldAuthAccResTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 44, 12, 0, 21)
)
accRadiusInvldAuthAccResTrap.setObjects(
      *(("ACC-RADIUS", "accRadiusTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRadiusInvldAuthAccResTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-RADIUS",
    **{"accRadius": accRadius,
       "accRadiusNASIdentifier": accRadiusNASIdentifier,
       "accRadiusInvAttribAction": accRadiusInvAttribAction,
       "accRadiusMaxPort": accRadiusMaxPort,
       "accRadiusPortRangeStart": accRadiusPortRangeStart,
       "accRadiusPortRangeEnd": accRadiusPortRangeEnd,
       "accRadiusAuth": accRadiusAuth,
       "accRadiusAuthServTable": accRadiusAuthServTable,
       "accRadiusAuthServEntry": accRadiusAuthServEntry,
       "accRadiusAuthServIndex": accRadiusAuthServIndex,
       "accRadiusAuthServAdState": accRadiusAuthServAdState,
       "accRadiusAuthServAddr": accRadiusAuthServAddr,
       "accRadiusAuthServPassword": accRadiusAuthServPassword,
       "accRadiusAuthServRetryInt": accRadiusAuthServRetryInt,
       "accRadiusAuthServRetryCnts": accRadiusAuthServRetryCnts,
       "accRadiusAuthServUDPPort": accRadiusAuthServUDPPort,
       "accRadiusAuthServOpState": accRadiusAuthServOpState,
       "accRadiusAuthServReqCnts": accRadiusAuthServReqCnts,
       "accRadiusAuthServAccCnts": accRadiusAuthServAccCnts,
       "accRadiusAuthServRejCnts": accRadiusAuthServRejCnts,
       "accRadiusAuthServAccessPart": accRadiusAuthServAccessPart,
       "accRadiusAuthServSecure": accRadiusAuthServSecure,
       "accRadiusAuthMsgLvl": accRadiusAuthMsgLvl,
       "accRadiusAuthRecoverTO": accRadiusAuthRecoverTO,
       "accRadiusAuthReqDiscs": accRadiusAuthReqDiscs,
       "accRadiusAuthRespDiscs": accRadiusAuthRespDiscs,
       "accRadiusAuthLastUser": accRadiusAuthLastUser,
       "accRadiusAuthLastType": accRadiusAuthLastType,
       "accRadiusAuthCallsRejs": accRadiusAuthCallsRejs,
       "accRadiusAuthConfigErrs": accRadiusAuthConfigErrs,
       "accRadiusAuthDebugTable": accRadiusAuthDebugTable,
       "accRadiusAuthDebugEntry": accRadiusAuthDebugEntry,
       "accRadiusAuthDebugName": accRadiusAuthDebugName,
       "accRadiusAuthDebugMask": accRadiusAuthDebugMask,
       "accRadiusAcct": accRadiusAcct,
       "accRadiusAcctServTable": accRadiusAcctServTable,
       "accRadiusAcctServEntry": accRadiusAcctServEntry,
       "accRadiusAcctServIndex": accRadiusAcctServIndex,
       "accRadiusAcctServAdState": accRadiusAcctServAdState,
       "accRadiusAcctServAddr": accRadiusAcctServAddr,
       "accRadiusAcctServPassword": accRadiusAcctServPassword,
       "accRadiusAcctServRetryInt": accRadiusAcctServRetryInt,
       "accRadiusAcctServRetryCnts": accRadiusAcctServRetryCnts,
       "accRadiusAcctServUDPPort": accRadiusAcctServUDPPort,
       "accRadiusAcctServOpState": accRadiusAcctServOpState,
       "accRadiusAcctServReqCnts": accRadiusAcctServReqCnts,
       "accRadiusAcctServAccCnts": accRadiusAcctServAccCnts,
       "accRadiusAcctServAccessPart": accRadiusAcctServAccessPart,
       "accRadiusAcctServIBCAttrSupp": accRadiusAcctServIBCAttrSupp,
       "accRadiusAcctMsgLvl": accRadiusAcctMsgLvl,
       "accRadiusAcctRecoverTO": accRadiusAcctRecoverTO,
       "accRadiusAcctReqDiscs": accRadiusAcctReqDiscs,
       "accRadiusAcctRespDiscs": accRadiusAcctRespDiscs,
       "accRadiusAcctLastUser": accRadiusAcctLastUser,
       "accRadiusAcctLastType": accRadiusAcctLastType,
       "accRadiusDebugMask": accRadiusDebugMask,
       "accRadiusGroupRangeStart": accRadiusGroupRangeStart,
       "accRadiusGroupRangeEnd": accRadiusGroupRangeEnd,
       "accRadiusNASIpAddress": accRadiusNASIpAddress,
       "accRadiusTraps": accRadiusTraps,
       "accRadiusServerDnTrap": accRadiusServerDnTrap,
       "accRadiusUsrNameTrap": accRadiusUsrNameTrap,
       "accRadiusInOpportuneEvntTrap": accRadiusInOpportuneEvntTrap,
       "accRadiusEvntCfgAddNakTrap": accRadiusEvntCfgAddNakTrap,
       "accRadiusEvntMutexAttribTrap": accRadiusEvntMutexAttribTrap,
       "accRadiusEvntReqTrap": accRadiusEvntReqTrap,
       "accRadiusEvntSPTrap": accRadiusEvntSPTrap,
       "accRadiusEvntCfgTrap": accRadiusEvntCfgTrap,
       "accRadiusEvntAttribTrap": accRadiusEvntAttribTrap,
       "accRadiusRedundantReqTrap": accRadiusRedundantReqTrap,
       "accRadiusBindApTrap": accRadiusBindApTrap,
       "accRadiusAllocUsrSessionBlkTrap": accRadiusAllocUsrSessionBlkTrap,
       "accRadiusPktUnknwnServTrap": accRadiusPktUnknwnServTrap,
       "accRadiusUDPBindFaildTrap": accRadiusUDPBindFaildTrap,
       "accRadiusAccPartnBindTrap": accRadiusAccPartnBindTrap,
       "accRadiusInvldLenAttrTrap": accRadiusInvldLenAttrTrap,
       "accRadiusInvldLenHdrTrap": accRadiusInvldLenHdrTrap,
       "accRadiusInvldAccChallPaktTrap": accRadiusInvldAccChallPaktTrap,
       "accRadiusNoChalMsgTrap": accRadiusNoChalMsgTrap,
       "accRadiusInvldAuthActResTrap": accRadiusInvldAuthActResTrap,
       "accRadiusInvldAuthAccResTrap": accRadiusInvldAuthAccResTrap,
       "accRadiusTrapMsg": accRadiusTrapMsg}
)
