# SNMP MIB module (HPN-ICF-MAC-INFORMATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-MAC-INFORMATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:02 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

hpnicfMACInformation = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87)
)
hpnicfMACInformation.setRevisions(
        ("2007-12-28 19:12",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfMACInfoWorkMode(Integer32, TextualConvention):
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

_HpnicfMACInformationObjects_ObjectIdentity = ObjectIdentity
hpnicfMACInformationObjects = _HpnicfMACInformationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1)
)
_HpnicfMACInformationMibGlobal_ObjectIdentity = ObjectIdentity
hpnicfMACInformationMibGlobal = _HpnicfMACInformationMibGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 1)
)


class _HpnicfMACInformationEnabled_Type(Integer32):
    """Custom type hpnicfMACInformationEnabled based on Integer32"""
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


_HpnicfMACInformationEnabled_Type.__name__ = "Integer32"
_HpnicfMACInformationEnabled_Object = MibScalar
hpnicfMACInformationEnabled = _HpnicfMACInformationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 1, 1),
    _HpnicfMACInformationEnabled_Type()
)
hpnicfMACInformationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMACInformationEnabled.setStatus("current")


class _HpnicfMACInformationcSendInterval_Type(Unsigned32):
    """Custom type hpnicfMACInformationcSendInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_HpnicfMACInformationcSendInterval_Type.__name__ = "Unsigned32"
_HpnicfMACInformationcSendInterval_Object = MibScalar
hpnicfMACInformationcSendInterval = _HpnicfMACInformationcSendInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 1, 2),
    _HpnicfMACInformationcSendInterval_Type()
)
hpnicfMACInformationcSendInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMACInformationcSendInterval.setStatus("current")
_HpnicfMACInformationLearntMACNum_Type = Counter32
_HpnicfMACInformationLearntMACNum_Object = MibScalar
hpnicfMACInformationLearntMACNum = _HpnicfMACInformationLearntMACNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 1, 3),
    _HpnicfMACInformationLearntMACNum_Type()
)
hpnicfMACInformationLearntMACNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMACInformationLearntMACNum.setStatus("current")
_HpnicfMACInformationRemovedMACNum_Type = Counter32
_HpnicfMACInformationRemovedMACNum_Object = MibScalar
hpnicfMACInformationRemovedMACNum = _HpnicfMACInformationRemovedMACNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 1, 4),
    _HpnicfMACInformationRemovedMACNum_Type()
)
hpnicfMACInformationRemovedMACNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMACInformationRemovedMACNum.setStatus("current")
_HpnicfMACInformationTrapSendNum_Type = Counter32
_HpnicfMACInformationTrapSendNum_Object = MibScalar
hpnicfMACInformationTrapSendNum = _HpnicfMACInformationTrapSendNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 1, 5),
    _HpnicfMACInformationTrapSendNum_Type()
)
hpnicfMACInformationTrapSendNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMACInformationTrapSendNum.setStatus("current")
_HpnicfMACInformationSyslogSendNum_Type = Counter32
_HpnicfMACInformationSyslogSendNum_Object = MibScalar
hpnicfMACInformationSyslogSendNum = _HpnicfMACInformationSyslogSendNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 1, 6),
    _HpnicfMACInformationSyslogSendNum_Type()
)
hpnicfMACInformationSyslogSendNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMACInformationSyslogSendNum.setStatus("current")


class _HpnicfMACInformationCacheLen_Type(Unsigned32):
    """Custom type hpnicfMACInformationCacheLen based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HpnicfMACInformationCacheLen_Type.__name__ = "Unsigned32"
