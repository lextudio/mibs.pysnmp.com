# SNMP MIB module (ZYXEL-PORT-AUTHENTICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-PORT-AUTHENTICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:31 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelPortAuthentication = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 62)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelPortAuthenticationSetup_ObjectIdentity = ObjectIdentity
zyxelPortAuthenticationSetup = _ZyxelPortAuthenticationSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 62, 1)
)
_ZyPortAuthenticationState_Type = EnabledStatus
_ZyPortAuthenticationState_Object = MibScalar
zyPortAuthenticationState = _ZyPortAuthenticationState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 62, 1, 1),
    _ZyPortAuthenticationState_Type()
)
zyPortAuthenticationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPortAuthenticationState.setStatus("current")
_ZyxelPortAuthenticationPortTable_Object = MibTable
zyxelPortAuthenticationPortTable = _ZyxelPortAuthenticationPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 62, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelPortAuthenticationPortTable.setStatus("current")
_ZyxelPortAuthenticationPortEntry_Object = MibTableRow
zyxelPortAuthenticationPortEntry = _ZyxelPortAuthenticationPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 62, 1, 2, 1)
)
zyxelPortAuthenticationPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelPortAuthenticationPortEntry.setStatus("current")
_ZyPortAuthenticationPortState_Type = EnabledStatus
_ZyPortAuthenticationPortState_Object = MibTableColumn
zyPortAuthenticationPortState = _ZyPortAuthenticationPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 62, 1, 2, 1, 1),
    _ZyPortAuthenticationPortState_Type()
)
zyPortAuthenticationPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPortAuthenticationPortState.setStatus("current")
_ZyPortReAuthenticationPortState_Type = EnabledStatus
_ZyPortReAuthenticationPortState_Object = MibTableColumn
zyPortReAuthenticationPortState = _ZyPortReAuthenticationPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 62, 1, 2, 1, 2),
    _ZyPortReAuthenticationPortState_Type()
)
zyPortReAuthenticationPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPortReAuthenticationPortState.setStatus("current")
_ZyPortReAuthenticationPortTimer_Type = Integer32
_ZyPortReAuthenticationPortTimer_Object = MibTableColumn
zyPortReAuthenticationPortTimer = _ZyPortReAuthenticationPortTimer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 62, 1, 2, 1, 3),
    _ZyPortReAuthenticationPortTimer_Type()
)
zyPortReAuthenticationPortTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPortReAuthenticationPortTimer.setStatus("current")
_ZyPortAuthenticationPortQuietPeriod_Type = Integer32
_ZyPortAuthenticationPortQuietPeriod_Object = MibTableColumn
zyPortAuthenticationPortQuietPeriod = _ZyPortAuthenticationPortQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 62, 1, 2, 1, 4),
    _ZyPortAuthenticationPortQuietPeriod_Type()
)
zyPortAuthenticationPortQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPortAuthenticationPortQuietPeriod.setStatus("current")
_ZyPortAuthenticationPortTxPeriod_Type = Integer32
_ZyPortAuthenticationPortTxPeriod_Object = MibTableColumn
zyPortAuthenticationPortTxPeriod = _ZyPortAuthenticationPortTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 62, 1, 2, 1, 5),
    _ZyPortAuthenticationPortTxPeriod_Type()
)
zyPortAuthenticationPortTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPortAuthenticationPortTxPeriod.setStatus("current")
_ZyPortAuthenticationPortSupplicantTimeout_Type = Integer32
_ZyPortAuthenticationPortSupplicantTimeout_Object = MibTableColumn
zyPortAuthenticationPortSupplicantTimeout = _ZyPortAuthenticationPortSupplicantTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 62, 1, 2, 1, 6),
    _ZyPortAuthenticationPortSupplicantTimeout_Type()
)
zyPortAuthenticationPortSupplicantTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPortAuthenticationPortSupplicantTimeout.setStatus("current")
_ZyPortAuthenticationPortMaxRequest_Type = Integer32
_ZyPortAuthenticationPortMaxRequest_Object = MibTableColumn
zyPortAuthenticationPortMaxRequest = _ZyPortAuthenticationPortMaxRequest_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 62, 1, 2, 1, 7),
    _ZyPortAuthenticationPortMaxRequest_Type()
)
zyPortAuthenticationPortMaxRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPortAuthenticationPortMaxRequest.setStatus("current")
_ZyPortAuthenticationPortGuestVlanState_Type = EnabledStatus
_ZyPortAuthenticationPortGuestVlanState_Object = MibTableColumn
zyPortAuthenticationPortGuestVlanState = _ZyPortAuthenticationPortGuestVlanState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 62, 1, 2, 1, 8),
    _ZyPortAuthenticationPortGuestVlanState_Type()
)
zyPortAuthenticationPortGuestVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPortAuthenticationPortGuestVlanState.setStatus("current")
_ZyPortAuthenticationPortGuestVlan_Type = Integer32
_ZyPortAuthenticationPortGuestVlan_Object = MibTableColumn
zyPortAuthenticationPortGuestVlan = _ZyPortAuthenticationPortGuestVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 62, 1, 2, 1, 9),
    _ZyPortAuthenticationPortGuestVlan_Type()
)
zyPortAuthenticationPortGuestVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPortAuthenticationPortGuestVlan.setStatus("current")


