# SNMP MIB module (SIP-UA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SIP-UA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:52:27 2024
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

(applIndex,) = mibBuilder.importSymbols(
    "NETWORK-SERVICES-MIB",
    "applIndex")

(sipMIB,) = mibBuilder.importSymbols(
    "SIP-MIB-SMI",
    "sipMIB")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

sipUAMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SipUACfg_ObjectIdentity = ObjectIdentity
sipUACfg = _SipUACfg_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 3, 1)
)
_SipUACfgTimer_ObjectIdentity = ObjectIdentity
sipUACfgTimer = _SipUACfgTimer_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 3, 1, 1)
)
_SipUACfgTimerTable_Object = MibTable
sipUACfgTimerTable = _SipUACfgTimerTable_Object(
    (1, 3, 6, 1, 2, 1, 9998, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    sipUACfgTimerTable.setStatus("current")
_SipUACfgTimerEntry_Object = MibTableRow
sipUACfgTimerEntry = _SipUACfgTimerEntry_Object(
    (1, 3, 6, 1, 2, 1, 9998, 3, 1, 1, 1, 1)
)
sipUACfgTimerEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    sipUACfgTimerEntry.setStatus("current")


class _SipUACfgTimerTrying_Type(Integer32):
    """Custom type sipUACfgTimerTrying based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_SipUACfgTimerTrying_Type.__name__ = "Integer32"
_SipUACfgTimerTrying_Object = MibTableColumn
sipUACfgTimerTrying = _SipUACfgTimerTrying_Object(
    (1, 3, 6, 1, 2, 1, 9998, 3, 1, 1, 1, 1, 1),
    _SipUACfgTimerTrying_Type()
)
sipUACfgTimerTrying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipUACfgTimerTrying.setStatus("current")
if mibBuilder.loadTexts:
    sipUACfgTimerTrying.setUnits("milliseconds")


class _SipUACfgTimerProv_Type(Integer32):
    """Custom type sipUACfgTimerProv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60000, 300000),
    )


_SipUACfgTimerProv_Type.__name__ = "Integer32"
_SipUACfgTimerProv_Object = MibTableColumn
sipUACfgTimerProv = _SipUACfgTimerProv_Object(
    (1, 3, 6, 1, 2, 1, 9998, 3, 1, 1, 1, 1, 2),
    _SipUACfgTimerProv_Type()
)
sipUACfgTimerProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipUACfgTimerProv.setStatus("current")
if mibBuilder.loadTexts:
    sipUACfgTimerProv.setUnits("milliseconds")


class _SipUACfgTimerAck_Type(Integer32):
    """Custom type sipUACfgTimerAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_SipUACfgTimerAck_Type.__name__ = "Integer32"
_SipUACfgTimerAck_Object = MibTableColumn
sipUACfgTimerAck = _SipUACfgTimerAck_Object(
    (1, 3, 6, 1, 2, 1, 9998, 3, 1, 1, 1, 1, 3),
    _SipUACfgTimerAck_Type()
)
sipUACfgTimerAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipUACfgTimerAck.setStatus("current")
if mibBuilder.loadTexts:
    sipUACfgTimerAck.setUnits("milliseconds")


class _SipUACfgTimerDisconnect_Type(Integer32):
    """Custom type sipUACfgTimerDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_SipUACfgTimerDisconnect_Type.__name__ = "Integer32"
_SipUACfgTimerDisconnect_Object = MibTableColumn
sipUACfgTimerDisconnect = _SipUACfgTimerDisconnect_Object(
    (1, 3, 6, 1, 2, 1, 9998, 3, 1, 1, 1, 1, 4),
    _SipUACfgTimerDisconnect_Type()
)
sipUACfgTimerDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipUACfgTimerDisconnect.setStatus("current")
if mibBuilder.loadTexts:
    sipUACfgTimerDisconnect.setUnits("milliseconds")


class _SipUACfgTimerReRegister_Type(Integer32):
    """Custom type sipUACfgTimerReRegister based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SipUACfgTimerReRegister_Type.__name__ = "Integer32"
_SipUACfgTimerReRegister_Object = MibTableColumn
sipUACfgTimerReRegister = _SipUACfgTimerReRegister_Object(
    (1, 3, 6, 1, 2, 1, 9998, 3, 1, 1, 1, 1, 5),
    _SipUACfgTimerReRegister_Type()
)
sipUACfgTimerReRegister.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipUACfgTimerReRegister.setStatus("current")
if mibBuilder.loadTexts:
    sipUACfgTimerReRegister.setUnits("seconds")
_SipUACfgRetry_ObjectIdentity = ObjectIdentity
sipUACfgRetry = _SipUACfgRetry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 3, 1, 2)
)
_SipUACfgRetryTable_Object = MibTable
sipUACfgRetryTable = _SipUACfgRetryTable_Object(
    (1, 3, 6, 1, 2, 1, 9998, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sipUACfgRetryTable.setStatus("current")
_SipUACfgRetryEntry_Object = MibTableRow
sipUACfgRetryEntry = _SipUACfgRetryEntry_Object(
    (1, 3, 6, 1, 2, 1, 9998, 3, 1, 2, 1, 1)
)
sipUACfgRetryEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    sipUACfgRetryEntry.setStatus("current")


class _SipUACfgRetryInvite_Type(Integer32):
    """Custom type sipUACfgRetryInvite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SipUACfgRetryInvite_Type.__name__ = "Integer32"