_HpnicfMACInformationCacheLen_Object = MibScalar
hpnicfMACInformationCacheLen = _HpnicfMACInformationCacheLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 1, 7),
    _HpnicfMACInformationCacheLen_Type()
)
hpnicfMACInformationCacheLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMACInformationCacheLen.setStatus("current")
_HpnicfMACInfomationWorkMode_Type = HpnicfMACInfoWorkMode
_HpnicfMACInfomationWorkMode_Object = MibScalar
hpnicfMACInfomationWorkMode = _HpnicfMACInfomationWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 1, 8),
    _HpnicfMACInfomationWorkMode_Type()
)
hpnicfMACInfomationWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMACInfomationWorkMode.setStatus("current")
_HpnicfMACInformationMIBTableTroop_ObjectIdentity = ObjectIdentity
hpnicfMACInformationMIBTableTroop = _HpnicfMACInformationMIBTableTroop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 2)
)
_HpnicfMACInfomationIfTable_Object = MibTable
hpnicfMACInfomationIfTable = _HpnicfMACInfomationIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfMACInfomationIfTable.setStatus("current")
_HpnicfMACInfomationIfEntry_Object = MibTableRow
hpnicfMACInfomationIfEntry = _HpnicfMACInfomationIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 2, 1, 1)
)
hpnicfMACInfomationIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMACInfomationIfEntry.setStatus("current")


class _HpnicfMACLearntEnable_Type(Integer32):
    """Custom type hpnicfMACLearntEnable based on Integer32"""
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


_HpnicfMACLearntEnable_Type.__name__ = "Integer32"
_HpnicfMACLearntEnable_Object = MibTableColumn
hpnicfMACLearntEnable = _HpnicfMACLearntEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 2, 1, 1, 1),
    _HpnicfMACLearntEnable_Type()
)
hpnicfMACLearntEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMACLearntEnable.setStatus("current")


class _HpnicfMACRemovedEnable_Type(Integer32):
    """Custom type hpnicfMACRemovedEnable based on Integer32"""
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


_HpnicfMACRemovedEnable_Type.__name__ = "Integer32"
_HpnicfMACRemovedEnable_Object = MibTableColumn
hpnicfMACRemovedEnable = _HpnicfMACRemovedEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 2, 1, 1, 2),
    _HpnicfMACRemovedEnable_Type()
)
hpnicfMACRemovedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMACRemovedEnable.setStatus("current")
_HpnicfMACInformationMibTrap_ObjectIdentity = ObjectIdentity
hpnicfMACInformationMibTrap = _HpnicfMACInformationMibTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 3)
)
_HpnicfMACInformationTraps_ObjectIdentity = ObjectIdentity
hpnicfMACInformationTraps = _HpnicfMACInformationTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 3, 0)
)
_HpnicfMACInformationTrapObjects_ObjectIdentity = ObjectIdentity
hpnicfMACInformationTrapObjects = _HpnicfMACInformationTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 3, 2)
)


class _HpnicfMACInfoTrapIndex_Type(Unsigned32):
    """Custom type hpnicfMACInfoTrapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfMACInfoTrapIndex_Type.__name__ = "Unsigned32"
_HpnicfMACInfoTrapIndex_Object = MibScalar
hpnicfMACInfoTrapIndex = _HpnicfMACInfoTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 3, 2, 1),
    _HpnicfMACInfoTrapIndex_Type()
)
hpnicfMACInfoTrapIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfMACInfoTrapIndex.setStatus("current")
_HpnicfMACInfoTrapCount_Type = Unsigned32
_HpnicfMACInfoTrapCount_Object = MibScalar
hpnicfMACInfoTrapCount = _HpnicfMACInfoTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 3, 2, 2),
    _HpnicfMACInfoTrapCount_Type()
)
hpnicfMACInfoTrapCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfMACInfoTrapCount.setStatus("current")


class _HpnicfMACInfoTrapMsg_Type(OctetString):
    """Custom type hpnicfMACInfoTrapMsg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 254),
    )


