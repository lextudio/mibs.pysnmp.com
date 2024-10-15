# SNMP MIB module (HH3C-MAC-INFORMATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-MAC-INFORMATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:03 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cMACInformation = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87)
)
hh3cMACInformation.setRevisions(
        ("2007-12-28 19:12",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cMACInfoWorkMode(Integer32, TextualConvention):
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

_Hh3cMACInformationObjects_ObjectIdentity = ObjectIdentity
hh3cMACInformationObjects = _Hh3cMACInformationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1)
)
_Hh3cMACInformationMibGlobal_ObjectIdentity = ObjectIdentity
hh3cMACInformationMibGlobal = _Hh3cMACInformationMibGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 1)
)


class _Hh3cMACInformationEnabled_Type(Integer32):
    """Custom type hh3cMACInformationEnabled based on Integer32"""
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


_Hh3cMACInformationEnabled_Type.__name__ = "Integer32"
_Hh3cMACInformationEnabled_Object = MibScalar
hh3cMACInformationEnabled = _Hh3cMACInformationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 1, 1),
    _Hh3cMACInformationEnabled_Type()
)
hh3cMACInformationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMACInformationEnabled.setStatus("current")


class _Hh3cMACInformationcSendInterval_Type(Unsigned32):
    """Custom type hh3cMACInformationcSendInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_Hh3cMACInformationcSendInterval_Type.__name__ = "Unsigned32"
_Hh3cMACInformationcSendInterval_Object = MibScalar
hh3cMACInformationcSendInterval = _Hh3cMACInformationcSendInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 1, 2),
    _Hh3cMACInformationcSendInterval_Type()
)
hh3cMACInformationcSendInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMACInformationcSendInterval.setStatus("current")
_Hh3cMACInformationLearntMACNum_Type = Counter32
_Hh3cMACInformationLearntMACNum_Object = MibScalar
hh3cMACInformationLearntMACNum = _Hh3cMACInformationLearntMACNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 1, 3),
    _Hh3cMACInformationLearntMACNum_Type()
)
hh3cMACInformationLearntMACNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMACInformationLearntMACNum.setStatus("current")
_Hh3cMACInformationRemovedMACNum_Type = Counter32
_Hh3cMACInformationRemovedMACNum_Object = MibScalar
hh3cMACInformationRemovedMACNum = _Hh3cMACInformationRemovedMACNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 1, 4),
    _Hh3cMACInformationRemovedMACNum_Type()
)
hh3cMACInformationRemovedMACNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMACInformationRemovedMACNum.setStatus("current")
_Hh3cMACInformationTrapSendNum_Type = Counter32
_Hh3cMACInformationTrapSendNum_Object = MibScalar
hh3cMACInformationTrapSendNum = _Hh3cMACInformationTrapSendNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 1, 5),
    _Hh3cMACInformationTrapSendNum_Type()
)
hh3cMACInformationTrapSendNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMACInformationTrapSendNum.setStatus("current")
_Hh3cMACInformationSyslogSendNum_Type = Counter32
_Hh3cMACInformationSyslogSendNum_Object = MibScalar
hh3cMACInformationSyslogSendNum = _Hh3cMACInformationSyslogSendNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 1, 6),
    _Hh3cMACInformationSyslogSendNum_Type()
)
hh3cMACInformationSyslogSendNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMACInformationSyslogSendNum.setStatus("current")


class _Hh3cMACInformationCacheLen_Type(Unsigned32):
    """Custom type hh3cMACInformationCacheLen based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Hh3cMACInformationCacheLen_Type.__name__ = "Unsigned32"
_Hh3cMACInformationCacheLen_Object = MibScalar
hh3cMACInformationCacheLen = _Hh3cMACInformationCacheLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 1, 7),
    _Hh3cMACInformationCacheLen_Type()
)
hh3cMACInformationCacheLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMACInformationCacheLen.setStatus("current")
_Hh3cMACInfomationWorkMode_Type = Hh3cMACInfoWorkMode
_Hh3cMACInfomationWorkMode_Object = MibScalar
hh3cMACInfomationWorkMode = _Hh3cMACInfomationWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 1, 8),
    _Hh3cMACInfomationWorkMode_Type()
)
hh3cMACInfomationWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMACInfomationWorkMode.setStatus("current")
_Hh3cMACInformationMIBTableTroop_ObjectIdentity = ObjectIdentity
hh3cMACInformationMIBTableTroop = _Hh3cMACInformationMIBTableTroop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 2)
)
_Hh3cMACInfomationIfTable_Object = MibTable
hh3cMACInfomationIfTable = _Hh3cMACInfomationIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cMACInfomationIfTable.setStatus("current")
_Hh3cMACInfomationIfEntry_Object = MibTableRow
hh3cMACInfomationIfEntry = _Hh3cMACInfomationIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 2, 1, 1)
)
hh3cMACInfomationIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cMACInfomationIfEntry.setStatus("current")


