# SNMP MIB module (CISCO-VISM-SESSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VISM-SESSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:56 2024
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

(voice,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "voice")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoVismSessionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 95)
)
ciscoVismSessionMIB.setRevisions(
        ("2004-02-26 00:00",
         "2003-07-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VismSessionGrp_ObjectIdentity = ObjectIdentity
vismSessionGrp = _VismSessionGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11)
)
_VismSessionSetTable_Object = MibTable
vismSessionSetTable = _VismSessionSetTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 1)
)
if mibBuilder.loadTexts:
    vismSessionSetTable.setStatus("current")
_VismSessionSetEntry_Object = MibTableRow
vismSessionSetEntry = _VismSessionSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 1, 1)
)
vismSessionSetEntry.setIndexNames(
    (0, "CISCO-VISM-SESSION-MIB", "vismSessionSetNum"),
)
if mibBuilder.loadTexts:
    vismSessionSetEntry.setStatus("current")


class _VismSessionSetNum_Type(Integer32):
    """Custom type vismSessionSetNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VismSessionSetNum_Type.__name__ = "Integer32"
_VismSessionSetNum_Object = MibTableColumn
vismSessionSetNum = _VismSessionSetNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 1, 1, 1),
    _VismSessionSetNum_Type()
)
vismSessionSetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSessionSetNum.setStatus("current")


class _VismSessionSetRowStatus_Type(Integer32):
    """Custom type vismSessionSetRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_VismSessionSetRowStatus_Type.__name__ = "Integer32"
_VismSessionSetRowStatus_Object = MibTableColumn
vismSessionSetRowStatus = _VismSessionSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 1, 1, 2),
    _VismSessionSetRowStatus_Type()
)
vismSessionSetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismSessionSetRowStatus.setStatus("current")


class _VismSessionSetState_Type(Integer32):
    """Custom type vismSessionSetState based on Integer32"""
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
        *(("activeIs", 3),
          ("fullIs", 5),
          ("idle", 1),
          ("oos", 2),
          ("standbyIs", 4),
          ("unknown", 6))
    )


_VismSessionSetState_Type.__name__ = "Integer32"
_VismSessionSetState_Object = MibTableColumn
vismSessionSetState = _VismSessionSetState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 1, 1, 3),
    _VismSessionSetState_Type()
)
vismSessionSetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSessionSetState.setStatus("current")


class _VismSessionSetTotalGrps_Type(Integer32):
    """Custom type vismSessionSetTotalGrps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismSessionSetTotalGrps_Type.__name__ = "Integer32"
_VismSessionSetTotalGrps_Object = MibTableColumn
vismSessionSetTotalGrps = _VismSessionSetTotalGrps_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 1, 1, 4),
    _VismSessionSetTotalGrps_Type()
)
vismSessionSetTotalGrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSessionSetTotalGrps.setStatus("current")


class _VismSessionSetActiveGrp_Type(Integer32):
    """Custom type vismSessionSetActiveGrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismSessionSetActiveGrp_Type.__name__ = "Integer32"
_VismSessionSetActiveGrp_Object = MibTableColumn
vismSessionSetActiveGrp = _VismSessionSetActiveGrp_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 1, 1, 5),
    _VismSessionSetActiveGrp_Type()
)
vismSessionSetActiveGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSessionSetActiveGrp.setStatus("current")
_VismSessionSetSwitchFails_Type = Counter32
_VismSessionSetSwitchFails_Object = MibTableColumn
vismSessionSetSwitchFails = _VismSessionSetSwitchFails_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 1, 1, 6),
    _VismSessionSetSwitchFails_Type()
)
vismSessionSetSwitchFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSessionSetSwitchFails.setStatus("current")
_VismSessionSetSwitchSuccesses_Type = Counter32
_VismSessionSetSwitchSuccesses_Object = MibTableColumn
vismSessionSetSwitchSuccesses = _VismSessionSetSwitchSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 1, 1, 7),
    _VismSessionSetSwitchSuccesses_Type()
)
vismSessionSetSwitchSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSessionSetSwitchSuccesses.setStatus("current")
_VismSessionSetFaultTolerant_Type = TruthValue
_VismSessionSetFaultTolerant_Object = MibTableColumn
vismSessionSetFaultTolerant = _VismSessionSetFaultTolerant_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 1, 1, 8),
    _VismSessionSetFaultTolerant_Type()
)
vismSessionSetFaultTolerant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismSessionSetFaultTolerant.setStatus("current")
_VismSessionGrpTable_Object = MibTable
vismSessionGrpTable = _VismSessionGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 2)
)
if mibBuilder.loadTexts:
    vismSessionGrpTable.setStatus("current")
