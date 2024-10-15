# SNMP MIB module (A3COM-HUAWEI-MAC-INFORMATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-MAC-INFORMATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:31 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

h3cMACInformation = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87)
)
h3cMACInformation.setRevisions(
        ("2007-12-28 19:12",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cMACInfoWorkMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("syslog", 2),
          ("trap", 1))
    )



# MIB Managed Objects in the order of their OIDs

_H3cMACInformationObjects_ObjectIdentity = ObjectIdentity
h3cMACInformationObjects = _H3cMACInformationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1)
)
_H3cMACInformationMibGlobal_ObjectIdentity = ObjectIdentity
h3cMACInformationMibGlobal = _H3cMACInformationMibGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 1)
)


class _H3cMACInformationEnabled_Type(Integer32):
    """Custom type h3cMACInformationEnabled based on Integer32"""
    defaultValue = 2

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


_H3cMACInformationEnabled_Type.__name__ = "Integer32"
_H3cMACInformationEnabled_Object = MibScalar
h3cMACInformationEnabled = _H3cMACInformationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 1, 1),
    _H3cMACInformationEnabled_Type()
)
h3cMACInformationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMACInformationEnabled.setStatus("current")


class _H3cMACInformationcSendInterval_Type(Unsigned32):
    """Custom type h3cMACInformationcSendInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_H3cMACInformationcSendInterval_Type.__name__ = "Unsigned32"
_H3cMACInformationcSendInterval_Object = MibScalar
h3cMACInformationcSendInterval = _H3cMACInformationcSendInterval_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 1, 2),
    _H3cMACInformationcSendInterval_Type()
)
h3cMACInformationcSendInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMACInformationcSendInterval.setStatus("current")
_H3cMACInformationLearntMACNum_Type = Counter32
_H3cMACInformationLearntMACNum_Object = MibScalar
h3cMACInformationLearntMACNum = _H3cMACInformationLearntMACNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 1, 3),
    _H3cMACInformationLearntMACNum_Type()
)
h3cMACInformationLearntMACNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMACInformationLearntMACNum.setStatus("current")
_H3cMACInformationRemovedMACNum_Type = Counter32
_H3cMACInformationRemovedMACNum_Object = MibScalar
h3cMACInformationRemovedMACNum = _H3cMACInformationRemovedMACNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 1, 4),
    _H3cMACInformationRemovedMACNum_Type()
)
h3cMACInformationRemovedMACNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMACInformationRemovedMACNum.setStatus("current")
_H3cMACInformationTrapSendNum_Type = Counter32
_H3cMACInformationTrapSendNum_Object = MibScalar
h3cMACInformationTrapSendNum = _H3cMACInformationTrapSendNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 1, 5),
    _H3cMACInformationTrapSendNum_Type()
)
h3cMACInformationTrapSendNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMACInformationTrapSendNum.setStatus("current")
_H3cMACInformationSyslogSendNum_Type = Counter32
_H3cMACInformationSyslogSendNum_Object = MibScalar
h3cMACInformationSyslogSendNum = _H3cMACInformationSyslogSendNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 1, 6),
    _H3cMACInformationSyslogSendNum_Type()
)
h3cMACInformationSyslogSendNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMACInformationSyslogSendNum.setStatus("current")


class _H3cMACInformationCacheLen_Type(Unsigned32):
    """Custom type h3cMACInformationCacheLen based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_H3cMACInformationCacheLen_Type.__name__ = "Unsigned32"
_H3cMACInformationCacheLen_Object = MibScalar
h3cMACInformationCacheLen = _H3cMACInformationCacheLen_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 1, 7),
    _H3cMACInformationCacheLen_Type()
)
h3cMACInformationCacheLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMACInformationCacheLen.setStatus("current")
_H3cMACInfomationWorkMode_Type = H3cMACInfoWorkMode
_H3cMACInfomationWorkMode_Object = MibScalar
h3cMACInfomationWorkMode = _H3cMACInfomationWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 1, 8),
    _H3cMACInfomationWorkMode_Type()
)
h3cMACInfomationWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMACInfomationWorkMode.setStatus("current")
_H3cMACInformationMIBTableTroop_ObjectIdentity = ObjectIdentity
h3cMACInformationMIBTableTroop = _H3cMACInformationMIBTableTroop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 2)
)
_H3cMACInfomationIfTable_Object = MibTable
h3cMACInfomationIfTable = _H3cMACInfomationIfTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cMACInfomationIfTable.setStatus("current")
_H3cMACInfomationIfEntry_Object = MibTableRow
h3cMACInfomationIfEntry = _H3cMACInfomationIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 2, 1, 1)
)
h3cMACInfomationIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cMACInfomationIfEntry.setStatus("current")


