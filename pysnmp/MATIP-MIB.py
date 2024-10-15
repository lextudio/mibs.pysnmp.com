# SNMP MIB module (MATIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MATIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:32 2024
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

_Ngcan_ObjectIdentity = ObjectIdentity
ngcan = _Ngcan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978)
)
_Tiger_ObjectIdentity = ObjectIdentity
tiger = _Tiger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2)
)
_MatipMIB_ObjectIdentity = ObjectIdentity
matipMIB = _MatipMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7)
)
_MatipUser_ObjectIdentity = ObjectIdentity
matipUser = _MatipUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 2)
)


class _MatipNumUsers_Type(Integer32):
    """Custom type matipNumUsers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MatipNumUsers_Type.__name__ = "Integer32"
_MatipNumUsers_Object = MibScalar
matipNumUsers = _MatipNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 1),
    _MatipNumUsers_Type()
)
matipNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matipNumUsers.setStatus("mandatory")
_MatipUserTable_Object = MibTable
matipUserTable = _MatipUserTable_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2)
)
if mibBuilder.loadTexts:
    matipUserTable.setStatus("mandatory")
_MatipUserEntry_Object = MibTableRow
matipUserEntry = _MatipUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1)
)
matipUserEntry.setIndexNames(
    (0, "MATIP-MIB", "matipUserIndex"),
)
if mibBuilder.loadTexts:
    matipUserEntry.setStatus("mandatory")


class _MatipUserIndex_Type(Integer32):
    """Custom type matipUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MatipUserIndex_Type.__name__ = "Integer32"
_MatipUserIndex_Object = MibTableColumn
matipUserIndex = _MatipUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 1),
    _MatipUserIndex_Type()
)
matipUserIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matipUserIndex.setStatus("mandatory")


class _MatipUserHLD_Type(Integer32):
    """Custom type matipUserHLD based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MatipUserHLD_Type.__name__ = "Integer32"
_MatipUserHLD_Object = MibTableColumn
matipUserHLD = _MatipUserHLD_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 2),
    _MatipUserHLD_Type()
)
matipUserHLD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matipUserHLD.setStatus("mandatory")


class _MatipUserA1_Type(Integer32):
    """Custom type matipUserA1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MatipUserA1_Type.__name__ = "Integer32"
_MatipUserA1_Object = MibTableColumn
matipUserA1 = _MatipUserA1_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 3),
    _MatipUserA1_Type()
)
matipUserA1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matipUserA1.setStatus("mandatory")


class _MatipUserA2_Type(Integer32):
    """Custom type matipUserA2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MatipUserA2_Type.__name__ = "Integer32"
_MatipUserA2_Object = MibTableColumn
matipUserA2 = _MatipUserA2_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 4),
    _MatipUserA2_Type()
)
matipUserA2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matipUserA2.setStatus("mandatory")


class _MatipUserSessionRef_Type(Integer32):
    """Custom type matipUserSessionRef based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MatipUserSessionRef_Type.__name__ = "Integer32"
_MatipUserSessionRef_Object = MibTableColumn
matipUserSessionRef = _MatipUserSessionRef_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 5),
    _MatipUserSessionRef_Type()
)
matipUserSessionRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matipUserSessionRef.setStatus("mandatory")


class _MatipUserCoding_Type(Integer32):
    """Custom type matipUserCoding based on Integer32"""
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
        *(("ascii", 3),
          ("ebcdic", 4),
          ("ipars", 2),
          ("paddedbaudot", 1))
    )


_MatipUserCoding_Type.__name__ = "Integer32"
_MatipUserCoding_Object = MibTableColumn
matipUserCoding = _MatipUserCoding_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 6),
    _MatipUserCoding_Type()
)
matipUserCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matipUserCoding.setStatus("mandatory")


class _MatipUserPresentationMode_Type(Integer32):
    """Custom type matipUserPresentationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("p1024b", 1),
          ("p1024c", 2),
          ("sna3270", 3))
    )


_MatipUserPresentationMode_Type.__name__ = "Integer32"
_MatipUserPresentationMode_Object = MibTableColumn
matipUserPresentationMode = _MatipUserPresentationMode_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 7),
    _MatipUserPresentationMode_Type()
)
matipUserPresentationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matipUserPresentationMode.setStatus("mandatory")


class _MatipUserQueueThresholdHi_Type(Integer32):
    """Custom type matipUserQueueThresholdHi based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MatipUserQueueThresholdHi_Type.__name__ = "Integer32"