_VismSessionGrpEntry_Object = MibTableRow
vismSessionGrpEntry = _VismSessionGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 2, 1)
)
vismSessionGrpEntry.setIndexNames(
    (0, "CISCO-VISM-SESSION-MIB", "vismSessionGrpNum"),
)
if mibBuilder.loadTexts:
    vismSessionGrpEntry.setStatus("current")


class _VismSessionGrpNum_Type(Integer32):
    """Custom type vismSessionGrpNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VismSessionGrpNum_Type.__name__ = "Integer32"
_VismSessionGrpNum_Object = MibTableColumn
vismSessionGrpNum = _VismSessionGrpNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 2, 1, 1),
    _VismSessionGrpNum_Type()
)
vismSessionGrpNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSessionGrpNum.setStatus("current")


class _VismSessionGrpSetNum_Type(Integer32):
    """Custom type vismSessionGrpSetNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismSessionGrpSetNum_Type.__name__ = "Integer32"
_VismSessionGrpSetNum_Object = MibTableColumn
vismSessionGrpSetNum = _VismSessionGrpSetNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 2, 1, 2),
    _VismSessionGrpSetNum_Type()
)
vismSessionGrpSetNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismSessionGrpSetNum.setStatus("current")


class _VismSessionGrpRowStatus_Type(Integer32):
    """Custom type vismSessionGrpRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_VismSessionGrpRowStatus_Type.__name__ = "Integer32"
_VismSessionGrpRowStatus_Object = MibTableColumn
vismSessionGrpRowStatus = _VismSessionGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 2, 1, 3),
    _VismSessionGrpRowStatus_Type()
)
vismSessionGrpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismSessionGrpRowStatus.setStatus("current")


class _VismSessionGrpState_Type(Integer32):
    """Custom type vismSessionGrpState based on Integer32"""
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
        *(("idle", 1),
          ("is", 3),
          ("oos", 2),
          ("unknown", 4))
    )


_VismSessionGrpState_Type.__name__ = "Integer32"
_VismSessionGrpState_Object = MibTableColumn
vismSessionGrpState = _VismSessionGrpState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 2, 1, 4),
    _VismSessionGrpState_Type()
)
vismSessionGrpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSessionGrpState.setStatus("current")


class _VismSessionGrpCurrSession_Type(Integer32):
    """Custom type vismSessionGrpCurrSession based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismSessionGrpCurrSession_Type.__name__ = "Integer32"
_VismSessionGrpCurrSession_Object = MibTableColumn
vismSessionGrpCurrSession = _VismSessionGrpCurrSession_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 2, 1, 5),
    _VismSessionGrpCurrSession_Type()
)
vismSessionGrpCurrSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSessionGrpCurrSession.setStatus("current")


class _VismSessionGrpTotalSessions_Type(Integer32):
    """Custom type vismSessionGrpTotalSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismSessionGrpTotalSessions_Type.__name__ = "Integer32"
_VismSessionGrpTotalSessions_Object = MibTableColumn
vismSessionGrpTotalSessions = _VismSessionGrpTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 2, 1, 6),
    _VismSessionGrpTotalSessions_Type()
)
vismSessionGrpTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSessionGrpTotalSessions.setStatus("current")
_VismSessionGrpSwitchFails_Type = Counter32
_VismSessionGrpSwitchFails_Object = MibTableColumn
vismSessionGrpSwitchFails = _VismSessionGrpSwitchFails_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 2, 1, 7),
    _VismSessionGrpSwitchFails_Type()
)
vismSessionGrpSwitchFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSessionGrpSwitchFails.setStatus("current")
_VismSessionGrpSwitchSuccesses_Type = Counter32
_VismSessionGrpSwitchSuccesses_Object = MibTableColumn
vismSessionGrpSwitchSuccesses = _VismSessionGrpSwitchSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 2, 1, 8),
    _VismSessionGrpSwitchSuccesses_Type()
)
vismSessionGrpSwitchSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSessionGrpSwitchSuccesses.setStatus("current")


class _VismSessionGrpMgcName_Type(DisplayString):
    """Custom type vismSessionGrpMgcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_VismSessionGrpMgcName_Type.__name__ = "DisplayString"
_VismSessionGrpMgcName_Object = MibTableColumn
vismSessionGrpMgcName = _VismSessionGrpMgcName_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 2, 1, 9),
    _VismSessionGrpMgcName_Type()
)
vismSessionGrpMgcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismSessionGrpMgcName.setStatus("current")
_VismRudpSessionCnfTable_Object = MibTable
vismRudpSessionCnfTable = _VismRudpSessionCnfTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3)
)
if mibBuilder.loadTexts:
    vismRudpSessionCnfTable.setStatus("current")
