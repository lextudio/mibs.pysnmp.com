# SNMP MIB module (TPLINK-8021X-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-8021X-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:44 2024
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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")


# MODULE-IDENTITY

tplink8021xMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31)
)
tplink8021xMIB.setRevisions(
        ("2012-12-17 10:50",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tplink8021xMIBObjects_ObjectIdentity = ObjectIdentity
tplink8021xMIBObjects = _Tplink8021xMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1)
)
_Tp8021xGlobalConfig_ObjectIdentity = ObjectIdentity
tp8021xGlobalConfig = _Tp8021xGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1)
)


class _Tp8021xGlobalEnable_Type(Integer32):
    """Custom type tp8021xGlobalEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Tp8021xGlobalEnable_Type.__name__ = "Integer32"
_Tp8021xGlobalEnable_Object = MibScalar
tp8021xGlobalEnable = _Tp8021xGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 1),
    _Tp8021xGlobalEnable_Type()
)
tp8021xGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp8021xGlobalEnable.setStatus("current")


class _Tp8021xAuthMode_Type(Integer32):
    """Custom type tp8021xAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eap", 1),
          ("pap", 0))
    )


_Tp8021xAuthMode_Type.__name__ = "Integer32"
_Tp8021xAuthMode_Object = MibScalar
tp8021xAuthMode = _Tp8021xAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 2),
    _Tp8021xAuthMode_Type()
)
tp8021xAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp8021xAuthMode.setStatus("current")


class _Tp8021xHandshake_Type(Integer32):
    """Custom type tp8021xHandshake based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Tp8021xHandshake_Type.__name__ = "Integer32"
_Tp8021xHandshake_Object = MibScalar
tp8021xHandshake = _Tp8021xHandshake_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 3),
    _Tp8021xHandshake_Type()
)
tp8021xHandshake.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp8021xHandshake.setStatus("current")


class _Tp8021xGuestVlanEnable_Type(Integer32):
    """Custom type tp8021xGuestVlanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Tp8021xGuestVlanEnable_Type.__name__ = "Integer32"
_Tp8021xGuestVlanEnable_Object = MibScalar
tp8021xGuestVlanEnable = _Tp8021xGuestVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 4),
    _Tp8021xGuestVlanEnable_Type()
)
tp8021xGuestVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp8021xGuestVlanEnable.setStatus("current")
_Tp8021xGuestVlanID_Type = Integer32
_Tp8021xGuestVlanID_Object = MibScalar
tp8021xGuestVlanID = _Tp8021xGuestVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 5),
    _Tp8021xGuestVlanID_Type()
)
tp8021xGuestVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp8021xGuestVlanID.setStatus("current")


class _Tp8021xQuietEnable_Type(Integer32):
    """Custom type tp8021xQuietEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Tp8021xQuietEnable_Type.__name__ = "Integer32"
_Tp8021xQuietEnable_Object = MibScalar
tp8021xQuietEnable = _Tp8021xQuietEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 6),
    _Tp8021xQuietEnable_Type()
)
tp8021xQuietEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp8021xQuietEnable.setStatus("current")
_Tp8021xQuietPeriod_Type = Integer32
_Tp8021xQuietPeriod_Object = MibScalar
tp8021xQuietPeriod = _Tp8021xQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 7),
    _Tp8021xQuietPeriod_Type()
)
tp8021xQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp8021xQuietPeriod.setStatus("current")
_Tp8021xRetryTimes_Type = Integer32
_Tp8021xRetryTimes_Object = MibScalar
tp8021xRetryTimes = _Tp8021xRetryTimes_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 8),
    _Tp8021xRetryTimes_Type()
)
tp8021xRetryTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp8021xRetryTimes.setStatus("current")
_Tp8021xSupplicantTimeOut_Type = Integer32
_Tp8021xSupplicantTimeOut_Object = MibScalar
tp8021xSupplicantTimeOut = _Tp8021xSupplicantTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 9),
    _Tp8021xSupplicantTimeOut_Type()
)
tp8021xSupplicantTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp8021xSupplicantTimeOut.setStatus("current")
_Tp8021xServerTimeOut_Type = Integer32
_Tp8021xServerTimeOut_Object = MibScalar
tp8021xServerTimeOut = _Tp8021xServerTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 10),
    _Tp8021xServerTimeOut_Type()
)
tp8021xServerTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp8021xServerTimeOut.setStatus("current")
_Tp8021xAuthPrimaryIP_Type = IpAddress
_Tp8021xAuthPrimaryIP_Object = MibScalar
tp8021xAuthPrimaryIP = _Tp8021xAuthPrimaryIP_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 11),
    _Tp8021xAuthPrimaryIP_Type()
)
tp8021xAuthPrimaryIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp8021xAuthPrimaryIP.setStatus("current")
_Tp8021xAuthSecondaryIP_Type = IpAddress
_Tp8021xAuthSecondaryIP_Object = MibScalar
tp8021xAuthSecondaryIP = _Tp8021xAuthSecondaryIP_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 12),
    _Tp8021xAuthSecondaryIP_Type()
)
tp8021xAuthSecondaryIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp8021xAuthSecondaryIP.setStatus("current")
_Tp8021xServerAuthPort_Type = Integer32
_Tp8021xServerAuthPort_Object = MibScalar
tp8021xServerAuthPort = _Tp8021xServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 13),
    _Tp8021xServerAuthPort_Type()
)
tp8021xServerAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp8021xServerAuthPort.setStatus("current")


class _Tp8021xServerAuthKey_Type(OctetString):
    """Custom type tp8021xServerAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Tp8021xServerAuthKey_Type.__name__ = "OctetString"