class _H3cMACLearntEnable_Type(Integer32):
    """Custom type h3cMACLearntEnable based on Integer32"""
    defaultValue = 2

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


_H3cMACLearntEnable_Type.__name__ = "Integer32"
_H3cMACLearntEnable_Object = MibTableColumn
h3cMACLearntEnable = _H3cMACLearntEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 2, 1, 1, 1),
    _H3cMACLearntEnable_Type()
)
h3cMACLearntEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMACLearntEnable.setStatus("current")


class _H3cMACRemovedEnable_Type(Integer32):
    """Custom type h3cMACRemovedEnable based on Integer32"""
    defaultValue = 2

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


_H3cMACRemovedEnable_Type.__name__ = "Integer32"
_H3cMACRemovedEnable_Object = MibTableColumn
h3cMACRemovedEnable = _H3cMACRemovedEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 2, 1, 1, 2),
    _H3cMACRemovedEnable_Type()
)
h3cMACRemovedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMACRemovedEnable.setStatus("current")
_H3cMACInformationMibTrap_ObjectIdentity = ObjectIdentity
h3cMACInformationMibTrap = _H3cMACInformationMibTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 3)
)
_H3cMACInformationTraps_ObjectIdentity = ObjectIdentity
h3cMACInformationTraps = _H3cMACInformationTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 3, 0)
)
_H3cMACInformationTrapObjects_ObjectIdentity = ObjectIdentity
h3cMACInformationTrapObjects = _H3cMACInformationTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 3, 2)
)


class _H3cMACInfoTrapIndex_Type(Unsigned32):
    """Custom type h3cMACInfoTrapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_H3cMACInfoTrapIndex_Type.__name__ = "Unsigned32"
_H3cMACInfoTrapIndex_Object = MibScalar
h3cMACInfoTrapIndex = _H3cMACInfoTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 3, 2, 1),
    _H3cMACInfoTrapIndex_Type()
)
h3cMACInfoTrapIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cMACInfoTrapIndex.setStatus("current")
_H3cMACInfoTrapCount_Type = Unsigned32
_H3cMACInfoTrapCount_Object = MibScalar
h3cMACInfoTrapCount = _H3cMACInfoTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 3, 2, 2),
    _H3cMACInfoTrapCount_Type()
)
h3cMACInfoTrapCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cMACInfoTrapCount.setStatus("current")


class _H3cMACInfoTrapMsg_Type(OctetString):
    """Custom type h3cMACInfoTrapMsg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 254),
    )


_H3cMACInfoTrapMsg_Type.__name__ = "OctetString"
_H3cMACInfoTrapMsg_Object = MibScalar
h3cMACInfoTrapMsg = _H3cMACInfoTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 3, 2, 3),
    _H3cMACInfoTrapMsg_Type()
)
h3cMACInfoTrapMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cMACInfoTrapMsg.setStatus("current")
_H3cMACInformationMibTrapExt_ObjectIdentity = ObjectIdentity
h3cMACInformationMibTrapExt = _H3cMACInformationMibTrapExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 4)
)
_H3cMACInformationTrapsExt_ObjectIdentity = ObjectIdentity
h3cMACInformationTrapsExt = _H3cMACInformationTrapsExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 4, 0)
)
_H3cMACInformationTrapObjectsExt_ObjectIdentity = ObjectIdentity
h3cMACInformationTrapObjectsExt = _H3cMACInformationTrapObjectsExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 4, 2)
)
_H3cMACInfoTrapVerExt_Type = Unsigned32
_H3cMACInfoTrapVerExt_Object = MibScalar
h3cMACInfoTrapVerExt = _H3cMACInfoTrapVerExt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 4, 2, 1),
    _H3cMACInfoTrapVerExt_Type()
)
h3cMACInfoTrapVerExt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cMACInfoTrapVerExt.setStatus("current")


class _H3cMACInfoTrapIndexExt_Type(Unsigned32):
    """Custom type h3cMACInfoTrapIndexExt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_H3cMACInfoTrapIndexExt_Type.__name__ = "Unsigned32"
_H3cMACInfoTrapIndexExt_Object = MibScalar
h3cMACInfoTrapIndexExt = _H3cMACInfoTrapIndexExt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 4, 2, 2),
    _H3cMACInfoTrapIndexExt_Type()
)
h3cMACInfoTrapIndexExt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cMACInfoTrapIndexExt.setStatus("current")
_H3cMACInfoTrapCountExt_Type = Unsigned32
_H3cMACInfoTrapCountExt_Object = MibScalar
h3cMACInfoTrapCountExt = _H3cMACInfoTrapCountExt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 4, 2, 3),
    _H3cMACInfoTrapCountExt_Type()
)
h3cMACInfoTrapCountExt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cMACInfoTrapCountExt.setStatus("current")


class _H3cMACInfoTrapMsgExt_Type(OctetString):
    """Custom type h3cMACInfoTrapMsgExt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 254),
    )