_HpnicfMACInfoTrapMsg_Type.__name__ = "OctetString"
_HpnicfMACInfoTrapMsg_Object = MibScalar
hpnicfMACInfoTrapMsg = _HpnicfMACInfoTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 3, 2, 3),
    _HpnicfMACInfoTrapMsg_Type()
)
hpnicfMACInfoTrapMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfMACInfoTrapMsg.setStatus("current")
_HpnicfMACInformationMibTrapExt_ObjectIdentity = ObjectIdentity
hpnicfMACInformationMibTrapExt = _HpnicfMACInformationMibTrapExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 4)
)
_HpnicfMACInformationTrapsExt_ObjectIdentity = ObjectIdentity
hpnicfMACInformationTrapsExt = _HpnicfMACInformationTrapsExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 4, 0)
)
_HpnicfMACInformationTrapObjectsExt_ObjectIdentity = ObjectIdentity
hpnicfMACInformationTrapObjectsExt = _HpnicfMACInformationTrapObjectsExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 4, 2)
)
_HpnicfMACInfoTrapVerExt_Type = Unsigned32
_HpnicfMACInfoTrapVerExt_Object = MibScalar
hpnicfMACInfoTrapVerExt = _HpnicfMACInfoTrapVerExt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 4, 2, 1),
    _HpnicfMACInfoTrapVerExt_Type()
)
hpnicfMACInfoTrapVerExt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfMACInfoTrapVerExt.setStatus("current")


class _HpnicfMACInfoTrapIndexExt_Type(Unsigned32):
    """Custom type hpnicfMACInfoTrapIndexExt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfMACInfoTrapIndexExt_Type.__name__ = "Unsigned32"
_HpnicfMACInfoTrapIndexExt_Object = MibScalar
hpnicfMACInfoTrapIndexExt = _HpnicfMACInfoTrapIndexExt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 4, 2, 2),
    _HpnicfMACInfoTrapIndexExt_Type()
)
hpnicfMACInfoTrapIndexExt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfMACInfoTrapIndexExt.setStatus("current")
_HpnicfMACInfoTrapCountExt_Type = Unsigned32
_HpnicfMACInfoTrapCountExt_Object = MibScalar
hpnicfMACInfoTrapCountExt = _HpnicfMACInfoTrapCountExt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 4, 2, 3),
    _HpnicfMACInfoTrapCountExt_Type()
)
hpnicfMACInfoTrapCountExt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfMACInfoTrapCountExt.setStatus("current")


class _HpnicfMACInfoTrapMsgExt_Type(OctetString):
    """Custom type hpnicfMACInfoTrapMsgExt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 254),
    )


_HpnicfMACInfoTrapMsgExt_Type.__name__ = "OctetString"
_HpnicfMACInfoTrapMsgExt_Object = MibScalar
hpnicfMACInfoTrapMsgExt = _HpnicfMACInfoTrapMsgExt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 4, 2, 4),
    _HpnicfMACInfoTrapMsgExt_Type()
)
hpnicfMACInfoTrapMsgExt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfMACInfoTrapMsgExt.setStatus("current")
_HpnicfMACInfoTrapMsgMovedAddress_Type = MacAddress
_HpnicfMACInfoTrapMsgMovedAddress_Object = MibScalar
hpnicfMACInfoTrapMsgMovedAddress = _HpnicfMACInfoTrapMsgMovedAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 4, 2, 5),
    _HpnicfMACInfoTrapMsgMovedAddress_Type()
)
hpnicfMACInfoTrapMsgMovedAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfMACInfoTrapMsgMovedAddress.setStatus("current")


class _HpnicfMACInfoTrapMsgMovedVlan_Type(Integer32):
    """Custom type hpnicfMACInfoTrapMsgMovedVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpnicfMACInfoTrapMsgMovedVlan_Type.__name__ = "Integer32"
_HpnicfMACInfoTrapMsgMovedVlan_Object = MibScalar
hpnicfMACInfoTrapMsgMovedVlan = _HpnicfMACInfoTrapMsgMovedVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 4, 2, 6),
    _HpnicfMACInfoTrapMsgMovedVlan_Type()
)
hpnicfMACInfoTrapMsgMovedVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfMACInfoTrapMsgMovedVlan.setStatus("current")


class _HpnicfMACInfoTrapMsgMovedFromIf_Type(Integer32):
    """Custom type hpnicfMACInfoTrapMsgMovedFromIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfMACInfoTrapMsgMovedFromIf_Type.__name__ = "Integer32"
