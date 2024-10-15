# SNMP MIB module (ACC-PHONE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-PHONE
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:42 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccPhoneGroup_ObjectIdentity = ObjectIdentity
accPhoneGroup = _AccPhoneGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 50)
)
_AccPhoneTable_Object = MibTable
accPhoneTable = _AccPhoneTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 50, 1)
)
if mibBuilder.loadTexts:
    accPhoneTable.setStatus("mandatory")
_AccPhoneTableEntry_Object = MibTableRow
accPhoneTableEntry = _AccPhoneTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 50, 1, 1)
)
accPhoneTableEntry.setIndexNames(
    (0, "ACC-PHONE", "accPhoneIndex"),
)
if mibBuilder.loadTexts:
    accPhoneTableEntry.setStatus("mandatory")
_AccPhoneIndex_Type = Integer32
_AccPhoneIndex_Object = MibTableColumn
accPhoneIndex = _AccPhoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 50, 1, 1, 1),
    _AccPhoneIndex_Type()
)
accPhoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPhoneIndex.setStatus("mandatory")
_AccPhoneDestinationPort_Type = DisplayString
_AccPhoneDestinationPort_Object = MibTableColumn
accPhoneDestinationPort = _AccPhoneDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 50, 1, 1, 2),
    _AccPhoneDestinationPort_Type()
)
accPhoneDestinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPhoneDestinationPort.setStatus("mandatory")


class _AccPhoneHookStatus_Type(Integer32):
    """Custom type accPhoneHookStatus based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 8),
          ("offhook-active-callwaiting", 10),
          ("offhook-active-normal", 7),
          ("offhook-active-threeparty", 11),
          ("offhook-active-twocalls", 9),
          ("offhook-cleared", 4),
          ("offhook-command-callwaiting", 12),
          ("offhook-command-twocalls", 13),
          ("offhook-congested", 3),
          ("offhook-enbloc-dialing", 6),
          ("offhook-enbloc-ready", 5),
          ("onhook-idle", 1),
          ("onhook-ringing", 2))
    )


_AccPhoneHookStatus_Type.__name__ = "Integer32"
_AccPhoneHookStatus_Object = MibTableColumn
accPhoneHookStatus = _AccPhoneHookStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 50, 1, 1, 3),
    _AccPhoneHookStatus_Type()
)
accPhoneHookStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPhoneHookStatus.setStatus("mandatory")


class _AccPhoneRingConfn_Type(Integer32):
    """Custom type accPhoneRingConfn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ring-EUR", 2),
          ("ring-NA", 1))
    )


_AccPhoneRingConfn_Type.__name__ = "Integer32"
_AccPhoneRingConfn_Object = MibTableColumn
accPhoneRingConfn = _AccPhoneRingConfn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 50, 1, 1, 4),
    _AccPhoneRingConfn_Type()
)
accPhoneRingConfn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPhoneRingConfn.setStatus("mandatory")
_AccPhoneNumber_Type = DisplayString
_AccPhoneNumber_Object = MibTableColumn
accPhoneNumber = _AccPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 50, 1, 1, 5),
    _AccPhoneNumber_Type()
)
accPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPhoneNumber.setStatus("mandatory")
_AccPhoneNumberStr_Type = DisplayString
_AccPhoneNumberStr_Object = MibTableColumn
accPhoneNumberStr = _AccPhoneNumberStr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 50, 1, 1, 6),
    _AccPhoneNumberStr_Type()
)
accPhoneNumberStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPhoneNumberStr.setStatus("mandatory")


class _AccPhoneAdminStatus_Type(Integer32):
    """Custom type accPhoneAdminStatus based on Integer32"""
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


_AccPhoneAdminStatus_Type.__name__ = "Integer32"
_AccPhoneAdminStatus_Object = MibTableColumn
accPhoneAdminStatus = _AccPhoneAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 50, 1, 1, 7),
    _AccPhoneAdminStatus_Type()
)
accPhoneAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPhoneAdminStatus.setStatus("mandatory")


class _AccPhoneAnswerMode_Type(Integer32):
    """Custom type accPhoneAnswerMode based on Integer32"""
    defaultValue = 2

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


_AccPhoneAnswerMode_Type.__name__ = "Integer32"
_AccPhoneAnswerMode_Object = MibTableColumn
accPhoneAnswerMode = _AccPhoneAnswerMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 50, 1, 1, 8),
    _AccPhoneAnswerMode_Type()
)
accPhoneAnswerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPhoneAnswerMode.setStatus("mandatory")


class _AccPhoneCallWaitingMode_Type(Integer32):
    """Custom type accPhoneCallWaitingMode based on Integer32"""
    defaultValue = 2

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