_Tp8021xServerAuthKey_Object = MibScalar
tp8021xServerAuthKey = _Tp8021xServerAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 14),
    _Tp8021xServerAuthKey_Type()
)
tp8021xServerAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp8021xServerAuthKey.setStatus("current")


class _Tp8021xAcctEnable_Type(Integer32):
    """Custom type tp8021xAcctEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Tp8021xAcctEnable_Type.__name__ = "Integer32"
_Tp8021xAcctEnable_Object = MibScalar
tp8021xAcctEnable = _Tp8021xAcctEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 15),
    _Tp8021xAcctEnable_Type()
)
tp8021xAcctEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp8021xAcctEnable.setStatus("current")
_Tp8021xAcctPrimaryIP_Type = IpAddress
_Tp8021xAcctPrimaryIP_Object = MibScalar
tp8021xAcctPrimaryIP = _Tp8021xAcctPrimaryIP_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 16),
    _Tp8021xAcctPrimaryIP_Type()
)
tp8021xAcctPrimaryIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp8021xAcctPrimaryIP.setStatus("current")
_Tp8021xAcctSecondaryIP_Type = IpAddress
_Tp8021xAcctSecondaryIP_Object = MibScalar
tp8021xAcctSecondaryIP = _Tp8021xAcctSecondaryIP_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 17),
    _Tp8021xAcctSecondaryIP_Type()
)
tp8021xAcctSecondaryIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp8021xAcctSecondaryIP.setStatus("current")
_Tp8021xAcctPort_Type = Integer32
_Tp8021xAcctPort_Object = MibScalar
tp8021xAcctPort = _Tp8021xAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 18),
    _Tp8021xAcctPort_Type()
)
tp8021xAcctPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp8021xAcctPort.setStatus("current")


class _Tp8021xAcctKey_Type(OctetString):
    """Custom type tp8021xAcctKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Tp8021xAcctKey_Type.__name__ = "OctetString"
_Tp8021xAcctKey_Object = MibScalar
tp8021xAcctKey = _Tp8021xAcctKey_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 1, 19),
    _Tp8021xAcctKey_Type()
)
tp8021xAcctKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp8021xAcctKey.setStatus("current")
_Tp8021xPortConfig_ObjectIdentity = ObjectIdentity
tp8021xPortConfig = _Tp8021xPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 2)
)
_Tp8021xPortConfigTable_Object = MibTable
tp8021xPortConfigTable = _Tp8021xPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tp8021xPortConfigTable.setStatus("current")
_Tp8021xPortConfigEntry_Object = MibTableRow
tp8021xPortConfigEntry = _Tp8021xPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 2, 1, 1)
)
tp8021xPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tp8021xPortConfigEntry.setStatus("current")


class _Tp8021xPortConfigPortIndex_Type(DisplayString):
    """Custom type tp8021xPortConfigPortIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Tp8021xPortConfigPortIndex_Type.__name__ = "DisplayString"
_Tp8021xPortConfigPortIndex_Object = MibTableColumn
tp8021xPortConfigPortIndex = _Tp8021xPortConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 2, 1, 1, 1),
    _Tp8021xPortConfigPortIndex_Type()
)
tp8021xPortConfigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp8021xPortConfigPortIndex.setStatus("current")


class _Tp8021xPortConfigEnable_Type(Integer32):
    """Custom type tp8021xPortConfigEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Tp8021xPortConfigEnable_Type.__name__ = "Integer32"
_Tp8021xPortConfigEnable_Object = MibTableColumn
tp8021xPortConfigEnable = _Tp8021xPortConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 2, 1, 1, 2),
    _Tp8021xPortConfigEnable_Type()
)
tp8021xPortConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp8021xPortConfigEnable.setStatus("current")


class _Tp8021xPortConfigGuestVlanEnable_Type(Integer32):
    """Custom type tp8021xPortConfigGuestVlanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Tp8021xPortConfigGuestVlanEnable_Type.__name__ = "Integer32"
_Tp8021xPortConfigGuestVlanEnable_Object = MibTableColumn
tp8021xPortConfigGuestVlanEnable = _Tp8021xPortConfigGuestVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 2, 1, 1, 3),
    _Tp8021xPortConfigGuestVlanEnable_Type()
)
tp8021xPortConfigGuestVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp8021xPortConfigGuestVlanEnable.setStatus("current")


class _Tp8021xPortConfigControlMode_Type(Integer32):
    """Custom type tp8021xPortConfigControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoAuth", 2),
          ("forceAuth", 0),
          ("forceUnAuth", 1))
    )