class _Hh3cMACLearntEnable_Type(Integer32):
    """Custom type hh3cMACLearntEnable based on Integer32"""
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


_Hh3cMACLearntEnable_Type.__name__ = "Integer32"
_Hh3cMACLearntEnable_Object = MibTableColumn
hh3cMACLearntEnable = _Hh3cMACLearntEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 2, 1, 1, 1),
    _Hh3cMACLearntEnable_Type()
)
hh3cMACLearntEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMACLearntEnable.setStatus("current")


class _Hh3cMACRemovedEnable_Type(Integer32):
    """Custom type hh3cMACRemovedEnable based on Integer32"""
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


_Hh3cMACRemovedEnable_Type.__name__ = "Integer32"
_Hh3cMACRemovedEnable_Object = MibTableColumn
hh3cMACRemovedEnable = _Hh3cMACRemovedEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 2, 1, 1, 2),
    _Hh3cMACRemovedEnable_Type()
)
hh3cMACRemovedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMACRemovedEnable.setStatus("current")
_Hh3cMACInformationMibTrap_ObjectIdentity = ObjectIdentity
hh3cMACInformationMibTrap = _Hh3cMACInformationMibTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 3)
)
_Hh3cMACInformationTraps_ObjectIdentity = ObjectIdentity
hh3cMACInformationTraps = _Hh3cMACInformationTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 3, 0)
)
_Hh3cMACInformationTrapObjects_ObjectIdentity = ObjectIdentity
hh3cMACInformationTrapObjects = _Hh3cMACInformationTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 3, 2)
)


class _Hh3cMACInfoTrapIndex_Type(Unsigned32):
    """Custom type hh3cMACInfoTrapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cMACInfoTrapIndex_Type.__name__ = "Unsigned32"
_Hh3cMACInfoTrapIndex_Object = MibScalar
hh3cMACInfoTrapIndex = _Hh3cMACInfoTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 3, 2, 1),
    _Hh3cMACInfoTrapIndex_Type()
)
hh3cMACInfoTrapIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cMACInfoTrapIndex.setStatus("current")
_Hh3cMACInfoTrapCount_Type = Unsigned32
_Hh3cMACInfoTrapCount_Object = MibScalar
hh3cMACInfoTrapCount = _Hh3cMACInfoTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 3, 2, 2),
    _Hh3cMACInfoTrapCount_Type()
)
hh3cMACInfoTrapCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cMACInfoTrapCount.setStatus("current")


class _Hh3cMACInfoTrapMsg_Type(OctetString):
    """Custom type hh3cMACInfoTrapMsg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 254),
    )


_Hh3cMACInfoTrapMsg_Type.__name__ = "OctetString"
_Hh3cMACInfoTrapMsg_Object = MibScalar
hh3cMACInfoTrapMsg = _Hh3cMACInfoTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 3, 2, 3),
    _Hh3cMACInfoTrapMsg_Type()
)
hh3cMACInfoTrapMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cMACInfoTrapMsg.setStatus("current")
_Hh3cMACInformationMibTrapExt_ObjectIdentity = ObjectIdentity
hh3cMACInformationMibTrapExt = _Hh3cMACInformationMibTrapExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 4)
)
_Hh3cMACInformationTrapsExt_ObjectIdentity = ObjectIdentity
hh3cMACInformationTrapsExt = _Hh3cMACInformationTrapsExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 4, 0)
)
_Hh3cMACInformationTrapObjectsExt_ObjectIdentity = ObjectIdentity
hh3cMACInformationTrapObjectsExt = _Hh3cMACInformationTrapObjectsExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 4, 2)
)
_Hh3cMACInfoTrapVerExt_Type = Unsigned32
_Hh3cMACInfoTrapVerExt_Object = MibScalar
hh3cMACInfoTrapVerExt = _Hh3cMACInfoTrapVerExt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 4, 2, 1),
    _Hh3cMACInfoTrapVerExt_Type()
)
hh3cMACInfoTrapVerExt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cMACInfoTrapVerExt.setStatus("current")


class _Hh3cMACInfoTrapIndexExt_Type(Unsigned32):
    """Custom type hh3cMACInfoTrapIndexExt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cMACInfoTrapIndexExt_Type.__name__ = "Unsigned32"
_Hh3cMACInfoTrapIndexExt_Object = MibScalar
hh3cMACInfoTrapIndexExt = _Hh3cMACInfoTrapIndexExt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 4, 2, 2),
    _Hh3cMACInfoTrapIndexExt_Type()
)
hh3cMACInfoTrapIndexExt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cMACInfoTrapIndexExt.setStatus("current")
_Hh3cMACInfoTrapCountExt_Type = Unsigned32
_Hh3cMACInfoTrapCountExt_Object = MibScalar
hh3cMACInfoTrapCountExt = _Hh3cMACInfoTrapCountExt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 4, 2, 3),
    _Hh3cMACInfoTrapCountExt_Type()
)
hh3cMACInfoTrapCountExt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cMACInfoTrapCountExt.setStatus("current")


class _Hh3cMACInfoTrapMsgExt_Type(OctetString):
    """Custom type hh3cMACInfoTrapMsgExt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 254),
    )