_MatipUserQueueThresholdHi_Object = MibTableColumn
matipUserQueueThresholdHi = _MatipUserQueueThresholdHi_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 8),
    _MatipUserQueueThresholdHi_Type()
)
matipUserQueueThresholdHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matipUserQueueThresholdHi.setStatus("mandatory")


class _MatipUserQueueThresholdLow_Type(Integer32):
    """Custom type matipUserQueueThresholdLow based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MatipUserQueueThresholdLow_Type.__name__ = "Integer32"
_MatipUserQueueThresholdLow_Object = MibTableColumn
matipUserQueueThresholdLow = _MatipUserQueueThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 9),
    _MatipUserQueueThresholdLow_Type()
)
matipUserQueueThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matipUserQueueThresholdLow.setStatus("mandatory")
_MatipUserStateTime_Type = TimeTicks
_MatipUserStateTime_Object = MibTableColumn
matipUserStateTime = _MatipUserStateTime_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 10),
    _MatipUserStateTime_Type()
)
matipUserStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matipUserStateTime.setStatus("mandatory")


class _MatipUserStatus_Type(Integer32):
    """Custom type matipUserStatus based on Integer32"""
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
        *(("activated", 2),
          ("bound", 3),
          ("closed", 1),
          ("connected", 4))
    )


_MatipUserStatus_Type.__name__ = "Integer32"
_MatipUserStatus_Object = MibTableColumn
matipUserStatus = _MatipUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 11),
    _MatipUserStatus_Type()
)
matipUserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matipUserStatus.setStatus("mandatory")
_MatipUserMsgsIn_Type = Counter32
_MatipUserMsgsIn_Object = MibTableColumn
matipUserMsgsIn = _MatipUserMsgsIn_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 12),
    _MatipUserMsgsIn_Type()
)
matipUserMsgsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matipUserMsgsIn.setStatus("mandatory")
_MatipUserMsgsOut_Type = Counter32
_MatipUserMsgsOut_Object = MibTableColumn
matipUserMsgsOut = _MatipUserMsgsOut_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 13),
    _MatipUserMsgsOut_Type()
)
matipUserMsgsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matipUserMsgsOut.setStatus("mandatory")
_MatipUserCharIn_Type = Counter32
_MatipUserCharIn_Object = MibTableColumn
matipUserCharIn = _MatipUserCharIn_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 14),
    _MatipUserCharIn_Type()
)
matipUserCharIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matipUserCharIn.setStatus("mandatory")
_MatipUserCharOut_Type = Counter32
_MatipUserCharOut_Object = MibTableColumn
matipUserCharOut = _MatipUserCharOut_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 15),
    _MatipUserCharOut_Type()
)
matipUserCharOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matipUserCharOut.setStatus("mandatory")
_MatipUserDisconnects_Type = Counter32
_MatipUserDisconnects_Object = MibTableColumn
matipUserDisconnects = _MatipUserDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 16),
    _MatipUserDisconnects_Type()
)
matipUserDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matipUserDisconnects.setStatus("mandatory")


class _MatipUserTrapReason_Type(Integer32):
    """Custom type matipUserTrapReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("none", 1),
          ("up", 2))
    )


_MatipUserTrapReason_Type.__name__ = "Integer32"
_MatipUserTrapReason_Object = MibTableColumn
matipUserTrapReason = _MatipUserTrapReason_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 17),
    _MatipUserTrapReason_Type()
)
matipUserTrapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matipUserTrapReason.setStatus("mandatory")


class _MatipUserStateChangeTrapEnable_Type(Integer32):
    """Custom type matipUserStateChangeTrapEnable based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 2),
          ("partial", 3))
    )


_MatipUserStateChangeTrapEnable_Type.__name__ = "Integer32"
_MatipUserStateChangeTrapEnable_Object = MibTableColumn
matipUserStateChangeTrapEnable = _MatipUserStateChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 2, 2, 1, 18),
    _MatipUserStateChangeTrapEnable_Type()
)
matipUserStateChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matipUserStateChangeTrapEnable.setStatus("mandatory")
_MatipSession_ObjectIdentity = ObjectIdentity
matipSession = _MatipSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 3)
)
_MatipSessionTable_Object = MibTable
matipSessionTable = _MatipSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3)
)
if mibBuilder.loadTexts:
    matipSessionTable.setStatus("mandatory")
_MatipSessionEntry_Object = MibTableRow
matipSessionEntry = _MatipSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1)
)
matipSessionEntry.setIndexNames(
    (0, "MATIP-MIB", "matipSessionIndex"),
)
if mibBuilder.loadTexts:
    matipSessionEntry.setStatus("mandatory")


class _MatipSessionIndex_Type(Integer32):
    """Custom type matipSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MatipSessionIndex_Type.__name__ = "Integer32"
