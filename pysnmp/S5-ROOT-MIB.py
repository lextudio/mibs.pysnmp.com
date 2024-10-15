# SNMP MIB module (S5-ROOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/S5-ROOT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:05 2024
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

(series5000,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "series5000")


# MODULE-IDENTITY

s5RootMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 0)
)
s5RootMib.setRevisions(
        ("2004-07-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_S5reg_ObjectIdentity = ObjectIdentity
s5reg = _S5reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1)
)
_S5Traps_ObjectIdentity = ObjectIdentity
s5Traps = _S5Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2)
)
_S5EthTrap_ObjectIdentity = ObjectIdentity
s5EthTrap = _S5EthTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1)
)
_S5TokTrap_ObjectIdentity = ObjectIdentity
s5TokTrap = _S5TokTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 2)
)
_S5FddTrap_ObjectIdentity = ObjectIdentity
s5FddTrap = _S5FddTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 3)
)
_S5ChaTrap_ObjectIdentity = ObjectIdentity
s5ChaTrap = _S5ChaTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 4)
)
_S5ComTrap_ObjectIdentity = ObjectIdentity
s5ComTrap = _S5ComTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 5)
)
_S5EcellTrap_ObjectIdentity = ObjectIdentity
s5EcellTrap = _S5EcellTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 6)
)
_AtmTraps_ObjectIdentity = ObjectIdentity
atmTraps = _AtmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 7)
)
_RemoteLoginTrap_ObjectIdentity = ObjectIdentity
remoteLoginTrap = _RemoteLoginTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 8)
)
_StpChangeTrap_ObjectIdentity = ObjectIdentity
stpChangeTrap = _StpChangeTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 9)
)
_S5Chassis_ObjectIdentity = ObjectIdentity
s5Chassis = _S5Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 3)
)
_S5Agent_ObjectIdentity = ObjectIdentity
s5Agent = _S5Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4)
)
_S5Com_ObjectIdentity = ObjectIdentity
s5Com = _S5Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 5)
)
_S5Eth_ObjectIdentity = ObjectIdentity
s5Eth = _S5Eth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6)
)
_S5Tok_ObjectIdentity = ObjectIdentity
s5Tok = _S5Tok_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7)
)
_S5Fddi_ObjectIdentity = ObjectIdentity
s5Fddi = _S5Fddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 8)
)
_S5EnTop_ObjectIdentity = ObjectIdentity
s5EnTop = _S5EnTop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 9)
)
_S5TrTop_ObjectIdentity = ObjectIdentity
s5TrTop = _S5TrTop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 10)
)
_S5FdTop_ObjectIdentity = ObjectIdentity
s5FdTop = _S5FdTop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 11)
)
_S5EnMsTop_ObjectIdentity = ObjectIdentity
s5EnMsTop = _S5EnMsTop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13)
)
_S5AtmTop_ObjectIdentity = ObjectIdentity
s5AtmTop = _S5AtmTop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14)
)
_S5IfExt_ObjectIdentity = ObjectIdentity
s5IfExt = _S5IfExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 15)
)
_BnLogMsg_ObjectIdentity = ObjectIdentity
bnLogMsg = _BnLogMsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 16)
)
_S5Tcs_ObjectIdentity = ObjectIdentity
s5Tcs = _S5Tcs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 17)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "S5-ROOT-MIB",
    **{"s5RootMib": s5RootMib,
       "s5reg": s5reg,
       "s5Traps": s5Traps,
       "s5EthTrap": s5EthTrap,
       "s5TokTrap": s5TokTrap,
       "s5FddTrap": s5FddTrap,
       "s5ChaTrap": s5ChaTrap,
       "s5ComTrap": s5ComTrap,
       "s5EcellTrap": s5EcellTrap,
       "atmTraps": atmTraps,
       "remoteLoginTrap": remoteLoginTrap,
       "stpChangeTrap": stpChangeTrap,
       "s5Chassis": s5Chassis,
       "s5Agent": s5Agent,
       "s5Com": s5Com,
       "s5Eth": s5Eth,
       "s5Tok": s5Tok,
       "s5Fddi": s5Fddi,
       "s5EnTop": s5EnTop,
       "s5TrTop": s5TrTop,
       "s5FdTop": s5FdTop,
       "s5EnMsTop": s5EnMsTop,
       "s5AtmTop": s5AtmTop,
       "s5IfExt": s5IfExt,
       "bnLogMsg": bnLogMsg,
       "s5Tcs": s5Tcs}
)
