# SNMP MIB module (BIANCA-BRICK-MSGBOX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-MSGBOX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:35 2024
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

(BitValue,
 Date) = mibBuilder.importSymbols(
    "BIANCA-BRICK-PPP-MIB",
    "BitValue",
    "Date")

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



class HexValue(Integer32):
    """Custom type HexValue based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Isdn_ObjectIdentity = ObjectIdentity
isdn = _Isdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 2)
)
_MsgForwardTable_Object = MibTable
msgForwardTable = _MsgForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 13)
)
if mibBuilder.loadTexts:
    msgForwardTable.setStatus("mandatory")
_MsgForwardEntry_Object = MibTableRow
msgForwardEntry = _MsgForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 13, 1)
)
msgForwardEntry.setIndexNames(
    (0, "BIANCA-BRICK-MSGBOX-MIB", "msgForwardExtension"),
)
if mibBuilder.loadTexts:
    msgForwardEntry.setStatus("mandatory")
_MsgForwardExtension_Type = DisplayString
_MsgForwardExtension_Object = MibTableColumn
msgForwardExtension = _MsgForwardExtension_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 13, 1, 1),
    _MsgForwardExtension_Type()
)
msgForwardExtension.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msgForwardExtension.setStatus("mandatory")
_MsgForwardAddr_Type = DisplayString
_MsgForwardAddr_Object = MibTableColumn
msgForwardAddr = _MsgForwardAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 13, 1, 2),
    _MsgForwardAddr_Type()
)
msgForwardAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msgForwardAddr.setStatus("mandatory")


class _MsgForwardDeleteAction_Type(Integer32):
    """Custom type msgForwardDeleteAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delivered", 1),
          ("forwarded", 2),
          ("polled", 3))
    )


_MsgForwardDeleteAction_Type.__name__ = "Integer32"
_MsgForwardDeleteAction_Object = MibTableColumn
msgForwardDeleteAction = _MsgForwardDeleteAction_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 13, 1, 3),
    _MsgForwardDeleteAction_Type()
)
msgForwardDeleteAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msgForwardDeleteAction.setStatus("mandatory")


class _MsgForwardDelay_Type(Integer32):
    """Custom type msgForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1209600),
    )


_MsgForwardDelay_Type.__name__ = "Integer32"
_MsgForwardDelay_Object = MibTableColumn
msgForwardDelay = _MsgForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 13, 1, 4),
    _MsgForwardDelay_Type()
)
msgForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msgForwardDelay.setStatus("mandatory")


class _MsgForwardPoll_Type(Integer32):
    """Custom type msgForwardPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_MsgForwardPoll_Type.__name__ = "Integer32"
_MsgForwardPoll_Object = MibTableColumn
msgForwardPoll = _MsgForwardPoll_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 13, 1, 5),
    _MsgForwardPoll_Type()
)
msgForwardPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msgForwardPoll.setStatus("mandatory")
_MsgForwardPollPassword_Type = DisplayString
_MsgForwardPollPassword_Object = MibTableColumn
msgForwardPollPassword = _MsgForwardPollPassword_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 13, 1, 6),
    _MsgForwardPollPassword_Type()
)
msgForwardPollPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msgForwardPollPassword.setStatus("mandatory")


class _MsgForwardMaxRetries_Type(Integer32):
    """Custom type msgForwardMaxRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MsgForwardMaxRetries_Type.__name__ = "Integer32"
_MsgForwardMaxRetries_Object = MibTableColumn
msgForwardMaxRetries = _MsgForwardMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 13, 1, 7),
    _MsgForwardMaxRetries_Type()
)
msgForwardMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msgForwardMaxRetries.setStatus("mandatory")


class _MsgForwardState_Type(Integer32):
    """Custom type msgForwardState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_MsgForwardState_Type.__name__ = "Integer32"
