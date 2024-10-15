# SNMP MIB module (PANDATEL-AGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PANDATEL-AGENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:39 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Pandatel_ObjectIdentity = ObjectIdentity
pandatel = _Pandatel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760)
)
_Mibs_ObjectIdentity = ObjectIdentity
mibs = _Mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1)
)
_Agent_ObjectIdentity = ObjectIdentity
agent = _Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 10000)
)
_AgentGroup_ObjectIdentity = ObjectIdentity
agentGroup = _AgentGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 10000, 1)
)
_AgentNetAddress_Type = IpAddress
_AgentNetAddress_Object = MibScalar
agentNetAddress = _AgentNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 10000, 1, 1),
    _AgentNetAddress_Type()
)
agentNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetAddress.setStatus("mandatory")
_AgentSubnetMask_Type = IpAddress
_AgentSubnetMask_Object = MibScalar
agentSubnetMask = _AgentSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 10000, 1, 2),
    _AgentSubnetMask_Type()
)
agentSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSubnetMask.setStatus("mandatory")
_AgentPhysAddress_Type = PhysAddress
_AgentPhysAddress_Object = MibScalar
agentPhysAddress = _AgentPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 10000, 1, 3),
    _AgentPhysAddress_Type()
)
agentPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPhysAddress.setStatus("mandatory")


class _AgentMgmtAccessMode_Type(Integer32):
    """Custom type agentMgmtAccessMode based on Integer32"""
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
        *(("inband", 2),
          ("other", 1),
          ("outband", 3),
          ("proxy", 4))
    )


_AgentMgmtAccessMode_Type.__name__ = "Integer32"
_AgentMgmtAccessMode_Object = MibScalar
agentMgmtAccessMode = _AgentMgmtAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 10000, 1, 4),
    _AgentMgmtAccessMode_Type()
)
agentMgmtAccessMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMgmtAccessMode.setStatus("mandatory")
_AgentHardwareRevision_Type = DisplayString
_AgentHardwareRevision_Object = MibScalar
agentHardwareRevision = _AgentHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 10000, 1, 5),
    _AgentHardwareRevision_Type()
)
agentHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentHardwareRevision.setStatus("mandatory")
_AgentSoftwareRevision_Type = DisplayString
_AgentSoftwareRevision_Object = MibScalar
agentSoftwareRevision = _AgentSoftwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 10000, 1, 6),
    _AgentSoftwareRevision_Type()
)
agentSoftwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSoftwareRevision.setStatus("mandatory")
_AgentTrapReceiverTable_Object = MibTable
agentTrapReceiverTable = _AgentTrapReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 10000, 1, 7)
)
if mibBuilder.loadTexts:
    agentTrapReceiverTable.setStatus("mandatory")
_AgTrapReceiverTableEntry_Object = MibTableRow
agTrapReceiverTableEntry = _AgTrapReceiverTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 10000, 1, 7, 1)
)
agTrapReceiverTableEntry.setIndexNames(
    (0, "PANDATEL-AGENT-MIB", "agTrapReceiverNetAddress"),
)
if mibBuilder.loadTexts:
    agTrapReceiverTableEntry.setStatus("mandatory")
_AgTrapReceiverNetAddress_Type = IpAddress
_AgTrapReceiverNetAddress_Object = MibTableColumn
agTrapReceiverNetAddress = _AgTrapReceiverNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 10000, 1, 7, 1, 1),
    _AgTrapReceiverNetAddress_Type()
)
agTrapReceiverNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agTrapReceiverNetAddress.setStatus("mandatory")
_AgTrapReceiverTrapCommunity_Type = DisplayString
_AgTrapReceiverTrapCommunity_Object = MibTableColumn
agTrapReceiverTrapCommunity = _AgTrapReceiverTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 10000, 1, 7, 1, 2),
    _AgTrapReceiverTrapCommunity_Type()
)
agTrapReceiverTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agTrapReceiverTrapCommunity.setStatus("mandatory")