_H3cMACInfoTrapMsgExt_Type.__name__ = "OctetString"
_H3cMACInfoTrapMsgExt_Object = MibScalar
h3cMACInfoTrapMsgExt = _H3cMACInfoTrapMsgExt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 4, 2, 4),
    _H3cMACInfoTrapMsgExt_Type()
)
h3cMACInfoTrapMsgExt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cMACInfoTrapMsgExt.setStatus("current")

# Managed Objects groups


# Notification objects

h3cMACInformationChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 3, 0, 1)
)
h3cMACInformationChangedTrap.setObjects(
      *(("A3COM-HUAWEI-MAC-INFORMATION-MIB", "h3cMACInfoTrapIndex"),
        ("A3COM-HUAWEI-MAC-INFORMATION-MIB", "h3cMACInfoTrapCount"),
        ("A3COM-HUAWEI-MAC-INFORMATION-MIB", "h3cMACInfoTrapMsg"))
)
if mibBuilder.loadTexts:
    h3cMACInformationChangedTrap.setStatus(
        "current"
    )

h3cMACInformationChangedTrapExt = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 87, 1, 4, 0, 1)
)
h3cMACInformationChangedTrapExt.setObjects(
      *(("A3COM-HUAWEI-MAC-INFORMATION-MIB", "h3cMACInfoTrapVerExt"),
        ("A3COM-HUAWEI-MAC-INFORMATION-MIB", "h3cMACInfoTrapIndexExt"),
        ("A3COM-HUAWEI-MAC-INFORMATION-MIB", "h3cMACInfoTrapCountExt"),
        ("A3COM-HUAWEI-MAC-INFORMATION-MIB", "h3cMACInfoTrapMsgExt"))
)
if mibBuilder.loadTexts:
    h3cMACInformationChangedTrapExt.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-MAC-INFORMATION-MIB",
    **{"H3cMACInfoWorkMode": H3cMACInfoWorkMode,
       "h3cMACInformation": h3cMACInformation,
       "h3cMACInformationObjects": h3cMACInformationObjects,
       "h3cMACInformationMibGlobal": h3cMACInformationMibGlobal,
       "h3cMACInformationEnabled": h3cMACInformationEnabled,
       "h3cMACInformationcSendInterval": h3cMACInformationcSendInterval,
       "h3cMACInformationLearntMACNum": h3cMACInformationLearntMACNum,
       "h3cMACInformationRemovedMACNum": h3cMACInformationRemovedMACNum,
       "h3cMACInformationTrapSendNum": h3cMACInformationTrapSendNum,
       "h3cMACInformationSyslogSendNum": h3cMACInformationSyslogSendNum,
       "h3cMACInformationCacheLen": h3cMACInformationCacheLen,
       "h3cMACInfomationWorkMode": h3cMACInfomationWorkMode,
       "h3cMACInformationMIBTableTroop": h3cMACInformationMIBTableTroop,
       "h3cMACInfomationIfTable": h3cMACInfomationIfTable,
       "h3cMACInfomationIfEntry": h3cMACInfomationIfEntry,
       "h3cMACLearntEnable": h3cMACLearntEnable,
       "h3cMACRemovedEnable": h3cMACRemovedEnable,
       "h3cMACInformationMibTrap": h3cMACInformationMibTrap,
       "h3cMACInformationTraps": h3cMACInformationTraps,
       "h3cMACInformationChangedTrap": h3cMACInformationChangedTrap,
       "h3cMACInformationTrapObjects": h3cMACInformationTrapObjects,
       "h3cMACInfoTrapIndex": h3cMACInfoTrapIndex,
       "h3cMACInfoTrapCount": h3cMACInfoTrapCount,
       "h3cMACInfoTrapMsg": h3cMACInfoTrapMsg,
       "h3cMACInformationMibTrapExt": h3cMACInformationMibTrapExt,
       "h3cMACInformationTrapsExt": h3cMACInformationTrapsExt,
       "h3cMACInformationChangedTrapExt": h3cMACInformationChangedTrapExt,
       "h3cMACInformationTrapObjectsExt": h3cMACInformationTrapObjectsExt,
       "h3cMACInfoTrapVerExt": h3cMACInfoTrapVerExt,
       "h3cMACInfoTrapIndexExt": h3cMACInfoTrapIndexExt,
       "h3cMACInfoTrapCountExt": h3cMACInfoTrapCountExt,
       "h3cMACInfoTrapMsgExt": h3cMACInfoTrapMsgExt}
)