_VismRudpSessionCnfEntry_Object = MibTableRow
vismRudpSessionCnfEntry = _VismRudpSessionCnfEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1)
)
vismRudpSessionCnfEntry.setIndexNames(
    (0, "CISCO-VISM-SESSION-MIB", "vismRudpSessionNum"),
)
if mibBuilder.loadTexts:
    vismRudpSessionCnfEntry.setStatus("current")


class _VismRudpSessionNum_Type(Integer32):
    """Custom type vismRudpSessionNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VismRudpSessionNum_Type.__name__ = "Integer32"
_VismRudpSessionNum_Object = MibTableColumn
vismRudpSessionNum = _VismRudpSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 1),
    _VismRudpSessionNum_Type()
)
vismRudpSessionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismRudpSessionNum.setStatus("current")


class _VismRudpSessionGrpNum_Type(Integer32):
    """Custom type vismRudpSessionGrpNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VismRudpSessionGrpNum_Type.__name__ = "Integer32"
_VismRudpSessionGrpNum_Object = MibTableColumn
vismRudpSessionGrpNum = _VismRudpSessionGrpNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 2),
    _VismRudpSessionGrpNum_Type()
)
vismRudpSessionGrpNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismRudpSessionGrpNum.setStatus("current")


class _VismRudpSessionCnfRowStatus_Type(Integer32):
    """Custom type vismRudpSessionCnfRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_VismRudpSessionCnfRowStatus_Type.__name__ = "Integer32"
_VismRudpSessionCnfRowStatus_Object = MibTableColumn
vismRudpSessionCnfRowStatus = _VismRudpSessionCnfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 3),
    _VismRudpSessionCnfRowStatus_Type()
)
vismRudpSessionCnfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismRudpSessionCnfRowStatus.setStatus("current")


class _VismRudpSessionPriority_Type(Integer32):
    """Custom type vismRudpSessionPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VismRudpSessionPriority_Type.__name__ = "Integer32"
_VismRudpSessionPriority_Object = MibTableColumn
vismRudpSessionPriority = _VismRudpSessionPriority_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 4),
    _VismRudpSessionPriority_Type()
)
vismRudpSessionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismRudpSessionPriority.setStatus("current")


class _VismRudpSessionState_Type(Integer32):
    """Custom type vismRudpSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("is", 2),
          ("oos", 1),
          ("unknown", 3))
    )


_VismRudpSessionState_Type.__name__ = "Integer32"
_VismRudpSessionState_Object = MibTableColumn
vismRudpSessionState = _VismRudpSessionState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 5),
    _VismRudpSessionState_Type()
)
vismRudpSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismRudpSessionState.setStatus("current")


class _VismRudpSessionCurrSession_Type(Integer32):
    """Custom type vismRudpSessionCurrSession based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismRudpSessionCurrSession_Type.__name__ = "Integer32"
_VismRudpSessionCurrSession_Object = MibTableColumn
vismRudpSessionCurrSession = _VismRudpSessionCurrSession_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 6),
    _VismRudpSessionCurrSession_Type()
)
vismRudpSessionCurrSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismRudpSessionCurrSession.setStatus("current")
_VismRudpSessionLocalIp_Type = IpAddress
_VismRudpSessionLocalIp_Object = MibTableColumn
vismRudpSessionLocalIp = _VismRudpSessionLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 7),
    _VismRudpSessionLocalIp_Type()
)
vismRudpSessionLocalIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismRudpSessionLocalIp.setStatus("current")


class _VismRudpSessionLocalPort_Type(Integer32):
    """Custom type vismRudpSessionLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1124, 65535),
    )


_VismRudpSessionLocalPort_Type.__name__ = "Integer32"
_VismRudpSessionLocalPort_Object = MibTableColumn
vismRudpSessionLocalPort = _VismRudpSessionLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 8),
    _VismRudpSessionLocalPort_Type()
)
vismRudpSessionLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismRudpSessionLocalPort.setStatus("current")
_VismRudpSessionRmtIp_Type = IpAddress
_VismRudpSessionRmtIp_Object = MibTableColumn
vismRudpSessionRmtIp = _VismRudpSessionRmtIp_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 9),
    _VismRudpSessionRmtIp_Type()
)
vismRudpSessionRmtIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismRudpSessionRmtIp.setStatus("current")


class _VismRudpSessionRmtPort_Type(Integer32):
    """Custom type vismRudpSessionRmtPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1124, 65535),
    )


