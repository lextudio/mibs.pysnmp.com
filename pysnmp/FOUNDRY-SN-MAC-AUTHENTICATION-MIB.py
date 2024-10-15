# SNMP MIB module (FOUNDRY-SN-MAC-AUTHENTICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FOUNDRY-SN-MAC-AUTHENTICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:57 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

snMacAuth = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28)
)
snMacAuth.setRevisions(
        ("2010-06-02 00:00",
         "2007-06-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnMacAuthGlobal_ObjectIdentity = ObjectIdentity
snMacAuthGlobal = _SnMacAuthGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 1)
)


class _SnMacAuthClearGlobalCmd_Type(Integer32):
    """Custom type snMacAuthClearGlobalCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("valid", 0))
    )


_SnMacAuthClearGlobalCmd_Type.__name__ = "Integer32"
_SnMacAuthClearGlobalCmd_Object = MibScalar
snMacAuthClearGlobalCmd = _SnMacAuthClearGlobalCmd_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 1, 1),
    _SnMacAuthClearGlobalCmd_Type()
)
snMacAuthClearGlobalCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMacAuthClearGlobalCmd.setStatus("current")


class _SnMacAuthGlobalConfigState_Type(Integer32):
    """Custom type snMacAuthGlobalConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnMacAuthGlobalConfigState_Type.__name__ = "Integer32"
_SnMacAuthGlobalConfigState_Object = MibScalar
snMacAuthGlobalConfigState = _SnMacAuthGlobalConfigState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 1, 2),
    _SnMacAuthGlobalConfigState_Type()
)
snMacAuthGlobalConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMacAuthGlobalConfigState.setStatus("current")
_SnMacAuthClearIfCmdTable_Object = MibTable
snMacAuthClearIfCmdTable = _SnMacAuthClearIfCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 2)
)
if mibBuilder.loadTexts:
    snMacAuthClearIfCmdTable.setStatus("current")
_SnMacAuthClearIfCmdEntry_Object = MibTableRow
snMacAuthClearIfCmdEntry = _SnMacAuthClearIfCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 2, 1)
)
snMacAuthClearIfCmdEntry.setIndexNames(
    (0, "FOUNDRY-SN-MAC-AUTHENTICATION-MIB", "snMacAuthClearIfCmdIfIndex"),
)
if mibBuilder.loadTexts:
    snMacAuthClearIfCmdEntry.setStatus("current")
_SnMacAuthClearIfCmdIfIndex_Type = InterfaceIndex
_SnMacAuthClearIfCmdIfIndex_Object = MibTableColumn
snMacAuthClearIfCmdIfIndex = _SnMacAuthClearIfCmdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 2, 1, 1),
    _SnMacAuthClearIfCmdIfIndex_Type()
)
snMacAuthClearIfCmdIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snMacAuthClearIfCmdIfIndex.setStatus("current")


class _SnMacAuthClearIfCmdAction_Type(Integer32):
    """Custom type snMacAuthClearIfCmdAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("valid", 0))
    )


_SnMacAuthClearIfCmdAction_Type.__name__ = "Integer32"
_SnMacAuthClearIfCmdAction_Object = MibTableColumn
snMacAuthClearIfCmdAction = _SnMacAuthClearIfCmdAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 2, 1, 2),
    _SnMacAuthClearIfCmdAction_Type()
)
snMacAuthClearIfCmdAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMacAuthClearIfCmdAction.setStatus("current")
_SnMacAuthTable_Object = MibTable
snMacAuthTable = _SnMacAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3)
)
if mibBuilder.loadTexts:
    snMacAuthTable.setStatus("current")
_SnMacAuthEntry_Object = MibTableRow
snMacAuthEntry = _SnMacAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1)
)
snMacAuthEntry.setIndexNames(
    (0, "FOUNDRY-SN-MAC-AUTHENTICATION-MIB", "snMacAuthIfIndex"),
    (0, "FOUNDRY-SN-MAC-AUTHENTICATION-MIB", "snMacAuthVlanId"),
    (0, "FOUNDRY-SN-MAC-AUTHENTICATION-MIB", "snMacAuthMac"),
)
if mibBuilder.loadTexts:
    snMacAuthEntry.setStatus("current")
_SnMacAuthIfIndex_Type = InterfaceIndex
_SnMacAuthIfIndex_Object = MibTableColumn
snMacAuthIfIndex = _SnMacAuthIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1, 1),
    _SnMacAuthIfIndex_Type()
)
snMacAuthIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snMacAuthIfIndex.setStatus("current")
_SnMacAuthVlanId_Type = Integer32
_SnMacAuthVlanId_Object = MibTableColumn
snMacAuthVlanId = _SnMacAuthVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1, 2),
    _SnMacAuthVlanId_Type()
)
snMacAuthVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snMacAuthVlanId.setStatus("current")
_SnMacAuthMac_Type = MacAddress
_SnMacAuthMac_Object = MibTableColumn
snMacAuthMac = _SnMacAuthMac_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1, 3),
    _SnMacAuthMac_Type()
)
snMacAuthMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snMacAuthMac.setStatus("current")


class _SnMacAuthState_Type(Integer32):
    """Custom type snMacAuthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authenticate", 1),
          ("unauthenticate", 2))
    )