_MatipSessionIndex_Object = MibTableColumn
matipSessionIndex = _MatipSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 1),
    _MatipSessionIndex_Type()
)
matipSessionIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matipSessionIndex.setStatus("mandatory")


class _MatipSessionClientServer_Type(Integer32):
    """Custom type matipSessionClientServer based on Integer32"""
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
        *(("both", 3),
          ("client", 1),
          ("server", 2))
    )


_MatipSessionClientServer_Type.__name__ = "Integer32"
_MatipSessionClientServer_Object = MibTableColumn
matipSessionClientServer = _MatipSessionClientServer_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 2),
    _MatipSessionClientServer_Type()
)
matipSessionClientServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matipSessionClientServer.setStatus("mandatory")


class _MatipSessionMuxMode_Type(Integer32):
    """Custom type matipSessionMuxMode based on Integer32"""
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
        *(("a1a2", 2),
          ("hlda1a2", 1),
          ("single", 3))
    )


_MatipSessionMuxMode_Type.__name__ = "Integer32"
_MatipSessionMuxMode_Object = MibTableColumn
matipSessionMuxMode = _MatipSessionMuxMode_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 3),
    _MatipSessionMuxMode_Type()
)
matipSessionMuxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matipSessionMuxMode.setStatus("mandatory")


class _MatipSessionPresentationMode_Type(Integer32):
    """Custom type matipSessionPresentationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("p1024b", 1),
          ("p1024c", 2),
          ("sna3270", 3))
    )


_MatipSessionPresentationMode_Type.__name__ = "Integer32"
_MatipSessionPresentationMode_Object = MibTableColumn
matipSessionPresentationMode = _MatipSessionPresentationMode_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 4),
    _MatipSessionPresentationMode_Type()
)
matipSessionPresentationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matipSessionPresentationMode.setStatus("mandatory")


class _MatipSessionCoding_Type(Integer32):
    """Custom type matipSessionCoding based on Integer32"""
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
        *(("ascii", 3),
          ("ebcdic", 4),
          ("ipars", 2),
          ("paddedbaudot", 1))
    )


_MatipSessionCoding_Type.__name__ = "Integer32"
_MatipSessionCoding_Object = MibTableColumn
matipSessionCoding = _MatipSessionCoding_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 5),
    _MatipSessionCoding_Type()
)
matipSessionCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matipSessionCoding.setStatus("mandatory")


class _MatipSessionRestartTimer_Type(Integer32):
    """Custom type matipSessionRestartTimer based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MatipSessionRestartTimer_Type.__name__ = "Integer32"
_MatipSessionRestartTimer_Object = MibTableColumn
matipSessionRestartTimer = _MatipSessionRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 6),
    _MatipSessionRestartTimer_Type()
)
matipSessionRestartTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matipSessionRestartTimer.setStatus("mandatory")


class _MatipSessionDialOnDemand_Type(Integer32):
    """Custom type matipSessionDialOnDemand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MatipSessionDialOnDemand_Type.__name__ = "Integer32"
_MatipSessionDialOnDemand_Object = MibTableColumn
matipSessionDialOnDemand = _MatipSessionDialOnDemand_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 7),
    _MatipSessionDialOnDemand_Type()
)
matipSessionDialOnDemand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matipSessionDialOnDemand.setStatus("mandatory")


class _MatipSessionActivityTimer_Type(Integer32):
    """Custom type matipSessionActivityTimer based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_MatipSessionActivityTimer_Type.__name__ = "Integer32"
_MatipSessionActivityTimer_Object = MibTableColumn
matipSessionActivityTimer = _MatipSessionActivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 8),
    _MatipSessionActivityTimer_Type()
)
matipSessionActivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matipSessionActivityTimer.setStatus("mandatory")


class _MatipSessionQueueThresholdHi_Type(Integer32):
    """Custom type matipSessionQueueThresholdHi based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MatipSessionQueueThresholdHi_Type.__name__ = "Integer32"
_MatipSessionQueueThresholdHi_Object = MibTableColumn
matipSessionQueueThresholdHi = _MatipSessionQueueThresholdHi_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 9),
    _MatipSessionQueueThresholdHi_Type()
)
matipSessionQueueThresholdHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matipSessionQueueThresholdHi.setStatus("mandatory")


class _MatipSessionQueueThresholdLow_Type(Integer32):
    """Custom type matipSessionQueueThresholdLow based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MatipSessionQueueThresholdLow_Type.__name__ = "Integer32"