_VismRudpSessionRmtPort_Type.__name__ = "Integer32"
_VismRudpSessionRmtPort_Object = MibTableColumn
vismRudpSessionRmtPort = _VismRudpSessionRmtPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 10),
    _VismRudpSessionRmtPort_Type()
)
vismRudpSessionRmtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismRudpSessionRmtPort.setStatus("current")


class _VismRudpSessionMaxWindow_Type(Integer32):
    """Custom type vismRudpSessionMaxWindow based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_VismRudpSessionMaxWindow_Type.__name__ = "Integer32"
_VismRudpSessionMaxWindow_Object = MibTableColumn
vismRudpSessionMaxWindow = _VismRudpSessionMaxWindow_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 11),
    _VismRudpSessionMaxWindow_Type()
)
vismRudpSessionMaxWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismRudpSessionMaxWindow.setStatus("current")


class _VismRudpSessionSyncAttempts_Type(Integer32):
    """Custom type vismRudpSessionSyncAttempts based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_VismRudpSessionSyncAttempts_Type.__name__ = "Integer32"
_VismRudpSessionSyncAttempts_Object = MibTableColumn
vismRudpSessionSyncAttempts = _VismRudpSessionSyncAttempts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 12),
    _VismRudpSessionSyncAttempts_Type()
)
vismRudpSessionSyncAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismRudpSessionSyncAttempts.setStatus("current")


class _VismRudpSessionMaxSegSize_Type(Integer32):
    """Custom type vismRudpSessionMaxSegSize based on Integer32"""
    defaultValue = 384

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 65535),
    )


_VismRudpSessionMaxSegSize_Type.__name__ = "Integer32"
_VismRudpSessionMaxSegSize_Object = MibTableColumn
vismRudpSessionMaxSegSize = _VismRudpSessionMaxSegSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 13),
    _VismRudpSessionMaxSegSize_Type()
)
vismRudpSessionMaxSegSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismRudpSessionMaxSegSize.setStatus("current")
if mibBuilder.loadTexts:
    vismRudpSessionMaxSegSize.setUnits("bytes")


class _VismRudpSessionMaxAutoReset_Type(Integer32):
    """Custom type vismRudpSessionMaxAutoReset based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VismRudpSessionMaxAutoReset_Type.__name__ = "Integer32"
_VismRudpSessionMaxAutoReset_Object = MibTableColumn
vismRudpSessionMaxAutoReset = _VismRudpSessionMaxAutoReset_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 14),
    _VismRudpSessionMaxAutoReset_Type()
)
vismRudpSessionMaxAutoReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismRudpSessionMaxAutoReset.setStatus("current")


class _VismRudpSessionRetransTmout_Type(Integer32):
    """Custom type vismRudpSessionRetransTmout based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 65535),
    )


_VismRudpSessionRetransTmout_Type.__name__ = "Integer32"
_VismRudpSessionRetransTmout_Object = MibTableColumn
vismRudpSessionRetransTmout = _VismRudpSessionRetransTmout_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 15),
    _VismRudpSessionRetransTmout_Type()
)
vismRudpSessionRetransTmout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismRudpSessionRetransTmout.setStatus("current")
if mibBuilder.loadTexts:
    vismRudpSessionRetransTmout.setUnits("milliseconds")


class _VismRudpSessionMaxRetrans_Type(Integer32):
    """Custom type vismRudpSessionMaxRetrans based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VismRudpSessionMaxRetrans_Type.__name__ = "Integer32"
_VismRudpSessionMaxRetrans_Object = MibTableColumn
vismRudpSessionMaxRetrans = _VismRudpSessionMaxRetrans_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 16),
    _VismRudpSessionMaxRetrans_Type()
)
vismRudpSessionMaxRetrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismRudpSessionMaxRetrans.setStatus("current")


class _VismRudpSessionMaxCumAck_Type(Integer32):
    """Custom type vismRudpSessionMaxCumAck based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VismRudpSessionMaxCumAck_Type.__name__ = "Integer32"
_VismRudpSessionMaxCumAck_Object = MibTableColumn
vismRudpSessionMaxCumAck = _VismRudpSessionMaxCumAck_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 17),
    _VismRudpSessionMaxCumAck_Type()
)
vismRudpSessionMaxCumAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismRudpSessionMaxCumAck.setStatus("current")


class _VismRudpSessionCumAckTmout_Type(Integer32):
    """Custom type vismRudpSessionCumAckTmout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 65535),
    )


_VismRudpSessionCumAckTmout_Type.__name__ = "Integer32"
_VismRudpSessionCumAckTmout_Object = MibTableColumn
vismRudpSessionCumAckTmout = _VismRudpSessionCumAckTmout_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 18),
    _VismRudpSessionCumAckTmout_Type()
)
vismRudpSessionCumAckTmout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismRudpSessionCumAckTmout.setStatus("current")


class _VismRudpSessionMaxOutOfSeq_Type(Integer32):
    """Custom type vismRudpSessionMaxOutOfSeq based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VismRudpSessionMaxOutOfSeq_Type.__name__ = "Integer32"