_MsgForwardState_Object = MibTableColumn
msgForwardState = _MsgForwardState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 13, 1, 8),
    _MsgForwardState_Type()
)
msgForwardState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msgForwardState.setStatus("mandatory")
_MsgDirTable_Object = MibTable
msgDirTable = _MsgDirTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 14)
)
if mibBuilder.loadTexts:
    msgDirTable.setStatus("mandatory")
_MsgDirEntry_Object = MibTableRow
msgDirEntry = _MsgDirEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 14, 1)
)
msgDirEntry.setIndexNames(
    (0, "BIANCA-BRICK-MSGBOX-MIB", "msgDirExtension"),
)
if mibBuilder.loadTexts:
    msgDirEntry.setStatus("mandatory")
_MsgDirExtension_Type = DisplayString
_MsgDirExtension_Object = MibTableColumn
msgDirExtension = _MsgDirExtension_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 14, 1, 1),
    _MsgDirExtension_Type()
)
msgDirExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgDirExtension.setStatus("mandatory")


class _MsgDirType_Type(Integer32):
    """Custom type msgDirType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fax", 2),
          ("none", 1))
    )


_MsgDirType_Type.__name__ = "Integer32"
_MsgDirType_Object = MibTableColumn
msgDirType = _MsgDirType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 14, 1, 2),
    _MsgDirType_Type()
)
msgDirType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgDirType.setStatus("mandatory")
_MsgDirContent_Type = DisplayString
_MsgDirContent_Object = MibTableColumn
msgDirContent = _MsgDirContent_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 14, 1, 3),
    _MsgDirContent_Type()
)
msgDirContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgDirContent.setStatus("mandatory")
_MsgDirTime_Type = Date
_MsgDirTime_Object = MibTableColumn
msgDirTime = _MsgDirTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 14, 1, 4),
    _MsgDirTime_Type()
)
msgDirTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgDirTime.setStatus("mandatory")
_MsgDirDuration_Type = Integer32
_MsgDirDuration_Object = MibTableColumn
msgDirDuration = _MsgDirDuration_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 14, 1, 5),
    _MsgDirDuration_Type()
)
msgDirDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgDirDuration.setStatus("mandatory")
_MsgDirSize_Type = Integer32
_MsgDirSize_Object = MibTableColumn
msgDirSize = _MsgDirSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 14, 1, 6),
    _MsgDirSize_Type()
)
msgDirSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgDirSize.setStatus("mandatory")


class _MsgDirState_Type(Integer32):
    """Custom type msgDirState based on Integer32"""
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
        *(("delete", 5),
          ("deleted", 4),
          ("received", 2),
          ("receiving", 1),
          ("sent", 3))
    )


_MsgDirState_Type.__name__ = "Integer32"
_MsgDirState_Object = MibTableColumn
msgDirState = _MsgDirState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 2, 14, 1, 7),
    _MsgDirState_Type()
)
msgDirState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msgDirState.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-MSGBOX-MIB",
    **{"HexValue": HexValue,
       "org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bibo": bibo,
       "isdn": isdn,
       "msgForwardTable": msgForwardTable,
       "msgForwardEntry": msgForwardEntry,
       "msgForwardExtension": msgForwardExtension,
       "msgForwardAddr": msgForwardAddr,
       "msgForwardDeleteAction": msgForwardDeleteAction,
       "msgForwardDelay": msgForwardDelay,
       "msgForwardPoll": msgForwardPoll,
       "msgForwardPollPassword": msgForwardPollPassword,
       "msgForwardMaxRetries": msgForwardMaxRetries,
       "msgForwardState": msgForwardState,
       "msgDirTable": msgDirTable,
       "msgDirEntry": msgDirEntry,
       "msgDirExtension": msgDirExtension,
       "msgDirType": msgDirType,
       "msgDirContent": msgDirContent,
       "msgDirTime": msgDirTime,
       "msgDirDuration": msgDirDuration,
       "msgDirSize": msgDirSize,
       "msgDirState": msgDirState}
)