_MatipSessionQueueThresholdLow_Object = MibTableColumn
matipSessionQueueThresholdLow = _MatipSessionQueueThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 10),
    _MatipSessionQueueThresholdLow_Type()
)
matipSessionQueueThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matipSessionQueueThresholdLow.setStatus("mandatory")
_MatipSessionConnectTime_Type = TimeTicks
_MatipSessionConnectTime_Object = MibTableColumn
matipSessionConnectTime = _MatipSessionConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 11),
    _MatipSessionConnectTime_Type()
)
matipSessionConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matipSessionConnectTime.setStatus("mandatory")


class _MatipSessionStatus_Type(Integer32):
    """Custom type matipSessionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sessionActivated", 2),
          ("sessionConnected", 3),
          ("sessionDown", 1))
    )


_MatipSessionStatus_Type.__name__ = "Integer32"
_MatipSessionStatus_Object = MibTableColumn
matipSessionStatus = _MatipSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 12),
    _MatipSessionStatus_Type()
)
matipSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matipSessionStatus.setStatus("mandatory")
_MatipSessionDisconnects_Type = Counter32
_MatipSessionDisconnects_Object = MibTableColumn
matipSessionDisconnects = _MatipSessionDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 13),
    _MatipSessionDisconnects_Type()
)
matipSessionDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matipSessionDisconnects.setStatus("mandatory")
_MatipSessionSOSent_Type = Counter32
_MatipSessionSOSent_Object = MibTableColumn
matipSessionSOSent = _MatipSessionSOSent_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 14),
    _MatipSessionSOSent_Type()
)
matipSessionSOSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matipSessionSOSent.setStatus("mandatory")
_MatipSessionSOReceived_Type = Counter32
_MatipSessionSOReceived_Object = MibTableColumn
matipSessionSOReceived = _MatipSessionSOReceived_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 15),
    _MatipSessionSOReceived_Type()
)
matipSessionSOReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matipSessionSOReceived.setStatus("mandatory")
_MatipSessionOCSent_Type = Counter32
_MatipSessionOCSent_Object = MibTableColumn
matipSessionOCSent = _MatipSessionOCSent_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 16),
    _MatipSessionOCSent_Type()
)
matipSessionOCSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matipSessionOCSent.setStatus("mandatory")
_MatipSessionOCReceived_Type = Counter32
_MatipSessionOCReceived_Object = MibTableColumn
matipSessionOCReceived = _MatipSessionOCReceived_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 17),
    _MatipSessionOCReceived_Type()
)
matipSessionOCReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matipSessionOCReceived.setStatus("mandatory")
_MatipSessionSCSent_Type = Counter32
_MatipSessionSCSent_Object = MibTableColumn
matipSessionSCSent = _MatipSessionSCSent_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 18),
    _MatipSessionSCSent_Type()
)
matipSessionSCSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matipSessionSCSent.setStatus("mandatory")
_MatipSessionSCReceived_Type = Counter32
_MatipSessionSCReceived_Object = MibTableColumn
matipSessionSCReceived = _MatipSessionSCReceived_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 19),
    _MatipSessionSCReceived_Type()
)
matipSessionSCReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matipSessionSCReceived.setStatus("mandatory")
_MatipSessionDataSent_Type = Counter32
_MatipSessionDataSent_Object = MibTableColumn
matipSessionDataSent = _MatipSessionDataSent_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 20),
    _MatipSessionDataSent_Type()
)
matipSessionDataSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matipSessionDataSent.setStatus("mandatory")
_MatipSessionDataReceived_Type = Counter32
_MatipSessionDataReceived_Object = MibTableColumn
matipSessionDataReceived = _MatipSessionDataReceived_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 21),
    _MatipSessionDataReceived_Type()
)
matipSessionDataReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matipSessionDataReceived.setStatus("mandatory")


class _MatipSessionStateChangeTrapEnable_Type(Integer32):
    """Custom type matipSessionStateChangeTrapEnable based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 2),
          ("partial", 3))
    )


_MatipSessionStateChangeTrapEnable_Type.__name__ = "Integer32"
_MatipSessionStateChangeTrapEnable_Object = MibTableColumn
matipSessionStateChangeTrapEnable = _MatipSessionStateChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 22),
    _MatipSessionStateChangeTrapEnable_Type()
)
matipSessionStateChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matipSessionStateChangeTrapEnable.setStatus("mandatory")