_VismRudpSessionMaxOutOfSeq_Object = MibTableColumn
vismRudpSessionMaxOutOfSeq = _VismRudpSessionMaxOutOfSeq_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 19),
    _VismRudpSessionMaxOutOfSeq_Type()
)
vismRudpSessionMaxOutOfSeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismRudpSessionMaxOutOfSeq.setStatus("current")


class _VismRudpSessionNullSegTmout_Type(Integer32):
    """Custom type vismRudpSessionNullSegTmout based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VismRudpSessionNullSegTmout_Type.__name__ = "Integer32"
_VismRudpSessionNullSegTmout_Object = MibTableColumn
vismRudpSessionNullSegTmout = _VismRudpSessionNullSegTmout_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 20),
    _VismRudpSessionNullSegTmout_Type()
)
vismRudpSessionNullSegTmout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismRudpSessionNullSegTmout.setStatus("current")
if mibBuilder.loadTexts:
    vismRudpSessionNullSegTmout.setUnits("milliseconds")


class _VismRudpSessionTransStateTmout_Type(Integer32):
    """Custom type vismRudpSessionTransStateTmout based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VismRudpSessionTransStateTmout_Type.__name__ = "Integer32"
_VismRudpSessionTransStateTmout_Object = MibTableColumn
vismRudpSessionTransStateTmout = _VismRudpSessionTransStateTmout_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 21),
    _VismRudpSessionTransStateTmout_Type()
)
vismRudpSessionTransStateTmout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismRudpSessionTransStateTmout.setStatus("current")


class _VismRudpSessionType_Type(Integer32):
    """Custom type vismRudpSessionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backhaul", 1),
          ("lapdTrunking", 2))
    )


_VismRudpSessionType_Type.__name__ = "Integer32"
_VismRudpSessionType_Object = MibTableColumn
vismRudpSessionType = _VismRudpSessionType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 22),
    _VismRudpSessionType_Type()
)
vismRudpSessionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismRudpSessionType.setStatus("current")
_VismRudpSessionRmtGwIp_Type = IpAddress
_VismRudpSessionRmtGwIp_Object = MibTableColumn
vismRudpSessionRmtGwIp = _VismRudpSessionRmtGwIp_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 23),
    _VismRudpSessionRmtGwIp_Type()
)
vismRudpSessionRmtGwIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismRudpSessionRmtGwIp.setStatus("current")
_VismRudpSessionStatTable_Object = MibTable
vismRudpSessionStatTable = _VismRudpSessionStatTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4)
)
if mibBuilder.loadTexts:
    vismRudpSessionStatTable.setStatus("current")
_VismRudpSessionStatEntry_Object = MibTableRow
vismRudpSessionStatEntry = _VismRudpSessionStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4, 1)
)
vismRudpSessionStatEntry.setIndexNames(
    (0, "CISCO-VISM-SESSION-MIB", "vismRudpSessionStatNum"),
)
if mibBuilder.loadTexts:
    vismRudpSessionStatEntry.setStatus("current")


class _VismRudpSessionStatNum_Type(Integer32):
    """Custom type vismRudpSessionStatNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VismRudpSessionStatNum_Type.__name__ = "Integer32"
_VismRudpSessionStatNum_Object = MibTableColumn
vismRudpSessionStatNum = _VismRudpSessionStatNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4, 1, 1),
    _VismRudpSessionStatNum_Type()
)
vismRudpSessionStatNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismRudpSessionStatNum.setStatus("current")
_VismRudpSessionAutoResets_Type = Counter32
_VismRudpSessionAutoResets_Object = MibTableColumn
vismRudpSessionAutoResets = _VismRudpSessionAutoResets_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4, 1, 2),
    _VismRudpSessionAutoResets_Type()
)
vismRudpSessionAutoResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismRudpSessionAutoResets.setStatus("current")
_VismRudpSessionRcvdAutoResets_Type = Counter32
_VismRudpSessionRcvdAutoResets_Object = MibTableColumn
vismRudpSessionRcvdAutoResets = _VismRudpSessionRcvdAutoResets_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4, 1, 3),
    _VismRudpSessionRcvdAutoResets_Type()
)
vismRudpSessionRcvdAutoResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismRudpSessionRcvdAutoResets.setStatus("current")
_VismRudpSessionRcvdInSeqs_Type = Counter32
_VismRudpSessionRcvdInSeqs_Object = MibTableColumn
vismRudpSessionRcvdInSeqs = _VismRudpSessionRcvdInSeqs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4, 1, 4),
    _VismRudpSessionRcvdInSeqs_Type()
)
vismRudpSessionRcvdInSeqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismRudpSessionRcvdInSeqs.setStatus("current")
if mibBuilder.loadTexts:
    vismRudpSessionRcvdInSeqs.setUnits("packets")