_HpnicfMACInfoTrapMsgMovedFromIf_Object = MibScalar
hpnicfMACInfoTrapMsgMovedFromIf = _HpnicfMACInfoTrapMsgMovedFromIf_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 4, 2, 7),
    _HpnicfMACInfoTrapMsgMovedFromIf_Type()
)
hpnicfMACInfoTrapMsgMovedFromIf.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfMACInfoTrapMsgMovedFromIf.setStatus("current")


class _HpnicfMACInfoTrapMsgMovedToIf_Type(Integer32):
    """Custom type hpnicfMACInfoTrapMsgMovedToIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfMACInfoTrapMsgMovedToIf_Type.__name__ = "Integer32"
_HpnicfMACInfoTrapMsgMovedToIf_Object = MibScalar
hpnicfMACInfoTrapMsgMovedToIf = _HpnicfMACInfoTrapMsgMovedToIf_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 4, 2, 8),
    _HpnicfMACInfoTrapMsgMovedToIf_Type()
)
hpnicfMACInfoTrapMsgMovedToIf.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfMACInfoTrapMsgMovedToIf.setStatus("current")
_HpnicfMACInfoTrapMsgMovedCount_Type = Counter32
_HpnicfMACInfoTrapMsgMovedCount_Object = MibScalar
hpnicfMACInfoTrapMsgMovedCount = _HpnicfMACInfoTrapMsgMovedCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 4, 2, 9),
    _HpnicfMACInfoTrapMsgMovedCount_Type()
)
hpnicfMACInfoTrapMsgMovedCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfMACInfoTrapMsgMovedCount.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfMACInformationChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 3, 0, 1)
)
hpnicfMACInformationChangedTrap.setObjects(
      *(("HPN-ICF-MAC-INFORMATION-MIB", "hpnicfMACInfoTrapIndex"),
        ("HPN-ICF-MAC-INFORMATION-MIB", "hpnicfMACInfoTrapCount"),
        ("HPN-ICF-MAC-INFORMATION-MIB", "hpnicfMACInfoTrapMsg"))
)
if mibBuilder.loadTexts:
    hpnicfMACInformationChangedTrap.setStatus(
        "current"
    )

hpnicfMACInformationChangedTrapExt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 4, 0, 1)
)
hpnicfMACInformationChangedTrapExt.setObjects(
      *(("HPN-ICF-MAC-INFORMATION-MIB", "hpnicfMACInfoTrapVerExt"),
        ("HPN-ICF-MAC-INFORMATION-MIB", "hpnicfMACInfoTrapIndexExt"),
        ("HPN-ICF-MAC-INFORMATION-MIB", "hpnicfMACInfoTrapCountExt"),
        ("HPN-ICF-MAC-INFORMATION-MIB", "hpnicfMACInfoTrapMsgExt"))
)
if mibBuilder.loadTexts:
    hpnicfMACInformationChangedTrapExt.setStatus(
        "current"
    )

hpnicfMACInformationMovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87, 1, 4, 0, 2)
)
hpnicfMACInformationMovedTrap.setObjects(
      *(("HPN-ICF-MAC-INFORMATION-MIB", "hpnicfMACInfoTrapMsgMovedAddress"),
        ("HPN-ICF-MAC-INFORMATION-MIB", "hpnicfMACInfoTrapMsgMovedVlan"),
        ("HPN-ICF-MAC-INFORMATION-MIB", "hpnicfMACInfoTrapMsgMovedFromIf"),
        ("HPN-ICF-MAC-INFORMATION-MIB", "hpnicfMACInfoTrapMsgMovedToIf"),
        ("HPN-ICF-MAC-INFORMATION-MIB", "hpnicfMACInfoTrapMsgMovedCount"))
)
if mibBuilder.loadTexts:
    hpnicfMACInformationMovedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-MAC-INFORMATION-MIB",
    **{"HpnicfMACInfoWorkMode": HpnicfMACInfoWorkMode,
       "hpnicfMACInformation": hpnicfMACInformation,
       "hpnicfMACInformationObjects": hpnicfMACInformationObjects,
       "hpnicfMACInformationMibGlobal": hpnicfMACInformationMibGlobal,
       "hpnicfMACInformationEnabled": hpnicfMACInformationEnabled,
       "hpnicfMACInformationcSendInterval": hpnicfMACInformationcSendInterval,
       "hpnicfMACInformationLearntMACNum": hpnicfMACInformationLearntMACNum,
       "hpnicfMACInformationRemovedMACNum": hpnicfMACInformationRemovedMACNum,
       "hpnicfMACInformationTrapSendNum": hpnicfMACInformationTrapSendNum,
       "hpnicfMACInformationSyslogSendNum": hpnicfMACInformationSyslogSendNum,
       "hpnicfMACInformationCacheLen": hpnicfMACInformationCacheLen,
       "hpnicfMACInfomationWorkMode": hpnicfMACInfomationWorkMode,
       "hpnicfMACInformationMIBTableTroop": hpnicfMACInformationMIBTableTroop,
       "hpnicfMACInfomationIfTable": hpnicfMACInfomationIfTable,
       "hpnicfMACInfomationIfEntry": hpnicfMACInfomationIfEntry,
       "hpnicfMACLearntEnable": hpnicfMACLearntEnable,
       "hpnicfMACRemovedEnable": hpnicfMACRemovedEnable,
       "hpnicfMACInformationMibTrap": hpnicfMACInformationMibTrap,
       "hpnicfMACInformationTraps": hpnicfMACInformationTraps,
       "hpnicfMACInformationChangedTrap": hpnicfMACInformationChangedTrap,
       "hpnicfMACInformationTrapObjects": hpnicfMACInformationTrapObjects,
       "hpnicfMACInfoTrapIndex": hpnicfMACInfoTrapIndex,
       "hpnicfMACInfoTrapCount": hpnicfMACInfoTrapCount,
       "hpnicfMACInfoTrapMsg": hpnicfMACInfoTrapMsg,
       "hpnicfMACInformationMibTrapExt": hpnicfMACInformationMibTrapExt,
       "hpnicfMACInformationTrapsExt": hpnicfMACInformationTrapsExt,
       "hpnicfMACInformationChangedTrapExt": hpnicfMACInformationChangedTrapExt,
       "hpnicfMACInformationMovedTrap": hpnicfMACInformationMovedTrap,
       "hpnicfMACInformationTrapObjectsExt": hpnicfMACInformationTrapObjectsExt,
       "hpnicfMACInfoTrapVerExt": hpnicfMACInfoTrapVerExt,
       "hpnicfMACInfoTrapIndexExt": hpnicfMACInfoTrapIndexExt,
       "hpnicfMACInfoTrapCountExt": hpnicfMACInfoTrapCountExt,
       "hpnicfMACInfoTrapMsgExt": hpnicfMACInfoTrapMsgExt,
       "hpnicfMACInfoTrapMsgMovedAddress": hpnicfMACInfoTrapMsgMovedAddress,
       "hpnicfMACInfoTrapMsgMovedVlan": hpnicfMACInfoTrapMsgMovedVlan,
       "hpnicfMACInfoTrapMsgMovedFromIf": hpnicfMACInfoTrapMsgMovedFromIf,
       "hpnicfMACInfoTrapMsgMovedToIf": hpnicfMACInfoTrapMsgMovedToIf,
       "hpnicfMACInfoTrapMsgMovedCount": hpnicfMACInfoTrapMsgMovedCount}
)