class _MatipSessionTrapReason_Type(Integer32):
    """Custom type matipSessionTrapReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("none", 1),
          ("up", 2))
    )


_MatipSessionTrapReason_Type.__name__ = "Integer32"
_MatipSessionTrapReason_Object = MibTableColumn
matipSessionTrapReason = _MatipSessionTrapReason_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 3, 3, 1, 23),
    _MatipSessionTrapReason_Type()
)
matipSessionTrapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matipSessionTrapReason.setStatus("mandatory")
_MatipTraps_ObjectIdentity = ObjectIdentity
matipTraps = _MatipTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 4)
)
_MatipUserTraps_ObjectIdentity = ObjectIdentity
matipUserTraps = _MatipUserTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 4, 1)
)
_MatipSessionTraps_ObjectIdentity = ObjectIdentity
matipSessionTraps = _MatipSessionTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 4, 2)
)

# Managed Objects groups


# Notification objects

matipUserStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 4, 1, 0, 1)
)
matipUserStateChange.setObjects(
      *(("MATIP-MIB", "matipUserIndex"),
        ("MATIP-MIB", "matipUserTrapReason"))
)
if mibBuilder.loadTexts:
    matipUserStateChange.setStatus(
        ""
    )

matipSessionStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1978, 2, 7, 4, 2, 0, 1)
)
matipSessionStateChange.setObjects(
      *(("MATIP-MIB", "matipSessionIndex"),
        ("MATIP-MIB", "matipSessionTrapReason"))
)
if mibBuilder.loadTexts:
    matipSessionStateChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MATIP-MIB",
    **{"ngcan": ngcan,
       "tiger": tiger,
       "matipMIB": matipMIB,
       "matipUser": matipUser,
       "matipNumUsers": matipNumUsers,
       "matipUserTable": matipUserTable,
       "matipUserEntry": matipUserEntry,
       "matipUserIndex": matipUserIndex,
       "matipUserHLD": matipUserHLD,
       "matipUserA1": matipUserA1,
       "matipUserA2": matipUserA2,
       "matipUserSessionRef": matipUserSessionRef,
       "matipUserCoding": matipUserCoding,
       "matipUserPresentationMode": matipUserPresentationMode,
       "matipUserQueueThresholdHi": matipUserQueueThresholdHi,
       "matipUserQueueThresholdLow": matipUserQueueThresholdLow,
       "matipUserStateTime": matipUserStateTime,
       "matipUserStatus": matipUserStatus,
       "matipUserMsgsIn": matipUserMsgsIn,
       "matipUserMsgsOut": matipUserMsgsOut,
       "matipUserCharIn": matipUserCharIn,
       "matipUserCharOut": matipUserCharOut,
       "matipUserDisconnects": matipUserDisconnects,
       "matipUserTrapReason": matipUserTrapReason,
       "matipUserStateChangeTrapEnable": matipUserStateChangeTrapEnable,
       "matipSession": matipSession,
       "matipSessionTable": matipSessionTable,
       "matipSessionEntry": matipSessionEntry,
       "matipSessionIndex": matipSessionIndex,
       "matipSessionClientServer": matipSessionClientServer,
       "matipSessionMuxMode": matipSessionMuxMode,
       "matipSessionPresentationMode": matipSessionPresentationMode,
       "matipSessionCoding": matipSessionCoding,
       "matipSessionRestartTimer": matipSessionRestartTimer,
       "matipSessionDialOnDemand": matipSessionDialOnDemand,
       "matipSessionActivityTimer": matipSessionActivityTimer,
       "matipSessionQueueThresholdHi": matipSessionQueueThresholdHi,
       "matipSessionQueueThresholdLow": matipSessionQueueThresholdLow,
       "matipSessionConnectTime": matipSessionConnectTime,
       "matipSessionStatus": matipSessionStatus,
       "matipSessionDisconnects": matipSessionDisconnects,
       "matipSessionSOSent": matipSessionSOSent,
       "matipSessionSOReceived": matipSessionSOReceived,
       "matipSessionOCSent": matipSessionOCSent,
       "matipSessionOCReceived": matipSessionOCReceived,
       "matipSessionSCSent": matipSessionSCSent,
       "matipSessionSCReceived": matipSessionSCReceived,
       "matipSessionDataSent": matipSessionDataSent,
       "matipSessionDataReceived": matipSessionDataReceived,
       "matipSessionStateChangeTrapEnable": matipSessionStateChangeTrapEnable,
       "matipSessionTrapReason": matipSessionTrapReason,
       "matipTraps": matipTraps,
       "matipUserTraps": matipUserTraps,
       "matipUserStateChange": matipUserStateChange,
       "matipSessionTraps": matipSessionTraps,
       "matipSessionStateChange": matipSessionStateChange}
)