_VismRudpSessionRcvdOutSeqs_Type = Counter32
_VismRudpSessionRcvdOutSeqs_Object = MibTableColumn
vismRudpSessionRcvdOutSeqs = _VismRudpSessionRcvdOutSeqs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4, 1, 5),
    _VismRudpSessionRcvdOutSeqs_Type()
)
vismRudpSessionRcvdOutSeqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismRudpSessionRcvdOutSeqs.setStatus("current")
if mibBuilder.loadTexts:
    vismRudpSessionRcvdOutSeqs.setUnits("packets")
_VismRudpSessionSentPackets_Type = Counter32
_VismRudpSessionSentPackets_Object = MibTableColumn
vismRudpSessionSentPackets = _VismRudpSessionSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4, 1, 6),
    _VismRudpSessionSentPackets_Type()
)
vismRudpSessionSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismRudpSessionSentPackets.setStatus("current")
_VismRudpSessionRcvdPackets_Type = Counter32
_VismRudpSessionRcvdPackets_Object = MibTableColumn
vismRudpSessionRcvdPackets = _VismRudpSessionRcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4, 1, 7),
    _VismRudpSessionRcvdPackets_Type()
)
vismRudpSessionRcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismRudpSessionRcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    vismRudpSessionRcvdPackets.setUnits("packets")
_VismRudpSessionSentBytes_Type = Counter32
_VismRudpSessionSentBytes_Object = MibTableColumn
vismRudpSessionSentBytes = _VismRudpSessionSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4, 1, 8),
    _VismRudpSessionSentBytes_Type()
)
vismRudpSessionSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismRudpSessionSentBytes.setStatus("current")
_VismRudpSessionRcvdBytes_Type = Counter32
_VismRudpSessionRcvdBytes_Object = MibTableColumn
vismRudpSessionRcvdBytes = _VismRudpSessionRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4, 1, 9),
    _VismRudpSessionRcvdBytes_Type()
)
vismRudpSessionRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismRudpSessionRcvdBytes.setStatus("current")
_VismRudpSessionDataSentPkts_Type = Counter32
_VismRudpSessionDataSentPkts_Object = MibTableColumn
vismRudpSessionDataSentPkts = _VismRudpSessionDataSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4, 1, 10),
    _VismRudpSessionDataSentPkts_Type()
)
vismRudpSessionDataSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismRudpSessionDataSentPkts.setStatus("current")
_VismRudpSessionDataRcvdPkts_Type = Counter32
_VismRudpSessionDataRcvdPkts_Object = MibTableColumn
vismRudpSessionDataRcvdPkts = _VismRudpSessionDataRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4, 1, 11),
    _VismRudpSessionDataRcvdPkts_Type()
)
vismRudpSessionDataRcvdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismRudpSessionDataRcvdPkts.setStatus("current")
_VismRudpSessionDiscardPkts_Type = Counter32
_VismRudpSessionDiscardPkts_Object = MibTableColumn
vismRudpSessionDiscardPkts = _VismRudpSessionDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4, 1, 12),
    _VismRudpSessionDiscardPkts_Type()
)
vismRudpSessionDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismRudpSessionDiscardPkts.setStatus("current")
_VismRudpSessionRetransPkts_Type = Counter32
_VismRudpSessionRetransPkts_Object = MibTableColumn
vismRudpSessionRetransPkts = _VismRudpSessionRetransPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4, 1, 13),
    _VismRudpSessionRetransPkts_Type()
)
vismRudpSessionRetransPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismRudpSessionRetransPkts.setStatus("current")
_CiscoVismSessionMIBConformance_ObjectIdentity = ObjectIdentity
ciscoVismSessionMIBConformance = _CiscoVismSessionMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 95, 2)
)
_CiscoVismSessionMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVismSessionMIBGroups = _CiscoVismSessionMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 95, 2, 1)
)
_CiscoVismSessionMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVismSessionMIBCompliances = _CiscoVismSessionMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 95, 2, 2)
)

# Managed Objects groups

ciscoVismSessionSetGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 95, 2, 1, 1)
)
ciscoVismSessionSetGrp.setObjects(
      *(("CISCO-VISM-SESSION-MIB", "vismSessionSetNum"),
        ("CISCO-VISM-SESSION-MIB", "vismSessionSetRowStatus"),
        ("CISCO-VISM-SESSION-MIB", "vismSessionSetState"),
        ("CISCO-VISM-SESSION-MIB", "vismSessionSetTotalGrps"),
        ("CISCO-VISM-SESSION-MIB", "vismSessionSetActiveGrp"),
        ("CISCO-VISM-SESSION-MIB", "vismSessionSetSwitchFails"),
        ("CISCO-VISM-SESSION-MIB", "vismSessionSetSwitchSuccesses"),
        ("CISCO-VISM-SESSION-MIB", "vismSessionSetFaultTolerant"))
)
if mibBuilder.loadTexts:
    ciscoVismSessionSetGrp.setStatus("current")

ciscoVismSessionGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 95, 2, 1, 2)
)
ciscoVismSessionGrp.setObjects(
      *(("CISCO-VISM-SESSION-MIB", "vismSessionGrpNum"),
        ("CISCO-VISM-SESSION-MIB", "vismSessionGrpSetNum"),
        ("CISCO-VISM-SESSION-MIB", "vismSessionGrpRowStatus"),
        ("CISCO-VISM-SESSION-MIB", "vismSessionGrpState"),
        ("CISCO-VISM-SESSION-MIB", "vismSessionGrpCurrSession"),
        ("CISCO-VISM-SESSION-MIB", "vismSessionGrpTotalSessions"),
        ("CISCO-VISM-SESSION-MIB", "vismSessionGrpSwitchFails"),
        ("CISCO-VISM-SESSION-MIB", "vismSessionGrpSwitchSuccesses"),
        ("CISCO-VISM-SESSION-MIB", "vismSessionGrpMgcName"))
)
if mibBuilder.loadTexts:
    ciscoVismSessionGrp.setStatus("current")

ciscoVismRudpSessionGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 95, 2, 1, 3)
)
ciscoVismRudpSessionGrp.setObjects(
      *(("CISCO-VISM-SESSION-MIB", "vismRudpSessionNum"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionGrpNum"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionCnfRowStatus"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionPriority"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionState"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionCurrSession"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionLocalIp"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionLocalPort"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionRmtIp"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionRmtPort"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionMaxWindow"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionSyncAttempts"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionMaxSegSize"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionMaxAutoReset"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionRetransTmout"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionMaxRetrans"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionMaxCumAck"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionCumAckTmout"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionMaxOutOfSeq"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionNullSegTmout"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionTransStateTmout"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionType"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionRmtGwIp"))
)
if mibBuilder.loadTexts:
    ciscoVismRudpSessionGrp.setStatus("current")

ciscoVismRudpSessionStatGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 95, 2, 1, 4)
)
ciscoVismRudpSessionStatGrp.setObjects(
      *(("CISCO-VISM-SESSION-MIB", "vismRudpSessionStatNum"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionAutoResets"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionRcvdAutoResets"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionRcvdInSeqs"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionRcvdOutSeqs"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionSentPackets"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionRcvdPackets"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionSentBytes"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionRcvdBytes"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionDataSentPkts"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionDataRcvdPkts"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionDiscardPkts"),
        ("CISCO-VISM-SESSION-MIB", "vismRudpSessionRetransPkts"))
)
if mibBuilder.loadTexts:
    ciscoVismRudpSessionStatGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoVismSessionCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 95, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoVismSessionCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VISM-SESSION-MIB",
    **{"vismSessionGrp": vismSessionGrp,
       "vismSessionSetTable": vismSessionSetTable,
       "vismSessionSetEntry": vismSessionSetEntry,
       "vismSessionSetNum": vismSessionSetNum,
       "vismSessionSetRowStatus": vismSessionSetRowStatus,
       "vismSessionSetState": vismSessionSetState,
       "vismSessionSetTotalGrps": vismSessionSetTotalGrps,
       "vismSessionSetActiveGrp": vismSessionSetActiveGrp,
       "vismSessionSetSwitchFails": vismSessionSetSwitchFails,
       "vismSessionSetSwitchSuccesses": vismSessionSetSwitchSuccesses,
       "vismSessionSetFaultTolerant": vismSessionSetFaultTolerant,
       "vismSessionGrpTable": vismSessionGrpTable,
       "vismSessionGrpEntry": vismSessionGrpEntry,
       "vismSessionGrpNum": vismSessionGrpNum,
       "vismSessionGrpSetNum": vismSessionGrpSetNum,
       "vismSessionGrpRowStatus": vismSessionGrpRowStatus,
       "vismSessionGrpState": vismSessionGrpState,
       "vismSessionGrpCurrSession": vismSessionGrpCurrSession,
       "vismSessionGrpTotalSessions": vismSessionGrpTotalSessions,
       "vismSessionGrpSwitchFails": vismSessionGrpSwitchFails,
       "vismSessionGrpSwitchSuccesses": vismSessionGrpSwitchSuccesses,
       "vismSessionGrpMgcName": vismSessionGrpMgcName,
       "vismRudpSessionCnfTable": vismRudpSessionCnfTable,
       "vismRudpSessionCnfEntry": vismRudpSessionCnfEntry,
       "vismRudpSessionNum": vismRudpSessionNum,
       "vismRudpSessionGrpNum": vismRudpSessionGrpNum,
       "vismRudpSessionCnfRowStatus": vismRudpSessionCnfRowStatus,
       "vismRudpSessionPriority": vismRudpSessionPriority,
       "vismRudpSessionState": vismRudpSessionState,
       "vismRudpSessionCurrSession": vismRudpSessionCurrSession,
       "vismRudpSessionLocalIp": vismRudpSessionLocalIp,
       "vismRudpSessionLocalPort": vismRudpSessionLocalPort,
       "vismRudpSessionRmtIp": vismRudpSessionRmtIp,
       "vismRudpSessionRmtPort": vismRudpSessionRmtPort,
       "vismRudpSessionMaxWindow": vismRudpSessionMaxWindow,
       "vismRudpSessionSyncAttempts": vismRudpSessionSyncAttempts,
       "vismRudpSessionMaxSegSize": vismRudpSessionMaxSegSize,
       "vismRudpSessionMaxAutoReset": vismRudpSessionMaxAutoReset,
       "vismRudpSessionRetransTmout": vismRudpSessionRetransTmout,
       "vismRudpSessionMaxRetrans": vismRudpSessionMaxRetrans,
       "vismRudpSessionMaxCumAck": vismRudpSessionMaxCumAck,
       "vismRudpSessionCumAckTmout": vismRudpSessionCumAckTmout,
       "vismRudpSessionMaxOutOfSeq": vismRudpSessionMaxOutOfSeq,
       "vismRudpSessionNullSegTmout": vismRudpSessionNullSegTmout,
       "vismRudpSessionTransStateTmout": vismRudpSessionTransStateTmout,
       "vismRudpSessionType": vismRudpSessionType,
       "vismRudpSessionRmtGwIp": vismRudpSessionRmtGwIp,
       "vismRudpSessionStatTable": vismRudpSessionStatTable,
       "vismRudpSessionStatEntry": vismRudpSessionStatEntry,
       "vismRudpSessionStatNum": vismRudpSessionStatNum,
       "vismRudpSessionAutoResets": vismRudpSessionAutoResets,
       "vismRudpSessionRcvdAutoResets": vismRudpSessionRcvdAutoResets,
       "vismRudpSessionRcvdInSeqs": vismRudpSessionRcvdInSeqs,
       "vismRudpSessionRcvdOutSeqs": vismRudpSessionRcvdOutSeqs,
       "vismRudpSessionSentPackets": vismRudpSessionSentPackets,
       "vismRudpSessionRcvdPackets": vismRudpSessionRcvdPackets,
       "vismRudpSessionSentBytes": vismRudpSessionSentBytes,
       "vismRudpSessionRcvdBytes": vismRudpSessionRcvdBytes,
       "vismRudpSessionDataSentPkts": vismRudpSessionDataSentPkts,
       "vismRudpSessionDataRcvdPkts": vismRudpSessionDataRcvdPkts,
       "vismRudpSessionDiscardPkts": vismRudpSessionDiscardPkts,
       "vismRudpSessionRetransPkts": vismRudpSessionRetransPkts,
       "ciscoVismSessionMIB": ciscoVismSessionMIB,
       "ciscoVismSessionMIBConformance": ciscoVismSessionMIBConformance,
       "ciscoVismSessionMIBGroups": ciscoVismSessionMIBGroups,
       "ciscoVismSessionSetGrp": ciscoVismSessionSetGrp,
       "ciscoVismSessionGrp": ciscoVismSessionGrp,
       "ciscoVismRudpSessionGrp": ciscoVismRudpSessionGrp,
       "ciscoVismRudpSessionStatGrp": ciscoVismRudpSessionStatGrp,
       "ciscoVismSessionMIBCompliances": ciscoVismSessionMIBCompliances,
       "ciscoVismSessionCompliance": ciscoVismSessionCompliance}
)