_SnMacAuthState_Type.__name__ = "Integer32"
_SnMacAuthState_Object = MibTableColumn
snMacAuthState = _SnMacAuthState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1, 4),
    _SnMacAuthState_Type()
)
snMacAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snMacAuthState.setStatus("current")
_SnMacAuthTimeStamp_Type = TimeStamp
_SnMacAuthTimeStamp_Object = MibTableColumn
snMacAuthTimeStamp = _SnMacAuthTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1, 5),
    _SnMacAuthTimeStamp_Type()
)
snMacAuthTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snMacAuthTimeStamp.setStatus("current")
_SnMacAuthAge_Type = Integer32
_SnMacAuthAge_Object = MibTableColumn
snMacAuthAge = _SnMacAuthAge_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1, 6),
    _SnMacAuthAge_Type()
)
snMacAuthAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snMacAuthAge.setStatus("current")


class _SnMacAuthDot1x_Type(Integer32):
    """Custom type snMacAuthDot1x based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnMacAuthDot1x_Type.__name__ = "Integer32"
_SnMacAuthDot1x_Object = MibTableColumn
snMacAuthDot1x = _SnMacAuthDot1x_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1, 7),
    _SnMacAuthDot1x_Type()
)
snMacAuthDot1x.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snMacAuthDot1x.setStatus("current")
_SnMacAuthClearMacSessionTable_Object = MibTable
snMacAuthClearMacSessionTable = _SnMacAuthClearMacSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 4)
)
if mibBuilder.loadTexts:
    snMacAuthClearMacSessionTable.setStatus("current")
_SnMacAuthClearMacSessionEntry_Object = MibTableRow
snMacAuthClearMacSessionEntry = _SnMacAuthClearMacSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 4, 1)
)
snMacAuthClearMacSessionEntry.setIndexNames(
    (0, "FOUNDRY-SN-MAC-AUTHENTICATION-MIB", "snMacAuthClearMacSessionIfIndex"),
    (0, "FOUNDRY-SN-MAC-AUTHENTICATION-MIB", "snMacAuthClearMacSessionMac"),
)
if mibBuilder.loadTexts:
    snMacAuthClearMacSessionEntry.setStatus("current")
_SnMacAuthClearMacSessionIfIndex_Type = InterfaceIndex
_SnMacAuthClearMacSessionIfIndex_Object = MibTableColumn
snMacAuthClearMacSessionIfIndex = _SnMacAuthClearMacSessionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 4, 1, 1),
    _SnMacAuthClearMacSessionIfIndex_Type()
)
snMacAuthClearMacSessionIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snMacAuthClearMacSessionIfIndex.setStatus("current")
_SnMacAuthClearMacSessionMac_Type = MacAddress
_SnMacAuthClearMacSessionMac_Object = MibTableColumn
snMacAuthClearMacSessionMac = _SnMacAuthClearMacSessionMac_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 4, 1, 2),
    _SnMacAuthClearMacSessionMac_Type()
)
snMacAuthClearMacSessionMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snMacAuthClearMacSessionMac.setStatus("current")


class _SnMacAuthClearMacSessionAction_Type(Integer32):
    """Custom type snMacAuthClearMacSessionAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("valid", 0))
    )


_SnMacAuthClearMacSessionAction_Type.__name__ = "Integer32"
_SnMacAuthClearMacSessionAction_Object = MibTableColumn
snMacAuthClearMacSessionAction = _SnMacAuthClearMacSessionAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 4, 1, 3),
    _SnMacAuthClearMacSessionAction_Type()
)
snMacAuthClearMacSessionAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMacAuthClearMacSessionAction.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-SN-MAC-AUTHENTICATION-MIB",
    **{"snMacAuth": snMacAuth,
       "snMacAuthGlobal": snMacAuthGlobal,
       "snMacAuthClearGlobalCmd": snMacAuthClearGlobalCmd,
       "snMacAuthGlobalConfigState": snMacAuthGlobalConfigState,
       "snMacAuthClearIfCmdTable": snMacAuthClearIfCmdTable,
       "snMacAuthClearIfCmdEntry": snMacAuthClearIfCmdEntry,
       "snMacAuthClearIfCmdIfIndex": snMacAuthClearIfCmdIfIndex,
       "snMacAuthClearIfCmdAction": snMacAuthClearIfCmdAction,
       "snMacAuthTable": snMacAuthTable,
       "snMacAuthEntry": snMacAuthEntry,
       "snMacAuthIfIndex": snMacAuthIfIndex,
       "snMacAuthVlanId": snMacAuthVlanId,
       "snMacAuthMac": snMacAuthMac,
       "snMacAuthState": snMacAuthState,
       "snMacAuthTimeStamp": snMacAuthTimeStamp,
       "snMacAuthAge": snMacAuthAge,
       "snMacAuthDot1x": snMacAuthDot1x,
       "snMacAuthClearMacSessionTable": snMacAuthClearMacSessionTable,
       "snMacAuthClearMacSessionEntry": snMacAuthClearMacSessionEntry,
       "snMacAuthClearMacSessionIfIndex": snMacAuthClearMacSessionIfIndex,
       "snMacAuthClearMacSessionMac": snMacAuthClearMacSessionMac,
       "snMacAuthClearMacSessionAction": snMacAuthClearMacSessionAction}
)
