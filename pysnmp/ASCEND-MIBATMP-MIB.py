# SNMP MIB module (ASCEND-MIBATMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBATMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:09 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibatmpProfile_ObjectIdentity = ObjectIdentity
mibatmpProfile = _MibatmpProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 42)
)
_MibatmpProfileTable_Object = MibTable
mibatmpProfileTable = _MibatmpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 42, 1)
)
if mibBuilder.loadTexts:
    mibatmpProfileTable.setStatus("mandatory")
_MibatmpProfileEntry_Object = MibTableRow
mibatmpProfileEntry = _MibatmpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 42, 1, 1)
)
mibatmpProfileEntry.setIndexNames(
    (0, "ASCEND-MIBATMP-MIB", "atmpProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibatmpProfileEntry.setStatus("mandatory")
_AtmpProfile_Index_o_Type = Integer32
_AtmpProfile_Index_o_Object = MibScalar
atmpProfile_Index_o = _AtmpProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 42, 1, 1, 1),
    _AtmpProfile_Index_o_Type()
)
atmpProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpProfile_Index_o.setStatus("mandatory")


class _AtmpProfile_AgentMode_Type(Integer32):
    """Custom type atmpProfile_AgentMode based on Integer32"""
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
        *(("foreignAgent", 3),
          ("homeAgent", 2),
          ("homeAndForeignAgent", 4),
          ("tunnelDisabled", 1))
    )


_AtmpProfile_AgentMode_Type.__name__ = "Integer32"
_AtmpProfile_AgentMode_Object = MibScalar
atmpProfile_AgentMode = _AtmpProfile_AgentMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 42, 1, 1, 2),
    _AtmpProfile_AgentMode_Type()
)
atmpProfile_AgentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmpProfile_AgentMode.setStatus("mandatory")


class _AtmpProfile_AgentType_Type(Integer32):
    """Custom type atmpProfile_AgentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gatewayHomeAgent", 2),
          ("routerHomeAgent", 1))
    )


_AtmpProfile_AgentType_Type.__name__ = "Integer32"
_AtmpProfile_AgentType_Object = MibScalar
atmpProfile_AgentType = _AtmpProfile_AgentType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 42, 1, 1, 3),
    _AtmpProfile_AgentType_Type()
)
atmpProfile_AgentType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmpProfile_AgentType.setStatus("mandatory")
_AtmpProfile_UdpPort_Type = Integer32
_AtmpProfile_UdpPort_Object = MibScalar
atmpProfile_UdpPort = _AtmpProfile_UdpPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 42, 1, 1, 4),
    _AtmpProfile_UdpPort_Type()
)
atmpProfile_UdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmpProfile_UdpPort.setStatus("mandatory")
_AtmpProfile_HomeAgentPassword_Type = DisplayString
_AtmpProfile_HomeAgentPassword_Object = MibScalar
atmpProfile_HomeAgentPassword = _AtmpProfile_HomeAgentPassword_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 42, 1, 1, 5),
    _AtmpProfile_HomeAgentPassword_Type()
)
atmpProfile_HomeAgentPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmpProfile_HomeAgentPassword.setStatus("mandatory")


class _AtmpProfile_AtmpSapReply_Type(Integer32):
    """Custom type atmpProfile_AtmpSapReply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AtmpProfile_AtmpSapReply_Type.__name__ = "Integer32"