class _AgTrapReceiverType_Type(Integer32):
    """Custom type agTrapReceiverType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AgTrapReceiverType_Type.__name__ = "Integer32"
_AgTrapReceiverType_Object = MibTableColumn
agTrapReceiverType = _AgTrapReceiverType_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 10000, 1, 7, 1, 3),
    _AgTrapReceiverType_Type()
)
agTrapReceiverType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agTrapReceiverType.setStatus("mandatory")
_AgentSecurityTable_Object = MibTable
agentSecurityTable = _AgentSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 10000, 1, 8)
)
if mibBuilder.loadTexts:
    agentSecurityTable.setStatus("mandatory")
_AgSecTableEntry_Object = MibTableRow
agSecTableEntry = _AgSecTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 10000, 1, 8, 1)
)
agSecTableEntry.setIndexNames(
    (0, "PANDATEL-AGENT-MIB", "agSecSecurityLevel"),
)
if mibBuilder.loadTexts:
    agSecTableEntry.setStatus("mandatory")


class _AgSecSecurityLevel_Type(Integer32):
    """Custom type agSecSecurityLevel based on Integer32"""
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
        *(("administrator-access", 4),
          ("high-security-access", 5),
          ("read-all-mgmt-objs", 2),
          ("read-only-sysgroup", 1),
          ("standard-mgmt-access", 3))
    )


_AgSecSecurityLevel_Type.__name__ = "Integer32"
_AgSecSecurityLevel_Object = MibTableColumn
agSecSecurityLevel = _AgSecSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 10000, 1, 8, 1, 1),
    _AgSecSecurityLevel_Type()
)
agSecSecurityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSecSecurityLevel.setStatus("mandatory")
_AgSecCommunity_Type = DisplayString
_AgSecCommunity_Object = MibTableColumn
agSecCommunity = _AgSecCommunity_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 10000, 1, 8, 1, 2),
    _AgSecCommunity_Type()
)
agSecCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agSecCommunity.setStatus("mandatory")
_AgentMgmtSecurity_ObjectIdentity = ObjectIdentity
agentMgmtSecurity = _AgentMgmtSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 10000, 1, 9)
)


class _AgentAuthRestrictMode_Type(Integer32):
    """Custom type agentAuthRestrictMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notRestricted", 2),
          ("other", 1),
          ("restricted", 3))
    )


_AgentAuthRestrictMode_Type.__name__ = "Integer32"
_AgentAuthRestrictMode_Object = MibScalar
agentAuthRestrictMode = _AgentAuthRestrictMode_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 10000, 1, 9, 1),
    _AgentAuthRestrictMode_Type()
)
agentAuthRestrictMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthRestrictMode.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PANDATEL-AGENT-MIB",
    **{"pandatel": pandatel,
       "mibs": mibs,
       "agent": agent,
       "agentGroup": agentGroup,
       "agentNetAddress": agentNetAddress,
       "agentSubnetMask": agentSubnetMask,
       "agentPhysAddress": agentPhysAddress,
       "agentMgmtAccessMode": agentMgmtAccessMode,
       "agentHardwareRevision": agentHardwareRevision,
       "agentSoftwareRevision": agentSoftwareRevision,
       "agentTrapReceiverTable": agentTrapReceiverTable,
       "agTrapReceiverTableEntry": agTrapReceiverTableEntry,
       "agTrapReceiverNetAddress": agTrapReceiverNetAddress,
       "agTrapReceiverTrapCommunity": agTrapReceiverTrapCommunity,
       "agTrapReceiverType": agTrapReceiverType,
       "agentSecurityTable": agentSecurityTable,
       "agSecTableEntry": agSecTableEntry,
       "agSecSecurityLevel": agSecSecurityLevel,
       "agSecCommunity": agSecCommunity,
       "agentMgmtSecurity": agentMgmtSecurity,
       "agentAuthRestrictMode": agentAuthRestrictMode}
)