_SipUACfgRetryInvite_Object = MibTableColumn
sipUACfgRetryInvite = _SipUACfgRetryInvite_Object(
    (1, 3, 6, 1, 2, 1, 9998, 3, 1, 2, 1, 1, 1),
    _SipUACfgRetryInvite_Type()
)
sipUACfgRetryInvite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipUACfgRetryInvite.setStatus("current")


class _SipUACfgRetryBye_Type(Integer32):
    """Custom type sipUACfgRetryBye based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SipUACfgRetryBye_Type.__name__ = "Integer32"
_SipUACfgRetryBye_Object = MibTableColumn
sipUACfgRetryBye = _SipUACfgRetryBye_Object(
    (1, 3, 6, 1, 2, 1, 9998, 3, 1, 2, 1, 1, 2),
    _SipUACfgRetryBye_Type()
)
sipUACfgRetryBye.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipUACfgRetryBye.setStatus("current")


class _SipUACfgRetryCancel_Type(Integer32):
    """Custom type sipUACfgRetryCancel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SipUACfgRetryCancel_Type.__name__ = "Integer32"
_SipUACfgRetryCancel_Object = MibTableColumn
sipUACfgRetryCancel = _SipUACfgRetryCancel_Object(
    (1, 3, 6, 1, 2, 1, 9998, 3, 1, 2, 1, 1, 3),
    _SipUACfgRetryCancel_Type()
)
sipUACfgRetryCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipUACfgRetryCancel.setStatus("current")


class _SipUACfgRetryRegister_Type(Integer32):
    """Custom type sipUACfgRetryRegister based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SipUACfgRetryRegister_Type.__name__ = "Integer32"
_SipUACfgRetryRegister_Object = MibTableColumn
sipUACfgRetryRegister = _SipUACfgRetryRegister_Object(
    (1, 3, 6, 1, 2, 1, 9998, 3, 1, 2, 1, 1, 4),
    _SipUACfgRetryRegister_Type()
)
sipUACfgRetryRegister.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipUACfgRetryRegister.setStatus("current")


class _SipUACfgRetryResponse_Type(Integer32):
    """Custom type sipUACfgRetryResponse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SipUACfgRetryResponse_Type.__name__ = "Integer32"
_SipUACfgRetryResponse_Object = MibTableColumn
sipUACfgRetryResponse = _SipUACfgRetryResponse_Object(
    (1, 3, 6, 1, 2, 1, 9998, 3, 1, 2, 1, 1, 5),
    _SipUACfgRetryResponse_Type()
)
sipUACfgRetryResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipUACfgRetryResponse.setStatus("current")
_SipUAStats_ObjectIdentity = ObjectIdentity
sipUAStats = _SipUAStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 3, 2)
)
_SipUAStatsRetry_ObjectIdentity = ObjectIdentity
sipUAStatsRetry = _SipUAStatsRetry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 3, 2, 1)
)
_SipUAStatsRetryTable_Object = MibTable
sipUAStatsRetryTable = _SipUAStatsRetryTable_Object(
    (1, 3, 6, 1, 2, 1, 9998, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sipUAStatsRetryTable.setStatus("current")
_SipUAStatsRetryEntry_Object = MibTableRow
sipUAStatsRetryEntry = _SipUAStatsRetryEntry_Object(
    (1, 3, 6, 1, 2, 1, 9998, 3, 2, 1, 1, 1)
)
sipUAStatsRetryEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    sipUAStatsRetryEntry.setStatus("current")
_SipStatsRetryInvites_Type = Counter32
_SipStatsRetryInvites_Object = MibTableColumn
sipStatsRetryInvites = _SipStatsRetryInvites_Object(
    (1, 3, 6, 1, 2, 1, 9998, 3, 2, 1, 1, 1, 1),
    _SipStatsRetryInvites_Type()
)
sipStatsRetryInvites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsRetryInvites.setStatus("current")
_SipStatsRetryByes_Type = Counter32
_SipStatsRetryByes_Object = MibTableColumn
sipStatsRetryByes = _SipStatsRetryByes_Object(
    (1, 3, 6, 1, 2, 1, 9998, 3, 2, 1, 1, 1, 2),
    _SipStatsRetryByes_Type()
)
sipStatsRetryByes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsRetryByes.setStatus("current")
_SipStatsRetryCancels_Type = Counter32
_SipStatsRetryCancels_Object = MibTableColumn
sipStatsRetryCancels = _SipStatsRetryCancels_Object(
    (1, 3, 6, 1, 2, 1, 9998, 3, 2, 1, 1, 1, 3),
    _SipStatsRetryCancels_Type()
)
sipStatsRetryCancels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsRetryCancels.setStatus("current")
_SipStatsRetryRegisters_Type = Counter32
_SipStatsRetryRegisters_Object = MibTableColumn
sipStatsRetryRegisters = _SipStatsRetryRegisters_Object(
    (1, 3, 6, 1, 2, 1, 9998, 3, 2, 1, 1, 1, 4),
    _SipStatsRetryRegisters_Type()
)
sipStatsRetryRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsRetryRegisters.setStatus("current")
_SipStatsRetryResponses_Type = Counter32
_SipStatsRetryResponses_Object = MibTableColumn
sipStatsRetryResponses = _SipStatsRetryResponses_Object(
    (1, 3, 6, 1, 2, 1, 9998, 3, 2, 1, 1, 1, 5),
    _SipStatsRetryResponses_Type()
)
sipStatsRetryResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipStatsRetryResponses.setStatus("current")
_SipUAMIBNotif_ObjectIdentity = ObjectIdentity
sipUAMIBNotif = _SipUAMIBNotif_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 3, 3)
)
_SipUAMIBConformance_ObjectIdentity = ObjectIdentity
sipUAMIBConformance = _SipUAMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 3, 4)
)
_SipUAMIBCompliances_ObjectIdentity = ObjectIdentity
sipUAMIBCompliances = _SipUAMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 3, 4, 1)
)
_SipUAMIBGroups_ObjectIdentity = ObjectIdentity
sipUAMIBGroups = _SipUAMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 9998, 3, 4, 2)
)