_Tp8021xPortConfigControlMode_Type.__name__ = "Integer32"
_Tp8021xPortConfigControlMode_Object = MibTableColumn
tp8021xPortConfigControlMode = _Tp8021xPortConfigControlMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 2, 1, 1, 4),
    _Tp8021xPortConfigControlMode_Type()
)
tp8021xPortConfigControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp8021xPortConfigControlMode.setStatus("current")


class _Tp8021xPortConfigControlType_Type(Integer32):
    """Custom type tp8021xPortConfigControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("macBased", 0),
          ("portBased", 1))
    )


_Tp8021xPortConfigControlType_Type.__name__ = "Integer32"
_Tp8021xPortConfigControlType_Object = MibTableColumn
tp8021xPortConfigControlType = _Tp8021xPortConfigControlType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 2, 1, 1, 5),
    _Tp8021xPortConfigControlType_Type()
)
tp8021xPortConfigControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp8021xPortConfigControlType.setStatus("current")


class _Tp8021xPortConfigAuthState_Type(Integer32):
    """Custom type tp8021xPortConfigAuthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("authorized", 1),
          ("unAuthorized", 0))
    )


_Tp8021xPortConfigAuthState_Type.__name__ = "Integer32"
_Tp8021xPortConfigAuthState_Object = MibTableColumn
tp8021xPortConfigAuthState = _Tp8021xPortConfigAuthState_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 2, 1, 1, 6),
    _Tp8021xPortConfigAuthState_Type()
)
tp8021xPortConfigAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp8021xPortConfigAuthState.setStatus("current")


class _Tp8021xPortConfigPortLag_Type(OctetString):
    """Custom type tp8021xPortConfigPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Tp8021xPortConfigPortLag_Type.__name__ = "OctetString"
_Tp8021xPortConfigPortLag_Object = MibTableColumn
tp8021xPortConfigPortLag = _Tp8021xPortConfigPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 1, 2, 1, 1, 7),
    _Tp8021xPortConfigPortLag_Type()
)
tp8021xPortConfigPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp8021xPortConfigPortLag.setStatus("current")
_Tplink8021xNotifications_ObjectIdentity = ObjectIdentity
tplink8021xNotifications = _Tplink8021xNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 31, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-8021X-MIB",
    **{"tplink8021xMIB": tplink8021xMIB,
       "tplink8021xMIBObjects": tplink8021xMIBObjects,
       "tp8021xGlobalConfig": tp8021xGlobalConfig,
       "tp8021xGlobalEnable": tp8021xGlobalEnable,
       "tp8021xAuthMode": tp8021xAuthMode,
       "tp8021xHandshake": tp8021xHandshake,
       "tp8021xGuestVlanEnable": tp8021xGuestVlanEnable,
       "tp8021xGuestVlanID": tp8021xGuestVlanID,
       "tp8021xQuietEnable": tp8021xQuietEnable,
       "tp8021xQuietPeriod": tp8021xQuietPeriod,
       "tp8021xRetryTimes": tp8021xRetryTimes,
       "tp8021xSupplicantTimeOut": tp8021xSupplicantTimeOut,
       "tp8021xServerTimeOut": tp8021xServerTimeOut,
       "tp8021xAuthPrimaryIP": tp8021xAuthPrimaryIP,
       "tp8021xAuthSecondaryIP": tp8021xAuthSecondaryIP,
       "tp8021xServerAuthPort": tp8021xServerAuthPort,
       "tp8021xServerAuthKey": tp8021xServerAuthKey,
       "tp8021xAcctEnable": tp8021xAcctEnable,
       "tp8021xAcctPrimaryIP": tp8021xAcctPrimaryIP,
       "tp8021xAcctSecondaryIP": tp8021xAcctSecondaryIP,
       "tp8021xAcctPort": tp8021xAcctPort,
       "tp8021xAcctKey": tp8021xAcctKey,
       "tp8021xPortConfig": tp8021xPortConfig,
       "tp8021xPortConfigTable": tp8021xPortConfigTable,
       "tp8021xPortConfigEntry": tp8021xPortConfigEntry,
       "tp8021xPortConfigPortIndex": tp8021xPortConfigPortIndex,
       "tp8021xPortConfigEnable": tp8021xPortConfigEnable,
       "tp8021xPortConfigGuestVlanEnable": tp8021xPortConfigGuestVlanEnable,
       "tp8021xPortConfigControlMode": tp8021xPortConfigControlMode,
       "tp8021xPortConfigControlType": tp8021xPortConfigControlType,
       "tp8021xPortConfigAuthState": tp8021xPortConfigAuthState,
       "tp8021xPortConfigPortLag": tp8021xPortConfigPortLag,
       "tplink8021xNotifications": tplink8021xNotifications}
)