class _ZyPortAuthenticationPortGuestVlanHostMode_Type(Integer32):
    """Custom type zyPortAuthenticationPortGuestVlanHostMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("multiHost", 0),
          ("multiSecure", 1))
    )


_ZyPortAuthenticationPortGuestVlanHostMode_Type.__name__ = "Integer32"
_ZyPortAuthenticationPortGuestVlanHostMode_Object = MibTableColumn
zyPortAuthenticationPortGuestVlanHostMode = _ZyPortAuthenticationPortGuestVlanHostMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 62, 1, 2, 1, 10),
    _ZyPortAuthenticationPortGuestVlanHostMode_Type()
)
zyPortAuthenticationPortGuestVlanHostMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPortAuthenticationPortGuestVlanHostMode.setStatus("current")
_ZyPortAuthenticationPortGuestVlanHostModeMultiSecureNumber_Type = Integer32
_ZyPortAuthenticationPortGuestVlanHostModeMultiSecureNumber_Object = MibTableColumn
zyPortAuthenticationPortGuestVlanHostModeMultiSecureNumber = _ZyPortAuthenticationPortGuestVlanHostModeMultiSecureNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 62, 1, 2, 1, 11),
    _ZyPortAuthenticationPortGuestVlanHostModeMultiSecureNumber_Type()
)
zyPortAuthenticationPortGuestVlanHostModeMultiSecureNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPortAuthenticationPortGuestVlanHostModeMultiSecureNumber.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-PORT-AUTHENTICATION-MIB",
    **{"zyxelPortAuthentication": zyxelPortAuthentication,
       "zyxelPortAuthenticationSetup": zyxelPortAuthenticationSetup,
       "zyPortAuthenticationState": zyPortAuthenticationState,
       "zyxelPortAuthenticationPortTable": zyxelPortAuthenticationPortTable,
       "zyxelPortAuthenticationPortEntry": zyxelPortAuthenticationPortEntry,
       "zyPortAuthenticationPortState": zyPortAuthenticationPortState,
       "zyPortReAuthenticationPortState": zyPortReAuthenticationPortState,
       "zyPortReAuthenticationPortTimer": zyPortReAuthenticationPortTimer,
       "zyPortAuthenticationPortQuietPeriod": zyPortAuthenticationPortQuietPeriod,
       "zyPortAuthenticationPortTxPeriod": zyPortAuthenticationPortTxPeriod,
       "zyPortAuthenticationPortSupplicantTimeout": zyPortAuthenticationPortSupplicantTimeout,
       "zyPortAuthenticationPortMaxRequest": zyPortAuthenticationPortMaxRequest,
       "zyPortAuthenticationPortGuestVlanState": zyPortAuthenticationPortGuestVlanState,
       "zyPortAuthenticationPortGuestVlan": zyPortAuthenticationPortGuestVlan,
       "zyPortAuthenticationPortGuestVlanHostMode": zyPortAuthenticationPortGuestVlanHostMode,
       "zyPortAuthenticationPortGuestVlanHostModeMultiSecureNumber": zyPortAuthenticationPortGuestVlanHostModeMultiSecureNumber}
)