_AtmpProfile_AtmpSapReply_Object = MibScalar
atmpProfile_AtmpSapReply = _AtmpProfile_AtmpSapReply_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 42, 1, 1, 6),
    _AtmpProfile_AtmpSapReply_Type()
)
atmpProfile_AtmpSapReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmpProfile_AtmpSapReply.setStatus("mandatory")
_AtmpProfile_RetryTimeout_Type = Integer32
_AtmpProfile_RetryTimeout_Object = MibScalar
atmpProfile_RetryTimeout = _AtmpProfile_RetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 42, 1, 1, 7),
    _AtmpProfile_RetryTimeout_Type()
)
atmpProfile_RetryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmpProfile_RetryTimeout.setStatus("mandatory")
_AtmpProfile_RetryLimit_Type = Integer32
_AtmpProfile_RetryLimit_Object = MibScalar
atmpProfile_RetryLimit = _AtmpProfile_RetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 42, 1, 1, 8),
    _AtmpProfile_RetryLimit_Type()
)
atmpProfile_RetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmpProfile_RetryLimit.setStatus("mandatory")
_AtmpProfile_IdleTimer_Type = Integer32
_AtmpProfile_IdleTimer_Object = MibScalar
atmpProfile_IdleTimer = _AtmpProfile_IdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 42, 1, 1, 9),
    _AtmpProfile_IdleTimer_Type()
)
atmpProfile_IdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmpProfile_IdleTimer.setStatus("mandatory")
_AtmpProfile_MtuLimit_Type = Integer32
_AtmpProfile_MtuLimit_Object = MibScalar
atmpProfile_MtuLimit = _AtmpProfile_MtuLimit_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 42, 1, 1, 10),
    _AtmpProfile_MtuLimit_Type()
)
atmpProfile_MtuLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmpProfile_MtuLimit.setStatus("mandatory")


class _AtmpProfile_ForceFragmentation_Type(Integer32):
    """Custom type atmpProfile_ForceFragmentation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AtmpProfile_ForceFragmentation_Type.__name__ = "Integer32"
_AtmpProfile_ForceFragmentation_Object = MibScalar
atmpProfile_ForceFragmentation = _AtmpProfile_ForceFragmentation_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 42, 1, 1, 11),
    _AtmpProfile_ForceFragmentation_Type()
)
atmpProfile_ForceFragmentation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmpProfile_ForceFragmentation.setStatus("mandatory")


class _AtmpProfile_AtmpSnmpTrap_Type(Integer32):
    """Custom type atmpProfile_AtmpSnmpTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AtmpProfile_AtmpSnmpTrap_Type.__name__ = "Integer32"
_AtmpProfile_AtmpSnmpTrap_Object = MibScalar
atmpProfile_AtmpSnmpTrap = _AtmpProfile_AtmpSnmpTrap_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 42, 1, 1, 12),
    _AtmpProfile_AtmpSnmpTrap_Type()
)
atmpProfile_AtmpSnmpTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmpProfile_AtmpSnmpTrap.setStatus("mandatory")


class _AtmpProfile_Action_o_Type(Integer32):
    """Custom type atmpProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_AtmpProfile_Action_o_Type.__name__ = "Integer32"
_AtmpProfile_Action_o_Object = MibScalar
atmpProfile_Action_o = _AtmpProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 42, 1, 1, 13),
    _AtmpProfile_Action_o_Type()
)
atmpProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmpProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBATMP-MIB",
    **{"DisplayString": DisplayString,
       "mibatmpProfile": mibatmpProfile,
       "mibatmpProfileTable": mibatmpProfileTable,
       "mibatmpProfileEntry": mibatmpProfileEntry,
       "atmpProfile-Index-o": atmpProfile_Index_o,
       "atmpProfile-AgentMode": atmpProfile_AgentMode,
       "atmpProfile-AgentType": atmpProfile_AgentType,
       "atmpProfile-UdpPort": atmpProfile_UdpPort,
       "atmpProfile-HomeAgentPassword": atmpProfile_HomeAgentPassword,
       "atmpProfile-AtmpSapReply": atmpProfile_AtmpSapReply,
       "atmpProfile-RetryTimeout": atmpProfile_RetryTimeout,
       "atmpProfile-RetryLimit": atmpProfile_RetryLimit,
       "atmpProfile-IdleTimer": atmpProfile_IdleTimer,
       "atmpProfile-MtuLimit": atmpProfile_MtuLimit,
       "atmpProfile-ForceFragmentation": atmpProfile_ForceFragmentation,
       "atmpProfile-AtmpSnmpTrap": atmpProfile_AtmpSnmpTrap,
       "atmpProfile-Action-o": atmpProfile_Action_o}
)