_AccPhoneCallWaitingMode_Type.__name__ = "Integer32"
_AccPhoneCallWaitingMode_Object = MibTableColumn
accPhoneCallWaitingMode = _AccPhoneCallWaitingMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 50, 1, 1, 9),
    _AccPhoneCallWaitingMode_Type()
)
accPhoneCallWaitingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPhoneCallWaitingMode.setStatus("mandatory")
_AccPhoneContainerTable_Object = MibTable
accPhoneContainerTable = _AccPhoneContainerTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 50, 2)
)
if mibBuilder.loadTexts:
    accPhoneContainerTable.setStatus("mandatory")
_AccPhoneContainerTableEntry_Object = MibTableRow
accPhoneContainerTableEntry = _AccPhoneContainerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 50, 2, 1)
)
accPhoneContainerTableEntry.setIndexNames(
    (0, "ACC-PHONE", "accPhoneContainerIndex"),
)
if mibBuilder.loadTexts:
    accPhoneContainerTableEntry.setStatus("mandatory")
_AccPhoneContainerIndex_Type = Integer32
_AccPhoneContainerIndex_Object = MibTableColumn
accPhoneContainerIndex = _AccPhoneContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 50, 2, 1, 1),
    _AccPhoneContainerIndex_Type()
)
accPhoneContainerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPhoneContainerIndex.setStatus("mandatory")
_AccPhoneContainerPhonePort_Type = Integer32
_AccPhoneContainerPhonePort_Object = MibTableColumn
accPhoneContainerPhonePort = _AccPhoneContainerPhonePort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 50, 2, 1, 2),
    _AccPhoneContainerPhonePort_Type()
)
accPhoneContainerPhonePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPhoneContainerPhonePort.setStatus("mandatory")


class _AccPhoneContainerStatus_Type(Integer32):
    """Custom type accPhoneContainerStatus based on Integer32"""
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
        *(("empty", 1),
          ("reserved", 2),
          ("used-held", 5),
          ("used-invisible", 3),
          ("used-visible", 4))
    )


_AccPhoneContainerStatus_Type.__name__ = "Integer32"
_AccPhoneContainerStatus_Object = MibTableColumn
accPhoneContainerStatus = _AccPhoneContainerStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 50, 2, 1, 3),
    _AccPhoneContainerStatus_Type()
)
accPhoneContainerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPhoneContainerStatus.setStatus("mandatory")
_AccPhoneContainerCallRef_Type = Integer32
_AccPhoneContainerCallRef_Object = MibTableColumn
accPhoneContainerCallRef = _AccPhoneContainerCallRef_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 50, 2, 1, 4),
    _AccPhoneContainerCallRef_Type()
)
accPhoneContainerCallRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPhoneContainerCallRef.setStatus("mandatory")


class _AccPhoneContainerCallDir_Type(Integer32):
    """Custom type accPhoneContainerCallDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("none", 3),
          ("outgoing", 2))
    )


_AccPhoneContainerCallDir_Type.__name__ = "Integer32"
_AccPhoneContainerCallDir_Object = MibTableColumn
accPhoneContainerCallDir = _AccPhoneContainerCallDir_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 50, 2, 1, 5),
    _AccPhoneContainerCallDir_Type()
)
accPhoneContainerCallDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPhoneContainerCallDir.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-PHONE",
    **{"accPhoneGroup": accPhoneGroup,
       "accPhoneTable": accPhoneTable,
       "accPhoneTableEntry": accPhoneTableEntry,
       "accPhoneIndex": accPhoneIndex,
       "accPhoneDestinationPort": accPhoneDestinationPort,
       "accPhoneHookStatus": accPhoneHookStatus,
       "accPhoneRingConfn": accPhoneRingConfn,
       "accPhoneNumber": accPhoneNumber,
       "accPhoneNumberStr": accPhoneNumberStr,
       "accPhoneAdminStatus": accPhoneAdminStatus,
       "accPhoneAnswerMode": accPhoneAnswerMode,
       "accPhoneCallWaitingMode": accPhoneCallWaitingMode,
       "accPhoneContainerTable": accPhoneContainerTable,
       "accPhoneContainerTableEntry": accPhoneContainerTableEntry,
       "accPhoneContainerIndex": accPhoneContainerIndex,
       "accPhoneContainerPhonePort": accPhoneContainerPhonePort,
       "accPhoneContainerStatus": accPhoneContainerStatus,
       "accPhoneContainerCallRef": accPhoneContainerCallRef,
       "accPhoneContainerCallDir": accPhoneContainerCallDir}
)