_Hh3cMACInfoTrapMsgExt_Type.__name__ = "OctetString"
_Hh3cMACInfoTrapMsgExt_Object = MibScalar
hh3cMACInfoTrapMsgExt = _Hh3cMACInfoTrapMsgExt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 4, 2, 4),
    _Hh3cMACInfoTrapMsgExt_Type()
)
hh3cMACInfoTrapMsgExt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cMACInfoTrapMsgExt.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cMACInformationChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 3, 0, 1)
)
hh3cMACInformationChangedTrap.setObjects(
      *(("HH3C-MAC-INFORMATION-MIB", "hh3cMACInfoTrapIndex"),
        ("HH3C-MAC-INFORMATION-MIB", "hh3cMACInfoTrapCount"),
        ("HH3C-MAC-INFORMATION-MIB", "hh3cMACInfoTrapMsg"))
)
if mibBuilder.loadTexts:
    hh3cMACInformationChangedTrap.setStatus(
        "current"
    )

hh3cMACInformationChangedTrapExt = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87, 1, 4, 0, 1)
)
hh3cMACInformationChangedTrapExt.setObjects(
      *(("HH3C-MAC-INFORMATION-MIB", "hh3cMACInfoTrapVerExt"),
        ("HH3C-MAC-INFORMATION-MIB", "hh3cMACInfoTrapIndexExt"),
        ("HH3C-MAC-INFORMATION-MIB", "hh3cMACInfoTrapCountExt"),
        ("HH3C-MAC-INFORMATION-MIB", "hh3cMACInfoTrapMsgExt"))
)
if mibBuilder.loadTexts:
    hh3cMACInformationChangedTrapExt.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-MAC-INFORMATION-MIB",
    **{"Hh3cMACInfoWorkMode": Hh3cMACInfoWorkMode,
       "hh3cMACInformation": hh3cMACInformation,
       "hh3cMACInformationObjects": hh3cMACInformationObjects,
       "hh3cMACInformationMibGlobal": hh3cMACInformationMibGlobal,
       "hh3cMACInformationEnabled": hh3cMACInformationEnabled,
       "hh3cMACInformationcSendInterval": hh3cMACInformationcSendInterval,
       "hh3cMACInformationLearntMACNum": hh3cMACInformationLearntMACNum,
       "hh3cMACInformationRemovedMACNum": hh3cMACInformationRemovedMACNum,
       "hh3cMACInformationTrapSendNum": hh3cMACInformationTrapSendNum,
       "hh3cMACInformationSyslogSendNum": hh3cMACInformationSyslogSendNum,
       "hh3cMACInformationCacheLen": hh3cMACInformationCacheLen,
       "hh3cMACInfomationWorkMode": hh3cMACInfomationWorkMode,
       "hh3cMACInformationMIBTableTroop": hh3cMACInformationMIBTableTroop,
       "hh3cMACInfomationIfTable": hh3cMACInfomationIfTable,
       "hh3cMACInfomationIfEntry": hh3cMACInfomationIfEntry,
       "hh3cMACLearntEnable": hh3cMACLearntEnable,
       "hh3cMACRemovedEnable": hh3cMACRemovedEnable,
       "hh3cMACInformationMibTrap": hh3cMACInformationMibTrap,
       "hh3cMACInformationTraps": hh3cMACInformationTraps,
       "hh3cMACInformationChangedTrap": hh3cMACInformationChangedTrap,
       "hh3cMACInformationTrapObjects": hh3cMACInformationTrapObjects,
       "hh3cMACInfoTrapIndex": hh3cMACInfoTrapIndex,
       "hh3cMACInfoTrapCount": hh3cMACInfoTrapCount,
       "hh3cMACInfoTrapMsg": hh3cMACInfoTrapMsg,
       "hh3cMACInformationMibTrapExt": hh3cMACInformationMibTrapExt,
       "hh3cMACInformationTrapsExt": hh3cMACInformationTrapsExt,
       "hh3cMACInformationChangedTrapExt": hh3cMACInformationChangedTrapExt,
       "hh3cMACInformationTrapObjectsExt": hh3cMACInformationTrapObjectsExt,
       "hh3cMACInfoTrapVerExt": hh3cMACInfoTrapVerExt,
       "hh3cMACInfoTrapIndexExt": hh3cMACInfoTrapIndexExt,
       "hh3cMACInfoTrapCountExt": hh3cMACInfoTrapCountExt,
       "hh3cMACInfoTrapMsgExt": hh3cMACInfoTrapMsgExt}
)