# Managed Objects groups

sipUAConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 9998, 3, 4, 2, 1)
)
sipUAConfigGroup.setObjects(
      *(("SIP-UA-MIB", "sipUACfgTimerTrying"),
        ("SIP-UA-MIB", "sipUACfgTimerProv"),
        ("SIP-UA-MIB", "sipUACfgTimerAck"),
        ("SIP-UA-MIB", "sipUACfgTimerDisconnect"),
        ("SIP-UA-MIB", "sipUACfgTimerReRegister"),
        ("SIP-UA-MIB", "sipUACfgRetryInvite"),
        ("SIP-UA-MIB", "sipUACfgRetryBye"),
        ("SIP-UA-MIB", "sipUACfgRetryCancel"),
        ("SIP-UA-MIB", "sipUACfgRetryRegister"),
        ("SIP-UA-MIB", "sipUACfgRetryResponse"))
)
if mibBuilder.loadTexts:
    sipUAConfigGroup.setStatus("current")

sipUAStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 9998, 3, 4, 2, 2)
)
sipUAStatsGroup.setObjects(
      *(("SIP-UA-MIB", "sipStatsRetryInvites"),
        ("SIP-UA-MIB", "sipStatsRetryByes"),
        ("SIP-UA-MIB", "sipStatsRetryCancels"),
        ("SIP-UA-MIB", "sipStatsRetryRegisters"),
        ("SIP-UA-MIB", "sipStatsRetryResponses"))
)
if mibBuilder.loadTexts:
    sipUAStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

sipUACompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 9998, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    sipUACompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIP-UA-MIB",
    **{"sipUAMIB": sipUAMIB,
       "sipUACfg": sipUACfg,
       "sipUACfgTimer": sipUACfgTimer,
       "sipUACfgTimerTable": sipUACfgTimerTable,
       "sipUACfgTimerEntry": sipUACfgTimerEntry,
       "sipUACfgTimerTrying": sipUACfgTimerTrying,
       "sipUACfgTimerProv": sipUACfgTimerProv,
       "sipUACfgTimerAck": sipUACfgTimerAck,
       "sipUACfgTimerDisconnect": sipUACfgTimerDisconnect,
       "sipUACfgTimerReRegister": sipUACfgTimerReRegister,
       "sipUACfgRetry": sipUACfgRetry,
       "sipUACfgRetryTable": sipUACfgRetryTable,
       "sipUACfgRetryEntry": sipUACfgRetryEntry,
       "sipUACfgRetryInvite": sipUACfgRetryInvite,
       "sipUACfgRetryBye": sipUACfgRetryBye,
       "sipUACfgRetryCancel": sipUACfgRetryCancel,
       "sipUACfgRetryRegister": sipUACfgRetryRegister,
       "sipUACfgRetryResponse": sipUACfgRetryResponse,
       "sipUAStats": sipUAStats,
       "sipUAStatsRetry": sipUAStatsRetry,
       "sipUAStatsRetryTable": sipUAStatsRetryTable,
       "sipUAStatsRetryEntry": sipUAStatsRetryEntry,
       "sipStatsRetryInvites": sipStatsRetryInvites,
       "sipStatsRetryByes": sipStatsRetryByes,
       "sipStatsRetryCancels": sipStatsRetryCancels,
       "sipStatsRetryRegisters": sipStatsRetryRegisters,
       "sipStatsRetryResponses": sipStatsRetryResponses,
       "sipUAMIBNotif": sipUAMIBNotif,
       "sipUAMIBConformance": sipUAMIBConformance,
       "sipUAMIBCompliances": sipUAMIBCompliances,
       "sipUACompliance": sipUACompliance,
       "sipUAMIBGroups": sipUAMIBGroups,
       "sipUAConfigGroup": sipUAConfigGroup,
       "sipUAStatsGroup": sipUAStatsGroup}
)
